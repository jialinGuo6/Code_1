def getMaximumAmount(quantity, m):
    # 将商品数量从大到小排序
    quantity.sort(reverse=True)
    print(quantity)  # 打印排序后的商品数量
    total_revenue = 0
    
    for i in range(m):
        if quantity[0] == 0:  # 如果所有商品都卖光了
            print("sold out! Sorry for customer", i+1,"th and after" )
            break
        # 检查当前最大数量的商品是否大于等于第二个最大数量
        if quantity[0] >= quantity[1]:
            total_revenue += quantity[0]  # 将最大数量的商品的价格加到总收入中
            quantity[0] -= 1  # 减少该商品的数量
            quantity.sort(reverse=True)  # 重新排序商品数量
            
    return total_revenue

if __name__ == '__main__':
    n = 5
    quantity = [10, 10, 8, 9, 1] 
    m = 6

    result = getMaximumAmount(quantity, m)
    print(result)  # 输出 55
    
    n = 3
    quantity = [1, 2, 4] 
    m = 4

    result = getMaximumAmount(quantity, m)
    print(result)  # 输出 11

    n = 3
    quantity = [1, 2, 4] 
    m = 8 

    result = getMaximumAmount(quantity, m)
    print(result)  # 输出 Sold out! Sorry to customers 8th and after.
