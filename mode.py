import csv
from collections import Counter
with open('SOCR-HeightWeight.csv') as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
m  = len(newData)
data = Counter(newData)
modeDataRange = {
    '50-100':0,
    '100-150':0,
    '150-200':0
}
for Height,occurence in data.items():
    if(100<float(Height)<150):
        modeDataRange['100-150']+=occurence
    elif(150<float(Height)<200):
        modeDataRange['150-200']+=occurence
    elif(200<float(Height)<250):
        modeDataRange['200-250']+=occurence

modeRange,modeOccurence = 0,0
for Range,occurence in modeDataRange.items():
    if(occurence>modeOccurence):
        modeRange,modeOccurence=[int(Range.split('-')[0]),int(Range.split('-')[1])],occurence
mode = float((modeRange[0]+modeRange[1])/2)
print(mode)
