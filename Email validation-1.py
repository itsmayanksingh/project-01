Email = input(' please enter a email : ')
k,j,d=0,0,0
# codition for email [once @, no space , all char  should be small latter , no comma , use dot and dot postion will
#   last ,minimum 6 char use and ]

if len(Email) >= 6:    #first off all we will check the length of email  and minimum charcter should be 6 or >=6 :
    if Email[0].isalpha():  # all charter should be in small latter 
        if ('@'in Email) and (Email.count("@")): #then we will count the @ in our email whic is enter by user
            if (Email[-4] == ".") ^ (Email[-3] == "."): # we will check the "." position   ----->  #    [^ (xor) ]  if both condations are true then we will get fals output and if one condtions is true then we will get a true  output
                for i in Email:  #loop will check the space , uppaer latter , and number's , and '@' , '_' , '.' etc.
                    if i==i.isspace():
                        k=1                      # define variable beacuse it will check the  [ > , < , % , ! , ^ , * , # ]
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i== "_" or i== "@" or i== ".":
                        continue
                    else:
                        d==1


                    if k==1  or j==1 or d==1:
                        print("wrong email 5")
                    else:
                        print('right email')
                        break
            else:
                print("Wrong email 4")
        else:
            print("Wrong email 3")
            
            
    else:

        print('Wrong email 2')

else:
    print('Wrong email 1')
