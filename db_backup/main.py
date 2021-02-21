import pandas as pd
from django.db import connection

data = pd.read_csv('blog_post.csv')
ch = input("1 for django connection\n2 for direct pandas string\nplease select your choice : ")
if ch == '1':
    print("data backup started")
    data.to_sql('blog_post', connection, index=False, if_exists='append')
    print("data backup completed")

if ch == '2':
    print("data backup started")
    data.to_sql('blog_post',
                'postgresql://themisource:huruhujhyob1z8v3@app-d4dfbce5-3dc3-4fcc-bad7-0102ca3f0a6a-do-user-8599880-0.b.db.ondigitalocean.com:25060/themisource?sslmode=require',
                index=False, if_exists='append')
    print("data backup completed")
