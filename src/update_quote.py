import random

def update_quote():
    # Define the file paths for input (all quotes) and output (quote of the day)
    # Mine are stored in the Documents and QOTD directories respectively, and I have a samsung so the path is different from IOS.
    input_file = "/storage/emulated/0/Documents/quotes.txt"  
    output_file = "/storage/emulated/0/QOTD/qotd.txt"  

    current_quote = None  # Variable to store the current quote
    quotes = []  # List to hold all available quotes

    # Attempt to read the current quote from the output file
    try:
        with open(output_file, "r", encoding="utf-8") as file:
            current_quote = file.read().strip()  
    except Exception as e:
        print(f"Error reading file: {e}") 

    # Attempt to read the list of quotes from the input file
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}") 

    # Attempt to update the output file with a new random quote
    try:
        with open(output_file, "w", encoding="utf-8") as output:
            if current_quote in quotes:
                quotes.remove(current_quote)  # Remove the current quote to avoid repetition

            if quotes:  
                quote = random.choice(quotes)  
                output.write(quote)
                print("Quote updated successfully")
            else:
                print("No available quotes to select from.")
    except Exception as e:
        print(f"Error writing file: {e}")  # Handle any file write errors  

# Run the function when the script is executed
if __name__ == "__main__":
    update_quote()

