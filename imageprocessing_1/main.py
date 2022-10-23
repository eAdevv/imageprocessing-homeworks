
#if statement

number = 26
if number < 26:
    print("number is smaller than 26")
elif number == 26:
    print("number is equal to 26")
else:
    print("number is bigger than 26")

#while statement

while number < 26:
    print("Number is :", number)
    number= number+1

#average
def getNumber():
    n= int(input("How many numer will be entered : "))
    a=[]
    for i in range (0,n):
        elem= int(input("enter a number : "))
        a.append(elem)
    avg = sum(a)/n
    print("Average is :",round(avg,2))

getNumber()