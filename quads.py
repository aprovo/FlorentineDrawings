#this script converts triples into quads by adding the graph uri to the end of the triple.
quads=[]

with open ('project_triples.rdf') as graph:
	for triple in graph:
		quad=triple.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/project2016> .\n")
		quads.append(quad + "\n")

with open ('project2016_quads.nt', 'w') as quads_file:
	quads_file.writelines(quads)