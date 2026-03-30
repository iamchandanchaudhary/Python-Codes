from sklearn.impute import SimpleImputer
import numpy as np

data = [[1, 2], [np.nan, 3], [7, 6]]

imputer = SimpleImputer(strategy='mean')
data = imputer.fit_transform(data)

print(data)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
data = ['cat', 'dog', 'cat']
encoded = le.fit_transform(data)

print(encoded)

from sklearn.preprocessing import OneHotEncoder
import numpy as np

data = np.array([[0], [1], [2]])

encoder = OneHotEncoder()
encoded = encoder.fit_transform(data).toarray()

print(encoded)

from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4]]
y = [0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)
