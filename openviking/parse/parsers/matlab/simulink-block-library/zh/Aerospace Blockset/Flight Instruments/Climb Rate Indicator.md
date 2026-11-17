---
type: simulink-block
title: 'Climb Rate Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'climbrateindicator'
documentation_source_path: 'climbrateindicator.html'
language: zh-CN
chinese_source: worker-translation
---

# Climb Rate Indicator

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
- name: Maximum
  summary: 最大刻度值 4000（默认）| 有限值 | double | 标量
  group: ''
  block_parameter: MaximumRate
  type: 字符向量
  values: 标量
  default: '''4000'''
- name: Label
  summary: 模块标签位置 Top（默认）| Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: 字符向量
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — 连接到信号 信号名称

连接到信号以进行显示，从信号名称列表中选择。

要查看信号的数据，请在模型中选择一个信号。该信号将出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

表中包含连接到该模块的信号的行。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则表为空。

### **Maximum** — 最大刻度值 4000（默认）| 有限值 | double | 标量

最大刻度值，指定为有限的 double 标量值，单位为 ft/min。

最小刻度值始终为 `0`。

#### 编程使用

|  |
| --- |
| **模块参数**：`MaximumRate` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'4000'` |

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

显示飞机爬升率的测量值

Climb Rate Indicator 模块显示飞机爬升率的测量值，单位为 ft/min。

如果速度为正值，指针覆盖上半圆；如果爬升率为负值，指针覆盖下半圆。指示器的范围从 –**Maximum** 英尺每分钟到 **Maximum** 英尺每分钟。主刻度表示 **Maximum**/4。次刻度表示 **Maximum**/8 和 **Maximum**/80。

**提示**

为了便于理解和调试您的模型，您可以在正常和加速模式仿真期间修改模型中的仪表模块连接。
