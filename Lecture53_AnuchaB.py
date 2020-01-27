def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
a = int(input("insert number :",))
print(vatCalculate(a))
