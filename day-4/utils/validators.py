def validate_numbers(data):
    if not data:
        return False, "Request body must be JSON"

    if "num1" not in data or "num2" not in data:
        return False, "num1 and num2 are required"

    num1 = data["num1"]
    num2 = data["num2"]

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return False, "num1 and num2 must be numbers"

    return True, (num1, num2)
