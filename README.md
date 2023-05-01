## ScoobyDoo Data Processor

A Python script to process ScoobyDoo franchise plot data in CSV format. It provides functionalities such as splitting
long plots, removing non-breaking spaces, removing custom characters, and removing season and episode indicators.

### Clone the Repository

To get started, clone this repository to your local machine using:

`git clone https://github.com/username/scoobydoo-data-processor.git  
cd scoobydoo-data-processor`

### Requirements

- Python 3.x
- pandas library

### Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install the pandas library using pip:

```
pip install pandas
``` 

### Usage

1. Save the Python script as `scoobydoo_data_processor.py`.
2. Run the script from the terminal/command prompt:

```
python scoobydoo_data_processor.py
```

3. Follow the on-screen prompts to select the desired action and provide necessary inputs, such as input and output CSV
   file paths.
   To make the script executable, run the following command in the terminal/command prompt:

```
chmod +x run_script.sh
``` 

### Running the script using the SH file

1. Save the `run_script.sh` file in the same directory as the `scoobydoo_data_processor.py` script.
2. Open a terminal/command prompt and navigate to the directory containing both files.
3. Run the SH file:

```
./run_script.sh
``` 

This will run the `scoobydoo_data_processor.py` script and display the command-line interface for selecting the desired
action and providing necessary inputs.

### Features

1. Split long plots: Splits long plots into smaller chunks based on the user-defined token limit.
2. Remove specific characters:
    - Remove non-breaking spaces (NBSP)
    - Remove custom characters
    - Remove season and episode indicators

### Example

An example CSV file format with the first 2 columns:

```
`Plot Source Name,Plot` 
```

### Python Script

The Python script `scoobydoo_data_processor.py` processes the CSV files containing plot collections of the ScoobyDoo
franchise. The script reads a CSV file, performs the desired action, and writes the processed data to a new CSV file.
The script provides a simple command-line interface for the user to choose the desired action and input the necessary
parameters.

After implementing the script, you will be able to process the CSV files by running the script and following the
on-screen prompts. The script will guide you through selecting the desired action and providing the necessary inputs,
such as input and output CSV file paths, maximum tokens per plot chunk, and custom characters to remove.

## Contributing

1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Create a new branch for your feature or bugfix (`git checkout -b my-feature`).
4. Commit your changes (`git commit -m 'Add my feature'`).
5. Push your branch to your fork on GitHub (`git push origin my-feature`).
6. Open a pull request on the original repository.


