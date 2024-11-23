import re

def convert_to_machine_readable(expression):
    expression = expression.replace('×', '*').replace('÷', '/').replace('−', '-')
    expression = re.sub(r'(?<=[0-9)])\(', '*(', expression)
    expression = re.sub(r'(?<![0-9)])\)', ')*', expression)
    expression = re.sub(r'(?<=[0-9])[^+\-*/()]', r'*\g<0>', expression)
    expression = re.sub(r'\s*\*\s*', '*', expression)
    return expression

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

human_expression = input("Enter a complex expression in BODMAS format: ")
machine_readable_expression = convert_to_machine_readable(human_expression)
print("Machine-readable expression:", machine_readable_expression)
result = evaluate_expression(machine_readable_expression)
print("Result:", result)
