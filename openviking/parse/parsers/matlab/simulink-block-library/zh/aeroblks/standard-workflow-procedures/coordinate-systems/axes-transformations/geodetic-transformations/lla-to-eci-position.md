---
type: simulink-block
title: 'LLA to ECI Position'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'llatoeciposition'
documentation_source_path: 'llatoeciposition.html'
language: zh-CN
chinese_source: worker-translation
---

# LLA to ECI Position

## 端口

### 输入

### **[μ l h]** — 纬度、经度和高度三元素向量

要转换坐标的纬度、经度和高度值，指定为三元素向量，单位为 degrees。

**数据类型：** `double`

### **ΔUT1** — UTC 与世界时之差标量

UTC 与世界时 (UT1) 之间的差，单位为 seconds，指定为标量，模块为其计算方向余弦或变换矩阵。

**示例：** `0.234`

#### 依赖关系

要启用此功能，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **ΔAT** — 国际原子时与 UTC 之差标量

国际原子时 (TAI) 与 UTC 之间的差，指定为标量，单位为 seconds，模块为其计算方向余弦或变换矩阵。

**示例：** `32`

#### 依赖关系

要启用此端口，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **[xp,yp]** — 地球极位移 1×2 数组

地球极位移，指定为 1×2 数组，单位为 radians，由地壳运动引起，沿 *x* 轴和 *y* 轴。

**示例：** `[-0.0682e-5 0.1616e-5]`

#### 依赖关系

要启用此端口，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **Port\_5** — 基于归约方法的调整 1×2 数组

基于归约方法的调整，指定为 1×2 数组。端口名称取决于 **Reduction** 参数的设置：

- 如果归约方法为 `IAU-2000/2006`，此输入是对天球中间极 (CIP) 位置的调整，单位为 radians。此位置 ([d*X*,d*Y*]) 沿 *x* 轴和 *y* 轴。
- 如果归约方法为 `IAU-76/FK5`，此输入是对经度的调整 ([Δδψ, Δδε])，单位为 radians。

有关历史值，请参见国际地球自转和参考系统服务网站 (`https://www.iers.org`)，并导航到地球定向数据 Data/Products 页面。

**示例：** `[-0.2530e-6 -0.0188e-6]`

#### 依赖关系

要启用此端口，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **Port\_6** — 时间增量源标量

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

### **Xi** — 原始位置 3×1 元素向量

相对于 ECI 参考系的原始位置向量，返回为 3×1 元素向量。

**数据类型：** `double`

## 参数

### **Reduction** — 归约方法 `IAU-76/FK5`（默认） | `IAU-2000/2006`

用于转换坐标的归约方法。方法可以是以下之一：

- `IAU-76/FK5`

  使用国际天文学联合会 76/第五基本星表 (IAU-76/FK5) 参考系来归约计算。如果转换的参考坐标系为 FK5，请选择此归约方法。

  **注意**

  此方法使用 IAU 1976 岁差模型和 IAU 1980 章动理论来归约计算。该模型和理论已不再是最新的，但软件为现有实现提供此归约方法。由于此归约方法使用极移近似，模块计算变换矩阵而不是方向余弦矩阵。
- `IAU-2000/2006`

  使用国际天文学联合会 2000/2006 参考系来归约计算。如果转换的参考坐标系为 IAU-2000，请选择此归约方法。此归约方法使用 P03 岁差模型来归约计算。

#### 程序化使用

|  |
| --- |
| **模块参数**: `red` |
| **类型**: character vector |
| **值**: `'IAU-2000/2006'` | `'IAU-76/FK5'` |
| **默认值**: `'IAU-2000/2006'` |

### **Year** — 年份 `2013`（默认） | double、整数、大于 1

用于计算协调世界时 (UTC) 日期的年份。请输入大于 1 的整数 double 值，例如 `2013`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `year` |
| **类型**: character vector |
| **值**: double、整数、大于 1 |
| **默认值**: `'2013'` |

### **Month** — 月份 `January`（默认） | `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算 UTC 日期的月份。

#### 程序化使用

