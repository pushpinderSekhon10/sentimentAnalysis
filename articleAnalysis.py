from textblob import TextBlob
from newspaper import Article
import nltk

url = 'https://www.cbc.ca/news/canada/ottawa/ottawa-homicide-barrhaven-berrigan-drive-arrest-1.7136366'
article = Article(url)  #sets variable to an object of type article

article.download()  # we use the Article object functions to download the article and parse it
article.parse()

article.nlp()  # this function will allow us to perform various natural language processing functions to the article

blob = TextBlob(article.text)  # creating TextBlob object using the summary of the text in the article
# we are doing this because this object has many useful functions
sentiment = blob.sentiment.polarity  # this will give us the sentiment of the article as a floating point number from
# -1 to 1

print(article.summary)  # prints summary

print(sentiment)  # prints sentiment


