#! python3

import requests

def get_top_100_addresses(address):
    # Set the API endpoint
    endpoint = "https://blockchain.info/rawaddr/"

    # Send a request to the endpoint to get the list of transactions
    response = requests.get(endpoint + address)
    data = response.json()

    # Extract transactions from  response
    transactions = data['txs']

    # Create dictionary to store the addresses / counts
    address_counts = {}

    # Iterate through the list of transactions
    for transaction in transactions:
        # Get list of inputs for the transaction
        inputs = transaction['inputs']
        # Iterate through the list of inputs
        for input in inputs:
            # Get Input address 
            input_address = input['prev_out']['addr']
            # Increment  count for the input address
            if input_address in address_counts:
                address_counts[input_address] += 1
            else:
                address_counts[input_address] = 1

        # Get outputs for the transaction
        outputs = transaction['out']
        # Iterate through the list of outputs
        for output in outputs:
            # Get the address of the output
            output_address = output['addr']
            # Increment the count for the output address
            if output_address in address_counts:
                address_counts[output_address] += 1
            else:
                address_counts[output_address] = 1

    # Sort the dictionary by values in descending order
    sorted_addresses = sorted(address_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top 100 addresses
    return sorted_addresses[:100]

# Run the function with the specified address
top_100_addresses = get_top_100_addresses("target address")

# Print the top 100 addresses
for address, count in top_100_addresses:
    print(address, count)

