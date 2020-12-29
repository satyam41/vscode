def budget(my_budget,house_prices):
    house_prices.sort()
    sum_house = 0
    case = 0
    for i in range(0,len(house_prices)):
        # if my_budget<=house_prices[i]:
        if sum_house <= my_budget:
            sum_house = sum_house+house_prices[i]
            if sum_house <= my_budget:
                count_list = house_prices.count(house_prices[i])
            case+=1
            print("Case # :",case)
            print("In your budget number of houses you buy", count_list)
            # break


test_cases = [] 
num_test_cases = int(input("Enter number of tests: "))
while num_test_cases > 0: 
	input_list = input('Input list: ').split(' ') 
	num_houses = int(input_list[0]) 
	my_budget = int(input_list[1]) 
	house_prices = input('input house price: ').split(' ') 
	house_prices = [int(price) for price in house_prices] 
	test_cases.append([my_budget, house_prices]) 
	num_test_cases -= 1 
budget(my_budget,house_prices)
