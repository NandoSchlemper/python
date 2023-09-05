import numpy as np
from scipy import stats as st

numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
extreme_numbers = [999, 1,5,6, -430]

# Media Aritmetica #
print(np.mean(numbers)) # <-- Average numbers --> Media aritmetca
print(np.mean(extreme_numbers), "\n") # <-- Average extreme numbers --> Media aritmetca

# Mediana #
print(np.median(numbers)) # <-- Median numbers --> Mediana
print(np.median(extreme_numbers), "\n") # <-- Median extreme numbers --> Mediana

# Moda #
print(st.mode(numbers), "\n") # <-- Mode numbers --> Moda

# Desvio Padrao #
# Quantifica o quanto os valores devem se dispersar da media!
# Eh a variancia ao quadrado.
print(np.std(numbers)) # <-- Standard deviation numbers --> Desvio padrao
print(np.std(extreme_numbers), "\n") # <-- Standard deviation --> Desvio padrao

# Variancia #
# Quantifica o quanto os valores se dispersam da media, indicando valores altos e baixos!
# Quanto maior o valor, maior a variancia. Quanto menor o valor, menor a variancia.
print(np.var(numbers)) # <-- Variance numbers --> Variancia
print(np.var(extreme_numbers), "\n") # <-- Variance --> Variancia