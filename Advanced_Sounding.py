# Copyright (c) 2015,2016,2017 MetPy Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause

# Modified by Severi Savukoski on 2023/04/08
"""
=================
Advanced Sounding
=================

Plot a sounding using MetPy with more advanced features.

Beyond just plotting data, this uses calculations from `metpy.calc` to find the lifted
condensation level (LCL) and the profile of a surface-based parcel. The area between the
ambient profile and the parcel profile is colored as well.
"""

import matplotlib.pyplot as plt
import pandas as pd

import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.plots import add_metpy_logo, SkewT
from metpy.units import units
from fmiopendata.wfs import download_stored_query


# import datetime as dt
# # Limit the time
# now = dt.datetime.utcnow()
# # Depending on the current time and availability of the model data, adjusting
# # the hours below might be necessary to get any data
# start_time = now.strftime('%Y-%m-%dT00:00:00Z')
# end_time = now.strftime('%Y-%m-%dT18:00:00Z')


#Makkonen 220 km FAI
#start_time = "2022-05-24T10:00:00Z"
#end_time = "2022-05-24T15:00:00Z"


# #Makkonen 200 km FAI
# start_time = "2021-07-26T10:00:00Z"
# end_time = "2021-07-26T15:00:00Z"

# #Makkonen 162 km avoin kolmio
# start_time = "2022-06-07T10:00:00Z"
# end_time = "2022-06-07T15:00:00Z"


# #Makkonen 508 km 
# start_time = "2021-06-11T10:00:00Z"
# end_time = "2021-06-11T15:00:00Z"

# #Makkonen 389 km 
# start_time = "2020-06-11T10:00:00Z"
# end_time = "2020-06-11T15:00:00Z"

# #Makkonen 432 km 
# start_time = "2021-05-29T10:00:00Z"
# end_time = "2021-05-29T15:00:00Z"



# #Makkonen 160 km FAI 
# start_time = "2021-06-10T10:00:00Z"
# end_time = "2021-06-10T15:00:00Z"

# #Makkonen 180 km FAI 
# start_time = "2020-05-26T10:00:00Z"
# end_time = "2020-05-26T15:00:00Z"


# #Savukoski 150 km 
# start_time = "2016-06-06T10:00:00Z"
# end_time = "2016-06-06T15:00:00Z"

#3000 tonnin keliä 
#start_time = "2020-05-25T10:00:00Z"
#end_time = "2020-05-25T15:00:00Z"

#keliä vielä 8 jälkeen 
start_time = "2021-07-03T10:00:00Z"
end_time = "2021-07-03T15:00:00Z"


# #keliä vielä 8 jälkeen 
# start_time = "2021-05-30T10:00:00Z"
# end_time = "2021-05-30T15:00:00Z"


# #Huippu keli Pallaksella 
# start_time = "2014-04-18T10:00:00Z"
# end_time = "2014-04-18T15:00:00Z"

# #Sahlström 190 km 
# start_time = "2012-06-12T10:00:00Z"
# end_time = "2012-06-12T15:00:00Z"

# #Sahlström 141 FAI km 
# start_time = "2022-08-09T10:00:00Z"
# end_time = "2022-08-09T15:00:00Z"

# #Sahlström 111 FAI km 
# start_time = "2020-08-28T10:00:00Z"
# end_time = "2020-08-28T15:00:00Z"

# #Sahlström 143 FAI km 
# start_time = "2020-07-15T10:00:00Z"
# end_time = "2020-07-15T15:00:00Z"

# #Rämö 257 km 
# start_time = "2015-05-30T10:00:00Z"
# end_time = "2015-05-30T15:00:00Z"

# #Rämö 201 km 
# start_time = "2014-05-17T10:00:00Z"
# end_time = "2014-05-17T15:00:00Z"


# #Kumpulainen 296 km 
# start_time = "2022-04-27T10:00:00Z"
# end_time = "2022-04-27T15:00:00Z"

# #Kumpulainen 267 km 
# start_time = "2022-04-29T10:00:00Z"
# end_time = "2022-04-29T15:00:00Z"

# #Kumpulainen 160 km FAI 
# start_time = "2021-06-07T10:00:00Z"
# end_time = "2021-06-07T15:00:00Z"


# #Hamne 160 km FAI 
# start_time = "2020-05-22T10:00:00Z"
# end_time = "2020-05-22T15:00:00Z"

# #Keinanen 208 km 
# start_time = "2022-05-20T10:00:00Z"
# end_time = "2022-05-20T15:00:00Z"

# #Haastava Elokuinen keli  
# start_time = "2022-08-14T10:00:00Z"
# end_time = "2022-08-14T15:00:00Z"

# #Junnonaho 231 km 
# start_time = "2020-05-23T10:00:00Z"
# end_time = "2020-05-23T15:00:00Z"

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                args=["starttime=" + start_time,
                                        "endtime=" + end_time,
                                        "place=Jokioinen"])



for sounding in soundings:
    plot_sounding(sounding)

def plot_sounding(sounding):

    sounding = snd.soundings[0]


    p = sounding.pressures * units.hPa
    T = sounding.temperatures * units.degC
    Td = sounding.dew_points * units.degC
    wind_speed = sounding.wind_speeds * units('m/s')
    wind_dir = sounding.wind_directions * units.degrees
    u, v = mpcalc.wind_components(wind_speed, wind_dir)

    ###########################################
    # Create a new figure. The dimensions here give a good aspect ratio.

    fig = plt.figure(figsize=(9, 9))
    add_metpy_logo(fig, 115, 100)
    skew = SkewT(fig, rotation=45)

    # Plot the data using normal plotting functions, in this case using
    # log scaling in Y, as dictated by the typical meteorological plot.
    skew.plot(p, T, 'r')
    skew.plot(p, Td, 'g')
    #skew.plot_barbs(p, u, v)
    # Plot the wind barbs from the original data
    skew.plot_barbs(p[::10], u[::10], v[::10])
    skew.ax.set_ylim(1000, 100)
    skew.ax.set_xlim(-40, 60)

    # Set some better labels than the default
    skew.ax.set_xlabel(f'Temperature ({T.units:~P})')
    skew.ax.set_ylabel(f'Pressure ({p.units:~P})')

    # Calculate LCL height and plot as black dot. Because `p`'s first value is
    # ~1000 mb and its last value is ~250 mb, the `0` index is selected for
    # `p`, `T`, and `Td` to lift the parcel from the surface. If `p` was inverted,
    # i.e. start from low value, 250 mb, to a high value, 1000 mb, the `-1` index
    # should be selected.
    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
    skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')

    # Calculate full parcel profile and add to plot as black line
    prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
    skew.plot(p, prof, 'k', linewidth=2)

    # Shade areas of CAPE and CIN
    skew.shade_cin(p, T, prof, Td)
    skew.shade_cape(p, T, prof)

    # An example of a slanted line at constant T -- in this case the 0
    # isotherm
    skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)

    # Add the relevant special lines
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()

    # Add some titles
    plt.title(sounding.name, loc='left')
    plt.title(sounding.nominal_time, loc='right')

    # Show the plot
    plt.show()
