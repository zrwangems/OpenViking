---
type: simulink-block
title: 'CIRA-86 Atmosphere Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'cira86atmospheremodel'
documentation_source_path: 'cira86atmospheremodel.html'
language: zh-CN
chinese_source: worker-translation
---

# CIRA-86 Atmosphere Model

## 端口

### 输入

### **Port\_1** — 纬度数组

包含以度表示的纬度（限制为 +/-80 度）。

**数据类型：** `double`

### **Port\_2** — 位势高度或压力数组

包含一个由以下任一项组成的 `m` 数组：

- 以所选长度单位表示的位势高度
  （**Coordinate type** 为
  `GPHeight`）
- 以所选压力单位表示的压力（**Coordinate
  type** 为 `Pressure`）

**数据类型：** `double`

### 输出

### **Port\_1** — 平均温度数组

平均温度，指定为数组，采用所选单位。

**数据类型：** `double`

### **Port\_2** — 压力或位势高度数组

`m` 数组，其中每项为以下之一：

- 以所选压力单位表示的压力（**Coordinate
  type** 为 `GPHeight`）
- 以所选长度单位表示的位势高度
  （**Coordinate type** 为
  `Pressure`）

**数据类型：** `double`

### **Port\_3** — 平均纬向风数组

平均纬向风，指定为数组，采用所选单位。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 高度 | 温度 | 声速 | 气压 | 空气密度 |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Kelvin | Meters per second | Pascal | Kilograms per cubic meter |
| `English (Velocity in ft/s)` | Feet | Degrees Rankine | Feet per second | Pound-force per square inch | Slug per cubic foot |
| `English (Velocity in kts)` | Feet | Degrees Rankine | Knots | Pound-force per square inch | Slug per cubic foot |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Coordinate type** — 坐标类型表示 `Pressure` (default) | `GPHeight`

坐标类型表示，指定为：

- `Pressure`

  表示以 pascal 为单位的压力。
- `GPHeight`

  表示以 meters 为单位的位势高度。

#### 编程用法

|  |
| --- |
| **模块参数**：`ctype` |
| **类型**：character vector |
| **值**：`'GPHeight'` | `'Pressure'` |
| **默认值**：`'GPHeight'` |

### **Mean value type** — 均值类型 `Monthly` (default) | `Annual`

均值类型，指定为：

- `Monthly`

  表示月度值。如果选择
  `Monthly`，还必须设置
  **Month** 参数。
- `Annual`

  表示年度值。当 **Coordinate
  type** 的值为
  `Pressure` 时有效。

#### 依赖关系

将此参数设置为 `Monthly` 会启用
**Month** 参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`mtype` |
| **类型**：character vector |
| **值**：`'Monthly'` | `'Annual'` |
| **默认值**：`'Monthly'` |

### **Month** — 均值的月份 `January` (default) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

取均值的月份。

#### 依赖关系

当 **Mean value type**
设置为 `Monthly` 时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`month` |
| **类型**：character vector |
| **值：** `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**：`'January'` |

### **Action for out-of-range input** — 超出范围的模块行为 `None` (default) | `Warning` | `Error`

超出范围的模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。 |
| `Error` (default) | 在诊断查看器中显示错误，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Environment / Atmosphere

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2023b：CIRA-86 Atmosphere Model 模块更新

CIRA-86 Atmosphere Model 模块已更新，以便当函数输入超出 CIRA 1986 模型限制时采取措施（请参阅“限制”）。

## 描述

实现 1986 CIRA 大气的数学表示

CIRA-86 Atmosphere Model 模块实现 1986 年空间研究委员会 (COSPAR) 国际参考大气 (CIRA) 的数学表示。该模块为输入的位势高度提供平均温度、压力和纬向风速值。

CIRA-86 Atmosphere Model 模块的端口标签会根据从 **Units** 列表中选择的输入和输出单位而变化。
