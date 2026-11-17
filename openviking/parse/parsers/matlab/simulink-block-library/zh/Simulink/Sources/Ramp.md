---
type: simulink-block
title: 'Ramp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'ramp'
documentation_source_path: 'slref/ramp.html'
language: zh-CN
chinese_source: worker-translation
---

# Ramp

## 端口

### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

生成的输出斜坡信号，由 **Slope**、**Start time** 和 **Initial output** 参数决定其特征。

**数据类型：** `double`

## 参数

### **Slope** — 信号的斜率 1（默认）| 标量 | 向量 | 矩阵

指定所生成信号的变化率。

#### 程序化使用

|  |
| --- |
| **模块参数：** `slope` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'1'` |

### **Start time** — 输出开始的时间 0（默认）| 标量

指定模块开始生成信号的时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `start` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

### **Initial output** — 输出信号的初始值 0（默认）| 标量 | 向量 | 矩阵

指定输出信号的初始值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Slope**、**Start time** 或 **Initial output** 参数求值为 `N` 元素的行向量或列向量，选中此复选框可输出长度为 `N` 的向量。

- 选中此复选框时，如果 **Slope**、**Start time** 或 **Initial output** 参数求值为 `N` 元素的行向量或列向量，模块将输出长度为 `N` 的向量。例如，模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 清除此复选框时，如果 **Slope**、**Start time** 或 **Initial output** 参数求值为 `N` 元素的行向量或列向量，模块不会输出长度为 `N` 的向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VectorParams1D` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认：** `'on'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成持续递增或递减的信号

Ramp 模块生成一个在指定时间以指定值开始并以指定速率变化的信号。该模块的 **Slope**、**Start time** 和 **Initial output** 参数决定输出信号的特征。在标量扩展后，所有参数必须具有相同的维度。
