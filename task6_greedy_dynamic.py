items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(food_items: dict, budget: int) -> tuple[list[str], int, int]:
    sorted_items = sorted(
        food_items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories

def dynamic_programming(food_items: dict, budget: int) -> tuple[list[str], int, int]:
    names = list(food_items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        item = names[i - 1]
        cost = food_items[item]["cost"]
        calories = food_items[item]["calories"]

        for current_budget in range(budget + 1):
            if cost <= current_budget:
                dp[i][current_budget] = max(
                    dp[i - 1][current_budget],
                    dp[i - 1][current_budget - cost] + calories,
                )
            else:
                dp[i][current_budget] = dp[i - 1][current_budget]

    selected_items = []
    current_budget = budget
    for i in range(n, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            item = names[i - 1]
            selected_items.append(item)
            current_budget -= food_items[item]["cost"]

    selected_items.reverse()
    total_cost = sum(food_items[item]["cost"] for item in selected_items)
    total_calories = dp[n][budget]

    return selected_items, total_cost, total_calories

if __name__ == "__main__":
    budget = 100
    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)
    print(f"Budget: {budget}")
    print("\nGreedy algorithm result:")
    print("Selected items:", greedy_result[0])
    print("Total cost:", greedy_result[1])
    print("Total calories:", greedy_result[2])
    print("\nDynamic programming result:")
    print("Selected items:", dp_result[0])
    print("Total cost:", dp_result[1])
    print("Total calories:", dp_result[2])
