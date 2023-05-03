# ScoobyDooCSVTool

ScoobyDooCSVTool is a command-line interface (CLI) Python application that processes ScoobyDoo franchise data in CSV
format. The tool provides additional functionality for generating a JSON file from the CSV data.

## Features

- Split long plots into multiple rows
- Remove specific characters from plots
  - Non-breaking spaces (NBSP)
  - Custom characters
  - Season and episode indicators
- Convert CSV data to JSON format

## Installation

1. Clone the repository or download the source files.

```bash
git clone https://github.com/yourusername/ScoobyDooCSVTool.git
```

2. Navigate to the project directory.

```bash
cd ScoobyDooCSVTool
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `main.py` script.

```bash
python main.py
```

2. Follow the prompts and select the desired operation.

### Split long plots

- Enter the input CSV file path.
- Enter the output CSV file path.
- Enter the maximum tokens per plot chunk (default: 1000).
- The tool will split long plots in the input CSV file into multiple rows based on the maximum tokens value and save the
  processed data to the output CSV file.

### Remove specific characters

#### Remove non-breaking spaces (NBSP)

- Enter the input CSV file path.
- Enter the output CSV file path.
- The tool will remove non-breaking spaces from the 'Plot' column in the input CSV file and save the processed data to
  the output CSV file.

#### Remove custom character

- Enter the input CSV file path.
- Enter the output CSV file path.
- Enter the custom character to remove.
- The tool will remove the custom character from the 'Plot' column in the input CSV file and save the processed data to
  the output CSV file.

#### Remove season and episode indicators

- Enter the input CSV file path.
- Enter the output CSV file path.
- The tool will remove season and episode indicators like "S01E01" from all columns and rows in the input CSV file and
  save the processed data to the output CSV file.

### Story plots data preparation to a JSON

- Enter the input CSV file path.
- Enter the number of JSON data objects to generate (default: all CSV data).
- The tool will create a JSON file named "story_plots.json" with data from the input CSV file, where the "Plot Source
  Name" column maps to the JSON's "PlotSource" field and the "Plot" column maps to the JSON's "Plot" field.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)