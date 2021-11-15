#Program to print total time taken in [years,months,days,hours]
#by Sandeep to cover 10,000 km distance on bicycle

#Input:Total distance, Average Speed per hour, Time per day

Total_distance = 10_000
#Lets take some average speed per day
Average_speed = int(input("Please enter average speed per day: "))
#Lets take time per day
Time_per_day = int(input("Please enter time taken per day: "))
Total_time = Total_distance //Average_speed

#Below lines[14-19 are repeated code.Hence converting it to function:
#Days = Total_time // Time_per_day
#Remaining_hrs = Total_time % Time_per_day
#Months = Days // 30
#Remaining_days = Days % 30
#Years = Months // 12
#Remaining_months = Months % 12

def divide(num,den):
     quot = num // den
     rem = num % den
     return(quot,rem)

Days,hours = divide(Total_time,Time_per_day)
Months,Days = divide(Days,30)
Years,Months = divide(Months,12)
print("Time taken by Sandeep: ",Years,"years",Months,"Months",Days,"Days",hours,"hours")


                
