#this script converts triples into quads by adding the graph uri to the end of the triple.
quads_project=[]
quads_1961=[]
quads_1938=[]
quads_1903=[]

with open ('august8_project_triples.nt') as graph_project:
	for triple_project in graph_project:
		quad_project=triple_project.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/project2016> .\n")
		quads_project.append(quad_project + "\n")

with open ('18july_1961_triples.nt') as graph_1961:
	for triple_1961 in graph_1961:
		quad_1961=triple_1961.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1961> .\n")
		quads_1961.append(quad_1961 + "\n")

with open ('18july_1938_triples.nt') as graph_1938:
	for triple_1938 in graph_1938:
		quad_1938=triple_1938.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1938> .\n")
		quads_1938.append(quad_1938 + "\n")

with open ('18july_1903_triples.nt') as graph_1903:
	for triple_1903 in graph_1903:
		quad_1903=triple_1903.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1903> .\n")
		quads_1903.append(quad_1903 + "\n")

with open ('august8_project_quads.nt', 'w') as quads_project_file:
	quads_project_file.writelines(quads_project)

with open ('1961_18July2016_quads.nt', 'w') as quads_1961_file:
	quads_1961_file.writelines(quads_1961)

with open ('1938_18July2016_quads.nt', 'w') as quads_1938_file:
	quads_1938_file.writelines(quads_1938)

with open ('1903_18July2016_quads.nt', 'w') as quads_1903_file:
	quads_1903_file.writelines(quads_1903)
