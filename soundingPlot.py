import metpy.calc as mpcalc
from metpy.plots import SkewT
from metpy.units import units
import matplotlib.pyplot as plt
from fmiopendata.wfs import download_stored_query

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                            ["place=Jokioinen"])

sounding = snd.soundings[0]
sounding.name  # Name of the sounding station
sounding.id  # Station ID of the sounding station
sounding.nominal_time  # Nominal time of the sounding
sounding.altitudes  # Numpy array of the measurement location altitudes [m]
sounding.times  # Numpy array of the measurement times [datetime]
sounding.temperatures  # Numpy array of measured temperatures [°C]
sounding.dew_points  # Numpy array of measured dew points [°C]
sounding.wind_speeds  # Numpy array of measured wind speeds [m/s]
sounding.wind_directions  # Numpy array of measured wind directions [°]

fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig)

# Plot the data using normal plotting functions, in this case using
# log scaling in Y, as dictated by the typical meteorological plot
skew.plot(sounding.times, sounding.pressures / units.hPa, 'r')
skew.plot(sounding.times, sounding.dew_points / units.degC, 'b')
skew.plot(sounding.times, sounding.temperatures / units.degC, 'r')

# Calculate LCL height and plot as black dot
lcl_pressure, lcl_temperature = mpcalc.lcl(sounding.pressures[0],
                                            sounding.temperatures[0],
                                            sounding.dew_points[0])
lcl_altitude = mpcalc.pressure_to_height_std(lcl_pressure)
skew.ax.plot(sounding.times[0], lcl_pressure.to('hPa'), 'ko', markerfacecolor='black')

# Calculate full parcel profile and add to plot as black line
prof = mpcalc.parcel_profile(sounding.pressures,
                             sounding.temperatures[0],
                             sounding.dew_points[0]).to('degC')
skew.plot(sounding.times, sounding.pressures / units.hPa, prof, 'k', linewidth=2)

# An example of a slanted line at constant T -- in this case the 0
# isotherm
skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)

# Add the relevant special lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

plt.show()