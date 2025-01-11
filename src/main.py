from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl
import os

driver = webdriver.Chrome()
driver.get(
    "https://jairamintas.com.br/search-results?status%5B%5D=venda&areas%5B%5D=centro-montes-claros-minas-gerais&min-price=0&max-price=0&bedrooms=&garage=&nome-condominio=&property_id="
)

precos = driver.find_elements(
    By.XPATH, "//div[@class='item-header']/ul/li[@class='item-price']"
)
links = driver.find_elements(By.XPATH, "//div[@class='listing-thumb']/a")


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "assets/imoveis.xlsx")
workbook = openpyxl.load_workbook(file_path)
pagina_imoveis = workbook["Planilha1"]


for preco, link in zip(precos, links):
    preco_imovel = preco.text.split("R$")[1]
    link_imovel = link.get_attribute("href")
    data_atual = datetime.now().strftime("%d/%m/%Y")

    pagina_imoveis.append([preco_imovel, link_imovel, data_atual])

workbook.save(file_path)
