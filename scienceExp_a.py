import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()

plt.rc('font', family=font_name)

m = 700 # 청새치의 무게(kg)
v = 22.222222 # 청새치의 평균 속도 80km/h를 m/s로 변환
t = np.linspace(1, 150, 150) # 0에서 80km/h까지 도달하는 데 걸리는 시간

def marlinForce(t):
    return m * (v/t)

def oldmanForce(t):
    return 0*t + 120

n = marlinForce(t)
y = oldmanForce(t)

difference = n - y
index = np.argmin(np.abs(difference))
a = round(t[index])
b = round(n[index], 2)

plt.figure(figsize=(6, 4))
plt.scatter(a, b, color='red', label=f'Intersection ({a}, {b})')
plt.plot(t, n, label='노인이 견뎌야 하는 청새치의 힘(N)')
plt.plot(t, y, ls='--')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('노인이 견뎌야 하는 청새치의 힘')
plt.xlabel('청새치가 최고 속력까지 도달하는 시간(s)')
plt.legend()
plt.grid()
plt.show()