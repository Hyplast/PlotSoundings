from fmiopendata.wfs import download_stored_query
import json
import matplotlib.pyplot as plt

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                            ["place=Jokioinen"])

sounding = snd.soundings[0]
# sounding.name  # Name of the sounding station
# sounding.id  # Station ID of the sounding station
# sounding.nominal_time  # Nominal time of the sounding
# sounding.altitudes  # Numpy array of the measurement location altitudes [m]
# sounding.times  # Numpy array of the measurement times [datetime]
# sounding.temperatures  # Numpy array of measured temperatures [°C]
# sounding.dew_points  # Numpy array of measured dew points [°C]
# sounding.wind_speeds  # Numpy array of measured wind speeds [m/s]
# sounding.wind_directions  # Numpy array of measured wind directions [°]

temps = sounding.temperatures
heights = sounding.altitudes
dewpoint = sounding.dew_points

plt.plot(temps, heights, label='Temperature', color='red')
plt.plot(dewpoint, heights, label='Dew Point', color='blue')
plt.xlabel('Temperature/Dew Point')
plt.ylabel('Height [m]')
plt.title(sounding.name + " " + sounding.nominal_time )
plt.legend()
plt.ylim(0, 3500)

plt.show()