import urllib.request
import os, sys

os.chdir(os.path.dirname(sys.argv[0]))

url_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

urllib.request.urlretrieve(url_confirmed, './corona_time_series.csv')
urllib.request.urlretrieve(url_deaths, './corona_time_series_deaths.csv')