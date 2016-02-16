import csv
import requests
import json

#create text file to store names that couldn't be matched
with open("human_brain_needed.csv", "w") as text_file:
	pass

#create csv file to store matches
with open("geonameIDs.csv", "w") as outfile:
	pass

with open("FlorentineDrawings.csv", "r") as csvfile:
	lines = csv.reader(csvfile)
	next(lines)
	
	#my API key
	token = #yourtokenhere
	
	#lists to store information later on
	unique_cities = []
	no_matches = []
	still_no_matches = []
	
	for a_line in lines:
		city = a_line[2].strip()
		country = a_line[3].strip()
		
		#need to account for discrepancies in the data
		if "United States" in country:
			country = "United States"
		if "Holland" in country:
			country = "Netherlands"
		if country == "UK":
			country = "United Kingdom"
		if city == '':
			pass
		else:
			#if statement to skip any cities that have already been successfully looked up
			if city in unique_cities:
				pass
			
			else:
				try:
					#do exact name match with only best match returned
					payload = {'name_equals': city, 'maxRows': 1, 'username': token}
					r = requests.get('http://api.geonames.org/searchJSON?', params=payload)
					data = json.loads(r.text)

					try:
						#if country in csv matches country in geonames match...
						if country == data['geonames'][0]['countryName']:

							#open and append the final csv with data
							with open("geonameIDs.csv", "a") as outfile:
								writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

								city_uri = "http://sws.geonames.org/" + str(data['geonames'][0]['geonameId'])
								country_uri = "http://sws.geonames.org/" + str(data['geonames'][0]['countryId'])

								writer.writerow([city, city_uri, country, country_uri])
								
								#keep list of cities already found
								unique_cities.append(city) 
						else:
							#keep city/country not matched in seperate list for later
							roundabout = city+","+country
							no_matches.append(roundabout)
							
					except:
						#keep city/country not matched in seperate list for later
						roundabout = city+","+country
						no_matches.append(roundabout)
						
				except:
					print("couldn't request!")
	
	#loop through cities that didn't match immediately
	for match in no_matches:
		#split the cities and countries
		city_try = match.split(",")[0]
		country_try = match.split(",")[1]

		try:
			#this time general search for names and return 5 best results
			payload = {'name': city_try, 'maxRows': 5, 'username': token}
			r = requests.get('http://api.geonames.org/searchJSON?', params=payload)
			data = json.loads(r.text)

			
			for stuff in data['geonames']:
				if city_try in unique_cities:
					pass
				else:
					#if second attempt makes any matches, write to text file for further confirmation
					if country_try == stuff['countryName']:
						with open("human_brain_needed.csv", "a") as text_file:
							writer = csv.writer(text_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
							writer.writerow([city_try,country_try, str(stuff['geonameId'])])
							unique_cities.append(city_try)
					else:
						still_no_matches.append(city_try+","+country_try) 
		except:
			print("still couldn't request!")

	#finally print a list of the difference between two no match lists to get cities that didn't get looked up
	still_no_matches = set(still_no_matches)
	for place in still_no_matches:
		print (place)

