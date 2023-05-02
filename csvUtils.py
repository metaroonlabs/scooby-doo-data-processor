import csv
import re


def split_long_plots(input_file, output_file, max_tokens=1000):
    with open(input_file, "r", newline="", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        writer.writerow(headers)

        for row in reader:
            plot = row[headers.index("Plot")]
            tokens = plot.split()
            chunks = []

            for i in range(0, len(tokens), max_tokens):
                chunk = " ".join(tokens[i:i + max_tokens])
                chunks.append(chunk)

            for chunk in chunks:
                new_row = row.copy()
                new_row[headers.index("Plot")] = chunk
                writer.writerow(new_row)


def remove_nbsp(input_file, output_file):
    with open(input_file, "r", newline="", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            new_row = [col.replace(u'\xa0', u' ') for col in row]
            writer.writerow(new_row)


def remove_custom_character(input_file, output_file, custom_char):
    with open(input_file, "r", newline="", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            new_row = [col.replace(custom_char, '') for col in row]
            writer.writerow(new_row)


def remove_season_episode_indicators(input_file, output_file):
    pattern = re.compile(r"S\d{2}E\d{2}")

    with open(input_file, "r", newline="", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            new_row = [pattern.sub("", col) for col in row]
            writer.writerow(new_row)
