#emerson baillie
#conversion table
def conversion():
    kg = None
    Convert = int(input("Please enter a a kilogram value to be convered to pounds: "))
    pounds = (Convert * 2.2)
    print()
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print()
    print("{0:<3} {1:^6} {2:>3}".format("Kg",":","Pounds"))
    print("------:--------------------")
    for kg in range((Convert - 2),(Convert + 3)):
        print("{0:<3} {1:^6}{2:>3.2f}".format(kg,":",pounds))
        kg = kg + 1
        pounds = (kg * 2.2)
