def arithmetic_arranger(problems, show_results = False):
    padding_char = ' ';
    arranged_problems = ''
    separator_char = '-'

    first_layer = ''
    second_layer = ''
    third_layer = ''
    fourth_layer = ''

    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    for i in problems:
      sequence = i.split()
      first_number = sequence[0].rstrip()
      operator = sequence[1].rstrip()
      second_number = sequence[2].rstrip()
      result = 0
      padding_len = max(len(first_number), len(second_number))

      if operator not in ['-', '+']:
        return "Error: Operator must be '+' or '-'."

      if len(first_number) > 4 or len(second_number) > 4:
        return "Error: Numbers cannot be more than four digits."
        
      if (first_number.isdigit() and second_number.isdigit()) == False:
        return "Error: Numbers must only contain digits."  

      if (operator == '-'):
        result = int(first_number) - int(second_number)
      else:
        result = int(first_number) + int(second_number)

      padded_first_number = first_number.rjust(int(padding_len) + 2, padding_char)
      padded_second_number = second_number.rjust(int(padding_len), padding_char)
      padded_result = str(result).rjust(int(padding_len) + 2, padding_char)
      padded_separator = separator_char.rjust(int(padding_len) + 2, separator_char)

      if (i != problems[-1]):
        first_layer += padded_first_number + '    '
        second_layer += operator + ' ' + padded_second_number + '    '
        third_layer += padded_separator + '    '
        fourth_layer += padded_result + '    '
      else:
        first_layer += padded_first_number
        second_layer += operator + ' ' + padded_second_number
        third_layer += padded_separator
        fourth_layer += padded_result

    arranged_problems = first_layer + '\n' + second_layer + '\n' + third_layer 

    if show_results == True:
      arranged_problems += '\n' + fourth_layer
      
    return arranged_problems