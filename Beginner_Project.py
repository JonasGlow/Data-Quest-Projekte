# Datei einlesen
f = open("US_births_1994-2003_CDC_NCHS.csv", "r").read()
rows = f.split("\n")
print(rows[0:11]) # Test-Ausgabe

# Allgemeine Funktion um Dateien einzulesen und dabei die Header Row zu entfernen und die Felder richtig umzuwandeln
def read_csv(file):
    string_data = open(file).read().split("\n")
    string_list = string_data[1:len(string_data)-1]
    final_list = []
    
    for row in string_list:
        int_fields = []
        string_fields = row.split(",")
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:11]) # Test-Ausgabe

# Funktion um die Geburten pro Monat zu bestimmen
def month_births(tempList):
    births_per_month = {}
    for row in tempList:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month
	
cdc_month_births = month_births(cdc_list)
print(cdc_month_births) # Test-Ausgabe

# Funktion um die Geburten pro Wochentag zu bestimmen
def dow_births(tempList):
    births_per_day = {}
    for row in tempList:
        day = row[3]
        births = row[4]
        if day in births_per_day:
            births_per_day[day] += births
        else:
            births_per_day[day] = births
    return births_per_day
cdc_day_births = dow_births(cdc_list)
print(cdc_day_births) # Test-Ausgabe


# Allgemeine Funktion um die Geburten für die übergebene Column zu berechnen
def calc_counts(data, column):
    number_of_births = {}
    for row in data:
        col_value = row[column]
        births = row[4]
        if col_value in number_of_births:
            number_of_births[col_value] += births
        else:
            number_of_births[col_value] = births
    return number_of_births
	
cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)

print(cdc_year_births) # Test-Ausgabe
print(cdc_month_births) # Test-Ausgabe
print(cdc_dom_births) # Test-Ausgabe
print(cdc_dow_births) # Test-Ausgabe
