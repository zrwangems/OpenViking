---
type: simulink-block
title: 'ECI Position to AER'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'ecipositiontoaer'
documentation_source_path: 'ecipositiontoaer.html'
language: zh-CN
chinese_source: worker-translation
---

# ECI Position to AER

## 端口

### 输入

### **Xi** — 位置 3×1 元素向量

位置，指定为 3×1 元素向量，采用 ECI 坐标。

**数据类型：** `double`

### **ΔUT1** — UTC 与世界时之间的差值标量

UTC 与世界时 (UT1) 之间的差值，以 seconds 为单位，指定为标量；模块针对该值计算方向余弦或变换矩阵。

**示例：** `0.234`

#### 依赖关系

要启用此端口，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **ΔAT** — 国际原子时与 UTC 之间的差值标量

国际原子时 (TAI) 与 UTC 之间的差值，以 seconds 为单位，指定为标量；函数针对该值计算方向余弦或变换矩阵。

**示例：** `32`

#### 依赖关系

如果清除 **Higher accuracy parameters** 复选框，则禁用此端口。

**数据类型：** `double`

### **[xp,yp]** — 地球极移 1×2 数组

地球极移，指定为 1×2 数组，以 radians 为单位，由地球地壳运动引起，沿 *x* 轴和 *y* 轴。

**示例：** `[-0.0682e-5 0.1616e-5]`

#### 依赖关系

要启用此端口，请选择 **Higher accuracy parameters**。

**数据类型：** `double`

### **Port\_5** — 基于归算方法的调整量 1×2 数组

基于归算方法的调整量，指定为 1×2 数组。端口名称取决于 **Reduction** 参数的设置：

- 如果归算方法为 `IAU-2000/2006`，此输入为对天球中间极 (CIP) 位置的调整量，以 radians 为单位。此位置 ([d*X*,d*Y*]) 沿 *x* 轴和 *y* 轴，例如 `[-0.2530e-6 -0.0188e-6]`。
- 如果归算方法为 `IAU-76/FK5`，此输入为对经度的调整量 ([Δδψ, Δδε])，以 radians 为单位。

有关历史值，请参阅 International Earth Rotation and Reference Systems Service 网站 (`https://www.iers.org`)，并导航到 Earth Orientation Data Data/Products 页面。

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

### **AER** — 方位角、仰角和斜距 3×1 元素向量

局部参考坐标的方位角 (degrees)、仰角 (degrees) 和斜距 (meters)，指定为 3×1 元素向量。

**数据类型：** `double`

## 参数

### **Reduction** — 归算方法 `IAU-76/FK5`（默认）| `IAU-2000/2006`

用于转换坐标的归算方法。方法可以是以下之一：

- `IAU-76/FK5`

  使用 International Astronomical Union 76/Fifth Fundamental Catalogue (IAU-76/FK5) 参考系统减少计算。如果用于转换的参考坐标系是 FK5，请选择此归算方法。

  **注意**

  此方法使用 IAU 1976 岁差模型和 IAU 1980 章动理论来减少计算。该模型和理论已不再现行，但软件为现有实现提供此归算方法。由于此归算方法使用极移近似，模块计算变换矩阵而不是方向余弦矩阵。
- `IAU-2000/2006`

  使用 International Astronomical Union 2000/2006 参考系统减少计算。如果用于转换的参考坐标系是 IAU-2000，请选择此归算方法。此归算方法使用 P03 岁差模型来减少计算。

#### 编程使用

|  |
| --- |
| **模块参数**：`red` |
| **类型**：character vector |
| **值**：`'IAU-2000/2006'` | `'IAU-76/FK5'` |
| **默认值**：`'IAU-2000/2006'` |

### **Year** — 年份 `2014`（默认）| double、整数、大于 1

用于计算协调世界时 (UTC) 日期的年份。输入一个大于 1 的整数 double 值，例如 `2014`。

#### 编程使用

|  |
| --- |
| **模块参数**：`year` |
| **类型**：character vector |
| **值**：double、整数、大于 1 |
| **默认值**：`'2013'` |

### **Month** — 月份 `January`（默认）| `February` | `March` | `April` | `May` | `June` | `July` | `August` | `September` | `October` | `November` | `December`

用于计算 UTC 日期的月份。

#### 编程使用

|  |
| --- |
| **模块参数**：`month` |
| **类型**：character vector |
| **值**：`'January'` | `'February'` | `'March'` | `'April'` | `'May'` | `'June'` | `'July'` | `'August'` | `'September'` | `'October'` | `'November'` | `'December'` |
| **默认值**：`'January'` |

### **Day** — 日 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

用于计算 UTC 日期的日。

#### 编程使用

|  |
| --- |
| **模块参数**：`day` |
| **类型**：character vector |
| **值**：`'1'` | `'2'` | `'3'` | `'4'` | `'5'` | `'6'` | `'7'` | `'8'` | `'9'` | `'10'` | `'11'` | `'12'` | `'13'` | `'14'` | `'15'` | `'16'` | `'17'` | `'18'` | `'19'` | `'20'` | `'21'` | `'22'` | `'23'` | `'24'` | `'25'` | `'26'` | `'27'` | `'28'` | `'29'` | `'30'` | `'31'` |
| **默认值**：`'1'` |

