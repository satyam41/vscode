# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

# Input
# Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

# Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

# Output
# Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

print("====Welcome to ATM====")

def isMultipleof5(n):
     
    while ( n > 0 ):
        n = n - 5
 
    if ( n == 0 ):
        return True

    return False

# print(isMultipleof5(15))

initialBalance = 120
withDrawlMoney = int(input("Enter withdrawl money: "))

if withDrawlMoney > initialBalance: 
    print(initialBalance)

elif isMultipleof5(withDrawlMoney) != True:
    print(initialBalance)

elif isMultipleof5(withDrawlMoney) <= initialBalance:
    print(initialBalance-withDrawlMoney-0.50)

else:
    print("ATM is Out of Order.")