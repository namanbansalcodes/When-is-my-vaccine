import psycopg2
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
print(table)
