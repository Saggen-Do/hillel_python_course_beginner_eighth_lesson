input_data = [('Sam', 17.95), ('Mike', 13.06),
              ('Dude', 4.24), ('Guy', 9.44)]
output_data = sorted(input_data, key=lambda x: x[1])
print(output_data)
