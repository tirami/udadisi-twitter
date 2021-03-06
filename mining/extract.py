from collections import defaultdict
import HTMLParser
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

tknzr = TweetTokenizer()
stop = stopwords.words('english') + stopwords.words('spanish')
tags_to_remove = ['PRP', 'PRP$', 'RP', 'TO', 'IN']


def remove_rt(text):
    return text.replace('RT', '')


def unescape_html_chars(text):
    h = HTMLParser.HTMLParser()
    return h.unescape(text)


def remove_urls(text):
    url_re = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.sub(url_re, '', text, flags=re.MULTILINE)


def remove_non_whitelisted_characters(text):
    regex = re.compile('\W+', re.UNICODE)
    return regex.sub('', text)


def remove_twitter_usernames(text):
    regex = re.compile('@\w*')
    return regex.sub(' ', text)


def remove_stopwords(tagged):
    terms = [word for (word, tag) in tagged if word.lower() not in stop and tag not in tags_to_remove and len(word) > 1]
    return terms


def process_status(text):
    text = remove_urls(text)
    text = unescape_html_chars(text)
    text = remove_twitter_usernames(text)
    text = remove_rt(text)
    text = remove_non_whitelisted_characters(text)
    tokens = tknzr.tokenize(text)
    # print tokens
    tagged = nltk.pos_tag(tokens)
    terms = remove_stopwords(tagged)
    terms_dict = defaultdict(int)
    for noun in terms:

        terms_dict[noun] += 1
    return terms_dict
