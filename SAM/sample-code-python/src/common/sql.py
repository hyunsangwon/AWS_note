import psycopg2
from src.common.constants import MAIN_DB, MAIN_DB_USER, MAIN_DB_HOST, MAIN_DB_PORT, MAIN_DB_PASSWORD

def sql_select(query):
    ret = []
    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' port={} password='{}'".format(MAIN_DB, MAIN_DB_USER, MAIN_DB_HOST, MAIN_DB_PORT, MAIN_DB_PASSWORD))
        cur = conn.cursor()
        print(query)
        cur.execute(query)
        rows = cur.fetchall()
        
        for row in rows:
            tmp = dict()
            for i in range(len(row)):
                tmp[cur.description[i].name] = row[i]
            ret.append(tmp)
        
        conn.close()
    except Exception as e:
        print(e)
    
    return ret

def sql(query):
    try:
        conn = psycopg2.connect("dbname='{}' user='{}' host='{}' port={} password='{}'".format(MAIN_DB, MAIN_DB_USER, MAIN_DB_HOST, MAIN_DB_PORT, MAIN_DB_PASSWORD))
        cur = conn.cursor()
        print(query)
        cur.execute(query)
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)