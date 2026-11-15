---
type: simulink-block
title: 'Orbit Propagator Kepler (unperturbed)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'orbitpropagatorkeplerunperturbed'
documentation_source_path: 'orbitpropagatorkeplerunperturbed.html'
language: zh-CN
chinese_source: worker-translation
---

# Orbit Propagator Kepler (unperturbed)

## 端口

### 输出

### **Xicrf** — 航天器位置 3 元素向量 | *numSat*-by-3

航天器相对于 (ICRF 或 fixed-frame) 的位置，在当前时间步返回为 3 元素向量或 *numSat*-by-3 数组，其中 *m* 是航天器数量。**Orbit** 选项卡中提供的初始条件大小控制端口维度。*numSat* 是航天器数量。

**数据类型：** `double`

### **Vicrf** — 速度 3 元素向量 | *numSat*-by-3 数组

航天器相对于 ICRF 或 fixed-frame 的速度，在当前时间步返回为 3 元素向量或 *numSat*-by-3 数组。*numSat*-by-3 数组。**Orbit** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **tutc** — 当前时间步的时间 标量 | 6 元素向量

当前时间步的时间，返回为：

- 标量 — 如果将 **Start data/time** 参数指定为 Julian date。
- 6 元素向量 — 如果将 **Start data/time** 参数指定为包含六个元素（year, month, day, hours, minutes, seconds）的 Gregorian date。

此值等于 **Start date/time** 参数值 + *the elapsed simulation time*。

#### 依赖关系

要启用此参数，请选中 **Output current date/time (UTC Julian date)** 复选框。

**数据类型：** `double`

## 参数

### 主

### **传播方法** — 轨道传播方法 `Kepler (unperturbed)` | `Numerical (high precision)`

轨道传播方法，指定为：

- `Kepler (unperturbed)` — 使用 Kepler 问题的通用变量公式来确定每个时间步的航天器位置和速度。此方法比 `Numerical (high precision)` 更快。
- `Numerical (high precision)` — 使用数值积分确定每个时间步的航天器位置和速度。此选项根据 **Central body** 选项卡中的设置对中心天体引力进行建模。此方法比 `Kepler (unperturbed)` 更准确，但更慢。

#### 程序化使用

|  |
| --- |
| **模块参数：** `propagator` |
| **类型：** character vector |
| **值：** `'Kepler (unperturbed)'` | `'Numerical (high precision)'` |
| **默认值：** `'Kepler (unperturbed)'` |

### **输入外部加速度** — 输入附加加速度 off（默认）| on

要启用将附加外部加速度包含在航天器运动方程的积分中，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此复选框，请将 **传播方法** 设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `accelIn` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **外部加速度坐标系** — 附加加速度的坐标系 `ICRF`（默认）| `Fixed-frame`

输入附加加速度，指定为 `ICRF` 或 `Fixed-frame`。这些加速度包含在航天器运动方程的积分中。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 设置为 `Numerical (high precision)`
- 选中 **输入外部加速度** 复选框

#### 程序化使用

|  |
| --- |
| **模块参数：** `accelFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认值：** `'ICRF'` |

### **状态向量输出坐标系** — 端口坐标系 `ICRF`（默认）| `Fixed-frame`

输出端口的坐标系，指定为 `ICRF` 或 `Fixed-frame`。受影响的端口标签包括：

- 输出端口 **X**
- 输出端口 **V**

#### 依赖关系

要启用此参数，请将 **传播方法** 设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outportFrame` |
| **类型：** character vector |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认值：** `'ICRF'` |

### **开始日期/时间 (UTC Julian date)** — 仿真的初始开始时间 `juliandate (2020, 1, 1, 12, 0, 0)`（默认）| 有效标量 Julian date | 有效 Gregorian date，包括 year, month, day, hours, minutes, seconds 作为 6 元素向量

仿真的初始开始日期和时间，指定为 Julian 或 Gregorian date。模块使用此值定义初始条件。

**提示**

要计算 Julian date，请使用 `juliandate` 函数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `startDate` |
| **类型：** character vector |
| **值：** `'juliandate(2020, 1, 1, 12, 0, 0)'` | valid scalar Julian date | valid Gregorian date including year, month, day, hours, minutes, seconds as 6-element vector |
| **默认值：**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **输出当前日期/时间 (UTC Julian date)** — 添加输出端口 tutc on（默认）| off

