import random
from collections import Counter
import matplotlib.pyplot as plt

ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

def monte_carlo_dice_simulation(number_of_rolls: int = 100_000) -> dict[int, float]:
    sums_counter: Counter[int] = Counter()
    for _ in range(number_of_rolls):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sums_counter[dice_1 + dice_2] += 1

    return {total: sums_counter[total] / number_of_rolls for total in range(2, 13)}

def print_comparison_table(simulated: dict[int, float]) -> None:
    print("Sum | Monte Carlo | Analytical | Difference")
    print("----|-------------|------------|-----------")
    for total in range(2, 13):
        monte_carlo = simulated[total]
        analytical = ANALYTICAL_PROBABILITIES[total]
        difference = abs(monte_carlo - analytical)
        print(f"{total:>3} | {monte_carlo * 100:>10.2f}% | {analytical * 100:>9.2f}% | {difference * 100:>8.2f}%")

def plot_probabilities(simulated: dict[int, float]) -> None:
    sums = list(range(2, 13))
    monte_carlo_values = [simulated[total] * 100 for total in sums]
    analytical_values = [ANALYTICAL_PROBABILITIES[total] * 100 for total in sums]
    plt.figure(figsize=(10, 6))
    plt.plot(sums, monte_carlo_values, marker="o", label="Monte Carlo")
    plt.plot(sums, analytical_values, marker="x", label="Analytical")
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability (%)")
    plt.title("Monte Carlo vs Analytical Probabilities")
    plt.xticks(sums)
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    rolls = 100_000
    probabilities = monte_carlo_dice_simulation(rolls)
    print(f"Number of rolls: {rolls}\n")
    print_comparison_table(probabilities)
    plot_probabilities(probabilities)
