# Mini Project: Bank Transaction Analyzer
# Demonstrates recursion, searching, and sorting on transaction data

transactions = [
    {"amount": 500, "date": "2026-01-05", "type": "deposit"},
    {"amount": -200, "date": "2026-01-10", "type": "withdrawal"},
    {"amount": 1500, "date": "2026-01-03", "type": "deposit"},
    {"amount": -50, "date": "2026-01-15", "type": "withdrawal"},
    {"amount": 300, "date": "2026-01-08", "type": "deposit"},
]


def calculate_total_balance(txns):
    # Recursive function to sum all transaction amounts
    if len(txns) == 0:
        return 0
    return txns[0]["amount"] + calculate_total_balance(txns[1:])


def sort_by_amount(txns):
    # Uses Python's built-in sort (Timsort, O(n log n)) - efficient for real use
    return sorted(txns, key=lambda t: t["amount"])


def sort_by_date(txns):
    return sorted(txns, key=lambda t: t["date"])


def linear_search_by_type(txns, txn_type):
    # O(n) - works on unsorted data
    results = []
    for txn in txns:
        if txn["type"] == txn_type:
            results.append(txn)
    return results


def binary_search_by_amount(sorted_txns, target_amount):
    # O(log n) - requires the list to be sorted by amount first
    low = 0
    high = len(sorted_txns) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_txns[mid]["amount"] == target_amount:
            return sorted_txns[mid]
        elif sorted_txns[mid]["amount"] < target_amount:
            low = mid + 1
        else:
            high = mid - 1
    return None


def report_above_threshold(txns, threshold, index=0, results=None):
    # Recursive function to build a report of transactions above a threshold
    if results is None:
        results = []
    if index >= len(txns):
        return results
    if txns[index]["amount"] > threshold:
        results.append(txns[index])
    return report_above_threshold(txns, threshold, index + 1, results)


# --- Demonstrate everything ---

print("--- All Transactions ---")
for t in transactions:
    print(t)

total = calculate_total_balance(transactions)
print(f"\nTotal balance (via recursion): {total}")

sorted_by_amount = sort_by_amount(transactions)
print(f"\nSorted by amount: {[t['amount'] for t in sorted_by_amount]}")

sorted_by_date = sort_by_date(transactions)
print(f"Sorted by date: {[t['date'] for t in sorted_by_date]}")

deposits = linear_search_by_type(transactions, "deposit")
print(f"\nDeposits found (linear search): {len(deposits)}")

found = binary_search_by_amount(sorted_by_amount, 1500)
print(f"Binary search for amount 1500: {found}")

report = report_above_threshold(transactions, 400)
print(f"\nTransactions above 400 (recursive report):")
for t in report:
    print(t)