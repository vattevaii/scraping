from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()
baseURL = "https://www.nhsinform.scot/"
driver.get(baseURL+"illnesses-and-conditions/a-to-z/")

listOfIllness = driver.find_elements_by_class_name("nhs-uk__az-link")
# print(listOfIllness)

soup = BeautifulSoup(listOfIllness[0], 'html5lib')
