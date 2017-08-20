for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(round((int(a) / int(b))))
    except ZeroDivisionError as e:
          print("Error Code:", "integer division or modulo by zero")
    except ValueError as e:
          print("Error Code:", e)
