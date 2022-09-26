import csv
import time

Descriptions = {"Pur Accessories", "Pur Homewares", "Pur Manchester", "Pur Sundries", "Mens Wear", "Childrens Wear", "Accessories", "Book", "Electrical", "Homewares", "Manchester", "Sundries", "Women wear", "Discount Allowed", "Donation", "Discount Allowed", "COGS", "30500", "Clearing - Bank", "Cash Total", " EFTPOS Total"}

allStores = {}

salesRepFile = open("salesRep.csv", newline = '')
vendJournalFile = open("vendJournal.csv", newline = '')

salesRep = csv.reader(salesRepFile)
vendJournal = csv.reader(vendJournalFile)

for row in salesRep:
    column = list(row)
    allStores.append(column[0]) if column not in allStores else allStores

for row in vendJournal:
    column = list(row)
    allStores.append(column[0]) if column not in allStores else allStores

print(allStores)