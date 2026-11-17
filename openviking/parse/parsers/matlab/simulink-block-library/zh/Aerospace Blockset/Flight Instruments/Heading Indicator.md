---
type: simulink-block
title: 'Heading Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'headingindicator'
documentation_source_path: 'headingindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Heading Indicator

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
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — 连接到信号 信号名称

选择要显示的信号，从信号名称列表中选择。

要查看信号的数据，请在模型中选择一个信号。该信号将出现在 **Connection** 表格中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

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
| **类型**：character vector |
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

显示飞机航向的测量值

Heading Indicator 模块以度为单位显示飞机航向的测量值。

该模块表示 0 到 360 度之间的值。

**提示**

为了便于理解和调试您的模型，您可以在正常和加速模式仿真期间修改模型中的仪表模块连接。
