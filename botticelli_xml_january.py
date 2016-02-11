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

root = Element('berenson')
drawing_record = 0
BB_1961 = 0
BB_1938 = 0
BB_1903 = 0
FlorentineDrawingsProject = 0
Collection_URI_main = 0
Collection_URI_main_name = "Collection_URI_main"
Collection_URI_former = 0
Collection_URI_former_name = "Collection_URI_former"
Place_URI = 0
Place_URI_name = "Place_URI"
MuseumObject_URI = 0
MuseumObject_URI_name = "MuseumObject_URI"
Artist_URI_1961 = 0
Artist_URI_1961_name = "Artist_URI_1961"
Artist_URI_1938 = 0
Artist_URI_1938_name = "Artist_URI_1938"
Artist_URI_1903 = 0
Artist_URI_1903_name = "Artist_URI_1903"

Technique_URI = 0

# import the CSV

# parse the rows and loop
with open('FlorentineDrawings_SpreadsheetsCombined_v1 - Botticelli sample.csv', 'r', encoding="ISO-8859-1") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		City_Country = row[1]
		City_Country_name = "City_Country"
		
		City = row[2]
		City_name = "City"
		
		Country = row[3]
		Country_name = "Country"
		
		Collection_main = row[4]
		Collection_main_name = "Collection_main"
		
		Collection_sub = row[5]
		Collection_sub_name = "Collection_sub"
		
		Former_collection = row[6]
		Former_collection_name ="Former_collection"

		BB_1961_Inventory_number = row[7]
		BB_1961_Inventory_number_name = "BB_1961_Inventory_number"

		Inventory_number_correction = row[8]
		Inventory_number_correction_name = "Inventory_number_correction"
		
		BB_1961_number_letter = row[9]
		BB_1961_number_letter_name = "BB_1961_number_letter"

		BB_1961_figure_number_recto = row[10]
		BB_1961_figure_number_recto_name = "BB_1961_figure_number_recto"

		BB_1961_figure_number_verso = row[11]
		BB_1961_figure_number_verso_name = "BB_1961_figure_number_verso"

		BB_1961_plate_number = row[12]
		BB_1961_plate_number_name = "BB_1961_plate_number"

		BB_1961_Artist_NoQualifier = row[13]
		BB_1961_Artist_NoQualifier_name = "BB_1961_Artist_NoQualifier"

		BB_1961_Qualifier = row[14]
		BB_1961_Qualifier_name = "BB_1961_Qualifier"

		BB_1961_title_recto = row[15]
		BB_1961_title_recto_name = "BB_1961_title_recto"

		BB_1961_title_verso = row[16]
		BB_1961_title_verso_name  = "BB_1961_title_verso"

		BB_1961_title_correction = row[17]
		BB_1961_title_correction_name = "BB_1961_title_correction"

		BB_1961_technique_recto_1 = row[18]
		BB_1961_technique_recto_1_name = "BB_1961_technique_recto_1"

		BB_1961_technique_recto_2 = row[19]
		BB_1961_technique_recto_2_name = "BB_1961_technique_recto_2"

		BB_1961_technique_recto_3 = row[20]
		BB_1961_technique_recto_3_name = "BB_1961_technique_recto_3"

		BB_1961_technique_recto_4 = row[21]
		BB_1961_technique_recto_4_name = "BB_1961_technique_recto_4"

		BB_1961_technique_recto_5 = row[22]
		BB_1961_technique_recto_5_name = "BB_1961_technique_recto_5"

		BB_1961_technique_verso_1 = row[23]
		BB_1961_technique_verso_1_name = "BB_1961_technique_verso_1"

		BB_1961_technique_verso_2 = row[24]
		BB_1961_technique_verso_2_name = "BB_1961_technique_verso_2"

		BB_1961_technique_verso_3 = row[25]
		BB_1961_technique_verso_3_name = "BB_1961_technique_verso_3"

		BB_1961_technique_verso_4 = row[26]
		BB_1961_technique_verso_4_name = "BB_1961_technique_verso_4"

		BB_1961_text_recto = row[27]
		BB_1961_text_recto_name = "BB_1961_text_recto"

		BB_1961_text_verso = row[28]
		BB_1961_text_verso_name = "BB_1961_text_verso"

		BB_1938_number_letter = row[29]
		BB_1938_number_letter_name = "BB_1938_number_letter"

		BB_1938_Artist_NoQualifier = row[30]
		BB_1938_Artist_NoQualifier_name = "BB_1938_Artist_NoQualifier"

		BB_1938_Qualifier = row[31]
		BB_1938_Qualifier_name = "BB_1938_Qualifier"

		BB_1938_title_recto = row[32]
		BB_1938_title_recto_name = "BB_1938_title_recto"

		BB_1938_title_verso = row[33]
		BB_1938_title_verso_name = "BB_1938_title_verso"

		BB_1938_text_recto = row[34]
		BB_1938_text_recto_name = "BB_1938_text_recto"

		BB_1938_text_verso = row[35]
		BB_1938_text_verso_name = "BB_1938_text_verso"

		BB_1903_number_letter = row[36]
		BB_1903_number_letter_name = "BB_1903_number_letter"

		BB_1903_Artist_NoQualifier = row[37]
		BB_1903_Artist_NoQualifier_name = "BB_1903_Artist_NoQualifier"

		BB_1903_Qualifier = row[38]
		BB_1903_Qualifier_name = "BB_1903_Qualifier"

		BB_1903_title_recto = row[39]
		BB_1903_title_recto_name = "BB_1903_title_recto"

		BB_1903_title_verso = row[40]
		BB_1903_title_verso_name = "BB_1903_title_verso"

		BB_1903_text_recto = row[41]
		BB_1903_text_recto_name = "BB_1903_text_recto"

		BB_1903_text_verso = row[42]
		BB_1903_text_verso_name = "BB_1903_text_verso"

