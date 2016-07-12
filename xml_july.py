# first steps:
# start a new xml data object
from xml.etree.ElementTree import Element, SubElement, ElementTree
import csv

def drawingsubsubChild(x, y): 
	if x != "":
		print("ok")
		childElement = SubElement(subChild, y) 
#problem here: need x here to be the variable name. can't put "x" or just get text "x" in my element tags.
#don't like it, but below created additional name variable.
		childElement.text = x
	elif x == "":
		pass

def drawingsubsubsubChild(x, y): 
	if x != "":
		print("ok")
		childElement = SubElement(subsubChild, y) 
#problem here: need x here to be the variable name. can't put "x" or just get text "x" in my element tags.
#don't like it, but below created additional name variable.
		childElement.text = x
	elif x == "":
		pass

root = Element('berenson')
drawing_record = 0
BB_1961 = 0
BB_1961_recto = 0
BB_1961_verso = 0
BB_1938 = 0
BB_1938_recto = 0
BB_1938_verso = 0
BB_1903 = 0
BB_1903_recto = 0
BB_1903_verso = 0
FlorentineDrawingsProject = 0


# import the massive CSV

# parse the rows and loop
with open('FlorentineDrawings_SpreadsheetsCombined_v5 - Botticelli_FilippinoCaseStudy_LocColl_Updates.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		City = row[1]
		City_name = "City"
		
		City_URI = row[2]
		City_URI_name = "City_URI"
		
		Country = row[3]
		Country_name = "Country"
		
		Country_URI = row[4]
		Country_URI_name = "Country_URI"

		Collection_main = row[5]
		Collection_main_name = "Collection_main"
		
		Collection_URI_main = row[6]
		Collection_URI_main_name = "Collection_URI_main"

		Collection_sub = row[7]
		Collection_sub_name = "Collection_sub"
		
		Collection_URI_sub = row[8]
		Collection_URI_sub_name = "Collection_URI_sub"

		Former_collection = row[9]
		Former_collection_name ="Former_collection"

		Former_collection_URI = row[10]
		Former_collection_URI_name ="Former_collection_URI"

		Inventory_number = row[11]
		Inventory_number_name = "Inventory_number"
		
		Object_repository_URI_corrected = row[12]
		Object_repository_URI_corrected_name = "Object_repository_URI"

		BB_1961_number_letter = row[13]
		BB_1961_number_letter_name = "BB_1961_number_letter"

		BB_1961_number_letter_NoSpace = row[14]
		BB_1961_number_letter_NoSpace_name = "BB_1961_number_letter_NoSpace"

		BB_1961_figure_number_recto = row[15]
		BB_1961_figure_number_recto_name = "BB_1961_figure_number_recto"

		BB_1961_figure_number_verso = row[16]
		BB_1961_figure_number_verso_name = "BB_1961_figure_number_verso"

		BB_1961_plate_number = row[17]
		BB_1961_plate_number_name = "BB_1961_plate_number"

		BB_1961_Artist_NoQualifier = row[18]
		BB_1961_Artist_NoQualifier_name = "BB_1961_Artist_NoQualifier"
	
		Artist_URI_1961 = row[19]
		Artist_URI_1961_name = "Artist_URI_1961"
	
		BB_1961_Qualifier = row[20]
		BB_1961_Qualifier_name = "BB_1961_Qualifier"

		BB_1961_title_recto = row[21]
		BB_1961_title_recto_name = "BB_1961_title_recto"

		BB_1961_title_verso = row[22]
		BB_1961_title_verso_name  = "BB_1961_title_verso"

		BB_1961_title_correction = row[23]
		BB_1961_title_correction_name = "BB_1961_title_correction"

		BB_1961_technique_recto_1 = row[24]
		BB_1961_technique_recto_1_name = "BB_1961_technique_recto_1"

		BB_1961_technique_recto_1_URI = row[25]
		BB_1961_technique_recto_1_URI_name = "BB_1961_technique_recto_1_URI"

		BB_1961_technique_recto_2 = row[26]
		BB_1961_technique_recto_2_name = "BB_1961_technique_recto_2"

		BB_1961_technique_recto_2_URI = row[27]
		BB_1961_technique_recto_2_URI_name = "BB_1961_technique_recto_2_URI"

		BB_1961_technique_recto_3 = row[28]
		BB_1961_technique_recto_3_name = "BB_1961_technique_recto_3"

		BB_1961_technique_recto_3_URI = row[29]
		BB_1961_technique_recto_3_URI_name = "BB_1961_technique_recto_3_URI"

		BB_1961_technique_recto_4 = row[30]
		BB_1961_technique_recto_4_name = "BB_1961_technique_recto_4"

		BB_1961_technique_recto_4_URI = row[31]
		BB_1961_technique_recto_4_URI_name = "BB_1961_technique_recto_4_URI"

		BB_1961_technique_recto_5 = row[32]
		BB_1961_technique_recto_5_name = "BB_1961_technique_recto_5"

		BB_1961_technique_recto_5_URI = row[33]
		BB_1961_technique_recto_5_URI_name = "BB_1961_technique_recto_5_URI"

		BB_1961_technique_verso_1 = row[34]
		BB_1961_technique_verso_1_name = "BB_1961_technique_verso_1"

		BB_1961_technique_verso_1_URI = row[35]
		BB_1961_technique_verso_1_URI_name = "BB_1961_technique_verso_1_URI"

		BB_1961_technique_verso_2 = row[36]
		BB_1961_technique_verso_2_name = "BB_1961_technique_verso_2"

		BB_1961_technique_verso_2_URI = row[37]
		BB_1961_technique_verso_2_URI_name = "BB_1961_technique_verso_2_URI"

		BB_1961_technique_verso_3 = row[38]
		BB_1961_technique_verso_3_name = "BB_1961_technique_verso_3"

		BB_1961_technique_verso_3_URI = row[39]
		BB_1961_technique_verso_3_URI_name = "BB_1961_technique_verso_3_URI"

		BB_1961_technique_verso_4 = row[40]
		BB_1961_technique_verso_4_name = "BB_1961_technique_verso_4"

		BB_1961_technique_verso_4_URI = row[41]
		BB_1961_technique_verso_4_URI_name = "BB_1961_technique_verso_4_URI"

		BB_1961_text_recto = row[42]
		BB_1961_text_recto_name = "BB_1961_text_recto"

		BB_1961_text_verso = row[43]
		BB_1961_text_verso_name = "BB_1961_text_verso"

		BB_1938_number_letter = row[44]
		BB_1938_number_letter_name = "BB_1938_number_letter"

		BB_1938_number_letter_NoSpace = row[45]
		BB_1938_number_letter_NoSpace_name = "BB_1938_number_letter_NoSpace"

		BB_1938_Artist_NoQualifier = row[46]
		BB_1938_Artist_NoQualifier_name = "BB_1938_Artist_NoQualifier"

		Artist_URI_1938 = row[47]
		Artist_URI_1938_name = "Artist_URI_1938"

		BB_1938_Qualifier = row[48]
		BB_1938_Qualifier_name = "BB_1938_Qualifier"

		BB_1938_title_recto = row[49]
		BB_1938_title_recto_name = "BB_1938_title_recto"

		BB_1938_title_verso = row[50]
		BB_1938_title_verso_name = "BB_1938_title_verso"

		BB_1938_text_recto = row[51]
		BB_1938_text_recto_name = "BB_1938_text_recto"

		BB_1938_text_verso = row[52]
		BB_1938_text_verso_name = "BB_1938_text_verso"

		BB_1903_number_letter = row[53]
		BB_1903_number_letter_name = "BB_1903_number_letter"

		BB_1903_number_letter_NoSpace = row[54]
		BB_1903_number_letter_NoSpace_name = "BB_1903_number_letter_NoSpace"

		BB_1903_Artist_NoQualifier = row[55]
		BB_1903_Artist_NoQualifier_name = "BB_1903_Artist_NoQualifier"

		Artist_URI_1903 = row[56]
		Artist_URI_1903_name = "Artist_URI_1903"

		BB_1903_Qualifier = row[57]
		BB_1903_Qualifier_name = "BB_1903_Qualifier"

		BB_1903_title_recto = row[58]
		BB_1903_title_recto_name = "BB_1903_title_recto"

		BB_1903_title_verso = row[59]
		BB_1903_title_verso_name = "BB_1903_title_verso"

		BB_1903_text_recto = row[60]
		BB_1903_text_recto_name = "BB_1903_text_recto"

		BB_1903_text_verso = row[61]
		BB_1903_text_verso_name = "BB_1903_text_verso"

#wrapper for entire drawing
		child = SubElement(root, 'drawing_record')
		child.text = drawing_record
		
#data from the project.
		subChild = SubElement(child, 'FlorentineDrawingsProject')
		subChild.text = FlorentineDrawingsProject
		
		drawingsubsubChild(FlorentineDrawings_IdentifierBB1961, FlorentineDrawings_IdentifierBB1961_name)	
	
		drawingsubsubChild(Inventory_number, Inventory_number_name)

		drawingsubsubChild(BB_1961_title_correction, BB_1961_title_correction_name)

		drawingsubsubChild(City, City_name)
		drawingsubsubChild(City_URI, City_URI_name)

		drawingsubsubChild(Country, Country_name)
		drawingsubsubChild(Country_URI, Country_URI_name)

		drawingsubsubChild(Collection_main, Collection_main_name)
		drawingsubsubChild(Collection_URI_main, Collection_URI_main_name)

		drawingsubsubChild(Collection_sub, Collection_sub_name)
		drawingsubsubChild(Collection_URI_sub, Collection_URI_sub_name)

		drawingsubsubChild(Object_repository_URI_corrected, Object_repository_URI_corrected_name)

		drawingsubsubChild(Former_collection, Former_collection_name)
		drawingsubsubChild(Former_collection_URI, Former_collection_URI_name)
		
		drawingsubsubChild(BB_1961_technique_recto_1, BB_1961_technique_recto_1_name)
		drawingsubsubChild(BB_1961_technique_recto_1_URI, BB_1961_technique_recto_1_URI_name)

		drawingsubsubChild(BB_1961_technique_recto_2, BB_1961_technique_recto_1_name)
		drawingsubsubChild(BB_1961_technique_recto_2_URI, BB_1961_technique_recto_1_URI_name)

		drawingsubsubChild(BB_1961_technique_recto_3, BB_1961_technique_recto_1_name)
		drawingsubsubChild(BB_1961_technique_recto_3_URI, BB_1961_technique_recto_1_URI_name)

		drawingsubsubChild(BB_1961_technique_recto_4, BB_1961_technique_recto_1_name)
		drawingsubsubChild(BB_1961_technique_recto_4_URI, BB_1961_technique_recto_1_URI_name)

		drawingsubsubChild(BB_1961_technique_recto_5, BB_1961_technique_recto_1_name)
		drawingsubsubChild(BB_1961_technique_recto_5_URI, BB_1961_technique_recto_1_URI_name)

		drawingsubsubChild(BB_1961_technique_verso_1, BB_1961_technique_verso_1_name)
		drawingsubsubChild(BB_1961_technique_verso_1_URI, BB_1961_technique_verso_1_URI_name)

		drawingsubsubChild(BB_1961_technique_verso_2, BB_1961_technique_verso_1_name)
		drawingsubsubChild(BB_1961_technique_verso_2_URI, BB_1961_technique_verso_1_URI_name)

		drawingsubsubChild(BB_1961_technique_verso_3, BB_1961_technique_verso_1_name)
		drawingsubsubChild(BB_1961_technique_verso_3_URI, BB_1961_technique_verso_1_URI_name)

		drawingsubsubChild(BB_1961_technique_verso_4, BB_1961_technique_verso_1_name)
		drawingsubsubChild(BB_1961_technique_verso_4_URI, BB_1961_technique_verso_1_URI_name)

		#drawingsubsubChild(MuseumObject_URI, MuseumObject_URI_name)

#data from the 1961 edition
		subChild = SubElement (child, 'BB_1961')
		subChild.text = BB_1961

		subsubChild = SubElement (subChild, 'BB_1961_recto')
		subsubChild.text = BB_1961_recto


		drawingsubsubsubChild(BB_1961_figure_number_recto, BB_1961_figure_number_recto_name)
		
		drawingsubsubsubChild(BB_1961_plate_number, BB_1961_plate_number_name)

		drawingsubsubsubChild(BB_1961_number_letter, BB_1961_number_letter_name)
		drawingsubsubsubChild(BB_1961_number_letter_NoSpace, BB_1961_number_letter_NoSpace_name)

		drawingsubsubsubChild(BB_1961_Artist_NoQualifier, BB_1961_Artist_NoQualifier_name)		

		drawingsubsubsubChild(Artist_URI_1961, Artist_URI_1961_name)
		
		drawingsubsubsubChild(BB_1961_Qualifier, BB_1961_Qualifier_name)
		
		drawingsubsubsubChild(BB_1961_title_recto, BB_1961_title_recto_name)

		drawingsubsubsubChild(BB_1961_text_recto, BB_1961_text_recto_name)

		subsubChild = SubElement (subChild, 'BB_1961_verso')
		subsubChild.text = BB_1961_verso

		drawingsubsubsubChild(BB_1961_title_verso, BB_1961_title_verso_name)

		drawingsubsubsubChild(BB_1961_figure_number_verso, BB_1961_figure_number_verso_name)

		drawingsubsubChild(BB_1961_text_verso, BB_1961_text_verso_name)


#data from the 1938 edition
		subChild = SubElement (child,'BB_1938')
		subChild.text = BB_1938

		subsubChild = SubElement (subChild, 'BB_1938_recto')
		subsubChild.text = BB_1938_recto

		drawingsubsubsubChild(BB_1938_number_letter, BB_1938_number_letter_name)
		drawingsubsubsubChild(BB_1938_number_letter_NoSpace, BB_1938_number_letter_NoSpace_name)

		drawingsubsubsubChild(BB_1938_Artist_NoQualifier, BB_1938_Artist_NoQualifier_name)
		
		drawingsubsubsubChild(Artist_URI_1938, Artist_URI_1938_name)

		drawingsubsubsubChild(BB_1938_Qualifier, BB_1938_Qualifier_name)

		drawingsubsubsubChild(BB_1938_title_recto, BB_1938_title_recto_name)

		drawingsubsubsubChild(BB_1938_text_recto, BB_1938_text_recto_name)

		subsubChild = SubElement (subChild, 'BB_1938_verso')
		subsubChild.text = BB_1938_verso

		drawingsubsubsubChild(BB_1938_title_verso, BB_1938_title_verso_name)

		drawingsubsubsubChild(BB_1938_text_verso, BB_1938_text_verso_name)

# #data from the 1903 edition
		subChild = SubElement (child, 'BB_1903')
		subChild.text = BB_1903

		subsubChild = SubElement (subChild, 'BB_1903_recto')
		subsubChild.text = BB_1903_recto

		drawingsubsubsubChild(BB_1903_number_letter, BB_1903_number_letter_name)
		drawingsubsubsubChild(BB_1903_number_letter_NoSpace, BB_1903_number_letter_NoSpace_name)

		drawingsubsubsubChild(BB_1903_Artist_NoQualifier, BB_1903_Artist_NoQualifier_name)

		drawingsubsubsubChild(Artist_URI_1903, Artist_URI_1903_name)

		drawingsubsubsubChild(BB_1903_Qualifier, BB_1903_Qualifier_name)

		drawingsubsubsubChild(BB_1903_title_recto, BB_1903_title_recto_name)

		drawingsubsubsubChild(BB_1903_text_recto, BB_1903_text_recto_name)

		subsubChild = SubElement (subChild, 'BB_1903_verso')
		subsubChild.text = BB_1903_verso

		drawingsubsubsubChild(BB_1903_title_verso, BB_1903_title_verso_name)

		drawingsubsubsubChild(BB_1903_text_verso, BB_1903_text_verso_name)


# write XML file
ElementTree(root).write("xml_11july_updatedColl.xml", encoding="UTF-8", xml_declaration=True, default_namespace=None)