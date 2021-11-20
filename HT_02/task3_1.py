#
#    3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
#   Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
#    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#
input_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
output_list = []
print(input_list)
for current_element in input_list :
    if current_element :
        output_list.append(current_element)
print(output_list)
