#import json
#from msilib.schema import tables
#from tkinter.tix import Tree
#from unittest import result
#from urllib import response

import requests
from bs4 import BeautifulSoup as bs
#from threading import *
from multiprocessing import Pool
from time import time, sleep
import csv
from random import choice
##### TRASH #####
def check_func_time(func):
    def wrapper (*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        work_time = end- start
        print(work_time)
        return result
    return wrapper

def write_csv(data):
    with open('coin.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
#################

def get_all_links(url):


    response = requests.get(url)
    soup = bs(response.content, 'lxml')
    list_of_cards = soup.find_all('div',{'data-cy':'l-card'}) 
    print(f"COUNT OF BLOCKS {len(list_of_cards)}")

    result = []
    for card in list_of_cards:   
        name = card.find('h6').text
        #print(name)
        location_and_date = card.find('p', {'data-testid':'location-date'}).text
        if " - " in location_and_date:
            (location,date_of_creating) = location_and_date.split(" - ")
        else:
            date_of_creating =  location_and_date  
            location = None
        try:
            price = card.find('p',{'data-testid':'ad-price'}).text
        except:
            price = None

        link_to_announcement = "https://www.olx.ua" + card.find('a', href=True).get('href')
        
        result.append([link_to_announcement, name, location, date_of_creating,price])

    return result


def get_page_data(info):
    try:
        url = info[0]
        response = requests.get(url)
        soup = bs(response.content)
        try:
            link_to_photo = soup.find('div', {"class":"swiper-zoom-container"}).find("img", src=True).get("src") #.get('href')
        except:
            link_to_photo = None
        try:
            description = soup.find('div',{"data-cy":"ad_description"}).find('div').text
            description = description.replace("\n", "").replace("\r","")
        except:
            description = None
        data = [url,info[1],info[2],info[3],info[4],link_to_photo,description]
        write_csv(data)
    
        #return (link_to_photo, description)
    except:
        print(f"ERROR AT {url}")




def get_href_to_random_category():
    list_of_cat = []
    response = requests.get("https://www.olx.ua/uk/")
    soup = bs(response.content,"lxml")
    all_category_block = soup.find_all('div',{'class':"subcategories-title"})
    for category in all_category_block:
        href_to_cat = category.find('a').get("href")
        if href_to_cat != "" and "https://www.olx.ua/d/" not in href_to_cat:
            href_to_cat = href_to_cat.replace("https://www.olx.ua/","https://www.olx.ua/d/")
        if href_to_cat != "":
            list_of_cat.append(href_to_cat)
    #print(list_of_cat)
    url = choice(list_of_cat)
    url_2 = url+"?page=2"

    return [url,url_2]
    
def main_parse():
    two_link = get_href_to_random_category()
        #получение всех ссылок для парсинга с главной страницы
    list_Of_links=[]
    for page_url in two_link:
        all_links = get_all_links(page_url)
        list_Of_links=list_Of_links+all_links
    #all_links = get_all_links(page_url)

         #обеспечение многопоточности
         #функции смотри help
    with Pool(10) as p:           
        p.map(get_page_data, list_Of_links)

#if __name__ == '__main__':
#    main()

#print(get_all_links("https://www.olx.ua/d/uk/zapchasti-dlya-transporta/"))
