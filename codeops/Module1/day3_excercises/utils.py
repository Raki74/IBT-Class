# utils.py
# A utility module with reusable functions

def add_tax(price, rate=0.15):
    # Returns the price including tax
    return price + (price * rate)
