---
type: web_source
source_url: "https://vibe-hub.org/npm"
title: "npm"
language: zh
category: "npm"
fetched_at: 2026-07-27T10:04:15+00:00
---
前端后端产品技术栈AIGit设计风格

复制为 Markdown已复制

←终端命令行构建→

# npm

你可能会说

AI 让我先“装依赖”，敲了一行命令就哗啦啦下载一堆东西，这是在干嘛？

**npm 是安装、管理和运行 JavaScript 项目依赖与脚本的包管理工具**·npm 根据 package.json 和锁文件安装依赖，也能运行项目脚本。npm install 通常会创建 node\_modules，并可能更新锁文件；持续集成中常用 npm ci 严格按现有锁文件安装。运行前要确认项目目录，陌生依赖还可能执行安装脚本。

先知道

[终端命令行 **Terminal**](/terminal)

也常被叫作*包管理**Node 包管理*

package.json · 清单
**"react"**: "^19.0.0"
**"vite"**: "^6.0.0"
**"scripts"**: dev / build

npm  
install  
→

node\_modules · 依赖目录
📦 react
📦 vite
📦 …共 42 个包

### 什么时候用

- **package.json 是清单**：记录项目名称、依赖范围和可运行脚本

  package.json  
  **"dependencies"**: react, vite  
  **"scripts"**: dev, build清单：装了哪些包、能跑哪些命令
- clone 项目后运行 **npm install**，按 package.json 和锁文件恢复声明的依赖

  **$** **npm install**⸨░░░░░░⸩ idealTreeadded 42 packages in 6s
- **npm run dev**：跑 scripts 里写好的快捷命令

  **$** **npm run dev**> vite✓ Ready in 1.2s
- **克隆别人的项目先 install**：根据清单和锁文件重建依赖目录

  ☁️ 克隆项目→ install →📦 仓库重建

### 什么时候不用

- 不要直接修改 node\_modules，重新安装依赖时改动会丢失

  📁 node\_modules / react✎ 手动改

  重新安装依赖时，这类本地改动通常会被替换
- 不要把 node\_modules 提交进 Git，它可以根据配置重新安装

  node\_modules 380MBgit push →

  大量可重新安装的依赖进入仓库，应由 .gitignore 排除
- 删掉 **package.json**：依赖和脚本声明丢失，其他环境无法按项目配置重建

  📄 package.json🗑
- 没有定位报错原因就安装多个包，会增加依赖冲突和排查范围

  dependencies:  
  react, vue, jquery, lodash, moment, axios, fetch-huh…

组成结构 · Anatomy

{
  **"name"**: "my-first-page",
  **"dependencies"**: { "react": "^19.0.0" },
  **"scripts"**: { "dev": "vite", "build": "vite build" }
}

1项目名name项目的名字和版本，发布、分享时用到

2依赖清单dependencies装了哪些包、什么版本；install 就照它搬货

3快捷命令scriptsnpm run dev 跑的就是这里写的命令

常见变体 · Variants

安装install

npm install

装新包，或重建 node\_modules

运行脚本run

npm run dev

执行 scripts 里的快捷命令

卸载uninstall

npm uninstall lodash

包用不上了，从清单划掉

锁版本lockfile

package-lock.json

团队统一版本，别手动改它

典型使用场景

package.json 清单示例

package.json

{  
  "name": "my-first-page",  
  "dependencies": { "react": "^19.0.0" },  
  "scripts": { "dev": "vite", "build": "vite build" }  
}

npm install 安装依赖

zsh — my-first-page

**$** **npm install**
⸨████████░░⸩ reify: react
added 42 packages in 6s
依赖会按 package.json 和锁文件安装到 node\_modules

不直接修改 node\_modules

my-first-page

📁 node\_modules380 MB · ⚠ 自动生成，勿动

📄 package.json清单

📄 .gitignore里面写着 node\_modules 和 .env

npm run dev 启动开发服务

zsh — my-first-page

**$** **npm run dev**
> my-first-page@0.1.0 dev
✓ Ready in 1.2s → http://localhost:3000
scripts 里的快捷命令，一条顶一串

延伸阅读 · 权威出处

[包管理基础MDN ↗](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_tools/Package_management)
