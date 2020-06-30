from selenium import webdriver
import time
import pandas as pd
import base64
import os
import numpy as np 
import datetime as dt
from sqlalchemy import create_engine
from random import randint
import time
import datetime


chromedriver = 'chromedriver_linux64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('headless')


driver = webdriver.Chrome(executable_path=chromedriver, options=options)
url ="https://www.fatsecret.com.br/calorias-nutri%C3%A7%C3%A3o"
url2 = 'https://www.fatsecret.com.br/calorias-nutri%C3%A7%C3%A3o/grupo/' 
url3 = 'https://www.fatsecret.com.br/calorias-nutri%C3%A7%C3%A3o/alimentos/'
driver.get(url)
lista_coisas = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "prominent", " " ))]//b')
grupos = []
produtos = []   

for coisa in lista_coisas:
    grupos.append(url2+coisa.text.replace(' ','-').replace(',','').lower())


for grupo in grupos:
    driver.get(grupo)
    lista_coisas2= driver.find_elements_by_xpath('//h2//a')
    for coisa2 in lista_coisas2:
        produtos.append(coisa2.text)

for produto in produtos:
    driver.get(url3+produto)
    calorias= driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nutrient", " " ))]')
    qtde = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "prominent", " " ))]')
    tipo = driver.find_elements_by_xpath('//h3')

    for ident in calorias:
        print('calorias')
        print(ident.text)
        
    for ident in tipo:
        print('Tipo')
        print(ident.text)
        
    for ident in qtde:
        print('quantidade')
        print(ident.text)