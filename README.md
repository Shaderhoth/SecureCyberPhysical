## How to Run

### [Merged Project (Part 1 & Part 2 Combined)](https://colab.research.google.com/drive/1TQPJmmdM1IYApCIjUJv7zqW6BrLE1Xw8?usp=sharing)
1. **Run All:** From the *Runtime* tab, choose *Run all* (or press `Ctrl + F9`).
2. **Select Mode:** In the second code block:
   - Enter `0` for Binary Classification (Part 1).
   - Enter `1` for Multi-Category Classification (Part 2).
3. **Model Generation:**
   - Keep `Generation = False` to load models.
   - Set `Generation = True` if you wish to generate new models.
      - You will need to stop the evolution loop manually when you're satisfied with the models
      - Then continue the program from the next code block to retrain and save the models

### [Part 1 (Binary Classification Only)](https://colab.research.google.com/drive/1yWPvQNLIHvBGU2H1twU99vHlXHyQ4qoy?usp=sharing)
1. **File Structure:** Ensure files are uploaded as follows:
   ```bash
   ├── TrainingDataBinary.csv
   ├── TestingDataBinary.csv
   ├── model_0.keras
   ├── model_1.keras
   ├── ...
   └── model_9.keras
   ```
2. **Run All:** From the *Runtime* tab, choose *Run all* (`Ctrl + F9`).
3. **Model Generation:**
   - Keep `Generation = False` to load models.
   - Set `Generation = True` if you wish to generate new models.
      - You will need to stop the evolution loop manually when you're satisfied with the models
      - Then continue the program from the next code block to retrain and save the models

### [Part 2 (Multi-Category Classification Only)](https://colab.research.google.com/drive/1qnW5RpoxxJnOlNlqsaG08w1J8ttIZhjr?usp=sharing)
1. **File Structure:** Ensure files are uploaded as follows:
```bash
├── TrainingDataMulti.csv
├── TestingDataMulti.csv
├── model_0.keras
├── model_1.keras
├── ...
└── model_21.keras
```
3. **Run All:** From the *Runtime* tab, choose *Run all* (`Ctrl + F9`).
4. **Model Generation:**
   - Keep `Generation = False` to load models.
   - Set `Generation = True` if you wish to generate new models.
      - You will need to stop the evolution loop manually when you're satisfied with the models
      - Then continue the program from the next code block to retrain and save the models

### [GitHub Version](https://github.com/Shaderhoth/SecureCyberPhysical)
1. **Locate Artifact:** Go to the [GitHub Actions page](https://github.com/Shaderhoth/SecureCyberPhysical/actions) for the latest build.
- Alternatively, visit the [Release Page](https://github.com/Shaderhoth/SecureCyberPhysical/releases/tag/Results).
