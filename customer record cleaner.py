raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Clean the values
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

# Ternary expression for adult status
status = "Adult" if age >= 18 else "Minor"

print("Name:", name)
print("City:", city)
print("Age:", age)
print("Email:", email)
print("Status:", status)