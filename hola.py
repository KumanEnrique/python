def vnom(nom):
    if len(nom) >= 6 and len(nom) <= 12 and nom.isalnum():
        return True
    else:
        return False

username = input("Enter username:")
print("Usernaazzzme is: " + username)
print(vnom(username))