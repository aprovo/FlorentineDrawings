import csv

with open('FlorentineDrawings_MissingData_FraPaolino-AntonioPollajuoloSchool - IdentifierPadding.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		identifier1 = row[0]
		identifier2 = str(identifier1)
		identifier3 = identifier2+"-Berenson"
		newidentifier = "{:0>20}".format(identifier3)
		print(identifier1, newidentifier)