from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


print("Test 1")
#print(get_files_info("calculator", "."))
#print(get_file_content("calculator", "lorem.txt"))
#print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(run_python_file("calculator", "main.py"))
print("Test 2")
#print(get_files_info("calculator", "pkg"))
#print(get_file_content("calculator", "main.py"))
#print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("Test 3")
#print(get_files_info("calculator", "/bin"))
#print(get_file_content("calculator", "pkg/calculator.py"))
#print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
print(run_python_file("calculator", "tests.py"))
print("Test 4")
#print(get_files_info("calculator", "../"))
#print(get_file_content("calculator", "/bin/cat"))
print(run_python_file("calculator", "../main.py"))
print("Test 5")
#print(get_file_content("calculator", "pkg/does_not_exist.py"))
print(run_python_file("calculator", "nonexistent.py"))