import numpy as np
from statistics import mode

# Sequência númerica
dados = [10, 12, 10, 14, 15, 15, 20]

# Média -> tendência central
media = np.mean(dados)
print(f"Média: {media}")

# Mediana -> Valor central, robusto a outliers
mediana = np.median(dados)
print(f"Mediana: {mediana}")

# Moda -> Valor mais frequente
moda = mode(dados)
print(f"Moda: {moda}")

# Desvio Padrão -> Dispersão dos dados
desvio_padrao = np.std(dados)
print(f"Desvio Padrão: {desvio_padrao}")

# Variância = Quadrado do desvio padrão
variancia = np.var(dados)
print(f"Variância: {variancia}")
