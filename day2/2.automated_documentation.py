class ProcHelper:
    def __init__(self, thresh):
        self.threshold = thresh
        self.current = 0
        self.track = []

    def part_one(self, dataset):
        for element in dataset.get('data', []):
            value = self.helper_func(element['amount'], element['rate'])
            self.track.append(value)
        if len(dataset['data']) > 5:
            self.extra_step()

    def helper_func(self, a, b):
        if a > 50:
            return a * b * 0.85 
        return a * b

    def extra_step(self):
        if sum(self.track) > self.threshold:
            self.current = sum(self.track) * 0.90

    def finalize(self):
        return self.current if self.current > 0 else sum(self.track)

def batch_proc(batch, thresh):
    helper = ProcHelper(thresh)
    for data in batch:
        helper.part_one(data)
    return helper.finalize()

def find_largest(data_batches):
    max_data = None
    largest = 0
    for batch in data_batches:
        total = 0
        for data in batch.get('data', []):
            total += data['amount'] * data['rate']
        if total > largest:
            largest = total
            max_data = batch
    return max_data

def aux_calc(lst):
    highest = 0
    for item in lst:
        if item['amount'] > highest:
            highest = item['amount']
    return highest

def sum_total(data, multiplier):
    total_sum = 0
    for item in data.get('info', []):
        total_sum += item['value'] * multiplier
    if total_sum > 1000:
        total_sum *= 0.95  # Apply a 5% discount for totals over 1000
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
