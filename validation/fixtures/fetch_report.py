"""社内レポートAPIからデータを取得するスクリプト。

cron で毎朝実行される。最近失敗が増えているとの報告あり。
"""

import time

import requests

API_URL = "https://api.internal.example.com/v1/reports/daily"
MAX_RETRIES = 5


def fetch_report(auth_token: str) -> dict:
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(
                API_URL,
                headers={"Authorization": f"Bearer {auth_token}"},
                timeout=10,
            )
            if resp.status_code != 200:
                raise RuntimeError(f"API error: {resp.status_code}")
            return resp.json()
        except Exception as e:
            last_error = e
            time.sleep(1)
    raise RuntimeError(f"failed after {MAX_RETRIES} retries: {last_error}")


if __name__ == "__main__":
    import os

    token = os.environ.get("REPORT_API_TOKEN", "")
    data = fetch_report(token)
    print(f"rows: {len(data.get('rows', []))}")
