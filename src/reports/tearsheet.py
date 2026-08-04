from pathlib import Path

import pandas as pd
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

INPUT_FILE = Path("output/cashflow_intelligence.xlsx")
OUTPUT_DIR = Path("reports/tearsheets")


def create_tearsheet(row):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdf_path = OUTPUT_DIR / f"{row['company_name']}_tearsheet.pdf"

    doc = SimpleDocTemplate(str(pdf_path))
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph(f"<b>{row['company_name']}</b>", styles["Title"]))
    story.append(Paragraph(f"Sector: {row['sector']}", styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Cash Flow Intelligence</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            f"CFO Quality: {row['cfo_quality_label']} ({row['cfo_quality_score']})",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"CapEx Intensity: {row['capex_intensity_pct']}% ({row['capex_label']})",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"Free Cash Flow: {row['free_cash_flow']}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"Capital Allocation: {row['capital_allocation']}",
            styles["Normal"],
        )
    )

    story.append(
        Paragraph(
            f"Distress Flag: {row['distress_flag']}",
            styles["Normal"],
        )
    )

    doc.build(story)

    return pdf_path


def main():
    df = pd.read_excel(INPUT_FILE)

    for _, row in df.iterrows():
        pdf = create_tearsheet(row)
        print(f"Generated: {pdf}")


if __name__ == "__main__":
    main()