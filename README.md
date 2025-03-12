# EDA-1Team - TNT 

## 팀원 소개 
| 김장수 | 이채은 | 황준호|
| --- | --- | --- |
| 사진 | 넣을 | 까요? |

# 프로젝트 주제 : ⚾️KBO 외야수 골든글러브 수상 예측 프로젝트 (K-NN 알고리즘)

# 📅 개발 기간
2025.03.10 ~ 2025.03.14 (총 4일)

##  🎯 프로젝트 목표

- **목적**: 2000 ~ 2024년 KBO 외야수 중 **연도별 골든글러브 수상 후보** 의 기록 데이터를 바탕으로 **‘골든글러브 수상 예측(0 OR 1)’**
- **접근 방식**: **K-NN 알고리즘(최근접 이웃)** 을 이용한 수상 예측
- **타겟 변수**: `골든글러브 수상여부 (수상 x:0 , 수상o:1)`

## 1.데이터 구성 

### 🔹 `kbo_outfielders_20years.csv` (400명)

|이름|연도|WAR|득점|안타|2루타|3루타|홈런|타점|도루|볼넷|사구|고의사구|삼진|병살|희생타|희생플라이|타율|출루|장타|OPS|wRC+|수상여부|
| --- | --- | --- | ---| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---|
|심정수 | 2000 | 4.73 | 75 | 138 | 21| 2 | 29 | 91| 5| 69 | 10 |1 | 67 | 12 | 0 | 9 | 0.304 | 0.4 | 0.551 | 0.951 | 147.8 |0 |


### 🔹 `league_avg_stats.csv` (20년치)

| 연도 | 리그_평균_타율 | 리그_평균_OPS | 리그_환경 |
| --- | --- | --- | --- |
| 2010 | 0.267 | 0.740 | 타고투저 |

## 🧹 EDA

### 1. 데이터 로드

- 결측치 확인 및 처리
- `골든글러브` → float(0.0 또는 1.0) 로 변환 (회귀용)

### 2. 데이터 구조 및 기초 통계 확인

### 3. 결측치 및 이상치 탐색

### 4. 데이터 시각화를 통한 탐색

### 5. 데이터 정제 및 전처리
- 수상 예측에 유의미하다고 판단되는 feature 추출
- 표준화 : 연도마다 변하는 수상 기준과 연도별 데이터의 특징 변화(ex. 제도 변경으로 인한 경기 내용 변화)를 반영하기 위함
  
### 6. 데이터 분할 및 학습

### 7. 예측 및 결과 평가

