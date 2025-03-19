print("Vítejte v programu pro vypočítání objemu a obsahu pro kužel")
v = float(input("Zadejte výšku kužele v cm: "))
r = float(input("Zadejte poloměr podstavy v cm: "))
s = float(input("Zadejte stranu kužele v cm:  "))

print("Vyberte z následující nabídky: ")

print("Pro vypočítání objemu kužele zadejte - 1 ")
print("Pro vypočítání obsahu kužele zadejte - 2 ")

operator = input("Zadejte volbu: ")

if operator == "1":
    objem = (3.14156*r*r*v)/3
    print("Objem kužele v centimetrech krychlových je:", objem) 
elif operator == "2": 
    obsah = (3.141456*r(r+s))
    print("Obsah kužele v centimetrech krychlových je:",)



