# Download satellite data from Celestrak using Python
import requests

# Get the URL for all active satellites
# This is the web address where Celestrak stores current satellite data
url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

# Download the data
# Send a request to the website and get the satellite information
print("Downloading satellite data...")
response = requests.get(url)

# Save it to a file called satellites.txt
# Write all the satellite data to a text file on your computer
with open("satellites.txt", "w") as file:
    file.write(response.text)

print("Done! Check satellites.txt for your data.")