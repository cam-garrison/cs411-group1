import nltk
from nltk.stem.snowball import SnowballStemmer
import snscrape.modules.twitter as sntwitter
import string


Sports = ['footbal', 'soccer', 'hockey', 'basketbal', 'basebal', 'mlb', 'mlh',
          'mls', 'nba', 'nfl', 'golf', 'pga', 'tenni', 'world', 'cup', 'fifa', 'olymp', 'team', 'sport', 'espn']

Fashion = ['shoe', 'cloth', 'top', 'bottom', 'dress', 'jewelri', 'fashion', 'outfit',
           'blous', 'belt', 'pant', 'jean', 'shirt', 'sweatshirt', 'sweatpant', 'bag', 'purs', 'heel', 'flat', 'gucci', 'chanel', 'prada', 'herm', 'nike',
           'zara', 'hm', 'adida', 'cartier', 'shop', 'jacket', 'versac', 'louis vuitton', 'boot']

Electronics = ['comput', 'phone', 'speaker', 'televis', 'tvs', 'audio',
               'video', 'onlin', 'internet', 'keyboard', 'mechan', 'graphic']

Videogames = ['gamer', 'playstat', 'nintendo', 'wii', 'arcad', 'consol', 'control', 'joystick', 'multiplay',
              'simul', 'gta', 'minecraft', 'fortnit', 'cod', 'mario', 'kart', 'sim', 'cross', 'xbox', 'ps3', 'ps4', 'ps5', 'smash']

Music = ['guitar', 'piano', 'instrument', 'orchestra', 'drum', 'beat', 'sing', 'play', 'listen', 'artist', 'band',
         'concert', 'live', 'spotifi', 'appl', 'music', 'soundcloud', 'singer', 'perform', 'album', 'song', 'track']

Food = ['chef', 'restaur', 'cook', 'eat', 'food', 'dinner', 'breakfast', 'lunch',
        'brunch', 'snack', 'burger', 'pasta', 'pizza', 'taco', 'burrito', 'sushi', 'meal']

Astrology = ['horoscop', 'zodiac', 'spiritu', 'retrograd', 'aquarius', 'capricorn', 'sagittarius', 'ari',
             'pisc', 'scorpio', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'sun', 'moon', 'star', 'constel']

Alcohol = ['beer', 'ipa', 'breweri', 'cocktail', 'whiski',
           'wine', 'wineri', 'bar', 'pub', 'liquor', 'drink']

Home = ['paint', 'canva', 'photographi', 'camera', 'art', 'artist',
        'pictur', 'portrait', 'color', 'frame', 'decor', 'potteri', 'craft']

# USED TO STEM OUR TOPICS KEYWORDS.
# snow_stemmer = SnowballStemmer(language='english', ignore_stopwords=True)
# stem_words = []

# for w in Home:
#     w = w.translate(
#         str.maketrans('', '', string.punctuation))
#     w = w.lower()
#     x = snow_stemmer.stem(w)
#     stem_words.append(x)
# print(stem_words)


def get_tweets(username):
    # first, we append user's tweets to a list.
    tweets_list = []

    print("from:{0}".format(username))
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper("from:{0}".format(username)).get_items()):
        if i > 1000:
            break
        tweets_list.append(tweet.content)
        if i % 100 == 0:
            print(tweet.content)

    # now lets make it all lowercase, remove punctuation etc.
    for x in range(len(tweets_list)):
        tweet = tweets_list[x].translate(
            str.maketrans('', '', string.punctuation))
        tweets_list[x] = tweet

    tweets_list = [t.lower() for t in tweets_list]

    # for x in range(len(tweets_list)):
    #     if x > 10:
    #         break
    #     print(tweets_list[x])

    # ok now we have it in lowercase w punctuation removed. now let's tokenize the strings
    tokens = [sub.split() for sub in tweets_list]

    # alright, have the tokenized strings, now lets stem them!
    snow_stemmer = SnowballStemmer(language='english', ignore_stopwords=True)
    stem_words = []
    for List in tokens:
        for w in List:
            x = snow_stemmer.stem(w)
            stem_words.append(x)
    print(stem_words)
    return stem_words


def choose_category(words):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # our nine categories initialize at 0
    categories = ['Sports', 'Fashion', 'Electronics', 'Videogames',
                  'Music', 'Food', 'Astrology', 'Alcohol', 'Home']
    for word in words:
        if word in Sports:
            count[0] += 1
        if word in Fashion:
            count[1] += 1
        if word in Electronics:
            count[2] += 1
        if word in Videogames:
            count[3] += 1
        if word in Music:
            count[4] += 1
        if word in Food:
            count[5] += 1
        if word in Astrology:
            count[6] += 1
        if word in Alcohol:
            count[7] += 1
        if word in Home:
            count[8] += 1
    print(count)
    max_value = max(count)
    if max_value == 0:
        return "NoCat"
    print(categories[count.index(max_value)])
    return categories[count.index(max_value)]


def get_category(user):
    list1 = get_tweets(user)
    if not list1:
        return "NoTweets"
    return choose_category(list1)


# print(get_category("Angela23283570"))
