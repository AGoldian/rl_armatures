def optimal_purchase(prices, max_items=10):
    # определяем стартовое значение запаса товара как 0
    current_items = 0
    days_number = len(prices)

    bought = [0] * days_number  # список количества купленного товара по дням
    remain = [0] * days_number  # список оставшегося товара на каждый день

    for day in range(days_number):
        max_period_to_predict = min(max_items, days_number - day)
        if current_items >= days_number - day:
            max_period_to_predict = 0
        quantity_to_buy = 1 if current_items == 0 else 0
        for i in range(1, min(max_period_to_predict, max_items - current_items + 1)):
            if prices[day + i] > prices[day]:
                quantity_to_buy += 1
            else:
                break
        current_items += quantity_to_buy - 1
        bought[day] = quantity_to_buy
        remain[day] = current_items
    return bought, remain
