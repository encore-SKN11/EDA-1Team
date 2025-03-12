import pandas as pd

data = [
    ["선수명", "구단", "경기", "타율", "타수", "안타", "2루타", "3루타", "홈런", "타점", "도루", "수비율", "실책", "자살", "보살", "비고"],
    ["박한이", "삼성", 123, 0.295, 471, 139, 21, 0, 9, 59, 12, 0.984, 4, 237, 11, "안타 3위, 타격 11위"],
    ["심정수", "삼성", 124, 0.275, 433, 119, 14, 0, 28, 87, 3, 0.988, 1, 84, 1, "홈런 2위, 타점/득점 3위 출루율 4위, 장타율 5위, 타격 24위"],
    ["임재철", "두산", 109, 0.310, 336, 104, 13, 3, 3, 30, 10, 0.972, 6, 204, 6, "타격 6위"],
    ["박재홍", "S K", 109, 0.304, 421, 128, 21, 1, 18, 63, 22, 0.991, 2, 223, 5, "득점 4위, 출루율 6위 타격/도루 7위, 안타/장타율 10위"],
    ["이진영", "S K", 122, 0.291, 453, 132, 19, 1, 20, 74, 8, 0.987, 3, 215, 8, "득점 4위, 안타 7위 타점 8위, 타격 15위"],
    ["데이비스", "한화", 118, 0.323, 431, 139, 24, 0, 24, 86, 7, 0.982, 4, 213, 9, "득점 1위, 타격/출루율 2위 안타/장타율 3위, 홈런/타점 4위"],
    ["조원우", "한화", 95, 0.302, 351, 106, 17, 1, 6, 42, 7, 1.000, 0, 124, 4, "타격 9위"],
    ["정수근", "롯데", 109, 0.286, 370, 106, 21, 2, 0, 29, 21, 0.961, 7, 169, 3, "도루 8위, 타격 17위"],
    ["펠로우", "롯데", 109, 0.284, 398, 113, 15, 1, 23, 69, 3, 0.978, 4, 169, 5, "홈런/장타율 6위, 타격 20위"],
    ["박용택", "L G", 126, 0.280, 472, 132, 25, 1, 15, 71, 43, 0.994, 1, 156, 1, "득점/도루 1위 안타 7위, 타격 21위"],
    ["이병규", "L G", 119, 0.337, 466, 157, 24, 2, 9, 75, 10, 0.996, 1, 226, 9, "타격/안타 1위, 타점 7위 출루율 8위"],
    ["클리어", "L G", 110, 0.303, 402, 122, 23, 4, 15, 61, 19, 0.990, 1, 102, 2, "타격 8위, 장타율 9위"],
    ["서튼", "현대", 119, 0.292, 424, 124, 18, 2, 35, 102, 0, 0.979, 2, 92, 2, "홈런/타점/장타율 1위, 출루율 3위 득점 4위, 타격 14위"],
    ["이종범", "기아", 118, 0.312, 430, 134, 25, 2, 6, 36, 28, 0.981, 4, 195, 7, "타격 5위, 안타/도루 6위 출루율 7위, 득점 10위"]
]

df = pd.DataFrame(data)

df.to_csv("baseball_stats_2005.csv", index=False, encoding="utf-8-sig")