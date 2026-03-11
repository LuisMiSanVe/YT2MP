> [See in spanish/Ver en español](https://github.com/LuisMiSanVe/YT2MP/blob/main/README.es.md)
# 🎞️ YT2MP - YouTube To MP3/4
[![image](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

Youtube video extractor to either MP3 or MP4 format.

## 📋 Prerequisites
In order to open the program and install the required libraries, make sure you have [Python](https://www.python.org/) installed.

## 🛠️ Setup
You need two libraries to use the program, open a CMD and paste this command:
```
pip install yt-dlp
```

Depending on the Python version, you may have to use this command instead:
```
py -m pip install yt-dlp
```

Once is installed, download **FFmpeg**, you can [compile](https://www.ffmpeg.org/) it's source code or [downlaod](https://www.gyan.dev/ffmpeg/builds/) a precompiled version (recomended).

Now, clone the `YT2MP.pyw` script in the same folder as `ffmpeg.exe`.
Alternatively, you can add `ffmpeg.exe` inside your Windows PATH, so you can place the script whenever you want.

To do so (in Windows 11), go to Settings > System > Information > Advanced System configuration > Enviroment variables > Search for `Path` and click `Edit...` > New > copy the route to the folder where `ffmpeg.exe` is, then click `Accept`.

## 📂 Files
The extracted MP3 or MP4 files will be inside the `Downloads` folder by default.

## 💻 Technologies Used
- Programming Language: [Python](https://www.python.org/)
- Libraries:
  - [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  - [FFmpeg](https://www.ffmpeg.org/) ([gyan.dev](https://www.gyan.dev/ffmpeg/builds/)'s compiled binary)
- Recommended IDE: [VS Code](https://code.visualstudio.com/)
