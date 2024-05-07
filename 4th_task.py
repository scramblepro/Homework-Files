def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        num_lines = len(content)
    return (file_name, num_lines, content)

file_list = ['1.txt', '2.txt', '3.txt']

# Считываем содержимое файлов и подсчитываем количество строк в каждом
files_info = []
for file_name in file_list:
    files_info.append(read_file(file_name))

# Сортируем список файлов по количеству строк
sorted_files_info = sorted(files_info, key=lambda x: x[1])

result_file_name = 'result.txt'
with open(result_file_name, 'w', encoding='utf-8') as result_file:
    for file_info in sorted_files_info:
        result_file.write(file_info[0] + '\n')
        result_file.write(str(file_info[1]) + '\n')
        result_file.writelines(file_info[2])
        result_file.write('\n')

print("Результат успешно записан в файл", result_file_name)
