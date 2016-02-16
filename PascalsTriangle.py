#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document]. Retrieved
#from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Tutorials Point. (Nov 14, 2015). Retrieved from http://www.tutorialspoint.com/python/string_center.htm

#Stack Overflow. (Nov 14, 2015) Retrieved from http://stackoverflow.com/questions/13094918/convert-list-of-strings-to-space-separated-string



def main (): 
    stopnum=1.0 #set the stop number to an unacceptable number 
    #keep getting a number until the user enter something valid
    while type(stopnum)!=int : 
        stopnum=input("What integer should I look for?: ") 
        try:
            stopnum=int(stopnum) #try to make the number entered an integer
            #it is an integer so check if it is greater than 0
            if stopnum<=0: 
                print("The integer needs to be greater than 0") #error messege
                #set the stop number back to an unacceptable number so that the while loop will continue
                stopnum=0.06 
            #otherwise the number is an acceptable integer 
            else: 
                #run the pascals triangle function with it stopping at the number entered
                pasctri(stopnum) 
                break #once done, end 
        #if the number entered is the wrong type (not an int)
        except ValueError: 
                print("That is not an integer") #error messege


def pasctri (stopnum): 
    rowlength=1 #the first rows length is 1
    row=[] #make an empty list to contain the values of the row
    n=0 #initial position  for the row is 0
    
    #Base case: stop num is 1
    if stopnum==1: 
        row.append('1') #add 1 to the row list 
        draw(row) #draw the row
    
    else: 
       flag=True 
       for i in range (stopnum+1): #run through until reaching the number that the user entered     
           #run through for every position in the row
            for k in range (rowlength): 
                value=combo(n,k) #the value of that position is calculated by the combo function
                if value==stopnum:
                    flag=False
                value=str(value)    
                row.append(value) #add the value to the row list

            n=n+1 # increase n by one for the next row
            rowlength=rowlength+1 #increase the row length by 1 for the next row
            row.append("\n") #add a new line to the end of the row 
            draw(row)#draw the row
            row=[] #reset the list to be empty for the next row
            if flag== False:
                break


def fact (num): #factorial funtction
    product=1 #start the product at 1
    #base case: number being factorized is 1, return 1
    if num==1: 
        return num
    else: 
        for i in range (1,num+1): #start at 1 and go to the number inputed
            #multiply the product by 1 then 2 then 3 and so on until last number to get factorial
            product=product*i 
        return product 
         
            
def combo (n,k): #combonation function
    #calculate the value of the position specified using the formula for pascals triangle
    #when requiring the factorial, call the fact function 
    value=int(fact(n)/(fact(k)*fact(n-k)))
    return value #give the value back to the pascalls triangle function


def draw (row):
    row=" ".join(row) #join the row list and put a space inbetween each value 
    print(row.center(60)) #draw each value of the row centered in the screen when the screen width is 60
    
    
    
main() 

