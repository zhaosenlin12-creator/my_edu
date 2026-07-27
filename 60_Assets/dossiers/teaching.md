---
type: dossier
status: active
domain: teaching
audience: self
local_path: C:\教案
related: "[[30_Teaching/index]]"
updated_at: 2026-07-27
tags: teaching,dossier,ursina,python,k12,project-based
---

# Dossier · 教学体系（C:\教案）

> 这是我从 C:\教案 下 18 个分类目录 + 25年寒假创赛营 7 天教案 + 坦克大战项目 + arcade / python 社团 / 比赛文件读到的事实。

## 一句话
**面向小学高年级到初中的项目式编程课程**，按“单元编号（1-120）+ 项目主题”组织，已落地的项目包括 3D 动作闯关（Ursina）、坦克大战、Arcade 平台游戏、AI 单元、网络编程、数据处理等，每门课都有 starter / complete 两套代码 + 教案 + 资源。

## 顶层目录（18 个）
| 目录 | 范围 |
|---|---|
| 艺术编程（1-10） | 艺术向入门 |
| 人机对话（11-20） | 聊天 / 交互 |
| 动画和交互（21-30） | 动效 |
| 创意编程（31-40） | 创意项目 |
| 图像处理（41-50） | OpenCV / Pillow |
| 音频处理（51-60） | 音频 / 音乐编程 |
| 游戏开发入门（61-70） | Pygame / Arcade |
| 3D编程（71-80） | Ursina / Panda3D |
| 加密算法（81-90） | 加解密 |
| 网络编程（91-100） | requests / socket |
| 数据处理（101-110） | pandas / numpy |
| 人工智能单元（111-120） | AI 入门 |
| 25年寒假创赛营 | 寒假 7 天项目营 |
| arcade_tiled | Tile 平台游戏素材包 |
| arcade的项目 | 学生作品归档 |
| python社团 | 社团长期课 |
| 比赛文件 | 比赛素材与提交模板 |
| 人工创新大赛 | 创新比赛项目 |

## 旗舰课程 · 25年寒假创赛营 · 3D 动作闯关（七天）
来源：C:\教案\25年寒假创赛营\adventure_game_course - 备份\day1-day7
- 适合对象：有 Python 基础的初中生（变量 / 函数 / 类）
- 技术栈：Python 3.8+ / Ursina Engine 5.x-8.x / Kenney Graveyard Kit
- 评选权重：完成度 40% / 创意 30% / 代码 15% / 展示 15%
- 课时：每天 2 小时 × 7 天

### 七天课程安排
| 天 | 主题 | 核心 | 阶段成果 |
|---|---|---|---|
| Day1 | 🌍 3D 世界初探 | Ursina 引擎 + 3D 坐标 + 场景搭建 | 看到 3D 墓地场景 |
| Day2 | 🧑 玩家角色 | 模型加载 + WASD 移动 + 相机跟随 | 能控制角色移动 |
| Day3 | 👾 敌人来袭 | 敌人 AI + 追踪算法 + 状态机 | 敌人会追踪玩家 |
| Day4 | ⚔️ 战斗系统 | 攻击判定 + 伤害计算 + 血量 UI | 能攻击 / 受伤 |
| Day5 | 🎁 道具与波次 | 道具系统 + 波次生成 + 计分 | 完整游戏循环 |
| Day6 | 👹 Boss 战 | Boss 设计 + 技能系统 + 特效 | 可挑战 Boss |
| Day7 | 🎨 个性化与展示 | 自由创作 + 优化打磨 + 作品展示 | 最终作品评选 |

### 真实代码结构（来自 Day1 教案）
- 项目结构：`adventure_game_course/day{1-7}/{starter, complete}/main.py`，**必须从 adventure_game_course 目录运行**
- 关键设置：`app = Ursina(title=..., asset_folder=course_root)` + `application.asset_folder = Path(course_root)`（Ursina 8.x 必须额外设置）
- 模型路径：`MODEL_PATH = 'assets/models/graveyard_temp/Models/GLB format/'`
- Day3 状态机：`idle → chase → attack`，循环条件 `distance_to < detect_range / attack_range`
- 敌人类型：Zombie（血厚）/ Skeleton（血少）/ Slime（几何体）/ Vampire（速度快）

