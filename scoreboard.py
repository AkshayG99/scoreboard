import matplotlib.pyplot as plt

class Scoreboard:
    def __init__(self):
        self.scores = {}

    def add_player(self, player_name):
        if player_name not in self.scores:
            self.scores[player_name] = 0
            print(f"Player '{player_name}' added to the scoreboard.")

    def remove_player(self, player_name):
        if player_name in self.scores:
            del self.scores[player_name]
            print(f"Player '{player_name}' removed from the scoreboard.")

    def update_score(self, player_name, points):
        if player_name in self.scores:
            self.scores[player_name] += points
            print(f"Player '{player_name}' earned {points} points.")

    def display_scores(self):
        print("Current Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    def plot_scores(self):
        players = list(self.scores.keys())
        scores = list(self.scores.values())

        plt.bar(players, scores, color='skyblue')
        plt.xlabel('Players')
        plt.ylabel('Scores')
        plt.title('Scoreboard')
        plt.show()


# Create a Scoreboard instance
scoreboard = Scoreboard()

# Prompt user to input players and scores
while True:
    player_name = input("Enter player name (or 'done' to finish): ")
    if player_name.lower() == 'done':
        break
    scoreboard.add_player(player_name)

    while True:
        try:
            points = int(input(f"Enter score for {player_name}: "))
            scoreboard.update_score(player_name, points)
            break
        except ValueError:
            print("Please enter a valid integer for score.")

# Display and plot scores
scoreboard.display_scores()
scoreboard.plot_scores()
