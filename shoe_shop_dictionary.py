def manage_purchase(shoe_sizes, purchase_plan):
    shoe_rack = dict()
    earn = 0

    for size in shoe_sizes.split():
        if shoe_rack.get(size) is None:
            shoe_rack[size] = 1
        else:
            shoe_rack[size] = shoe_rack.get(size) + 1

    for purchase in purchase_plan:
        size, cost = purchase.split()

        if shoe_rack.get(size) is not None:
            shoe_rack[size] = shoe_rack.get(size) - 1
            earn += int(cost)
            if shoe_rack.get(size) == 0:
                del shoe_rack[size]

    return earn


if __name__ == "__main__":
    shoes = int(input())
    shoe_sizes = input()
    customers = int(input())
    purchase = list()

    [purchase.append(input()) for _ in range(customers)]

    print(manage_purchase(shoe_sizes, purchase))