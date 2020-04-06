import numpy as np
import matplotlib.pyplot as plt
import os, sys
import pandas as pnds

os.chdir(os.path.dirname(sys.argv[0]))
print(sys.argv)
file_ = "./corona_time_series.csv"
avg_days = int(sys.argv[1]) if len(sys.argv)>1 else 5

country_list_ = sys.argv[2:len(sys.argv)] if len(sys.argv)>2 else ["Italy", "US", "Germany"]

print(country_list_)

csv = pnds.read_csv(file_)
iList = [0]*len(country_list_)
for i,obj in enumerate(csv["Country/Region"]):
    if obj in country_list_:
        iList[country_list_.index(obj)] = i

fig, ax = plt.subplots(1,1, dpi=300, figsize=(3,3))
fig2, ax2 = plt.subplots(1,1, dpi=300, figsize=(3,3))

for i_c, cntry in zip(iList, country_list_):
    time_series = csv.loc[i_c][4:]
    delta_per_day = [time_series[i+1]-time_series[i] for i in range(len(time_series)-1)]
    last_days_patients = [np.sum(delta_per_day[i:i+avg_days]) for i in range(len(delta_per_day)-avg_days)]

    x = time_series[avg_days+1:]
    y = np.array(last_days_patients)[list(x>100)]
    x = x[x>100]

    ax.plot(x,y,'o--',label=cntry,markersize=3, fillstyle='none',linewidth=1)
    ax2.plot(range(len(y)),y/avg_days,"o--", label=cntry,markersize=3, linewidth=1, fillstyle='none')

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

#plt.show()