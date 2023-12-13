import re

def replace_in_sql(string):
    try:
        pattern = r"^IF\s*[a-zA-Z0-9_]+\s*>\s*0\s*[a-zA-Z0-9_]+\n\s*[a-zA-Z0-9_]+\.+[a-zA-Z0-9_]+\('.+'\)\s*[a-zA-Z0-9_]+\s+[a-zA-Z0-9_]+\s*<\s*0\s*[a-zA-Z0-9_]+\n\s*[a-zA-Z0-9_]+\.+[a-zA-Z0-9_]+\('.+'\);\s*[a-zA-Z0-9_]+\n\s*[a-zA-Z0-9_]+\.+[a-zA-Z0-9_]+\('.+'\);\s*END\s*IF;?$"
        if re.match(pattern, string):   
            new_string = re.sub('DBMS_OUTPUT.PUT_LINE', 'print', string)
            print('Replaced string:', new_string)
        else:
            print('String did not match the expected pattern.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
sql_string = """IF p_num > 0 THEN
         DBMS_OUTPUT.PUT_LINE('Positive Number')
   ELSIF p_num < 0 THEN
      DBMS_OUTPUT.PUT_LINE('Negative Number');
    ELSE
      DBMS_OUTPUT.PUT_LINE('Zero');
    END IF;"""
replace_in_sql(sql_string)
