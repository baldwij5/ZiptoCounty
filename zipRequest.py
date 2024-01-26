from cmath import nan
from fileinput import FileInput
import requests
import pandas as pd
import json
import os
import numpy as np
#################

## Source: https://www.huduser.gov/portal/dataset/uspszip-api.html


hudToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiNGFmMzE3ZjYyODg3ZDEzN2Y0NjM5NmNlOGNhZGFlOGMzMGE5NTFjNWFmYWQyNGU0ZDkzNDZlMDY4ZjU5OTUwOTE2YzM2MmNmNmYyNjRiOTYiLCJpYXQiOjE3MDYyODIxNDguMzQ5OTQzLCJuYmYiOjE3MDYyODIxNDguMzQ5OTQ1LCJleHAiOjIwMjE5MDEzNDguMzQ2MDk5LCJzdWIiOiI2NTAwMyIsInNjb3BlcyI6W119.Gw86lTFmAr6A0IHpL2ehyY4FdELLp6jfXVrfRaAY09NWB9EpWlTDUQKndXyc4e78r7VTRWaPUJ1eve5YSgV71A"

# url = "https://www.huduser.gov/hudapi/public/usps"

# r = requests.get(url + )

# return a Pandas Dataframe of HUD USPS Crosswalk values

# Note that type is set to 1 which will return values for the ZIP to Tract file and query is set to VA which will return Zip Codes in Virginia
url = "https://www.huduser.gov/hudapi/public/usps?type=1&query=VA"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiNGFmMzE3ZjYyODg3ZDEzN2Y0NjM5NmNlOGNhZGFlOGMzMGE5NTFjNWFmYWQyNGU0ZDkzNDZlMDY4ZjU5OTUwOTE2YzM2MmNmNmYyNjRiOTYiLCJpYXQiOjE3MDYyODIxNDguMzQ5OTQzLCJuYmYiOjE3MDYyODIxNDguMzQ5OTQ1LCJleHAiOjIwMjE5MDEzNDguMzQ2MDk5LCJzdWIiOiI2NTAwMyIsInNjb3BlcyI6W119.Gw86lTFmAr6A0IHpL2ehyY4FdELLp6jfXVrfRaAY09NWB9EpWlTDUQKndXyc4e78r7VTRWaPUJ1eve5YSgV71A"
headers = {"Authorization": "Bearer {0}".format(token)}

response = requests.get(url, headers = headers)

if response.status_code != 200:
	print ("Failure, see status code: {0}".format(response.status_code))
else: 
	df = pd.DataFrame(response.json()["data"]["results"])	
	print(df);

####################
## TYPE of Crosswalk##
####################

# REQUIRED; Must be a number between 1 and 12 depending on the Crosswalk type.

# zip-tract
# zip-county
# zip-cbsa
# zip-cbsadiv (Available 4th Quarter 2017 onwards)
# zip-cd
# tract-zip
# county-zip
# cbsa-zip
# cbsadiv-zip (Available 4th Quarter 2017 onwards)
# cd-zip
# zip-countysub (Available 2nd Quarter 2018 onwards)
# countysub-zip (Available 2nd Quarter 2018 onwards)

####################
## Query ##
####################

# REQUIRED;

# 5 digit USPS ZIP code of the data to retrieve. E.g. 22031 for type 1 to 5 and 11 .
# or
# 11 digit unique 2000 or 2010 Census tract GEOID consisting of state FIPS + county FIPS + tract code. Eg: 51059461700  for type 6
# or
# 5 digit unique 2000 or 2010 Census county GEOID consisting of state FIPS + county FIPS. Eg: 51600 for type 7
# or
# 5 digit CBSA code for Micropolitan and Metropolitan Areas Eg: 10380 for type 8
# or
# 5-dgit CBSA Division code which only applies to Metropolitan Areas. Eg: 35614 for type 9
# or
# 4-digit GEOID for the Congressional District which consists of state FIPS + Congressional District code. Eg: 7200 for type 10
# or
# 10-digit GEOID for the County sub Eg: 4606720300 for type 12
# or
# 2-letter state code for state level data - (Available 1st Quarter 2021 onwards for all types , 1 to 12)
# or
# The word "All" for the entire file - (Available 1st Quarter 2021 onwards for all types, 1 to 12)

####################
## Year ##
####################

# Year of the data to retrieve E.g. 2017. Default is latest year. Optional

####################
## Quarter ##
####################

# Quarter of the year. Number between 1 and 4. Default is latest quarter. Optional