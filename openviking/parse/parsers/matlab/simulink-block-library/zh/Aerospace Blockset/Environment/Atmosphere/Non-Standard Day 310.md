---
type: simulink-block
title: 'Non-Standard Day 310'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'nonstandardday310'
documentation_source_path: 'nonstandardday310.html'
language: zh-CN
chinese_source: worker-translation
---

# Non-Standard Day 310

## 端口

### 输入

### **Port\_1** — 位势高度 标量 | 数组

位势高度，指定为标量或数组，采用指定的单位。

**数据类型：** `double`
### 输出

### **Port\_1** — 温度 标量 | 数组

温度，指定为标量或数组，采用指定的单位。

**数据类型：** `double`

### **Port\_2** — 声速 标量 | 数组

声速，指定为标量或数组，采用指定的单位。

**数据类型：** `double`

### **Port\_3** — 空气压力 标量 | 数组

空气压力，指定为标量或数组，采用指定的单位。

**数据类型：** `double`

### **Port\_4** — 空气密度 标量 | 数组

空气密度，指定为标量或数组，采用指定的单位。

**数据类型：** `double`

## 参数

### **单位** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 高度 | 温度 | 声速 | 空气压力 | 空气密度 |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Kelvin | Meters per second | Pascal | Kilograms per cubic meter |
| `English (Velocity in ft/s)` | Feet | Degrees Rankine | Feet per second | Pound-force per square inch | Slug per cubic foot |
| `English (Velocity in kts)` | Feet | Degrees Rankine | Knots | Pound-force per square inch | Slug per cubic foot |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **规范** — 大气模型类型 `1976 COESA-extended U.S. Standard Atmosphere`（默认） | `MIL-HDBK-310` | `MIL-STD-210C`

大气模型类型，指定为 `1976 COESA-extended U.S. Standard Atmosphere`、`MIL-HDBK-310` 或 `MIL-STD-210C`。对于 `MIL-HDBK-310` 和 `MIL-STD-210C` 选项：

|  |  |
| --- | --- |
| `MIL-HDBK-310` | 此选择链接到 Non-Standard Day 310 模块。有关详细信息，请参阅模块参考。选择 `MIL-HDBK-310` 会启用参数 **大气模型类型**、**极端参数**、**出现频率** 和 **极值高度**。 |
| `MIL-STD-210C` | 此选择链接到 Non-Standard Day 210C 模块。有关详细信息，请参阅模块参考。选择 `MIL-HDBK-310` 会启用参数 **大气模型类型**、**极端参数**、**出现频率** 和 **极值高度**。 |

#### 依赖关系

为 **规范** 参数选择 `MIL-HDBK-310` 或 `MIL-STD-210C` 会启用以下参数：

- **大气模型类型**
- **极端参数**
- **出现频率**
- **极值高度**

#### 编程使用

|  |
| --- |
| **模块参数**: `spec` |
| **类型**: character vector |
| **值**: `'1976 COESA-extended U.S. Standard Atmosphere'` | `'MIL-HDBK-310'` | `'MIL-STD-210C'` |
| **默认值**: `'1976 COESA-extended U.S. Standard Atmosphere'` |

### **大气模型类型** — 模型类型 `Profile`（默认） | `Envelope`

大气模型类型的表示形式，指定为：

|  |  |
| --- | --- |
| `Profile` | 与指定高度处的极值相关的真实大气剖面。推荐用于垂直穿越大气层的飞行器仿真，或需要大气总影响时。 |
| `Envelope` | 使用每个高度处的极端大气值。推荐用于仅水平穿越大气层且高度变化不大的飞行器。 |

#### 依赖关系

- 为 **规范** 参数选择 `MIL-HDBK-310` 或 `MIL-STD-210C` 会启用此参数。
- 选择 `Profile` 会启用 **极值高度** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**: `model` |
| **类型**: character vector |
| **值**: `'Profile'` | `'Envelope'` |
| **默认值**: `'Profile'` |

### **极端参数** — 模型类型 `High temperature`（默认） | `Low temperature` | `High density` | `Low density` | `High pressure` | `Low pressure`

作为极值的大气参数。

#### 依赖关系

- 为 **规范** 参数选择 `MIL-HDBK-310` 或 `MIL-STD-210C` 会启用此参数。
- `High pressure` 和 `Low pressure` 选项仅在 **大气模型类型** 设置为 `Envelope` 时出现。

#### 编程使用

|  |
| --- |
| **模块参数**: `profile_var` |
| **类型**: character vector |
| **值**: `'High temperature'` | `'Low temperature'` | `'High density'` | `'Low density'` | `'High pressure'` | `'Low pressure'` |
| **默认值**: `'High temperature'` |

### **出现频率** — 模型类型 `1%`（默认） | `Extreme values` | `5%` | `10%` | `20%`

这些值出现的时间百分比。

#### 依赖关系

- 为 **规范** 参数选择 `MIL-HDBK-310` 或 `MIL-STD-210C` 会启用此参数。
- `Extreme values`、`5%` 和 `20%` 仅在为 **大气模型类型** 选择 `Envelope` 时可用。
- `1%` 和 `10%` 始终可用。

#### 编程使用

|  |
| --- |
| **模块参数**: `profile_percent` |
| **类型**: character vector |
| **值**: `'Extreme values'` | `'1%'` | `'5%'` | `'10%'` | `'20%'` |
| **默认值**: `'1%'` |

### **极值高度** — 几何高度 `5 km (16404 ft)`（默认） | `10 km (32808 ft)` | `20 km (65617 ft)` | `30 km (98425 ft)` | `40 km (131234 ft)`

极值出现处的几何高度，指定为 `5 km (16404 ft)`、`10 km (32808 ft)`、`20 km (65617 ft)`、`30 km (98425 ft)` 或 `40 km (131234 ft)`。

#### 依赖关系

如果 **大气模型类型** 设置为 `Profile`，则会出现此参数。

#### 编程使用

|  |
| --- |
| **模块参数**: `profile_alt` |
| **类型**: character vector |
| **值**: `5 km (16404 ft)` | `10 km (32808 ft)` | `20 km (65617 ft)` | `30 km (98425 ft)` | `40 km (131234 ft)` |
| **默认值**: `40 km (131234 ft)` |

### **超出范围输入的操作** — 超出范围模块行为 `None`（默认） | `Warning` | `Error`

超出范围模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在 Diagnostic Viewer 中发出警告，模型仿真继续。 |
| `Error`（默认） | 在 Diagnostic Viewer 中发出错误，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

## 所属库

Aerospace Blockset / Environment / Atmosphere

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现 MIL-HDBK-310 气候数据

Non-Standard Day 310 模块针对输入位势高度，实现 MIL-HDBK-310 全球空气环境气候数据的一部分，最高至 80 km（几何高度或约 262,467 英尺几何高度），用于绝对温度、压力、密度和声速。

COESA Atmosphere Model、Non-Standard Day 210C 和 Non-Standard Day 310 模块是相同的模块。当配置为 COESA Atmosphere Model 时，该模块实现 COESA 数学表示。当配置为 Non-Standard Day 210C 时，该模块实现 MIL-STD-210C 气候数据。当配置为 Non-Standard Day 310 时，该模块实现 MIL-HDBK-310 气候数据。

COESA Atmosphere Model 模块的端口标签会根据从 **单位** 列表中选择的输入和输出单位而变化。
