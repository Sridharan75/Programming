print("----------Asymmetric Data Encryption----------")
pub_Key=input("Enter your Public key: ")
priv_Key=input("Enter your Private key: ")
select_key=input("Are you want to Encrypt with public key/private key:(pub/priv) ")
if select_key=="pub":
    print("----------Continuing with Public Key----------")
    message=input("Enter your Message: ")
    retrive=input("Are you want to retrive your secret message:(Y/N) ")
    if retrive=="y"or"Y":
        retrive_Key=input("Enter your private key: ")
        if retrive_Key==priv_Key:
            print("The Message :{}".format(message))
        else:
            print("The key you entered was wrong.")
    else:
        print("Thanks for your response.")
    
elif select_key=="priv":
    print("----------Continuing with Public Key----------")
    message=input("Enter your Message: ")
    retrive=input("Are you want to retrive your secret message:(Y/N) ")
    if retrive=="y"or"Y":
        retrive_Key=input("Enter your public key: ")
        if retrive_Key==pub_Key:
            print("The Message :{}".format(message))
        else:
            print("The key you entered was wrong.")
    else:
        print("Thanks for your response.")
