# assignment52.py
num=0
tot=0
lst=[]
while True:
    sval=input('Enter a number: ')
    if sval == 'done':
        break
    try:
        ival=int(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    lst.append(ival)
    #num=num+1
    #tot=tot+fval

#print('ALL DONE')
#print('The total is: ', tot,'Numbers used are: ', num,'Average is: ', tot/num)
print('Maximum is: ', max(lst))
print('Minimum is: ', min(lst))