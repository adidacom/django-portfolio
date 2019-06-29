import datetime
import math
import re

from django.utils.html import strip_tags


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0)
    # read_time_sec = read_time_min * 60
    read_time = str(datetime.timedelta(minutes=read_time_min))
    return read_time


def get_header_text():
    header_text = ['If you heard it from us, then it\'s possibly true.', 'The #1 source of real fake news.',
                   'Sometimes it\'s not what you said, it\'s how you said it.',
                   'There is fake news. And there is REAL fake news.',
                   'Numbers don\'t lie, but then there are imaginary numbers.']
    return header_text
