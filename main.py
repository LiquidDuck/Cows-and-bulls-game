import random

def user_number():
    print "Enter a number: "
    user_num=int(input(">>>"))
    return user_num
    
def cows_bulls(user_num,num):
    user_num=str(user_num)
    num=str(num)
    cows=0
    bulls=0
    for i, number in enumerate(user_num):
        if number in num:
            if number==num[i]:
                cows=cows+1
        if number in num:
            if number != num[i]:
                bulls=bulls+1
    return [cows, bulls]
    
num=random.randint(1000,10000)
tries=0
print "Welcome to the Cows and Bulls Game!"

while True:
    user_num=user_number()
    tries=tries+1
    result=cows_bulls(user_num,num)
    if user_num == num:
        break
    print str(result[0]) + " cows, " + str(result[1]) + " bulls"
    
print "You win! Your number of tries were: " + str(tries)