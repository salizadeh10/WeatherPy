
# coding: utf-8

# # WeatherPy
# ----
# 
# ### Analysis
# * As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
# * There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
# * There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.
# 
# ---
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[161]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import datetime as dt 

from pprint import pprint

# Import API key
from config import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[162]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# In[163]:


# set up the url address
url = "http://api.openweathermap.org/data/2.5/weather?"

# set up lists to hold reponse info
City        = []
Cloudiness  = []
Country     = []
Date        = []
Humidity    = []
Lat         = []
Lng         = []
Max_Temp    = []
Wind_Speed  = []

# for each of the city from the list genereated
for city in cities:
    print("Extracting data for " + city)
    
    # handle key errors.  Weather API may not have information on some of 
    # random cities genereated above. 
    try:
        # get the weather data using the city as key 
        # temperature unit in Fahrenheit
        query_url = url + "appid=" + api_key + "&q=" + city + "&units=imperial"
        weather_response = requests.get(query_url)
        data = weather_response.json()

        # extract from data received and populate the lists
        City.append(data['name'])
        Cloudiness.append(data['clouds']['all'])
        Country.append(data['sys']['country'])
        Date.append(data['dt'])
        Humidity.append(data['main']['humidity'])
        Lat.append(data['coord']['lat'])
        Lng.append(data['coord']['lon'])
        Max_Temp.append(data['main']['temp_max'])
        Wind_Speed.append(data['wind']['speed'])
    
    except KeyError:
        print("No information on " + city)


# In[168]:


# create a data frame from cities, lat, and temp
weather_dict = {
    'city': City,
    'cloudiness': Cloudiness,
    'country': Country,
    'date': Date,
    'humidity': Humidity,
    'lat': Lat,
    'lng': Lng,
    'max_temp': Max_Temp,
    'wind_speed': Wind_Speed
}

weather_df = pd.DataFrame(weather_dict)
weather_df.head()

print("We have weather information on " + str(weather_df.shape[0]) + " cities")
weather_df.head()


# In[172]:


# Save the data in csv file
# Note to avoid any issues later, use encoding="utf-8"
weather_df.to_csv("weather_data.csv", encoding="utf-8", index=False)


# In[183]:


#  --------------  Latitude vs. Temperature Plot  --------------------

# x_axis ==> Latitude
# y_axis ==> Max Temperature (F)

plt.scatter(weather_df['lat'], weather_df['max_temp'], edgecolors="black",
            marker="o", alpha=0.7, facecolors="blue")

# cosmatic stuff
todays_date = dt.datetime.today().strftime("%m/%d/%Y")
plt.title("City Latitude vs. Temperature (" + todays_date + ")")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")
plt.grid(True)

# Save Figure
plt.savefig("City_Latitude_vs_Temperature.png")
plt.show()


# In[184]:


#  --------------  Latitude vs. Humidity Plot  --------------------

# x_axis ==> Latitude
# y_axis ==> Humidity (%)

plt.scatter(weather_df['lat'], weather_df['humidity'], edgecolors="black",
            marker="o", alpha=0.7, facecolors="blue")

# cosmatic stuff
todays_date = dt.datetime.today().strftime("%m/%d/%Y")
plt.title("City Latitude vs. Humidity (" + todays_date + ")")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.grid(True)

# Save Figure
plt.savefig("City_Latitude_vs_Humidity.png")
plt.show()


# In[185]:


#  --------------  Latitude vs. Cloudiness Plot  --------------------

# x_axis ==> Latitude
# y_axis ==> Cloudiness (%)

plt.scatter(weather_df['lat'], weather_df['cloudiness'], edgecolors="black",
            marker="o", alpha=0.7, facecolors="blue")

# cosmatic stuff
todays_date = dt.datetime.today().strftime("%m/%d/%Y")
plt.title("City Latitude vs. Cloudiness (" + todays_date + ")")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.grid(True)

# Save Figure
plt.savefig("City_Latitude_vs_Cloudiness.png")
plt.show()


# In[186]:


#  --------------  Latitude vs. Wind Speed Plot  --------------------

# x_axis ==> Latitude
# y_axis ==> Wind Speed (%)

plt.scatter(weather_df['lat'], weather_df['wind_speed'], edgecolors="black",
            marker="o", alpha=0.7, facecolors="blue")

# cosmatic stuff
todays_date = dt.datetime.today().strftime("%m/%d/%Y")
plt.title("City Latitude vs. Wind Speed (" + todays_date + ")")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.grid(True)

# Save Figure
plt.savefig("City_Latitude_vs_Wind_Speed.png")
plt.show()


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[6]:





# #### Latitude vs. Humidity Plot

# In[7]:





# #### Latitude vs. Cloudiness Plot

# In[8]:





# #### Latitude vs. Wind Speed Plot

# In[9]:





# In[174]:


get_ipython().system('jupyter nbconvert --to script WeatherPy.ipynb')

