#Подключаем библиотеки
import os
from PIL import Image
import shutil
import pillow_avif
#Папка исходных изображений для конвертации
source_folder = '/home/arthur/Projects/Image-Converter/Pictures'

#Папка с результатами после процесса конвертации
result_folder = '/home/arthur/Projects/Image-Converter/Result'

#Создаем папку назначения, если её нет
os.makedirs(result_folder, exist_ok=True)

#Получаем файлы из папки с исходными изображениями 
files = os.listdir(source_folder)

#Валидация форматов исходных файлов (для теста client.txt)
valid_image_formats = ('.png', '.bmp', '.gif', '.avif', '.webp')

#Конвертация файлов в формат .jpg
for filename in files:
    if filename.lower().endswith(valid_image_formats):
        src_path = os.path.join(source_folder, filename)
        try:
            with Image.open(src_path) as img:
#Конвертируем и сохраняем как .jpg
                base_name = os.path.splitext(filename)[0]
                new_path = os.path.join(source_folder, base_name + '.jpg')
                rgb_img = img.convert('RGB')
                rgb_img.save(new_path, 'JPEG')
                print(f'Конвертировал: {filename} в {base_name}.jpg')
        except Exception as e:
            print(f'Ошибка при обработке {filename}: {e}')

#Проверка,чтобы убедиться, что появились новые .jpg хех)
files = os.listdir(source_folder)
jpeg_files = [f for f in files if f.lower().endswith('.jpg')]

# Процесс переименования файлов 
for index, filename in enumerate(jpeg_files, start=1):
    src_path = os.path.join(source_folder, filename)
    dest_path = os.path.join(result_folder, f"{index}.jpg")
    shutil.move(src_path, dest_path)
    print(f'Переименовал: {filename} в {dest_path}')