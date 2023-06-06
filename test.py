import time
import random



money_value = 1000
money = "{: }".format(money_value)

name = input('Hello, what is you name? ')

print('Nice to meet you' , name ,  ':D')

time.sleep(0.5)

while True:


    rba = input('How much would you like to bet? ')
    #roulette bid amount
    

    while True:

        if not int(rba) > 0 :
            print('Sorry' , ', you need to bet more than zero')
            time.sleep(2)
            continue

        elif int(rba) > int(money) :
            print('Insufficient funds | Balance available : $' , money)
            continue

        else :
            break
        
        
    

    def bet() :   
        
        rbp = input("What would you like to bet on? ")
        options = ["red", "black", "odd", "even", "high", "low"]
            
        for o in options :
            if rbp.lower() == o :
                print('Placing your bet on' , o)
                return rbp

        for i in range(1,36):
            if rbp == str(i) :
                print('Placing your bet on' , i)
                return rbp

        else :
            print('Sorry, I did not understand this' , name)
        bet()
    rbp = bet()



    time.sleep(1.5)

    print("Spinning wheel")

    time.sleep(random.randint(2,5))
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    

    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]

    low = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    high = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    first_12 = [1,2,3,4,5,6,7,8,9,10,11,12]
    second_12 = [13,14,15,16,17,18,19,20,21,22,23,24]
    third_12 = [25,26,27,28,29,30,31,32,33,34,35,36,]

    pick = (random.randint(1,36))

    win_2to1 = (int(rba)*2)
    win_3to1 = (int(rba)*3)
    win_36to1 = (int(rba)*36)




#number
    try :
        if pick == int(rbp) :
            print('You win! Here is your win $' , win_36to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_36to1))
            money = (int(money) + win_36to1)
    except :
#colour
        if pick in black and (rbp == 'black')  :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)

        elif pick in red and (rbp == 'red') :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)
    #high low
        elif pick in high and (rbp == 'high') :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)

        elif pick in low and (rbp == 'low') :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)
    #even odd
        elif pick in odd and (rbp == 'odd') :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)

        elif pick in even and (rbp == 'even') :
            print('You win! Here is your win $' , win_2to1)
            time.sleep(1)
            print('Your total is : $' , (int(money) + win_2to1))
            money = (int(money) + win_2to1)

        else :
            print('You lost.. better luck next time!')
            time.sleep(1)
            print('Your total is : $' , (int(money) - int(rba)))
            money = (int(money) - int(rba))
            print(pick)
            print(rbp)

    if 0 >= int(money) :
        print('If you wish to continue, deposit money here :')





    continue