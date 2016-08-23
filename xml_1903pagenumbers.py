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
with open('FlorentineDrawings_PageNumbers - MasterList.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		PageNumber_1903 = row[10]
		PageNumber_1903_name = "PageNumber_1903"
		
		IIIF_Page_URL = row[12]
		IIIF_Page_URL_name = "IIIF_Page_URL"
		
		AWS_PageImage_URL = row[13]
		AWS_PageImage_URL_name = "AWS_PageImage_URL"

		AWS_PageThumbnail_URL = row[14]
		AWS_PageThumbnail_URL_name = "AWS_PageThumbnail_URL"
		
		
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

		drawingsubsubChild(PageNumber_1903, PageNumber_1903_name)
		drawingsubsubChild(IIIF_Page_URL, IIIF_Page_URL_name)
		drawingsubsubChild(AWS_PageImage_URL, AWS_PageImage_URL_name)
		drawingsubsubChild(AWS_PageThumbnail_URL, AWS_PageThumbnail_URL_name)


# write XML file
ElementTree(root).write("xml_1903pagenumbers_22August.xml", encoding="UTF-8", xml_declaration=True, default_namespace=None)