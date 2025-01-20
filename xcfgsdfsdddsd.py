import logging


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="error_log.log"
)

class Calculator:

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            logging.error("Division by zero error occurred", exc_info=True)
            return "Error: Division by zero is not allowed."
        except Exception as e:
            logging.error("An unexpected error occurred", exc_info=True)
            return f"Error: {str(e)}"

if __name__ == "__main__":
    calc = Calculator()

    print(calc.divide(10, 2))
    print(calc.divide(10, 0))
    print(calc.divide("10", 2))
