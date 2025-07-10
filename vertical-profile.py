# -*- coding: utf-8 -*-
"""

@author: Amirhossein Sedghi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#----------------------------------
src1 = 'D:\\education\\BTU\\microclimate\\ex3\\Abu-Dhabi.txt'

da = pd.read_csv(src1,
                 header=[0,1],
                 skipfooter=4, 
                 delim_whitespace=True,
                 na_values=-999.00)

src2= 'D:\\education\\BTU\\microclimate\\ex3\\africa.txt'
db = pd.read_csv(src2,
                 header=[0,1],
                 skipfooter=4, 
                 delim_whitespace=True,
                 na_values=-999.00)
#------------------------------------
da.columns
# 
# 
#
da['SKNT', 'knot']= da['SKNT', 'knot']*0.514444 # convert to m/s
db['SKNT', 'knot']= db['SKNT', 'knot']*0.514444 # convert to m/s

fig, (tmp1,tmp2) = plt.subplots(1,2,figsize=(6,6))
tmp11=tmp1.twinx()
tmp1.plot(da[('TEMP','C')],da[('HGHT','m')],'r',label='Temp')
tmp1.set_ylabel('height [m]')
tmp1.set_xlabel('[°C]')
tmp1.set_title('Air temperature')
tmp1.invert_yaxis()
tmp2.plot(db[('TEMP','C')],db[('HGHT','m')],'r',label='Temp')
tmp2.invert_yaxis()
tmp2.set_ylabel('height [m]')
tmp2.set_xlabel('[°C]')
tmp2.set_title('Air temperature')
fig.tight_layout()
plt.show()
#wind speed
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # دو نمودار افقی کنار هم


ax1.plot(da['SKNT'], da['HGHT'], 'b-', linewidth=2)
ax1.set_xlabel('Wind speed [m/s]')
ax1.set_ylabel('Height [m]')
ax1.set_title('Wind Speed - Abu Dhabi')
ax1.invert_yaxis()
ax1.grid(True)


ax2.plot(db['SKNT'], db['HGHT'], 'r-', linewidth=2)
ax2.set_xlabel('Wind speed [m/s]')
ax2.set_ylabel('Height [m]')
ax2.set_title('Wind Speed - Africa')
ax2.invert_yaxis()
ax2.grid(True)

fig.tight_layout()
plt.show()
#wind 
#direction
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

#abu dhabi wind direction
ax1.plot(da['DRCT'], da['HGHT'], color='green', linewidth=2)
ax1.set_xlabel('Wind direction [°]', fontsize=12)
ax1.set_ylabel('Height [m]', fontsize=12)
ax1.set_title('Wind Direction - Abu Dhabi', fontsize=14)
ax1.invert_yaxis()
ax1.grid(True)

#wind direction africa
ax2.plot(db['DRCT'], db['HGHT'], color='orange', linewidth=2)
ax2.set_xlabel('Wind direction [°]', fontsize=12)
ax2.set_ylabel('Height [m]', fontsize=12)
ax2.set_title('Wind Direction - Africa', fontsize=14)
ax2.invert_yaxis()
ax2.grid(True)


fig.tight_layout()
plt.show()
# one plot
fig, tmp1 = plt.subplots(1,figsize=(6,8))
tmp2=tmp1.twinx()
tmp1.plot(da[('TEMP','C')],da[('HGHT','m')],'r',label='Temp')
tmp1.set_ylabel('height [m]')
tmp1.set_xlabel('[°C]')
tmp1.set_title('Air temperature')

tmp2.plot(da[('TEMP','C')],da[('PRES','hPa')],'k',label='Temp')
tmp2.invert_yaxis()
tmp2.set_ylabel('pressure [hPa]')
tmp2.set_xlabel('[°C]')
tmp2.set_title('Air temperature')
fig.tight_layout()
plt.show()
#----------------------------
# logarithmic
fig, tmp1 = plt.subplots(1, figsize=(6, 8))
tmp2 = tmp1.twinx()

# temp ~ height
tmp1.plot(da[('TEMP','C')], da[('HGHT','m')], 'r',linewidth=2 ,label='Temp')
tmp1.set_ylabel('Height [m]',fontsize=14)
tmp1.set_xlabel('Temperature [°C]',fontsize=14)
tmp1.set_title('Air Temperature',fontsize=18)
tmp1.tick_params(axis='both', which='major', labelsize=14)

# temp vs. pressure (log-scale)
tmp2.plot(da[('TEMP','C')], da[('PRES','hPa')], 'b',linewidth=2 ,label='Temp (vs pressure)')
tmp2.set_yscale('log')
tmp2.invert_yaxis()
tmp2.set_ylabel('Pressure [hPa]',fontsize=14)
tmp2.grid(True, which="both", axis="y", linestyle="--", linewidth=1)

lines1, labels1 = tmp1.get_legend_handles_labels()
lines2, labels2 = tmp2.get_legend_handles_labels()
tmp2.legend(lines1 + lines2, labels1 + labels2, loc='best',ncol=1,fontsize=14)

fig.tight_layout()
plt.show()
#fig.savefig(src+'Temp_profiles.png', dpi=600,bbox_inches='tight')

