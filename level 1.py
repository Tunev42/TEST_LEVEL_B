#                                    LEVEL B
bit = int(input())
if bit == 1000:
  list_num = [1000]
  list_num1 = [1000 / 8]
  list_num2 = [1000 / 8 / 1024]
  list_num3 = [1000 / 8 / 1024 / 1024]
  list_num4 = [1000 / 8 / 1024 / 1024 / 1024]
  list_num5 = [1000 / 8 / 1024 / 1024 / 1024 / 1024]
  print(f"Бит {list_num}",'\n'
        f"Байт {list_num1}",'\n'
        f"Кб {list_num2}",'\n'
        f"Мб {list_num3}",'\n'
        f"Гб {list_num4}"'\n',
        f"Тб, {list_num5}"'\n')
