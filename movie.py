import datetime
import os 
#create a  class for the Inox 


class Inox:
    
    #this is a construtor It is called automatic when class object create 
    def __init__(self):

        print("____________wlecome to Inox___________")


    '''kow i craete a staticmethod becuase know i want to create a function without a self 
       The function movie_list show movies running in inox 
       and ask your how many ticket he want to buy 
    ''' 
    @staticmethod
    def movie_list():
        print("1.KGF -- 3:00 PM \n2.Housefull -- 3:00 PM  \n3.Tu Jhuthi Me Makkar -- 3:00 PM")
        try:
            movie_choice=int(input("Enter movise choice: "))
      
        
            if movie_choice<4:    
                count=int(input("How many Ticket you want to buy: "))
                print("")
                
                if count<10:
                    i1.ticket_count(count,user_name)
                    
                    
                    if movie_choice==1:
                        print(f"Hello {user_name.capitalize()}\nYour Ticket Successfully Booked \n Movie : KGF \n Time: 3:00 PM\n Total Ticket: {count}")

                    elif movie_choice==2:
                        print(f"Hello {user_name.capitalize()}\nYour Ticket Successfully Book \n Movie : Housefull \n Time: 3:00 PM\n Total Ticket: {count}")

                    elif movie_choice==3:
                        print(f"Hello {user_name.capitalize()}\nYour Ticket Successfully Book \n Movie : Tu jhuthi Me makkar \n Time: 3:00 PM\n Total Ticket: {count}")  

                else:
                    print("Only Buy 10 Ticket  ") 
                    print("###########################################")
                    i1.movie_list()   
            
            else:
                print("Enter valid Choise ")
                print("************************************************")
                i1.movie_list()

        except:

            print("Invalid Syntax")
            print("*************************************************")
            i1.movie_list()


    def ticket_count(self,count,user_name):

        f = open(f"{user_name}ticket_count.txt","w")
        f.write(str(count))
        f.close()


        f =open("total_movie_ticket.txt","r")
        total_ticket=f.read()
        f.close()



        total_ticket=int(total_ticket)-count
        f= open("total_movie_ticket.txt","w")
        f.write(str(total_ticket))
        f.close()


    
temp="yes"
while temp=="yes":
    
    i1=Inox()

    print("1.Book Ticket\n2.Cancel Ticket\n3.Exit")
    choice = input("Enter Your choice:")


    if choice == "1":
        user_name=input("Enter your name:")
        f = open(f"{user_name}.txt","w")
        f.write(user_name)
        f.close()

        i1.movie_list()


    elif choice == "2":

        try:
            user_name=input("Enter your name:")

            

            f = open(f"{user_name}.txt","r")
            temp_user_name=f.read()
            f.close
        

            
            if  user_name==temp_user_name:

                f = open(f"{user_name}ticket_count.txt","r")
                temp_user_ticket_count=f.read()
                # print(temp_user_ticket_count)
                f.close()

                user_ticket_count=input("Enter Numbers of Ticket You Buy:")


                if user_ticket_count==temp_user_ticket_count:

                    print(f"{user_name} Your Ticket Successfully Cancelled")

                    f =open("total_movie_ticket.txt","r")
                    total_ticket=f.read()
                    f.close()
                    total_ticket=int(total_ticket)+int(temp_user_ticket_count)
                    
                    f =open("total_movie_ticket.txt","w")
                    f.write(str(total_ticket))
                    f.close()

                    os.remove(f"{user_name}.txt")
                    os.remove(f"{user_name}ticket_count.txt") 
                
                else:
                    print(" Total Ticket count incorrect ")
        
                
            else:
                print("You are not book any ticket")

        except:
             print("Invalid Details")



    elif choice=="3":
        temp="no"
    
    else:
        print("Invalid Choice")

