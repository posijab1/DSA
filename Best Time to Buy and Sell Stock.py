def best_time_to_buy_and_sell_stocks(arr):

    l, r = 0, 1
    maxP = 0

    while r < len(arr):
        if arr[l] < arr[r]:
            profit = arr[r] - arr[l]
            maxP = max(maxP, profit)
        else:
            l += 1
        r += 1
    return maxP

print(best_time_to_buy_and_sell_stocks([1,2,3,4,5]))