print("The test Score program")
print("")
print("Enter Test Score")
print("Enter 'end'to end input")
print("============================")
choose="y"
while choose.lower()=="y":
    test_score=0
    total_score=0
    counter=0
    while True:
        test_score=input("Enter test score:")
        if test_score.lower()=="end":
            break
        else:
            test_score=int(test_score)
            if test_score>=0 and test_score<=100:
                total_score+=test_score
                counter+=1
            else:
                print("Test Score must be between 0 and 100")
    average_total=(total_score/counter)
    print("===============================")
    print("Total Score:\t\t",total_score)
    print("Average Total:\t\t",average_total)
    print()
    choose=input("You wanna enter another data(y/n):")
    print("")
    print("Thank You!")                   
        
            
