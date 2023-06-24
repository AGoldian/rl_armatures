import math


def optimal_purchase(prices, max_items):
    days_number = len(prices)
    spent = [math.inf] * days_number
    buy_to_from = [{} for _ in range(days_number)]
    buy_from = [0] * days_number

    spent[0] = prices[0]
    buy_to_from[0][0] = 1
    for dayInd in range(1, days_number):
        spent[dayInd] = spent[dayInd - 1] + prices[dayInd]

        buy_to_from[dayInd][dayInd] = 1
        buy_from[dayInd] = dayInd
        for buy_from_day in range(max(0, dayInd - max_items + 1), dayInd):
            days_left = dayInd - buy_from_day
            need_to_spent = spent[buy_from_day] + prices[buy_from_day] * days_left
            if spent[dayInd] > need_to_spent:
                spent[dayInd] = need_to_spent
                buy_to_from[buy_from_day][dayInd] = days_left + 1
                buy_from[dayInd] = buy_from_day

    bought = [0] * days_number
    ind = days_number - 1
    while ind >= 0:
        bought[buy_from[ind]] = buy_to_from[buy_from[ind]][ind]
        if buy_from[ind] == ind:
            ind = ind - 1
        else:
            ind = buy_from[ind]

    remain_items = [0] * days_number
    current_items = 0
    for i in range(days_number):
        current_items += bought[i]
        current_items -= 1
        remain_items[i] = current_items
    return bought, remain_items
