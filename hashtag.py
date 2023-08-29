import re
text=' This is a #simple text with #hashtag and #morehashtags'
hashtags=re.findall(r'#\w+',text)
print(hashtags)