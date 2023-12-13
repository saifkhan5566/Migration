import re

def replace_in_sql(sql_string):
    pattern = r'^select\s+[a-zA-Z0-9_]+\s+into\s+[a-zA-Z0-9_]+\s+from\s+[a-zA-Z0-9_]+\s+where\s+[a-zA-Z0-9_]+\s+:=\s+\d+\s+return\s+[a-zA-Z0-9_]+;$'
    if re.match(pattern, sql_string):
        new_string = re.sub(':=', '=', sql_string)
        new_string = re.sub('your_table', 'db.your_table', new_string)
        print('Replaced string:', new_string)
    else:
        print('String did not match the expected pattern.')

sql_string = 'select your_column into v_result from your_table where col1 := 12 return v_result;'
replace_in_sql(sql_string)
