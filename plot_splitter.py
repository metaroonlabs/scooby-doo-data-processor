import argparse
import pandas as pd

# Add ASCII text logo and argument parser
def display_logo():
    logo = r"""
  ____                  _          ____        _     
 / ___|  ___ _ ____   _(_) ___ ___|  _ \ _   _| |__  
 \___ \ / _ \ '__\ \ / / |/ __/ _ \ | | | | | | '_ \ 
  ___) |  __/ |   \ V /| | (_|  __/ |_| | |_| | |_) |
 |____/ \___|_|    \_/ |_|\___\___|____/ \__,_|_.__/ 
    """
    print(logo)


def parse_args():
    parser = argparse.ArgumentParser(description="ScoobyDoo Plot Splitter")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file path")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file path")
    parser.add_argument("-t", "--tokens", type=int, default=1000, help="Maximum tokens per plot chunk (default: 1000)")
    parser.add_argument("-r", "--remove-nbsp", action="store_true", help="Remove non-breaking spaces from the texts")
    return parser.parse_args()


# Read the input CSV file
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


# Define the function to split the plots
def split_plot(plot, max_tokens):
    tokens = plot.split()
    chunks = [' '.join(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]
    return chunks


# Process the DataFrame
def process_data(df, max_tokens, remove_nbsp):
    new_rows = []

    for index, row in df.iterrows():
        plot = row['Plot']
        if remove_nbsp:
            plot = plot.replace(u'\xa0', u' ')

        chunks = split_plot(plot, max_tokens)

        for i, chunk in enumerate(chunks):
            new_row = row.copy()
            if i > 0:
                new_row['Plot Source Name'] = f"{row['Plot Source Name']} - part {i + 1}"
                new_row['Plot'] = f"part {i + 1} - {chunk}"
            new_rows.append(new_row)

    return pd.DataFrame(new_rows)


# Write the output CSV file
def write_csv(df, output_file_path):
    df.to_csv(output_file_path, index=False)


# Define the main function
def main(args):
    display_logo()
    df = read_csv(args.input)
    processed_df = process_data(df, args.tokens, args.remove_nbsp)
    write_csv(processed_df, args.output)



# Execute the script
if __name__ == '__main__':
    args = parse_args()
    main(args)


