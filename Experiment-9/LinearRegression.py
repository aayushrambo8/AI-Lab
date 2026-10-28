import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data
hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
marks = [12, 22, 31, 40, 52, 58, 70, 78, 88, 95]

# Train the model
model = LinearRegression()
model.fit(hours, marks)

# Predict marks for new study time
new_hours = float(input("Enter the Number of hours you study: "))
predicted = model.predict([[new_hours]])[0]
print("Predicted marks for", new_hours, "hours:", round(predicted,2))

passing_marks = 40

# Plot
plt.scatter(hours, marks, color="blue", label="Training data")
plt.plot(hours, model.predict(hours), color="green", label="Regression line")
plt.scatter(new_hours, predicted, color="red", s=100, label="New prediction")

# Passing marks line (parallel to x-axis)
plt.axhline(y=passing_marks, color="black", linestyle="-", label="Passing marks (40)")

# Perpendicular dotted lines from the predicted point to both axes
plt.plot([new_hours, new_hours], [0, predicted], color="red", linestyle="--")  # down to x-axis
plt.plot([0, new_hours], [predicted, predicted], color="red", linestyle="--")  # across to y-axis

# Number the intersections on the axes
plt.text(new_hours, -4, f"{new_hours}", color="red", ha="center", va="top")
plt.text(-0.2, predicted, f"{predicted:.1f}", color="red", ha="right", va="center")

plt.xlim(0, 11)
plt.ylim(0, 105)
plt.xlabel("Hours Studied", labelpad=20)
plt.ylabel("Marks Obtained", labelpad=25)
plt.title("Hours Studied vs Marks Obtained")
plt.legend()
plt.show()