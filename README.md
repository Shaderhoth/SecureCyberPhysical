# How to run
## [Merged project](https://colab.research.google.com/drive/1TQPJmmdM1IYApCIjUJv7zqW6BrLE1Xw8?usp=sharing)
#### This contains both of the models together
https://colab.research.google.com/drive/1TQPJmmdM1IYApCIjUJv7zqW6BrLE1Xw8?usp=sharing
### Step 1: Upload files
All the models and data sets are available in this repository \
The file structure should look like this
```bash
|-- TrainingDataBinary.csv
|-- TrainingDataMulti.csv
|-- TestingDataBinary.csv
|-- TestingDataMulti.csv
|-- models
    |-- part_1
    |    |-- model_0.keras
    |    |-- model_1.keras
    |    |-- ...
    |    |-- model_9.keras
    |-- part_2
         |-- model_0.keras
         |-- model_1.keras
         |-- ...
         |-- model_21.keras
```
### Step 2: Run all
From the Runtime tab select run all (Ctrl + F9) \
The second code block will ask you for which part you want to run \
select 0 for Binary (Part 1) \
Select 1 for Multi (Part 2) \
(You can run the project twice for both parts) \
Ensure Generation = False (Its set to this by default, this will stop the model generation scripts from running, so it only functions to load the models) \
If you want to test out the scripts for generating models you can set Generation = True in the second code block, just be aware that the model evolution will run until manually stopped, and you will then need to run the program from the next code block to take the best models and retrain them on the full data set before saving 



## [Part 1](https://colab.research.google.com/drive/1yWPvQNLIHvBGU2H1twU99vHlXHyQ4qoy?usp=sharing)
#### This contains the code to run part 1 (the Binary Classification)
https://colab.research.google.com/drive/1yWPvQNLIHvBGU2H1twU99vHlXHyQ4qoy?usp=sharing
### Step 1: Upload files
All the models and data sets are available in this repository
The file structure should look like this
```bash
|-- TrainingDataBinary.csv
|-- TestingDataBinary.csv
|-- model_0.keras
|-- model_1.keras
|-- ...
|-- model_9.keras
```
### Step 2: Run all
From the Runtime tab select run all (Ctrl + F9) \
Ensure Generation = False (Its set to this by default, this will stop the model generation scripts from running, so it only functions to load the models) \
If you want to test out the scripts for generating models you can set Generation = True in the second code block, just be aware that the model evolution will run until manually stopped, and you will then need to run the program from the next code block to take the best models and retrain them on the full data set before saving



## [Part 2](https://colab.research.google.com/drive/1qnW5RpoxxJnOlNlqsaG08w1J8ttIZhjr?usp=sharing)
#### This contains the code to run part 2 (the Multi Category Classification)
https://colab.research.google.com/drive/1qnW5RpoxxJnOlNlqsaG08w1J8ttIZhjr?usp=sharing
### Step 1: Upload files
All the models and data sets are available in this repository
The file structure should look like this
```bash
|-- TrainingDataMulti.csv
|-- TestingDataMulti.csv
|-- model_0.keras
|-- model_1.keras
|-- ...
|-- model_21.keras
```
### Step 2: Run all
From the Runtime tab select run all (Ctrl + F9) \
Ensure Generation = False (Its set to this by default, this will stop the model generation scripts from running, so it only functions to load the models) \
If you want to test out the scripts for generating models you can set Generation = True in the second code block, just be aware that the model evolution will run until manually stopped, and you will then need to run the program from the next code block to take the best models and retrain them on the full data set before saving



## [Github version](https://github.com/Shaderhoth/SecureCyberPhysical)
#### This is This is done automatically using github actions
### Step 1:
Simply locate the artifact produced by the most recent github action \
https://github.com/Shaderhoth/SecureCyberPhysical/actions \
(at the time of writing this, that's here: https://github.com/Shaderhoth/SecureCyberPhysical/actions/runs/8933212879/artifacts/1469278199) \
I have also published them here: https://github.com/Shaderhoth/SecureCyberPhysical/releases/tag/Results
