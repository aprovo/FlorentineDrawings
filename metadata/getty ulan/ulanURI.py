import csv
import requests
import json


####THIS WILL FIND ULAN URI#####
#create csv file to store matches
with open("ulanURIs.csv", "w") as outfile:
	pass

with open('florentine_drawings_for_ulan.csv', 'r') as csvfile:
	lines = csv.reader(csvfile)
	next(lines)

	unique_names = []

	for a_line in lines:

		name_1961 = a_line[15]
		viafURI_1961 = a_line[16]
		viafURIJSON_1961 = viafURI_1961 + "justlinks-json"

		name_1938 = a_line[33]
		viafURI_1938 = a_line[34]
		viafURIJSON_1938 = viafURI_1938 + "justlinks-json"

		name_1903 = a_line[41]
		viafURI_1903 = a_line[42]
		viafURIJSON_1903 = viafURI_1903+"justlinks-json"

		if name_1961 == "":
			
			pass
		else:

			if name_1961 in unique_names:
				pass


			
			else:
				#requests JSON data from API
				try:
					r = requests.get(viafURIJSON_1961)

					#takes the API response and turn it into JSON
					response = json.loads(r.text)

					#Loop through JSON to find ULAN which is abbreviated "JPG" for some reason
					try:
						for entry in response['JPG']:

							#this is the ulan id
							ulanID = entry

							#add URI info to beginning of ID to get final URI
							ulanURI = "http://vocab.getty.edu/ulan/"+ulanID 
							
							with open("ulanURIs.csv", "a") as outfile:
								writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

								writer.writerow([name_1961,ulanURI])

								unique_names.append(name_1961)

					except:
						print (name_1961 + ';' +'no ULAN')
						unique_names.append(name_1961)
				except:
					print (name_1961)
		if name_1938 == "":
			
			pass
		else:

			if name_1938 in unique_names:
				pass


			
			else:
				#requests JSON data from API
				try:
					r = requests.get(viafURIJSON_1938)

					#takes the API response and turn it into JSON
					response = json.loads(r.text)

					#Loop through JSON to find ULAN which is abbreviated "JPG" for some reason
					try:
						for entry in response['JPG']:

							#this is the ulan id
							ulanID = entry

							#add URI info to beginning of ID to get final URI
							ulanURI = "http://vocab.getty.edu/ulan/"+ulanID 
							
							with open("ulanURIs.csv", "a") as outfile:
								writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

								writer.writerow([name_1938,ulanURI])

								unique_names.append(name_1938)

					except:
						print (name_1938 + ';' +'no ULAN')
						unique_names.append(name_1938)
				except:
					print (name_1938)
		if name_1903 == "":
			
			pass
		else:

			if name_1903 in unique_names:
				pass


			
			else:
				#requests JSON data from API
				try:
					r = requests.get(viafURIJSON_1903)

					#takes the API response and turn it into JSON
					response = json.loads(r.text)

					#Loop through JSON to find ULAN which is abbreviated "JPG" for some reason
					try:
						for entry in response['JPG']:

							#this is the ulan id
							ulanID = entry

							#add URI info to beginning of ID to get final URI
							ulanURI = "http://vocab.getty.edu/ulan/"+ulanID 
							
							with open("ulanURIs.csv", "a") as outfile:
								writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

								writer.writerow([name_1903,ulanURI])

								unique_names.append(name_1903)

					except:
						print (name_1903 + ';' +'no ULAN')
						unique_names.append(name_1903)
				except:
					print (name_1903)


