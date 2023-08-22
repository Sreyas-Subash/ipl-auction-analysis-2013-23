
"""
With this snippet you can connect to snowflake with python
More docs
https://docs.snowflake.com/en/user-guide/python-connector-pandas.html
In your .bashrc or .zshrc make sure you add the following variables
export user='MYUSERNAME'
export password='MYPASSWORD'
export account='hi68877'
Dependecies to run the script:
pip install "snowflake_connector_python[pandas]==2.8.2"
pip install jwt==1.3.1
To run it (after doing the other tasks):
python worksheets/connect.py
"""
import os
import pandas as pd
from snowflake import connector

print('starting connection')

snowflake_id = 'ps85586'
conn = connector.connect(
    user='****',
    password='****',
    region= 'ap-southeast-1',
    account=f'{snowflake_id}.snowflakecomputing.com',
    warehouse='IPL_AUCTION_DATA',
    database='IPL_AUC_13-23',
    schema ='IPL_SCHEMA',
    autocommit=True
    )

print('connection established')
print('connection object : ', type(conn))
print('account : ', conn.account)
print('db : ', conn.database)
print('schema : ', conn.schema)
print('warehouse : ', conn.warehouse)
print('application : ', conn.application)
print(os.getcwd())
cur = conn.cursor()

print('cursor obj : ', type(cur))

cur.execute("""
PUT file://D:\python_projects\ipl_scraping_13-23\data\ipl_player_13-23.csv @%player auto_compress = false overwrite = true
""")

cur.execute('COPY INTO PLAYER FILE_FORMAT = IPL_CSV_FORMAT')

# Fetches all records retrieved by the query and formats them in pandas DataFrame
# df = res.fetchall()
print('sql command executed')

cur.close()
conn.close()