import sys
import csv


def main(arg1, arg2):
    # 在这里执行你的Python脚本逻辑
    print("参数1:", arg1)
    print("参数2:", arg2)

    # 示例：生成一个.csv文件
    csv_data = [
        ['Name', 'Age'],
        ['John', '30'],
        ['Jane', '25']
    ]
    csv_file = 'output.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    print("生成的.csv文件已保存:", csv_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <arg1> <arg2>")
        sys.exit(1)

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    main(arg1, arg2)
