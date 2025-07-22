from sklearn.preprocessing import LabelEncoder
import joblib

# Sample training categories
encoderlabel = LabelEncoder()
X['category'] = encoderlabel.fit_transform(X['category'])

# Save it
joblib.dump(encoderlabel, "label_encoder.pkl")