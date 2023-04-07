import argparse
import json
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='Name of the input file')
args = parser.parse_args()

with open(args.filename) as f:
    data = json.load(f)

temps = []
heights = []
dewpoint = []

for feature in data['features']:
    if 'temp' in feature['properties']:
        temp = feature['properties']['temp'] - 273.15
        height = feature['properties']['gpheight']
        if height <= 3500:
            temps.append(temp)
            heights.append(height)
        if 'dewpoint' in feature['properties'] and height <= 3500:
            dewpoint.append(feature['properties']['dewpoint'] - 273.15)

plt.plot(temps, heights, label='Temperature', color='red')
plt.plot(dewpoint, heights, label='Dew Point', color='blue')
plt.xlabel('Temperature/Dew Point')
plt.ylabel('GP Height')
plt.title('GP Height vs Temperature/Dew Point')
plt.legend()
plt.ylim(0, 3500)

plt.show()