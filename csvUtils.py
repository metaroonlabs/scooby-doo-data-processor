import csv
import re
import roman

import re

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
            plot_source_name = row[headers.index("Plot Source Name")]

            # Split plot into sentences
            sentences = re.split(r'(?<=\.)\s+', plot)

            # Split sentences into chunks with max_tokens
            chunks, chunk = [], []
            token_count = 0
            for sentence in sentences:
                sentence_tokens = len(sentence.split())
                if token_count + sentence_tokens <= max_tokens:
                    chunk.append(sentence)
                    token_count += sentence_tokens
                else:
                    chunks.append(chunk)
                    chunk = [sentence]
                    token_count = sentence_tokens
            if chunk:
                chunks.append(chunk)

            if len(chunks) == 1:
                writer.writerow(row)
            else:
                for idx, chunk in enumerate(chunks):
                    part = idx + 1

                    new_row = row.copy()
                    new_row[headers.index("Plot Source Name")] = f"{plot_source_name} - part {roman.toRoman(part)}"
                    if part > 1:
                        chunk[0] = chunk[0]

                    new_row[headers.index("Plot")] = " ".join(chunk)
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
