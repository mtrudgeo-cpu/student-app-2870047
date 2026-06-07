import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('data.csv', sep=';')
df.columns = [c.strip().replace('\t', '') for c in df.columns]

FEATURES = [
    'Course', 'Educational special needs', 'Debtor', 'Tuition fees up to date',
    'Gender', 'Scholarship holder', 'Age at enrollment', 'International',
    'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (approved)',
    'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (approved)',
]
# Note: dropped 'Nacionality' 
X = df[FEATURES]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

clf = RandomForestClassifier(
    n_estimators=300, max_depth=None, min_samples_leaf=2,
    class_weight='balanced', random_state=42, n_jobs=-1)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
print(classification_report(y_test, pred))
print('Confusion matrix (rows=true):')
print(pd.DataFrame(confusion_matrix(y_test, pred, labels=clf.classes_),
                   index=clf.classes_, columns=clf.classes_))

joblib.dump({'model': clf, 'features': FEATURES}, 'model.joblib')
print('\nSaved model.joblib with classes:', list(clf.classes_))