### Kenney 模型清单（来自 README）
- 角色：character-keeper / character-zombie / character-skeleton / character-vampire / character-ghost
- 树木：pine / pine-crooked
- 墓碑：gravestone-cross / gravestone-round
- 装饰：pumpkin / rocks
- 武器：shovel

### Ursina 速查（来自运行说明附录）
- 模型加载失败回退：`os.path.exists` + 备用模型 'cube'
- 始终面向相机：`billboard=True`
- 平滑移动：`time.dt * speed` 或 `lerp(player.x, target_x, time.dt * 5)`
- 鼠标点击检测：`if key == 'left mouse down' and mouse.hovered_entity:`
- 性能建议：对象池 / 简单碰撞体（box > sphere > mesh）/ 及时 destroy 粒子 / 间隔计算（每 0.1 秒）

## 坦克大战（25年寒假创赛营/tank_battle_v2-w）
- 7 天完整教案 day1-day7
- 企业级升级方案：`tank_battle_v2-w\升级方案.md`（1015 字节）+ 提示词 + 修改 package.py 打包脚本
- 主题：长江江豚保护（competition_theme_01_yangtze_porpoise）/ 三峡救援 / 火星探险
- 粒子系统开发计划：`md/PARTICLE_SYSTEM_DEVELOPMENT_PLAN.md`
- 资源：kenney_pico-8-city 像素素材

## 网络爬虫与文档处理
- C:\kaifa\Scrapling 是学生/教师向 Python 抓取库（项目卡见 [[20_Projects/Scrapling]]）
- C:\kaifa_boot\firecrawl 是 firecrawl 项目的本地参考

## 学员作品 / 团队产出
- C:\kaifa_senlin\airi（项目卡见 [[20_Projects/airi]]）
- C:\kaifa_senlin\promits、\soccer-game、\soccer-game-landscape
- C:\kaifa_senlin\yichang_travel、\yichang_travel-main、\world_website（教学与商业并行）
- C:\kaifa_teacher\food-web / senlin_website / xiangmin1_website / xiangmin_website / yangtao（学员作品镜像）

## 真实风险与卡点
- 同一课程有 `adventure_game_course` / `adventure_game_course - 备份` / `adventure_game_course - 详细版完整备份` / `adventure_game_coursew` 四个目录并存，结构基本一致，命名混乱
- 寒创赛营 README 中并没有标注“运行环境 / 推荐 Python 版本 / GPU 要求”，只写了 Python 3.8+
- 一些 day 教案在“完整版备份”里更详细（Day1 1387 字节 vs 详细版完整备份 1181 字节）
- Ursina 8.x 的 `application.asset_folder` 必须在创建 Entity 之前设置
- 模型路径对目录结构依赖很强（必须从 adventure_game_course 根目录运行）
- 比赛文件目录里没有 README，需要先清点

## 我从这里学到的能力
- 把课程拆成 1-120 号的“单元体系”，便于进度管理
- 7 天创客营的节奏：环境→核心机制→扩展→作品化（与 LIVE SOP 的 6 轮结构思路一致）
- 项目代码三套：starter / complete / final，给学生不同入口
- 真实模型 + 真实素材包（Kenney）+ 真实游戏循环（追逐 / 战斗 / 道具 / Boss）
- 用状态机 + 距离检测 + 波次生成做完整 AI

## 下一步可做
- [ ] 把 `adventure_game_course` / `adventure_game_course - 备份` / 详细版 / w 合并成一个
- [ ] 抽出每门课的 README 模板（适合对象 / 时长 / 资源 / 评估）
- [ ] 把 Kenney 模型清单做成 60_Assets/teaching-assets.md
- [ ] 把 Ursina 速查做成 30_Teaching/ursina-cheatsheet.md
- [ ] 把 day1-day7 教案重写成 Obsidian 卡 + 留 starter/complete 链接