### **Hour** — 小时 `0`（默认）| double、整数、`0` 到 `24`

用于计算 UTC 日期的小时。输入一个从 `0` 到 `24` 的整数 double 值。

#### 编程使用

|  |
| --- |
| **模块参数**：`hour` |
| **类型**：character vector |
| **值**：double、整数、`0` 到 `24` |
| **默认值**：`'0'` |

### **Minutes** — 分钟 `0`（默认）| double、整数、`0` 到 `60`

用于计算 UTC 日期的分钟。输入一个从 `0` 到 `60` 的整数 double 值。

#### 编程使用

|  |
| --- |
| **模块参数**：`min` |
| **类型**：character vector |
| **值**：double、整数、`0` 到 `60` |
| **默认值**：`'0'` |

### **Seconds** — 秒 `0`（默认）

用于计算 UTC 日期的秒。输入一个从 `0` 到 `60` 的整数 double 值。

#### 编程使用

|  |
| --- |
| **模块参数**：`sec` |
| **类型**：character vector |
| **值**：double、整数、`0` 到 `60` |
| **默认值**：`'0'` |

### **Time increment** — 时间增量 `None`（默认）| `Day` | `Hour` | `Min` | `Sec`

指定日期与所需模型仿真时间之间的时间增量。模块调整计算得到的方向余弦矩阵，以考虑模型仿真的时间增量。例如，选择 `Day` 并将仿真计时器连接到端口，意味着每个时间增量单位是一天，模块会基于该仿真时间调整其计算。

此参数对应于时间增量输入，即时钟源。

如果选择 `None`，计算得到的儒略日不考虑模型仿真时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`deltaT` |
| **类型**：character vector |
| **值**：`'None'` | `'Day'` | `'Hour'` | `'Min'` | `'Sec'` |
| **默认值**：`'Day'` |

### **Action for out-of-range input** — 超出范围模块行为 `None`（默认）| `Warning` | `Error`

超出范围模块行为，指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`errorflag` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |

### **Higher accuracy parameters** — 启用更高精度参数 `on`（默认）| `off`

选中此复选框以允许以下项作为模块输入。这些输入可让您更好地控制转换结果。有关说明，请参阅输入。

- Δ *UT1*
- Δ *AT*
- [ *xp* , *yp* ]
- [Δδψ, Δδε] 或 [d *X* ,d *Y* ]

#### 编程使用

|  |
| --- |
| **模块参数**：`extraparamflag` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Units** — 单位 `Metric (MKS)`（默认）| `English`

指定参数和输出单位。

| 单位 | 位置 | 赤道半径 | 高度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### 依赖关系

要启用此选项，请将 **Earth model** 设置为 `WGS84`。

#### 编程使用

|  |
| --- |
| **模块参数**：`eunits` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Earth model** — 地球模型 `Custom`（默认）| `WGS84`

要使用的地球模型，`Custom` 或 `Earth (WGS84)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`earthmodel` |
| **类型**：character vector |
| **值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **Flattening** — 行星扁率 `1/298.257223563`（默认）| scalar

行星扁率，指定为 double scalar。

#### 依赖关系

要启用此参数，请将 **Earth model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`flat` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`1/298.257223563` |

### **Equatorial radius** — 赤道处行星半径 `6378137`（默认）| double scalar

行星在其赤道处的半径。

#### 依赖关系

要启用此参数，请将 **Earth model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`eqradius` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`6378137` |

### **Initial geodetic latitude and longitude [deg]** — 初始大地纬度和经度 `[0 0]`（默认）| 2×1 向量

以纬度和经度表示的参考位置，指定为 2×1 向量，以 degrees 为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`latlon0` |
| **类型**：character vector |
| **值**：2×1 向量 |
| **默认值**：`[0 0]` |

### **Angular direction of the local reference system (degrees clockwise from north)** — 角方向 `0`（默认）| scalar

指定用于将平面地球 *x* 和 *y* 坐标分别转换为北向和东向坐标的角度。一个示例是载体与真大地北之间的角度。

#### 编程使用

|  |
| --- |
| **模块参数**：`psi0` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`0` |

### **Reference height** — 参考高度 `0`（默认）| scalar

指定从地球表面到平面地球坐标系的参考高度。它使用与 ECI 位置相同的单位。相对于地球坐标系估计参考高度。

#### 编程使用

|  |
| --- |
| **模块参数**：`href` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`0` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

将地心惯性 (ECI) 坐标转换为方位坐标

ECI Position to AER 模块基于大地位置（纬度、经度和高度），将地心惯性 (ECI) 位置坐标转换为方位角、仰角和斜距坐标 (AER)。

- 方位角 (A) — 从真北顺时针测量的角度。范围为 0 到 360 degrees。
- 仰角 (E) — 垂直于椭球体的平面与从局部参考点到目标位置的连线之间的角度。范围为 –90 到 90 degrees。
- 斜距 (R) — 局部参考点与目标之间的直线距离。