|  |
| --- |
| **模块参数**: `month` |
| **类型**: character vector |
| **值**: `'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**: `'January'` |

### **Day** — 日 `1`（默认） | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

用于计算 UTC 日期的日。

#### 程序化使用

|  |
| --- |
| **模块参数**: `day` |
| **类型**: character vector |
| **值**: `'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **默认值**: `'1'` |

### **Hour** — 小时 `0`（默认） | double、整数、`0` 到 `24`

用于计算 UTC 日期的小时。请输入从 `0` 到 `24` 的整数 double 值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `hour` |
| **类型**: character vector |
| **值**: double、整数、`0` 到 `24` |
| **默认值**: `'0'` |

### **Minutes** — 分钟 `0`（默认） | double、整数、`0` 到 `60`

用于计算 UTC 日期的分钟。请输入从 `0` 到 `60` 的整数 double 值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `min` |
| **类型**: character vector |
| **值**: double、整数、`0` 到 `60` |
| **默认值**: `'0'` |

### **Seconds** — 秒 `0`（默认）

用于计算 UTC 日期的秒。请输入从 `0` 到 `60` 的整数 double 值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `sec` |
| **类型**: character vector |
| **值**: double、整数、`0` 到 `60` |
| **默认值**: `'0'` |

### **Time increment** — 时间增量 `Day`（默认） | `None` | `Hour` | `Min` | `Sec`

指定日期与所需模型仿真时间之间的时间增量。模块会调整计算得到的方向余弦矩阵，以考虑来自模型仿真的时间增量。例如，选择 `Day` 并将仿真计时器连接到端口，意味着每个时间增量单位为一天，模块会根据该仿真时间调整其计算。

此参数对应于时间增量输入，即时钟源。

如果选择 `None`，计算得到的儒略日不考虑模型仿真时间。

#### 程序化使用

|  |
| --- |
| **模块参数**: `deltaT` |
| **类型**: character vector |
| **值**: `'None'` | `'Day'` | `'Hour'` | `'Min'` | `'Sec'` |
| **默认值**: `'Day'` |

### **Action for out-of-range input** — 超出范围的模块行为 `None`（默认） | `Warning` | `Error`

超出范围的模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 诊断查看器中显示警告，模型仿真继续。 |
| `Error`（默认） | 诊断查看器中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `errorflag` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Error'` |

### **Higher accuracy parameters** — 启用更高精度参数 `on`（默认） | `off`

选中此复选框可将以下内容允许为模块输入。这些输入可让您更好地控制转换结果。有关说明，请参见输入。

- Δ *UT1*
- Δ *AT*
- [ *xp* , *yp* ]
- [Δδψ, Δδε] 或 [d *X*, d *Y* ]

#### 程序化使用

|  |
| --- |
| **模块参数**: `extraparamflag` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Units** — 单位 `Metric (MKS)`（默认） | `English`

指定参数和输出单位。

| 单位 | 位置 | 赤道半径 | 高度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### 依赖关系

要启用此参数，请将 **Earth model** 设置为 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `eunits` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **Earth model** — 地球模型 `WGS84`（默认） | `Custom`

要使用的地球模型，`Custom` 或 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `earthmodel` |
| **类型**: character vector |
| **值**: `'Earth (WGS84)'` | `'Custom'` |
| **默认值**: `'Earth (WGS84)'` |

### **Flattening** — 行星扁率 `1/298.257223563`（默认） | 标量

行星的扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **Earth model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `flat` |
| **类型**: character vector |
| **值**: double 标量 |
| **默认值**: `1/298.257223563` |

### **Equatorial radius** — 赤道处行星半径 `6378137`（默认） | 标量

行星在其赤道处的半径。

#### 依赖关系

要启用此参数，请将 **Earth model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `eqradius` |
| **类型**: character vector |
| **值**: double 标量 |
| **默认值**: `6378137` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2014a 中引入**

## 描述

将纬度、经度、高度 (LLA) 坐标转换为地心惯性 (ECI) 坐标

LLA to ECI Position 模块根据指定的归约方法和协调世界时 (UTC)，针对指定时间和地球物理数据，将纬度、经度和高度 (LLA) 坐标转换为地心惯性 (ECI) 位置坐标。纬度和经度值可以是任意值。但是，由于两极处的奇异性，纬度值为 +90 和 -90 时可能返回意外值。
