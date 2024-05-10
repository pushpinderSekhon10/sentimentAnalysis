from textblob import TextBlob  # import textblob

with open('text.txt', 'r') as f:  # opens the file and
    text = f.read()  # reads the

blob = TextBlob(text)  # creates TextBlob object called blob
sentiment = blob.sentiment.polarity  # sets sentiment variable
print(sentiment)  # prints sentiment
