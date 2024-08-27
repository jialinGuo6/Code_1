def getMostVisited(n, sprints):
    # 创建一个数组来记录每个点的访问次数
    visit_count = [0] * (n + 1)  # 使用 n + 1 因为点是从 1 到 n

    # 遍历每对相邻的冲刺点
    for i in range(len(sprints) - 1):
        start = min(sprints[i], sprints[i + 1])
        end = max(sprints[i], sprints[i + 1])
        
        # 更新访问计数
        for j in range(start, end + 1):
            visit_count[j] += 1

    # 找到访问次数最多的点
    max_visits = max(visit_count)
    for i in range(1, n + 1):
        if visit_count[i] == max_visits:
            return i  # 返回第一个访问次数最多的点

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    sprints_count = int(input().strip())
    sprints = []

    for _ in range(sprints_count):
        sprints_item = int(input().strip())
        sprints.append(sprints_item)

    result = getMostVisited(n, sprints)

    fptr.write(str(result) + '\n')
    fptr.close()
