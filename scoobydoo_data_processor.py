import argparse
import math
import re

import pandas as pd


# Add ASCII text logo and main menu
def display_logo():
    logo = r"""
  ______                                 __                 
 /      \                               |  \                
|  $$$$$$\  _______   ______    ______  | $$____   __    __ 
| $$___\$$ /       \ /      \  /      \ | $$    \ |  \  |  \
 \$$    \ |  $$$$$$$|  $$$$$$\|  $$$$$$\| $$$$$$$\| $$  | $$
 _\$$$$$$\| $$      | $$  | $$| $$  | $$| $$  | $$| $$  | $$
|  \__| $$| $$_____ | $$__/ $$| $$__/ $$| $$__/ $$| $$__/ $$
 \$$    $$ \$$     \ \$$    $$ \$$    $$| $$    $$ \$$    $$
  \$$$$$$   \$$$$$$$  \$$$$$$   \$$$$$$  \$$$$$$$  _\$$$$$$$
                                                  |  \__| $$
                                                   \$$    $$
                                                    \$$$$$$ 
    """
    print(logo)


def main_menu():
    print("\nScoobyDoo Data Processor - Main Menu")
    print("1. Split long plots")
    print("2. Remove non-breaking spaces (NBSP)")
    print("3. Exit\n")
    print("-i", "--input", "Input CSV file path")
    print("-o", "--output", "Output CSV file path")
    print("-t", "--tokens", "Maximum tokens per plot chunk (default: 1000)")


# Create a function to handle user input
def get_user_choice():
    return input("Please select an option (1-3): ")


# Function to remove season and episode indicators from all columns and rows
def remove_season_episode(text):
    return re.sub(r'S\d{2}E\d{2}', '', text)


# to split the text into chunks, ensuring that the split occurs at the end of a sentence, denoted by a period
def split_at_sentence(text, max_tokens):
    tokens = text.split()
    chunks = []
    chunk = []

    for token in tokens:
        chunk.append(token)

        if token.endswith('.') and len(chunk) >= max_tokens:
            chunks.append(' '.join(chunk))
            chunk = []

    if chunk:
        chunks.append(' '.join(chunk))

    return chunks


# Function to split a plot into smaller chunks based on the user-defined token limit
def split_plot(plot, max_tokens):
    words = plot.split()
    num_parts = math.ceil(len(words) / max_tokens)
    tokens_per_part = math.ceil(len(words) / num_parts)

    chunks = []
    for i in range(0, len(words), tokens_per_part):
        chunk = ' '.join(words[i:i + tokens_per_part])
        chunks.append(chunk)

    return chunks


def tokenize(text):
    return re.findall(r'\b\w+\b', text)


def get_num_chunks(tokens, max_tokens):
    return (len(tokens) + max_tokens - 1) // max_tokens


# Function to process the data by either splitting long plots or removing specific characters
# Updated process_data function with 'remove_se' option
def process_data(df, max_tokens, action):
    new_rows = []

    for index, row in df.iterrows():
        if action == 'split':
            plot_source_name = row['Plot Source Name']
            plot = row['Plot']

            tokens = tokenize(plot)
            num_chunks = get_num_chunks(tokens, max_tokens)

            for i in range(num_chunks):
                chunk_start = i * max_tokens
                chunk_end = min((i + 1) * max_tokens, len(tokens))
                chunk_tokens = tokens[chunk_start:chunk_end]

                new_row = {}
                new_row['Plot Source Name'] = f"{plot_source_name} - part {i + 1}"
                new_row['Plot'] = ' '.join(chunk_tokens)
                new_rows.append(new_row)

        elif action == 'remove_nbsp':
            new_row = row.copy()
            new_row['Plot'] = new_row['Plot'].replace(u'\xa0', u' ')
            new_rows.append(new_row)

        elif action == 'remove_custom':
            custom_char = input("Enter the custom character(s) to remove: ")
            new_row = row.copy()
            new_row['Plot'] = new_row['Plot'].replace(custom_char, '')
            new_rows.append(new_row)

        elif action == 'remove_season_episode':
            new_row = row.copy()
            new_row['Plot'] = re.sub(r'S\d{2}E\d{2}', '', new_row['Plot'])
            new_rows.append(new_row)

    return pd.DataFrame(new_rows)


# Function to read a CSV file using pandas and return a DataFrame
def read_csv(file_path):
    return pd.read_csv(file_path)


# Function to write a DataFrame to a CSV file using pandas
def write_csv(df, file_path):
    df.to_csv(file_path, index=False)


def parse_args():
    parser = argparse.ArgumentParser(description="ScoobyDoo Data Tool")
    parser.add_argument("-i", "--input", help="Input CSV file path")
    parser.add_argument("-o", "--output", help="Output CSV file path")
    parser.add_argument("-t", "--tokens", type=int, default=1000, help="Maximum tokens per plot chunk (default: 1000)")
    return parser.parse_args()


# Create a function to handle the selected action
def handle_action(choice, args):
    if choice == "1":
        args.action = "splitter"
        return True
    elif choice == "2":
        args.action = "remove_nbsp"
        return True
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option, please try again.")
        return False


# Main function for handling user inputs and calling appropriate functions
def main():
    while True:
        display_logo()
        print("ScoobyDoo Data Processor")
        print("-------------------------")
        print("1. Split long plots")
        print("2. Remove specific characters")
        print("3. Exit")
        choice = input("Please select an option (1-3): ")

        if choice == "1":
            input_file = input("Enter the Input CSV file path: ")
            df = read_csv(input_file)
            max_tokens = int(input("Enter the maximum tokens per plot chunk (default: 1000): "))
            result = process_data(df, max_tokens, 'split')

        elif choice == "2":
            print("1. Remove non-breaking spaces (NBSP)")
            print("2. Remove custom character")
            print("3. Remove season and episode indicators")
            sub_choice = input("Please select an option (1-3): ")

            input_file = input("Enter the Input CSV file path: ")
            df = read_csv(input_file)

            if sub_choice == "1":
                result = process_data(df, None, 'remove_nbsp')
            elif sub_choice == "2":
                custom_char = input("Enter the custom character to remove: ")
                result = process_data(df, custom_char, 'remove_custom')
            elif sub_choice == "3":
                result = process_data(df, None, 'remove_season_episode')

        elif choice == "3":
            print("Exiting...")
            break

        if choice in ['1', '2']:
            output_file = input("Enter the Output CSV file path: ")
            result.to_csv(output_file, index=False)
            print(f"Data processed! Results saved to {output_file}\n")


# the conditional block
if __name__ == "__main__":
    main()
