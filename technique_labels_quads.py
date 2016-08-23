import csv

# make drawing ID into URI
# add schema.org has URL
# add URL


# FlorentineDrawingsTripleRecto = 0
# FlorentineDrawingsTripleVerso = 0
TechniqueQuads = []

with open('FlorentineDrawings_SpreadsheetsCombined_v5 - Unique Technique Terms.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		TechniqueLabel = row[0]

		TechniqueURI = row[1]
		

		TechniqueTriple = "<"+ TechniqueURI + ">" + "<http://www.w3.org/2000/01/rdf-schema#label>"+ '"'+TechniqueLabel+'"'
			#print(FlorentineDrawingsTripleRecto)
		TechniqueQuads.append(TechniqueTriple + "<http://data.itatti.harvard.edu/florentinedrawings/project2016>."+"\n")


#print(FlorentineDrawingsTriples)

with open ('technique_labels_quads.nt', 'w') as technique_labels_quads_file:
	technique_labels_quads_file.writelines(TechniqueQuads)