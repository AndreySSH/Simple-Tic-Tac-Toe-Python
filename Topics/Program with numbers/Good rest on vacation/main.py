duration_days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

total = food_cost * duration_days + flight_cost * 2 + hotel_cost * (duration_days - 1)

print(total)