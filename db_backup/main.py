import html
import re

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
                'postgresql://usman:Fa@12345@localhost:5432/tms',
                index=False, if_exists='append')
    print("data backup completed")


# def remove_tags(string):
#     result = re.sub('<.*?>', '', string)
#     return result
#
#
# data['post_content'] = data['post_content'].apply(lambda cw : remove_tags(cw))
# data['post_content'] = data['post_content'].apply(
#     lambda x: " ".join(re.sub('(http|https)://[a-zA-Z0-9./-]+', '', x) for x in x.split()))
# data['post_content'] = data['post_content'].apply(lambda x: " ".join(html.unescape(x) for x in x.split()))
# data['post_content'] = data['post_content'].apply(lambda x: " ".join(x.lower() for x in x.split()))
# # data['sentence'] = data['sentence'].str.replace('[^\w\s]', '')
# print(data['post_content'].head())
# data.to_csv("clean_posts.csv", index=False)
