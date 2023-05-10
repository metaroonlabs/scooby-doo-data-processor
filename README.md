# ScoobyDoo CSV Tool with Tkinter GUI

ScoobyDoo CSV Tool is a Python application that processes CSV files containing story plot information. It provides the
following functionalities:

## Features

1. **Split long plots**: Splits long plots in a CSV file into multiple smaller plots, based on a given maximum token
   count.
2. **Remove specific characters**: This feature provides several options:
   - Remove non-breaking spaces (NBSP)
   - Remove custom character
   - Remove season and episode indicators
3. **Story plots data preparation to a JSON**: Extract a specified number of story plots from the CSV file and generate
   a `story_plots.json` file.
4. **Generate Text File**: Extract a specified number of story plots from the CSV file and generate a `story_plots.txt`
   file in a given format.
5. **Generate PDF File**: Extract a specified number of story plots from the CSV file and generate a `story_plots.pdf`
   file in a given format.
6. **Exit**: Exit the application.

This version of the project includes a Tkinter-based graphical user interface (GUI) for a more user-friendly experience.

## Installation

To install the required dependencies, simply run:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python scoobydoo_csv_gui.py
```

The application will open in a new window with the main menu.

### Split long plots

1. Click on the 'Split long plots' button.
2. Select the input CSV file.
3. Select the output CSV file.
4. Enter the maximum tokens per plot chunk (default: 1000).
5. Click 'OK' and the plots will be split in the output CSV file.

### Remove specific characters

1. Click on the 'Remove specific characters' button.
2. Choose one of the following options:
   - Remove non-breaking spaces (NBSP)
   - Remove custom character
   - Remove season and episode indicators
3. Select the input CSV file.
4. Select the output CSV file.
5. If you chose 'Remove custom character', enter the custom character to remove.
6. Click 'OK' and the specified characters will be removed in the output CSV file.

### Story plots data preparation to a JSON

1. Click on the 'Story plots data preparation to a JSON' button.
2. Select the input CSV file.
3. Enter the number of JSON data objects to generate (default: all CSV data).
4. Click 'OK' and a `story_plots.json` file will be generated in the current directory.

### Exit

To exit the application, click on the 'Exit' button and confirm your choice.

Sure, here's how you can update the `README.md` file in your GitHub repository to include the new features.

---

