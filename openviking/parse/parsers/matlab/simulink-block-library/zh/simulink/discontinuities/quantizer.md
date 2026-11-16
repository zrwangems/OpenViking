---
type: simulink-block
title: 'Quantizer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Discontinuities'
documentation_page: 'quantizer'
documentation_source_path: 'slref/quantizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Quantizer

## 端口

### 输入

### **Port\_1** — 要量化的输入信号 标量 | 向量

输入到量化算法的信号。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 量化后的输出信号 标量 | 向量

由离散值组成的输出信号，使用舍入到最近值方法进行量化：

```
y = q * round(u/q)
```

其中 `y` 是输出，`u` 是输入，`q` 是**量化间隔**。

**数据类型：** `single` | `double`

## 参数

### **量化间隔** — 定义输出信号量化级别的间隔 `0.5`（默认）| 标量 | 向量

指定算法中使用的量化间隔。Quantizer 模块输出的量化级别是**量化间隔**的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数**: `QuantizationInterval` |
| **类型**: 字符向量 |
| **值**: 任意实数或复数值 |
| **默认值**: `'0.5'` |

### **线性化时视为增益** — 指定增益值 `on`（默认）| `off`

Simulink® 软件中的线性化命令会将此模块视为状态空间中的增益。选中此参数可使命令将增益视为 1。清除此参数可使命令将增益视为 0。

#### 编程用法

|  |
| --- |
| **模块参数**: `LinearizeAsGain` |
| **类型**: 字符向量 |
| **值**: `'off'` | `'on'` |
| **默认值**: `'on'` |

### **采样时间（-1 表示继承）** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当将此参数设置为 `-1` 以外的值时，此参数才可见。要了解详细信息，请参阅不建议指定采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"`（默认）| 带引号的标量或向量 |

## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

按给定间隔离散化输入

Quantizer 模块使用量化算法对输入信号进行离散化。该模块使用舍入到最近值方法将信号值映射到输出处由**量化间隔**定义的量化值。平滑的输入信号在量化后可能呈现阶梯形状。

此方程从数学上描述了舍入到最近值方法：

```
y = q * round(u/q)
```

其中 `y` 是量化后的输出，`u` 是输入，`q` 是**量化间隔**。