#wrapper for entire drawing
		child = SubElement(root, 'drawing_record')
		child.text = drawing_record
		
#data from the project. this could be come a function for sure..i'd like to try that!
		subChild = SubElement(child, 'FlorentineDrawingsProject')
		subChild.text = FlorentineDrawingsProject

		#subChild1 = SubElement(subChild, 'FlorentineDrawings_IdentifierBB1961')
		#subChild1.text = FlorentineDrawings_IdentifierBB1961
		drawingsubsubChild(FlorentineDrawings_IdentifierBB1961, FlorentineDrawings_IdentifierBB1961_name)	
		#subChild1 = SubElement(subChild, 'Inventory_number_correction')
		#subChild1.text = Inventory_number_correction
		drawingsubsubChild(Inventory_number_correction, Inventory_number_correction_name)

		
		# subChild2 = SubElement(subChild, 'BB_1961_title_correction')
		# subChild2.text = BB_1961_title_correction
		drawingsubsubChild(BB_1961_title_correction, BB_1961_title_correction_name)

		# subChild1 = SubElement (subChild, 'City_Country')	
		# subChild1.text = City_Country
		drawingsubsubChild(City_Country, City_Country_name)

		# subChild1 = SubElement(subChild, 'City')
		# subChild1.text = City
		drawingsubsubChild(City, City_name)
		# subChild1 = SubElement(subChild, 'Country')
		# subChild1.text = Country
		drawingsubsubChild(Country, Country_name)

		# subChild1 = SubElement(subChild, 'Place_URI')
		# subChild1.text = Place_URI
		drawingsubsubChild(Place_URI, Place_URI_name)

		# subChild1 = SubElement(subChild, 'Collection_main')
		# subChild1.text = Collection_main
		drawingsubsubChild(Collection_main, Collection_main_name)

		# subChild1 = SubElement(subChild, 'Collection_URI_main')
		# subChild1.text = Collection_URI_main
		drawingsubsubChild(Collection_URI_main, Collection_URI_main_name)
		# subChild1 = SubElement(subChild, 'Collection_sub')
		# subChild1.text = Collection_sub
		drawingsubsubChild(Collection_sub, Collection_sub_name)
		# subChild1 = SubElement(subChild, 'Former_collection')
		# subChild1.text = Former_collection
		drawingsubsubChild(Former_collection, Former_collection_name)
		# subChild1 = SubElement(subChild, 'Collection_URI_former')
		# subChild1.text = Collection_URI_former
		drawingsubsubChild(Collection_URI_former, Collection_URI_former_name)
		# subChild2 = SubElement(subChild, 'BB_1961_technique_recto_1')
		# subChild2.text = BB_1961_technique_recto_1
		drawingsubsubChild(BB_1961_technique_recto_1, BB_1961_technique_recto_1_name)
		# subChild2 = SubElement(subChild, 'BB_1961_technique_recto_2')
		# subChild2.text = BB_1961_technique_recto_2
		drawingsubsubChild(BB_1961_technique_recto_2, BB_1961_technique_recto_2_name)
		# subChild2 = SubElement(subChild, 'BB_1961_technique_recto_3')
		# subChild2.text = BB_1961_technique_recto_3
		drawingsubsubChild(BB_1961_technique_recto_3, BB_1961_technique_recto_3_name)

		# subChild2 = SubElement(subChild, 'BB_1961_technique_recto_4')
		# subChild2.text = BB_1961_technique_recto_4
		drawingsubsubChild(BB_1961_technique_recto_4, BB_1961_technique_recto_4_name)

		# subChild2 = SubElement(subChild, 'BB_1961_technique_recto_5')
		# subChild2.text = BB_1961_technique_recto_5
		drawingsubsubChild(BB_1961_technique_recto_5, BB_1961_technique_recto_5_name)


		# subChild2 = SubElement(subChild, 'BB_1961_technique_verso_1')
		# subChild2.text = BB_1961_technique_verso_1
		drawingsubsubChild(BB_1961_technique_verso_1, BB_1961_technique_verso_1_name)

		# subChild2 = SubElement(subChild, 'BB_1961_technique_verso_2')
		# subChild2.text = BB_1961_technique_verso_2
		drawingsubsubChild(BB_1961_technique_verso_2, BB_1961_technique_verso_2_name)

		# subChild2 = SubElement(subChild, 'BB_1961_technique_verso_3')
		# subChild2.text = BB_1961_technique_verso_3
		drawingsubsubChild(BB_1961_technique_verso_3, BB_1961_technique_verso_3_name)

		# subChild2 = SubElement(subChild, 'BB_1961_technique_verso_4')
		# subChild2.text = BB_1961_technique_verso_4
		drawingsubsubChild(BB_1961_technique_verso_4, BB_1961_technique_verso_4_name)

		# subChild1 = SubElement(subChild, 'MuseumObject_URI')
		# subChild1.text = MuseumObject_URI
		drawingsubsubChild(MuseumObject_URI, MuseumObject_URI_name)

