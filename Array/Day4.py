def maximumWealth(accounts):
    max_wealth = 0
    for money in accounts:
        wealth = sum(money)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

accounts1 = [[1, 2, 3], [3, 2, 1]]
print("maximum welth account 1:", maximumWealth(accounts1))  # Output: 6

accounts2 = [[1, 5], [7, 3], [3, 5]]
print("maximum welth account 2", maximumWealth(accounts2))  # Output: 10