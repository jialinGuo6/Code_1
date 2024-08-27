def minDaysToTargetEngagement(initialEngagementScore, targetEngagementScore, trainingEngagementScore):
    # Write your code here
    resultDay = 0
    maxTraningSet = max(trainingEngagementScore)
    used = set()
    resultDay = 1
    maxSocre= max(trainingEngagementScore)
    while initialEngagementScore < targetEngagementScore:
        if initialEngagementScore >= targetEngagementScore:
            break 
        if any(trainingEngagementScore) >= initialEngagementScore:
            initialEngagementScore = initialEngagementScore + resultDay
            resultDay += 1
        else:
            for i in range(len(trainingEngagementScore)):
                if initialEngagementScore >= trainingEngagementScore[i] and not used:
                    initialEngagementScore = initialEngagementScore + trainingEngagementScore[i]
                    used.add(trainingEngagementScore[i])
                    resultDay += 1
                    continue
                if initialEngagementScore >= trainingEngagementScore[i] and used and initialEngagementScore < maxSocre:
                    initialEngagementScore = initialEngagementScore + resultDay
                    resultDay += 1
                else:
                    initialEngagementScore = initialEngagementScore + maxSocre
                    resultDay += 1

    
    return resultDay
    
    
a = minDaysToTargetEngagement(0,30,[15,3,2])
print(a)
####################################

def training_days(initialEngagementScore, targetEngagementScore, trainingEngagementScore):
    days = 0
    used_scores = [False] * len(trainingEngagementScore)  # 记录训练分数是否已使用

    while initialEngagementScore < targetEngagementScore:
        days += 1  # 增加天数
        
        # 查找可以使用的训练分数
        can_use_score = False
        for i in range(len(trainingEngagementScore)):
            if not used_scores[i] and initialEngagementScore >= trainingEngagementScore[i] and days <= trainingEngagementScore[i]:
                initialEngagementScore += trainingEngagementScore[i]  # 使用训练分数
                used_scores[i] = True  # 标记为已使用
                can_use_score = True  # 标记为可以使用分数
                break  # 使用一个分数后退出循环
        
        if not can_use_score:
            # 如果没有可以使用的训练分数，则增加初始分数
            initialEngagementScore += days  # 每天增加的分数为天数
        
    return days

# 示例输入
initialEngagementScore = 0
targetEngagementScore = 30
trainingEngagementScore = [15, 3, 2]

# 调用函数并打印结果
result = training_days(initialEngagementScore, targetEngagementScore, trainingEngagementScore)
print("完成任务天数:", result)
