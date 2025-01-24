const fs = require('fs');
const path = require('path');

// Directorio donde están los proyectos y videos
const projectsDir = path.join(__dirname, 'proyectos');
const videosDir = path.join(__dirname, 'videos');
const outputFile = path.join(__dirname, 'data', 'proyectos.json');

// Función para generar el archivo JSON
function generateProjectsJSON() {
    const projects = [];

    // Leer los archivos de la carpeta de proyectos
    const projectFiles = fs.readdirSync(projectsDir);
    projectFiles.forEach(file => {
        const projectName = path.basename(file, path.extname(file));
        const projectHTML = `/projects/${file}`;
        const projectVideo = `/videos/${projectName}.mp4`;

        projects.push({
            titulo: projectName,
            link: projectHTML,
            video: projectVideo
        });
    });

    // Guardar la lista de proyectos en un archivo JSON
    fs.writeFileSync(outputFile, JSON.stringify(projects, null, 2));
    console.log('Archivo proyectos.json generado con éxito.');
}

generateProjectsJSON();