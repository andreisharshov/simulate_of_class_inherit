NumberClasses = int(input())
i = 0

inheritment = {}

def getInh(parent, inherit):
    ans = 0
    a = inheritment.get(parent)
    b = a.get('inh')
    if inherit in b:
        print('Yes')
        return 1
    else:
        for J in b:
            parent = J
            ans = getInh(parent, inherit)
            if ans == 1:
                break
    if ans == 0:
        print('No')
        
        
        
        
    

def addClass(x):
    if x not in inheritment:
        dictionary = dict.fromkeys([x],{'inh':[]})
        inheritment.update(dictionary)        
                    
while NumberClasses > i:
    inputClasses = input()
    listClasses = inputClasses.split(' ')
    if len(listClasses) == 1:
        dictionary = dict.fromkeys([listClasses[0]],{'inh':[]})
        inheritment.update(dictionary)
    else:
        del listClasses[1]
        for I in listClasses:
            addClass(I)
        tmp = listClasses[0]
        del listClasses[0]
        for I in listClasses:
            a = inheritment.get(I)
            b = a.get('inh')
            b.append(tmp)
            dictionary = dict.fromkeys([I],{'inh':b})
            inheritment.update(dictionary)
    i += 1

print(inheritment)
NumberTest = int(input())
j = 0
while NumberTest > j:
    try:
        parent, inherit = input().split()
    except ValueError:
        print('Yes')
    if inherit == parent:
        print('Yes')
    else:
        getInh(parent, inherit)
    j += 1
