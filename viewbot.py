#author: Michael Gulson
#viewbot goes to a page and refreshes after a period of time
import time;
from selenium import webdriver;
import os

timer = 3

##swimming with the dolphins
linkSWD = 'https://www.youtube.com/watch?v=olkZejLYFnE'
linkLinkedin = 'https://www.linkedin.com/in/michael-gulson-578270111'
linkStLorraine = 'https://master.d12a3k5j6x4df1.amplifyapp.com/'
linkYoutubeChannel = 'https://www.youtube.com/channel/UC9Ja9578qhjCLOoGXheKYwQ'

views = 1000

driver = webdriver.Chrome(executable_path='C:\Users\msgul\Downloads\chromedriver_win32\chromedriver.exe')
driver.get(linkSWD)

for i in range(views):
    time.sleep(timer)
    driver.refresh()