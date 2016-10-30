import time
import itertools

start = time.time()

print('------------------------------------------------------------------------')
print('Running...')
#-------------------------------------------------------------------------------

myFile = open('retail.dat')

tHold = 0.03
itemSet = 2

table = []
candidSet= {}
freqSet = {}
totalSet = {}

lines = myFile.readlines()
lines = lines[0:80000] 

myFile.close()

for line in lines:
   for item in line.split():
       if item not in candidSet:
           candidSet[item]=1
       else:
           candidSet[item]+=1
           
for item in candidSet:
   if candidSet[item] > (len(lines) * tHold):
       totalSet[item] = candidSet[item]
       freqSet[item] = candidSet[item]
       
for item in freqSet:
   for i in item.split(','):
       if i not in table:
           table.append(i)
           
while len(table) > itemSet:
   freqSet = {}
   candidSet = {}
   for sub in itertools.combinations(table, itemSet):
       candidSet[','.join(sub)] = 0
       
   for line in lines:
       for sub in itertools.combinations(line.split(), itemSet):
           for item in candidSet:
               if set(sub) == set(item.split(',')):
                   candidSet[item] +=1
                   
   for item in candidSet:
       if candidSet[item] > (len(lines) * tHold):
           totalSet[item] = candidSet[item]
           freqSet[item] = candidSet[item]
           
   table = []
   for item in freqSet:
       for i in item.split(','):
           if i not in table:
               table.append(i)         
   itemSet +=1

ordered = []

for pair in totalSet:
    if totalSet[pair] > (len(lines) * tHold):
        ordered.append([totalSet[pair], pair])

ordered.sort(reverse=True)

total = 0
for i in ordered:
    total+=1
    print(total, ')', i[1], ':', i[0])

#-------------------------------------------------------------------------------
print('Done!')

end = time.time()
print('Time taken in seconds:', end - start)

print(total, "results found!")
