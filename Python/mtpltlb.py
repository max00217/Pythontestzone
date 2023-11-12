import matplotlib.pyplot as plt
import numpy as np
    
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

regions = np.array(['경기', '서울', '경남', '부산', '대구', '인천', '충남', '전북', '전남', '대전', '충북', '강원', '광주', '울산', '제주', '경북'])
factory_counts = np.array([64.957, 11.741, 0.758, 10.959, 8.087, 11.411, 5.966, 6.172, 13.861, 2.626, 9.71, 7.732, 38.0913, 34.2092, 0.693, 18.243])
car_counts = np.array([30.71170, 23.94901, 9.69983, 8.51684, 7.00026, 6.69863, 5.54070, 4.76982, 4.40982, 4.38888, 4.18879, 4.15660, 3.80913, 3.42092, 1.60138, 0.56377])
pollution_levels = np.array([10, 9, 3, 7, 6, 7, 6, 5, 5, 5, 10, 9, 8, 3, 3, 10])

sorted_indices = np.argsort(pollution_levels)[::-1]
regions = regions[sorted_indices]
factory_counts = factory_counts[sorted_indices]
car_counts = car_counts[sorted_indices]
pollution_levels = pollution_levels[sorted_indices]

barWidth = 0.15 
r1 = np.arange(len(factory_counts))  
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2] 

plt.figure(figsize=(10,6))

bar1 = plt.bar(r1, factory_counts, color ='b', width = barWidth, edgecolor ='grey', alpha = 0.7, label='공장 등록 수 (천 개)')
bar2 = plt.bar(r2, pollution_levels, color ='r', width = barWidth, edgecolor ='grey', alpha = 0.7, label='초미세먼지 농도 (㎍/㎥)')
bar3 = plt.bar(r3, car_counts, color ='g', width = barWidth, edgecolor ='grey', alpha = 0.7, label='승용차 등록 대수 (십만 대)') 

plt.title('전국 지역별 공장 등록 수, 초미세먼지 농도, 승용차 대수')
plt.xlabel('지역', fontweight ='bold', fontsize = 15)
plt.ylabel('개수 및 농도', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(factory_counts))], regions, rotation=45)
plt.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height.is_integer():
            label_format = '%d'
        else:
            label_format = '%.3f'
        plt.text(rect.get_x() + rect.get_width() / 2, height, label_format % height, ha='center', va='bottom', fontsize=8)
        
autolabel(bar1)
autolabel(bar2)
autolabel(bar3)

plt.show()


