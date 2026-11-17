---
type: simulink-block
title: 'Turn Coordinator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'turncoordinator'
documentation_source_path: 'turncoordinator.html'
language: zh-CN
chinese_source: worker-translation
---

# Turn Coordinator

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Connection
  summary: 连接到信号 信号名称 | 二元素信号
  group: ''
- name: Label
  summary: 模块标签位置 Top（默认）| Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — 连接到信号 信号名称 | 二元素信号

连接到二元素信号以进行显示，从信号名称列表中选择。该二元素信号由转弯指示器和倾斜仪信号组成，在 Mux 模块中合并，单位为度。您连接并显示该合并信号。此输入不能是总线信号。

要查看信号中的数据，请在模型中选择一个信号。该信号会出现在 **Connection** 表中。选择要显示的信号旁边的选项按钮。点击 **Apply** 以连接该信号。

该表中有一行用于连接到该模块的信号。如果模型中没有选择任何信号，或者该模块未连接到任何信号，则该表为空。

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

## 版本历史

**在 R2016a 中引入**

## 描述

在转弯协调器和倾斜仪上显示测量值

Turn Coordinator 模块在陀螺转弯速率仪表和倾斜仪上显示测量值。

- 陀螺转弯速率仪表通过仪表中飞机符号的倾斜来显示飞机的航向变化率。
- 倾斜仪通过球的位置显示转弯是协调、侧滑还是滑移。

当球居中时，转弯是协调的。当球偏离中心时，转弯是侧滑或滑移。转弯速率仪表具有机翼水平和标准速率转弯的标记。标准速率转弯是每秒 3 度的航向变化，也称为两分钟转弯。

陀螺转弯速率仪表和倾斜仪的输入单位为度。转弯速率值作为仪表中飞机符号的倾斜度数输入。标准速率转弯标记位于 ±15 度的角度。倾斜角值限制为 ±20 度，而倾斜仪角度限制为 ±15 度。

按以下顺序在 Mux 模块中合并转弯指示器和倾斜仪信号：

1. 转弯指示器
2. 倾斜仪

例如，转弯指示器和倾斜仪值为 `[15 0]` 表示协调的标准速率转弯。

**提示**

为了便于理解和调试您的模型，您可以在正常和加速器模式仿真期间修改模型中的仪表模块连接。
