import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count ={
    'A':2,
    'B':3,
    'C':4
}

all_symbols = []

for symbol,count in symbol_count.items():
    for _ in range(count):
        all_symbols.append(symbol)
print(all_symbols)

output_column =[]
duplicate_symbol = all_symbols[:]
for _ in range(COLS):
    temp_column =[]
    for _ in range(ROWS):
        value = random.choice(duplicate_symbol)
        temp_column.append(value)
        duplicate_symbol.remove(value)
    output_column.append(temp_column)

print(output_column)

#for row in range(len(output_column[0])):
for item in output_column:
    for box in item:
        print(box,end='|')
    print('\n')
#added for testing.           
            

def deposit():
    while True:
        amount= input("Enter the amount  want to give- ")
        if amount.isdigit():
            amount= int(amount)
            if amount>0:
                break
            else:
                print("Enter the amount greater than 0")
        else:
            print("Please enter the valid amount")
    return amount

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines you want to bet 1-"+str(MAX_LINES)+"?")
        if lines.isdigit():
            lines= int(lines)
            if 1<= lines<= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter number")
    return lines

def get_bet():
    while True:
        amount = input(f"Please enter the amount you want to bet -{MIN_BET} - {MAX_BET}- ")      
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print(f"Enter the amount between -{MIN_BET} - {MAX_BET} ")
        else:
            print("Please enter the valid amount")
    return amount    
        


def main():
    balance= deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"your total bet is not enough as you have balance of - {balance}")
        else:
            break
    

    print(balance, lines)

main()
    



