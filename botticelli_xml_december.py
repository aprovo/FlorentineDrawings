# first steps:
# start a new xml data object
from xml.etree.ElementTree import Element, SubElement, ElementTree
import csv

root = Element('berenson')
BB_1961 = 0
BB_1938 = 0
BB_1903 = 0
FlorentineDrawingsProject = 0
Collection_URI_main = 0
Collection_URI_former = 0
Place_URI = 0
MuseumObject_URI = 0
Artist_URI_1961 = 0
Artist_URI_1938 = 0
Artist_URI_1903 = 0

Technique_URI = 0

# import the CSV

# parse the rows and loop
with open('FlorentineDrawings_SpreadsheetsCombined_v1 - Botticelli sample.csv', 'r', encoding="ISO-8859-1") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		City_Country = row[1]
		City = row[2]
		Country = row[3]
		Collection_main = row[4]
		Collection_sub = row[5]
		Former_collection = row[6]
		BB_1961_Inventory_number = row[7]
		Inventory_number_correction = row[8]
		BB_1961_number_letter = row[9]
		BB_1961_figure_number_recto = row[10]
		BB_1961_figure_number_verso = row[11]
		BB_1961_plate_number = row[12]
		BB_1961_Artist_NoQualifier = row[13]
		BB_1961_Qualifier = row[14]
		BB_1961_title_recto = row[15]
		BB_1961_title_verso = row[16]
		BB_1961_title_correction = row[17]
		BB_1961_technique_recto_1 = row[18]
		BB_1961_technique_recto_2 = row[19]
		BB_1961_technique_recto_3 = row[20]
		BB_1961_technique_recto_4 = row[21]
		BB_1961_technique_recto_5 = row[22]
		BB_1961_technique_verso_1 = row[23]
		BB_1961_technique_verso_2 = row[24]
		BB_1961_technique_verso_3 = row[25]
		BB_1961_technique_verso_4 = row[26]
		BB_1961_text_recto = row[27]
		BB_1961_text_verso = row[28]
		BB_1938_number_letter = row[29]
		BB_1938_Artist_NoQualifier = row[30]
		BB_1938_Qualifier = row[31]
		BB_1938_title_recto = row[32]
		BB_1938_title_verso = row[33]
		BB_1938_text_recto = row[34]
		BB_1938_text_verso = row[35]
		BB_1903_number_letter = row[36]
		BB_1903_Artist_NoQualifier = row[37]
		BB_1903_Qualifier = row[38]
		BB_1903_title_recto = row[39]
		BB_1903_title_verso = row[40]
		BB_1903_text_recto = row[41]
		BB_1903_text_verso = row[42]



#wrapper for entire drawing
		child = SubElement(root, 'FlorentineDrawings_IdentifierBB1961')
		child.text = FlorentineDrawings_IdentifierBB1961
		
#data from the project
		subChild = SubElement(child, 'FlorentineDrawingsProject')
		subChild.text = FlorentineDrawingsProject

		subChild1 = SubElement(subChild, 'Inventory_number_correction')
		subChild1.text = Inventory_number_correction
		subChild2 = SubElement(subChild, 'BB_1961_title_correction')
		subChild2.text = BB_1961_title_correction

		subChild1 = SubElement (subChild, 'City_Country')	
		subChild1.text = City_Country

		subChild1 = SubElement(subChild, 'City')
		subChild1.text = City
		subChild1 = SubElement(subChild, 'Country')
		subChild1.text = Country
		
		subChild1 = SubElement(subChild, 'Place_URI')
		subChild1.text = Place_URI


		subChild1 = SubElement(subChild, 'Collection_main')
		subChild1.text = Collection_main
		
		subChild1 = SubElement(subChild, 'Collection_URI_main')
		subChild1.text = Collection_URI_main

		subChild1 = SubElement(subChild, 'Collection_sub')
		subChild1.text = Collection_sub

		subChild1 = SubElement(subChild, 'Former_collection')
		subChild1.text = Former_collection
		
		subChild1 = SubElement(subChild, 'Collection_URI_former')
		subChild1.text = Collection_URI_former

		subChild2 = SubElement(subChild, 'BB_1961_technique_recto_1')
		subChild2.text = BB_1961_technique_recto_1

		subChild2 = SubElement(subChild, 'BB_1961_technique_recto_2')
		subChild2.text = BB_1961_technique_recto_2
		subChild2 = SubElement(subChild, 'BB_1961_technique_recto_3')
		subChild2.text = BB_1961_technique_recto_3
		subChild2 = SubElement(subChild, 'BB_1961_technique_recto_4')
		subChild2.text = BB_1961_technique_recto_4
		subChild2 = SubElement(subChild, 'BB_1961_technique_recto_5')
		subChild2.text = BB_1961_technique_recto_5


		subChild2 = SubElement(subChild, 'BB_1961_technique_verso_1')
		subChild2.text = BB_1961_technique_verso_1
		subChild2 = SubElement(subChild, 'BB_1961_technique_verso_2')
		subChild2.text = BB_1961_technique_verso_2
		subChild2 = SubElement(subChild, 'BB_1961_technique_verso_3')
		subChild2.text = BB_1961_technique_verso_3
		subChild2 = SubElement(subChild, 'BB_1961_technique_verso_4')
		subChild2.text = BB_1961_technique_verso_4

		subChild1 = SubElement(subChild, 'MuseumObject_URI')
		subChild1.text = MuseumObject_URI

