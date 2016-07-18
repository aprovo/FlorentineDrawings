import csv

# make drawing ID into URI
# add schema.org has URL
# add URL


# FlorentineDrawingsTripleRecto = 0
# FlorentineDrawingsTripleVerso = 0
FlorentineDrawings1961Quads = []
FlorentineDrawings1938Quads = []
FlorentineDrawings1903Quads = []


with open('FlorentineDrawings_PageNumbers - MasterList.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]

		BB_1961_FirstPageNumber = row[2]
		
		BB_1961_LastPageNumber = row[3]
		
		BB_1938_FirstPageNumber = row[5]
		
		BB_1938_LastPageNumber = row[6]

		BB_1903_FirstPageNumber = row[8]
		
		BB_1903_LastPageNumber = row[9]

		FlorentineDrawingsURI = "<http://data.itatti.harvard.edu/florentinedrawings/"+FlorentineDrawings_IdentifierBB1961+">"


		if BB_1961_FirstPageNumber != "":
			FlorentineDrawingsTriple1961 = FlorentineDrawingsURI+"<http://dbpedia.org/ontology/atPage>"+'"'+BB_1961_FirstPageNumber+'"'
			#print(FlorentineDrawingsTripleRecto)
			FlorentineDrawings1961Quads.append(FlorentineDrawingsTriple1961+"<http://data.itatti.harvard.edu/florentinedrawings/berenson1961>."+"\n")

		if BB_1938_FirstPageNumber != "":
			FlorentineDrawingsTriple1938 = FlorentineDrawingsURI+"<http://dbpedia.org/ontology/atPage>"+'"'+BB_1938_FirstPageNumber+'"'
			#print(FlorentineDrawingsTripleRecto)
			FlorentineDrawings1938Quads.append(FlorentineDrawingsTriple1938+"<http://data.itatti.harvard.edu/florentinedrawings/berenson1938>."+"\n")

		if BB_1903_FirstPageNumber != "":
			FlorentineDrawingsTriple1903 = FlorentineDrawingsURI+"<http://dbpedia.org/ontology/atPage>"+'"'+BB_1903_FirstPageNumber+'"'
			#print(FlorentineDrawingsTripleRecto)
			FlorentineDrawings1903Quads.append(FlorentineDrawingsTriple1903+"<http://data.itatti.harvard.edu/florentinedrawings/berenson1903>."+"\n")

#print(FlorentineDrawings1961Quads)

with open ('page_numbers1961.nt', 'w') as page_numbers_file:
	page_numbers_file.writelines(FlorentineDrawings1961Quads)

with open ('page_numbers1938.nt', 'w') as page_numbers_file:
	page_numbers_file.writelines(FlorentineDrawings1938Quads)

with open ('page_numbers1903.nt', 'w') as page_numbers_file:
	page_numbers_file.writelines(FlorentineDrawings1903Quads)