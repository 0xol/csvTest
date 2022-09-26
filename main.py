import pandas as pd

salesRep = pd.read_csv("salesRep.csv")
vendJournal = pd.read_csv("vendJournal.csv")

print(vendJournal.loc[vendJournal["OutletName"] == "Windsor"])

print(salesRep.loc[salesRep["Outlet"] == "Windsor"])