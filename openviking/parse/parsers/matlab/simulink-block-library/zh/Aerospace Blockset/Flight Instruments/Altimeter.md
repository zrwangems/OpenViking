---
type: simulink-block
title: 'Altimeter'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'altimeter'
documentation_source_path: 'altimeter.html'
language: zh-CN
chinese_source: worker-translation
---

# Altimeter

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 连接到信号 信号名称
  group: ''
- name: Label
  summary: 模块标签位置 Top（默认）| Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — 连接到信号 信号名称

连接到要显示的信号，从信号名称列表中选择。

要查看信号的数据，请在模型中选择一个信号。该信号将出现在 **Connection** 表格中。选中要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

表格中有一行用于显示连接到该模块的信号。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则表格为空。

### **Label** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签，显示在模块顶部或底部，或隐藏。

- `Top`

  在模块顶部显示标签。
- `Bottom`

  在模块底部显示标签。
- `Hide`

  当模块未连接时，不显示标签或说明文本。

#### 编程使用

|  |
| --- |
| **模块参数**：`LabelPosition` |
| **类型**：字符向量 |
| **值**：`'Top'` | `'Bottom'` | `'Hide'` |
| **默认值**：`'Top'` |
## 所属库

Aerospace Blockset / Flight Instruments

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块在代码生成时被忽略。

## 版本历史

**在 R2016a 中引入**

## 描述

显示飞机高度的测量值

Altimeter Indicator 模块以英尺为单位显示海平面以上的高度，也称为气压高度。该模块通过仪表上的指针和数字指示器显示高度值。

- 仪表有 10 个主刻度。每个主刻度内有五个次刻度。
  该仪表有三个指针。使用这些指针，高度表只能准确显示 0 到 100,000 英尺之间的高度。

  - 对于最长的指针，一个小刻度增量代表 20 英尺，一个大刻度代表 100 英尺。
  - 对于第二长的指针，一个小刻度代表 200 英尺，一个大刻度代表 1,000 英尺。
  - 对于最短的指针，一个小刻度代表 2,000 英尺，一个大刻度代表 10,000 英尺。
- 对于数字显示，该模块以 0 到 9,999 英尺之间的数字字符显示值。当数字显示值达到 10,000 英尺时，仪表将该值显示为低于 10,000 英尺的剩余值。例如，12,345 英尺显示为 2,345 英尺。当值小于 0（低于海平面）时，该模块显示 `0`。指针显示相应的值，除非值低于海平面或超过 100,000 英尺。低于海平面时，指针设置为 `0`；超过 100,000 时，指针保持在 100,000。

**提示**

为了便于理解和调试您的模型，您可以在正常和加速模式仿真期间修改模型中的仪表模块连接。
