salary = float(input())
time = int(input())
sindikallen = input()

all = salary


for i in range(100):
    i += 1
    all += all * 0.06

    if i % 5 == 0:
        all += 100
    if i % 5 == 0:
        all += 200

    if i == time:
        all = "%.2f" % all
        print("Current salary: %s" % (all))


       



       

      
        
       

 
 

