# COVID-19_Br_data
Number of cases of COVID-19 in Brazilian cities. 
This repository contains daily case reports. All updates are made at 21:00 (GMT). 

"Unknown" corresponds to the sum of cases in cities whose names were not disclosed by the goverment.


## File naming:
Archived files (archived_files folder): MM-DD-YYYY.csv 

Latest file (in 'today_data' folder): latest_covid_br.csv

## How to use
You can read the files with [pandas](https://github.com/pandas-dev/pandas):
```python
df = pd.read_csv('today_data/latest_covid_br.csv', encoding="utf-16")
```
Or you can directly give pandas the data url:
```python
df = pd.read_csv('https://raw.githubusercontent.com/ljduarte/COVID-19_Br_data/master/today_data/latest_covid_br.csv', encoding='utf-16')
```

## Source: 
https://especiais.g1.globo.com/bemestar/coronavirus/mapa-coronavirus/


About COVID-19: https://www.who.int/emergencies/diseases/novel-coronavirus-2019

