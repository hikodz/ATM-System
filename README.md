# ATM System

This is a command-line based ATM (Automated Teller Machine) system implemented in Python. It allows users to perform various banking operations such as depositing, withdrawing, transferring funds, checking balance, and viewing transaction history. Additionally, it includes a customer management system for creating and managing user accounts, cards, and personal information.

## Features

- Add a new card by entering the card number and CVV
- Deposit cash into the account
- Withdraw cash from the account
- Transfer funds to another account
- Check account balance
- Recharge mobile number
- View transaction history (deposits, withdrawals, transfers)
- Quit the ATM system

- Show account information
- Change CVV (Card Verification Value)
- Create new card
- Show card information
- Change account password
- Remove account
- Logout

## Prerequisites

- Python 3.x
- Inquirer library (`pip install inquirer`)
- Simple Chalk library (`pip install simple-chalk`)

## Usage

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the `ATM.py` file using Python: `python ATM.py`
4. Follow the prompts to perform various ATM operations or customer account management tasks.

## File Structure

- `ATM.py`: The main file containing the ATM system logic and user interface.
- `Customer.py`: Contains the customer account management logic and user interface.
- `backend/database.py`: Contains the `DataBaseUsage` class for handling data storage and retrieval.
- `backend/effect.py`: Contains the `Effect` class for displaying progress bars and other visual effects.
- `backend/Card.py`: Contains the `Card` class for generating and managing card information.

## Dependencies

- `inquirer`: A Python library for creating interactive command-line user interfaces.
- `simple_chalk`: A Python library for adding colors and styles to terminal output.
- `re`: The Python regular expression module for input validation.
- `abc`: The Python abstract base class module for defining abstract classes.
- `datetime`: The Python module for working with dates and times.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
