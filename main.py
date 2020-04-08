import numpy as np
import matplotlib.pyplot as plt
import os, sys
import pandas as pnds

# set file directory as working directory
os.chdir(os.path.dirname(sys.argv[0]))
# print command line arguments
print(sys.argv)

# load data from file
file_ = sys.argv[1] if len(sys.argv)>1 else "./corona_time_series.csv"

# how many days should be averaged over, either take from command line arguments if provided or use 5
avg_days = int(sys.argv[2]) if len(sys.argv)>2 else 5

# which countries should be displayed, take from n last command line arguments if provided, else use Italy, US and Germany
country_list_ = sys.argv[3:len(sys.argv)] if len(sys.argv)>3 else ["Italy", "US", "Germany"]

# print list of countries displayed
print(country_list_)

# read csv file using pandas, add Lines corresponding to countries in country_list_ to iList
csv = pnds.read_csv(file_)
iList = [0]*len(country_list_)
for i,obj in enumerate(csv["Country/Region"]):
    if obj in country_list_:
        iList[country_list_.index(obj)] = i

# setup figures
fig, ax = plt.subplots(1,1, dpi=150, figsize=(3,3))
fig2, ax2 = plt.subplots(1,1, dpi=150, figsize=(3,3))

# run through countries and get plot data
for i_c, cntry in zip(iList, country_list_):
    time_series = csv.loc[i_c][4:]
    delta_per_day = [time_series[i+1]-time_series[i] for i in range(len(time_series)-1)]
    last_days_patients = [np.sum(delta_per_day[i:i+avg_days]) for i in range(len(delta_per_day)-avg_days)]

    x = time_series[avg_days+1:]
    y = np.array(last_days_patients)[list(x>100)]
    x = x[x>100]

    ax.plot(x,y,'o--',label=cntry,markersize=3, fillstyle='none',linewidth=1)
    ax2.plot(range(len(y)),y/avg_days,"o--", label=cntry,markersize=3, linewidth=1, fillstyle='none')

# set graph options
if file_ == "./corona_time_series.csv":
    ax.set_ylabel('Neue Patienten letzte %d Tage' % avg_days)
    ax.set_xlabel('Patienten Total')
    ax.legend()
    fig.tight_layout()
    fig.savefig('NeuePatienten-PatientenTotal_%dTage.png'%avg_days)
    ax.set_yscale("log")
    ax.set_xscale("log")
    fig.tight_layout()
    fig.savefig('NeuePatienten-PatientenTotal_%dTage_loglog.png'%avg_days)

    ax2.set_ylabel("$\\varnothing$ neue Patienten pro Tag")
    ax2.set_xlabel("Tage nach 100 erreichten Fällen")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig('NeuePatienten-Tage_%dTageDurchschnitt.png'%avg_days)
else:
    ax.set_ylabel('Neue Tote letzte %d Tage' % avg_days)
    ax.set_xlabel('Tote Total')
    ax.legend()
    fig.tight_layout()
    fig.savefig('NeueTote-ToteTotal_%dTage.png'%avg_days)
    ax.set_yscale("log")
    ax.set_xscale("log")
    fig.tight_layout()
    fig.savefig('NeueTote-ToteTotal_%dTage_loglog.png'%avg_days)

    ax2.set_ylabel("$\\varnothing$ neue Tote pro Tag")
    ax2.set_xlabel("Tage nach 100 erreichten Toten")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig('NeueTote-Tage_%dTageDurchschnitt.png'%avg_days)