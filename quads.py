#this script converts triples into quads by adding the graph uri to the end of the triple.
# quads_project=[]
# quads_1961=[]
# quads_1938=[]
# quads_1903=[]
# pagequads_1903=[]
#platequads_1903=[]
BMimagequads =[]

# with open ('project_issues_2september.nt') as graph_project:
# 	for triple_project in graph_project:
# 		quad_project=triple_project.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/project2016> .\n")
# 		quads_project.append(quad_project + "\n")

with open ('BMimageURLs.nt') as BMgraph_project:
	for BMtriple_project in BMgraph_project:
		BMquad_project=BMtriple_project.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/project2016> .\n")
		BMimagequads.append(BMquad_project + "\n")



# with open ('1961_issues_2september.nt') as graph_1961:
# 	for triple_1961 in graph_1961:
# 		quad_1961=triple_1961.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1961> .\n")
# 		quads_1961.append(quad_1961 + "\n")

# with open ('1938_issues_2september.nt') as graph_1938:
# 	for triple_1938 in graph_1938:
# 		quad_1938=triple_1938.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1938> .\n")
# 		quads_1938.append(quad_1938 + "\n")

# with open ('1903_issues_2september.nt') as graph_1903:
# 	for triple_1903 in graph_1903:
# 		quad_1903=triple_1903.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1903> .\n")
# 		quads_1903.append(quad_1903 + "\n")

# with open ('pagenumbers_issues_2september.nt') as pagegraph_1903:
# 	for pagetriple_1903 in pagegraph_1903:
# 		pagequad_1903=pagetriple_1903.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1903> .\n")
# 		pagequads_1903.append(pagequad_1903 + "\n")

# with open ('platenumbers30aug.nt') as plategraph_1903:
# 	for platetriple_1903 in plategraph_1903:
# 		platequad_1903=platetriple_1903.replace(".\n", "<http://data.itatti.harvard.edu/florentinedrawings/berenson1903> .\n")
# 		platequads_1903.append(platequad_1903 + "\n")

# with open ('project_issues_2september_quads.nt', 'w') as quads_project_file:
# 	quads_project_file.writelines(quads_project)

# with open ('1961_issues_2september_quads.nt', 'w') as quads_1961_file:
# 	quads_1961_file.writelines(quads_1961)

# with open ('1938_issues_2september_quads.nt', 'w') as quads_1938_file:
# 	quads_1938_file.writelines(quads_1938)

# with open ('1903_issues_2september_quads.nt', 'w') as quads_1903_file:
# 	quads_1903_file.writelines(quads_1903)

# with open ('pagenumbers_issues_2september_quads.nt', 'w') as quads_page1903_file:
# 	quads_page1903_file.writelines(pagequads_1903)

with open ('BMimageURLs_quads.nt', 'w') as quads_BMimageURLs_file:
	quads_BMimageURLs_file.writelines(BMimagequads)
