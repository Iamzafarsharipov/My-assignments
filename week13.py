import datetime as dt
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day:"))
exam_date=dt.date(year,month,day)
current_date=dt.date.today()

diff=exam_date-current_date
print(exam_date)
print(current_date)
print(diff)

if diff.days>0:
    print(f"You have {diff.days} and days left")
elif diff.days<0:
    print(f"Your exam was {abs(diff.days)} today")
else:
    print("Good luck! The exam is today")
print(diff)

