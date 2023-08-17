def read_numbers_from_file(filename, lines):
    numbers = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    number = parts[1].strip()
                    try:
                        number = float(number)
                        numbers.append(number)
                    except ValueError:
                        print(f"Invalid number found on line {line_number}: {number}")
    results = 0
    for i in range(len(numbers)):
        results += numbers[i]
    return results / len(numbers)


# Usage example
lines_to_read = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]  # Specify the line numbers you want to read here

exp_path = ['./des_perf/', './vga_lcd/', './tv80/', './wb_dma/', './aes_core/', './ac97_ctrl/']
strname = ['des_perf_original_tbb_ftask', 'vga_lcd_original_tbb_ftask', 'tv80_original_tbb_ftask', 'wb_dma_original_tbb_ftask', 'aes_core_original_tbb_ftask', 'ac97_ctrl_original_tbb_ftask']
index = 0
for path in exp_path: 
    file_path2 = path + 'tbb_log_t2.txt'
    file_path3 = path + 'tbb_log_t3.txt'
    file_path4 = path + 'tbb_log_t4.txt'
    file_path5 = path + 'tbb_log_t5.txt'
    file_path6 = path + 'tbb_log_t6.txt'
    file_path7 = path + 'tbb_log_t7.txt'
    file_path8 = path + 'tbb_log_t8.txt'
    file_path9 = path + 'tbb_log_t9.txt'
    file_path10 = path + 'tbb_log_t10.txt'
    file_path11 = path + 'tbb_log_t11.txt'
    file_path12 = path + 'tbb_log_t12.txt'
    file_path13 = path + 'tbb_log_t13.txt'
    file_path14 = path + 'tbb_log_t14.txt'
    file_path15 = path + 'tbb_log_t15.txt'
    file_path16 = path + 'tbb_log_t16.txt'
    file_path17 = path + 'tbb_log_t17.txt'
    file_path18 = path + 'tbb_log_t18.txt'
    file_path19 = path + 'tbb_log_t19.txt'
    file_path20 = path + 'tbb_log_t20.txt'

    results2 = read_numbers_from_file(file_path2, lines_to_read)
    results3 = read_numbers_from_file(file_path3, lines_to_read)
    results4 = read_numbers_from_file(file_path4, lines_to_read)
    results5 = read_numbers_from_file(file_path5, lines_to_read)
    results6 = read_numbers_from_file(file_path6, lines_to_read)
    results7 = read_numbers_from_file(file_path7, lines_to_read)
    results8 = read_numbers_from_file(file_path8, lines_to_read)
    results9 = read_numbers_from_file(file_path9, lines_to_read)
    results10 = read_numbers_from_file(file_path10, lines_to_read)
    results11 = read_numbers_from_file(file_path11, lines_to_read)
    results12 = read_numbers_from_file(file_path12, lines_to_read)
    results13 = read_numbers_from_file(file_path13, lines_to_read)
    results14 = read_numbers_from_file(file_path14, lines_to_read)
    results15 = read_numbers_from_file(file_path15, lines_to_read)
    results16 = read_numbers_from_file(file_path16, lines_to_read)
    results17 = read_numbers_from_file(file_path17, lines_to_read)
    results18 = read_numbers_from_file(file_path18, lines_to_read)
    results19 = read_numbers_from_file(file_path19, lines_to_read)
    results20 = read_numbers_from_file(file_path20, lines_to_read)

    print("y_"+strname[index], end = " = [",)
    print(results2, end = ",")
    print(results3, end = ",")
    print(results4, end = ",")
    print(results5, end = ",")
    print(results6, end = ",")
    print(results7, end = ",")
    print(results8, end = ",")
    print(results9, end = ",")
    print(results10, end = ",")
    print(results11, end = ",")
    print(results12, end = ",")
    print(results13, end = ",")
    print(results14, end = ",")
    print(results15, end = ",")
    print(results16, end = ",")
    print(results17, end = ",")
    print(results18, end = ",")
    print(results19, end = ",")
    print(results20, end = "")
    print("]\n")
    index += 1;






















