import numpy as np
import pandas as pd

# Create NumPy array of electricity bills
bills = np.array([2500, 3200, 4100, 2800, 3500, 2200, 5000])

# Calculate statistics
mean_bill = np.mean(bills)
median_bill = np.median(bills)
max_bill = np.max(bills)
min_bill = np.min(bills)

# Display statistics
print("Electricity Bill Statistics")
print("-" * 30)
print("Mean Bill Amount   : ₹", mean_bill)
print("Median Bill Amount : ₹", median_bill)
print("Maximum Bill Amount: ₹", max_bill)
print("Minimum Bill Amount: ₹", min_bill)

# Create Pandas DataFrame
data = {
    "Consumer": ["Raj", "Priya", "Amit", "Neha", "Karan", "Sneha", "Rohit"],
    "Bill_Amount": bills
}

df = pd.DataFrame(data)

print("\nConsumer Bill Details")
print(df)

# Display consumers whose bill exceeds ₹3000
high_bills = df[df["Bill_Amount"] > 3000]

print("\nConsumers with Bill Amount Exceeding ₹3000")
print(high_bills)