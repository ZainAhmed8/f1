import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# get our data
races = pd.read_csv('../data/races.csv')
pit_stops = pd.read_csv('../data/pit_stops.csv')
lap_times = pd.read_csv('../data/lap_times.csv')
drivers = pd.read_csv('../data/drivers.csv')
circuits = pd.read_csv('../data/circuits.csv')

# merge our data
data = pit_stops.merge(races, on='raceId')
data = data.merge(drivers, on='driverId')
data = data.merge(circuits, on='circuitId')

# feature engineering
data['pit_stop_interval'] = data['lap'] / data['stop']
data['driver_age'] = pd.to_datetime(data['date']).dt.year - pd.to_datetime(data['dob']).dt.year

# encode categorical vars
data = pd.get_dummies(data, columns=['country', 'constructorId'])

# define our features and target
features = data[['pit_stop_interval', 'driver_age', '...']]
target = data['number_of_pit_stops']

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# train our model (Random Forest, group of decision trees)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# do a prediction and eval if good
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
