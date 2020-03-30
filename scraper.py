
from selenium.webdriver import Chrome
import pandas as pd
import datetime

current_date = datetime.datetime.now()
filename = str(format(current_date.month, '02d'))+'_'+ str(format(current_date.day, '02d'))+'_'+str(current_date.year)


webdriver = "chromedriver.exe"
url = 'https://especiais.g1.globo.com/bemestar/coronavirus/mapa-coronavirus/'
driver = Chrome(webdriver)
driver.get(url)

items = driver.find_elements_by_class_name("places__item")

total = []

for data in items:
    if data.find_element_by_class_name('places__cell').text == 'Não informado':
        city = 'Unknown'
        state = 'Unknown'
    elif len(data.find_element_by_class_name('places__cell').text.split(',')) == 1:
        city = data.find_element_by_class_name('places__cell').text.split(',')[0]
        state = 'Unknown'
    else:
        city = data.find_element_by_class_name('places__cell').text.split(',')[0]
        state = data.find_element_by_class_name('places__cell').text.split(',')[1]
    
    cases = data.find_element_by_class_name('places__cell--right').text
    new = ((city, state, cases))
    total.append(new)

df = pd.DataFrame(total,columns=['City' , 'State', 'Confirmed Cases'])


df.to_csv('archived_files/' + filename + '.csv', encoding='utf-16')
df.to_csv('today_data/latest_covid_br.csv', encoding='utf-16')

driver.close()
      