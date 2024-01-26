from cmath import nan
from fileinput import FileInput
import requests
import pandas as pd
import json
import os
import numpy as np
#################

# url = "https://www.huduser.gov/hudapi/public/usps"

# r = requests.get(url + )

# return a Pandas Dataframe of HUD USPS Crosswalk values

# Note that type is set to 1 which will return values for the ZIP to Tract file and query is set to VA which will return Zip Codes in Virginia

crosswalkType = "2"
crosswalkCharType = "ZipToCounty"

crosswalkQuery = "NY"

url = "https://www.huduser.gov/hudapi/public/usps?type=" + crosswalkType + "&query=" + crosswalkQuery

token = "TOKEN"

headers = {"Authorization": "Bearer {0}".format(token)}

response = requests.get(url, headers = headers)

if response.status_code != 200:
	print ("Failure, see status code: {0}".format(response.status_code))
else: 
	df = pd.DataFrame(response.json()["data"]["results"])	
	print(df);

# Remove duplicate values with less than half of addresses in County
df2 = df[df['tot_ratio'] > 0.5] 

# Assign Regions
regionDict = {'North Country': ["36045", "36049", "36089", "36033", "36019", "36041", "36031"],
	'Western New York': ["36063", "36029", "36013", "36009", "36003"],
	'Finger Lakes': ["36073", "36037", "36121", "36055", "36051", "36117", "36069", "36123", "36099"],
	'Central New York': ["36075", "36011", "36067", "36023", "36053"],
	'Mohawk Valley': ["36065", "36043", "36077", "36035", "36057", "36095"],
	'Capital Region': ["36113", "36091", "36093", "36001", "36039", "36115", "36083", "36021"],
	'Southern Tier': ["36101", "36097","36015", "36109", "36107", "36017", "36007", "36025"],
	'Mid-Hudson': ["36105", "36111", "36071", "36027", "36079", "36119", "36087"],
	'New York City': ["36005", "36061", "36081", "36085", "36047"],
	'Long Island': ["36059", "36103"],
    }
# dfRegion = pd.DataFrame(data=regionDict)

regionDict2 = { "36045": 'North Country',
			    "36049": 'North Country',
				"36089": 'North Country',
				"36033": 'North Country',
				"36019": 'North Country',
				"36041": 'North Country',
				"36031": 'North Country',
				"36063": 'Western New York',
				"36029": 'Western New York',
				"36013": 'Western New York',
				"36009": 'Western New York',
				"36003": 'Western New York',
				"36073": 'Finger Lakes',
				"36037": 'Finger Lakes',
				"36121": 'Finger Lakes',
				"36055": 'Finger Lakes',
				"36051": 'Finger Lakes',
				"36117": 'Finger Lakes',
				"36069": 'Finger Lakes',
				"36123": 'Finger Lakes',
				"36099": 'Finger Lakes',
				"36075": 'Central New York',
				"36011": 'Central New York',
				"36067": 'Central New York',
				"36023": 'Central New York',
				"36053": 'Central New York',
				"36065": 'Mohawk Valley',
				"36043": 'Mohawk Valley',
				"36077": 'Mohawk Valley',
				"36035": 'Mohawk Valley',
				"36057": 'Mohawk Valley',
				"36095": 'Mohawk Valley',
				"36113": 'Capital Region',
				"36091": 'Capital Region',
				"36093": 'Capital Region',
				"36001": 'Capital Region',
				"36039": 'Capital Region',
				"36115": 'Capital Region',
				"36083": 'Capital Region',
				"36021": 'Capital Region',
				"36101": 'Southern Tier',
				"36097": 'Southern Tier',
				"36015": 'Southern Tier',
				"36109": 'Southern Tier',
				"36107": 'Southern Tier',
				"36017": 'Southern Tier',
				"36007": 'Southern Tier',
				"36025": 'Southern Tier',
				"36105": 'Mid-Hudson',
				"36111": 'Mid-Hudson',
				"36071": 'Mid-Hudson',
				"36027": 'Mid-Hudson',
				"36079": 'Mid-Hudson',
				"36119": 'Mid-Hudson',
				"36087": 'Mid-Hudson',
				"36005": 'New York City',
				"36061": 'New York City',
				"36081": 'New York City',
				"36085": 'New York City',
				"36047": 'New York City',
				"36059": 'Long Island',
				"36103": 'Long Island'
}

regionDict3 = { "North Country": '1',
			    "Western New York": '2',
				"Finger Lakes": '3',
				"Central New York": '4',
				"Mohawk Valley": '5',
				"Capital Region": '6',
				"Southern Tier": '7',
				"Mid-Hudson": '8',
				"New York City": '9',
				"Long Island": '10',
}

df2['region'] = df2['geoid'] 

# df['region'].replace({'apple': 'fruit', 'banana': 'fruit', 'orange': 'citrus'}, inplace=True)

# df2.loc[df2['region'] == ["36045", "46049", "36089", "36033", "36019", "36041", "36031"], 'region'] = 'North Country'


# df2['region'] = np.where(df['geoid']!= "36045", 'North Country', "")

# df2.loc[df2['geoid'].isin(regionDict.values()), 'col2'] = df2['geoid'].map(regionDict)

# df2['region'].update(pd.Series(regionDict2))

df3 = df2.replace({'region': regionDict2})

df3['regionCategorical'] = df3['region'] 

df4 = df3.replace({'regionCategorical': regionDict3})

# for row in df2:
# 	for key, value in regionDict.items():
# 		if row[1] in value:
# 			row['region'] = key

# for index, row in df2.oterrows:
# 	print (row)
	# for key, value in regionDict.items():
	# 	if row[1] in value:
	# 		row['region'] = key
			
# for key, value in regionDict.items():
# 	print(key, value)
# 	if '36105' in value:
# 		print(key)

# df2.loc[df2['geoid'].eq(regionDict.values()).all(1), '']

path = r'PATH'

filename = crosswalkQuery + crosswalkCharType + '.csv'

df4.to_csv(path + filename,
                  index=False)
