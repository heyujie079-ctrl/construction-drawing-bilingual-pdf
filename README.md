# Construction Drawing Bilingual PDF / 施工图中英双语 PDF

A Codex skill for translating Chinese construction, shop, millwork, furniture, and retail-display drawing PDFs into bilingual Chinese-English drawings while preserving the original geometry and dimensions.

用于将中文施工图、深化图、木作图、家具图及商业展示图翻译为中英双语 PDF 的 Codex Skill。处理过程保留原图、中文和 mm 尺寸，并在主要尺寸附近添加四舍五入后的整数 inch 标注。

## Features / 功能

- Preserves the original PDF, Chinese annotations, page size, title block, and all mm dimensions.  
  保留原始 PDF、中文标注、页面尺寸、标题栏及全部 mm 尺寸。
- Adds concise professional English translations in blue near the corresponding Chinese text.  
  在对应中文附近添加简洁、专业的蓝色英文翻译。
- Works from the perspective of a senior construction and retail-display designer, using professional drafting, fabrication, installation, material, finish, hardware, and lighting terminology instead of conversational or literal machine translation.
  以资深施工图及商业空间设计师的专业视角处理翻译，使用符合制图、制作、安装、材料、饰面、五金和照明行业习惯的专业用词，避免口语化及生硬直译。
- Converts major and useful dimensions with `inch = mm / 25.4` and half-up whole-number rounding.  
  按 `inch = mm / 25.4` 换算主要尺寸，并采用四舍五入得到整数 inch。
- Keeps inch labels close to their matching mm values.  
  inch 标注紧邻其对应的 mm 数值。
- Uses render-based visual review to prevent overlays from covering text, dimensions, leaders, or drawing geometry.  
  通过逐页渲染检查，避免新增内容遮挡文字、尺寸、引线或图线。

## Font preset / 字体规范

For a `11906 x 8419 pt` drawing sheet:

针对 `11906 x 8419 pt` 的大型图纸页面：

| Content / 内容 | Typeface / 字体 | PDF size / PDF 字号 |
|---|---|---:|
| Main or top English notes / 顶部主要英文备注 | Helvetica | about / 约 `200 pt` |
| Other English translations / 其他英文翻译 | Helvetica | about / 约 `120 pt` |
| Inch labels / inch 标注 | Helvetica | about / 约 `100 pt` |

For other page sizes, all three sizes are scaled by the same page-size ratio. Text is moved, wrapped, or shortened before any font reduction is considered.

其他页面尺寸按相同比例缩放以上三档字号。若空间不足，优先移动、换行或精简文字，最后才考虑小幅缩小字号。

## Installation / 安装

Clone the repository into the Codex skills directory:

将仓库克隆到 Codex Skills 目录：

```powershell
git clone https://github.com/heyujie079-ctrl/construction-drawing-bilingual-pdf.git "$env:USERPROFILE\.codex\skills\construction-drawing-bilingual-pdf"
```

Restart Codex after installation if the skill is not discovered immediately.

如果 Codex 未立即识别该 Skill，请重启 Codex。

## Usage / 使用方法

Example request in Chinese:

中文调用示例：

```text
使用 $construction-drawing-bilingual-pdf 翻译这份施工图。保留中文和 mm，在主要尺寸旁添加四舍五入后的 inch，并确保英文和 inch 不遮挡图线或标注。
```

Example request in English:

英文调用示例：

```text
Use $construction-drawing-bilingual-pdf to create a bilingual Chinese-English version of this drawing. Preserve all mm dimensions, add rounded whole-inch labels beside major dimensions, and keep every overlay clear of the source drawing.
```

## Workflow / 工作流程

1. Render and inspect every source page. / 渲染并检查每一页源图。
2. Identify translation targets, major dimensions, and nearby blank space. / 识别翻译对象、主要尺寸及附近空白区域。
3. Translate technical notes with concise drafting terminology. / 使用简洁的工程制图术语翻译技术说明。
4. Calculate whole-inch equivalents using half-up rounding. / 采用四舍五入计算整数 inch。
5. Add vector overlays without modifying the source geometry. / 添加矢量覆盖层，不修改原始图形。
6. Re-render full pages and dense crops, then correct all collisions. / 重新渲染整页和密集区域，修正所有遮挡。
7. Verify page count, page size, readability, and representative overlay text. / 校验页数、页面尺寸、可读性及代表性英文文本。

## Layout priorities / 排版优先级

1. Never cover Chinese text, mm values, dimension lines, leaders, symbols, geometry, or title-block content.  
   不得遮挡中文、mm 数值、尺寸线、引线、符号、图线或标题栏。
2. Place each inch label directly above, below, left, or right of its matching mm value.  
   每个 inch 必须放在对应 mm 数值的上、下、左或右侧。
3. Place English below its Chinese callout when possible; otherwise use the nearest clear space.  
   英文优先放在中文下方；空间不足时使用最近的无干扰空白区。
4. Omit a non-essential inch conversion rather than obstruct the drawing.  
   宁可省略非关键 inch，也不能遮挡原图。

## Repository structure / 仓库结构

```text
construction-drawing-bilingual-pdf/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   └── layout-rules.md
└── scripts/
    └── mm_to_inch.py
```

Detailed placement and QA requirements are maintained in [`references/layout-rules.md`](references/layout-rules.md).  
详细排版和质量检查规则见 [`references/layout-rules.md`](references/layout-rules.md)。
