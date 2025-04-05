import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 60, 10
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'k-', label=f'N(μ={mu}, σ={sigma})')
plt.fill_between(x, y, where=(x < 83), color='skyblue', alpha=0.5, label='P(X < 83) ≈ 98.93%')
plt.title('Distribución Normal: $P(X < 83)$')
plt.xlabel('Valores de X')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()