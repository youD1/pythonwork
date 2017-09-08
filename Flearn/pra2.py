years_list = [1994,1995,1996,1997,1998]
years_list[2]
len(years_list)
years_list[len(years_list)-1]
years_list[-1]
thing =['mozzarella','cinderella','salmonella']

#首字母大写
def normalize(name):
    return name.capitalize()
thing1 = list(map(normalize,thing))
print(thing1)

#字母大写
def name_upper(name):
    return name.upper()
thing2 = (list(map(name_upper,thing1[0])))
joined = ''.join(thing2)
thing1[0]=joined
print(thing1)
thing3 = thing1.pop(2)
print(thing1)

surprise = ['Groucho','Chico','Harpo']

#字母小写
def name_lower(name):
    return name.lower()

surprise1 = list(map(name_lower,surprise[2]))
joined2 = ''.join(surprise1)
surprise[2] = joined2

print(surprise)

e2f = [['dog','chien'],['cat','chat'],['walrus','morse']]
f = dict(e2f)
print(f['walrus'])
f2e = {value:key for key, value in f.items()}
print(f2e['chien'])




life = {'animals':{'cats':{'Henris','Grumpy','Lucy'},'octopi':{},'emus':{}},'plants':{},'others':{}}

print(life)
print(life['animals'])
print(life['animals']['cats'])


life1 = ['animals1','plants','others']
animals1 = ['cats1','octopi','emus']
cats1 = ['Henris','Grumpy','Lucy']
dict_life={'life1':life1,'animals1':animals1,'cat1':cats1}
print(dict_life)
print(dict_life['animals1'])
print(dict_life['animals1']['cats1'])
