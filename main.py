def sum_values(d):
    return sum(d.values())

def average_values(d):
    if not d:
        return 0
    return sum(d.values()) / len(d)

scores = {'math': 85, 'science': 90, 'history': 78}
print(sum_values(scores))      # 253
print(average_values(scores))  # 84.333...
