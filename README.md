# senlin-knowledge-base · 个人知识库

> 这是森林的个人 Obsidian 知识库。
> 目的不是“记笔记”，而是让你和 AI 都能立刻知道：你有哪些能力、你有哪些项目、你下一步要往哪走。

## 这个库解决什么

- **我是谁** — 个人画像、能力图谱、定位、品牌、认证
- **我在哪** — 当前项目、教学、内容、产品、资产的实时快照
- **我要去哪** — 目标、里程碑、成长计划
- **快速找** — 自己搜得到，AI 也读得到；用 properties / 标签 / MOC 索引实现

## 目录（PARA + 编号地址）

- `00_Home` — 4 个首页 + 5 个模板 + 4 个 MOC 索引
- `10_Profile` — 个人画像、能力图谱、定位
- `20_Projects` — 每个项目一张卡（GitHub 仓库、直播项目、教学项目）
- `30_Teaching` — 教案、课堂案例、学员作品
- `40_Content` — 抖音 / 视频 / 文章 / 直播脚本 / 复盘
- `50_AI` — 提示词、Skills、工具评测、工作流
- `60_Assets` — 物料、模板、脚本、PPT、图片
- `80_Canvas` — 大图：能力地图 / 流水线 / 关系图
- `90_Archive` — 旧项目、历史快照

每个核心笔记都带这套 properties（统一格式，方便 AI 读）：

```
type:
status:        # active / draft / done / hold
domain:        # web / teaching / content / ai / game / system
audience:      # student / parent / teacher / maker / self
repo:
url:
summary:
next_action:
updated_at:    # YYYY-MM-DD
```

## 推荐插件（手动安装）

启动 Obsidian 后 → Settings → Community plugins → 浏览并打开：

- Dataview — 把每个 MD 当数据库查，用来画看板
- Excalidraw — 在 80_Canvas 画关系图
- Templater — 自动套用 `00_Home/_templates/`
- Tag Wrangler — 整理标签
- Git — 提交 / 拉取（默认自带）

## 与 GitHub 同步（必读）

本库在 `C:\my_know`，**默认不自动提交**。同步方式：

1. 在 GitHub 创建一个空仓库（不要勾 README / .gitignore / License）。建议仓库名：
   - `senlin-knowledge-base`（公开）或 `senlin-knowledge-private`（私有）
2. 把仓库 URL 告诉我，我会一次性：
   - `git init`
   - 加 `.gitignore`（.obsidian/workspace、cache、plugins、trash 不入库）
   - 首次 commit + push
3. 之后每次本地更新 → 给我一句 “提交并同步” 即可

`.gitignore` 已经预备好：

```
# Obsidian workspace
.obsidian/workspace/
.obsidian/cache/
.obsidian/themes/
.obsidian/plugins/
.obsidian/log/

# 系统 / 备份
Thumbs.db
desktop.ini
~$*
```

## 怎么用（建议的工作流）

1. **每次开始**：打开 “00_Home/我是谁.md” 校准方向
2. **每周日晚上**：打开 “本周最重要的事.md”，复盘 + 写下周 3 件事
3. **新增项目**：复制 `00_Home/_templates/project.md` 一份到 `20_Projects/`
4. **新增一门课**：复制 `00_Home/_templates/teaching.md`
5. **新写完一个抖音脚本**：复制 `00_Home/_templates/content.md`
6. **新增一个 AI 工具**：复制 `00_Home/_templates/ai_tool.md`
7. **每两周**：整理 `90_Archive`，把不再用的沉到历史

## 与 Codex 的约定

让 Codex 帮我做事时，把它需要的信息直接放在以下几页：

- “我是谁” / “我在哪” / “我要去哪” / “本周最重要的事”
- `00_Home/MOCs/` 下面相关的索引
- 任务涉及的笔记本身（`20_Projects/*` / `30_Teaching/*` 等）

不要把教案、合同、token、密钥放进本库。敏感文件单独保存。

## License

个人观点 / 笔记默认保留。共享 / 转用需走我同意。
