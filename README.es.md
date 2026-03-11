> [Ver en ingles/See in english](https://github.com/LuisMiSanVe/YT2MP/blob/main/README.md)
# 🎞️ YT2MP - YouTube A MP3/4
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

Extractor de videos de Youtube a formatos MP3 y MP4.

## 📋 Prerequisitos
Para abrir el programa e instalar las librerias necesarias, asegurate de tener [Python](https://www.python.org/) instalado.

## 🛠️ Instalación
Necesitas dos librerias para usar el programa, abre el CMD y pega este comando:
```
pip install yt-dlp
```

Dependiendo de la versión de Python, es posible que tengas que usar este comando en su lugar:
```
py -m pip install yt-dlp
```

Una vez instalado, descarga **FFmpeg**, puedes [compilar](https://www.ffmpeg.org/) su código fuente o [descargar](https://www.gyan.dev/ffmpeg/builds/) una version precompilada (recomendado).

Ahora, clona el script `YT2MP.pyw` en la misma carpeta que `ffmpeg.exe`.
Alternativamente, puedes añadir `ffmpeg.exe` dentro de tu PATH de Windows, para que puedas usar el script donde quieras.

Para ello (en Windows 11), ve a Configuración > Sistema > Información > Configuración avanazada del sistema > Variables de entorno > buscar por `Path` y dale a `Editar...` > Nuevo > copia la ruta de la carpeta en la que está `ffmpeg.exe` y dale click a `Aceptar`.

## 📂 Archivos
Los archivos MP3 o MP4 extraidos se guardarán en `Descargas` por defecto.

## 💻 Tecnologías usadas
- Lenguaje de programación: [Python](https://www.python.org/)
- Librerías:
  - [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  - [FFmpeg](https://www.ffmpeg.org/) (Binario compilado de [gyan.dev](https://www.gyan.dev/ffmpeg/builds/))
- IDE Recomendado: [VS Code](https://code.visualstudio.com/)