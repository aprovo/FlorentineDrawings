#this script converts triples into quads by adding the graph uri to the end of the triple.

with open ('BotticelliTriples1961_23March2016.nt') as graph:
	for triple in graph:
		triple=triple.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1961> .\n")
		print(triple)