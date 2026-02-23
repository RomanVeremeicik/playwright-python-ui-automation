VALID_CHECKOUT = {
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "12345"
}

INVALID_CHECKOUT_CASES = [
    {"first_name": "", "last_name": "Doe", "postal_code": "12345"},
    {"first_name": "John", "last_name": "", "postal_code": "12345"},
    {"first_name": "John", "last_name": "Doe", "postal_code": ""},
]
