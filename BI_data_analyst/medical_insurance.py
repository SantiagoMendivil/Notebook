# Records will be saved here.
medical_costs = {}

# Update dictionaries with one line of code
medical_costs.update(
    {
        "Marina": 6607.0,
        "Vinay": 3225.0,
        "Connie": 8886.0,
        "Isaac": 16444.0,
        "Valentina": 6420,
    }
)

# Update single values
medical_costs["Vinat"] = 3325.0

# Average medical cost / Iterate through values
total_cost = 0
for value in medical_costs.values():
    total_cost += value

average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")
