import random

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0

    def predict(self, X):
        """Computes the linear regression prediction."""
        predictions = []
        for x in X:
            prediction = sum(w * x_i for w, x_i in zip(self.weights, x)) + self.bias
            predictions.append(prediction)
        return predictions

    def compute_loss(self, y_true, y_pred):
        """Computes Mean Squared Error (MSE)."""
        n = len(y_true)
        return sum((y_t - y_p) ** 2 for y_t, y_p in zip(y_true, y_pred)) / n

    def update_weights(self, X, y_true, y_pred):
        """Performs Gradient Descent to update weights and bias."""
        n = len(y_true)
        gradient_w = [0] * len(self.weights)
        gradient_b = 0

        for i in range(n):
            error = y_pred[i] - y_true[i]
            for j in range(len(self.weights)):
                gradient_w[j] += (error * X[i][j]) / n  # Partial derivative w.r.t weight
            gradient_b += error / n  # Partial derivative w.r.t bias

        # Update weights and bias using gradients
        for j in range(len(self.weights)):
            self.weights[j] -= self.learning_rate * gradient_w[j]
        self.bias -= self.learning_rate * gradient_b

    def fit(self, X, y):
        """Trains the model using gradient descent."""
        self.weights = [random.uniform(-1, 1) for _ in range(len(X[0]))]  # Initialize weights randomly
        self.bias = random.uniform(-1, 1)

        for epoch in range(self.epochs):
            y_pred = self.predict(X)
            loss = self.compute_loss(y, y_pred)
            self.update_weights(X, y, y_pred)

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.5f}")

# Example Dataset: Predicting house prices based on square feet and number of bedrooms
X_train = [
    [1400, 3],
    [1600, 3],
    [1700, 3],
    [1875, 2],
    [1100, 2],
    [1550, 4],
    [2350, 4],
    [2450, 3]
]
y_train = [245000, 312000, 279000, 308000, 199000, 315000, 400000, 410000]

# Train the model
model = LinearRegression(learning_rate=0.00000001, epochs=1000)
model.fit(X_train, y_train)

# Test Prediction
X_test = [[2000, 3], [1200, 2]]  # Predict house prices for these inputs
predictions = model.predict(X_test)
print("\nPredictions:", predictions)
