def title():
    print("list-Display all the List")
    print("add-Add movie in list")
    print("del-Delete the Movie List")
    print("exit-Exit the program")

def list(movie_list):
    i=1
    for movie in movie_list:
        print(str(i)+" ."+movie)
        i+=1
    print()

def add(movie_list):
    movie=input("Name:")
    movie_list.append(movie)
    print(movie +" "+"has been add in list")

def delete(movie_list):
    number=int(input("Enter The Movie number:"))
    if number<1 and number>len(movie_list):
        print("Invalid Number")
    else:
        movie=movie_list.pop(number-1)
        print(movie+" "+ "has been delete")

def main():
    movie_list=["Ramma the Saviour",\
        "Tarzan the wonder car",\
        "Pinocchio"]
    title()
    while True:
        choice=input("Enter the command:") 
        if choice.lower()=="list":
            list(movie_list)
        elif choice.lower()=="add":
            add(movie_list)
        elif choice.lower()=="del":
            delete(movie_list)
        elif choice.lower()=="exit":
            break
        else:
            print("Enter command is not valid,Please Try Again\n")

    print("Thank u for visting!")
if __name__ == "__main__":
    main()

