import numpy as np
import pandas as pd
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler

from optimal_purchase import optimal_purchase

N_FEATURES = 10

df = pd.read_csv(r'data/train_dataframe.csv')
df.set_index('dt', inplace=True)

scaler = StandardScaler()
df_filtered = df.filter(['Цена на арматуру']).values
df_scaled = pd.DataFrame(scaler.fit_transform(df_filtered))

dataset = df_scaled.values
training_data_len = int(np.ceil(len(dataset) * 1.0))

train_data = dataset[0:int(training_data_len), :]
x_train = []

for i in range(10, len(train_data)):
    x_train.append(train_data[i - 10:i])

x_train = np.array(x_train)
x_train = np.nan_to_num(x_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * dataset.shape[1], 1))

model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(N_FEATURES, 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(32))
model.add(Dense(1))

# Загрузка весов в модель
model.load_weights(r'data/model_weights.h5')

predictions = []

input_data = x_train[-1]
prediction = []
for _ in range(28):
    # Выполнение предсказания
    prediction = list(model.predict(input_data))[0][0]
    input_data = np.concatenate((input_data[1:], [[prediction]]), axis=0)

    # Обратное масштабирование предсказания
    prediction = scaler.inverse_transform([[prediction]])
    predictions.append(int(prediction[0][0]))

# Вывод предсказаний
print(predictions)

test = pd.read_excel(r'data/test.xlsx')

test['Цена на арматуру'] = pd.Series(data=predictions)

bought, remain = optimal_purchase(prediction)

test['Закупка'] = pd.Series(data=bought)
test.to_csv('subm.csv', index=False)
