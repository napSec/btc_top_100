#! Python3
import requests

def get_top_100_addresses(address):
    # Set the API endpoint
    endpoint = "https://blockchain.info/rawaddr/"

    # Send request to endpoint to retrieve list of transactions
    response = requests.get(endpoint + address)
    data = response.json()

    # Extract transactions from the response
    transactions = data['txs']

    # Create dictionary to store the addresses and their counts
    address_counts = {}

    # Iterate list of transactions
    for transaction in transactions:
        # Get the list inputs for the transaction
        inputs = transaction['inputs']
        # Iterate through the list of inputs
        for input in inputs:
            # Get input address 
            input_address = input['prev_out']['addr']
            # Increment input address count
            if input_address in address_counts:
                address_counts[input_address] += 1
            else:
                address_counts[input_address] = 1

        # Get list of outputs for the transaction
        outputs = transaction['out']
        # Iterate list of outputs
        for output in outputs:
            # Get address of the output
            output_address = output['addr']
            # Increment output address count
            if output_address in address_counts:
                address_counts[output_address] += 1
            else:
                address_counts[output_address] = 1

    # Sort the dictionary by values in descending order
    sorted_addresses = sorted(address_counts.items(), key=lambda x: x[1], reverse=True)

    # Return top 100 addresses
    return sorted_addresses[:100]

# Get address from the user
address = input("Enter the address: ")

# Test the function with the specified address
top_100_addresses = get_top_100_addresses(address)

# Print the top 100 addresses
for address, count in top_100_addresses:
    print(address, count)
