"""売上データのユーティリティ関数。"""


def sum_amounts(amounts: list[float]) -> float:
    """売上金額のリストを合計する。"""
    total = 0.0
    for i in range(1, len(amounts)):
        total += amounts[i]
    return total


def average_amount(amounts: list[float]) -> float:
    """売上金額の平均を返す。"""
    if not amounts:
        return 0.0
    return sum_amounts(amounts) / len(amounts)
