import urllib.request
import os, sys

os.chdir(os.path.dirname(sys.argv[0]))

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

urllib.request.urlretrieve(url, './corona_time_series.csv')