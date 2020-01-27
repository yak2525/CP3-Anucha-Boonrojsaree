user = "love"
passWord = 1234
userNameInput = input("User :")
passWordInput = int(input("Pass :"))
if user == userNameInput and passWord == passWordInput:
    print("Done !!!")
    print("----YAK Shop----")
    print("1. Price Calculator")
    print("2. VAT Calculator")
    customerSelected = int(input("Select >>"))
    if customerSelected == 1:
        price1 = int(input("Price of product 1 :"))
        price2 = int(input("Price of product 2 :"))
        price3 = int(input("Price of product 3 :"))
        Total = price1 + price2 + price3
        print(Total, "THB")
    elif customerSelected == 2:
        price = int(input("Product price, THB:\n"))
        vat = int(input("VAT, %:\n"))
        result = price + (price * (vat / 100))
        print("Price include VAT, THB:", result)