import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 200)

y = (1/x) * np.sin(5*x)

plt.plot(x, y, label='1/x * sin(5*x)', color='green', linewidth=3, linestyle='-')

plt.title('Графік функції Y(x) = 1/x * sin(5*x)', fontsize=15) # Назва графіка
plt.xlabel('x', fontsize=12, color='blue') # Позначення вісі абсцис
plt.ylabel('Y(x)', fontsize=12, color='blue') # Позначення вісі ординат

plt.legend()
plt.grid(True)

plt.show()