months = ("January","February","March","April","May","June","July","August","September","October","November","December")
spring = (3,4,5)
summer = (6,7,8)
autumn = (9,10,11)
winter = (12,1,2)

month_number = int(input("Give the number of the month (1-12):  "))

month = months[month_number-1]

if month_number in spring:
    season = "spring"
elif month_number in summer:
    season = "summer"
elif month_number in autumn:
    season = "autumn"
else:
    season = "winter"

print (f"{month} is in {season}.")