import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

conn = "postgresql://tms:0cxqVdnP2j7LLxv2@app-c63a9ccd-ad0e-4248-b14f-a5a07e6c4882-do-user-8599880-0.b.db.ondigitalocean.com" \
       ":25060/tms"
engine = create_engine(conn, echo=True)
df = pd.read_csv('blog_post.csv')
print("columns : ", df.columns)
df['city'] = ''
df['seen'] = 0
df.to_sql("blog_post", if_exists='append', con=engine,  index=False)  # ,
