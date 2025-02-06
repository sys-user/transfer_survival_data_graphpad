
### README


# GraphPad 生存曲线数据生成与转换工具

本项目提供了一组 Python 脚本，用于生成模拟的生存实验数据，并将其转换为 GraphPad Prism 软件所需的格式，以便绘制生存曲线。

## 文件说明

1. **`test_set.py`**  
   用于生成模拟的输入数据 `input.csv`，其中包含每天每组小鼠的死亡数量。

2. **`in_to_out.py`**  
   将 `input.csv` 中的数据转换为 GraphPad Prism 所需的格式 `output.csv`，其中每行表示一只小鼠的生存状态。

3. **`input.csv`**  
   模拟的输入数据文件，包含每天每组小鼠的死亡数量。

4. **`output.csv`**  
   转换后的输出数据文件，包含每只小鼠的生存状态，格式符合 GraphPad Prism 的要求。

## 使用方法

### 1. 安装依赖

确保已安装 Python 3.x，https://www.python.org

并安装所需的库：

```bash
pip install pandas
```

### 2. 生成模拟数据

运行 `test_set.py` 脚本生成模拟数据：

```bash
python test_set.py
```

脚本会在当前目录生成 `input.csv` 文件。

### 3. 转换数据格式

运行 `in_to_out.py` 脚本将 `input.csv` 转换为 `output.csv`：

```bash
python in_to_out.py
```

脚本会在当前目录生成 `output.csv` 文件。

### 4. 使用 GraphPad Prism 绘制生存曲线

1. 打开 GraphPad Prism 软件。
2. 选择 `Survival` 模块，创建一个新的生存分析项目。
3. 导入 `output.csv` 文件。
4. 按照软件提示完成生存曲线的绘制。

## 示例数据

### 输入文件 (`input.csv`)

```csv
时间（天）,Group1死亡数,Group2死亡数,Group3死亡数,Group4死亡数,Group5死亡数
1,2,1,0,1,0
2,1,0,1,0,1
3,14,0,13,8,6
4,3,12,11,8,14
5,3,2,11,2,7
6,2,3,8,11,11
7,6,2,5,5,12
8,7,1,2,12,2
9,10,15,14,8,7
10,8,13,12,7,15
...
```

### 输出文件 (`output.csv`)

```csv
X,Group1,Group2,Group3,Group4,Group5
1,1,0,0,1,0
1,1,0,0,0,0
1,0,1,0,0,0
2,1,0,0,0,0
2,0,0,1,0,0
3,1,0,0,0,0
3,1,0,0,0,0
3,1,0,0,0,0
3,1,0,0,0,0
3,1,0,0,0,0
...
```

## 注意事项

1. **数据格式**  
   确保 `input.csv` 文件的格式正确，列名与脚本中的列名一致。

2. **数据范围**  
   脚本中的模拟数据生成逻辑可以根据需要调整，例如每组的小鼠数量、实验天数等。

3. **GraphPad Prism 版本**  
   本工具生成的 `output.csv` 文件适用于 GraphPad Prism 8 及以上版本。

## 联系方式

如有任何问题或建议，请联系作者:xiexiaowei0513@163.com




