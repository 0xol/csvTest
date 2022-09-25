import csv
import time

salesRepFile = open("salesRep.csv", newline = '')
vendJournalFile = open("vendJournal.csv", newline = '')

salesRep = csv.reader(salesRepFile)
vendJournal = csv.reader(vendJournalFile)

for row in salesRep:
    print(row)

for row in vendJournal:
    print(row)