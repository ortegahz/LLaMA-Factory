import glob
import json

# 获取所有txt文件的路径
input_file_paths = glob.glob('/home/Huangzhe/Test/AI智服答案整理/**/*.txt', recursive=True)
output_file_path = '../data/jade.json'

qa_pairs = []
for input_file_path in input_file_paths:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        instruction = None
        output = []

        for line in lines:
            line = line.strip()
            if line.startswith("Q:"):
                if instruction and output:  # 如果已经有了一个问答对，先保存
                    qa_pairs.append({
                        "instruction": instruction,
                        "input": "",
                        "output": "\n".join(output)
                    })
                instruction = line.replace("Q:", "", 1).strip()
                output = []
            elif line.startswith("Q："):
                if instruction and output:  # 如果已经有了一个问答对，先保存
                    qa_pairs.append({
                        "instruction": instruction,
                        "input": "",
                        "output": "\n".join(output)
                    })
                instruction = line.replace("Q：", "", 1).strip()
                output = []
            elif line.startswith("A:"):
                output.append(line.replace("A:", "", 1).strip())
            elif line.startswith("A："):
                output.append(line.replace("A：", "", 1).strip())
            else:
                if output:  # 如果当前正在读取答案部分
                    output.append(line)

        # 最后一个问答对
        if instruction and output:
            qa_pairs.append({
                "instruction": instruction,
                "input": "",
                "output": "\n".join(output)
            })

with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(qa_pairs, json_file, ensure_ascii=False, indent=4)

print(f"数据已成功写入到 {output_file_path} 文件中")
