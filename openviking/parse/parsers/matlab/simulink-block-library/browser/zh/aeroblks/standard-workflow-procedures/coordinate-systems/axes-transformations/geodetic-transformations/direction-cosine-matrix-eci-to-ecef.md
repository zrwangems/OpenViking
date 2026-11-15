---
type: simulink-block
title: 'Direction Cosine Matrix ECI to ECEF'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixecitoecef'
documentation_source_path: 'directioncosinematrixecitoecef.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix ECI to ECEF

## 端口

### 输入

### **ΔUT1** — UTC 与世界时之差 标量

UTC 与世界时 (UT1) 之差，以 seconds 为单位，指定为标量，该函数为其计算方向余弦或变换矩阵。

**示例：**
`0.234`

#### 依赖关系

要启用此端口，请选中 **Higher accuracy parameters** 复选框。

**数据类型：** `double`

### **ΔAT** — 国际原子时与 UTC 之差 标量

国际原子时 (TAI) 与 UTC 之差，指定为标量，以 seconds 为单位，该函数为其计算方向余弦或变换矩阵。

**示例：**
`32`

#### 依赖关系

要启用此端口，请选中 **Higher accuracy parameters** 复选框。

**数据类型：** `double`

### **[xp,yp]** — 地球极移 1×2 数组

地球极移，指定为 1×2 数组，以 radians 为单位，由地壳沿 x 轴和 y 轴的运动引起。

**示例：**
`[-0.0682e-5 0.1616e-5]`

#### 依赖关系

要启用此端口，请选中 **Higher accuracy parameters** 复选框。

**数据类型：** `double`

### **Port\_5** — 基于归约方法的调整 1×2 数组

基于归约方法的调整，指定为 1×2 数组。端口名称取决于 **Reduction** 参数的设置：

- 如果归约方法为 `IAU-2000/2006`，此输入是对天球中间极 (CIP) 位置的调整，以 radians 为单位。此位置 ([d*X*, d*Y*]) 沿 x 轴和 y 轴。
- 如果归约方法为 `IAU-76/FK5`，此输入是对经度的调整 ([Δδψ, Δδε])，以 radians 为单位。

有关历史值，请参见国际地球自转和参考系统服务网站 (`https://www.iers.org`)。

**示例：**
`[-0.2530e-6 -0.0188e-6]`

#### 依赖关系

要启用此端口，请选中 **Higher accuracy parameters** 复选框。

**数据类型：** `double`

### **Port\_6** — 时间增量源 标量

时间增量源，指定为标量，例如 Clock 模块。

#### 依赖关系

- 端口名称和时间增量取决于 **Time Increment** 参数。

  | **Time Increment** 值 | 端口名称 |
  | --- | --- |
  | `Day` | **day** |
  | `Hour` | **hour** |
  | `Min` | **min** |
  | `Sec` | **sec** |
  | `None` | 无端口 |
- 要禁用此端口，请将 **Time Increment** 参数设置为 `None`。

**数据类型：** `double`

### 输出

### **DCMfi** — 方向余弦矩阵 3×3 矩阵

ECI 到 ECEF 的方向余弦矩阵。

**数据类型：** `double`

## 参数

### **Reduction** — 归约方法 `IAU-76/FK5` (默认) | `IAU-2000/2006`

用于计算方向余弦矩阵的归约方法。该方法可以是以下之一：

- `IAU-76/FK5`

  使用 IAU-76/第五基本星表 (FK5) 参考系统归约计算。如果转换的参考坐标系为 FK5，请选择此归约方法。

  **注意**

  此方法使用 IAU 1976 岁差模型和 IAU 1980 章动理论来归约计算。此模型和理论已不再是最新的，但软件为现有实现提供此归约方法。由于此归约方法使用的极移近似，该模块计算变换矩阵而非方向余弦矩阵。
