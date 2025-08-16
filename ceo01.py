import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

path = "/home/malvavisco/Documentos/proyectos/TripleTen_bootcamp/datasets/"
path_1=path+ "instacart_orders.csv"
path_2=path+ "products.csv"
path_3=path+ "aisles.csv"
path_4=path+ "order_products.csv"
path_5=path+ "departments.csv"

instacart = pd.read_csv(path_1, sep=";")
print(instacart.head())