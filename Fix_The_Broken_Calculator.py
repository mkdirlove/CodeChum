while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    op = input("Enter operator: ")
    
    if op == '+':
        print("%d + %d = %d\n" % (a, b, (a + b)))
    elif op == '-':
        print ("%d - %d = %d\n" % (a, b, (a - b)))
    elif op == '*':
        print("%d * %d = %d\n" % (a, b, (a * b)))
    elif op == '/':
        print("%d / %d = %d\n" % (a, b, (a / b)))
    else:
        break
