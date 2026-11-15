---
type: simulink-block
title: 'NRLMSISE-00 Atmosphere Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Atmosphere'
documentation_page: 'nrlmsise00atmospheremodel'
documentation_source_path: 'nrlmsise00atmospheremodel.html'
language: zh-CN
chinese_source: worker-translation
---

# NRLMSISE-00 Atmosphere Model

## 端口

### 输入

### **Port\_1** — Geodetic latitudes, longitude, and altitude 三元组矩阵

大地纬度（以 degrees 为单位）、经度（以 degrees 为单位）和高度（以所选 length units 为单位），指定为三元组矩阵。

**数据类型：** `double`

### **Port\_2** — Years 数组

*N* 个年份，指定为数组。

**数据类型：** `double`

### **Port\_3** — Days 数组

一年中的 *N* 天（1 到 365（或 366）），指定为数组。

**数据类型：** `double`

### **Port\_4** — Seconds 数组

一天中的 *N* 秒，指定为数组，采用 universal time (UT)。

**数据类型：** `double`

### **Port\_5** — Local apparent solar time 数组

*N* 个 local apparent solar time，指定为数组，以 hours 为单位。

**数据类型：** `double`

### **Port\_6** — 81-day average F10.7 flux `150` (默认) | 数组

*N* 个 F10.7 通量的 81 天平均值，以一年中的第几天 (doy) 为中心，指定为数组。

**数据类型：** `double`

### **Port\_7** — Daily average F10.7 flux `150` (默认) | 数组

*N* 个前几日的每日 F10.7 通量，指定为数组。

**数据类型：** `double`

### **Port\_8** — Magnetic index information *N*-by-7 数组

Magnetic index information，指定为 *N*-by-7。如果指定 *magneticIndex*，还必须指定 *f107Average* 和 *f107Daily*。磁指数信息包含：

|  |
| --- |
| 每日磁指数 (AP) |
| 当前时间的 3 hour AP |
| 当前时间之前 3 hours 的 3 hour AP |
| 当前时间之前 6 hours 的 3 hour AP |
| 当前时间之前 9 hours 的 3 hour AP |
| 从当前时间之前 12 到 33 hours 的八个 3 hour AP 指数的平均值 |
| 从当前时间之前 36 到 57 hours 的八个 3 hour AP 指数的平均值 |

每日磁指数的影响在 80,000 m 以下不大或尚未确定。因此，该模块将默认值设置为 `4`。默认情况下，它将所有其他索引设置为 `0`。有关更多信息，请参阅 Limitations 中的限制。

**数据类型：** `double`

### **Port\_9** — Flags 数组（23）

Flags，指定为 21 的数组，用于启用或禁用输出的特定变化。

| 字段 | 描述 |
| --- | --- |
| `Flags(1)` | F10.7 对均值的影响 |
| `Flags(2)` | 与时间无关 |
| `Flags(3)` | 对称年变化 |
| `Flags(4)` | 对称半年变化 |
| `Flags(5)` | 非对称年变化 |
| `Flags(6)` | 非对称半年变化 |
| `Flags(7)` | 日变化 |
| `Flags(8)` | 半日变化 |
| `Flags(9)` | 每日 AP。如果将该字段设置为 -1，则该模块使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)` |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度 |
| `Flags(12)` | UT 和混合 UT、经度 |
| `Flags(13)` | 混合 AP、UT、经度 |
| `Flags(14)` | 三分之一日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 所有来自 120,000 meter 温度 (TLB) 的变化 |
| `Flags(18)` | 所有低热层 (TN1) 温度变化 |
| `Flags(19)` | 所有 120,000 meter 梯度 (S) 变化 |
| `Flags(20)` | 所有上平流层 (TN2) 温度变化 |
| `Flags(21)` | 所有来自 120,000 meter 值 (ZLB) 的变化 |
| `Flags(22)` | 所有低中间层温度 (TN3) 变化 |
| `Flags(23)` | 湍流层顶标高变化 |

**数据类型：** `double`

### 输出

### **Port\_1** — Temperature *N*-by-2 数组

温度值，以 *N*-by-2 的值数组返回，采用所选 temperature units。第一列包含外逸层温度，第二列包含高度处的温度。

**数据类型：** `double`

### **Port\_2** — Densities *N*-by-9 数组

密度值，以 *N*-by-9 数组返回，采用所选 density units。

| 密度 | 描述 |
| --- | --- |
| `Density(1)` | He 的密度 |
| `Density(2)` | O 的密度 |
| `Density(3)` | N2 的密度 |
| `Density(4)` | O2 的密度 |
| `Density(5)` | Ar 的密度 |
| `Density(6)` | 总质量密度 `Density(6)`，总质量密度，定义为 He、O、N2、O2、Ar、H 和 N 的质量密度之和。可选地，`Density(6)` 可以包括异常氧的质量密度，使 `Density(6)` 成为用于阻力的有效总质量密度。 |
| `Density(7)` | H 的密度 |
| `Density(8)` | N 的密度 |
| `Density(9)` | 异常氧数密度 |

**数据类型：** `double`

## 参数

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English`