#data from the 1961 edition
		subChild = SubElement (child, 'BB_1961')
		subChild.text = BB_1961



		subChild1 = SubElement(subChild, 'BB_1961_Inventory_number')
		subChild1.text = BB_1961_Inventory_number

		subChild1 = SubElement(subChild, 'BB_1961_figure_number_recto')
		subChild1.text = BB_1961_figure_number_recto
		subChild1 = SubElement(subChild, 'BB_1961_figure_number_verso')
		subChild1.text = BB_1961_figure_number_verso

		subChild1 = SubElement(subChild, 'BB_1961_plate_number')
		subChild1.text = BB_1961_plate_number

		subChild2 = SubElement(subChild, 'BB_1961_number_letter')
		subChild2.text = BB_1961_number_letter
		
		subChild2 = SubElement(subChild, 'BB_1961_Artist_NoQualifier')
		subChild2.text = BB_1961_Artist_NoQualifier

		subChild2 = SubElement(subChild, 'Artist_URI_1961')
		subChild2.text = Artist_URI_1961

		subChild2 = SubElement(subChild, 'BB_1961_Qualifier')
		subChild2.text = BB_1961_Qualifier

		subChild2 = SubElement(subChild, 'BB_1961_title_recto')
		subChild2.text = BB_1961_title_recto
		subChild2 = SubElement(subChild, 'BB_1961_title_verso')
		subChild2.text = BB_1961_title_verso




		subChild2 = SubElement(subChild, 'BB_1961_text_recto')
		subChild2.text = BB_1961_text_recto
		subChild2 = SubElement(subChild, 'BB_1961_text_verso')
		subChild2.text = BB_1961_text_verso


#data from the 1938 edition
		subChild = SubElement (child, 'BB_1938')
		subChild.text = BB_1938

		subChild3 = SubElement(subChild, 'BB_1938_number_letter')
		subChild3.text = BB_1938_number_letter
		subChild3 = SubElement(subChild, 'BB_1938_Artist_NoQualifier')
		subChild3.text = BB_1938_Artist_NoQualifier

		subChild3 = SubElement(subChild, 'Artist_URI_1938')
		subChild3.text = Artist_URI_1938

		subChild3 = SubElement(subChild, 'BB_1938_Qualifier')
		subChild3.text = BB_1938_Qualifier

		subChild3 = SubElement(subChild, 'BB_1938_title_recto')
		subChild3.text = BB_1938_title_recto
		subChild3 = SubElement(subChild, 'BB_1938_title_verso')
		subChild3.text = BB_1938_title_verso
		subChild3 = SubElement(subChild, 'BB_1938_text_recto')
		subChild3.text = BB_1938_text_recto
		subChild3 = SubElement(subChild, 'BB_1938_text_verso')
		subChild3.text = BB_1938_text_verso

#data from the 1903 edition
		subChild = SubElement (child, 'BB_1903')
		subChild.text = BB_1903

		subChild4 = SubElement(subChild, 'BB_1903_number_letter')
		subChild4.text = BB_1903_number_letter

		subChild4 = SubElement(subChild, 'BB_1903_Artist_NoQualifier')
		subChild4.text = BB_1903_Artist_NoQualifier

		subChild4 = SubElement(subChild, 'Artist_URI_1903')
		subChild4.text = Artist_URI_1903

		subChild4 = SubElement(subChild, 'BB_1903_Qualifier')
		subChild4.text = BB_1903_Qualifier

		subChild4 = SubElement(subChild, 'BB_1903_title_recto')
		subChild4.text = BB_1903_title_recto
		subChild4 = SubElement(subChild, 'BB_1903_title_verso')
		subChild4.text = BB_1903_title_verso
		subChild4 = SubElement(subChild, 'BB_1903_text_recto')
		subChild4.text = BB_1903_text_recto
		subChild4 = SubElement(subChild, 'BB_1903_text_verso')
		subChild4.text = BB_1903_text_verso

# 	assign the different columns in the rows to variables
		
# 	make a new indexentry child element of the root
#	make a childchild (aka grandchild), name, note, ref
#	fill the grandchilden with the variables

# write XML file
ElementTree(root).write("botticelli_xml_december.xml", encoding="ISO-8859-1")	
	


#loop through and if a column has a value that you want to put in a particular xml element,

# 	define the xml element and dump the data in