import math

# 위도,경도 좌표 두개 사이의 거리 리턴(m
def distance(lat1, lng1, lat2, lng2):
    lat1_rad = float(lat1) * math.pi / 180
    lng1_rad = float(lng1) * math.pi / 180
    lat2_rad = float(lat2) * math.pi / 180
    lng2_rad = float(lng2) * math.pi / 180
    
    dlat = lat1_rad - lat2_rad
    dlng = lng1_rad - lng2_rad
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlng / 2) * math.sin(dlng / 2)
    d = int(2 * 6371 * math.asin(math.sqrt(a)) * 1000)
    
    return d
