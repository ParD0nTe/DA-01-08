import pandas as pd
import numpy as np
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [10, 20, 30, 40, 50]
})
print("Исходные данные")
print(df)

# Сумма
df['sum'] = df['feature1'] + df['feature2']

# Разность
df['diff'] = df['feature2'] - df['feature1']

# Произведение
df['product'] = df['feature1'] * df['feature2']

print("Итоговые значения")
print(df)