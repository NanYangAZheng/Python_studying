import os

# 读取 report.txt 文件中的成绩；
with open('report.txt', 'r') as f:
    lines = f.readlines()
print(lines)

print('----------------------------')
print('----------------------------')


records = []
for i in lines:
    string = i.split() #依次将单个字符串转为多个字符串数组列表
    records.append(string)
print(records)

print('----------------------------')
print('----------------------------')

records[0].insert(0, '平均分')
records[0].insert(0, '总分')
records[0].insert(0, '排名')
print(records)


# 统计每名学生总成绩、计算平均并从高到低重新排名
# 汇总每一科目的平均分和总平均分（见下表第一行）
for i in records[1:]:
    zongfen = 0
    pingjunfen = 0
    for j in i[1:]:
        zongfen += int(j)
        # print(zongfen)
    pingjunfen = round(zongfen / len(i[1:]), 1)  # 将平均数四舍五入为一位小数
    # print(pingjunfen)
    i.insert(0, pingjunfen)  # 将总分和平均分插入列表
    i.insert(0, zongfen) # 将总分插入列表
    i.insert(0, records[1:].index(i) + 1) # 计算排名
print(records)

print('----------------------------')
print('----------------------------')

# 添加名次，替换60分以下的成绩为“不及格”

for i in records[1:]:
    xb = 4
    if int(i[xb]) < 60:
        i[xb] = i[xb] + '(不及格)'  # 将不及格添加到<60的成绩后面
    xb = xb + 1
print(records)


print('----------------------------')
file = input('请输入保存文件名+格式：')
print('----------------------------')

# 将处理后的成绩另存为一个新文件（result.txt）
if os.path.exists(file): # 如果文件存在，则删除
    os.remove(file)
# 保存文件

for i in records[0:]:
    with open(file, 'a') as f:
        f.write(str(i) + '\t\n')

print('处理完成！')

