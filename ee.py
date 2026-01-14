import math

class BipolarPerceptron:
    def __init__(self, learning_rate=0.1):
        self.c = learning_rate
        self.weights = []

    def activation_func(self, net):
        """Bipolar sigmoid activation function."""
        return 2 / (1 + math.exp(-net))

    def activation_derivative(self, o):
        """Derivative of the activation function based on output."""
        return (1 - o * o) / 2

    @staticmethod
    def dot_product(l1, l2):
        return sum(a * b for a, b in zip(l1, l2))

    def update_weights(self, inputs, desired, actual):
        """Calculates delta and updates the weight vector."""
        f_net_dash = self.activation_derivative(actual)
        delta = self.c * (desired - actual) * f_net_dash
        
        # weight = weight + (c * error * f'(net) * input)
        self.weights = [round(w + (delta * xi), 3) for w, xi in zip(self.weights, inputs)]
        return f_net_dash

    def train(self, training_data, desired_outputs, initial_weights):
        self.weights = initial_weights
        
        print("\n--- Training Results ---")
        for xi, di in zip(training_data, desired_outputs):
            net = self.dot_product(self.weights, xi)
            oi = round(self.activation_func(net), 3)
            f_dash = self.update_weights(xi, di, oi)
            
            print(f"Input: {xi} | Output (oi): {oi} | f'(net): {f_dash}")
            print(f"Updated Weights: {self.weights}\n")

def get_user_input():
    """Handles data entry from the console."""
    try:
        n = int(input('Enter number of training samples: '))
        xn, dn = [], []
        
        for i in range(n):
            xi = list(map(float, input(f'Enter input vector x({i+1}) (space-separated): ').split()))
            di = float(input(f'Enter desired output d({i+1}): '))
            xn.append(xi)
            dn.append(di)
            
        w_init = list(map(float, input('Enter initial weights (space-separated): ').split()))
        return xn, dn, w_init
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None, None

if __name__ == "__main__":
    # 1. Initialize the model
    model = BipolarPerceptron(learning_rate=0.1)
    
    # 2. Collect data
    inputs, targets, weights = get_user_input()
    
    # 3. Run training
    if inputs:
        model.train(inputs, targets, weights)
