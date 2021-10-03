from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
from joblib import dump, load

def ml_model(criteria_arr):
    model = KNeighborsClassifier(n_neighbors= 3)
    input_h = 'training.csv'
    df = pd.read_csv(input_h, header=None)

    X = df.iloc[:, :-1].values
    y = df.iloc[: ,-1].values
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.33, random_state = 21)
    model.fit(X_train,y_train)

    y_pred = model.predict([criteria_arr])
    if y_pred == 1:
        return "<h1>The predicted score is greater than 50, which means that it is a safe address to interact with.</h1>"
    else:
        return "<h1>BEWARE! The predicted score is less than 50, which means that it is NOT a safe address to interact with and the algorithm has interecepted malicious transactions.</h1>"
