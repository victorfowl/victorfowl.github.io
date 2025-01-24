import os
import json

projects_dir = 'proyectos'
output_file = 'data/proyectos.json'

projects = []

for folder in os.listdir(projects_dir):
    project_path = os.path.join(projects_dir, folder)
    html_file = os.path.join(project_path, 'index.html')
    video_file = os.path.join(project_path, 'video.mp4')

    if os.path.isfile(html_file) and os.path.isfile(video_file):
        project = {
            'titulo': folder,
            'link': f'proyectos/{folder}/index.html',
            'video': f'proyectos/{folder}/video.mp4',
            'descripcion': f'Descripción del proyecto {folder}'
        }
        projects.append(project)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)

print(f'Archivo {output_file} generado correctamente.')
