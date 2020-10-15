# First create a list.
my_list = [11, 2, 8, 27, 15] 
my_list

my_list.reverse()

# Create the 'get_binary_function()'.
def get_binary_function(num):
    return bin(num).replace('0b', '')

# Create an empty list called 'cards' containing 6 other empty lists.
cards = [[], [], [], [], [], []]

# Fill the 'cards' list by applying the game logic in python.
cards = [[[i for i in range(61)if i&2**k][j::5]for j in range(5)]for k in range(6)]
#print(cards, end = ' ')

# Run the game here.

# Give a message 'Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.' to the player
start = input("Enter start to continue the game. ")
player_input = 0#int(input("Think of a number between 1 and 63. Hit the 'Enter' key to start the game."))
# Keep printing the message until the player enters only 'start'.
while player_input != "start":
    player_input = int(input("Think of a number between 1 and 63. Hit the 'Enter' key to start the game."))
    break

# Create the 'num' variable and set its initial value equal to 0.
num = 0
# Create a list named valid_entries.
valid_entries = ['yes', 'no']
# Create a loop to display the numbers of each card and to take the input whether the number exists in the card displayed. 
show_num = [i for i in range(61) if i&1]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

show_num = [i for i in range(61) if i&2]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

show_num = [i for i in range(61) if i&4]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

show_num = [i for i in range(61) if i&8]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

show_num = [i for i in range(61) if i&16]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

show_num = [i for i in range(61) if i&32]
print("\n",show_num)
yn = input("Enter your number is exist in the first card. If yes write 'YES' or no write 'NO' : ")

    # If the number exists in the card displayed, then add the first number to the 'num' variable. Use list indexing, to get the first number.
if show_num == cards:
    show_num.index[player_input] = show_num
    show_num = player_input
# Print the value of the 'num' variable.
print("\nYour number is", player_input)
