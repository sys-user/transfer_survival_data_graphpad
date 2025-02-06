# 随机生成测试集input.csv


import pandas as pd
import random

# 设置随机种子以确保结果可重复
random.seed(42)

# 初始化数据
data = {
    "时间（天）": [],
    "Group1死亡数": [],
    "Group2死亡数": [],
    "Group3死亡数": [],
    "Group4死亡数": [],
    "Group5死亡数": [],
}

# 模拟数据
total_days = 30  # 模拟30天
groups = 5
mice_per_group = 300  # 每组300只小鼠

for day in range(1, total_days + 1):
    data["时间（天）"].append(day)
    for group in range(1, groups + 1):
        # 随机生成每天每组的死亡数（0到剩余存活数量）
        remaining = mice_per_group - sum(data[f"Group{group}死亡数"])
        deaths = min(random.randint(0, remaining), random.randint(0,15))
        data[f"Group{group}死亡数"].append(deaths)

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存到 CSV 文件
df.to_csv("input.csv", index=False)

print("模拟数据已成功生成并保存到 input.csv")