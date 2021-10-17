purchase =[]
ticket_price=int()
income=[]

class Movie_Ticket_Booking:
   
    
    def __init__(self,rows,seats,seats_disp):
        self.rows= rows
        self.seats= seats
        self.seats_disp= seats_disp
        self.all_user_info = {}               
        
    
    
    def show_seats(self): 
        for i in range(self.rows+1):
            for j in range(self.seats+1):
                if i==0 and j==0:
                    print(' ',end=' ')
                elif i==0:
                    print(j,end=' ')
                elif j==0:
                    print(i, end=' ')
                else:
                    print(self.seats_disp[i][j],end=' ')
            print()
        self.Options()
        
    def Options(self):
        print('Please Select from the Following options ')
        print('1. Show the Seats')
        print('2. Buy a ticket')
        print('3. Statistics')
        print('4. Show booked tickets user info ')
        print('0. Exit')
        option = int(input())
        
        if option == 1:
            self.show_seats()
        elif option == 2:
            self.buy_ticket()
        elif option == 3:
            self.stats()
        elif option == 4:
            self.show_info()
        elif option == 0:
            exit()
        else:
            print("Please try again!!!!!")
       
    

    def buy_ticket(self):
        self.row_no=int(input('Enter the row number: '))
        self.seat_no=int(input('Enter the seat number in that particular row: '))
        
        self.total_seats = self.rows * self.seats
        print('Total seats are: ', self.total_seats)
        global ticket_price
        
        if (self.total_seats) < 60:
            ticket_price= 10
            income.append(ticket_price)
            self.total_inc = self.total_seats * ticket_price         
            print("Your ticket_price will be $", ticket_price)
        if (self.total_seats) > 60:
            self.first_half= self.rows // 2
            self.other_half= self.rows - self.first_half
            if self.rows % 2==0:
                self.total_inc = (self.first_half*10) + (self.other_half*8)    
                                               
                if self.row_no < self.first_half:
                                               
                    ticket_price= 10 
                    income.append(ticket_price)
                    
                    print('Ticket_price for the tickets is $',ticket_price)
                elif self.row_no > self.first_half and self.row_no < self.rows:
                                            
                    ticket_price = 8
                    income.append(ticket_price)
                    print('Ticket_price of your ticket is $', ticket_price)
            elif self.row_no %2!=0:                                          
                self.total_inc = (self.first_half*10) + (self.other_half*8)      
                if self.row_no<=self.first_half:
                                                 
                    ticket_price = 10
                    income.append(ticket_price)
                    print('Ticket_price for the ticket is $', ticket_price)
                elif self.row_no > self.first_half and self.row_no <self.rows:
                                        
                    ticket_price = 8 
                    income.append(ticket_price)
                    print('Ticket_price of your ticket is $', ticket_price)
        
        print('DO U WANT TO BOOK THE TICKET')
        print('1. YES')
        print('2. No')
        ask=int(input())
             
        if ask == 1:
            purchase.append(self.seat_no)        
            
            
            self.user_Options(self.row_no,self.seat_no)
        elif ask == 2:
            print("You can choose from the main menu ")
            self.Options()
    
    def user_Options(self,row_no,seat_no):
        print('To book kindly enter your Options ')
        self.name=input('Enter Name ')
        self.age=int(input('Enter Age '))
        self.gender=input('Enter your Gender ')
        self.phone=int(input('Enter your phone number '))
        
        
        dict1={}
        global ticket_price
        
        dict1["Name"]=self.name
        dict1["Gender"]=self.gender
        dict1["Age"]=self.age
        dict1["Ticket_Ticket_price"]=ticket_price
        dict1["Phone_No"]=self.phone
        self.all_user_info[(self.row_no,self.seat_no)] = dict1         
        
        
        
        print('Cinema: ')
       
        if self.seats_disp[self.row_no][self.seat_no]=='S':
            self.seats_disp[self.row_no][self.seat_no]='B'
            for i in range(self.rows+1):
                for j in range(self.seats+1):
                    if i==0 and j==0:
                        print(' ',end=' ')
                    elif i==0:
                        print(j,end=' ')
                    elif j==0:
                        print(i, end=' ')
                    else:
                        print(self.seats_disp[i][j],end=' ')
                print()
        print('Your ticket booked succesfully') 

        self.Options()
    
    def stats(self):
        
        print('Number of tickets purchased: ',len(purchase))
        percent =(len(purchase) / self.total_seats)* 100
        print('Percentage: ', percent , '%')
        print('Current Income :$',sum(income))
        
        print('Total Income:$',self.total_inc)
        self.Options()

    
    def show_info(self):
        row_num2 = int(input('Enter the row number you booked: '))
        seat_num2 = int(input('Enter the seat number you booked: '))
        if seats_disp[row_num2][seat_num2]=="B":
            for i in self.all_user_info[(row_num2,seat_num2)]:
                print(i , ': ' , self.all_user_info[(row_num2,seat_num2)][i])
        else:
            print('Seat is not booked')
        self.Options()   
if __name__ == "__main__":
    rows = int(input('Enter the number of rows: '))
    seats = int(input('Enter the number of seats in each row: '))
    print('Cinema: ')
    seats_disp=[['S' for j in range(seats + 1)]for i in range(rows + 1)]
    Display=Movie_Ticket_Booking(rows,seats,seats_disp)
    Display.Options()


    