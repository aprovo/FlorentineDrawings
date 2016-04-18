import csv

ArtistCellFilled_ListList = []

with open('FlorentineDrawings_SpreadsheetsCombined_v3 - FlorentineDrawings_CombinedSpreadsheets.csv', 'r', encoding="UTF-8") as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:

		###smaller list created in for loop so it resets evertime you get to a new row####
		ArtistCellFilled_List = []


		FlorentineDrawings_IdentifierBB1961 = row[0]
		FlorentineDrawings_IdentifierBB1961_name = "FlorentineDrawings_IdentifierBB1961"
		
		# City = row[1]
		# City_name = "City"
		
		# City_URI = row[2]
		# City_URI_name = "City_URI"
		
		# Country = row[3]
		# Country_name = "Country"
		
		# Country_URI = row[4]
		# Country_URI_name = "Country_URI"

		# Collection_main = row[5]
		# Collection_main_name = "Collection_main"
		
		# Collection_URI_main = row[6]
		# Collection_URI_main_name = "Collection_URI_main"

		# Collection_sub = row[7]
		# Collection_sub_name = "Collection_sub"
		
		# Collection_URI_sub = row[8]
		# Collection_URI_sub_name = "Collection_URI_sub"

		# Former_collection = row[9]
		# Former_collection_name ="Former_collection"

		# Former_collection_URI = row[10]
		# Former_collection_URI_name ="Former_collection_URI"

		# BB_1961_Inventory_number = row[11]
		# BB_1961_Inventory_number_name = "BB_1961_Inventory_number"

		# Inventory_number_correction = row[12]
		# Inventory_number_correction_name = "Inventory_number_correction"
		
		BB_1961_number_letter = row[13]
		BB_1961_number_letter_name = "BB_1961_number_letter"

		# BB_1961_number_letter_NoSpace = row[14]
		# BB_1961_number_letter_NoSpace_name = "BB_1961_number_letter_NoSpace"

		# BB_1961_figure_number_recto = row[15]
		# BB_1961_figure_number_recto_name = "BB_1961_figure_number_recto"

		# BB_1961_figure_number_verso = row[16]
		# BB_1961_figure_number_verso_name = "BB_1961_figure_number_verso"

		# BB_1961_plate_number = row[17]
		# BB_1961_plate_number_name = "BB_1961_plate_number"

		BB_1961_Artist_NoQualifier = row[18]
		BB_1961_Artist_NoQualifier_name = "BB_1961_Artist_NoQualifier"
	
		# Artist_URI_1961 = row[19]
		# Artist_URI_1961_name = "Artist_URI_1961"
	
		# BB_1961_Qualifier = row[20]
		# BB_1961_Qualifier_name = "BB_1961_Qualifier"

		# BB_1961_title_recto = row[21]
		# BB_1961_title_recto_name = "BB_1961_title_recto"

		# BB_1961_title_verso = row[22]
		# BB_1961_title_verso_name  = "BB_1961_title_verso"

		# BB_1961_title_correction = row[23]
		# BB_1961_title_correction_name = "BB_1961_title_correction"

		# BB_1961_technique_recto_1 = row[24]
		# BB_1961_technique_recto_1_name = "BB_1961_technique_recto_1"

		# BB_1961_technique_recto_1_URI = row[25]
		# BB_1961_technique_recto_1_URI_name = "BB_1961_technique_recto_1_URI"

		# BB_1961_technique_recto_2 = row[26]
		# BB_1961_technique_recto_2_name = "BB_1961_technique_recto_2"

		# BB_1961_technique_recto_2_URI = row[27]
		# BB_1961_technique_recto_2_URI_name = "BB_1961_technique_recto_2_URI"

		# BB_1961_technique_recto_3 = row[28]
		# BB_1961_technique_recto_3_name = "BB_1961_technique_recto_3"

		# BB_1961_technique_recto_3_URI = row[29]
		# BB_1961_technique_recto_3_URI_name = "BB_1961_technique_recto_3_URI"

		# BB_1961_technique_recto_4 = row[30]
		# BB_1961_technique_recto_4_name = "BB_1961_technique_recto_4"

		# BB_1961_technique_recto_4_URI = row[31]
		# BB_1961_technique_recto_4_URI_name = "BB_1961_technique_recto_4_URI"

		# BB_1961_technique_recto_5 = row[32]
		# BB_1961_technique_recto_5_name = "BB_1961_technique_recto_5"

		# BB_1961_technique_recto_5_URI = row[33]
		# BB_1961_technique_recto_5_URI_name = "BB_1961_technique_recto_5_URI"

		# BB_1961_technique_verso_1 = row[34]
		# BB_1961_technique_verso_1_name = "BB_1961_technique_verso_1"

		# BB_1961_technique_verso_1_URI = row[35]
		# BB_1961_technique_verso_1_URI_name = "BB_1961_technique_verso_1_URI"

		# BB_1961_technique_verso_2 = row[36]
		# BB_1961_technique_verso_2_name = "BB_1961_technique_verso_2"

		# BB_1961_technique_verso_2_URI = row[37]
		# BB_1961_technique_verso_2_URI_name = "BB_1961_technique_verso_2_URI"

		# BB_1961_technique_verso_3 = row[38]
		# BB_1961_technique_verso_3_name = "BB_1961_technique_verso_3"

		# BB_1961_technique_verso_3_URI = row[39]
		# BB_1961_technique_verso_3_URI_name = "BB_1961_technique_verso_3_URI"

		# BB_1961_technique_verso_4 = row[40]
		# BB_1961_technique_verso_4_name = "BB_1961_technique_verso_4"

		# BB_1961_technique_verso_4_URI = row[41]
		# BB_1961_technique_verso_4_URI_name = "BB_1961_technique_verso_4_URI"

		# BB_1961_text_recto = row[42]
		# BB_1961_text_recto_name = "BB_1961_text_recto"

		# BB_1961_text_verso = row[43]
		# BB_1961_text_verso_name = "BB_1961_text_verso"

		BB_1938_number_letter = row[44]
		BB_1938_number_letter_name = "BB_1938_number_letter"

		BB_1938_number_letter_NoSpace = row[45]
		BB_1938_number_letter_NoSpace_name = "BB_1938_number_letter_NoSpace"

		BB_1938_Artist_NoQualifier = row[46]
		BB_1938_Artist_NoQualifier_name = "BB_1938_Artist_NoQualifier"

		# Artist_URI_1938 = row[47]
		# Artist_URI_1938_name = "Artist_URI_1938"

		# BB_1938_Qualifier = row[48]
		# BB_1938_Qualifier_name = "BB_1938_Qualifier"

		# BB_1938_title_recto = row[49]
		# BB_1938_title_recto_name = "BB_1938_title_recto"

		# BB_1938_title_verso = row[50]
		# BB_1938_title_verso_name = "BB_1938_title_verso"

		# BB_1938_text_recto = row[51]
		# BB_1938_text_recto_name = "BB_1938_text_recto"

		# BB_1938_text_verso = row[52]
		# BB_1938_text_verso_name = "BB_1938_text_verso"

		BB_1903_number_letter = row[53]
		BB_1903_number_letter_name = "BB_1903_number_letter"

		BB_1903_number_letter_NoSpace = row[54]
		BB_1903_number_letter_NoSpace_name = "BB_1903_number_letter_NoSpace"

		BB_1903_Artist_NoQualifier = row[55]
		BB_1903_Artist_NoQualifier_name = "BB_1903_Artist_NoQualifier"

		# Artist_URI_1903 = row[56]
		# Artist_URI_1903_name = "Artist_URI_1903"

		# BB_1903_Qualifier = row[57]
		# BB_1903_Qualifier_name = "BB_1903_Qualifier"

		# BB_1903_title_recto = row[58]
		# BB_1903_title_recto_name = "BB_1903_title_recto"

		# BB_1903_title_verso = row[59]
		# BB_1903_title_verso_name = "BB_1903_title_verso"

		# BB_1903_text_recto = row[60]
		# BB_1903_text_recto_name = "BB_1903_text_recto"

		# BB_1903_text_verso = row[61]
		# BB_1903_text_verso_name = "BB_1903_text_verso"

		if BB_1961_Artist_NoQualifier != "" and BB_1961_number_letter != "":
			BB_1961_Artist_NoQualifier = BB_1961_Artist_NoQualifier


		if BB_1938_Artist_NoQualifier == "" and BB_1938_number_letter != "":
			BB_1938_Artist_NoQualifier_filled = BB_1961_Artist_NoQualifier
			

			ArtistCellFilled_List.append(FlorentineDrawings_IdentifierBB1961)
			ArtistCellFilled_List.append(BB_1961_Artist_NoQualifier)
			ArtistCellFilled_List.append(BB_1961_number_letter)
			ArtistCellFilled_List.append(BB_1938_number_letter)
			ArtistCellFilled_List.append(BB_1938_Artist_NoQualifier_filled)

		elif BB_1938_Artist_NoQualifier != "" and BB_1938_number_letter != "" :
			BB_1938_Artist_NoQualifier_filled = BB_1938_Artist_NoQualifier
			
			ArtistCellFilled_List.append(FlorentineDrawings_IdentifierBB1961)
			ArtistCellFilled_List.append(BB_1961_Artist_NoQualifier)
			ArtistCellFilled_List.append(BB_1938_number_letter)
			ArtistCellFilled_List.append(BB_1938_Artist_NoQualifier_filled)
		
		if BB_1903_Artist_NoQualifier == "" and BB_1903_number_letter != "":
			BB_1903_Artist_NoQualifier_filled = BB_1938_Artist_NoQualifier_filled
			
			ArtistCellFilled_List.append(BB_1903_number_letter)
			ArtistCellFilled_List.append(BB_1903_Artist_NoQualifier_filled)
			ArtistCellFilled_ListList.append(ArtistCellFilled_List)

		elif BB_1903_Artist_NoQualifier != "" and BB_1903_number_letter != "":
			BB_1903_Artist_NoQualifier_filled = BB_1903_Artist_NoQualifier
			
			ArtistCellFilled_List.append(BB_1903_number_letter)
			ArtistCellFilled_List.append(BB_1903_Artist_NoQualifier_filled)
			ArtistCellFilled_ListList.append(ArtistCellFilled_List)

####print the larger list in the same indendation you created the list####
#print(ArtistCellFilled_ListList)
		print(FlorentineDrawings_IdentifierBB1961, BB_1961_Artist_NoQualifier, BB_1938_number_letter, BB_1938_Artist_NoQualifier_filled, BB_1903_number_letter, BB_1903_Artist_NoQualifier_filled)


with open('FlorentineDrawings_AllArtistsFilledIn.csv', 'w', encoding="UTF-8") as f:
	writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	writer.writerows(ArtistCellFilled_ListList)
	#writer.writerow([FlorentineDrawings_IdentifierBB1961,BB_1961_Artist_NoQualifier,BB_1903_number_letter,BB_1903_Artist_NoQualifier_filled])


