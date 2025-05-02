import random

class Hat:
    def __init__(self, **balls):
        # Create the list of balls based on the arguments passed into the constructor
        self.contents = []
        self.original_contents = {}  # Keep track of the original ball counts
        for color, count in balls.items():
            self.contents.extend([color] * count)
            self.original_contents[color] = count

    def draw(self, num_balls):
        # If the number of balls to draw exceeds the available balls, return all available balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []  # Clear the contents, as all balls are drawn
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)  # Remove the drawn balls from the hat
        return drawn_balls

    def reset(self):
        # Reset the hat to its original state
        self.contents = []
        for color, count in self.original_contents.items():
            self.contents.extend([color] * count)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0  # Track how many experiments result in drawing the expected balls

    # Perform the experiment 'num_experiments' times
    for _ in range(num_experiments):
        # Make a fresh copy of the hat for each experiment
        hat.reset()  # Reset the hat to its original state
        drawn_balls = hat.draw(num_balls_drawn)

        # Count how many balls of each color we drew
        drawn_balls_count = {color: drawn_balls.count(color) for color in drawn_balls}

        # Check if the drawn balls meet or exceed the expected count for each color
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < expected_count:
                success = False
                break

        if success:
            success_count += 1

    # Return the probability of success as the ratio of successful experiments
    return success_count / num_experiments
