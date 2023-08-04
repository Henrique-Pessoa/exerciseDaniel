from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt 
import numpy as np  
modelo = LinearRegression()
q = np.array([100,200,300,400,500,600,700]).reshape(-1,1)
t = np.array([30,35,40,45,60,100,150]).reshape(-1,1)
modelo.fit(q,t)
teste = np.array([522,749,845]).reshape(-1,1)
previsto = modelo.predict(teste)
plt.scatter(q,t, color = "blue")
plt.plot(teste,previsto, color = "orange")
plt.show()