!apt install chromium-chromedriver #bibliotecas necessárias
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium
import time
import random, os, sys
import tweepy
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.ChromeOptions() # options declaradas para que o algoritmo rode no google colab
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

while(True):
  chrome = webdriver.Chrome('chromedriver',options=options)
  sites=['https://www.receiteria.com.br/receitas-fit/',
         'https://www.receiteria.com.br/receitas-fitness-simples/',
         'https://www.receiteria.com.br/receitas-de-bolo-fitness/',
         'https://www.receiteria.com.br/receitas-de-doces-fitness/',
         'https://www.receiteria.com.br/receitas-de-lanches-fitness/',
         'https://www.receiteria.com.br/receitas-para-marmita-fitness/',
         'https://www.receiteria.com.br/receitas-fitness/',
         'https://www.receiteria.com.br/receitas-de-pure-de-batata-doce/',
         'https://www.receiteria.com.br/receitas-de-maionese-vegana/',
         'https://www.receiteria.com.br/receitas-de-pao-de-cenoura/',
         'https://www.receiteria.com.br/+receitas-de-comida-light/',
         'https://www.receiteria.com.br/receitas-de-brigadeiro-de-batata-doce/',
         'https://www.receiteria.com.br/receitas-para-almoco-saudavel/',
         'https://www.receiteria.com.br/receitas-com-aveia-em-flocos/',
         'https://www.receiteria.com.br/receitas-de-bolo-fitness/',
         'https://www.receiteria.com.br/receitas-de-brownie-fit/',
         'https://www.receiteria.com.br/receitas-de-bolo-de-caneca-fit/',
         'https://www.receiteria.com.br/receitas-de-pao-de-queijo-fit/',
         'https://www.receiteria.com.br/receitas-de-bolinho-de-chuva-assado/'] #exemplos de sites com receitas

  num = random.randint(0,18) #escolhe o site de maneira aleatória usando random
  site = sites[num]
  print("site eh: ",site) #printa site escolhido
  chrome.get(site)
  if(num == 18):
    conteudo = chrome.find_elements_by_css_selector('h2 a')
  else:
    conteudo = chrome.find_elements_by_css_selector('p a')
  
  for i in (range(0, len(conteudo))):
    print(i)
    print("conteudo :", conteudo[i].text)
  
  print("tamanho de conteudo: ", len(conteudo))
  
  numero = 0
  if (num == 0): #ifs para escolher uma receita aleatória no site escolhido acima
    numero = random.randint(0, 100) #primeiro site possui 100 receitas, por isso random entre 0 e 100
  elif(num == 1):
    numero = random.randint(0, 73) #segundo site possui 73 receitas
  elif(num == 2):
    numero = random.randint(0, 36) #assim por diante..
  elif(num == 3):
    numero = random.randint(0, 40)
  elif(num == 4):
    numero = random.randint(0, 50)
  elif(num == 5):
     numero = random.randint(0, 60)
  elif(num == 6):
     numero = random.randint(0, 60)
  elif(num == 7):
     numero = random.randint(0, 19)
  elif(num == 8):
     numero = random.randint(0, 17)
  elif(num == 9):
     numero = random.randint(0, 18)
  elif(num == 10):
     numero = random.randint(0, 22)
  elif(num == 11):
     numero = random.randint(0, 11)
  elif(num == 12):
     numero = random.randint(0, 30)
  elif(num == 13):
     numero = random.randint(0, 25)
  elif(num == 14):
     numero = random.randint(0, 36)
  elif(num == 15):
     numero = random.randint(0, 17)
  elif(num == 16):
     numero = random.randint(0, 21)
  elif(num == 17):
     numero = random.randint(0, 16)
  elif(num == 18):
    numero = random.randint(0, 7)
  print("o numero eh: ", numero)
  post_title = conteudo[numero].text
  post_link = conteudo[numero].get_attribute('href')

  hashtags = ['#emagrecer', '#perderpeso', 'quero perder peso', 'quero emagrecer',
              'emagrecer', 'perder peso', 'preciso emagrcer', 'preciso perder peso', 'emagrecer já', 'perder peso agora'  ] #hashtags sobre o assunto 

  numero2 = random.randint(0,5)
  numero3 = random.randint(0,5)
  tag = hashtags[numero2] 
  tag1 = hashtags[numero3]

  texto = "{titulo} \nLink: {link} \n\n\n\n TAGS (ignore) \n {hashtag1} {hashtag2} ".format(
	      titulo=post_title,
	      link=post_link,
        hashtag1 = tag,
        hashtag2 = tag1)
  print(texto)
 
  consumer_secret = ""
  consumer_key = ""           #Credenciais do twitter dev necessárias para postar no twitter através da API
  access_token = ""
  access_token_secret = ""
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)          #Logando 
  
  api.update_status(status=texto) #Então postamos no twitter o texto gerado
	#chrome.quit()
  time.sleep(3600)