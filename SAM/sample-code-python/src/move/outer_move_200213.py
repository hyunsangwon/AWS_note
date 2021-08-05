import os
import boto3
import haversine
from datetime import date, datetime
from boto3.dynamodb.conditions import Key
from pytz import timezone

from src.common.sql import sql, sql_select
from src.move.utils.utils import distance
from src.move.utils.lbs import reqeust_bluechip
from src.common.constants import *

def check_outer_move_event(data_map):
    is_outer_move_event = False
    inner_move = False
    outer_move = False
    fmt = "%Y-%m-%d %H:%M:%S"
    MAX_DATE = 30
    packet_id = data_map["packet_id"]
    
    if packet_id == "2" or packet_id == "3":
        query = "SELECT * from log1_event_outer_move_v3 WHERE warranty_srl={} and euid='{}' and finish_at is null"
        query = query.format(data_map["warranty_srl"], data_map["euid"])
        outer_move_state = sql_select(query)
        if len(outer_move_state) == 0:
            ## 장거리 이동 발생
            inner_move = False
            outer_move = True
            is_outer_move_event = True
            ## tb_unexpected 조회
            unexpected_cell_data_query = "SELECT created_at FROM tb_unexpected_cell WHERE warranty_srl={} AND cell_id='{}'"
            unexpected_cell_data_query = unexpected_cell_data_query.format(data_map["warranty_srl"], data_map["cell_id"])
            unexpected_cell_data = sql_select(unexpected_cell_data_query)
            ## unexpected cell에 데이터가 없다면 거리 비교
            if len(unexpected_cell_data) == 0 :
                inner_move = False
                outer_move = True
                is_outer_move_event = True
                ## 최초 단말기 설치된 위치 조회
                installed_gps_query = "SELECT installed_lat,installed_lng FROM tb_detector WHERE euid='{}'"
                installed_gps_query = installed_gps_query.format(data_map["euid"])
                tb_detector_data = sql_select(installed_gps_query)
                installed_lat = float(tb_detector_data[0]['installed_lat'])
                installed_lng = float(tb_detector_data[0]['installed_lng'])
                packet_lat = float(data_map["lat"])
                packet_lng = float(data_map["lng"])
                ## 단말기 부착 위치와 CELL 위치 비교
                dis =  haversine.haversine((packet_lat, packet_lng), (installed_lat, installed_lng))
                if dis >= 2.0:
                    inner_move = False
                    outer_move = True
                    is_outer_move_event = True
                else:
                    inner_move = True
                    outer_move = False
                    is_outer_move_event = False
            ## unexpected cell에 데이터가 있다면 날짜 비교
            if len(unexpected_cell_data) > 0 :
                inner_move = True
                outer_move = False
                is_outer_move_event = False
                created_at = unexpected_cell_data[0]['created_at']
                KST = datetime.now(timezone('Asia/Seoul'))
                today = KST.strftime(fmt) # 오늘 날짜
                created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                today = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
                diff = (today - created_at).days
                if diff >= MAX_DATE :
                    inner_move = False
                    outer_move = True
                    is_outer_move_event = True
                    unexpected_cell_data_delete_query = "DELETE FROM tb_unexpected_cell WHERE warranty_srl={} AND cell_id='{}'"
                    unexpected_cell_data_delete_query = unexpected_cell_data_delete_query.format(data_map["warranty_srl"], data_map["cell_id"])
                    sql(unexpected_cell_data_delete_query)
                else:
                    inner_move = True
                    outer_move = False
                    is_outer_move_event = False
                    unexpected_cell_data_update_query = "UPDATE tb_unexpected_cell SET created_at='{}' WHERE warranty_srl={} AND cell_id='{}'"
                    unexpected_cell_data_update_query = unexpected_cell_data_update_query.format(today, data_map["warranty_srl"], data_map["cell_id"])
                    sql(unexpected_cell_data_update_query)
        else:
            outer_move = True
            inner_move = False
    
    euid = data_map["euid"]
    received_at_utc0 = data_map["received_at_utc0"]
    log_srl = data_map["log_srl"]
    mag = data_map["mag"]
    bank_srl = data_map["bank_srl"]
    branch_srl = data_map["branch_srl"]
    company_srl = data_map["company_srl"]
    warranty_srl = data_map["warranty_srl"]

    query = "UPDATE log1_device_event SET inner_move={}, outer_move={} WHERE log_srl={}"
    query = query.format(inner_move, outer_move, log_srl)
    sql(query)
    
    if inner_move:
        query = "INSERT INTO log1_event_inner_move_lbs (euid, mag, created_at, bank_srl, branch_srl, company_srl, warranty_srl)"
        query += "VALUES ('{}', '{}', CAST('{}' as timestamp without time zone) + interval '9 hour', {}, {}, {}, {})"
        query = query.format(euid, mag, received_at_utc0,bank_srl, branch_srl, company_srl, warranty_srl)
        sql(query)
    
    data_map["is_outer_move_event"] = is_outer_move_event
    data_map["inner_move"] = inner_move
    data_map["outer_move"] = outer_move
    data_map["distance"] = d
    data_map["outer_move_event_check"] = os.path.basename(__file__)

    return data_map
