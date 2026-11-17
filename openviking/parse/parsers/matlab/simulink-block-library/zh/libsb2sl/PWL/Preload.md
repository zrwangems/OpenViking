---
type: simulink-block
title: 'Quantizer'
family: 'simulink-extras'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'quantizer'
documentation_source_path: '../simulink/slref/quantizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizer

## 端口

### 输入

### **Port\_1** — 要量化的输入信号 标量 | 向量

量化算法的输入信号。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 量化后的输出信号 标量 | 向量

由离散值组成的输出信号，采用四舍五入方法进行量化：

```
y = q * round(u/q)
```

其中 `y` 是输出，`u` 是输入，`q` 是**量化间隔**。

**数据类型：** `single` | `double`

## 参数

### **Quantization interval** — 定义输出信号量化级别的间隔 `0.5`（默认）| 标量 | 向量

指定算法中使用的量化间隔。Quantizer 模块输出的量化级别是**量化间隔**的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`QuantizationInterval` |
| **类型**：character vector |
| **Value**: Any real or complex value |
| **默认值**：`'0.5'` |

### **Treat as gain when linearizing** — 指定增益值 `on`（默认）| `off`

Simulink® 软件中的线性化命令将此模块视为状态空间中的增益。选中此参数可使这些命令将增益视为 1。清除此参数可使这些命令将增益视为 0。

#### 编程使用

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：character vector |
| **Value**: `'off'` | `'on'` |
| **默认值**：`'on'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"` (default) | scalar or vector in quotes |

## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

按给定间隔对输入进行离散化

Quantizer 模块使用量化算法对输入信号进行离散化。该模块使用四舍五入方法将信号值映射到输出端由**量化间隔**定义的量化值。平滑的输入信号在量化后可能呈现阶梯形状。

此方程在数学上描述了四舍五入方法：

```
y = q * round(u/q)
```

其中 `y` 是量化后的输出，`u` 是输入，`q` 是**量化间隔**。
