import os, re
import requests
from bs4 import BeautifulSoup as bs
from collections import Counter

def get_text_from_url(url):
    # 주어진 URL에서 HTML 콘텐츠를 가져옴
    response = requests.get(url)
    # BeautifulSoup를 사용하여 HTML 파싱 
    soup = bs(response.text, 'html.parser')
    # 모든 텍스트를 추출
    text = soup.get_text()
    return text

def calculate_word_frequencies(text):
    # 단어만 추출하기 위해 정규식 사용
    words = re.findall(r'\b\w+\b', text.lower())
    # 단어 빈도수 계산
    word_counts = Counter(words)
    # 가장 많이 나온 5개 단어 찾기
    top_five = word_counts.most_common(5)
    return word_counts, top_five

# 웹페이지 URL
url = "https://quotes.toscrape.com/tag/life/"
# 웹페이지에서 텍스트 추출
webpage_text = get_text_from_url(url)

# 텍스트에서 빈도수 계산 및 상위 5개 단어 추출
_, top_five_words = calculate_word_frequencies(webpage_text)

print(top_five_words)
