import hashlib
import json
def main():
    process=True
    while (process == True):
        chk_majuscule=False
        chk_minuscule=False
        chk_cardinal=False
        Password = input("Vueillez saisir un mot de passe: ")
        if (len(Password)<8):
            print("Votre mot de passe est trop court !")
            process = True
        else:
            if(Password.find("!")>=0) or (Password.find("@")>=0) or (Password.find("#")>=0) or (Password.find("$")>=0) or (Password.find("%")>=0) or (Password.find("*")>=0) or (Password.find("&")>=0) or (Password.find("^")>=0):
                for i in Password:
                    if i.isupper():
                        chk_majuscule=True
                if(chk_majuscule==True):
                    for j in Password:
                        if j.islower():
                            chk_minuscule=True
                    if(chk_minuscule==True):
                        for k in Password:
                            if k.isnumeric():
                                chk_cardinal=True
                        if(chk_cardinal==True):
                                print("Mot de passe correct")
                                process=False
                        else:
                            print("Votre mot de passe doit contenir au moins un chiffre.")
                            process=True
                    else:
                        print("Votre mot de passe doit contenir au moins une minuscule.")
                        process=True
                else:
                    print("Votre mot de passe doit contenir au moins une majuscule.")
                    process=True
            else:
                print("Votre mot de passe doit contenir au moins un caractère spécial")
                process=True
main()  