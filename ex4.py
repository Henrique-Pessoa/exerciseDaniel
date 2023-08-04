import matplotlib.pyplot as plt
import numpy as np  
from sklearn.linear_model import LinearRegression 


renda = np.array([1200,5000,8000,10000,30000]).reshape(-1,1)
gastos = np.array([750,1500,4000,6000,18000])

teste = np.array([10000,20000,30000,40000,50000]).reshape(-1,1)

modelo = LinearRegression()

modelo.fit(renda,gastos)

previsto = modelo.predict(teste)

plt.scatter(renda,gastos, color = "blue")
plt.plot(teste,previsto, color = "orange")
plt.show()