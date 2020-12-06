import pandas as pd 
import matplotlib.pyplot as plt

dataset_path = "datasets/hellodata.csv"

df = pd.read_csv(dataset_path)

df_list = df.values.tolist()

x_values = [i for i in range(10,91)]

for eachrow in df_list[:10]:
    y_values = eachrow[10:91]
    plt.plot(x_values,y_values)

plt.show()