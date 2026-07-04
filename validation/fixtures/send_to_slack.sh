#!/bin/bash
# 毎朝9時にcronで実行。前夜の日次レポートを営業チームのSlackにアップロードする。
set -euo pipefail

SLACK_TOKEN="${SLACK_BOT_TOKEN:?}"
REPORT_FILE="reports/daily_report.csv"

curl -sf -F "file=@${REPORT_FILE}" \
     -F "channels=#sales-daily" \
     -F "initial_comment=昨日の日次売上レポートです" \
     -H "Authorization: Bearer ${SLACK_TOKEN}" \
     https://slack.com/api/files.upload
