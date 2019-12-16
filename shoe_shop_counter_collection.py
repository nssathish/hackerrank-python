from collections import Counter


def manage_purchase(rack, purchase):
    purchased_amount = 0

    for size_and_cost in purchase:
        size, cost = size_and_cost.split()

        if rack.get(size) is not None:
            purchased_amount += int(cost)
            rack[size] = rack.get(size) - 1
            if rack.get(size) == 0:
                del rack[size]

    return purchased_amount


if __name__ == "__main__":
    shoes = int(input())
    shoes_sizes = input()
    shoe_rack = Counter(shoes_sizes.split())
    customers = int(input())
    purchase_plan = list()

    [purchase_plan.append(input()) for _ in range(customers)]

    print(manage_purchase(shoe_rack, purchase_plan))