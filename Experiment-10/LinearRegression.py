import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data: [size (sq ft), bedrooms, age (years)]
features = [
    [800, 2, 15],
    [1000, 2, 10],
    [1200, 3, 8],
    [1500, 3, 12],
    [1800, 3, 5],
    [2000, 4, 3],
    [2200, 3, 10],
    [2500, 4, 2],
    [2800, 4, 6],
    [3000, 5, 1],
]
prices = [44, 60, 83, 90, 118, 136, 130, 165, 172, 200]  # in lakhs

# Train the model
model = LinearRegression()
model.fit(features, prices)

# New house to predict
new_size, new_bedrooms, new_age = 1600, 3, 7
predicted = model.predict([[new_size, new_bedrooms, new_age]])[0]
print(f"Predicted price: {predicted:.1f} lakhs")

budget = 100  # your budget line (in lakhs)

# Regression line: vary size, keep bedrooms and age fixed at the new house's values
sizes = [x[0] for x in features]
line_sizes = list(range(min(sizes), max(sizes) + 1, 50))
line_prices = model.predict([[s, new_bedrooms, new_age] for s in line_sizes])

# Plot
plt.scatter(sizes, prices, color="blue", label="Training data")
plt.plot(line_sizes, line_prices, color="green",
         label=f"Regression line ({new_bedrooms} bed, {new_age} yrs old)")
plt.scatter(new_size, predicted, color="red", s=100, label="New prediction")

# Budget line (parallel to x-axis)
plt.axhline(y=budget, color="orange", linestyle="-", label=f"Budget ({budget} lakhs)")

# Perpendicular dashed lines from the predicted point to both axes
plt.plot([new_size, new_size], [0, predicted], color="red", linestyle="--")
plt.plot([0, new_size], [predicted, predicted], color="red", linestyle="--")

# Number the intersections on the axes
plt.text(new_size, -6, f"{new_size}", color="red", ha="center", va="top")
plt.text(-30, predicted, f"{predicted:.1f}", color="red", ha="right", va="center")

plt.xlim(0, 3200)
plt.ylim(0, 220)
plt.xlabel("House Size (sq ft)", labelpad=20)
plt.ylabel("House Price (lakhs)", labelpad=30)
plt.title("House Size vs Price")
plt.legend()
plt.show()