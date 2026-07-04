"""日次売上レポートをCSVに書き出すスクリプト。

cron で毎晩23時に実行される。
"""

import csv

from db import fetch_daily_sales  # 社内DBユーティリティ

OUTPUT_PATH = "reports/daily_report.csv"


def export() -> None:
    rows = fetch_daily_sales()
    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["customer_id", "product", "amount"])
        for row in rows:
            writer.writerow([row["customer_id"], row["product"], row["amount"]])


if __name__ == "__main__":
    export()
