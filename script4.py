first_name = "chinmay"
e1 = first_name.upper()
print(e1)

last_name = "DESHPANDE"
e2 = last_name.lower()
print(e2)

middle_name = "shrish"
e3 = middle_name.capitalize()
print(e3)

e4 = e1.isupper()
print(e4)

e5 = e2.islower()
print(e5)

city = "Pune"
e6 = city.startswith("P")
e7 = city.startswith("p")
e8 = city.startswith("Pun")
print(e6)
print(e7)
print(e8)

e9 = city.endswith('e')
e10 = city.endswith('une')
print(e9)
print(e10)

city3  = " Goa "
print(len(city3))
e11 = city3.lstrip()
print(len(e11))

city3  = "Goa "
print(len(city3))
e12 = city3.rstrip()
print(len(e12))

city3  = " Goa "
e13 = city3.strip()
print(len(e13))

strOne = "123"
strTwo = "chinmay"
strThree = "½"
strFour = "chinmay123"
strFive = "chinmay123#@$#"

e14 = strOne.isdigit()
e15 = strOne.isnumeric()

print(e14)
print(e15)