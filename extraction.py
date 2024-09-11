import json

def leer_texto(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
        return None

def procesar_contenido(text):
    lines = text.split('\n')
    bible_structure = {}
    current_chapter = 0

    for line in lines:
        if line.strip() == '':
            continue
        if ':' in line:
            try:
                chapter_verse, verse_text = line.split(' ', 1)
                chapter, verse_num = chapter_verse.split(':')
                chapter = int(chapter)
                verse_num = int(verse_num)

                if chapter not in bible_structure:
                    bible_structure[chapter] = []

                bible_structure[chapter].append({'number': verse_num, 'text': verse_text})
            except ValueError as e:
                print(f"Error procesando la línea: {line}, error: {e}")
        else:
            print(f"Formato de línea no esperado: {line}")

    return bible_structure

def guardar_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo {file_path}: {e}")

# Ruta del archivo de texto
archivo_texto = 'versions/rvr1960/apocalipsis.txt'

# Leer contenido del archivo
contenido = leer_texto(archivo_texto)

if contenido:
    # Procesar el contenido para convertirlo en estructura de datos
    bible_data = procesar_contenido(contenido)

    # Guardar la estructura de datos en un archivo JSON
    guardar_json(bible_data, 'versions/rvr1960/apocalipsis.json')
else:
    print("No se pudo leer el archivo.")
