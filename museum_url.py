import csv

# make drawing ID into URI
# add schema.org has URL
# add URL


# FlorentineDrawingsTripleRecto = 0
# FlorentineDrawingsTripleVerso = 0
FlorentineDrawingsQuads = []

with open('FlorentineDrawings_FilippinoBotticelli_CaseStudy - Sheet1.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]

		Museum_Link_Recto = row[5]
		
		Museum_Link_Verso = row[6]

		FlorentineDrawingsURIrecto = "<http://data.itatti.harvard.edu/florentinedrawings/"+FlorentineDrawings_IdentifierBB1961+"/recto>"
		#print(FlorentineDrawingsURIrecto)
		FlorentineDrawingsURIverso = "<http://data.itatti.harvard.edu/florentinedrawings/"+FlorentineDrawings_IdentifierBB1961+"/verso>"
		#print(FlorentineDrawingsURIrecto)

		if Museum_Link_Recto != "":
			FlorentineDrawingsTripleRecto = FlorentineDrawingsURIrecto+"<http://schema.org/url>"+"<"+Museum_Link_Recto+">"
			#print(FlorentineDrawingsTripleRecto)
			FlorentineDrawingsQuads.append(FlorentineDrawingsTripleRecto+"<http://data.itatti.harvard.edu/florentinedrawings/project2016>."+"\n")
		if Museum_Link_Verso != "":
			FlorentineDrawingsTripleVerso = FlorentineDrawingsURIverso+"<http://schema.org/url>"+"<"+Museum_Link_Verso+">"
			#print(FlorentineDrawingsTripleVerso)
			FlorentineDrawingsQuads.append(FlorentineDrawingsTripleVerso+"<http://data.itatti.harvard.edu/florentinedrawings/project2016>."+"\n")

#print(FlorentineDrawingsTriples)

with open ('museum_links.nt', 'w') as museum_links_file:
	museum_links_file.writelines(FlorentineDrawingsQuads)