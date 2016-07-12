import csv

# make drawing ID into URI
# add schema.org has URL
# add URL


# FlorentineDrawingsTripleRecto = 0
# FlorentineDrawingsTripleVerso = 0
FlorentineDrawingsQuads = []

with open('FlorentineDrawings_SpreadsheetsCombined_v5 - FlorentineDrawings_CombinedSpreadsheets.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]

		Object_repository_URI_corrected = row[12]

		FlorentineDrawingsURI = "<http://data.itatti.harvard.edu/florentinedrawings/"+FlorentineDrawings_IdentifierBB1961+">"
		#print(FlorentineDrawingsURI)
		
		if Object_repository_URI_corrected != "":
			FlorentineDrawingsTriple = FlorentineDrawingsURI+"<http://www.w3.org/2002/07/owl#sameAs>"+"<"+Object_repository_URI_corrected+">"
			#print(FlorentineDrawingsTripleRecto)
			FlorentineDrawingsQuads.append(FlorentineDrawingsTriple+"<http://data.itatti.harvard.edu/florentinedrawings/project2016>."+"\n")

#print(FlorentineDrawingsTriples)

with open ('BM_URIs.nt', 'w') as BM_URIs_file:
	BM_URIs_file.writelines(FlorentineDrawingsQuads)