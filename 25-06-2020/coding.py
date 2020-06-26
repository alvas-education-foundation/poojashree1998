//Python Program for number of days
Month = int(input('Enter the Month :'))
Year = int(input('Enter the Year :'))
#Check condition for Month and leap year
if(Month == 2 and (Year%4 == 0) or ((Year%100 == 0) and (Year%400 == 0))):
    #if condition is TRUE
    print('Number of days is 29')
#if False check for other conditions
elif(Month == 2):
    print('Number of days is 28')
elif(Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12):
    print('Number of days is 31')
else:
    print('Number of days is 30')
    
