from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# 1. Sample Data
data = [
    ("I love this product!", "positive"),
    ("This is a terrible movie.", "negative"),
    ("It's okay, not great.", "neutral"),
    ("Highly recommend!", "positive"),
    ("Waste of money.", "negative"),
]
texts = [item[0] for item in data]
labels = [item[1] for item in data]

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 3. Build and Train Model (TF-IDF Vectorizer + Naive Bayes Classifier)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# 4. Evaluate Model
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# 5. Make Predictions
new_text = "This is a fantastic experience."
prediction = model.predict([new_text])
print(f"Sentiment of '{new_text}': {prediction[0]}")

