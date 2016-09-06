
#this script converts triples into quads by adding the graph uri to the end of the triple.
quads_bicci=[]

with open ('Bicci_di_Lorenzo_triples.nt') as biccigraph_1903:
	for biccitriple_1903 in biccigraph_1903:
		bicciquad_1903=biccitriple_1903.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1903> .\n")
		quads_bicci.append(bicciquad_1903 + "\n")

with open ('Bicci_di_Lorenzo_quads.nt', 'w') as quads_bicci_file:
	quads_bicci_file.writelines(quads_bicci)