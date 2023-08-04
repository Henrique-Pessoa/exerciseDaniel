import matplotlib.pyplot as plt
import numpy as np  
from sklearn.linear_model import LinearRegression 


a = np.array([50,100,120,300]).reshape(-1,1)
valor = np.array([180.000,300.000,375.000,600.000])

teste = np.array([522,749,845]).reshape(-1,1)

modelo = LinearRegression()

modelo.fit(a,valor)

previsto = modelo.predict(teste)

plt.scatter(a,valor, color = "blue")
plt.plot(teste,previsto, color = "orange")
plt.show()