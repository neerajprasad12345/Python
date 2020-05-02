def calculate_future_value(montly_investment,yearly_intrest,years):
    montly_intrest_rate=yearly_intrest/12/100
    months=years*12
    future_value=0
    i=0
    for i in range(months):
        future_value+=montly_investment
        montly_intrest_ammount=future_value*montly_intrest_rate
        future_value+=montly_intrest_ammount
        i+=1
    return future_value
def main():
    choice="y"
    while choice.lower()=="y":
        montly_investment=int(input("Enter the montly investment:"))
        yearly_intrest_rate=int(input("Enter the yearly intrest:"))
        years=int(input("Enter the no of Years:"))
        future_value=calculate_future_value(montly_investment,yearly_intrest_rate,years)
        print("Future Value:\t\t\t"+str(round(future_value,2)))
        print()
        choice=input("Wanna Continue(y/n):")
        print()
        print("Bye")
if __name__ == "__main__":
    main()