#data from the 1961 edition
		subChild = SubElement (child, 'BB_1961')
		subChild.text = BB_1961

		# subChild1 = SubElement(subChild, 'BB_1961_Inventory_number')
		# subChild1.text = BB_1961_Inventory_number
		drawingsubsubChild(BB_1961_Inventory_number, BB_1961_Inventory_number_name)

		# subChild1 = SubElement(subChild, 'BB_1961_figure_number_recto')
		# subChild1.text = BB_1961_figure_number_recto
		drawingsubsubChild(BB_1961_figure_number_recto, BB_1961_figure_number_recto_name)
		
		# subChild1 = SubElement(subChild, 'BB_1961_figure_number_verso')
		# subChild1.text = BB_1961_figure_number_verso
		drawingsubsubChild(BB_1961_figure_number_verso, BB_1961_figure_number_verso_name)

		# subChild1 = SubElement(subChild, 'BB_1961_plate_number')
		# subChild1.text = BB_1961_plate_number
		drawingsubsubChild(BB_1961_plate_number, BB_1961_plate_number_name)

		# subChild2 = SubElement(subChild, 'BB_1961_number_letter')
		# subChild2.text = BB_1961_number_letter
		drawingsubsubChild(BB_1961_number_letter, BB_1961_number_letter_name)

		# subChild2 = SubElement(subChild, 'BB_1961_Artist_NoQualifier')
		# subChild2.text = BB_1961_Artist_NoQualifier
		drawingsubsubChild(BB_1961_Artist_NoQualifier, BB_1961_Artist_NoQualifier_name)		
		# subChild2 = SubElement(subChild, 'Artist_URI_1961')
		# subChild2.text = Artist_URI_1961
		drawingsubsubChild(Artist_URI_1961, Artist_URI_1961_name)
		
		# subChild2 = SubElement(subChild, 'BB_1961_Qualifier')
		# subChild2.text = BB_1961_Qualifier
		drawingsubsubChild(BB_1961_Qualifier, BB_1961_Qualifier_name)
		
		# subChild2 = SubElement(subChild, 'BB_1961_title_recto')
		# subChild2.text = BB_1961_title_recto
		drawingsubsubChild(BB_1961_title_recto, BB_1961_title_recto_name)
		
		# subChild2 = SubElement(subChild, 'BB_1961_title_verso')
		# subChild2.text = BB_1961_title_verso
		drawingsubsubChild(BB_1961_title_verso, BB_1961_title_verso_name)
		
		# subChild2 = SubElement(subChild, 'BB_1961_text_recto')
		# subChild2.text = BB_1961_text_recto	
		drawingsubsubChild(BB_1961_text_recto, BB_1961_text_recto_name)
		
		# subChild2 = SubElement(subChild, 'BB_1961_text_verso')
		# subChild2.text = BB_1961_text_verso
		drawingsubsubChild(BB_1961_text_verso, BB_1961_text_verso_name)


