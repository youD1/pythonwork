guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me == 7:
    print('just right')
else:
    print('too high')

start = 1
guess_me = 7
while 1:
    if start < guess_me:
        print('too low')
    elif(start == guess_me):
        print('find it')
    else:
        print('oops')
        break

    start += 1
for x in range(3,-1,-1):
    print(x)

#偶数序列
def odds(x):
for x in range(0,9):
    if x % 2 ==0:
        print(x)
    continue

squares = {key=odds(x):}