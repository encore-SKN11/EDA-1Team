import pandas as pd

data = [
    ["선수명", "구단", "경기", "타율", "타수", "안타", "2루타", "3루타", "홈런", "타점", "도루", "수비율", "실책", "자살", "보살", "비고"],
    ["박재홍", "SK", 115, 0.280, 347, 97, 19, 1, 17, 54, 10, 0.984, 3, 174, 5, "장타율8위 / 홈런9위 / 타격25위"],
    ["이종욱", "두산", 123, 0.316, 465, 147, 20, 12, 1, 46, 47, 1.000, 0, 257, 5, "득점,도루2위 / 최다안타3위 / 타격7위 / 출루율10위"],
    ["박한이", "삼성", 123, 0.267, 479, 128, 12, 1, 2, 27, 10, 0.980, 6, 280, 11, "득점8위"],
    ["심정수", "삼성", 124, 0.258, 427, 110, 17, 0, 31, 101, 6, 1.000, 0, 125, 11, "홈런,타점1위 / 장타율6위"],
    ["박용택", "LG", 126, 0.278, 479, 133, 24, 4, 14, 66, 20, 0.987, 3, 226, 5, "득점7위/도루,최다안타9위/타격26위"],
    ["발데스", "LG", 116, 0.283, 435, 123, 15, 0, 13, 72, 4, 0.988, 2, 162, 6, "타점10위 / 타격19위"],
    ["이대형", "LG", 125, 0.308, 451, 139, 13, 1, 1, 31, 53, 0.987, 4, 295, 3, "도루1위/최다안타4위/득점8위/타격12위"],
    ["송지만", "현대", 120, 0.281, 413, 116, 25, 0, 15, 64, 10, 0.991, 2, 211, 7, "타격23위"],
    ["이택근", "현대", 116, 0.313, 438, 137, 15, 1, 11, 56, 6, 0.989, 2, 172, 1, "득점,최다안타6위 / 타격9위"],
    ["전준호", "현대", 121, 0.296, 371, 110, 8, 1, 1, 13, 11, 0.983, 2, 111, 3, "타격14위"],
    ["김주찬", "롯데", 113, 0.261, 387, 101, 17, 1, 5, 30, 22, 0.986, 3, 198, 10, "도루7위"],
    ["정수근", "롯데", 105, 0.293, 341, 100, 25, 1, 4, 36, 10, 0.976, 3, 120, 3, "타격15위"],
    ["이용규", "KIA", 118, 0.280, 439, 123, 17, 8, 0, 27, 17, 0.996, 1, 242, 1, "타격24위"]
]

df = pd.DataFrame(data)

df.to_csv("baseball_stats_2007.csv", index=False, encoding="utf-8-sig")