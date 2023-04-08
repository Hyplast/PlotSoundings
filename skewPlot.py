
from fmiopendata.wfs import download_stored_query
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from metpy.plots import SkewT

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                            ["place=Jokioinen"])

sounding = snd.soundings[0]

fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig)#, rotation=45)

print(type(sounding.pressures))
print(type(sounding.wind_speeds))


# Add the data
skew.plot(sounding.pressures, sounding.temperatures, 'r')
skew.plot(sounding.pressures, sounding.dew_points, 'g')

# Set some appropriate axes limits
skew.ax.set_ylim(1000, 700)
skew.ax.set_xlim(-40, 60)

# Add the relevant special lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()

# Add inset axes
#ax2 = inset_axes(skew.ax, '100%', '100%', loc='lower left', bbox_to_anchor=(0.6, 0.2), bbox_transform=skew.ax.transAxes)
#skew.plot_barbs(sounding.pressures, sounding.wind_speeds, sounding.wind_directions)
#skew.ax.set_ylim(1000, 700)

# Add wind barbs
#ax2 = inset_axes(skew.ax, '100%', '100%', loc='lower left', bbox_to_anchor=(0.6, 0.2), bbox_transform=skew.ax.transAxes)
#ax2.barbs(sounding.wind_speeds.to('knots').m, sounding.pressures.mbar.values,
#          sounding.wind_directions.to('knots').m, sounding.wind_speeds.to('knots').m,
#          length=6)


# Add titles and labels
plt.title('Skew-T Log-P Diagram')
plt.xlabel('Temperature (C)')
plt.ylabel('Pressure (hPa)')


plt.show()

""" 
fig = plt.figure(figsize=(9, 9))
skew = SkewT(fig)

# Plot data
skew.plot(pressure, temperature, 'r')
skew.plot(pressure, dewpoint, 'g')

# Add legend
plt.legend(['Temperature', 'Dew Point'], loc='upper right')

# Add inset axes
ax2 = inset_axes(skew.ax, '100%', '100%', loc='lower left', bbox_to_anchor=(0.6, 0.2), bbox_transform=skew.ax.transAxes)
skew.plot_barbs(pressure_levels, u_wind, v_wind)
skew.ax.set_ylim(1000, 100)

# Add titles and labels
plt.title('Skew-T Log-P Diagram')
plt.xlabel('Temperature (C)')
plt.ylabel('Pressure (hPa)')

plt.show() """