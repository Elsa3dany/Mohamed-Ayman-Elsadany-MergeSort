def merge_sort_flights(flights, key):
    if len(flights) <= 1:
        return flights
    
    mid = len(flights) // 2
    left_half = merge_sort_flights(flights[:mid], key)
    right_half = merge_sort_flights(flights[mid:], key)
    
    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

flights = [
    {"Flight ID": "A123", "Time": "12:30", "Altitude": 35000, "Speed": 540},
    {"Flight ID": "B456", "Time": "10:15", "Altitude": 37000, "Speed": 560},
    {"Flight ID": "C789", "Time": "14:45", "Altitude": 33000, "Speed": 520},
    {"Flight ID": "D101", "Time": "09:00", "Altitude": 34000, "Speed": 530}
]

sorted_flights = merge_sort_flights(flights, key="Time")

for flight in sorted_flights:
    print(flight)
