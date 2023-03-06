# 文件
"""
import os

def main():
   pass
"""

# 打开文件
fr = open("/Users/kuan/Desktop/word", "r", encoding="UTF-8")
fw = open("/Users/kuan/Desktop/word1", "w", encoding="UTF-8")
# 写入文件
for line in fr:
    w_line = line.strip()
    print(line)
    if line == "4":
        print(line == "4")
        print("测试==")
        continue
    fw.write(w_line)
    fw.write("\n")
# 关闭文件
fr.close()
fr.close()