要输出当前日期或时间，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dateOut` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **超出范围输入的操作** — 超出范围时的模块行为 `Warning`（默认）| `Error` | `None`

超出范围时的模块行为，指定如下：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。 |
| `Error`（默认） | 在 Diagnostic Viewer 中显示错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**： character vector |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认值**： `'Warning'` |

### 轨道

定义航天器的初始状态。

### **初始状态格式** — 轨道初始状态的输入方法 `Orbital elements`（默认）| `ICRF state vector`

轨道初始状态的输入方法，指定为 `Orbital elements` 或 `ICRF state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数** `stateFormatKep` |
| **类型：** character vector |
| **值：**  `'Orbital elements'` | `'ICRF state vector'` |
| **默认值：** `'Orbital elements'` |

### **轨道类型** — 轨道分类 `Keplerian`（默认）| `Elliptical equatorial` | `Circular` | `Circular equatorial`

轨道分类，指定为：

- `Keplerian` — 使用六个标准 Keplerian 轨道元素对椭圆轨道建模。
- `Elliptical equatorial` — 定义赤道轨道，其中倾角为 0 或 180 degrees，升交点赤经未定义。
- `Circular` — 定义圆轨道，其中偏心率为 0，近拱点幅角未定义。
- `Circular equatorial` — 定义圆轨道，其中偏心率为 0 或 10 degrees。近拱点幅角和升交点赤经未定义。

#### 依赖关系

要启用此参数，请将 **初始状态格式** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `orbitType` |
| **类型：** character vector |
| **值：** `'Keplerian'` | `'Elliptical equatorial'` | `'Circular inclined'` | `'Circular equatorial'` |
| **默认值：** `'Keplerian'` |

### **半长轴** — 椭圆长轴的一半 6786000（默认）| 大小为 *numSat* 的 1D 数组

椭圆长轴的一半，指定为大小等于航天器数量的一维数组。

- 对于抛物线轨道，此模块将此参数解释为近拱点半径（从近拱点到轨道焦点的距离）。
- 对于双曲线轨道，此模块将此参数解释为从近拱点到双曲线中心的距离。

#### 依赖关系

要启用此参数，请将 **初始状态格式** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `semiMajorAxis` |
| **类型：** character vector |
| **值：** scalar | 1D array of size *m*, number of spacecraft |
| **默认值：** `'6786000'` |

### **偏心率** — 轨道偏离 0.01（默认）| scalar | 介于 `0` 和 `1` 之间的值，或对于 Keplerian 轨道类型大于 `1` | 大小为 *numSat* 的 1D 数组

轨道偏离完美圆的程度，指定为标量或大小等于航天器数量的一维数组。

如果 **轨道** 类型设置为 `Keplerian`，值可以为：

- `0`：圆轨道
- 介于 `0` 和 `1` 之间：椭圆轨道
- `1`：抛物线轨道
- 大于 `1`：双曲线轨道

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Keplerian` 或 `Elliptical equatorial`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eccentricity` |
| **类型：** character vector |
| **值：** `0.01` | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat* |
| **默认值：** `'0.01'` |

### **倾角 (deg)** — 轨道平面倾斜角 50（默认）| scalar | 大小为 *numSat* 的 1D 数组 | degrees 介于 0 和 180 之间 | radians 介于 0 和 pi 之间

椭圆相对于参考平面的垂直倾斜角，在升交点处测量，指定为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`
- **轨道类型** 为 `Keplerian` 或 `Circular inclined`

#### 程序化使用

|  |
| --- |
| **模块参数：** `inclination` |
| **类型：** character vector |
| **值：** 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi |
| **默认值：** `'50'` |

### **RAAN (deg)** — 赤道平面中的角距离 95（默认）| 介于 `0` 和 `360` 之间的标量值 | 大小为 *numSat* 的 1D 数组

升交点赤经 (RAAN)，指定为介于 `0` 和 `360` 之间的标量值或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。RAAN 是沿参考平面从 ICRF *x* 轴到升交点位置（航天器从南到北穿过参考平面的点）的角距离。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Keplerian` 或 `Circular inclined`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `raan` |
| **类型：** character vector |
| **值：** `95` | scalar value between `0` and `360` | 1D array of size *m* number of spacecraft |
| **默认值：** `'95'` |

### **近拱点幅角 (deg)** — 从航天器升交点到近拱点的角度 93（默认）| degrees 介于 `0` 和 `360` 之间 | radians 介于 `0` 和 `2*pi` 之间 | 大小为 *m* 的 1D 数组，航天器数量

