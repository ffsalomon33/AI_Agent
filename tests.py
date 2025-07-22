from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("Test 1")
#print(get_files_info("calculator", "."))
#print(get_file_content("calculator", "lorem.txt"))
print("Test 2")
#print(get_files_info("calculator", "pkg"))
print(get_file_content("calculator", "main.py"))
print("Test 3")
#print(get_files_info("calculator", "/bin"))
print(get_file_content("calculator", "pkg/calculator.py"))
print("Test 4")
#print(get_files_info("calculator", "../"))
print(get_file_content("calculator", "/bin/cat"))
print("Test 5")
print(get_file_content("calculator", "pkg/does_not_exist.py"))