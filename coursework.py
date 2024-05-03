# %% [markdown]
# ## Set up environment

# %%
import numpy as np
import pandas as pd
import tensorflow as tf
import random
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# %% [markdown]
# ## Decide which part to work on
# - 0: Part A (Binary data set)
# - 1: Part B (Multi data set)

# %%
while (part := input("Do you want to work on 0: binary or 1: multi-class classification? ")) not in ["0", "1"]:
    print("Invalid input, enter 0 or 1")

part = bool(int(part))
print("Part B" if part else "Part A")

Generation = False # Set to True to generate new models

# %% [markdown]
# ## Prepare the initial training data

# %%

if part:
    train_df = pd.read_csv("TrainingDataMulti.csv")
    test_df = pd.read_csv("TestingDataMulti.csv")
else:
    train_df = pd.read_csv("TrainingDataBinary.csv")
    test_df = pd.read_csv("TestingDataBinary.csv")


scaler = StandardScaler()
x_train, y_train = train_df.iloc[:, :-1].values, train_df.iloc[:, -1].values
X_train_scaled = scaler.fit_transform(x_train)

x_train, x_test, y_train, y_test = train_test_split(train_df.iloc[:, :-1].values, train_df.iloc[:, -1].values, test_size=0.15,shuffle=True)
if part:
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

X_train_scaled = scaler.transform(x_train)
X_test_scaled = scaler.transform(x_test)
print(scaler.mean_)
print(scaler.scale_ )

# %% [markdown]
# ## Set up the models
# This is a template class to create random models, and merge/evolve them to get new (hopefully improved) models

# %%


class RandomModel:
    def __init__(self):
        self.model = Sequential()
        self.layer_details = []
        self.optimizer = None
        self.loss_function = None
        self.create_random_model()

    def create_random_model(self):
        layers = random.randint(1, 6) 
        self.model.add(Input(shape=(X_train_scaled.shape[1],)))

        for i in range(layers):
            units = random.choice([8, 16, 32, 64, 128, 256, 512])
            activation = random.choice(["relu", "sigmoid", "tanh"])
            if i == 0:
                self.model.add(Dense(units, activation=activation))
            else:
                self.model.add(Dense(units, activation=activation))
            self.layer_details.append((units, activation))

            if random.random() > 0.7:
                dropout_rate = random.choice([0.2, 0.3, 0.5])
                self.model.add(Dropout(dropout_rate))
                self.layer_details.append(("dropout", dropout_rate))

        if part:
            self.model.add(Dense(3, activation='softmax'))
        else:
            self.model.add(Dense(1, activation='sigmoid'))  
        self.compile_model()

    def compile_model(self):
        self.optimizer = random.choice(["adam", "rmsprop", "sgd"])
        self.loss_function = random.choice([
            'binary_crossentropy',
            'mean_squared_error',
            'mean_absolute_error',
            'categorical_crossentropy'
        ])
        self.model.compile(optimizer=self.optimizer, loss=self.loss_function, metrics=['accuracy'])
        
        if part:
            self.model.fit(X_train_scaled, y_train, batch_size=16, epochs=30, verbose=0)
        else:
            self.model.fit(X_train_scaled, y_train, batch_size=32, epochs=20, verbose=0)
        self.loss, self.accuracy = self.model.evaluate(X_test_scaled, y_test, verbose=0)




def evolve(models):
    top_performers = models[:2]  

    new_models = []
    for _ in range(8):  
        new_model = Sequential()
        new_model.add(Input(shape=(X_train_scaled.shape[1],)))
        max_layers = max(len(top_performers[0].layer_details), len(top_performers[1].layer_details))

        new_layers = []
        for i in range(max_layers):
            chosen_parent = random.choice([top_performers[0], top_performers[1]])
            if i < len(chosen_parent.layer_details):
                layer = chosen_parent.layer_details[i]
                new_layers.append(layer)
                if layer[0] == "dropout":
                    new_model.add(Dropout(layer[1]))
                else:
                    new_model.add(Dense(layer[0], activation=layer[1]))

        if part:
            new_model.add(Dense(3, activation='softmax'))
        else:
            new_model.add(Dense(1, activation='sigmoid'))  

        chosen_optimizer = random.choice([top_performers[0].optimizer, top_performers[1].optimizer])
        chosen_loss_function = random.choice([top_performers[0].loss_function, top_performers[1].loss_function])

        random_model = RandomModel()
        random_model.model = new_model
        random_model.layer_details = new_layers
        random_model.optimizer = chosen_optimizer
        random_model.loss_function = chosen_loss_function
        random_model.compile_model() 
        new_models.append(random_model)

    return new_models






