---
type: simulink-block
title: 'Quantizer'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'quantizer'
documentation_source_path: 'slref/quantizer.html'
language: zh-CN
chinese_source: official
---

# Quantizer

## 端口

### 输入

### **Port\_1** — 要量化的输入信号 标量 | 向量

要应用量化算法的输入信号。

**数据类型:** `single` | `double`
**复数支持:** 是
### 输出

### **Port\_1** — 量化后的输出信号 标量 | 向量

输出信号由离散值组成，用舍入到最邻近整数方法量化：

```
y = q * round(u/q)
```

其中，`y` 是输出，`u` 是输入，`q` 是**量化区间**。

**数据类型:** `single` | `double`

## 参数

### **量化区间** — 定义输出信号量化级别的间隔 `0.5` (默认) | 标量 | 向量

指定算法中使用的量化间隔。Quantizer 模块输出的量化级别是**量化区间**的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数**：`QuantizationInterval` |
| **类型**：字符向量 |
| **值**：任何实数或复数值 |
| **默认值**：`'0.5'` |

### **线性化时视为增益** — 指定增益值 `on` (默认) | `off`

Simulink® 软件中的线性化命令将此模块视为状态空间中的增益。选择此参数将使得这些命令将增益视为 1。清除此参数可使命令将增益视为 0。

#### 编程用法

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

按给定间隔将输入离散化

Quantizer 模块使用量化算法离散化输入信号。该模块使用舍入到最邻近整数方法将信号值映射到由**量化区间**定义的输出端的量化值。平滑的输入信号在量化后可能会呈现阶梯形状。

以下方程用数学方法说明舍入到最邻近整数方法：

```
y = q * round(u/q)
```

其中，`y` 是量化输出，`u` 是输入，`q` 是**量化区间**。
