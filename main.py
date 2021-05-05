from home.models import Customer as c
import requests
from requests_futures import sessions
import json
from datetime import datetime, timedelta

def check(params):
    session = sessions.FuturesSession(max_workers=3)
    futures = [session.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin", params=p) for p in  params]
    for f in futures:
        f.result()
        
    session.close()
    return futures

pins = c.objects().values_list('pin').distinct()

params=[]
date = datetime.today() + timedelta(1)

for pin in pins:
    params.append({'pincode': str(pin), 'date': str(date.strftime("%d-%m-%Y"))})

result.append(check(params))

print(result)









'''import psycopg2
from psycopg2 import Error
import pandas.io.sql as psql
import pandas as pd

try:
    conn = psycopg2.connect(dbname='d6nl8uste5t3fk', user='igtnybsnftnmqu',
                            password='ea76fc1725bd520b7f79115893279cf4905791f85140bd7af0bf677ee8a4dc3f',
                            host='ec2-54-166-167-192.compute-1.amazonaws.com', port='5432', sslmode='require')

    print('Connected!')

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

table = psql.read_sql('SELECT * FROM home_customer', conn)

def make_true(pin):
    pass

def make_false(pin):
    pass

while True:
    pincodes = table['pin'].uniques()
'''