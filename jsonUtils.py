import csv
import json


def prepare_story_plots(input_file, num_json_objects=None):
    data = []

    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        for index, row in enumerate(reader):
            if num_json_objects is not None and index >= num_json_objects:
                break

            plot_source = row[headers.index("Plot Source Name")]
            plot = row[headers.index("Plot")]

            data.append({"plot_source_name": plot_source, "plot": plot})

    with open("story_plots.json", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
