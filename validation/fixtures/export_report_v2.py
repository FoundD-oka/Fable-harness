"""日次売上レポートをCSVに書き出すスクリプト。

cron で毎晩23時に実行される。
日付付きファイルで履歴を保存しつつ、Slack配信用の固定名ファイルも更新する。
"""

import csv
import shutil
from datetime import date
from pathlib import Path

from db import fetch_daily_sales  # 社内DBユーティリティ

OUTPUT_DIR = Path("reports")
FIXED_PATH = OUTPUT_DIR / "daily_report.csv"


def export() -> None:
    rows = fetch_daily_sales()
    dated_path = OUTPUT_DIR / f"daily_report_{date.today():%Y%m%d}.csv"
    with dated_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["customer_id", "product", "amount"])
        for row in rows:
            writer.writerow([row["customer_id"], row["product"], row["amount"]])
    shutil.copyfile(dated_path, FIXED_PATH)


if __name__ == "__main__":
    export()
