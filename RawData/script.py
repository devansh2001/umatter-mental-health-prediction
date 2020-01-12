import pandas as pd

df = pd.read_csv('train.csv', names=['sentiment', 'id', 'date', 'query', 'user', 'data'], sep =',')

print(df)
print('Completed reading...')

df.to_csv(r'training_data.csv', columns=['sentiment', 'data'], header = False, sep =',')
print('Completed writing...')

df = pd.read_csv('training_data.csv', names=['sentiment', 'data'], sep=',')

# df_temp = pd.DataFrame()
# for index, row in df.iterrows():
#     if row['sentiment'] == 0:
#         df_temp = df[index: index + (size/3)]
print('Completed reading for test...')
# num_zeroes = 0
# num_twos = 0
# num_fours = 0
# num_errors = 0
# count = 0
# for index, row in df.iterrows():
#     if count % 10000 == 0:
#         print('Count: ' + str(count))
#         print('0s: ' + str(num_zeroes)) # 800,000
#         print('2s: ' + str(num_twos))
#         print('4s: ' + str(num_fours)) #
#         print('Errors: ' + str(num_errors))
#         print('Total: ' + str(num_zeroes + num_twos + num_fours + num_errors))
#         print('************')
#     if row['sentiment'] == 0:
#         num_zeroes += 1
#     elif row['sentiment'] == 2:
#         num_twos += 1
#     elif row['sentiment'] == 4:
#         num_fours += 1
#     else:
#         print(row['sentiment'])
#         num_errors += 1


#     count = count + 1

# print(num_zeroes)
# print(num_twos)
# print(num_fours)
# print(num_errors)

df_negatives = df.iloc[0: 120000, :]
df_positives = df.iloc[800001:920001, :]
print(df_positives)
print(df_negatives)
training_df = df_negatives.append(df_positives)
# print(df[df['data'].str.contains("MySQL")==True])

print(training_df)
print(len(training_df))

training_df.to_csv(r'training_data_final.csv', columns=['sentiment', 'data'], header = False, sep =',')
print('Completed Writing! :)')
