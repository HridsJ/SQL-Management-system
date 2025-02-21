import Book 

c = 'y'
while c.lower() == 'y' :
    print("Book Shop Management".center(89 , '='))
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice4 = int(input("Enter the serial number of your choice : "))
    if choice4 == 1 :
        Book.clrscreen()
        Book.add_user()
    elif choice4 == 2 :
        Book.clrscreen()
        if Book.login() :
            Book.clrscreen
            C = 'y'
            while C.lower() == 'y' :
                Book.clrscreen()
                print("Book Shop Management".center(89 , '='))
                print("1. Book Stock")
                print("2. Book Selling")
                print("3. Exit")
                choice = int(input("Enter the serial number of your choice : "))
                if choice == 1 :
                    Book.clrscreen()
                    print("Book Book".center(89 , '='))
                    print("1. Add a new Stock")
                    print("2. Update an existing Stock")
                    print("3. Exit")
                    choice2 = int(input("Enter the choice : "))
                    if choice2 == 1 :
                        Book.clrscreen()
                        Book.add_stock()
                    elif choice2 == 2 :
                        Book.clrscreen()
                        Book.update_stock()
                    elif choice2 == 3 :
                        print("Good Bye")
                        break
                    else : print("INVALID CHOICE")
                elif choice == 2 :
                    Book.clrscreen()
                    print('Book Selling'.center(89 , '='))
                    print('1. Sell a book')
                    print("2. Exit")
                    choice3 = int(input("Enter your choice : "))
                    if choice3 == 1 :
                        Book.clrscreen()
                        Book.sell_book()                   
                    elif choice3 == 2 : 
                        print("Good Bye")
                        break
                    else : print("INVALID CHOICE")
                elif choice == 3 : 
                    print("Good Bye")
                    break
                else : print("INVALID CHOICE")
                C = input("Do you want to continue (y/[n]) : ")
            else : print("Good Bye")
        else : 
            print("Either your username or password is incorrect")            
    elif choice4 == 3 :
        print("Good Bye")
        break
    else : print("INVALID CHOICE")
    c = input("Do you want to return to main menu (y/[n]) : ")
else : print("Good Bye")
        
