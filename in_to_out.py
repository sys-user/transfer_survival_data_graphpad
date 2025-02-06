import pandas as pd

# 输入文件路径
input_file = "input.csv"
output_file = "output.csv"

total_group_count = 5  #总共5组
total_mouse = 300 #每组20只
days = 30 #总实验天数 10天

# 读取 CSV 文件
csv_data = pd.read_csv(input_file)

# 创建输出数据列表
output_data = []
# 遍历每组
for group in range(1, total_group_count+1):  # Group1到Group5
    
    group_column = f"Group{group}死亡数"
    survived_count = total_mouse

    # 遍历每天
    for _, row in csv_data.iterrows():
        day = row["时间（天）"]

        death_count = row[group_column]
        survived_count = survived_count - death_count

        # 生成死亡记录
        for _ in range(death_count):
            record = {"X": day, "Group1": None, "Group2": None, "Group3": None, "Group4": None, "Group5": None}
            record[f"Group{group}"] = "1"
            output_data.append(record)

    # 生成存活记录
    print(group, survived_count)
    for _ in range(survived_count):
        
        record = {"X": days, "Group1": None, "Group2": None, "Group3": None, "Group4": None, "Group5": None}
        record[f"Group{group}"] = "0"
        output_data.append(record)

# 将数据保存为 CSV 文件
output_df = pd.DataFrame(output_data)
output_df.to_csv(output_file, index=False)

print(f"数据已成功转换并保存到 {output_file}")