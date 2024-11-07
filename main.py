def northwest_corner_method(supply, demand):
    allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    total_supply = supply.copy()
    total_demand = demand.copy()

    i, j = 0, 0

    while i < len(supply) and j < len(demand):
        allocated_amount = min(total_supply[i], total_demand[j])
        allocation[i][j] = allocated_amount
        total_supply[i] -= allocated_amount
        total_demand[j] -= allocated_amount

        if total_supply[i] == 0:
            i += 1
        if total_demand[j] == 0:
            j += 1

    return allocation


# Пример использования
supply = [20, 30, 25]  # Доступные ресурсы
demand = [10, 30, 35]  # Потребности

result = northwest_corner_method(supply, demand)
print("Опорный план (распределение):")
for row in result:
    print(row)