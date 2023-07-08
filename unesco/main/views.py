from django.shortcuts import render
from .models import CrollData
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def index(request): 
    if not CrollData.objects.all(): 
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        url = ('https://www.youtube.com/results?search_query=우리나라+유네스코+세계유산')
        driver.get(url)
        soup = bs(driver.page_source, 'lxml')
        my_titles = soup.select(
        'h3 > a'
        )

        title = []
        url = []
        
        for i in range(4):
            title.append(my_titles[i].text[:29]+'...')
            url.append('https://www.youtube.com'+ my_titles[i].get('href'))
        
        for i in range(4):
            crolling_data = CrollData
            crolling_data(
                title=title[i],
                link=url[i],
            ).save()
        
    tmp = CrollData.objects.all()
    data = {}
    data["crolling_data"] = tmp
        
    return render(request, 'main.html', data)

def map(request): 
    return render(request, 'map.html')
