while True:
     num = int(input("Enter number: "))
     if num >1:
          for i in range(2,num):
               if num % i==0:
                    print("This is NOT a prime number")
                    break
          else:
               print("This is a prime number!")
     else:
          print('This is NOT a prime number')
