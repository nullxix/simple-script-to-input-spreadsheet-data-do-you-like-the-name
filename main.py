import sys
import config
import sheetinator

args = sys.argv

def main():
    sheet_name = args[1]
    input_rows_count = 1 #by default, input 1 row
    if len(args) >= 3:
        input_rows_count = int(args[2]) #user can optionally specify row count

    sheet_config = config.sheets[sheet_name]
    print('\n--getting', input_rows_count, 'rows for', sheet_name)
    payload = []
    for x in range(1, input_rows_count + 1):
        print('\n --new row--')
        payload.append(get_row(sheet_config))

    print('connecting to sheets (this may take a while). . .')
    sheetinator.upload(
        payload, 
        sheet_name = args[1], 
        sheet_id=sheet_config['id'],
        tab_name=sheet_config['tab_name']
    )

def get_row(sheet_config):
    row = []
    for col_name in sheet_config['columns']:
        col_val = input('    ' + col_name + ': ')
        row.append(col_val)
    return row

if __name__ == '__main__':
    main()