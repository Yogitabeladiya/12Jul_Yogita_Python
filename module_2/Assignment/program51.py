# highest 3 value
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
result = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3])
print(result)
