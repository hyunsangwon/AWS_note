import json
import os
import psycopg2

ACCESS_KEY=os.environ.get('ACCESS_KEY')
SECRET_KEY=os.environ.get('SECRET_KEY')
HOST=os.environ.get('HOST')
DATABASE=os.environ.get('DATABASE')
USER=os.environ.get('USER')
PASSWORD=os.environ.get('PASSWORD')


def get_car_info():
    db = psycopg2.connect(host=HOST, user=USER, password =PASSWORD, dbname=DATABASE)
    cur = db.cursor()
    try:
        select_query = "SELECT car_srl ,car_type, car_number FROM car_info"
        cur.execute(select_query)
        car_records = cur.fetchall() 
        for row in car_records:
            print("Id = ", row[0], )
            print("Car Model = ", row[1])
            print("Car Number  = ", row[2], "\n")

    except Exception as e:
        print('sql error ===> ',e)

def handler_function(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            msg = record['dynamodb']['NewImage']['Message']['S']
            print(msg)
            
    get_car_info()
    print('handler_function exit')