#!/bin/bash
# cron から1時間ごとに呼ばれるラッパー。同期の成否を判定して失敗時はアラートを飛ばす。
set -uo pipefail

if python3 sync_inventory.py | grep -q "SYNC OK"; then
    exit 0
fi

curl -sf -X POST "$ALERT_WEBHOOK_URL" \
     -H 'Content-Type: application/json' \
     -d '{"text": "在庫同期が失敗しました。ログを確認してください。"}'
exit 1
