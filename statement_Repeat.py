def fun():
    statement = input("Please enter a statement: ")
    repeat = int(input("How many times shall this statement be repeated: "))
    for repeat in range(repeat):
        print(statement)
fun()
