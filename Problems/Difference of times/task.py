# put your python code here
first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())

first_value = (first_hours * 3600) + (first_minutes * 60) + first_seconds
second_value = (second_hours * 3600) + (second_minutes * 60) + second_seconds

print(abs(first_value - second_value))
