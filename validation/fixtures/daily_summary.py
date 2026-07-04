"""顧客イベントの日次バッチ処理。

cron で深夜に実行される。データ量が増える月末にメモリ不足で落ちるとの報告あり。
出力の daily_summary.json は翌朝のダッシュボード集計が読み込む。
"""

import csv
import json

INPUT_PATH = "/data/events/daily_events.csv"
OUTPUT_PATH = "/data/events/daily_summary.json"
BATCH_SIZE = 1000


def transform(rows: list[dict]) -> list[dict]:
    summaries = []
    for row in rows:
        summaries.append(
            {
                "customer_id": row["customer_id"],
                "event": row["event_type"].lower().strip(),
                "value": float(row["value"] or 0),
            }
        )
    return summaries


def run() -> None:
    all_results = []
    batch = []
    with open(INPUT_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            batch.append(row)
            if len(batch) >= BATCH_SIZE:
                all_results.extend(transform(batch))
                batch = []
        if batch:
            all_results.extend(transform(batch))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False)


if __name__ == "__main__":
    run()
