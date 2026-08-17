total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# Calculate problematic rows and percentage
problematic_rows = missing_rows + duplicate_rows
problem_percentage = (problematic_rows / total_rows) * 100

# Classify the dataset
if problem_percentage <= 2:
    classification = "Excellent"
elif problem_percentage <= 5:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

# Display results
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f}%")
print(f"Final classification: {classification}")

file_name = input("Enter a file name: ")

file_name = file_name.strip().lower()

if file_name.endswith(".csv"):
    print("Accepted: CSV file")
elif file_name.endswith(".json"):
    print("Accepted: JSON file")
elif file_name.endswith(".parquet"):
    print("Accepted: Parquet file")
else:
    print("Invalid file type. Please use .csv, .json, or .parquet.")