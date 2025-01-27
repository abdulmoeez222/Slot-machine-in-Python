import random

class SlotMachine:
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1

    ROWS = 3
    COLS = 3

    def __init__(self):
        self.symbol_count = {
            "A": 2,
            "B": 4,
            "C": 6,
            "D": 8
        }
        self.symbol_values = {
            "A": 5,
            "B": 4,
            "C": 3,
            "D": 2
        }

    def deposit(self):
        while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be greater than 0.")
            else:
                print("Please enter a valid number.")

    def get_number_of_lines(self):
        while True:
            lines = input(f"Enter the number of lines to bet on (1-{self.MAX_LINES}): ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self.MAX_LINES:
                    return lines
                else:
                    print("Enter a valid number of lines.")
            else:
                print("Please enter a valid number.")

    def get_bet(self):
        while True:
            amount = input(f"What would you like to bet on each line? (${self.MIN_BET}-${self.MAX_BET}): ")
            if amount.isdigit():
                amount = int(amount)
                if self.MIN_BET <= amount <= self.MAX_BET:
                    return amount
                else:
                    print(f"Amount must be between ${self.MIN_BET} and ${self.MAX_BET}.")
            else:
                print("Please enter a valid number.")

    def get_slot_machine_spin(self):
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(self.COLS):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.ROWS):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns

    def print_slot_machine(self, columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")
            print()

    def check_winning(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += self.symbol_values[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines

    def play_game(self, balance):
        lines = self.get_number_of_lines()
        while True:
            bet = self.get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough balance! Your current balance is ${balance}.")
            else:
                break

        print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

        slots = self.get_slot_machine_spin()
        self.print_slot_machine(slots)

        winnings, winning_lines = self.check_winning(slots, lines, bet)
        print(f"You won ${winnings}")
        if winning_lines:
            print(f"You won on lines: {', '.join(map(str, winning_lines))}")
        else:
            print("You did not win on any lines.")

        return winnings - total_bet

    def main(self):
        balance = self.deposit()
        while True:
            print(f"Current balance is: ${balance}")
            answer = input("Press Enter to spin (q to quit): ")
            if answer.lower() == "q":
                break
            balance_change = self.play_game(balance)
            balance += balance_change

        print(f"You left with ${balance}")

game = SlotMachine()
game.main()
