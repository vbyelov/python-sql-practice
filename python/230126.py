# Day 5 — Python
# Task 1: average_per_category
#
# You are given a list of dictionaries, where each dictionary represents a sale:
# {"category": "A", "amount": 100}
#
# Write a function average_per_category(data) that:
# 1. Calculates the average amount per category
# 2. Returns a dictionary: {category: average_amount}
#
# Example input:
# data = [
#     {"category": "A", "amount": 100},
#     {"category": "A", "amount": 200},
#     {"category": "B", "amount": 300}
# ]
#
# Expected output:
# {"A": 150, "B": 300}
#
# Restrictions:
# - Use for-loops
# - Use dictionaries
# - Do NOT use pandas
# - Do NOT use collections

data = [
     {"category": "A", "amount": 100},
     {"category": "A", "amount": 200},
     {"category": "B", "amount": 300}
]

def average_per_category(data):
    totaldict = {}
    for item in data:
        category = item["category"]
        amount = item["amount"]
        if category not in totaldict:
            totaldict[category] = [amount, 1]
        else:
            totaldict[category][0] += amount
            totaldict[category][1] += 1

     result_dict = {}
    for category in totaldict:
        result_dict[category] = totaldict[category][0] / totaldict[category][1]
    return result_dict
