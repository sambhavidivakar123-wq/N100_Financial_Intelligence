from pathlib import Path

import pandas as pd
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate

INPUT_FILE = Path("output/cashflow_intelligence.xlsx")
OUTPUT_FILE = Path("reports/portfolio/portfolio_summary.pdf")


def main():
    df = pd.read_excel(INPUT_FILE)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(str(OUTPUT_FILE))
    styles = getSampleStyleSheet()

    story = []

    for _, row in df.sort_values("company_name").iterrows():

        story.append(
            Paragraph(f"<b>{row['company_name']}</b>", styles["Title"])
        )

        story.append(
            Paragraph(f"Sector: {row['sector']}", styles["Normal"])
        )

        story.append(
            Paragraph(
                f"CFO Quality: {row['cfo_quality_label']} ({row['cfo_quality_score']})",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"CapEx: {row['capex_label']} ({row['capex_intensity_pct']}%)",
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

        story.append(PageBreak())

    doc.build(story)

    print(f"Portfolio summary created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()