从航天器升交点到近拱点（轨道距中心天体的最近点）的角度，指定为大小为 *m* 的一维数组，其中 *m* 是航天器数量，使用指定单位。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`
- **轨道类型** 为 `Keplerian`

#### 程序化使用

|  |
| --- |
| **模块参数：** `argPeriapsis` |
| **类型：** character vector |
| **值：** `'95'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **默认值：** `'93'` |

### **真近点角** — 近拱点和航天器初始位置之间的角度 203（默认）| scalar | degrees 介于 `0` 和 `360` 之间 | radians 介于 `0` 和 `2*pi` 之间 | 大小为 *numSat* 的 1D 数组

近拱点（轨道距中心天体的最近点）和航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Keplerian` 或 `Elliptical inclined`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `trueAnomaly` |
| **类型：** character vector |
| **值：** `'203'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'203'` |

### **纬度幅角 (deg)** — 升交点和航天器初始位置之间的角度 200（默认）| scalar | degrees 介于 `0` 和 `360` 之间 | radians 介于 `0` 和 `2*pi` 之间 | 大小为 *numSat* 的 1D 数组

升交点和航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为标量或 3 元素向量或大小等于航天器数量的一维数组，使用指定单位。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Circular inclined`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `argLat` |
| **类型：** character vector |
| **值：** `'200'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'200'` |

### **近拱点经度 (deg)** — ICRF *x* 轴和偏心率向量之间的角度 100（默认）| scalar | degrees 介于 `0` 和 `360` 之间 | radians 介于 `0` 和 `2*pi` 之间 | 大小为 *numSat* 的 1D 数组

ICRF x 轴和偏心率向量之间的角度，指定为标量或 3 元素向量或大小等于航天器数量的一维数组，使用指定单位。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Elliptical equatorial`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `lonPeriapsis` |
| **类型：** character vector |
| **值：** 100 | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *m*, number of spacecraft |
| **默认值：** `'100'` |

### **真经度 (deg)** — ICRF *x* 轴和航天器初始位置之间的角度 150（默认）| scalar | degrees 介于 `0` 和 `360` 之间 | radians 介于 `0` 和 `2*pi` 之间 | 大小为 *numSat* 的 1D 数组

ICRF x 轴和航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- **初始状态格式** 为 `Orbital elements`。
- **轨道类型** 为 `Circular equatorial`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `trueLon` |
| **类型：** character vector |
| **值：** `'150'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'150'` |

### **ICRF 位置** — 航天器的笛卡尔位置向量 `[3649700.0 3308200.0 -4676600.0]`（默认）| 3 元素向量 | | *numSat*-by-3 数组

航天器在 **Start date/time** 时在 ICRF 坐标系中的笛卡尔位置向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请将 **初始状态格式** 设置为 `ICRF state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertialPosition` |
| **类型：** character vector |
| **值：** `[3649700.0 3308200.0 -4676600.0]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF 速度** — 航天器的笛卡尔速度向量 `[-2750.8 6666.4 2573.4]`（默认）| 单个航天器的 3 元素向量或大小为 *m*-by-3 的 2-D 数组（多个航天器）

航天器在 **Start date/time** 时在 ICRF 坐标系中的笛卡尔速度向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为大小为 *m*-by-3 的 2-D 数组。

#### 依赖关系

要启用此参数，请将 **初始状态格式** 设置为 `ICRF state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertialVelocity` |
| **类型：** character vector |
| **值：** `[-2750.8 6666.4 2573.4]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame 位置** — 航天器位置向量 [-4142689.0 -2676864.7 -4669861.6]（默认）| 单个航天器的 3 元素向量或大小为 *m*-by-3 的 2-D 数组（多个航天器）

航天器在 **Start date/time** 时在 fixed-frame 坐标系中的笛卡尔位置向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为大小为 *m*-by-3 的 2-D 数组。

#### 依赖关系

要启用此参数，请设置：

- **传播方法** 为 `Numerical (high precision)`。
- 将 **初始状态格式** 设置为 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fixedPosition` |
| **类型：** character vector |
| **值：** `'[-4142689.0 -2676864.7 -4669861.6]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame 速度** — 航天器速度向量 [1452.7 -6720.7 2568.1]（默认）| 单个航天器的 3 元素向量或大小为 *m*-by-3 的 2-D 数组（多个航天器）

航天器在 **Start date/time** 时在 fixed-frame 坐标系中的笛卡尔速度向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为大小为 *m*-by-3 的 2-D 数组。

#### 依赖关系

要启用此参数，请设置：

- **传播方法** 为 `Numerical (high precision)`。
- **初始状态格式** 为 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fixedVelocity` |
| **类型：** character vector |
| **值：** `'[1452.7 -6720.7 2568.1]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[1452.7 -6720.7 2568.1]'` |

