import tensorflow as tf
import pandas as pd
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import layers
import re

base_file_path = './'
test_file = 'test.csv'
train_file = 'training_data.csv'

def check_utf8(input_string):
    input_list = [input_string]
    regexp = re.compile(r'[^\u0020-\u00FF]')
    good_strs = list(filter(lambda s: not regexp.search(s), input_list))
    if (len(good_strs) == 0):
        print('Ignoring: ' + input_string)
        return False
    else:
        return True
    # return good_strs

def generate_obj(input_string):
    try:
        # print('Splitting: ' + input_string)
        split = input_string.split(",")
        # print('Success')
        # return {label, data}
        return split
    except Exception:
        # print(traceback.format_exc())
        return None

# generate_obj('4,"@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right."')

def create_dataframe(input_file_path):
    num_invalid = 0
    num_valid = 0
    label_0_count = 0
    label_2_count = 0
    label_4_count = 0
    count = 0
    df = pd.DataFrame(columns=['sentiment', 'text'])
    with open(base_file_path + input_file_path, "r") as file:
        line = file.readline()
        # print(line)
        while line:
            count = count + 1
            try:
                line = file.readline()
                line = line.strip('\n')
                # print(line) if check_utf8(line) and generate_obj(line) else print('N')
                # print(line)
                if (check_utf8(line) == True):
                    # print('UTF')
                    split = generate_obj(line)
                    # print(split)
                    if (split != None):
                        # print('Split okay')
                        try:
                            # df[count] = split
                            # print('Split 0')
                            # print(split[0])
                            # print('Split 1')
                            # print(split[1])

                            data = {'sentiment': split[0], 'text': split[1]}
                            if data['sentiment'] == '0':
                                label_0_count = label_0_count + 1
                            elif data['sentiment'] == '2':
                                label_2_count = label_2_count + 1
                            elif data['sentiment'] == '4':
                                label_4_count = label_4_count + 1
                            else:
                                print(data)
                            temp_df = pd.DataFrame(data, index=[num_valid])
                            num_valid = num_valid + 1
                            # print(temp_df)
                            df = df.append(temp_df)
                            # num_valid = num_valid + 1
                            # print('Done')
                            # print(df[count])
                            if (count % 10000 == 0):
                                print('Total: ' + str(count))
                                print('Valid: ' + str(num_valid))
                                print('Invalid: ' + str(num_invalid))
                                print('0 Label: ' + str(label_0_count))
                                print('2 Label: ' + str(label_2_count))
                                print('4 Label: ' + str(label_4_count))
                                print('*****')
                        except Exception:
                            # print(sys.info())
                            num_invalid = num_invalid + 1
                            pass
                    else:
                        num_invalid = num_invalid + 1
                else:
                    num_invalid = num_invalid + 1
            # print(line)
            except Exception:
                # traceback.print_exc()
                num_invalid = num_invalid + 1
    return df


print('-----DF----')
df = create_dataframe(test_file)
print(len(df))
print('Final frame:')
print(df)
print('-----DF----')


# df = pd.read_csv(base_file_path + train_file, names=['sentiment', 'data'], sep = ',')
# print(df)


tweets = df['text'].values
labels = df['sentiment'].values
print(labels)

tweets_train, tweets_test, y_train, y_test = train_test_split(tweets, labels, test_size=0.99, random_state=1000)
print(y_train)

print(y_test)
print(len(tweets))
print(len(tweets_train))
print(len(tweets_test))

unique_elements = set()
count = 0
max_tweet_length = 0
# print(df)

for i in range(0, len(df['text'])):
    if (i + 1) % 10000 == 0:
        print('Completed: ' + str(i + 1) + ' of ' + str(len(df['text'])))
    for j in range(0, len(df['text'][i])):
        tweet = df['text'][i]
        max_tweet_length = max(max_tweet_length, len(tweet))
        tweet_tokens = tweet.split()
        count = count + 1
        for k in range(0, len(tweet_tokens)):
            unique_elements.add(tweet_tokens[k])

print(len(unique_elements))
# print(unique_elements)
print(count)

vocab_size = len(unique_elements) + 1
tokenizer = Tokenizer(num_words = vocab_size)
tokenizer.fit_on_texts(tweets_train)

X_train = tokenizer.texts_to_sequences(tweets_train)
X_test = tokenizer.texts_to_sequences(tweets_test)
print(X_test[0])
print(X_train[0])
maxlen = 100
X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)
print(X_test[0])
print(X_train[0])

embedding_dim = 50

model = Sequential()
model.add(layers.Embedding(input_dim=vocab_size,
                           output_dim=embedding_dim,
                           input_length=maxlen))
model.add(layers.Flatten())
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()

print(X_train)
history = model.fit(X_train, y_train,
                    epochs=3,
                    verbose=True,
                    validation_data=(X_test, y_test),
                    batch_size=50)
loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
# loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
# print("Testing Accuracy:  {:.4f}".format(accuracy))
