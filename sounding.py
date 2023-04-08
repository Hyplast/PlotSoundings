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
from datetime import datetime


class Sounding:
    def __init__(self, date:str = "01.01.2022", place:str = "Jokioinen"):
        self.date = date
        self.place = place
    
    def fetchSounding(self):
        start_time = datetime.strptime(self.date, '%d.%m.%Y').strftime('%Y-%m-%dT00:00:00Z')
        end_time = datetime.strptime(self.date, '%d.%m.%Y').strftime('%Y-%m-%dT24:00:00Z')
        snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                    args=["starttime=" + start_time,
                                            "endtime=" + end_time,
                                            "place=" + self.place])
        return snd

        

    def plotSounding(self, sounding):
        p = sounding.pressures * units.hPa
        a = sounding.altitudes * units.meters
        T = sounding.temperatures * units.degC
        Td = sounding.dew_points * units.degC
        wind_speed = (sounding.wind_speeds * 2) * units('m/s')
        wind_dir = sounding.wind_directions * units.degrees
        u, v = mpcalc.wind_components(wind_speed, wind_dir)

        ###########################################
        # Create a new figure. The dimensions here give a good aspect ratio.

        fig = plt.figure(figsize=(10, 20))
        #add_metpy_logo(fig, 115, 100)
        skew = SkewT(fig, rotation=45)

        # Plot the data using normal plotting functions, in this case using
        # log scaling in Y, as dictated by the typical meteorological plot.
        skew.plot(p, T, 'r')
        skew.plot(p, Td, 'g')
        #skew.plot_barbs(p, u, v)
        # Plot the wind barbs from the original data
        skew.plot_barbs(p[::10], u[::10], v[::10])
        skew.ax.set_ylim(1050, 600)
        skew.ax.set_xlim(-15, 30)

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
