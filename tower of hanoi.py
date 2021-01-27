# Write your code here
def tower_hanoi(disks):
    steps = 2**disks - 1
    return steps
step = int(input("Enter the steps requred to shift the disks : "))
print(f"Minimum number of steps requred to shift {step} disks is {tower_hanoi(step)}")