输入和输出单位，指定为：

| 单位 | 温度 | 高度 | 密度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Kelvin | Meters | kg/m3，某些密度输出为 1/m3 |
| `English` | Rankine | Feet | lbm/ft3，某些密度输出为 1/ft3 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认**：`'Metric (MKS)'` |

### **输入当地视太阳时** — 视太阳时 `off` (默认) | `on`

选中此复选框以输入当地视太阳时，以 hours 为单位。否则，模块输入默认值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`1st input` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

### **输入通量和磁指数信息** — 前一日的每日 F10.7 通量和磁指数信息 `off` (默认) | `on`

选中此复选框以输入 F10.7 的 81 天平均值、前一日的每日 F10.7 通量，以及 7 个磁指数信息的数组（请参阅 `atmosnrlmsise00` 函数中的 `aph` 参数）。否则，模块为 F10.7 和 F10.7a 输入默认值 `150`，并为地磁指数输入 `[4, 0, 0, 0, 0, 0, 0]`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`flux_ap_input` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

### **标志来源** — 变化标志来源 `Internal` (默认) | `External`

变化标志来源，指定为 `Internal` 或 `External`。如果指定 `External`，请将变化标志指定为 23 的数组。如果指定 `Internal`，则标志来源在模块内部。

#### 依赖关系

将 **标志来源** 设置为 `Internal` 会启用 **标志** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`flags_input` |
| **类型**：character vector |
| **值**：`'Internal'` | `'External'` |
| **默认**：`'Internal'` |

### **标志** — 变化标志 `ones(1,23)` (默认)

变化标志，指定为 23 的数组（`ones(1,23)`）。此参数仅在 **标志来源** 的值为 `Internal` 时适用。您可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0

  移除该值对输出的影响。
- 1.0

  将该值的主效应和交叉项效应用于输出。
- 2.0

  仅将该值的交叉项效应用于输出。

该数组具有以下字段。

| 字段 | 描述 |
| --- | --- |
| `Flags(1)` | F10.7 对均值的影响 |
| `Flags(2)` | 与时间无关 |
| `Flags(3)` | 对称年变化 |
| `Flags(4)` | 对称半年变化 |
| `Flags(5)` | 非对称年变化 |
| `Flags(6)` | 非对称半年变化 |
| `Flags(7)` | 日变化 |
| `Flags(8)` | 半日变化 |
| `Flags(9)` | 每日 AP。如果将该字段设置为 -1，则该模块使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)` |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度 |
| `Flags(12)` | UT 和混合 UT、经度 |
| `Flags(13)` | 混合 AP、UT、经度 |
| `Flags(14)` | 三分之一日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 所有来自 120,000 meter 温度 (TLB) 的变化 |
| `Flags(18)` | 所有低热层 (TN1) 温度变化 |
| `Flags(19)` | 所有 120,000 meter 梯度 (S) 变化 |
| `Flags(20)` | 所有上平流层 (TN2) 温度变化 |
| `Flags(21)` | 所有来自 120,000 meter 值 (ZLB) 的变化 |
| `Flags(22)` | 所有低中间层温度 (TN3) 变化 |
| `Flags(23)` | 湍流层顶标高变化 |

#### 依赖关系

将 **标志来源** 设置为 `Internal` 会启用 **标志** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`flags` |
| **类型**：character vector |
| **值**：`'ones(1,23)'` |
| **默认**：`'ones(1,23)'` |

### **在总质量密度中包括异常氧数密度** — 异常氧 `off` (默认) | `on`

选中此复选框以在计算从地表到下外逸层（0 到 1,000,000 meters）的中性大气经验模型时考虑异常氧。考虑该数密度会影响 500,000 meters 以上的卫星阻力。

#### 程序化使用

|  |
| --- |
| **模块参数**：`oxygen_in` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认**：`'off'` |

### **超出范围输入的操作** — 超出范围模块行为 `None` (默认) | `Warning` | `Error`

超出范围模块行为，指定为：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` (默认) | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认**：`'Warning'` |

## 所属库

Aerospace Blockset / Environment / Atmosphere

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2007b 中引入**

## 描述

实现 2001 United States Naval Research Laboratory Mass Spectrometer and Incoherent Scatter Radar Exosphere 的数学表示

NRLMSISE-00 Atmosphere Model 模块实现 MSIS® 类模型的 2001 United States Naval Research Laboratory Mass Spectrometer and Incoherent Scatter Radar Exosphere (NRLMSISE-00) 的数学表示。该模块计算从地表到下外逸层（0 到 1,000,000 meters）的中性大气经验模型。为该计算配置模块时，您还可以考虑异常氧，它会影响 500,000 meters 以上的卫星阻力。
