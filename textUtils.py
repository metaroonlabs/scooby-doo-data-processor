import csv


def generate_text_file(input_file, num_story_inputs=None):
    data = []

    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        for index, row in enumerate(reader):
            if num_story_inputs is not None and index >= num_story_inputs:
                break

            plot_source = row[headers.index("Plot Source Name")]
            plot = row[headers.index("Plot")]

            data.append(f"Plot Source Title: {plot_source}\nStory Plot: {plot}\n")

    with open("story_plots.txt", "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(data))
