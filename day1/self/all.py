import sys
import modules.survey as survey
import modules.thinkstats as gen_stats
import modules.Pmf as pmf_fun

# 1.3.1
print('-------------------------')
print('example 1.3.1')
table = survey.Pregnancies()
table.ReadRecords()
df = table.records
print ('Number of pregnancies', len(df))

# exercise 1.3

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
# 1.3.2
print('-------------------------')
print('example 1.3.2')
print('live births are where outcomes are 1')
print('No of live births: ',sum(1 for x in table.records if x.outcome == 1))


print('-------------------------')

# 1.3.3

print('example 1.3.3')
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


print('example 1.3.4')
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



print('example 2.1')
def pumpkinStats(data):
    print('Mean - ',gen_stats.Mean(data))
    print('Variance - ',gen_stats.Var(data))
    print('standard deviation - ',gen_stats.Standard_deviation(data))

pumpkin_data = [3,3,591]
pumpkinStats(pumpkin_data)
print('-------------------------')

print('example 2.2')
def calculate_gestation(a,b):
    first_gest = [x.prglength for x in a if x.outcome == 1]
    other_gest = [x.prglength for x in b if x.outcome == 1]
    print('standard deviation of gestation period for first born - ',gen_stats.Standard_deviation(first_gest))
    print('standard deviation of gestation period for non-first born - ',gen_stats.Standard_deviation(other_gest))
calculate_gestation(firstbabies, otherbabies)
print('-------------------------')


print('*************')
print('Distributions')
t = [1,2,3,4,1,5,5,4,3,1,4,5,3,1]
hist = {}
for x in t:
    hist[x] = hist.get(x,0) + 1;

print(hist)
print('normalization of Distributions');
n = float(len(t))
pmf = {}
for x, freq in hist.items():
    pmf[x] = freq/n
print(pmf)
hist = pmf_fun.MakeHistFromList([1,2,2,3,5,5,5,5,2,2])
print(hist)
print('histogram frequency', hist.Freq(5))
print('histogram values', hist.Values())
for val in sorted(hist.Values()):
    print(val, hist.Freq(val))
print('*************')

print('-------------------------')
print('Example 2.3')

print('Mode of the hist - ',hist.Mode())
print('-------------------------')
