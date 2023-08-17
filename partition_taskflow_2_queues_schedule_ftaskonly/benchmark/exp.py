def read_numbers_from_file(filename, lines):
    numbers = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    number = parts[1].strip().rstrip('%')
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
lines_to_read = [15, 31, 47, 63, 79, 95, 111, 127, 143, 159]  # Specify the line numbers you want to read here

exp_path = ['./des_perf/', './vga_lcd/', './tv80/', './wb_dma/', './aes_core/', './ac97_ctrl/']
strname = ['des_perf_2queue_pftask_only', 'vga_lcd_2queue_pftask_only', 'tv80_2queue_pftask_only', 'wb_dma_2queue_pftask_only', 'aes_core_2queue_pftask_only', 'ac97_ctrl_2queue_pftask_only']
index = 0
for path in exp_path:
    file_path2 = path + '2_queue_pftask_only_log_p2.txt'
    file_path3 = path + '2_queue_pftask_only_log_p3.txt'
    file_path4 = path + '2_queue_pftask_only_log_p4.txt'
    file_path5 = path + '2_queue_pftask_only_log_p5.txt'
    file_path6 = path + '2_queue_pftask_only_log_p6.txt'
    file_path7 = path + '2_queue_pftask_only_log_p7.txt'
    file_path8 = path + '2_queue_pftask_only_log_p8.txt'
    file_path9 = path + '2_queue_pftask_only_log_p9.txt'
    file_path10 = path + '2_queue_pftask_only_log_p10.txt'
    file_path11 = path + '2_queue_pftask_only_log_p11.txt'
    file_path12 = path + '2_queue_pftask_only_log_p12.txt'
    file_path13 = path + '2_queue_pftask_only_log_p13.txt'
    file_path14 = path + '2_queue_pftask_only_log_p14.txt'
    file_path15 = path + '2_queue_pftask_only_log_p15.txt'
    file_path16 = path + '2_queue_pftask_only_log_p16.txt'
    file_path17 = path + '2_queue_pftask_only_log_p17.txt'
    file_path18 = path + '2_queue_pftask_only_log_p18.txt'
    file_path19 = path + '2_queue_pftask_only_log_p19.txt'
    file_path20 = path + '2_queue_pftask_only_log_p20.txt'

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
