from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import requests
import psycopg2
import string
import requests
import psycopg2
import re


def get_all_pages():
  URLS=[]
  for c in string.ascii_lowercase:
    URL = f'https://oect.org.tn/annuaire-des-membres-de-lordre-des-experts-comptables-de-tunisie-{c}/'
    URLS.append(URL)
  return URLS
def est_numero_telephone(chaine):
        # Définir le motif d'un numéro de téléphone
        motif = r"^\d{8}$"  # Exemple de motif pour un numéro de téléphone de format
        motif1=  r"^\d{2}\s\d{3}\s\d{3}$"
        # Vérifier si la chaîne correspond au motif
        if re.match(motif, chaine) or re.match(motif1,chaine):
            return True
        else:
            return False
         


    # Wait for the page to load completely

    # Find the element containing phone numbers
def parse_attroney(url): 
  PATH = "C:\\Program Files (x86)\\chromedriver.exe"
  driver = webdriver.Chrome(PATH) 
  driver.get(url)  
  elements = driver.find_elements(By.CLASS_NAME, 'contact-info')
  for element in elements :
    numero_telephone=element.find_elements(By.CSS_SELECTOR, "p a")
    name=element.find_element(By.TAG_NAME, "h4")
    try:
      numero_tel=numero_telephone[1].text
    except AttributeError as e :
      numero_tel=" "  
    try:
     name= name.text.rstrip("| Inscrit")
    except AttributeError as e :
      name=" "  
    chemin=r"C:\Users\Dell\Desktop\MYphpp\annuaire_experts.txt"
    with open(chemin,"a" ) as f :
      f.write(f"{name}\n")
      f.write(f"{numero_tel}\n")
      f.write("Expert Comptable\n\n")
    
    
def parse_all_attorneys():
  pages=get_all_pages()
  for page in pages :

   parse_attroney(page)


parse_all_attorneys()  
