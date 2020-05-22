import math

print ('Hello WOrld') 
#%% Question 1
print('Total Seoconds is ' , 42 * 60 + 42)

#%% Question 2
print('Total Miles are ', 10 / 1.61)

#%% Question 3
print('Average pace per mile in minutes is ' , 6.211 / 42.7)
print('Average pace per mile in seconds is' , 6.211 / 2562)
print('Average speed in mph is ' , 6.211 / (42.7 / 60) )

#%% Question 4
print('Convert 1 Radian to Degree' , 1 * 180/math.pi )

#%% Question 5
h = 4
r = 6

v = math.pi * r ** 2 * h
print('Volume is', v)

#%% Question 6
R = 6373.0

lat1 = math.radians(69.96985432)
lon1 = math.radians(29.07573987)
lat2 = math.radians(63.1896464)
lon2 = math.radians(17.93575681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

Distance = R * c

print(Distance)


#%% Question 7
print('  ----   ')
print(' /    \\')
print(' /     \\')
print(' | STOP  |')
print(' \\     /   ')
print('  \\    / ')
print('    ----   ')
