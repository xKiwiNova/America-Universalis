import csv
import os

class Province:
    id = 0
    r = 0
    g = 0
    b = 0
    name = ""
    terrain = ""
    culture = ""
    religion = ""
    tax = 0
    prod = 0
    man = 0
    tg = ""

    def __init__(self, i, r, g, b, n, t, c, re, ta, p, m, tg):
        self.id = i
        self.r = r
        self.g = g
        self.b = b
        self.name = n
        self.terrain = t
        self.culture = c
        self.religion = re
        self.tax = ta
        self.prod = p
        self.man = m
        self.tg = tg

    def str(self):
        return str(self.id) + " - " + self.name
    
    def toCSV(self):
        return [str(self.id), str(self.r), str(self.g), str(self.b), self.name,"x"]

cwd = os.getcwd()
file = open(cwd + '\TEMP\Provinces\settlement-plans.csv')

csvreader = csv.reader(file)
provinces = []

for province in csvreader:
    if len(province) == 12 and province[0]:
        provinces.append(Province(province[0], province[1], province[2], province[3], province[4], province[5], province[6], province[7], province[8], province[9], province[10], province[11]))

file.close()

defs = open(cwd + '\TEMP\Provinces\definitions.csv', 'r+',encoding='utf8')
olddefs = open(cwd + '\TEMP\Provinces\definitions_backup.csv', 'w',encoding='utf8')

new = csv.reader(defs)
old = csv.writer(olddefs)


for province in new:
    old.writerow(province)

writer = csv.writer(defs)
print()
for province in provinces:
    i = 0
    for row in new:
        if(i == province.id + 1):
            print(province.toCSV())
            writer.writerow(province.toCSV())
        else:
            writer.writerow(row)
        i += 1
    