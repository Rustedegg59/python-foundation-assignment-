user_role = "analyst"
is_active = True
requested_dataset = "sales_data"

allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


def check_access(user_role, is_active, requested_dataset):
    if not is_active:
        print("Access denied because the user is inactive.")
    elif user_role not in allowed_roles:
        print("Access denied because the role is not allowed.")
    elif requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    else:
        print("Access granted.")


# Scenario 1: Active analyst requesting sales_data
check_access("analyst", True, "sales_data")

# Scenario 2: Inactive analyst requesting sales_data
check_access("analyst", False, "sales_data")

# Scenario 3: Active user with an unauthorized role
check_access("manager", True, "sales_data")

# Scenario 4: Active analyst requesting a restricted dataset
check_access("analyst", True, "salary_data")