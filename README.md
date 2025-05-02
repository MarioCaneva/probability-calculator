# Probability Calculator

This Python project simulates random experiments of drawing balls from a hat and estimates the probability of drawing a specific combination of balls. The program models a hat using an object-oriented approach and allows for conducting experiments to estimate the probability of drawing a set of balls.

---

## 📦 Features

- **Hat Class**: Represents a hat containing a variety of colored balls, with methods to draw balls randomly and reset the hat.
- **Experiment Function**: Runs multiple experiments to simulate random draws and calculates the probability of drawing a specific combination of balls.
- **Monte Carlo Simulation**: The program uses Monte Carlo simulations to estimate probabilities through repeated random sampling.

---

## 🧠 Concepts Practiced

- **Probability**: Using random sampling and counting successful outcomes to estimate probabilities.
- **Object-Oriented Programming**: The Hat class uses encapsulation to manage the balls in the hat, and the experiment function works with this class to run simulations.
- **Randomness**: Simulating random draws from a hat and checking how often a certain combination of balls is drawn.
- **Monte Carlo Method**: A statistical method that uses repeated random sampling to estimate probabilities.

---

## 📚 Usage Example

```python
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={'red': 1, 'green': 2}, num_balls_drawn=4, num_experiments=1000)
print(probability)
Output:
Copy
Edit
0.356
This example simulates 1000 experiments of drawing 4 balls from a hat containing 5 blue, 4 red, and 2 green balls, and calculates the probability of drawing at least 1 red ball and 2 green balls.

⚙️ Functions
Hat Class
The Hat class contains:

Attributes:

contents: A list of balls in the hat.

original_contents: Keeps track of the original number of balls in the hat for resetting.

Methods:

draw(num_balls): Draws a specified number of balls from the hat and removes them.

reset(): Resets the hat back to its original state.

experiment() Function
The experiment() function:

Takes a Hat object, expected_balls (a dictionary of expected balls), num_balls_drawn, and num_experiments.

Simulates multiple random draws and calculates the probability of getting the expected number of balls in each experiment.

🛠️ How to Run
Clone this repository to your local machine.

Run the following Python script to perform an experiment and calculate the probability:

bash
Copy
Edit
python probability_calculator.py
You can modify the parameters in the script to test different scenarios.
