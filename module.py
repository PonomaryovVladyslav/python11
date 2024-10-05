def check_max_value(li: list[int]) -> int:
    min_value = 0
    for i in range(len(li)):
        if li[i] > min_value:
            min_value = li[i]