#data from the 1938 edition
		subChild = SubElement (child,'BB_1938')
		subChild.text = BB_1938

		# subChild3 = SubElement(subChild, 'BB_1938_number_letter')
		# subChild3.text = BB_1938_number_letter
		drawingsubsubChild(BB_1938_number_letter, BB_1938_number_letter_name)

		# subChild3 = SubElement(subChild, 'BB_1938_Artist_NoQualifier')
		# subChild3.text = BB_1938_Artist_NoQualifier
		drawingsubsubChild(BB_1938_Artist_NoQualifier, BB_1938_Artist_NoQualifier_name)
		
		# subChild3 = SubElement(subChild, 'Artist_URI_1938')
		# subChild3.text = Artist_URI_1938
		drawingsubsubChild(Artist_URI_1938, Artist_URI_1938_name)

		# subChild3 = SubElement(subChild, 'BB_1938_Qualifier')
		# subChild3.text = BB_1938_Qualifier
		drawingsubsubChild(BB_1938_Qualifier, BB_1938_Qualifier_name)

		# subChild3 = SubElement(subChild, 'BB_1938_title_recto')
		# subChild3.text = BB_1938_title_recto
		drawingsubsubChild(BB_1938_title_recto, BB_1938_title_recto_name)

		# subChild3 = SubElement(subChild, 'BB_1938_title_verso')
		# subChild3.text = BB_1938_title_verso
		drawingsubsubChild(BB_1938_title_verso, BB_1938_title_verso_name)

		# subChild3 = SubElement(subChild, 'BB_1938_text_recto')
		# subChild3.text = BB_1938_text_recto
		drawingsubsubChild(BB_1938_text_recto, BB_1938_text_recto_name)

		# subChild3 = SubElement(subChild, 'BB_1938_text_verso')
		# subChild3.text = BB_1938_text_verso
		drawingsubsubChild(BB_1938_text_verso, BB_1938_text_verso_name)

# #data from the 1903 edition
		subChild = SubElement (child, 'BB_1903')
		subChild.text = BB_1903

		# subChild4 = SubElement(subChild, 'BB_1903_number_letter')
		# subChild4.text = BB_1903_number_letter
		drawingsubsubChild(BB_1903_number_letter, BB_1903_number_letter_name)

		# subChild4 = SubElement(subChild, 'BB_1903_Artist_NoQualifier')
		# subChild4.text = BB_1903_Artist_NoQualifier
		drawingsubsubChild(BB_1903_Artist_NoQualifier, BB_1903_Artist_NoQualifier_name)

		# subChild4 = SubElement(subChild, 'Artist_URI_1903')
		# subChild4.text = Artist_URI_1903
		drawingsubsubChild(Artist_URI_1903, Artist_URI_1903_name)

		# subChild4 = SubElement(subChild, 'BB_1903_Qualifier')
		# subChild4.text = BB_1903_Qualifier
		drawingsubsubChild(BB_1903_Qualifier, BB_1903_Qualifier_name)

		# subChild4 = SubElement(subChild, 'BB_1903_title_recto')
		# subChild4.text = BB_1903_title_recto
		drawingsubsubChild(BB_1903_title_recto, BB_1903_title_recto_name)

		# subChild4 = SubElement(subChild, 'BB_1903_title_verso')
		# subChild4.text = BB_1903_title_verso
		drawingsubsubChild(BB_1903_title_verso, BB_1903_title_verso_name)

		# subChild4 = SubElement(subChild, 'BB_1903_text_recto')
		# subChild4.text = BB_1903_text_recto
		drawingsubsubChild(BB_1903_text_recto, BB_1903_text_recto_name)

		# subChild4 = SubElement(subChild, 'BB_1903_text_verso')
		# subChild4.text = BB_1903_text_verso
		drawingsubsubChild(BB_1903_text_verso, BB_1903_text_verso_name)

# 	before writing the file, want to check to see if an element is empty.
#if so, do not include.
#to do this, should i write the file, then re-import it to parse it, and then go through
#and remove empty elements? or can i do that from here?
#get(key, default=None)
# show the text of that key (attribute)
#if text != None:
#go ahead and make the element or subelement
#maybe:		if subChild1.text == None:
				#SubElement.remove(subChild1)
#maybe something to be found here: http://stackoverflow.com/questions/12694091/python-lxml-how-to-remove-empty-repeated-tags


#iterator = ElementTree(root).getiterator(tag=None)
#for elem in iterator:
	#print(elem.text)
#	if elem.text == 0:
#		print (elem)
	#if elem.text == 0:
#	elem.remove()
#print(elem.text)
# write XML file
ElementTree(root).write("botticelli_xml_january.xml", encoding="ISO-8859-1")	



# 	define the xml element and dump the data in