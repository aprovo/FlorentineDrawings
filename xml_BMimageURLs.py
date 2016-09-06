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
FlorentineDrawingsProject = 0


# import the massive CSV

# parse the rows and loop
with open('FlorentineDrawings_SpreadsheetsCombined_v5 - BM_Image_URLs.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		BM_Image_URL = row[1]
		BM_Image_URL_name = "BM_Image_URL"
		
		
#wrapper for entire drawing
		child = SubElement(root, 'drawing_record')
		child.text = drawing_record
		
#data from the project.
		subChild = SubElement(child, 'FlorentineDrawingsProject')
		subChild.text = FlorentineDrawingsProject
		
		drawingsubsubChild(FlorentineDrawings_IdentifierBB1961, FlorentineDrawings_IdentifierBB1961_name)	
		drawingsubsubChild(BM_Image_URL, BM_Image_URL_name)	


# write XML file
ElementTree(root).write("xml_BMimageURLs.xml", encoding="UTF-8", xml_declaration=True, default_namespace=None)