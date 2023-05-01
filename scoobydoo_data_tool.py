import argparse
import pandas as pd


# Add ASCII text logo and main menu
def display_logo():
    logo = r"""

  _________                  ___.          ________          __           ___________           .__   
 /   _____/ ____  ____   ____\_ |__ ___.__.\______ \ _____ _/  |______    \__    ___/___   ____ |  |  
 \_____  \_/ ___\/  _ \ /  _ \| __ <   |  | |    |  \\__  \\   __\__  \     |    | /  _ \ /  _ \|  |  
 /        \  \__(  <_> |  <_> ) \_\ \___  | |    `   \/ __ \|  |  / __ \_   |    |(  <_> |  <_> )  |__
/_______  /\___  >____/ \____/|___  / ____|/_______  (____  /__| (____  /   |____| \____/ \____/|____/
        \/     \/                 \/\/             \/     \/          \/                              

    """
    print(logo)


def main_menu():
    print("\nScoobyDoo Data Tool - Main Menu")
    print("1. Split long plots")
    print("2. Remove non-breaking spaces (NBSP)")
    print("3. Exit\n")


# Create a function to handle user input
def get_user_choice():
    return input("Please select an option (1-3): ")


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


# Define the function to split the plots
def split_plot(plot, max_tokens):
    return split_at_sentence(plot, max_tokens)


# Process the DataFrame
def process_data(df, max_tokens, remove_nbsp):
    new_rows = []

    for index, row in df.iterrows():
        plot_source_name = row['Plot Source Name']
        plot = row['Plot']

        if remove_nbsp:
            plot = plot.replace('\xa0', ' ')

        if len(plot.split()) > max_tokens:
            chunks = split_plot(plot, max_tokens)

            for i, chunk in enumerate(chunks, 1):
                new_rows.append({
                    'Plot Source Name': f"{plot_source_name} - part {i}",
                    'Plot': f"part {i}: {chunk}"
                })
        else:
            new_rows.append({'Plot Source Name': plot_source_name, 'Plot': plot})

    return pd.DataFrame(new_rows)


# Read the input CSV file
def read_csv(file_path):
    return pd.read_csv(file_path)


# Write the output CSV file
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
        main(args)
    elif choice == "2":
        args.action = "remove_nbsp"
        main(args)
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid option, please try again.")


# main function
def main(args):
    display_logo()
    main_menu()
    choice = get_user_choice()

    if args.action == "splitter":
        df = read_csv(args.input)
        processed_df = process_data(df, args.tokens, remove_nbsp=False)
        write_csv(processed_df, args.output)
    elif args.action == "remove_nbsp":
        df = read_csv(args.input)
        processed_df = process_data(df, args.tokens, remove_nbsp=True)
        write_csv(processed_df, args.output)
        handle_action(choice, args)


# the conditional block
if __name__ == '__main__':
    args = parse_args()

    while True:
        main(args)
