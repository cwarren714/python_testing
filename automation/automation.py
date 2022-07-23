# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/ for cheat sheet


from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service(executable_path='./msedgedriver.exe')
edge = webdriver.Edge(service=service)

edge.maximize_window()
edge.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

print('Selenium Easy Demo' in edge.title)
