hour =  1
min = hour*60
sec1 = min *60


print(sec1)
hour = 24
min = hour*60
sec2 = min *60
print(sec2)
print(sec2/sec1)
print(sec2//sec1)

def cal_time(x):
    s = x*60*60
    print(s)
    return(s)

s1 = cal_time(x=1)
s2 = cal_time(x=24)
t = s2/s1
print(t)

