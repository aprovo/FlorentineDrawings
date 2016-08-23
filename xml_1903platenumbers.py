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
BB_1903 = 0
BB_1903_recto = 0
BB_1903_verso = 0
FlorentineDrawingsProject = 0


# import the massive CSV

# parse the rows and loop
with open('FlorentineDrawings_1903_PlateNumbers - Sheet1.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		PlateNumber_1903 = row[1]
		PlateNumber_1903_name = "PlateNumber_1903"
		
		VersoYN = row[5]
		VersoYN_name = "VersoYN"
		
		IIIF_Plate_URL = row[8]
		IIIF_Plate_URL_name = "IIIF_Plate_URL"
		
		AWS_Image_URL = row[9]
		AWS_Image_URL_name = "AWS_Image_URL"

		AWS_Thumbnail_URL = row[10]
		AWS_Thumbnail_URL_name = "AWS_Thumbnail_URL"
		
		
#wrapper for entire drawing
		child = SubElement(root, 'drawing_record')
		child.text = drawing_record
		
#data from the project.
		subChild = SubElement(child, 'FlorentineDrawingsProject')
		subChild.text = FlorentineDrawingsProject
		
		drawingsubsubChild(FlorentineDrawings_IdentifierBB1961, FlorentineDrawings_IdentifierBB1961_name)	
	

# #data from the 1903 edition
		subChild = SubElement (child, 'BB_1903')
		subChild.text = BB_1903

		drawingsubsubChild(PlateNumber_1903, PlateNumber_1903_name)
		drawingsubsubChild(VersoYN, VersoYN_name)
		drawingsubsubChild(IIIF_Plate_URL, IIIF_Plate_URL_name)
		drawingsubsubChild(AWS_Image_URL, AWS_Image_URL_name)
		drawingsubsubChild(AWS_Thumbnail_URL, AWS_Thumbnail_URL_name)

		subsubChild = SubElement (subChild, 'BB_1903_recto')
		subsubChild.text = BB_1903_recto


		subsubChild = SubElement (subChild, 'BB_1903_verso')
		subsubChild.text = BB_1903_verso


# write XML file
ElementTree(root).write("xml_1903platenumbers_22August.xml", encoding="UTF-8", xml_declaration=True, default_namespace=None)