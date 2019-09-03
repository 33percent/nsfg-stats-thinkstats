import sys
import modules.survey as survey

# 2.3.1
print('-------------------------')
print('example 2.3.1')
table = survey.Pregnancies()
table.ReadRecords()
df = table.records
print ('Number of pregnancies', len(df))

# exercise 2.3

'''available methods
table.GetFilename() - to retrieve all methods
table.GetFields() - to get all field names
table.records - the actual data
        return [
            ('caseid', 1, 12, int),
            ('nbrnaliv', 22, 22, int),
            ('babysex', 56, 56, int),
            ('birthwgt_lb', 57, 58, int),
            ('birthwgt_oz', 59, 60, int),
            ('prglength', 275, 276, int),
            ('outcome', 277, 277, int),
            ('birthord', 278, 279, int),
            ('agepreg', 284, 287, int),
            ('finalwgt', 423, 440, float),
            ]
'''
# 2.3.2
print('-------------------------')
print('example 2.3.2')
print('live births are where outcomes are 1')
print('No of live births: ',sum(1 for x in table.records if x.outcome == 1))


print('-------------------------')

# 2.3.3

print('example 2.3.3')
def getbirthOrders(data):
    firsts = []
    lasts = []
    count = 0;
    for x in data:
        if(x.outcome == 1 and x.birthord == 1):
            firsts.append(x)
        elif (x.outcome == 1):
            lasts.append(x)
    return firsts, lasts

firstbabies, otherbabies = getbirthOrders(df)
print('No of first babies',len(firstbabies))
print('No of non-first babies',len(otherbabies))
print('-------------------------')


print('example 2.3.4')
def averagepreg(data):
    total = sum(x.prglength for x in data if x.outcome == 1)
    count = len(data)
    return total/count;

firstBornAveragePreg = averagepreg(firstbabies)
otherBornAveragePreg = averagepreg(otherbabies)
print('Average weeks of first born babies',firstBornAveragePreg)
print('Average weeks of non-first born babies',otherBornAveragePreg)
print('difference between both of them is ',(firstBornAveragePreg - otherBornAveragePreg) * 7)
print('-------------------------')