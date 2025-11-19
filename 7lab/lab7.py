import re  

def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except Exception as e:
        print(f"File {file_name} wasn't opened! Error: {e}")
        return None
    else:
        print(f"File {file_name} was opened in '{mode}' mode!")
        return file

file1_name = "TF2_1.txt"
file2_name = "TF2_2.txt"

print("\n--- Step A: Creating file ---")
file_1_w = Open(file1_name, "w")

if file_1_w:
    test_text = "The flight number 2024 is postponed for 40 minutes. Gate 5. Capacity: 100. ID: 123456."
    file_1_w.write(test_text)
    print(f"Text written to {file1_name}: \"{test_text}\"")
    file_1_w.close()
    print(f"File {file1_name} closed!")

print("\n--- Step B: Processing data ---")
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r and file_2_w:
    content = file_1_r.read()
    
    all_numbers = re.findall(r'\d+', content)
    
    filtered_numbers = [num for num in all_numbers if len(num) > 2]
    
    result_line = " ".join(filtered_numbers)
    
    file_2_w.write(result_line)
    
    print(f"Found numbers (len > 2): {filtered_numbers}")
    print("Data saved to TF2_2.txt in one line.")
    
    file_1_r.close()
    file_2_w.close()
    print("Files closed!")

print("\n--- Step C: Reading result ---")
print(f"Content of {file2_name}:")

file_2_r = Open(file2_name, "r")
if file_2_r:
    print(file_2_r.read())
    file_2_r.close()
    print(f"\nFile {file2_name} closed!")