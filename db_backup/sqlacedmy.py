import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

conn = "postgresql://tms:oBINEZjwEdiRtoKj@app-9173c0ea-e32d-46c2-9a1e-11551afb6053-do-user-8599880-0.b.db" \
       ".ondigitalocean.com:25060/tms"
engine = create_engine(conn, echo=True)
df = pd.read_csv('clean_posts.csv')
print("columns : ", df.columns)
df['city'] = ''
df['seen'] = 0
df.to_sql("blog_post", if_exists='replace', con=engine,  index=False)  # ,
