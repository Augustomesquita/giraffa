from modules import giraffa_tools as gt

# Test character
my_character = gt.get_character()
print(my_character.get("equipaments", "Not a key valid"))
print(my_character)

# Test data with pagination
data = gt.get_data_with_pagination()
print(data)

# Test input number
print(gt.get_input_number())

# Test text file writing
gt.input_file_content("text_file.txt")

# Test text file reading
gt.output_file_content("text_file.txt")
