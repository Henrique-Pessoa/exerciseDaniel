import matplotlib.pyplot as plt
import numpy as np  
from sklearn.linear_model import LinearRegression 


consumo = np.array([50,140,30,75,123]).reshape(-1,1)
demanda = np.array([100,200,80,100,160])

teste = np.array([10000,20000,30000,40000,50000]).reshape(-1,1)

modelo = LinearRegression()

modelo.fit(consumo,demanda)

previsto = modelo.predict(teste)

plt.scatter(consumo,demanda, color = "blue")
plt.plot(teste,previsto, color = "orange")
plt.show()