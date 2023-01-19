#import pandas as pd
#import numpy as np
import csv
#df = pd.read_csv("Book4.csv")

#df = df.fillna(0)
champDict = {};
names= []
matrix = [];


with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file);
    for row in csv_reader:
        champDict[row["name"]] = row["relations"];


#Calculate the score of the team
def calcTeamScore(mat, champIDs):
    res = ""
    for i in range(0,4):
        for j in range(i+1,5):
            champ1 = champIDs[i]
            champ2 = champIDs[j]
            res += "(" + names[champ2] +"," +(mat[champ2][champ1]) +"), "
    return res


#Puts the names of the team together
def teamString(team, names):
    res = ""
    i=0
    while i<5:
        res += f"{names[team[i]]} "
        i +=1
    return res

def addChamp(newID):
    if newID in champDict:
        currentRelations = [];
        currDict = champDict[newID];
        for n in names:
            currentRelations.append(currDict[n]);
        matrix.append(currentRelations);
        names.append(newID);
    else:
        print(newID+ " is not a valid ID");

     
def remChamp(newID):
    if newID in names:
        i = names.index(newID);
        names.pop(i)
        matrix.pop(i)
        
        
        for x in range(i,len(matrix)):
            matrix[x].pop(i);
            
            
    else:
        print(newID+ " is not in current list");

def findBest():
    nsize = len(names)
    hnum = [nsize-5, nsize-4, nsize-3, nsize-2, nsize-1]
    max = calcTeamScore(matrix, hnum)
    
    
    
    for i1 in range (0, nsize-5):
        for i2 in range (i1+1, nsize-3):
            for i3 in range (i2+1, nsize-2):
                for i4 in range (i3+1, nsize-1):
                    for i5 in range (i4+1, nsize):
                        cnum = [i1, i2, i3, i4, i5]
                        curr = calcTeamScore(matrix, cnum)
                        i5 += 1
                        print(curr)
                        
    
'''
                        if curr > max:
                            max = curr
                            for i in range(0,5):
                                hnum[i] = cnum[i]

    bestteam = teamString(hnum, names)
    print(max)
    print(bestteam)
    print(df)
    print(df2)

'''
    

while(1):
    val = input("Enter a command: ")
    if(val == "add"):
        x= [x for x in input("Enter any amount of championIDs: ").split()]
        for champs in x:
            addChamp(champs);
    elif(val == "remove"):
        x= [x for x in input("Enter any amount of championIDs: ").split()]
        for champs in x:
            remChamp(champs);
    elif(val == "run"):
        if(len(names) <5):
            print("Needs at least 5 champions to run")
        else:
            findBest();
    else:
        break;
    print("names: ")
    print(names)
    print("matrix: ")
    print(matrix)



'''

cname = ""
cscore = 0
max = 0
min = 0
nsize = len(df.index)
hnum = [nsize-5, nsize-4, nsize-3, nsize-2, nsize-1]

i1=0
while i1 <= nsize-6:
    i2 = i1+1
    i1 +=1
    while i2 <= nsize-4:
        i3 = i2+1
        i2 += 1
        while i3 <= nsize-3:
            i4 = i3+1
            i3 += 1
            while i4 <= nsize-2:
                i5 = i4+1
                i4 += 1
                while i5 <= nsize-1:
                    i5 += 1
                    cnum = [i1, i2, i3, i4, i5]
                    curr = calcTeamScore(matrix, cnum)
                    if curr > max:
                        max = curr
                        for i in range(0,5):
                            hnum[i] = cnum[i]

bestteam = teamString(hnum, names)
print(max)
print(bestteam)
print(df)
print(df2)
'''
