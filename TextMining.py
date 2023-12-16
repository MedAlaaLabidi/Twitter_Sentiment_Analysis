from textblob import TextBlob
from newspaper import Article
import nltk

#https://en.wikipedia.org/wiki/Mathematics
#https://www.cnbc.com/2021/01/18/stock-market-futures-open-to-close-news.html
#https://www.cnbc.com/2023/12/15/feds-john-williams-says-the-central-bank-isnt-really-talking-about-rate-cuts-right-now.html

url= 'https://www.cnbc.com/2021/01/18/stock-market-futures-open-to-close-news.html'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
if sentiment < 0:
    print('============> Negative <============')   
else:
    print('============> Positive <============')   