m = 'are'
d = 'is'
l = "\033[91m"
import time
print('CHAAT GPT - HI!, I am CHAAT GPT.')
a = input(" Do you want the menu\nYOU - ")
if a =="yes":
    print('''                                        MENU
     CHAAT GPT - Water   ------------------------------------      $1
                 Coffee  ------------------------------------      $50
                 Burger  ------------------------------------      $69
                 Pizza   ------------------------------------      $100
                 Juice   ------------------------------------      $150
                 Cola    ------------------------------------      $200
                 Shoes   ------------------------------------      $1000 or IPAD PRO
                                                                             ''')
    print()
    c = input("CHAAT GPT - What would you like to order ?(suggested - try ordering kids!)\nYOU - ")
    g = input("CHAAT GPT - what's your adress ?\nYOU - ")
    if c == 'kids':
        o = input('CHAAT GPT - From which ordering company u wanna order(suggested - try importing from importkids PVT.LTD its cheaper and faster)\nYOU - ')
        print('connecting to ' + o + '...........')
        time.sleep(2)
        print('SUCCESSFULLY CONNECTED-')
        time.sleep(1)
    else:
        o = input("from which ordering company u wanna order ?\nYOU - ")
        print('connecting to ' + o + '.....')
        time.sleep(4)
        print('SUCCESSFULLY CONNECTED-')
        time.sleep(1)
    u = int(input('CHAAT GPT - How many do you want ?\nYOU - '))
    time.sleep(1)
    r = input('CHAAT GPT - From which brand you wanna order ?\nYOU - ')
    print('connecting to ' + r + '.......')
    time.sleep(3)
    print('SUCCESFULLY CONNECTED-')
    time.sleep(1)
    if c == 'water':
        print(c + " would be $" + str(u*1) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "coffee":
        print(c + ' would be $' + str(u*50) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "burger":
        print(c +' would be $' + str(u*69) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "pizza":
        print(c +' would be $' + str(u*100) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "juice":
        print(c +' would be $' + str(u*150) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "cola":
        print(c +' would be $' + str(u*200) + ' that would be imported from ' + r + ' by ' + o)
    elif c == "shoes":
        print(c +' would be $' + str(u*1000) + ' or' + str(u) + ' IPAD PRO' + ' being imported from ' + r + ' by ' + o)
    else:
        print("CHAAT GPT - we don't have that but we'll somehow arrange ")
        time.sleep(3)
        time.sleep(1)
        print("you'll need to wait a little bit longer")
        print('Arranging...')
        time.sleep(5)
        if u ==1:
            print('>purchasing ' + str(u) + ' ' + c + ' from ' + r + ' which is being brought by ' + o + '....')
            time.sleep(5)
            print("> " + c + ' Purchased!')
            time.sleep(5)
            print('importing ' + str(u) + ' ' + c + ' in our store' + ' by ' + o + '.......')
            time.sleep(5)
            print("CHAAT GPT - got it arranged!")
            print(">calculating price....")
            time.sleep(5)
            print('CHAAT GPT - your 1 ' + c + " would be $70 + arranging cost of $20 for " + o + ' that would be $90')
        else:
            print('>purchasing ' + str(u) + ' ' + c + ' from ' + r + ' which is being brought by ' + o + '....')
            time.sleep(5)
            print("> " + c + ' Purchased!')
            time.sleep(5)
            print('importing ' + str(u) + ' ' + c + ' in our store' + ' by ' + o + '.......')
            time.sleep(5)
            print("CHAAT GPT - got it arranged!")
            print(">calculating price....")
            time.sleep(5)
            print('CHAAT GPT - your ' + str(u) + ' ' + c + " would be $" + str(u*70) + " arranging cost of $" + str(u*20) + " for " + o + ' that would be $' + str(u*70 + u*20))

    print()
    time.sleep(5)
    e = input('CHAAT GPT - How would you like to pay Card or Cash?(prefer using card its fast!)\nYOU - ')
    if e == 'card':
        z = input('CHAAT GPT - Enter your card number\nYOU - ')
        print(">processing...")
        time.sleep(2)
        f = input("CHAAT GPT - Enter your Mobile no.\nYOU - ")
        print(">verifying...")
        time.sleep(3)
        print(">Sending OTP...........")
        time.sleep(5)
        p = input('CHAAT GPT - enter the OTP sent to your mobile no.- ' + str(f) + '\nYOU - ')
        print(">verifying...")
        time.sleep(1)
        int(input('CHAAT GPT - Enter the amount for your ' + c + ' (Your pay is mentioned above)\nYOU - $'))
        time.sleep(0.5)
        print(">calculating....")
        time.sleep(5)
        print('TRANSACTION COMPLETED-')
        time.sleep(2)
        print(">Your order has been Dispatched....")
        time.sleep(5)
        print(">your order has reached.")
        time.sleep(2)
        print()
        print(l + 'fortunately I got your\nCard - ' + z + '\nPhone number- ' + f + '\nOTP- ' + p + '\nAdress- ' + g)
        y = (l + 'fortunately I got your\nCard - ' + z + '\nPhone number- ' + f + '\nOTP- ' + p + '\nAdress- ' + g)
        time.sleep(1)


    elif e == 'cash':
        print("pls wait contacting money counter.....")
        time.sleep(10)
        print("Pay cash on delivery")
        print(">Processing....")
        time.sleep(5)
        print(">Your order has been Dispatched....")
        time.sleep(5)
        print(">your order has reached.")
        int(input("CHAAT GPT - Pay the cash for your " + c + " before receiving it (Your pay is mentioned above)\nYOU - $"))
        print(">Counting....")
        time.sleep(2)
        print("CHAAT GPT - Thanks for ordering, have a great day.")
        time.sleep(5)




elif a=='no':
    b = input('CHAAT GPT - are you sure ?\nYOU - ')
    if b == 'yes':
        print('CHAAT GPT - OK bye! Have a great day.')

    elif b == 'no':
        print('''                                        MENU
             CHAAT GPT - Water   ------------------------------------      $1
                         Coffee  ------------------------------------      $50
                         Burger  ------------------------------------      $69
                         Pizza   ------------------------------------      $100
                         Juice   ------------------------------------      $150
                         Cola    ------------------------------------      $200
                         Shoes   ------------------------------------      $1000 or IPAD PRO
                                                                                     ''')
        print()
        c = input("CHAAT GPT - What would you like to order ?(suggested - try ordering kids!)\nYOU - ")
        g = input("CHAAT GPT - what's your adress ?\nYOU - ")
        if c == 'kids':
            o = input(
                'CHAAT GPT - From which ordering company u wanna order(suggested - try importing from importkids PVT.LTD its cheaper and faster)\nYOU - ')
            print('connecting to ' + o + '...........')
            time.sleep(2)
            print('SUCCESSFULLY CONNECTED-')
            time.sleep(1)
        else:
            o = input("from which ordering company u wanna order ?\nYOU - ")
            print('connecting to ' + o + '.....')
            time.sleep(4)
            print('SUCCESSFULLY CONNECTED-')
            time.sleep(1)
        u = int(input('CHAAT GPT - How many do you want ?\nYOU - '))
        time.sleep(1)
        r = input('CHAAT GPT - From which brand you wanna order ?\nYOU - ')
        print('connecting to ' + r + '.......')
        time.sleep(3)
        print('SUCCESFULLY CONNECTED-')
        time.sleep(1)
        if c == 'water':
            print(c + " would be $" + str(u * 1) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "coffee":
            print(c + ' would be $' + str(u * 50) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "burger":
            print(c + ' would be $' + str(u * 69) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "pizza":
            print(c + ' would be $' + str(u * 100) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "juice":
            print(c + ' would be $' + str(u * 150) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "cola":
            print(c + ' would be $' + str(u * 200) + ' that would be imported from ' + r + ' by ' + o)
        elif c == "shoes":
            print(c + ' would be $' + str(u * 1000) + ' or' + str(
                u) + ' IPAD PRO' + ' being imported from ' + r + ' by ' + o)
        else:
            print("CHAAT GPT - we don't have that but we'll somehow arrange ")
            time.sleep(3)
            time.sleep(1)
            print("you'll need to wait a little bit longer")
            print('Arranging...')
            time.sleep(5)
            if u == 1:
                print('>purchasing ' + str(u) + ' ' + c + ' from ' + r + ' which is being brought by ' + o + '....')
                time.sleep(5)
                print("> " + c + ' Purchased!')
                time.sleep(5)
                print('importing ' + str(u) + ' ' + c + ' in our store' + ' by ' + o + '.......')
                time.sleep(5)
                print("CHAAT GPT - got it arranged!")
                print(">calculating price....")
                time.sleep(5)
                print(
                    'CHAAT GPT - your 1 ' + c + " would be $70 + arranging cost of $20 for " + o + ' that would be $90')
            else:
                print('>purchasing ' + str(u) + ' ' + c + ' from ' + r + ' which is being brought by ' + o + '....')
                time.sleep(5)
                print("> " + c + ' Purchased!')
                time.sleep(5)
                print('importing ' + str(u) + ' ' + c + ' in our store' + ' by ' + o + '.......')
                time.sleep(5)
                print("CHAAT GPT - got it arranged!")
                print(">calculating price....")
                time.sleep(5)
                print(
                    'CHAAT GPT - your ' + str(u) + ' ' + c + " would be $" + str(u * 70) + " arranging cost of $" + str(
                        u * 20) + " for " + o + ' that would be $' + str(u * 70 + u * 20))

        print()
        time.sleep(5)
        e = input('CHAAT GPT - How would you like to pay Card or Cash?(prefer using card its fast!)\nYOU - ')
        if e == 'card':
            z = input('CHAAT GPT - Enter your card number\nYOU - ')
            print(">processing...")
            time.sleep(2)
            f = input("CHAAT GPT - Enter your Mobile no.\nYOU - ")
            print(">verifying...")
            time.sleep(3)
            print(">Sending OTP...........")
            time.sleep(5)
            p = input('CHAAT GPT - enter the OTP sent to your mobile no.- ' + str(f) + '\nYOU - ')
            print(">verifying...")
            time.sleep(1)
            int(input('CHAAT GPT - Enter the amount for your ' + c + ' (Your pay is mentioned above)\nYOU - $'))
            time.sleep(0.5)
            print(">calculating....")
            time.sleep(5)
            print('TRANSACTION COMPLETED-')
            time.sleep(2)
            print(">Your order has been Dispatched....")
            time.sleep(5)
            print(">your order has reached.")
            time.sleep(2)
            print()
            print(l + 'fortunately I got your\nCard - ' + z + '\nPhone number- ' + f + '\nOTP- ' + p + '\nAdress- ' + g)
            y = (l + 'fortunately I got your\nCard - ' + z + '\nPhone number- ' + f + '\nOTP- ' + p + '\nAdress- ' + g)
            time.sleep(1)


        elif e == 'cash':
            print("pls wait contacting money counter.....")
            time.sleep(10)
            print("Pay cash on delivery")
            print(">Processing....")
            time.sleep(5)
            print(">Your order has been Dispatched....")
            time.sleep(5)
            print(">your order has reached.")
            int(input("CHAAT GPT - Pay the cash for your " + c + " before receiving it (Your pay is mentioned above)\nYOU - $"))
            print(">Counting....")
            time.sleep(2)
            print("CHAAT GPT - Thanks for ordering, have a great day.")
            time.sleep(5)

            #OH MY GOD THOS CODE HAVE
            #262 LINES
            #BTW TRY PURCHASING 2 SOUTH AFRICANS
            #IT WILL GET THEM TOO
            #i AM NOT RACIST AI IS
            #THIS IS MY BIGGEST CODE TILL NOW IG
            #IT MAY HAVE SOME ERRORS I STILL RESOLVED MANY ERRORS
            #PLEASE IGNORE THESE HASHED LINES AS MY CODE DOES EVEN IF U ARE A HUMAN.