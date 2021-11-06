  
import sys
import base

first_msg = """
        Выберите команду:
        1. help 
        2. delete - удалить файл/директорию
        3. copy - скопировать файл/директорию
        4. move - переместить файл/директорию
        5. rename - переименовать файл/директорию
        6. write - запись текста в файл
        7. create_file - создать новый файл
        8. create_folder - создать папку
        9. change_directory - перемещение между папками
        10. exit - выход
    """
work_directory = sys.argv[0].lstrip('/').split(sep='/')[:-1]
work_directory[0] = '/' + work_directory[0]
work_path = '/'.join(work_directory) + '/'

print(first_msg)
while True:
    cmd = input('Введите команду')
    if cmd == 'help':
        print(first_msg)

    elif cmd == 'exit':
        exit(print('До свидания.'))

    elif cmd == 'delete':
        delete_file_name = input('Введите имя файла, который вы хотите удалить')
        base.delete_file(work_path + delete_file_name)

    elif cmd == 'copy':
        name = input('Введите имя файла/директории, которую вы хотите скопировать')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Что-то пошло не так')
            continue
        new_name = input('Введите название нового файла')
        if '/' not in new_name:
            new_name = work_path + new_name
        base.copy_file(name, new_name)

    elif cmd == 'move':
        name = input('Введите имя файла/директории, которую вы хотите переместить')
        if name.startswith('/') and not base.check_bounds('/'.join(work_directory), name):
            print('Что-то пошло не так')
            continue
        new_name = input('Выберите директорию для перемещения')
        if '/' not in new_name:
            new_name = work_path + new_name
        base.move_or_rename_file(name, new_name)

    elif cmd == 'rename':
        name = input('Введите имя файла/директории, которую вы хотите переименовать')
        if name.startswith('/') and not base.check_bounds('/'.join(work_directory), name):
            print('Что-то пшло не так')
            continue
        new_name = input('Введите новое название')
        base.move_or_rename_file(name, new_name)

    elif cmd == 'write':
        name = input('Введите имя файла/директории, в которую вы хотите записать текст')
        if name.startswith('/') and not base.check_bounds('/'.join(work_directory), name):
            print('Что-то пошло не так')
            continue
        text = input('Введите текст')

        if '/' not in name:
            name = work_path + name
        base.add_text_to_file(name, text)

    elif cmd == 'create_file':
        name = input('Введите название нового файла')
        if name.startswith('/') and not base.check_bounds('/'.join(work_directory), name):
            print('Что-то пошло не так')
            continue
        text = input('Введите текст, если вы хотите записать его в файл')
        if '/' not in name:
            name = work_path + name
        base.create_file(name, text=text)

    elif cmd == 'change_directory':
        print("""
        .  если вы хотите остаться в текущей директории
        ..  если вы хотите подняться
        <имя папки> если вы хотите перейти в конкретную папку
        """)
        folder = input()
        work_directory = base.cd_command(work_directory, folder)
        work_path = '/'.join(work_directory) + '/'
        
    elif cmd == 'create_folder':
        name = input('Введите название новой папки')
        if name.startswith('/') and not base.check_bounds('/'.join(work_directory), name):
            print('Что-то пошло не так')
            continue
        if '/' not in name:
            name = work_path + name
        base.create_folder(name)
    else:
        print('Неверная команда')
