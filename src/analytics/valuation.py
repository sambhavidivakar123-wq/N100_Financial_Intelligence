from pathlib import Path

import pandas as pd


class ValuationEngine:

    def __init__(
        self,
        financial_file="data/processed/master_financial_dataset.xlsx",
        market_cap_file="data/processed/market_cap.xlsx",
    ):

        self.financial_file = financial_file
        self.market_cap_file = market_cap_file


    def calculate_valuation(self):

        financial_df = pd.read_excel(
            self.financial_file
        )

        market_df = pd.read_excel(
            self.market_cap_file
        )


        latest = (
            financial_df
            .sort_values("year")
            .groupby("ticker")
            .tail(1)
        )


        df = latest.merge(
            market_df,
            on=[
                "company_id",
                "company_name",
                "ticker",
                "sector"
            ],
            how="left"
        )


        # Derived valuation multiples
        df["pe"] = (
            df["market_cap"]
            /
            df["net_profit"].replace(0, 1)
        )


        df["pb"] = (
            df["market_cap"]
            /
            df["equity"].replace(0, 1)
        )


        df["ev_ebitda"] = (
            df["market_cap"]
            /
            df["operating_profit"].replace(0, 1)
        )


        # FCF Yield
        df["FCF_yield_pct"] = (
            df["free_cash_flow"]
            /
            df["market_cap"]
            *
            100
        ).round(2)


        # Sector median PE

        sector_median = (
            df.groupby("sector")["pe"]
            .median()
            .rename("5yr_median_PE")
        )


        df = df.merge(
            sector_median,
            on="sector",
            how="left"
        )


        df["PE_vs_sector_median_pct"] = (
            (
                df["pe"]
                -
                df["5yr_median_PE"]
            )
            /
            df["5yr_median_PE"]
            *
            100
        ).round(2)


        def flag(row):

            if row["pe"] > row["5yr_median_PE"] * 1.5:
                return "Caution"

            elif row["pe"] < row["5yr_median_PE"] * 0.7:
                return "Discount"

            else:
                return "Fair"


        df["flag"] = df.apply(
            flag,
            axis=1
        )


        return df


    def export(self):

        Path("output").mkdir(
            exist_ok=True
        )


        df = self.calculate_valuation()


        summary = df[
            [
                "company_id",
                "company_name",
                "sector",
                "pe",
                "pb",
                "ev_ebitda",
                "FCF_yield_pct",
                "5yr_median_PE",
                "PE_vs_sector_median_pct",
                "flag"
            ]
        ]


        summary.to_excel(
            "output/valuation_summary.xlsx",
            index=False
        )


        flags = summary[
            summary["flag"]
            .isin(
                [
                    "Caution",
                    "Discount"
                ]
            )
        ]


        flags.to_csv(
            "output/valuation_flags.csv",
            index=False
        )


        print(
            "Valuation reports generated successfully"
        )