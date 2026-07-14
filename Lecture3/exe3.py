hour_work = int(input("Enter the number of hours worked: "))
Pay_rate = int(input("Enter the hourly pay rate: "))

if hour_work > 40:
    pay = (hour_work-40)*Pay_rate*1.5+(40*Pay_rate)
    print("The Gross pay is ", format(pay,".2f"))
else:
    pay = hour_work*Pay_rate
    print("The Gross pay is ", format(pay,".2f"))
