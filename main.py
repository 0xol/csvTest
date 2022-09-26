'''

import csv
import time

Descriptions = {"Pur Accessories", "Pur Homewares", "Pur Manchester", "Pur Sundries", "Mens Wear", "Childrens Wear", "Accessories", "Book", "Electrical", "Homewares", "Manchester", "Sundries", "Women wear", "Discount Allowed", "Donation", "Discount Allowed", "COGS", "30500", "Clearing - Bank", "Cash Total", " EFTPOS Total"}

allStores = set(())

salesRepFile = open("salesRep.csv", newline = '')
vendJournalFile = open("vendJournal.csv", newline = '')

salesRep = csv.reader(salesRepFile)
vendJournal = csv.reader(vendJournalFile)

for row in salesRep:
    column = list(row)
    allStores.add(column[0])

for row in vendJournal:
    column = list(row)
    allStores.add(column[2])

#weird bug with csv functions

allStores.remove('')
allStores.remove('Revenue')
allStores.remove('OutletName')
allStores.remove('Margin (%)')
allStores.remove('Cost of Goods Sold')
allStores.remove('Revenue (Incl. Tax)')
allStores.remove('Tax')

print("TEST")

for row in vendJournal:
    column = list(row)
    print(column)

print("TEST")

print(allStores)

'''

import panda as pd

df = pd.read_csv('salesRep.csv')

print(df) 