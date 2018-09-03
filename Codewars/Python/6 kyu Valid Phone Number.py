def validPhoneNumber(phoneNumber):
    import re
    return True if re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phoneNumber) else False