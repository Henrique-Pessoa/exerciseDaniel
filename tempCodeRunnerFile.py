# import pandas as pd
# import numpy as np 
# from sklearn.linear_model import LinearRegression 
# import matplotlib.pyplot as plt 


# vazao = np.array([10,20,30,5,35,40]).reshape(-1,1)
# nivel = np.array([50,60,70,45,80,85]).reshape(-1,1)

# modelo = LinearRegression()

# modelo.fit(vazao,nivel)

# vazao_teste = np.array([15,25,33]).reshape(-1,1)

# nivel_previsto = modelo.predict(vazao_teste)


# for i in range(len(vazao_teste)):
#    print(f"Vazão {vazao_teste[i][0]} m3/min - Nivel previsto : Nivel previsto: {nivel_previsto[i]}")
   
# plt.scatter(vazao,nivel)
# plt.scatter(vazao_teste,nivel_previsto)
# plt.show()






# from sklearn.linear_model import LinearRegression 
# import matplotlib.pyplot as plt 
# import numpy as np  

# modelo = LinearRegression()


# q = np.array([100,200,300,400,500,600,700]).reshape(-1,1)
# t = np.array([30,35,40,45,60,100,150]).reshape(-1,1)

# modelo.fit(q,t)

# teste = np.array([522,749,845]).reshape(-1,1)

# previsto = modelo.predict(teste)

# plt.scatter(q,t, color = "blue")

# plt.plot(teste,previsto, color = "orange")

# plt.show()






#import matplotlib.pyplot as plt
#import numpy as np  
#from sklearn.linear_model import LinearRegression 
#
#
#a = np.array([50,100,120,300]).reshape(-1,1)
#valor = np.array([180.000,300.000,375.000,600.000])
#
#teste = np.array([522,749,845]).reshape(-1,1)
#
#modelo = LinearRegression()
#
#modelo.fit(a,valor)
#
#previsto = modelo.predict(teste)
#
#plt.scatter(a,valor, color = "blue")
#plt.plot(teste,previsto, color = "orange")
#plt.show()




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









