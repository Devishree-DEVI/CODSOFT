To_Do_List = []
while True:
    print("1.Create Tasks")
    print("2.Update the old one")
    print("3.List the Existing Tasks")
    print("4.EXIT")
    
    choice = input("whats your choice?")
    
    if choice == "1":
        challenge = input("Want to add somerhing new?")
        To_Do_List.append(challenge)
        print("successfully added the new challenge!")
    elif choice=="2":
        if len(challenge) == 0:
            print("ouch! Nothing found to Update")
        else:
            index=1
            for challenge in To_Do_List:
                print(str(index)+"."+ challenge)
                index+=1
                challenge_num=int(input("enter the challenege number to update"))
                if 1<=challenge_num <= len(To_Do_List):
                    new_challenge=input("Enter the new one")
                    To_Do_List[challenge_num-1]=new_challenge
                    print("Successfulyy updated CHALLENGE")
                else:
                    print("Challenge number not Found ")
            
    elif choice=="3":
        if len(challenge)==0:
            print("oops! Looks like you have no challenegs right now")
        else:
            index=1
            for challenge in To_Do_List:
                print(str(index)+"."+challenge)
                index+=1
                
    elif choice=="4":
        print("Thanks for staying Organized.See you Next Time!")
        
    else:
        print("looks like its a invlaid choice .please enter the valid one")
    
    
    
    