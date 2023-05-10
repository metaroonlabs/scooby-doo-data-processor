import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf_file(input_csv, num_story_inputs):
    story_data = []

    with open(input_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            story_data.append({"title": row[0], "plot": row[1]})

    story_data = story_data[:num_story_inputs]

    pdf_output = "story_plots.pdf"
    doc = SimpleDocTemplate(pdf_output, pagesize=letter)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Bold", fontName="Helvetica-Bold"))

    story_elements = []

    for story in story_data:
        title = Paragraph(f"Plot Source Title: {story['title']}", styles["Bold"])
        plot = Paragraph(f"Story Plot: {story['plot']}", styles["Normal"])

        story_elements.append(title)
        story_elements.append(plot)
        story_elements.append(Spacer(1, 12))

    doc.build(story_elements)
