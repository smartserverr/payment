import requests

# Replace with your API endpoint and API key
api_endpoint = "https://api.yourbank.com/transfer"
api_key = "your_api_key"

# Replace with actual transfer details
transfer_data = {
    "from_account": "1234567890",  # Your account number
    "to_account": "0987654321",  # Recipient's account number
    "to_bank": "Bank Name",
    "to_country": "Country Code",  # ISO country code
    "amount": 1000.00,  # Transfer amount
    "currency": "USD",  # Currency code
    "purpose": "Payment for services",
    "reference": "Invoice #12345"
}

# Add authorization header and content type
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    # Make the API request
    response = requests.post(api_endpoint, json=transfer_data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Transfer successful:", response.json())
    else:
        print("Transfer failed:", response.status_code, response.text)

except Exception as e:
    print("An error occurred:", e)
