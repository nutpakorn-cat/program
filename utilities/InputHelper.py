
import pandas as pd
import openpyxl


def data_frame_from_xlsx(xlsx_file, range_name):
    """ Get a single rectangular region from the specified file.
    range_name can be a standard Excel reference ('Sheet1!A2:B7') or 
    refer to a named region ('my_cells')."""
    wb = openpyxl.load_workbook(xlsx_file, data_only=True, read_only=True)
    if '!' in range_name:
        # passed a worksheet!cell reference
        ws_name, reg = range_name.split('!')
        if ws_name.startswith("'") and ws_name.endswith("'"):
            # optionally strip single quotes around sheet name
            ws_name = ws_name[1:-1]
        region = wb[ws_name][reg]
    else:
        # passed a named range; find the cells in the workbook
        full_range = wb.get_named_range(range_name)
        if full_range is None:
            raise ValueError(
                'Range "{}" not found in workbook "{}".'.format(
                    range_name, xlsx_file)
            )
        # convert to list (openpyxl 2.3 returns a list but 2.4+ returns a generator)
        destinations = list(full_range.destinations)
        if len(destinations) > 1:
            raise ValueError(
                'Range "{}" in workbook "{}" contains more than one region.'
                .format(range_name, xlsx_file)
            )
        ws, reg = destinations[0]
        # convert to worksheet object (openpyxl 2.3 returns a worksheet object
        # but 2.4+ returns the name of a worksheet)
        if isinstance(ws, str):
            ws = wb[ws]
        region = ws[reg]
    # an anonymous user suggested this to catch a single-cell range (untested):
    # if not isinstance(region, 'tuple'): df = pd.DataFrame(region.value)

    if not isinstance(region, tuple):
        df = pd.DataFrame([region.value])
    else:
        df = pd.DataFrame([cell.value for cell in row] for row in region)

    return df


def read_input(input_name):
    file_input = open('input/model-2-input.txt', 'r')
    lines_input = file_input.readlines()

    output = []
    can_start_reading_output = False

    for line in lines_input:
        if (can_start_reading_output and line.strip() == ''):
            can_start_reading_output = False
            break

        if (line.strip() == input_name):
            can_start_reading_output = True
            continue

        if can_start_reading_output:
            output.append([float(each_data)
                          for each_data in line.strip().split(' ')])

    return output


def read_initial_input():

    global model

    file_input = open('input/initial-input.txt', 'r')
    lines_input = file_input.readlines()

    test_count = 0

    for line in lines_input:
        splited_line = line.split(' ')

        if len(splited_line) <= 1:
            continue

        test_count = test_count + 1

        model += d[splited_line[0]] == float(splited_line[1])

    print("Final count is ", test_count)


def read_range(input_name):
    file_input = open('input/model-2-input.txt', 'r')
    lines_input = file_input.readlines()

    output = []
    can_start_reading_output = False

    for line in lines_input:
        if (can_start_reading_output and line.strip() == ''):
            can_start_reading_output = False
            break

        if (line.strip() == input_name):
            can_start_reading_output = True
            continue

        if can_start_reading_output:
            output.append([int(each_data)
                          for each_data in line.strip().split(' ')])

    return output


def read_input_1(input_name):
    file_input = open('input/model-1-input.txt', 'r')
    lines_input = file_input.readlines()

    output = []
    output_read = False

    for line in lines_input:
        if (output_read and line.strip() == ''):
            output_read = False
            break

        if (line.strip() == input_name):
            output_read = True
            continue

        if output_read:
            output.append([float(each_data)
                          for each_data in line.strip().split(' ')])

    return output


def read_range_1(input_name):
    file_input = open('input/model-1-input.txt', 'r')
    lines_input = file_input.readlines()

    output = []
    output_read = False

    for line in lines_input:
        if (output_read and line.strip() == ''):
            output_read = False
            break

        if (line.strip() == input_name):
            output_read = True
            continue

        if output_read:
            output.append([int(each_data)
                          for each_data in line.strip().split(' ')])

    return output
