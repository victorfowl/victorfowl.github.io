import os
import json

proyectos = []

try:
    for carpeta in os.listdir('proyectos'):
        path_carpeta = os.path.join('proyectos', carpeta)
        if os.path.isdir(path_carpeta):
            proyecto_html = os.path.join(path_carpeta, 'index.html')
            proyecto_video = os.path.join(path_carpeta, 'video.mp4')
            proyecto_txt = os.path.join(path_carpeta, 'description.txt')

            # Leer el contenido del archivo HTML
            with open(proyecto_html, 'r', encoding='utf-8') as f_html:
                contenido_html = f_html.read()

            descripcion = ""
            etiquetas = []
            if os.path.exists(proyecto_txt):
                with open(proyecto_txt, 'r', encoding='utf-8') as f_txt:
                    lines = f_txt.readlines()
                    # Separar etiquetas que empiezan con '#'
                    for line in lines:
                        if line.startswith('#'):
                            etiqueta = line.strip().lstrip('#').lower() 
                            print(etiqueta)
                            etiquetas.append(etiqueta)
                        else:
                            descripcion += line.strip() + " " 

            # Crear el proyecto con los datos correspondientes
            proyecto = {
                'titulo': carpeta,
                'link': proyecto_html,
                'video': proyecto_video,
                'descripcion': descripcion.strip(),  # Limpiar espacios extra
                'etiquetas': etiquetas
            }
            proyectos.append(proyecto)

    # Escribir el archivo JSON
    with open('data/proyectos.json', 'w', encoding='utf-8') as json_file:
        json.dump(proyectos, json_file, ensure_ascii=False, indent=4)

except Exception as e:
    print(f"Error al procesar: {e}")


