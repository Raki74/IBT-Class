# Exercise 9: Tip Calculator
# Calculates tip, total, and per-person amount for a bill

def calculate_tip(bill, tip_percent):
    # Returns the tip amount based on percentage
    return bill * (tip_percent / 100)

def split_bill(total, people):
    # Returns the amount each person owes
    return total / people

bill_amount = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage (10, 15, or 20): "))
num_people = int(input("Enter number of people splitting the bill: "))

tip_amount = calculate_tip(bill_amount, tip_percent)
total_amount = bill_amount + tip_amount
amount_per_person = split_bill(total_amount, num_people)

print(f"\nTip amount: {tip_amount:.2f}")
print(f"Total amount: {total_amount:.2f}")
print(f"Each person pays: {amount_per_person:.2f}")


# Exercise 10: Simple Quiz Game
# A 5-question quiz about Ethiopia with a running score

def ask_question(question, correct_answer):
    # Asks a question and returns 1 if correct, 0 if wrong
    answer = input(question).strip().lower()
    if answer == correct_answer.lower():
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return 0

def show_result(score, total):
    # Prints final score and a message based on performance
    print(f"\nYour final score: {score}/{total}")
    if score == total:
        print("Perfect score! Excellent!")
    elif score >= total * 0.6:
        print("Good job!")
    else:
        print("Keep practicing!")

print("\n--- Ethiopia Quiz ---\n")
score = 0
total_questions = 5

score += ask_question("What is the capital of Ethiopia? ", "Addis Ababa")
score += ask_question("What is the official language of Ethiopia? ", "Amharic")
score += ask_question("What is the currency of Ethiopia? ", "Birr")
score += ask_question("How many seasons are commonly recognized in Ethiopia (in words: one/two/three/four)? ", "two")
score += ask_question("What calendar system does Ethiopia uniquely use? ", "Ethiopian calendar")

show_result(score, total_questions)

# Exercise 11: Function with Default & Return
# Calculates final price after tax and discount

def calculate_final_price(price, tax_rate=0.15, discount=0):
    # Applies discount first, then adds tax, and returns the final price
    discounted_price = price - (price * discount)
    final_price = discounted_price + (discounted_price * tax_rate)
    return final_price

# Test with different values
print("\n--- Final Price Calculator Tests ---")
print(f"Price 100, default tax, no discount: {calculate_final_price(100):.2f}")
print(f"Price 100, default tax, 10% discount: {calculate_final_price(100, discount=0.10):.2f}")
print(f"Price 200, tax 10%, discount 20%: {calculate_final_price(200, tax_rate=0.10, discount=0.20):.2f}")