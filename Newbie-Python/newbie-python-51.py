guests = int(input())
budget = int(input())

kuvert = 20 * guests

if kuvert < budget:
    left = budget - kuvert
    
    fire = left * 0.4
    don = left - fire
    fire = int(fire)
    don = int(don)
    print("Yes! " + str(fire) + " are for fireworks and " + str(don) + " lv are for donation.")

elif kuvert > budget:
    noE = kuvert - budget
    noE = int(noE)


    print("They won't have enough money to pay the covert. They will need " + str(noE) + " lv more.")

