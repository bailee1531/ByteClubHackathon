from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib


data_cleaned = pd.read_csv('Weather_Data_Encoded.csv')

x = data_cleaned.drop(['EVENT_TYPE', 'EVENT_TYPE_ENCODED', 'NAME', 'CALL_SIGN'], axis=1)
y = data_cleaned['EVENT_TYPE_ENCODED']

ros = RandomOverSampler(random_state=20)
x_resampled, y_resampled = ros.fit_resample(x, y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=20)

# Hyperparameters
param_grid = {
    'n_estimators': [100, 150],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced']
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=20), param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose = 2)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Evaluate the model
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Best Model Parameters: {grid_search.best_params_}")
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", class_report)


joblib.dump(best_model, 'weather_model.pkl')