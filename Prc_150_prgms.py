#Source of practice is W3 resources

'''pi=3.14
rad=int(input('give radius: '))
Area=pi*rad*rad

print(Area)'''

'''fn=input('what is first name: ')
ln=input('what is last name: ')
print(ln+' '+fn)'''

'''
values= input('enter numbers with comma')
list1=values.split(',')
print(list1)
tuple1=tuple(list1)
print(tuple1)'''

'''fn=input('file name: ')
op=fn.split('.')
print(op)
print(op[-1])
'''

'''color_list = ["Red","Green","White" ,"Black"]
print(color_list[0::3])'''
# chk this
'''exam_st_date = (11, 12, 2014)
l=list(exam_st_date)
st='/'.join(str(e) for e in l)
print(st)'''

#Doubt
'''n=int(input('enter number: '))
s1=str(n)
s2=str(n)
s3=int(s1+s2)
print(s3)'''


#what is abs value

'''a=int(input('num1: '))
b=int(input('num2: '))
c=int(input('num3: '))
sum1=a+b+c
if a==b==c:
    print(sum1*3)
else:
    print(sum1)'''


'''str=input('enter a string: ')
if 'Is' in str:
    print(str)
else:
    print('Is'+ ' '+str)'''


'''s=input('String: ')
print(s*3)'''


'''li=[1,2,4,4,5,6,4,7]
count=0
for i in li:
    if i==4:
        count=count+1
print('number of 4s are: '+''+ str(count))'''

'''st=input('enter string: ')
if len(st)==2:
    print(len(st))
    print(st)'''

'''x=st.split()
print(x)
'''

'''n=int(input('enter number'))
sum=f'{n}{n{n}}{n{n}{n}}'
print(sum)'''


'''exam_st_date = (11, 12, 2014)

print(type(exam_st_date))

nd=str(exam_st_date)
z=nd.replace(',','/')
print(z)'''




'''n=int(input('enter number: '))

n1=str(n)
sum1=n+int(n1+n1)+int(n1+n1+n1)
print(f'{n1}+{n1+n1}+{n1+n1+n1}={sum1}')'''




'''exam_st_date = (11, 12, 2014)
l=list(exam_st_date)
print(l)
st='/'.join(str(e) for e in l)
print(st)'''



'''def add2(a,b):
    return a+b

print(add2(2,3))'''


'''
s='Srikanth'
n=int(input('enter value of n'))
s=s[0:2]
print(s)
st=s*n
print(st)
'''
'''
vowels=['a','e','i','o','u']
st=input('enter string: ')
if st in vowels:
    print(f'{st} is a vowel')
else:
    print(f'{st} is not a vowel')
'''

'''
l=[1.5,8,3]
x=int(input('enter a num'))
if x in l:
    print('True')
else:
    print ('False')

'''

'''
li=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527]
for num in li:  
    if  num==237:
        break
    elif num%2==0:
        print(num)
'''      
        


'''

x=0
y=0
#printing tables 
#for x in range(1,11):
    #for y in range(1,11):
        #print(f'{x}x{y}=',x*y)

        #print(f'{x}x{x}=' , x*x)
'''

'''for x in range(4):
    
    for y in range(x+1):
        
        print('.', end='')
    print()
'''
'''for x in range(4):
    for y in range(4-x):
         print('.', end='')
    print()'''
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
final=color_list_1 acolor_list_2
print(final)
'''
import json

person = {"name": "Asabeneh",    "country": "Finland",    "city": "Helsinki",    "skills": ["JavaScrip", "React", "Python"]}




with open('example2.json','r') as file:
    x=json.load(file)
print(type(x))
print(x)
    #f.write(str(person))



    

        



