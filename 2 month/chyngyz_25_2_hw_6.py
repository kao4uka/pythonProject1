import re

with open("MOCK_DATA.txt", 'r') as file:
    file_name = file.read()
    file_list = re.findall(r'[A-Z][a-zA-Z]*\.[a-z0-9]+', file_name)
    email_list = re.findall(r'[\w.-]+@[\w.-]+', file_name)
    name_list = re.findall(r"[A-Z][a-z-]+\s+[A-Za-d][A-Za-z- O']+", file_name)
    rgb_list = re.findall(r'#[\w]+', file_name)
print("1-get name list, 2-get file name list, 3-get email list, 4-get color list, 5-exit")

while True:
    user_input = int(input(f"Enter number: "))
    if user_input == 1:
        print('process completed')
        with open('name.txt', 'w') as file:
            file.write(f'{name_list}')
    elif user_input == 4:
        print("process completed")
        with open('rgb.txt', 'w') as file:
            file.write(f'{rgb_list}')
    elif user_input == 3:
        print("process completed")
        with open('email.txt', 'w') as file:
            file.write(f'{email_list}')
    elif user_input == 2:
        print('process completed')
        with open('files.txt', 'w') as file:
            file.write(f'{file_list}')
    elif user_input == 5:
        print("process completed")
        break
    else:
        raise ValueError("Enter number from 1 to 5!")