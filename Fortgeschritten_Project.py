# Datei einlesen
import csv
f = open("guns.csv", "r")
data = list(csv.reader(f))

print(data[:5]) # Test-Ausgabe


# Headers der Daten entfernen
headers = data[:1]
data = data[1:]

print(headers) # Test-Ausgabe
print(data[:5]) # Test-Ausgabe


# Schusswaffen-Tode per Jahr
years = [row[1] for row in data]
year_counts = {}

for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
		 
print(year_counts) # Test-Ausgabe


# Schusswaffen-Tode per Monat und Jahr
import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]

print(dates[:5]) # Test-Ausgabe

date_counts = {}

for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
		
print(date_counts) # Test-Ausgabe


# Schusswaffen-Tode per Rasse und Geschlecht
sexes = [row[5] for row in data]
sex_counts = {}

for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex] +=  1
    else:
        sex_counts[sex] = 1
		
print(sex_counts) # Test-Ausgabe

races = [row[7] for row in data]
race_counts = {}

for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
		
print(race_counts) # Test-Ausgabe


# Zweites Dataset einlesen
f = open("census.csv", "r")
census = list(csv.reader(f))
print(census) # Test-Ausgabe


# Rate von Schusswaffen-Tode per Rasse
mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Black": 40250635,
    "Native American/Native Alaskan": 3739506,
    "Hispanic": 44618105,
    "White": 197318956
}
race_per_hundredk = {}

for k,v in race_counts.items():
    race_per_hundredk[k] = (v/mapping[k]) * 100000

print(race_per_hundredk) # Test-Ausgabe


# Filtern nach Suizid
intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}

for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

print(race_per_hundredk) # Test-Ausgabe

