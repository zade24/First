

print("Exclusive Members Only")

members = []

files = """
    1)Financial statement
    2)Employees Details
    3)Product Customers

    """

financial_statements = """
                        company balance = R10000000
                        company expenditure = R234243
                        
                         """
employees = """
                        Name            age     date of employment
                        ntando manson   24      21-july-2017
                        thami carrel    27      24-september-2017
                        jim rod         26      1-january-2019

                        """

product_customers = f"""
                        Main product : Cyber-Security services
                        Decription   : Provide protection of company data against cyber attacks
                        Main Customers:
                                        Standard Bank : R232424
                                        ST john secondary school : R231424
                                        ABSA Bank : R234536                                       
                                        Pick n Pay : R1423123


                         """

options = [
          {
    "financial statement" : financial_statements,
    "employees" : employees,
    "product customers" : product_customers
          }
    

]



user_options = "which files would you like to access??\n"

def recieve_file():
    try:
        print("which files would you like to access??")
        user_options = input()
    except Exception as e:
        print("ERROR", e)
        print("1,2,3,4")

        if user_options == "1":
            for i in options:
             print(i["financial statement"])
        elif user_options == "2":
            for i in options:
                print(i["employees"])
        elif user_options == "3":
            print(i["product customers"])

print()

username = input("Username : ")
password = input("Password : ")


a = "access granted".upper()

if username == "Chris" and password == "tekashi24":
    print(a)
    print("")
    print(files)
    recieve_file()
elif username == "john" and password == "qwerty":
    print(a)
    print(files)
    recieve_file()
elif username == "chrino" and password == "mukanya": 
    print(a)
    print(files)
    recieve_file()
elif username == "david" and password == "mugaruka":
    print(a)
    print(files)
    recieve_file()
elif username == "vuyo" and password == "sibiya":
    print(a)
    print(files)
    recieve_file()
elif username == "jeremaih" and password == "matatari":
    print(a)
    print(files)
    recieve_file()
elif username == "njabulo" and password == "aiomine":
    print(a)
    print(files)
    recieve_file()
elif username == "emza" and password == "king":
    print(a)
    print(files)
    recieve_file()
elif username == "mashabela" and password == "elon":
    print(a)
    print(files)
    recieve_file()
elif username == "elohim" and password == "justin":
    print(a)
    print(files)
    recieve_file()

else:
    print("you are not an exclusive member")

