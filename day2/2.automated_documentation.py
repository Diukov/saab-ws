class ProcHelper:
    """
    This class processes data in batches, applying calculations and a potential discount.

    Attributes:
        threshold (float): A threshold value used for a potential discount.
        current (float): Stores a calculated value, potentially discounted.
        track (list): A list to store intermediate calculation results.

    Methods:
        __init__(self, thresh): Initializes the ProcHelper object with a threshold value.
        part_one(self, dataset): Processes a single dataset within a batch.
            - It iterates through 'data' entries in the dataset.
            - For each entry, it calls helper_func to calculate a value based on 'amount' and 'rate'.
            - The calculated value is appended to the 'track' list.
            - If the dataset has more than 5 entries, it calls extra_step.
        helper_func(self, a, b): Calculates a value based on two input numbers.
            - If 'a' is greater than 50, it multiplies 'a' and 'b' by 0.85.
            - Otherwise, it simply multiplies 'a' and 'b'.
        extra_step(self): Performs an additional calculation if the sum of values in 'track' exceeds the threshold.
            - If the sum is greater than the threshold, it sets 'current' to 90% of the sum.
        finalize(self): Returns the final calculated value.
            - If 'current' is greater than 0, it returns 'current'.
            - Otherwise, it returns the sum of values in 'track'.
    """

def batch_proc(batch, thresh):
    """
    Processes a batch of data using the ProcHelper class.

    Args:
        batch (list): A list of datasets to be processed.
        thresh (float): The threshold value for the ProcHelper object.

    Returns:
        float: The final calculated value after processing the batch.
    """
    helper = ProcHelper(thresh)  # Create a ProcHelper object
    for data in batch:
        helper.part_one(data)  # Process each dataset in the batch
    return helper.finalize()  # Return the final result

def find_largest(data_batches):
    """
    Finds the batch with the largest total amount * rate.

    Args:
        data_batches (list): A list of data batches.

    Returns:
        dict: The batch with the largest total amount * rate, or None if the list is empty.
    """
    max_data = None  # Initialize to None
    largest = 0  # Initialize the largest total to 0
    for batch in data_batches:
        total = 0
        for data in batch.get('data', []):
            total += data['amount'] * data['rate']  # Calculate total for the current batch
        if total > largest:
            largest = total  # Update largest if current total is bigger
            max_data = batch  # Store the batch with the largest total
    return max_data

def aux_calc(lst):
    """
    Finds the highest 'amount' value in a list of dictionaries.

    Args:
        lst (list): A list of dictionaries, each containing an 'amount' key.

    Returns:
        int: The highest 'amount' value found in the list.
    """
    highest = 0
    for item in lst:
        if item['amount'] > highest:
            highest = item['amount']
    return highest

def sum_total(data, multiplier):
    """
    Calculates the sum of values in a list, applying a multiplier and a potential discount.

    Args:
        data (dict): A dictionary containing a list of dictionaries under the 'info' key.
        multiplier (float): A multiplier to apply to each 'value'.

    Returns:
        float: The total sum after applying the multiplier and potential discount.
    """
    total_sum = 0
    for item in data.get('info', []):
        total_sum += item['value'] * multiplier
    if total_sum > 1000:
        total_sum *= 0.95  # Apply a 5% discount if total_sum is over 1000
    return total_sum

if __name__ == "__main__":
    # Sample data for testing
    sample_data = [
        {"data": [{"amount": 60, "rate": 20}, {"amount": 30, "rate": 15}]},
        {"data": [{"amount": 10, "rate": 5}, {"amount": 200, "rate": 1.5}]},
    ]

    batch_data = [
        {"data": [{"amount": 80, "rate": 12}, {"amount": 15, "rate": 10}]},
        {"data": [{"amount": 20, "rate": 25}, {"amount": 50, "rate": 7}]},
    ]

    result = batch_proc(sample_data, 500)

    largest_data = find_largest(batch_data)

    item_list = [{"amount": 10}, {"amount": 40}, {"amount": 5}, {"amount": 100}]
    highest_amount = aux_calc(item_list)

    data_with_values = {"info": [{"value": 500}, {"value": 700}, {"value": 200}]}
    total_with_multiplier = sum_total(data_with_values, 2)
