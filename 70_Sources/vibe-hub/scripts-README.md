# VibeHub 本地镜像启动脚本

这里放了三个一键脚本，方便手动开/关 vibe-hub.org 的本地浏览器镜像（`site/` 目录，1030 个文件，42 MB）。

## 用法

### 1. 启动：`start-server.bat`

- 先杀掉端口 8765 上已有进程（避免冲突）
- 用 Python 内置 `http.server` 在后台启动（最小化窗口）
- 自动打开浏览器到 http://localhost:8765/

**前提**：先跑过 `python mirror_site.py` 生成了 `site/` 目录。

### 2. 停止：`stop-server.bat`

杀掉端口 8765 上所有 LISTENING 进程。多次运行安全，没有就提示。

### 3. 重启：`restart-server.bat`

等于先 stop 再 start。

## 为什么不用 npm？

`site/` 是静态文件（HTML/CSS/JS/JSON/MP3），不需要构建、不需要依赖。Python 内置 http server 是最轻量的选择。

如果以后你装了 `npx serve` 或类似的工具，也可以用：

```powershell
npx serve C:\my_know\70_Sources\vibe-hub\site -l 8765
```

效果一样。

## 端口冲突怎么办？

如果 8765 被占用了，编辑三个 .bat 文件，把 `PORT` 改成别的（比如 8800、9000）。三个文件要同步改。

## 后台运行模式

`start-server.bat` 用 `start /MIN` 把 server 放在后台，关闭窗口也不会停。要彻底停就再跑 `stop-server.bat`。