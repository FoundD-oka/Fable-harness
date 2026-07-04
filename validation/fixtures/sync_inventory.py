"""在庫データを基幹システムからECサイトへ同期するスクリプト。

cron で1時間ごとに実行される。
"""

from api_clients import fetch_stock, push_stock  # 社内APIユーティリティ


def sync() -> None:
    print("sync start")
    items = fetch_stock()
    updated = 0
    for item in items:
        if item["stock"] < 0:
            print(f"skip: negative stock {item['sku']}")
            continue
        push_stock(item["sku"], item["stock"])
        updated += 1
    print(f"updated {updated} items")
    print("SYNC OK")


if __name__ == "__main__":
    sync()
