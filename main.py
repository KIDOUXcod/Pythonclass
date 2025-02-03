# Prompt the user to enter the KW hours used
kwh_used = int(input("Enter the kWh used: "))

# Define the rates
rate_first_1000 = 7.633  # cents per kWh
rate_over_1000 = 9.259   # cents per kWh
# Calculate the total cost in cents
if kwh_used <= 1000:
    total_cost_cents = kwh_used * rate_first_1000
else:
    total_cost_cents = 1000 * rate_first_1000 + (kwh_used - 1000) * rate_over_1000

# Convert the total cost to dollars
total_cost_dollars = total_cost_cents / 100

# Output the result rounded to two decimal places
print(f"Amount owed is ${total_cost_dollars:.2f}")




