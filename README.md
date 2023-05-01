# ScoobyDoo Data Processor

The ScoobyDoo Data Processor is a Python CLI project that processes CSV files containing plot collections of the ScoobyDoo franchise. Users can choose between two tasks: splitting long plots into smaller chunks or removing non-breaking spaces (NBSP) from the texts. The tool also provides an exit option.

## Installation

### Prerequisites

-   Python 3.x installed
-   pandas library installed (Install using: `pip install pandas`)

### Clone the Repository

To get started, clone this repository to your local machine using:

`git clone https://github.com/username/scoobydoo-data-processor.git
cd scoobydoo-data-processor` 

## Running with a Shell Script

You can run the ScoobyDoo Data Processor using a shell script for a more convenient execution.

### Creating the Shell Script

Create a new file named `run_scoobydoo_data_processor.sh` in the project folder and add the following content:

`#!/bin/sh

python scoobydoo_data_processor.py -i input.csv -o output.csv -t 1000` 

### Making the Script Executable

In your terminal, navigate to the project folder and make the script executable by running:

`chmod +x run_scoobydoo_data_processor.sh` 

### Running the Script

To run the script, execute the following command in your terminal (bash, zsh, or other compatible shells):
```
./run_scoobydoo_data_processor.sh
```
The shell script will run the `scoobydoo_data_processor.py` script with the specified input, output, and token parameters.

## Usage

Run the `scoobydoo_data_processor.py` script:

`python scoobydoo_data_processor.py -i input.csv -o output.csv -t 1000` 

-   `-i`, `--input`: Input CSV file path
-   `-o`, `--output`: Output CSV file path
-   `-t`, `--tokens`: Maximum tokens per plot chunk (default: 1000)

The main menu will be displayed. Choose between splitting long plots, removing non-breaking spaces (NBSP), or exiting the program. The output will be saved in the specified output file path.

## Contributing

1.  Fork the repository on GitHub.
2.  Clone the forked repository to your local machine.
3.  Create a new branch for your feature or bugfix (`git checkout -b my-feature`).
4.  Commit your changes (`git commit -m 'Add my feature'`).
5.  Push your branch to your fork on GitHub (`git push origin my-feature`).
6.  Open a pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.

The project documentation has been updated to include the complete `scoobydoo_data_processor.py` script provided earlier. This should cover all the requested features and provide a clear guide on how to use and contribute to the project.
