import pandas as pd

# 데이터 정의
data = [
    ["박한이", "삼성", 125, 0.331, 83, 156, 9, 80, 7, 0.443, 0.409, 0.980],
    ["최형우", "삼성", 113, 0.356, 92, 153, 31, 100, 4, 0.649, 0.426, 0.996],
    ["유한준", "넥센", 122, 0.316, 71, 128, 20, 91, 2, 0.541, 0.384, 0.995],
    ["이택근", "넥센", 122, 0.306, 87, 135, 21, 91, 11, 0.526, 0.386, 0.977],
    ["나성범", "NC", 123, 0.329, 88, 157, 30, 101, 14, 0.597, 0.400, 0.989],
    ["박용택", "LG", 124, 0.343, 71, 159, 9, 73, 11, 0.461, 0.430, 0.995],
    ["이병규(7)", "LG", 116, 0.306, 66, 110, 16, 87, 5, 0.533, 0.423, 0.995],
    ["김강민", "SK", 113, 0.302, 86, 130, 16, 82, 32, 0.495, 0.368, 0.987],
    ["김현수", "두산", 125, 0.322, 75, 149, 17, 90, 2, 0.488, 0.396, 0.996],
    ["민병헌", "두산", 124, 0.345, 85, 162, 12, 79, 16, 0.500, 0.395, 1.000],
    ["정수빈", "두산", 128, 0.306, 79, 132, 6, 49, 32, 0.422, 0.379, 0.997],
    ["손아섭", "롯데", 122, 0.362, 105, 175, 18, 80, 10, 0.538, 0.456, 0.984],
    ["피 에", "한화", 119, 0.326, 61, 145, 17, 92, 9, 0.524, 0.373, 0.980],
    ["이대형", "kt", 126, 0.323, 75, 149, 1, 40, 22, 0.401, 0.372, 0.988],
]

columns = ["선수명", "구단", "경기", "타율", "득점", "안타", "홈런", "타점", "도루", "장타율", "출루율", "수비율"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("baseball_stats_2014.csv", index=False, encoding="utf-8-sig")


