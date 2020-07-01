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
        produtos.append(coisa2.text.replace(' ','-').replace(',','').lower())
        
dic_prod = {}
for produto in produtos:
    try:
        print(produto)
        driver.get(url3+produto)
        calorias= driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nutrient", " " ))]')
        qtde = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "prominent", " " ))]')
        tipo = driver.find_elements_by_xpath('//h3')
    
    
        x = int(len(calorias)/4)
        y = int(len(qtde)/len(tipo))
       
        for v in range(0,len(tipo)):
            for i in range(1,x):
                dic_especific = {}
                for k in range(0,y):
                    dic_especific[qtde[k].text] = [tipo[v].text,[calorias[i*4].text,calorias[(i*4+1)].text,calorias[i*4+2].text,calorias[i*4+3].text]]
        dic_prod[produto] = dic_especific
        driver.close()
    except:
        driver.close()
        continue
    
x = pd.DataFrame(data=dic_prod).T