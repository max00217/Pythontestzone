import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 데이터
regions = np.array(['경기', '서울', '경남', '부산', '대구', '인천', '충남', '전북', '전남', '대전', '충북', '강원', '광주', '울산', '제주', '경북'])
factory_counts = np.array([64.957, 11.741, 0.758, 10.959, 8.087, 11.411, 5.966, 6.172, 13.861, 2.626, 9.71, 7.732, 38.0913, 34.2092, 0.693, 18.243])
car_counts = np.array([307.1170, 239.4901, 96.9983, 85.1684, 70.0026, 66.9863, 55.4070, 47.6982, 44.0982, 43.8888, 41.8879, 41.5660, 38.0913, 34.2092, 16.0138, 5.6377])
pollution_levels = np.array([10, 9, 3, 7, 6, 7, 6, 5, 5, 5, 10, 9, 8, 3, 3, 10])

# 공장 등록 수와 초미세먼지 농도 사이의 피어슨 상관계수 계산
corr_factory_pollution, _ = pearsonr(factory_counts, pollution_levels)
print(f'공장 등록 수와 초미세먼지 농도의 피어슨 상관계수: {corr_factory_pollution:.3f}')

# 승용차 등록 수와 초미세먼지 농도 사이의 피어슨 상관계수 계산
corr_car_pollution, _ = pearsonr(car_counts, pollution_levels)
print(f'승용차 등록 대수와 초미세먼지 농도의 피어슨 상관계수: {corr_car_pollution:.3f}')

# 산점도 그리기
plt.figure(figsize=(20, 5))

plt.subplot(1, 3, 2)
plt.scatter(factory_counts, pollution_levels)
plt.title('공장 등록 수와 초미세먼지 농도')
plt.xlabel('공장 등록 수')
plt.ylabel('초미세먼지 농도')

plt.subplot(1, 3, 3)
plt.scatter(car_counts, pollution_levels)
plt.title('승용차 등록 대수와 초미세먼지 농도')
plt.xlabel('승용차 등록 대수')
plt.ylabel('초미세먼지 농도')

plt.tight_layout()
plt.show()