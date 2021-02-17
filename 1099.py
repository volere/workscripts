import pandas as pd
import numpy as np

#I use this script to parse through quickbooks transactions
#for how much I have paid my contractors
# I added tags for each of my contractors

class Contractor:
    def __init__(self, name, values):
        self.name = name
        self.values = [] 
    def myfunc(self):
        print("totals for " + self.name)
    def setValues(self):
        number = np.sum(self.values)
        return number  * 1
    def sumValues(self):
        print(np.sum(self.values))


        
##I've removed names and Strings you will have to insert your own strings
##you can create as many instances as you have contractors

p1 = Contractor("p1",0)
p2 = Contractor("p2",0)
p3 = Contractor("p3",0)

data = pd.read_csv('PATH_TO_CSV')
df = pd.DataFrame(data, columns = ['Date', 'Description', 'Amount'])
################Grab and print person 1
Name1 = df[df['Description'].str.contains('STRING')].Amount
p1.values=Name1
p1.myfunc()
p1.sumValues()
##########Grab and print person 2
Name2 = df[df['Description'].str.contains('STRING',regex=True)].Amount
p2.values = Name2 
p2.myfunc()

p2.sumValues()
###############Grab and print person 3
Name3 = df[df['Description'].str.contains('STRING')].Amount
p3.values = Name3
p3.myfunc()

p3.sumValues()

#checks total of collected values for to check for 

print(p1.setValues()+ p2.setValues()+p3.setValues())