- `IAU-2000/2006`

  使用国际天文学联合会 (IAU)-2000/2006 参考系统归约计算。如果转换的参考坐标系为 IAU-2000，请选择此归约方法。此归约方法使用 P03 岁差模型来归约计算。

#### 编程用法

|  |
| --- |
| **模块参数**：`red` |
| **类型**：字符向量 |
| **值**：`'IAU-2000/2006'` | `'IAU-76/FK5'` |
| **默认值**：`'IAU-2000/2006'` |

### **Year** — 年份 `2013` (默认) | double，大于 1 的整数

用于计算协调世界时 (UTC) 日期的年份。输入一个大于 1 的整数 double 值，例如 `2013`。

#### 编程用法

|  |
| --- |
| **模块参数**：`year` |
| **类型**：字符向量 |
| **值**：double，大于 1 的整数 |
| **默认值**：`'2013'` |

### **Month** — 月份 `January` (默认) | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算 UTC 日期的月份。

#### 编程用法

|  |
| --- |
| **模块参数**：`month` |
| **类型**：字符向量 |
| **值**：`'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**：`'January'` |

### **Day** — 日 `1` (默认) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

用于计算 UTC 日期的日。

#### 编程用法

|  |
| --- |
| **模块参数**：`day` |
| **类型**：字符向量 |
| **值**：`'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **默认值**：`'1'` |

### **Hour** — 小时 `0` (默认) | double，整数，在 `0` 和 `24` 范围内

用于计算 UTC 日期的小时。输入一个从 `0` 到 `24` 的整数 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**：`hour` |
| **类型**：字符向量 |
| **值**：double，整数，`0` 到 `24` |
| **默认值**：`'0'` |

### **Minutes** — 分钟 `0` (默认) | double，整数，在 `0` 和 `60` 范围内

用于计算 UTC 日期的分钟。输入一个从 `0` 到 `60` 的整数 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**：`min` |
| **类型**：字符向量 |
| **值**：double，整数，`0` 到 `60` |
| **默认值**：`'0'` |

### **Seconds** — 秒 `0` (默认) | double，整数，在 `0` 和 `60` 范围内

用于计算 UTC 日期的秒。输入一个从 `0` 到 `60` 的整数 double 值。

#### 编程用法

|  |
| --- |
| **模块参数**：`sec` |
| **类型**：字符向量 |
| **值**：double，整数，`0` 到 `60` |
| **默认值**：`'0'` |

### **Time increment** — 时间增量 `Day` (默认) | `Hour` | `Min` | `Sec` | `None`

指定日期与所需模型仿真时间之间的时间增量。该模块调整计算出的方向余弦矩阵，以考虑来自模型仿真的时间增量。例如，选择 `Day` 并将仿真计时器连接到该端口意味着每个时间增量单位为一天，并且该模块基于该仿真时间调整其计算。

此参数对应于时间增量输入，即时钟源。

如果选择 `None`，计算出的儒略日不考虑模型仿真时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`deltaT` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Day'` | `'Hour'` | `'Min'` | `'Sec'` |
| **默认值**：`'Day'` |

### **Action for out-of-range input** — 超出范围模块行为 `None` (默认) | `Warning` | `Error`

超出范围模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error` (默认) | 在 Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`errorflag` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |

### **Higher accuracy parameters** — 启用更高精度参数 `on` (默认) | `off`

选中此复选框以启用这些输入。这些输入使您能够更好地控制转换结果。有关说明，请参见输入。

- Δ *UT1*
- Δ *AT*
- [ *xp* , *yp* ]
- [Δδψ, Δδε] 或 [d *X*, d *Y* ]

#### 编程用法

|  |
| --- |
| **模块参数**：`extraparamflag` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

将地心惯性系 (ECI) 坐标转换为地心固连系 (ECEF) 坐标

Direction Cosine Matrix ECI to ECEF 模块基于指定的归约方法和协调世界时 (UTC)，针对指定的时间和地球物理数据，计算位置方向余弦矩阵（地心惯性系到地心固连系）。
