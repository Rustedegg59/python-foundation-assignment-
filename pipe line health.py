# Test 1
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate > 5:
    status = "Critical"
else:
    status = "Warning"

print("Test 1")
print(f"Failure rate: {failure_rate:.2f}%")
print("Pipeline status:", status)
print()

# Test 2
rows_loaded = 9500
rows_failed = 500
runtime_minutes = 15

failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate > 5:
    status = "Critical"
else:
    status = "Warning"

print("Test 2")
print(f"Failure rate: {failure_rate:.2f}%")
print("Pipeline status:", status)
print()

# Test 3
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

failure_rate = (rows_failed / (rows_loaded + rows_failed)) * 100

if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
elif failure_rate > 5:
    status = "Critical"
else:
    status = "Warning"

print("Test 3")
print(f"Failure rate: {failure_rate:.2f}%")
print("Pipeline status:", status)