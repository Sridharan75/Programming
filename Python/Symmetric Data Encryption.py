print("----------Symmetric Data Encryption----------")
common_Key=input("Enter your common key: ")
message=input("Enter your Message: ")
retrive=input("Are you want to retrive your secret message:(Y/N) ")
if retrive=="y"or"Y":
    retrive_Key=input("Enter your common key: ")
    if retrive_Key==common_Key:
        print("The Message :{}".format(message))
    else:
        print("The common key was wrong.")
else:
    print("Thanks for your response.")
    
