# Academic Paper Team Skill

一个可通过 Git 复用的 Codex 论文多智能体 Skill。它将论文工作拆分为九个可独立升级的角色，并通过稳定的文件契约完成规划、检索、写作、制图、排版、批注修改和回归检查。

## 安装

macOS / Linux：

```bash
git clone https://github.com/lfyin-ux/lunwenSkill.git ~/.codex/skills/academic-paper-team
```

Windows PowerShell：

```powershell
git clone https://github.com/lfyin-ux/lunwenSkill.git "$HOME\.codex\skills\academic-paper-team"
```

重启 Codex 后，可直接提出论文任务，或显式使用 `$academic-paper-team`。

## 更新

```bash
git -C ~/.codex/skills/academic-paper-team pull --ff-only
```

Windows PowerShell：

```powershell
git -C "$HOME\.codex\skills\academic-paper-team" pull --ff-only
```

## 初始化论文项目

```bash
python3 ~/.codex/skills/academic-paper-team/scripts/init_paper_project.py /absolute/path/to/my-paper
```

Windows PowerShell：

```powershell
py "$HOME\.codex\skills\academic-paper-team\scripts\init_paper_project.py" "C:\path\to\my-paper"
```

脚本只依赖 Python 3.9+ 标准库。

首先填写 `00-input/requirements.md` 与 `00-input/format-profile.yaml`，再让 Codex 使用该 Skill 工作。

## 单独优化角色

九个角色分别位于 `references/roles/`。优化某个角色时，应保持其 `Role contract` 中的角色标识、输入、输出、升级条件以及 `references/shared-contract.md` 规定的公共字段兼容。修改后运行 `python3 scripts/validate_contract.py .`。若必须变更公共契约，应在同一次提交中迁移所有受影响角色并提升契约版本。

## 角色列表

- `global-planner.md`：全局规划师
- `outline-architect.md`：目录师
- `research-data.md`：数据师
- `content-writer.md`：内容师
- `figure-designer.md`：画图师
- `format-specialist.md`：格式师
- `global-reviewer.md`：全局检查师
- `revision-manager.md`：论文修改师
- `revision-reviewer.md`：修改检查师

## 安全边界

本 Skill 不应被用于伪造文献、数据、引用、实验或调研结果。自动生成内容仍需遵守学校、期刊及研究机构的学术诚信与 AI 使用规定。
