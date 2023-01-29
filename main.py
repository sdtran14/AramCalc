#import pandas as pd
#import numpy as np
import csv
import ast


#df = pd.read_csv("Book4.csv")

#df = df.fillna(0)
champDict = {};
locked = []
names= []
matrix = [];
#print(type([1,2]))



#Calculate the score of the team
def calcTeamScore(mat, champIDs):
    res = 0;
    for i in range(0,4):
        for j in range(i+1,5):
            champ1 = champIDs[i]
            champ2 = champIDs[j]
            res += (float)(mat[champ2][champ1])
    return res


#Puts the names of the team together
def teamString(team):
    res = ""
    for i in team:
        res += f"{names[i]} "
    return res

def addChamp(newID):
    if(newID in champDict and newID not in names):
        currentRelations = [];
        currDict = champDict[newID];
        for n in names:
            currentRelations.append(currDict[n]);
        matrix.append(currentRelations);
        names.append(newID);
    else:
        print(newID+ " is not a valid ID");

def lockChamp(newID):
    if newID in names and newID not in locked:
        if(len(locked) <5):
            locked.append(newID)
    else:
        print(newID+" is not valid")
    
    
def unlockChamp(newID):
    if newID in names and newID in locked:
        locked.remove(newID)
    else:
        print(newID+" is not valid")
    
        
     
def remChamp(newID):
    if newID in names:
        i = names.index(newID);
        names.pop(i)
        matrix.pop(i)
        if(newID in locked):
            locked.remove(newID)
            
        
        for x in range(i,len(matrix)):
            matrix[x].pop(i);
            
            
    else:
        print(newID+ " is not in current list");


def findBest():
    nsize = len(names)
    hnum = [nsize-5, nsize-4, nsize-3, nsize-2, nsize-1]
    max = calcTeamScore(matrix, hnum)
    
    
    
    for i1 in range (0, nsize-5):
        #print(names[i1])
        for i2 in range (i1+1, nsize-3):
            for i3 in range (i2+1, nsize-2):
                for i4 in range (i3+1, nsize-1):
                    for i5 in range (i4+1, nsize):
                        cnum = [i1, i2, i3, i4, i5]
                        if(len(locked) > 0):
                            cnames = [names[i1], names[i2], names[i3], names[i4], names[i5]]
                            if not (all(x in cnames for x in locked)):
                                continue;
                        curr = calcTeamScore(matrix, cnum)
                        i5 += 1
                        #print (teamString(cnum))
                        #print(curr)
                        
                        if curr > max:
                            max = curr
                            for i in range(0,5):
                                hnum[i] = cnum[i]

    bestteam = teamString(hnum)
    print("The best team is:")
    print(bestteam)
    print("Their score is:")
    print(max)



with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file);
        for row in csv_reader:
            champDict[row["name"]] = ast.literal_eval(row["relations"])[0];


while(1):
    val = input("\nEnter a command: ")
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
    elif(val == "lock"):
        x= [x for x in input("Enter any amount of championIDs: ").split()]
        for champs in x:
            lockChamp(champs);
    elif(val == "unlock"):
        x= [x for x in input("Enter any amount of championIDs: ").split()]
        for champs in x:
            unlockChamp(champs)
    else:
        break;
    print("Current champs: ")
    print(names)
    if(len(locked)>0):
        print("Locked champs: ")
        print(locked)
   # print("matrix: ")
    #print(matrix)



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
