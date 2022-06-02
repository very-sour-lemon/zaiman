import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from googletrans import Translator
import re
tr = Translator(service_urls=['translate.googleapis.com'])

def main(request):
    URL = "https://www.yahoo.co.jp/"
    rest = requests.get(URL)
    soup = BeautifulSoup(rest.text, "html.parser")
    data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    found = soup.find('p', class_='_2vq5UBfOFpYcyqNRy51gDf')
    list1 = []
    list2 = []
    for data in data_list:
        result1 = data.span.string
        result2 = tr.translate(data.span.string, src="ja", dest="en")
        list1.append(result1)
        list2.append(result2.text)
    content ={ 'news1':list1[0],
               'news2':list1[1],
               'news3':list1[2],
               'news4':list1[3],
               'news5':list1[4],
               'trans1':list2[0],
               'trans2':list2[1],
               'trans3':list2[2],
               'trans4':list2[3],
               'trans5':list2[4],
               'date':found.text  }
    return render(request, 'main/index.html', content)