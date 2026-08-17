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