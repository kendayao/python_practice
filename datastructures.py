# list
[0,0,0]
[0]*3 

list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)

d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])

for num in range(10):
    print(num)