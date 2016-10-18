#
# Alexander Keller <alexander.keller@uoit.ca>
# Mohammed Savari <mohammed.savari@uoit.net>
#

import time

# Start the clock
start = time.time()

print('------------------------------------------------------------------------')
print('Running...')
#-------------------------------------------------------------------------------

myFile = open("movies.dat")

myTable = {}
tHold = 0.03
lines = myFile.readlines()


for line in lines:
    for item1 in line.split():
        for item2 in line.split():
            for item3 in line.split():
                if item1 < item2 < item3:
                    if item1 + ", " + item2 + ", " + item3 not in myTable:
                        myTable[item1 + ", " + item2 + ", " + item3] = 1
                    else:
                        myTable[item1 + ", " + item2 + ", " + item3] += 1
ordered = []

for pair in myTable:
    if myTable[pair] > (len(lines) * tHold):
        ordered.append([myTable[pair], pair])

ordered.sort(reverse=True)

total = 0
for i in ordered:
    total+=1
    print(total, ')', i[1], i[0])


#scan all items put in table1
#delete any items that does not meet threshold

#-------------------------------------------------------------------------------
print('Done!')

# Stop the clock
end = time.time()
print('Time taken in seconds:', end - start)
