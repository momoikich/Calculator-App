
# Scientific Calculator

This is a simple scientific calculator implemented in Python using the Tkinter GUI library. The calculator supports basic arithmetic operations, trigonometric functions, mathematical constants (π and e), logarithmic functions, square root, and exponentiation.

## Requirements

- Python 3.10
- tkinter 0.1.0
- sympy 1.3.0

## Usage

1. **Clone the Repository:**
   ```bash
   git clone 
   cd Calculator-App
   ```

2. **Install Dependencies (if needed):**
   The application relies on Python and the built-in Tkinter library, which is typically included with most Python installations.
   ```bash
   pip install tk==0.1.0
   ```
   ```bash
   pip install sympy==1.3.0
   ```


## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Trigonometric Functions**: sin, cos, tan.
- **Mathematical Constants**: π (pi) and e (E).
- **Logarithmic Functions**: log (base 10) and ln (natural logarithm).
- **Other Functions**: Square root (√), exponentiation (^2), and parentheses for complex expressions.
- **Error Handling**: Proper error handling for invalid expressions.

## How to Use

1. Enter the mathematical expression using the provided buttons.
2. Press the "=" button to evaluate the expression.
3. Use the "C" button to clear the entry.

## Additional Buttons

- "sin": Inserts "sin(" into the entry.
- "cos": Inserts "cos(" into the entry.
- "tan": Inserts "tan(" into the entry.
- "√": Inserts "sqrt(" for square root.
- "π": Inserts the mathematical constant π.
- "e": Inserts the mathematical constant e.
- "log": Inserts "log(" into the entry.
- "ln": Inserts "ln(" into the entry.
- "^2": Inserts "^2" for exponentiation.
- "(": Inserts "(" into the entry.
- ")": Inserts ")" into the entry.

## Important Note

- The calculator uses the `sympy` library to handle mathematical constants more accurately.

## How to Run

Ensure you have Python installed, and then run the following command:

```bash
python Calculator_App.py
```

Feel free to contribute or customize the calculator as needed!

```

Feel free to customize the README further based on your specific application and any additional details you'd like to include.