### 中心天体

配置航天器环绕的中心天体环境。

### **中心天体** — 航天器环绕的天体 `Earth`（默认）| `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune`、`Sun` 或 `Custom`，**Orbit** 选项卡中定义的航天器环绕该天体运行。

#### 程序化使用

|  |
| --- |
| **模块参数：** `centralBody` |
| **类型：** character vector |
| **值：** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Sun'` | `'Custom'` | |
| **默认值：** `'Earth'` |

### 单位

### **单位** — 参数和端口单位 `Metric (m/s)`（默认）| `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

参数和端口单位，指定为：

| 单位 | 距离 | 速度 | 加速度 | 质量 | 面积 | 密度 |
| --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | meters | meters/sec | meters/sec2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/s)` | kilometers | kilometers/sec | kilometers/sec2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/h)` | kilometers | kilometers/hour | kilometers/hour2 | Kilograms | m2 | kg/m3, some density outputs 1/m3 |
| `English (ft/s)` | feet | feet/sec | feet/sec2 | Slugs | feet2 | lbm/ft3, some density outputs 1/ft3 |
| `English (kts)` | nautical mile | knots | knots/sec | Slugs | feet2 | lbm/ft3, some density outputs 1/ft3 |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **默认值：** `'Metric (m/s)'` |

### **角度单位** — 角度单位 `Degrees`（默认）| `Radians`

用于角度的参数和端口单位，指定为 `Degrees` 或 `Radians`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `angleUnits` |
| **类型：** character vector |
| **值：** `'Degrees'` | `'Radians'` |
| **默认值：** `'Degrees'` |

### **时间格式** — 开始日期和时间输出的时间格式 `Julian date`（默认）| `Gregorian`

用于 **开始日期/时间 (UTC Julian date)** 和输出端口 **tutc** 的时间格式，指定为 `Julian date` 或 `Gregorian`。

#### 程序化使用

|  |
| --- |
| **模块参数：**  `timeFormat` |
| **类型：** character vector |
| **值：** `'Julian date'` | `'Gregorian'` |
| **默认值：** `'Julian date'` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2023b: Orbit Propagator 模块变更

Orbit Propagator 模块已更新，以考虑：

- 第三体引力对轨道传播的影响。
- 来自 `aeroReadSpaceWeatherData` 函数生成的数据文件的空间天气数据。
- 太阳辐射压力 (SRP)。

## 描述

使用 Kepler 通用变量公式传播一个或多个航天器的轨道

Orbit Propagator Kepler (unperturbed) 模块使用 Kepler 通用变量公式传播一个或多个航天器的轨道。Orbit Propagator Kepler (unperturbed) 和 Orbit Propagator Numerical (high precision) 模块是同一模块的替代配置。

- Orbit Propagator Kepler (unperturbed) — Kepler 通用变量公式（更快）
- Orbit Propagator Kepler Numerical (high precision) — 更准确

Orbit Propagator Kepler (unperturbed) 模块不考虑大气阻力、第三体引力或太阳辐射压力。对于考虑这些效应的轨道传播，请参阅 Orbit Propagator Numerical (high precision) 模块。

提供的初始条件大小决定所建模的航天器数量。如果为 **Orbit** 选项卡中的参数提供多个值，模块将输出卫星星座。任何仅提供单个值的参数都会扩展并应用于星座中的所有卫星。例如，如果为模块上的所有参数提供单个值，但 **True anomaly** 包含六个值，则模块会创建由六颗卫星组成的星座，仅改变真近点角。

模块对输入端口 **A\_icrf**（施加的加速度）应用相同的扩展行为。此端口接受扩展为所有所建模航天器的单个值，或应用于每艘航天器的单独值。

有关 Orbit Propagator 模块使用的传播方法的更多信息，请参阅 Orbit Propagation Methods。

您可以在 **Orbit** 选项卡中将初始轨道状态定义为：

- 一组轨道元素
- International Celestial Reference Frame (ICRF) 或 fixed-frame 坐标系中的位置和速度状态向量。

模块使用四元数，这些四元数使用 scalar-first 约定定义。

有关 Orbit Propagator 模块使用的坐标系的更多信息，请参阅 Coordinate Systems。
