import requests
from requests_futures.sessions import FuturesSession
from requests_futures import sessions
import json
import psycopg2
from psycopg2 import Error
import pandas.io.sql as psql
import pandas as pd
from datetime import datetime, timedelta
import time
from json import JSONDecodeError

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def check(params):
    print(len(params))
    session = sessions.FuturesSession(max_workers=6)
    futures = [session.get(url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin",
                           headers=headers, params=p) for p in params]
    for f in futures:
        f.result()

    session.close()

    return futures


def send(pin):
    emails = table[table['pin'] == pin]['email'].values

    for email in emails:
        print(f'Sent {pin} {email}')
        requests.post(
            "https://api.mailgun.net/v3/whenismyvaccine.in/messages",
            auth=("api", "83c8481eed353ca9d76bbdd3101a2b33-2a9a428a-5bb25d17"),
            data={"from": "When is my vaccine? <alerts@whenismyvaccine.in>",
                  "to": email,
                  "subject": "Thank for registering to WhenIsMyVaccine",
                  "text": f"Hello {email}, \n Vaccines are available in your area. For pin: {pin}"})

    cur.execute(
        f'UPDATE home_customer SET flag1=1, flag2=1 WHERE pin={pin};')
    conn.commit()


def unflag(pin):
    emails = table[table['pin'] == pin]['email'].values

    for email in emails:
        print(f'{pin} {email} Unflagged')

    cur.execute(
        f'UPDATE home_customer SET flag1=0, flag2=0 WHERE pin={pin};')
    conn.commit()


x = 100


while True:
    # Check connection
    try:
        conn = psycopg2.connect(dbname='dfpglck7sd4deq', user='vfpfcrcywbbppp',
                                password='2306588cdf3b2662603049a475863835f2ac89cdd52af890323a181d0405601c',
                                host='ec2-52-0-114-209.compute-1.amazonaws.com', port='5432', sslmode='require')
        cur = conn.cursor()

        print('Connected!')

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    # Get Table & pincodes
    table = psql.read_sql('SELECT * FROM home_customer', conn)
    P = table['pin'].value_counts()

    #will run for each 100
    for z in range(len(P)//100 + 1):
        pins = P[z*x:z*x+x].index
        avail = [0 for i in range(len(pins))]
        current = []

        for pin in pins:
            current.append(table[table['pin'] == pin]['flag2'].values[0])

        params = []
        date = datetime.today()

        for pin in pins:
            params.append(
                {'pincode': str(pin), 'date': str(date.strftime("%d-%m-%Y"))})

        try:
            responses = check(params)

        except JSONDecodeError:
            print('JSONDecodeError')
            time.sleep(300)

        for i in range(len(pins)):
            res = responses[i].result().json()

            if list(res.keys())[0] == 'sessions':
                if len(res['sessions']) != 0:
                    for session in res['sessions']:
                        for j in range(len(session)):
                            if session['available_capacity'] > 0 and session['min_age_limit'] == 18:
                                avail[i] = 1

            elif list(res.keys())[0] == 'centers':
                if len(res['centers']) != 0:
                    for center in res['centers']:
                        for j in range(len(center['sessions'])):
                            if center['sessions'][j]['available_capacity'] > 0 and center['sessions'][j]['min_age_limit'] == 18:
                                avail[i] = 1


        for i in range(len(pins)):
            if avail[i] != current[i]:
                if avail[i] > current[i]:
                    send(pins[i])

                elif avail[i] < current[i]:
                    unflag(pins[i])

        time.sleep(300)

    print("*"*100)
