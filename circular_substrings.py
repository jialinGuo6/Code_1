def circular_substrings(s):
    n = len(s)
    result = set()  # 使用集合以确保唯一性

    # 生成循环字符串
    circular_string = s + s  # 将字符串自身连接以模拟循环
    print(circular_string)
    # 从每个字符开始生成子字符串
    for i in range(n):
        for j in range(1, n + 1):  # j 表示子字符串的长度
            substring = circular_string[i:i + j]
            result.add(substring)

    return result

# 示例输入
s = 'bac'
substrings = circular_substrings(s)

# 打印结果
print("所有可能的子字符串:")
for substring in sorted(substrings):  # 排序以便于查看
    print(substring)
