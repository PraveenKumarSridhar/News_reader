from GoogleNews import GoogleNews
googlenews = GoogleNews(lang='en')

def get_news(news_topic:str):
    googlenews.search(news_topic) 
    headlines = googlenews.get_texts()[1:10]
    links = googlenews.get_links()[1:10]
    
    return headlines, links


# print('Enter news you are interested in:')
# news_topic = input()
# get_news(news_topic)