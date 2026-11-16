---
type: simulink-block
title: 'Digital Clock'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Sources'
documentation_page: 'digitalclock'
documentation_source_path: 'slref/digitalclock.html'
language: zh-CN
chinese_source: official
---

# Digital Clock

## 端口

### 输出

### **Port\_1** — 采样时间 标量

采用指定的采样间隔的采样时间（以秒为单位）。在其他时间，此模块保留输出的上一个值。

**数据类型:** `double`

## 参数

### **采样时间** — 采样间隔 `1` (默认) | 标量 | 向量

指定采样间隔（以秒为单位）。您可以通过以下两种方式之一指定采样间隔：

- 作为期间，指定为双精度数据类型的实数值标量。
- 作为期间和偏移量，指定为双精度数据类型的长度为 2 的实数值向量。期间和偏移量必须是有限非负值，并且偏移值必须小于期间。

有关详细信息，请参阅指定采样时间。

**提示**

不要指定连续采样时间 `0` 或 `[0,0]`。也不要指定 `-1`（继承采样时间），因为此模块是源。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'1'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含动态分配和释放内存、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

## 版本历史

**在 R2006a 之前推出**

## 描述

以指定的采样间隔输出仿真时间

Digital Clock 模块仅以指定的采样间隔输出仿真时间。在其他时间，此模块保留输出的上一个值。要控制此模块的精度，请使用模块对话框中的**采样时间**参数。

当您需要离散系统中的当前仿真时间时，请使用此模块，而不是 Clock 模块（它输出连续时间）。