# %% [markdown]
# ## Evolutionarily find best algorithm
# ### (Skip this)
# Don't run this (you can, but it'll just go on for ever) \
# this was simply to help me find the best models to use

# %%
if Generation:
  final_AIs = []
  AIs = [RandomModel() for _ in range(10)]
  counter = 0
  while True:
    AIs.sort(key=lambda AI: AI.accuracy, reverse=True)
    print(f"\033[2;36mRound {(counter := counter + 1)}")
    [print(f"{"\033[1;34m" if AIs[i].accuracy > 0.95 else 
              "\033[1;32m" if AIs[i].accuracy > 0.9 else
              "\033[1;33m" if AIs[i].accuracy < 0.6 else
              "\033[1;31m" if AIs[i].accuracy < 0.5 else
              "\033[1;37m"
              }{i}: [{AIs[i].accuracy}, {AIs[i].layer_details}, ['{AIs[i].optimizer}','{AIs[i].loss_function}']]") for i in range(len(AIs))]
    newAIs = AIs[:2]
    newAIs += evolve(AIs)
    for i in range(6):
      newAIs.append(RandomModel())
    for AI in AIs[2:]:
      if AI.accuracy > 0.95:
        final_AIs.append((AI.model,AI.accuracy))
      elif AI.accuracy > 0.9 and part:
        final_AIs.append((AI.model,AI.accuracy))
    AIs = newAIs


# %%

if Generation:
    print("\033[0;37mFinal Models")
    print("============")
    [print(f"{AI.accuracy}") for (AI.model,AI.accuracy) in final_AIs]
    for AI in AIs:
        print(AI.model.input_shape)

# %% [markdown]
# # Accumulate the best models into the final_AIs array

# %%
if Generation:
  for AI in AIs:
      if AI.accuracy > 0.95:
        final_AIs.append((AI.model,AI.accuracy))
      elif AI.accuracy > 0.9 and part:
        final_AIs.append((AI.model,AI.accuracy))
  final_AIs.sort(key=lambda AI: AI[1], reverse=True)
  final_AIs = final_AIs[:20]
  print("\033[0;37mFinal Models")
  print("============")
  [print(f"{AI.accuracy}") for (AI.model,AI.accuracy) in final_AIs]


# %% [markdown]
# ## Set up the training and test data for the final models

# %%
x_train, y_train = train_df.iloc[:, :-1].values, train_df.iloc[:, -1].values
x_train_scaled = scaler.transform(x_train)
if part:
    y_train = to_categorical(y_train)

# %% [markdown]
# # Fit the best AIs with the full training set

# %%
if Generation:
    final_models = [AI[0] for AI in final_AIs]
    for model in final_models:
        model.summary()
        print(model.input_shape)
        model.fit(x_train_scaled, y_train, batch_size=16, epochs=200, verbose=1)

# %% [markdown]
# # Save the models

# %%
if Generation:
    directory = f"models/part_{int(part)+1}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, model in enumerate(final_models, start=len([f for f in os.listdir(directory) if f.endswith('.keras')])):
        model.save(f'{directory}/model_{i}.keras')

# %% [markdown]
# # Load models

# %%
loaded_models = []
directory = f"models/part_{int(part)+1}"
x_test = test_df.values
x_test_scaled = scaler.transform(x_test)

if os.path.exists(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".keras"):
            file_path = os.path.join(directory, filename)
            model = tf.keras.models.load_model(file_path)
            loaded_models.append(model)
else:
    print(f"The directory {directory} does not exist.")

print(f"{len(loaded_models)} models loaded")

# %% [markdown]
# # Retrain models (for testing)

# %%
if Generation:
    x_train, y_train = train_df.iloc[:, :-1].values, train_df.iloc[:, -1].values
    x_train_scaled = scaler.transform(x_train)
    if part:
        y_train = to_categorical(y_train)
    for i, model in enumerate(loaded_models):
        model.fit(x_train_scaled, y_train, batch_size=16, epochs=200, verbose=0)
        print(f"Model {i} trained")
        
    directory = f"models/part_{int(part)+1}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i, model in enumerate(loaded_models):
        model.save(f'{directory}/model_{i}.keras')

# %% [markdown]
# # Use the models to make predictions
# This will also generate a confidence score by averaging out all of the final responses to figure out how certain the model is of its results

# %%
predictions = []
scores = []
if part:
    for model in loaded_models:
        test_scores = model.predict(x_test_scaled)
        scores.append(test_scores)
        prediction = np.argmax(test_scores, axis=1)
        predictions.append(prediction)
    predictions_stack = np.vstack(predictions).T
    final_predictions = np.apply_along_axis(lambda x: np.bincount(x, minlength=np.max(x)+1).argmax(), axis=1, arr=predictions_stack)
    for i in range(len(final_predictions)):
        score = sum([j[i][final_predictions[i]] for j in scores])/len(loaded_models)
        colour = "\033[1;36m" if score > 0.9 else "\033[1;32m" if score > 0.8 else "\033[1;33m" if score > 0.7 else "\033[38;5;214m" if score > 0.6 else "\033[1;31m"
        print(f"\033[1;37m{i}: {colour if final_predictions[i] == 0 else '\033[1;37m'}{sum([j[i][0] for j in scores])/len(loaded_models)} {colour if final_predictions[i] == 1 else '\033[1;37m'}{sum([j[i][1] for j in scores])/len(loaded_models)} {colour if final_predictions[i] == 2 else '\033[1;37m'}{sum([j[i][2] for j in scores])/len(loaded_models)}")
    
    
    test_df['marker'] = final_predictions.astype(float)
    test_df.to_csv('TestingResultsMulti.csv', index=False)
    print("Model training complete and predictions saved.")
    print(f"Confidence: {sum([sum([j[i][final_predictions[i]] for j in scores])/len(loaded_models) for i in range(len(final_predictions))])/len(final_predictions) }")
else:
    for model in loaded_models:
        prediction = ((test:=model.predict(x_test_scaled)) > 0.5).astype(int)
        predictions.append(prediction)
        scores.append(test)
    predictions_stack = np.hstack(predictions)
    final_predictions = np.apply_along_axis(lambda x: np.bincount(x, minlength=2).argmax(), axis=1, arr=predictions_stack)
    for i in range(len(scores[0])):
        score = sum([scores[j][i] for j in range(len(scores))])/len(scores)
        print(f"{"\033[1;36m" if score > 0.9 else 
                "\033[1;32m" if score > 0.8 else
                "\033[1;33m" if score > 0.7 else
                "\033[38;5;214m" if score > 0.6 else
                "\033[1;36m" if score < 0.1 else
                "\033[1;32m" if score < 0.2 else
                "\033[1;33m" if score < 0.3 else
                "\033[38;5;214m" if score < 0.4 else
                "\033[1;31m"}{final_predictions[i]}: {score}", end=" | ")
        if i % 5 == 4:
            print()
        
    test_df['marker'] = final_predictions.astype(float)
    test_df.to_csv('TestingResultsBinary.csv', index=False)
    print("Model training complete and predictions saved.")
    print(f"Confidence: {sum([sum([abs((j-0.5)*2) for j in i]) for i in scores])/sum([sum([1 for j in i]) for i in scores])}")


# %% [markdown]
# # Figuring out console colour codes :P

# %%
print("\\033[38;5;{i}m")
for i in range(16):
    print(f"\033[38;5;{i}m| {i:<3} ".format(), end="")
print()
for i in range (7):
    for j in range(36):
        print(f"\033[38;5;{(a := i*36+j+16)}m| {a:<3} ".format(), end="")
    print()
print("\\033[48;5;{i}m")
for i in range(16):
    print(f"\033[48;5;{i}m| {i:<3} ".format(), end="")
print()
for i in range (7):
    for j in range(36):
        print(f"\033[48;5;{(a := i*36+j+16)}m| {a:<3} ".format(), end="")
    print()

for i in range(120):
    string = "\\033[{i};"+f"{i:<3}"+"m: "
    for j in range(64):
        string += (f"\033[{j};{i}m{j}  ")
    print(string)


