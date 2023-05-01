
# ScoobyDoo Plot Splitter

ScoobyDoo Plot Splitter is a Python project that processes CSV files containing plot collections of the ScoobyDoo franchise. It splits long plots into smaller chunks, inserting them into new rows with an appropriate naming format.

## Installation

### Prerequisites

-   Python 3.x installed
-   pandas library installed (Install using: `pip install pandas`)

### Clone the Repository

To get started, clone this repository to your local machine using:

bashCopy code

`git clone https://github.com/username/scoobydoo-plot-splitter.git
cd scoobydoo-plot-splitter` 

## Usage

1.  Place your input CSV file in the project folder and rename it to `input.csv`. Make sure it has the following format:

mathematicaCopy code

`Plot Source Name,Plot` 

2.  Run the `plot_splitter.py` script:

bashCopy code

`python plot_splitter.py` 

3.  The output will be saved in the same directory as `output.csv`.

## Contributing

1.  Fork the repository on GitHub.
2.  Clone the forked repository to your local machine.
3.  Create a new branch for your feature or bugfix (`git checkout -b my-feature`).
4.  Commit your changes (`git commit -m 'Add my feature'`).
5.  Push your branch to your fork on GitHub (`git push origin my-feature`).
6.  Open a pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.
