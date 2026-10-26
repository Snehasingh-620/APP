import numpy as np
import pandas as pd

# Create NumPy array of course fees
fees = np.array([15000, 28000, 32000, 22000, 45000, 18000, 27000])

# Calculate statistics
average_fee = np.mean(fees)
maximum_fee = np.max(fees)
minimum_fee = np.min(fees)

# Display statistics
print("Course Fee Statistics")
print("-" * 30)
print("Average Course Fee : ₹", average_fee)
print("Maximum Course Fee : ₹", maximum_fee)
print("Minimum Course Fee : ₹", minimum_fee)

# Create Pandas DataFrame
data = {
    "Course": [
        "Python Programming",
        "Data Science",
        "Machine Learning",
        "Web Development",
        "Artificial Intelligence",
        "C Programming",
        "Cloud Computing"
    ],
    "Fee": fees
}

df = pd.DataFrame(data)

print("\nCourse Fee Details")
print(df)

# Display courses whose fee is greater than ₹25,000
high_fee_courses = df[df["Fee"] > 25000]

print("\nCourses with Fee Greater Than ₹25,000")
print(high_fee_courses)