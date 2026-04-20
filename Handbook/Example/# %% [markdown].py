# %% [markdown]
# ### Example 1-1. Training and running a linear model using Scikit-Learn

# %%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# %%

data_root = "https://github.com/ageron/data/raw/main/"    # github repo main file path for easy access
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")  # in that github repo main file, we use csv file

# %%
lifesat.head()   #getting idea , whats in the csv

# %%
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# %%
# Visualize Data
lifesat.plot(kind ='scatter', grid = True,
            x = "GDP per capita (USD)", y = "Life satisfaction")
plt.axis([23_500,62_500,4,9])
plt.show()

# %% [markdown]
# ## Linear Regression

# %%
model =  LinearRegression()

# %%
model.fit(X,y)

# %%
X_new = [[37_655.2]]
print(model.predict(X_new))

# %%
# Generate line points
X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model.predict(X_line)

# Plot scatter
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")

# Plot best-fit line
plt.plot(X_line, y_line, color='red', linewidth=2)

plt.axis([23_500, 62_500, 4, 9])
plt.show()

# %% [markdown]
# ## KNN

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

# Load data
data_root1 = "https://github.com/ageron/data/raw/main/"
lifesat1 = pd.read_csv(data_root + "lifesat/lifesat.csv")

X1 = lifesat[["GDP per capita (USD)"]].values
y1 = lifesat[["Life satisfaction"]].values

# Scatter plot
lifesat1.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")

# Create KNN model
model1 = KNeighborsRegressor(n_neighbors=3)

# Train
model1.fit(X, y)

# Prediction for Cyprus
X_new1 = [[37655.2]]
print(model1.predict(X_new1))

# %%
model1 = KNeighborsRegressor(n_neighbors=3)

# %%
model1.fit(X1,y1)

# %%
X_new1 = [[37_655.2]]
print(model1.predict(X_new1))

# %%
# Create smooth X values
X_range = np.linspace(X1.min(), X1.max(), 50


).reshape(-1, 1)
y_pred = model.predict(X_range)

# Plot
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")

plt.plot(X_range, y_pred, color='red', linewidth=2)

plt.axis([23_500, 62_500, 4, 9])
plt.show()


