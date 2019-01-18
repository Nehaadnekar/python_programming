#this program will give you the remaining no. of days in this year after the date and month you entered
month=int(input("enter the month"))
date=int(input("enter the date"))
if month==1:
	rem=(31-date)+(365-31)
elif month==2:
	rem=(28-date)+(365-31-28)
elif month==2:
	rem=(28-date)+(365-31-28)
elif month==3:
	rem=(31-date)+(365-31-28-31)
elif month==4:
	rem=(30-date)+(365-31-28-31-30)
elif month==5:
	rem=(31-date)+(365-31-28-31-30-31)
elif month==6:
	rem=(30-date)+(365-31-28-31-30-31-30)
elif month==7:
	rem=(31-date)+(365-31-28-31-30-31-30-31)
elif month==8:
	rem=(31-date)+(365-31-28-31-30-31-30-31-31)
elif month==9:
	rem=(30-date)+(365-31-28-31-30-31-30-31-31-30)
elif month==10:
	rem=(31-date)+(365-31-28-31-30-31-30-31-31-30-31)
elif month==11:
	rem=(30-date)+(365-31-28-31-30-31-30-31-31-30-31-30)
elif month==12:
	rem=(31-date)+(365-31-28-31-30-31-30-31-31-30-31-30-31)
print(rem)
