import pandas as pd

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
def process_data(df, max_tokens):
    new_rows = []

    for index, row in df.iterrows():
        chunks = split_plot(row['Plot'], max_tokens)

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
def main(input_file_path, output_file_path, max_tokens=1000):
    df = read_csv(input_file_path)
    processed_df = process_data(df, max_tokens)
    write_csv(processed_df, output_file_path)


# Execute the script
if __name__ == '__main__':
    input_file_path = 'input.csv'
    output_file_path = 'output.csv'
    max_tokens = 1000

    main(input_file_path, output_file_path, max_tokens)

