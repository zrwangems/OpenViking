---
type: simulink-block
title: 'Orbit Propagator Numerical (high precision)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft Simulation'
documentation_page: 'orbitpropagatornumericalhighprecision'
documentation_source_path: 'orbitpropagatornumericalhighprecision.html'
language: zh-CN
chinese_source: worker-translation
---

# Orbit Propagator Numerical (high precision)

## 端口

### 输入

### **Aicrf** — 施加的加速度 三元素向量 | *m*-3 数组

相对于端口坐标系（ICRF 或固定坐标系）施加到航天器上的加速度，在当前时间步长指定为三元素向量或 *m*×3 数组。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 选中 **输入外部加速度** 复选框。

**数据类型：** `double`

### **φθψ** — 月球天平动角 三元素向量

用于在 ICRF 与以月球为中心的固定坐标系之间进行转换的月球天平动角，使用以月球为中心的主轴 (PA) 系统，指定为三元素向量。要获取这些值，请使用 Moon Libration 模块。

**注意**

当 **中心天体** 设置为 `Moon` 时，此模块使用的固定坐标系是平均地球/极轴 (ME) 系统。有关详细信息，请参阅算法。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Moon`。
- 选中 **输入月球天平动角** 复选框。

**数据类型：** `double`

### **αδW** — 赤经、赤纬和旋转角 三元素向量

中心天体自转轴的瞬时赤经、赤纬和旋转角，指定为三元素向量。此端口仅适用于自定义中心天体。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴源** 设置为 `Port`。

**数据类型：** `double`

### **m** — 大气阻力计算所使用的航天器质量 标量 | 大小为 *numSat* 的向量

大气阻力计算所使用的航天器质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **质量源** 参数设置为 `Dialog`。

**数据类型：** `double`

### **ρ** — 大气密度 标量

用于计算大气阻力加速度的大气密度。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度源** 参数设置为 `Port`。

**数据类型：** `double`

### **F107a** — 81 天平均渥太华 F10.7 cm 太阳通量 标量

81 天平均渥太华 F10.7 cm 太阳通量，以 **开始日期/时间** 中指定的当前日为中心。这些 F107 Average 值对应于地球与太阳实际距离处的 10.7 cm 无线电通量。此站点提供这两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度源** 参数设置为 `Dialog`。

**数据类型：** `double`

### **F107** — 每日渥太华 F10.7 cm 太阳通量 标量

每日渥太华 F10.7 cm 太阳通量，以 **开始日期/时间** 中指定的当前日为中心。f107Daily 值不对应于 1 AU 处的无线电通量。此站点提供这两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度源** 参数设置为 `Dialog`。

**数据类型：** `double`

### **aph** — 每日磁指数信息 *N*×7 数组

每日磁指数信息 (aph)，指定为 *N*×7 数组。磁指数信息包括：

|  |
| --- |
| 每日磁指数 (AP) |
| 当前时间的 3 小时 AP |
| 当前时间前 3 小时的 3 小时 AP |
| 当前时间前 6 小时的 3 小时 AP |
| 当前时间前 9 小时的 3 小时 AP |
| 当前时间前 12 至 33 小时的八个 3 小时 AP 指数的平均值 |
| 当前时间前 36 至 57 小时的八个 3 小时 AP 指数的平均值 |

在低于 80,000 m 时，每日磁指数的影响不大或尚未确定。有关详细信息，请参阅 NRLMSISE-00 大气模型的局限性。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度源** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Flags** — 变化标志 23 元素数组

变化标志，指定为 23 元素数组，用于启用或禁用输出的特定变化。可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0

  移除该值对输出的影响。
- 1.0

  将该值的主效应和交叉项效应用于输出。
- 2.0

  仅将该值的交叉项效应用于输出。

| 字段 | 描述 |
| --- | --- |
| `Flags(1)` | F10.7 对平均值的影响 |
| `Flags(2)` | 与时间无关 |
| `Flags(3)` | 对称年变化 |
| `Flags(4)` | 对称半年变化 |
| `Flags(5)` | 非对称年变化 |
| `Flags(6)` | 非对称半年变化 |
| `Flags(7)` | 日变化 |
| `Flags(8)` | 半日变化 |
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，则模块使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)` |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度 |
| `Flags(12)` | UT 和混合 UT、经度 |
| `Flags(13)` | 混合 AP、UT、经度 |
| `Flags(14)` | 三分日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 所有来自 120,000 米温度 (TLB) 的变化 |
| `Flags(18)` | 所有低热层 (TN1) 温度变化 |
| `Flags(19)` | 所有 120,000 米梯度 (S) 变化 |
| `Flags(20)` | 所有上平流层 (TN2) 温度变化 |
| `Flags(21)` | 所有来自 120,000 米值 (ZLB) 的变化 |
| `Flags(22)` | 所有低中间层温度 (TN3) 变化 |
| `Flags(23)` | 湍流层顶标高变化 |

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度源** 参数设置为 `Dialog`。
- 将 **标志源** 参数设置为 `Port`。

**数据类型：** `double`

### **Cd** — 大气阻力系数 标量 | 大小为 *numSat* 的向量

大气阻力系数，指定为标量或大小为 *numSat* 的向量。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **阻力系数源** 参数设置为 `Port`。

**数据类型：** `double`

### **Ad** — 大气阻力面积 标量 | 大小为 *numSat* 的向量

大气阻力面积，指定为标量或大小为 *numSat* 的向量。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **阻力面积源** 参数设置为 `Port`。

**数据类型：** `double`

### **Rcb, 3** — 一个或多个自定义天体的位置 三元素向量 | *numCustom3rdBodies*×3 元素向量

一个或多个自定义天体相对于当前中心天体的位置，位于 ICRF 坐标系中。*numCustom3rdBodies* 是自定义天体的数量。有关详细信息，请参阅 **自定义引力参数 (m^3/s^2)**。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 选中 **包含第三体引力** 复选框。
- 选中 **自定义** 复选框。

**数据类型：** `double`

### **Fraction** — 太阳圆面可见比例，介于 `0`（全食）和 `1`（全日照）之间 | 标量 | *numSat*

从航天器位置可见的太阳圆面比例。*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 选中 **包含太阳辐射压 (SRP)** 复选框。
- 将 **食分源** 设置为 `Port`。

**数据类型：** `double`

### **RC** — 反射率系数 标量或 *numSat* 个值，范围为 `1`≤*RC*≤`2`

反射率系数，指定为标量或 *numSat* 个值，范围为
`1`≤*RC*≤`2`。
*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 选中 **包含太阳辐射压 (SRP)** 复选框。
- 将 **反射率系数源** 参数设置为 `Port`。

**数据类型：** `double`

### **Asrp** — 航天器的横截面积 标量 | *numSat*

太阳可见的航天器横截面积，指定为标量或 *numSat*。模块使用此值计算太阳辐射压产生的加速度。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 选中 **包含太阳辐射压 (SRP)** 复选框。
- 将 **SRP 面积源** 参数设置为 `Port`。

**数据类型：** `double`

### 输出

### **Xicrf** — 航天器位置 三元素向量 | *numSat*×3

航天器相对于（ICRF 或固定坐标系）的位置，在当前时间步长返回为三元素向量或 *numSat*×3 数组，其中 *m* 是航天器数量。**轨道**选项卡中提供的初始条件的大小控制端口维度。*numSat* 是航天器数量。

**数据类型：** `double`

### **Vicrf** — 速度 三元素向量 | *numSat*×3 数组

航天器相对于 ICRF 或固定坐标系的速度，在当前时间步长返回为三元素向量或 *numSat*×3 数组。*numSat*×3 数组。**轨道**选项卡中提供的初始条件的大小控制端口维度。

**数据类型：** `double`

### **qicrf2ff** — 变换 四元素四元数（标量在前）

ICRF 坐标系与固定坐标系之间的变换，在当前时间步长返回为四元素向量（标量在前）。

#### 依赖关系

要启用此端口：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 选中 **输出四元数 (ICRF 到固定坐标系)** 复选框。

**数据类型：** `double`

### **tutc** — 当前时间步长的时间 标量 | 6 元素向量

当前时间步长的时间，返回为：

- 标量 — 如果将 **开始日期/时间** 参数指定为儒略日期。
- 6 元素向量 — 如果将 **开始日期/时间** 参数指定为包含六个元素（年、月、日、小时、分钟、秒）的格里高利日期。

此值等于 **开始日期/时间** 参数值 + *经过的仿真时间*。

#### 依赖关系

要启用此参数，请选中 **输出当前日期/时间 (UTC 儒略日期)** 复选框。

**数据类型：** `double`

## 参数

### 主要

### **传播方法** — 轨道传播方法 `Kepler (unperturbed)` | `Numerical (high precision)`

轨道传播方法，指定为：

- `Kepler (unperturbed)` — 使用开普勒问题的通用变量公式确定每个时间步长的航天器位置和速度。此方法比 `Numerical (high precision)` 更快。
- `Numerical (high precision)` — 使用数值积分确定每个时间步长的航天器位置和速度。此选项基于 **中心天体** 选项卡中的设置对中心天体引力建模。此方法比 `Kepler (unperturbed)` 更准确，但更慢。

#### 程序化使用

|  |
| --- |
| **模块参数：** `propagator` |
| **类型：** character vector |
| **值：** `'Kepler (unperturbed)'` | `'Numerical (high precision)'` |
| **默认值：** `'Kepler (unperturbed)'` |

### **输入外部加速度** — 输入附加加速度 off（默认） | on

要允许将附加外部加速度包含在航天器运动方程的积分中，请选中此复选框。否则，清除此复选框。

#### 依赖关系

要启用此复选框，请将 **传播方法** 设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `accelIn` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **外部加速度坐标系** — 附加加速度的坐标系 `ICRF`（默认） | `Fixed-frame`

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

### **状态向量输出坐标系** — 端口坐标系 `ICRF`（默认） | `Fixed-frame`

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

### **开始日期/时间 (UTC 儒略日期)** — 仿真的初始开始时间 `juliandate (2020, 1, 1, 12, 0, 0)`（默认） | 有效的标量儒略日期 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，以 6 元素向量表示

仿真的初始开始日期和时间，指定为儒略日期或格里高利日期。模块使用此值定义初始条件。

**提示**

要计算儒略日期，请使用 `juliandate` 函数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `startDate` |
| **类型：** character vector |
| **值：** `'juliandate(2020, 1, 1, 12, 0, 0)'` | 有效的标量儒略日期 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，以 6 元素向量表示 |
| **默认值：** `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **输出当前日期/时间 (UTC 儒略日期)** — 添加输出端口 tutc on（默认） | off

要输出当前日期或时间，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dateOut` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **质量源** — 质量源 `Dialog`（默认） | `Port`

质量源，指定为 `Dialog` 或 `Port`。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `massSrc` |
| **类型：** character vector |
| **取值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **Mass** — 用于大气阻力计算的航天器质量 `4.0` (default) | scalar | vector of size *numSat*

用于大气阻力计算的航天器质量，指定为 scalar 或大小为 *numSat* 的 vector。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数：

- 将 **Propagation method** 参数设置为 `Numerical (high precision)`。
- 将 **Central Body** 参数设置为 `Earth`。
- 选中 **Include atmospheric drag** 复选框。
- 将 **Mass source** 设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** character vector |
| **取值：** scalar | vector of size *numSat* |
| **默认值：** `'4.0'` |

### **Action for out-of-range input** — 超出范围的模块行为 `Warning` (default) | `Error` | `None`

超出范围的模块行为，指定如下：

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中发出警告，模型仿真继续。 |
| `Error` (default) | 在诊断查看器中报错，模型仿真停止。 |

#### 编程用法

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **取值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

### Orbit

定义航天器的初始状态。

### **Initial state format** — 轨道初始状态的输入方法 `Orbital elements` (default) | `ICRF state vector` | `Fixed-frame state vector`

轨道初始状态的输入方法，指定为 `Orbital elements`、`ICRF state vector` 或 `Fixed-frame state vector`。

#### 编程用法

|  |
| --- |
| **模块参数** `stateFormatNum` |
| **类型：** character vector |
| **取值：**  `'Orbital elements'` | `'ICRF state vector'` | `'Fixed-frame state vector'` |
| **默认值：** `'Orbital elements'` |

### **Orbit Type** — 轨道分类 `Keplerian` (default) | `Elliptical equatorial` | `Circular` | `Circular equatorial`

轨道分类，指定为：

- `Keplerian` — 使用六个标准 Keplerian 轨道根数对椭圆轨道建模。
- `Elliptical equatorial` — 定义赤道轨道，其中 inclination 为 0 或 180 degrees，且升交点赤经未定义。
- `Circular` — 定义圆轨道，其中偏心率为 0，且近地点幅角未定义。
- `Circular equatorial` — 定义圆轨道，其中偏心率为 0 或 10 degrees。近地点幅角和升交点赤经未定义。

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `Orbital elements`。

#### 编程用法

|  |
| --- |
| **模块参数：** `orbitType` |
| **类型：** character vector |
| **取值：** `'Keplerian'` | `'Elliptical equatorial'` | `'Circular inclined'` | `'Circular equatorial'` |
| **默认值：** `'Keplerian'` |

### **Semi-major axis** — 椭圆长轴的一半 6786000 (default) | 1D array of size *numSat*

椭圆长轴的一半，指定为大小等于航天器数量的 1D array。

- 对于抛物线轨道，此模块将此参数解释为近地点半径（从近地点到轨道焦点的距离）。
- 对于双曲线轨道，此模块将此参数解释为从近地点到双曲线中心的距离。

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `Orbital elements`。

#### 编程用法

|  |
| --- |
| **模块参数：** `semiMajorAxis` |
| **类型：** character vector |
| **取值：** scalar | 1D array of size *m*, number of spacecraft |
| **默认值：** `'6786000'` |

### **Eccentricity** — 轨道偏离度 0.01 (default) | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat*

轨道偏离正圆的程度，指定为 scalar 或大小等于航天器数量的 1D array。

如果 **Orbit** 类型设置为 `Keplerian`，则值可以为：

- `0` 表示圆轨道
- 介于 `0` 和 `1` 之间表示椭圆轨道
- `1` 表示抛物线轨道
- 大于 `1` 表示双曲线轨道

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Elliptical equatorial`。

#### 编程用法

|  |
| --- |
| **模块参数：** `eccentricity` |
| **类型：** character vector |
| **取值：** `0.01` | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat* |
| **默认值：** `'0.01'` |

### **Inclination (deg)** — 轨道平面倾角 50 (default) | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi

在升交点处测量的椭圆相对于参考平面的垂直倾角，指定为 scalar 或大小为 *numSat* 的 1D array，以指定单位表示。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`
- 将 **Orbit type** 设置为 `Keplerian` 或 `Circular inclined`

#### 编程用法

|  |
| --- |
| **模块参数：** `inclination` |
| **类型：** character vector |
| **取值：** 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi |
| **默认值：** `'50'` |

### **RAAN (deg)** — 赤道面内的角距离 95 (default) | scalar value between `0` and `360` | 1D array of size *numSat*

升交点赤经 (RAAN)，指定为介于 `0` 和 `360` 之间的 scalar value 或大小为 *numSat* 的 1D array，以指定单位表示。*numSat* 是航天器数量。RAAN 是沿参考平面从 ICRF *x* 轴到升交点位置（航天器从南向北穿过参考平面的点）的角距离。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Circular inclined`。

#### 编程用法

|  |
| --- |
| **模块参数：** `raan` |
| **类型：** character vector |
| **取值：** `95` | scalar value between `0` and `360` | 1D array of size *m* number of spacecraft |
| **默认值：** `'95'` |

### **Argument of periapsis (deg)** — 从航天器升交点到近地点的角度 93 (default) | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *m*, number of spacecraft

从航天器升交点到近地点（轨道距中心天体最近的点）的角度，指定为大小为 *m* 的 1D array，其中 *m* 是航天器数量，以指定单位表示。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`
- 将 **Orbit type** 设置为 `Keplerian`

#### 编程用法

|  |
| --- |
| **模块参数：** `argPeriapsis` |
| **类型：** character vector |
| **取值：** `'95'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **默认值：** `'93'` |

### **True anomaly** — 近地点与航天器初始位置之间的角度 203 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

近地点（轨道距中心天体最近的点）与航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为 scalar 或大小为 *numSat* 的 1D array，以指定单位表示。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Elliptical inclined`。

#### 编程用法

|  |
| --- |
| **模块参数：** `trueAnomaly` |
| **类型：** character vector |
| **取值：** `'203'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'203'` |

### **Argument of latitude (deg)** — 升交点与航天器初始位置之间的角度 200 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

升交点与航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为 scalar、3-element vector 或大小等于航天器数量的 1D array，以指定单位表示。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit Type** 设置为 `Circular inclined`。

#### 编程用法

|  |
| --- |
| **模块参数：** `argLat` |
| **类型：** character vector |
| **取值：** `'200'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'200'` |

### **Longitude of periapsis (deg)** — ICRF *x* 轴与偏心率矢量之间的角度 100 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

ICRF x 轴与偏心率矢量之间的角度，指定为 scalar、3-element vector 或大小等于航天器数量的 1D array，以指定单位表示。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Elliptical equatorial`。

#### 编程用法

|  |
| --- |
| **模块参数：** `lonPeriapsis` |
| **类型：** character vector |
| **取值：** 100 | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *m*, number of spacecraft |
| **默认值：** `'100'` |

### **True longitude (deg)** — ICRF *x* 轴与航天器初始位置之间的角度 150 (default) | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat*

ICRF x 轴与航天器在 **Start date/time** 时沿其轨道的初始位置之间的角度，指定为 scalar 或大小为 *numSat* 的 1D array，以指定单位表示。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请设置：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Circular equatorial`。

#### 编程用法

|  |
| --- |
| **模块参数：** `trueLon` |
| **类型：** character vector |
| **取值：** `'150'` | scalar | degrees between `0` and `360` | radians between `0` and `2*pi` | 1D array of size *numSat* |
| **默认值：** `'150'` |

### **ICRF position** — 航天器的笛卡尔位置矢量 `[3649700.0 3308200.0 -4676600.0]` (default) | 3-element vector | | *numSat*-by-3 array

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔位置矢量，指定为单个航天器的 3-element vector 或多个航天器的 *numSat*-by-3 array。*numSat* 是航天器数量。

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `ICRF state vector`。

#### 编程用法

|  |
| --- |
| **模块参数：** `inertialPosition` |
| **类型：** character vector |
| **取值：** `[3649700.0 3308200.0 -4676600.0]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF velocity** — 航天器的笛卡尔速度矢量 `[-2750.8 6666.4 2573.4]` (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔速度矢量，指定为单个航天器的 3-element vector 或多个航天器的 *m*-by-3 array 的 2-D array。

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `ICRF state vector`。

#### 编程用法

|  |
| --- |
| **模块参数：** `inertialVelocity` |
| **类型：** character vector |
| **取值：** `[-2750.8 6666.4 2573.4]` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame position** — 航天器的位置矢量 [-4142689.0 -2676864.7 -4669861.6] (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

在 **Start date/time** 时，航天器在 fixed-frame 坐标系中的笛卡尔位置矢量，指定为单个航天器的 3-element vector 或多个航天器的 *m*-by-3 array 的 2-D array。

#### 依赖关系

要启用此参数，请设置：

- 将 **Propagation method** 设置为 `Numerical (high precision)`。
- 将 **Initial state format** 设置为 `Fixed-frame state vector`。

#### 编程用法

|  |
| --- |
| **模块参数：** `fixedPosition` |
| **类型：** character vector |
| **取值：** `'[-4142689.0 -2676864.7 -4669861.6]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame velocity** — 航天器的速度矢量 [1452.7 -6720.7 2568.1] (default) | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft

在 **Start date/time** 时，航天器在 fixed-frame 坐标系中的笛卡尔速度矢量，指定为单个航天器的 3-element vector 或多个航天器的 *m*-by-3 array 的 2-D array。

#### 依赖关系

要启用此参数，请设置：

- 将 **Propagation method** 设置为 `Numerical (high precision)`。
- 将 **Initial state format** 设置为 `Fixed-frame state vector`。

#### 编程用法

|  |
| --- |
| **模块参数：** `fixedVelocity` |
| **类型：** character vector |
| **取值：** `'[1452.7 -6720.7 2568.1]'` | 3-element vector for single spacecraft or 2-D array of size *m*-by-3 array of multiple spacecraft |
| **默认值：** `'[1452.7 -6720.7 2568.1]'` |

### Central Body

配置航天器环绕运行的中心天体环境。

### **Central body** — 航天器环绕运行的天体 `Earth` (default) | `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune`、`Sun` 或 `Custom`，在 **Orbit** 选项卡中定义的航天器环绕该天体运行。

#### 编程用法

|  |
| --- |
| **模块参数：** `centralBody` |
| **类型：** character vector |
| **取值：** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Sun'` | `'Custom'` | |
| **默认值：** `'Earth'` |

### **Gravitational potential model** — 控制中心天体的重力模型 当 **Central body** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom` 时为 `Spherical harmonics`，当 **Central body** 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 Oblate ellipsoid (default) | `None` | `Point-mass` | `Oblate ellipsoid (J2)`

控制中心天体的重力模型，指定为 `Spherical harmonics`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 依赖关系

要启用此参数，请将 **Propagation method** 设置为 `Numerical (high precision)`。可用选项基于 **Central body** 设置：

| Earth、Moon、Mars 或 Custom | Mercury、Venus、Jupiter、Saturn、Uranus 或 Neptune |
| --- | --- |
| `None` | `None` |
| `Spherical harmonics` | `Oblate ellipsoid (J2)` |
| `Point-mass` | `Point-mass` |
| `Oblate ellipsoid (J2)` | — |

#### 程序化使用

|  |
| --- |
| **模块参数：** `gravityModel` 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时 | `gravityModelnoSH` 当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时 |
| **类型：** character vector |
| **取值：** `'Spherical harmonics'` | `'None'` | `'Point-mass'` | `'Oblate ellipsoid (J2)'` 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时；`'Point-mass'` | `'Oblate ellipsoid (J2)'` 当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时 |
| **默认值：** `'Spherical harmonics'` 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时；`'Oblate ellipsoid (J2)'` 当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时 |

### **球谐模型** — 当 **中心天体** 设置为 `Earth` 时使用球谐模型 `EGM2008`，当 **中心天体** 设置为 `Moon` 时使用 `LP-100K`，当 **中心天体** 设置为 `Mars` 时使用 `GMM2B`，(默认) | `EGM96` | `EIGEN-GL04C` | `LP-165P`

球谐引力势模型，根据指定的 **中心天体** 指定。

#### 依赖项

要启用此参数，请将 **传播方法** 设置为 `Numerical (high precision)`。可用选项基于 **中心天体** 设置：

| 中心天体 | 球谐模型选项 |
| --- | --- |
| Earth | EGM2008、EGM96 或 EIGEN-GL04C |
| Moon | LP-100K 或 LP-165P |
| Mars | GMM2B |

#### 程序化使用

|  |
| --- |
| **模块参数：** `'earthSH'` 当 `centralBody` 设置为 `'Earth'` 时 | `'moonSH'` 当 `centralBody` 设置为 `'Moon'` 时 | `'marsSH'` 当 `centralBody` 设置为 `'Mars'` 时 |
| **类型：** character vector |
| **取值：** `'EGM2008'` | `'EGM96'` | `'EIGEN-GL04C'` 当 `centralBody` 设置为 `'earthSH'` 时；`'LP-100K'` | `'LP-165P'` 当 `centralBody` 设置为 `'moonSH'` 时；`'GMM2B'` 当 `centralBody` 设置为 `'marsSH'` 时 |
| **默认值：** `'Spherical harmonics'` |

### **球谐系数文件** — 调和系数 MAT 文件 `aerogmm2b.mat` (默认) | 球谐系数 MAT 文件

包含自定义行星模型定义的调和系数 MAT 文件，指定为 character vector 或 string。

此文件必须包含：

| 变量 | 描述 |
| --- | --- |
| *Re* | 行星赤道半径的标量，以 meters (m) 为单位。 |
| *GM* | 行星引力参数的标量，以 meters cubed per second squared (m3/s2) 为单位。 |
| *degree* | 最大阶数的标量。 |
| *C* | 包含归一化球谐系数矩阵 *C* 的 (*degree*+1)×(*degree*+1) 矩阵。 |
| *S* | 包含归一化球谐系数矩阵 *S* 的 (*degree*+1)×(*degree*+1) 矩阵。 |

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **引力势模型** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `shFile` |
| **类型：** character vector |
| **取值：** `'aerogmm2b.mat'` | 球谐系数 MAT 文件 |
| **默认值：** `'aerogmm2b.mat'` |

### **阶数** — 调和模型的阶数 `120` (默认) | scalar | 最大为 2159

调和模型的阶数，指定为 double scalar：

| 行星模型 | 建议阶数 | 最大阶数 |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |
| `Custom` | — | 最大阶数从球谐系数文件中提取。 |

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom`。
- 将 **引力势模型** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `shDegree` |
| **类型：** character vector |
| **取值：** `'80'` | scalar |
| **默认值：** `'80'` |

### **使用地球定向参数 (EOPs)** — 使用地球定向参数 on (默认) | off

选中此复选框以使用地球定向参数进行 ICRF 与 Fixed-frame 坐标系之间的转换。否则，清除此复选框。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Earth`。

此外，它必须满足以下条件之一：

- **引力势模型** 设置为 `Spherical harmonics` 或 `Oblate ellipsoid (J2)` 之一。
- **外部加速度坐标系** 设置为 `Fixed-frame`。
- **状态矢量输出坐标系** 设置为 `Fixed-frame`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useEOPs` |
| **类型：** character vector |
| **取值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **IERS EOP 数据文件** — 地球定向数据 `aeroiersdata.mat` (默认) | MAT 文件

自定义地球定向数据列表，在 MAT 文件中指定。

#### 依赖项

要启用此参数：

- 选中 **使用地球定向参数 (EOPs)** 复选框。
- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eopFile` |
| **类型：** character vector |
| **取值：** `'aeroiersdata.mat'` | `MAT file` |
| **默认值：** `'aeroiersdata.mat'` |

### **输入月球天平动角** — 月球天平动角速率 off (默认) | on

要为月球定向指定天平动角 (φ θ ψ)，请选中此复选框。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Moon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useMoonLib` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **输出四元数 (ICRF 到 Fixed-frame)** — 添加输出变换四元数端口 off (默认) | on

要添加用于从 ICRF 到 Fixed-frame 坐标系的四元数变换的输出变换四元数端口，请选中此复选框。

#### 依赖项

要启用此复选框，请将 **传播方法** 设置为 `Numerical (high precision)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outputTransform` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **中心天体自转轴来源** — 中心天体自转来源 `Port` (默认) | `Dialog`

中心天体自转轴，指定为 `Port` 或 `Dialog`。该模块使用自转轴来计算自定义中心天体的从 ICRF 到 Fixed-frame 坐标系的转换。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbPoleSrc` |
| **类型：** character vector |
| **取值：** `'Port'` | `'Dialog'` |
| **默认值：** `'Port'` |

### **J2000 时自转轴赤经 (RA) (deg)** — J2000 时中心天体自转轴的赤经 `317.68143` (默认) | double scalar

J2000 时中心天体自转轴的赤经 (2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT)，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRA` |
| **类型：** character vector |
| **取值：** `'317.68143'` | double scalar |
| **默认值：** `'317.68143'` |

### **自转轴赤经变化率 (deg/century)** — 中心天体自转轴的赤经变化率 `-0.1061` (默认) | double scalar

中心天体自转轴的赤经变化率，指定为 double scalar，以指定的角度单位/century 为单位。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRARate` |
| **类型：** character vector |
| **取值：** `'-0.1061'` | double scalar |
| **默认值：** `'-0.1061'` |

### **J2000 时自转轴赤纬 (Dec) (deg)** — J2000 时中心天体自转轴的赤纬 `52.88650` (默认) | double scalar

J2000 时中心天体自转轴的赤纬 (2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT)，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDec` |
| **类型：** character vector |
| **取值：** `'52.88650'` | double scalar |
| **默认值：** `'52.88650'` |

### **自转轴赤纬变化率 (deg/century)** — 中心天体自转轴的赤纬变化率 `-0.0609` (默认) | double scalar

中心天体自转轴的赤纬变化率，指定为 double scalar，以指定的角度单位/century 为单位。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDecRate` |
| **类型：** character vector |
| **取值：** `'-0.0609'` | double scalar |
| **默认值：** `'-0.0609'` |

### **J2000 时的初始旋转角 (deg)** — 中心天体 *x* 轴的旋转角 `176.630` (默认) | double scalar

J2000 时中心天体 x 轴相对于 ICRF *x* 轴的旋转角 (2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT)，指定为 double scalar，以指定的角度单位为单位。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotAngle` |
| **类型：** character vector |
| **取值：** `'176.630'` | double scalar |
| **默认值：** `'176.630'` |

### **旋转速率 (deg/day)** — 中心天体 *x* 轴的旋转速率 `350.89198226` (默认) | double scalar

中心天体 x 轴相对于 ICRF *x* 轴的旋转速率 (2451545.0 JD，2000 年 1 月 1 日 12:00:00 UTC)，指定为 double scalar，以指定的角度单位/day 为单位。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **中心天体自转轴来源** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotRate` |
| **类型：** character vector |
| **取值：** `'350.89198226'` | double scalar |
| **默认值：** `'350.89198226'` |

### **赤道半径** — 赤道半径 `3396200` (默认) | double scalar

自定义中心天体的赤道半径，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **引力势模型** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customR` |
| **类型：** character vector |
| **取值：** `'3396200'` | double scalar |
| **默认值：** `'3396200'` |

### **扁率** — 行星扁率 `0.00589` (默认) | double scalar

自定义中心天体的行星扁率，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **中心天体** 设置为 `Custom`。
- 将 **引力势模型** 设置为 `Point-mass`、`Oblate ellipsoid (J2)` 或 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customF` |
| **类型：** character vector |
| **取值：** `'0.00589'` | double scalar |
| **默认值：** `'0.00589'` |

### **引力参数** — 引力参数 `4.305e13` (默认) | double scalar

自定义中心天体的引力参数，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **中心天体** 设置为 `Custom`。
- 将 **引力势模型** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customMu` |
| **类型：** character vector |
| **取值：** `'4.305e13'` | double scalar |
| **默认值：** `'4.305e13'` |

### **二阶带谐项 (J2)** — 最重要或最大的球谐项 `1.0826269e-03` (默认) | double scalar

最重要或最大的球谐项，用于说明天体的扁率，指定为 double scalar。

#### 依赖项

要启用此参数，请设置：

- 将 **传播方法** 设置为 `Numerical (high precision)`。
- 将 **中心天体** 设置为 `Custom`。
- 将 **引力势模型** 设置为 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customJ2` |
| **类型：** character vector |
| **取值：** `'1.0826269e-03'` | double scalar |
| **默认值：** `'1.0826269e-03'` |

### 阻力

配置大气阻力环境。

### **包含大气阻力** — 包含大气阻力的选项 off (默认) | on

要包含大气阻力，请选中此复选框。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useDrag` |
| **类型：** character vector |
| **取值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **大气密度来源** — 大气密度值的来源 `Dialog` (默认) | `Port`

大气密度值的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `atmosSrc` |
| **类型：** character vector |
| **取值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **大气模型** — 大气模型 `NRLMSISE-00` (默认)

用于大气阻力计算的大气模型，指定为 `NRLMSISE-00`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `atmosModel` |
| **类型：** character vector |
| **取值：** `'NRLMSISE-00'` |
| **默认值：** `'NRLMSISE-00'` |

### **通量来源** — 空间天气数据来源 `Dialog` (默认) | `Port`

用于大气密度计算的历史和预测通量及地磁指数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fluxSrc` |
| **类型：** character vector |
| **取值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **空间气象数据文件** — 空间气象数据的 MAT 文件 `aeroSpaceWeatherData.mat`（默认）| MAT 文件名

空间气象数据的 MAT 文件。此文件是 `aeroReadSpaceWeatherData` 函数的输出。

Aerospace Blockset™ 包含默认空间气象数据文件 `aeroSpaceWeatherData.mat`。要使用可用的最新数据，请使用 `aeroReadSpaceWeatherData` 生成新的 MAT 文件，并为该参数指定文件名。有关详细信息，请参阅 `aeroReadSpaceWeatherData`。

如果该文件不在 MATLAB® 路径上，请指定完整路径名。MAT 文件必须包含空间气象数据文件中的这些变量：

- `YEAR`
- `MONTH`
- `DAY`
- `AP1`
- `AP2`
- `AP3`
- `AP4`
- `AP5`
- `AP6`
- `AP7`
- `AP8`
- `AP_AVG`
- `F107_OBS`
- `F107_DATA_TYPE`
- `F107_OBS_CENTER81`

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数**：`SpaceWeatherDataFile` |
| **类型**：character vector |
| **值**：`'aeroSpaceWeatherData.mat'` | MAT 文件名 |
| **默认**：`'aeroSpaceWeatherData.mat'` |

### **F10.7 外推方法** — `f107Average` 和 `f107Daily` 的外推方法 `None - clip`（默认）| `Constant` | `Least squares fit`

`f107Average` 和 `f107Daily` 在 MAT 文件数据范围之外时间的外推方法，指定为下列值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将 `f107Average` 和 `f107Daily` 设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将 `f107Average` 和 `f107Daily` 设置为由 **磁指数外推方法** 参数值指定的常量值。 |
| `Least squares fit` | 使用从 1957 年 10 月 1 日到 2040 年 12 月 1 日的空间气象数据的最小二乘拟合来近似 `f107Average` 和 `f107Daily`。此方法使用以下形式的三角函数：`a + b*cos(c*t + d*sin(e*t))`，其中：  - *a* 为 `128.2351780622538` - *b* 为 `54.3285872213434` - *c* 为 `0.0015460708364` - *d* 为 `0.2429462096495` - *e* 为 `0.0015563188188` - `t` 为 *jdCurrent* - *jdReftime* - *jdCurrent* 是当前儒略日 - *jdRef* 为 `2436112.5` |

**注意**

对于 `f107Average` 值，如果 81 天周期的一部分落在 MAT 文件的空间气象数据范围内，Solar Flux and Geomagnetic Index 模块使用重叠部分的实际每日值。为了计算非重叠部分的平均值，该模块使用裁剪、常量或最小二乘每日值。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数**：`F107ExtrapMethod` |
| **类型**：character vector |
| **值**：`'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **默认**：`'None - clip'` |

### **F10.7 外推值** — 要分配给 `f107Average` 并用于计算 `f107Daily` 的外推值 `150.0`（默认）| scalar

要分配给 `f107Average` 并用于计算 `f107Daily` 的外推值，指定为 scalar。

**可调：** 是

#### 依赖项

在以下情况下会分配此值：

- **F10.7 外推方法** 设置为 `Constant`。
- 由 **Year**、**DOY** 和 **UT (sec)** 端口指定的时间在 MAT 文件中数据范围之外。

#### 编程用法

|  |
| --- |
| **模块参数**：`F107ExtrapValue` |
| **类型**：character vector |
| **值**：`'150.0'` | scalar |
| **默认**：`'150.0'` |

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。
- 将 **F10.7 外推方法** 设置为 `Constant`。

### **磁指数外推方法** — 磁指数信息的外推方法 `None - clip`（默认）| `Constant` | `IGRF`

用于 MAT 文件数据范围之外时间的磁指数信息值的外推方法，指定为下列值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将磁指数信息的元素设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将磁指数信息的元素设置为由 **磁指数外推方法** 参数指定的常量值。此范围之外时间的磁指数元素基于这些时间界限处水平磁场强度的裁剪值。 |
| `IGRF` | 使用国际地磁参考场计算磁指数信息的元素。由于此模型定义为 1900 年 1 月 1 日 12:00 AM UTC 到 2025 年 1 月 1 日 12:00 AM UTC 之间的时间，因此此范围之外时间的预测会被裁剪到这些时间界限处的值。 |

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数**：`MagneticIndexExtrapMethod` |
| **类型**：character vector |
| **值**：`'None - clip'` | `'Constant'` | `'IGRF'` |
| **默认**：`'None - clip'` |

### **磁指数外推值** — 用于计算磁指数元素的外推值 `4.0`（默认）| scalar

用于计算磁指数元素的外推值，指定为 scalar。

**可调：** 是

#### 依赖项

当 **磁指数外推方法** 设置为 `Constant` 时，此参数启用。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数**：`MagneticIndexExtrapValue` |
| **类型**：character vector |
| **值**：`'4.0'` | scalar |
| **默认**：`'4.0'` |

### **标志源** — 变化标志来源 `Dialog`（默认）| `Port`

变化标志来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 参数设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数：** `fluxFlagsSrc` |
| **类型：** character vector |
| **值：** `'Dialog'` | `'Port'` |
| **默认：** `'Dialog'` |

### **标志** — 变化标志 `ones(1,23)`（默认）

变化标志，指定为 23 个元素的数组（`ones(1,23)`）。可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0 — 移除对输出的影响。
- 1.0 — 将该值的主效应和交叉项效应用于输出。
- 2.0 — 仅将该值的交叉项效应用于输出。

该数组包含以下字段。

| 字段 | 描述 |
| --- | --- |
| `Flags(1)` | 对均值的 F10.7 效应 |
| `Flags(2)` | 与时间无关 |
| `Flags(3)` | 对称年变化 |
| `Flags(4)` | 对称半年变化 |
| `Flags(5)` | 非对称年变化 |
| `Flags(6)` | 非对称半年变化 |
| `Flags(7)` | 日变化 |
| `Flags(8)` | 半日变化 |
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，则该模块使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)`。 |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度 |
| `Flags(12)` | UT 和混合 UT、经度 |
| `Flags(13)` | 混合 AP、UT、经度 |
| `Flags(14)` | 三分日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 来自 120,000 meter 温度 (TLB) 的所有变化 |
| `Flags(18)` | 所有低热层 (TN1) 温度变化 |
| `Flags(19)` | 所有 120,000 meter 梯度 (S) 变化 |
| `Flags(20)` | 所有上平流层 (TN2) 温度变化 |
| `Flags(21)` | 来自 120,000 meter 值 (ZLB) 的所有变化 |
| `Flags(22)` | 所有下中间层 (TN3) 温度变化 |
| `Flags(23)` | 湍流层顶标高变化 |

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **标志源** 设置为 `Dialog`。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 参数设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数：** `fluxFlags` |
| **类型：** character vector |
| **值：** `'ones(1,23)'` |
| **默认：** `'ones(1,23)'` |

### **在密度计算中包含异常氧** — 在密度计算中包含异常氧的选项 off（默认）| on

要在密度计算中包含异常氧，请选中此复选框。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **大气密度来源** 参数设置为 `Dialog`。
- 将 **大气模型** 参数设置为 `NRLMSISE-00`。

#### 编程用法

|  |
| --- |
| **模块参数：** `useOxygen` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **阻力系数来源** — 阻力系数的来源 `Dialog`（默认）| `Port`

阻力系数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `dragCoeffSrc` |
| **类型：** character vector |
| **值：** `'Dialog'` | `'Source'` |
| **默认：** `'Dialog'` |

### **阻力系数** — 航天器阻力系数 2.179（默认）| scalar | vector of size *numSat*

大气阻力计算使用的航天器阻力系数，指定为 scalar 或大小为 *numSat* 的 vector。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **阻力系数来源** 参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `dragCoeff` |
| **类型：** character vector |
| **值：** scalar | vector of size *numSat* |
| **默认：** `'2.179'` |

### **阻力面积来源** — 阻力面积的来源 `Dialog`（默认）| `Port`

阻力面积的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `dragAreaSrc` |
| **类型：** character vector |
| **值：** `'Dialog'` | `'Source'` |
| **默认：** `'Dialog'` |

### **阻力面积** — 用于计算大气阻力所致加速度的面积 1.0（默认）| scalar | vector of size *numSat*

用于计算大气阻力所致加速度的面积，指定为 scalar 或大小为 *numSat* 的 vector。航天器的该面积垂直于航天器相对速度。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为 `Earth`。
- 选中 **包含大气阻力** 复选框。
- 将 **阻力面积来源** 参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数：** `dragArea` |
| **类型：** character vector |
| **值：** scalar | vector of size *numSat* |
| **默认：** `'1.0'` |

### Third Body

配置用于引力加速度的第三体点质量。

### **星历模型** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择 Jet Propulsion Laboratory 定义的一种星历模型。该模块使用星历数据计算第三体点质量引力和太阳辐射压力所需的相对天体位置。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 发布于 1998 年。此星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）到 2525008.50（2201 年 2 月 20 日）。该模块相对于 1998 年采用的 International Celestial Reference Frame 版本 1.0 实现这些星历。 |
| `DE421` | 发布于 2008 年。此星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）到 2469808.5（2050 年 1 月 2 日）。该模块相对于 1998 年采用的 International Celestial Reference Frame 版本 1.0 实现这些星历。 |
| `DE423` | 发布于 2010 年。此星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）到 2524624.5（2200 年 2 月 1 日）。该模块相对于 2010 年采用的 International Celestial Reference Frame 版本 2.0 实现这些星历。 |
| `DE430` | 发布于 2013 年。此星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）到 2688976.5（2650 年 1 月 25 日）。该模块相对于 2010 年采用的 International Celestial Reference Frame 版本 2.0 实现这些星历。 |
| `DE432t` | 发布于 2014 年 4 月。此星历考虑的儒略日范围为 2287184.5,（1549 年 12 月 21 日）到 2688976.5,（2650 年 1 月 25 日）。该模块相对于 2010 年采用的 International Celestial Reference Frame 版本 2.0 实现这些星历。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，点击 **Add-Ons**。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ephemerisModel` |
| **类型**：character vector |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认**：`'DE405'` |

### **限制星历日期范围** — 用于启用星历数据范围起始和结束的选项 `off` (默认) | `on`

控制在仿真期间加载到内存中的数据量，以及为该模块生成的代码中包含的数据量：

- 选中此复选框，将星历数据的加载限制在指定日期范围内。
- 清除此复选框，以包含 **星历模型** 表中定义的完整日期范围的数据。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。

#### 编程使用

|  |
| --- |
| **模块参数**: `useDateRange` |
| **类型**: character vector |
| **值**: `'off'` | `'on'` |
| **默认值**: `'off'` |

### **起始日期 (JD)** — 星历日期范围的起始日期 `juliandate(2020, 1, 1)` (默认) | 儒略日期

星历日期范围的起始日期，指定为儒略日期。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 选中 **限制星历日期范围** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**: `startDate` |
| **类型**: character vector |
| **值**: `'juliandate(2020, 1, 1)'` | 儒略日期 |
| **默认值**: `'juliandate(2020, 1, 1)'` |

### **结束日期 (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)` (默认) | 儒略日期

星历日期范围的结束日期，指定为儒略日期。

#### 依赖关系

要启用此参数，请选中 **限制星历日期范围** 复选框。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **限制星历日期范围** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**: `endDate` |
| **类型**: character vector |
| **值**: `'juliandate(2050, 1, 1)'` | 儒略格式日期 |
| **默认值**: `'juliandate(2050, 1, 1)'` |

### **包括第三体引力** — 由第三体引力引起的加速度 `off` (默认) | `on`

要在轨道传播计算中包括由第三体引力引起的加速度，请选中此复选框。否则，请清除此复选框。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。

#### 编程使用

|  |
| --- |
| **模块参数:** `useThirdBodyGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **太阳** — 包括由太阳引起的引力加速度 `on` (默认) | `off`

要包括由太阳引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从太阳引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Sun` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeSunGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'on'` |

### **太阳引力模型** — 太阳的第三体引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **太阳** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Sun` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **太阳** 第三体引力参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `sunThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **水星** — 包括由水星引起的引力加速度 `off` (默认) | `on`

要包括由水星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从水星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Mercury` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeMercuryGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **水星引力模型** — 水星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **水星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Sun` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **水星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `mercuryThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **金星** — 包括由金星引起的引力加速度 `off` (默认) | `on`

要包括由金星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从金星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Venus` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeVenusGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **金星引力模型** — 金星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **金星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Sun` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **金星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `venusThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **地球** — 包括由地球引起的引力加速度 `on` (默认) | `off`

要包括由地球引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从地球引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Earth` 的值。
- 将 **包括第三体引力** 设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeEarthGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **地球引力模型** — 地球引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **地球** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Earth` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **地球** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `earthThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值:** `'Point-mass'` |

### **月球** — 包括由月球引起的引力加速度 `on` (默认) | `off`

要包括由月球引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从月球引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Moon` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeMoonGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` | |
| **默认值:** `'on'` |

### **月球引力模型** — 月球引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **月球** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Moon` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **月球** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `moonThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值:** `'Point-mass'` |

### **火星** — 包括由火星引起的引力加速度 `off` (默认) | `on`

要包括由火星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从火星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Mars` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeMarsGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` | |
| **默认值:** `'off'` |

### **火星引力模型** — 火星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **火星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Mars` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **火星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `marsThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值:** `'Point-mass'` |

### **木星** — 包括由木星引起的引力加速度 `off` (默认) | `on`

要包括由木星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从木星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Jupiter` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeJupiterGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **木星引力模型** — 木星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **木星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Jupiter` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **木星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `jupiterThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **土星** — 包括由土星引起的引力加速度 `off` (默认) | `on`

要包括由土星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从土星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Saturn` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeSaturnGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **土星引力模型** — 土星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **土星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Saturn` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **土星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `saturnThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **天王星** — 包括由天王星引起的引力加速度 `off` (默认) | `on`

要包括由天王星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从天王星引力模型中选择。

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Uranus` 的值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数:** `includeUranusGravity` |
| **类型:** character vector |
| **值**: `'off'` | `'on'` |
| **默认值:** `'off'` |

### **天王星引力模型** — 天王星引力模型 `Point-mass` (默认) | `Oblate ellipsoid (J2)`

当选择 **天王星** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为任何不等于 `Uranus` 的值。
- 选中 **包括第三体引力** 参数。
- 选中 **天王星** 参数。

#### 编程使用

|  |
| --- |
| **模块参数:** `uranusThirdBodyGravityModel` |
| **类型:** character vector |
| **值**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值:** `'Point-mass'` |

### **海王星** — 包括由海王星引起的引力加速度 `off`（默认） | `on`

要包括由海王星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从海王星引力模型中选择。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为除 `Neptune` 之外的任何值。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数：** `includeNeptuneGravity` |
| **类型：** character vector |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **海王星引力模型** — 海王星引力模型 `Point-mass`（默认） | `Oblate ellipsoid (J2)`

从列表中选择一个引力势模型，以便在选中 **海王星** 第三体引力参数时使用。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为除 `Neptune` 之外的任何值。
- 选中 **包括第三体引力** 参数。
- 选中 **海王星** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `neptuneThirdBodyGravityModel` |
| **类型：** character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **冥王星** — 包括由冥王星引起的引力加速度 `off`（默认） | `on`

要包括由冥王星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从冥王星引力模型中选择。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数：** `includePlutoGravity` |
| **类型：** character vector |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **冥王星引力模型** — 冥王星引力模型 `Point-mass`（默认） | `Oblate ellipsoid (J2)`

从列表中选择一个引力势模型，以便在选中 **冥王星** 第三体引力参数时使用。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 选中 **包括第三体引力** 参数。
- 选中 **冥王星** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `plutoThirdBodyGravityModel` |
| **类型：** character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **自定义** — 包括由自定义行星引起的引力加速度 `off`（默认） | `on`

要包括由自定义行星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从自定义引力模型中选择。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括第三体引力** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数：** `includeCustomGravity` |
| **类型：** character vector |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **自定义引力模型** — 自定义引力模型 `Point-mass`（默认） | `Oblate ellipsoid (J2)` | `Spherical harmonics`

从列表中选择一个引力势模型，以便在选中 **自定义** 第三体引力参数时使用。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **中心天体** 参数设置为除 `Sun` 之外的任何值。
- 选中 **包括第三体引力** 参数。
- 选中 **自定义** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `customThirdBodyGravityModel` |
| **类型：** character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **引力参数 (m^3/s^2)** — 自定义引力加速度 `42.828314258067e12`（默认） | 标量 | 长度为 *numCustom3rdBodies* 的向量

用于自定义第三体的自定义引力加速度，指定为标量或长度为 *numCustom3rdBodies* 的向量。*numCustom3rdBodies* 是提供给 **R\_cb** 输入端口的行数。提供多个值以包括多个自定义天体。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括第三体引力** 参数设置为 `on`。
- 将 **自定义** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数：** `customThirdBodyMu` |
| **类型：** character vector |
| **值**：`'42.828314258067e12'` | 标量 | 长度为 *numCustom3rdBodies* 的向量 |
| **默认值：** `'42.828314258067e12'` |

### SRP

### **包括太阳辐射压力 (SRP)** — 由太阳辐射压力引起的加速度 `off`（默认） | `on`

要在轨道传播计算中包括由太阳辐射压力引起的加速度，请选中此复选框。否则，请清除此复选框。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。

#### 编程用法

|  |
| --- |
| **模块参数**：`useSRP` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **食分来源** — 食分的来源 `Dialog`（默认） | `Port`

食分（从航天器位置可见的太阳圆盘比例）的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括太阳辐射压力 (SRP)** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数**：`useSRP` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Port'` |
| **默认值**：`'Dialog'` |

### **阴影模型** — 阴影模型 `Dual cone`（默认） | `Cylindrical`

用于食计算的阴影模型，指定为以下值之一。

- `Cylindrical` — 分数可以是 0.0（本影）或 1.0（阳光）。
- `Dual cone` — 分数可以是 0.0（本影）、介于 0.0 和 1.0 之间（半影或伪本影），或 1.0（阳光）。

#### 编程用法

|  |
| --- |
| **模块参数：** `shadowModel` |
| **类型：** character vector |
| **值：** `'Dual cone'` | `'Cylindrical'` |
| **默认值：** `'Dual cone'` |

### **包括地球** — 包含地球的选项 `on`（默认） | `off`

当中心天体为月球时，在食计算中将地球作为次要遮挡天体的选项。

#### 依赖项

将 **中心天体** 参数设置为 `Moon`。

#### 编程用法

|  |
| --- |
| **模块参数**：`includeEarth` |
| **类型**：character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

### **包括月球** — 包含月球的选项 `on`（默认） | `off`

当中心天体为地球时，在食计算中将月球作为次要遮挡天体的选项。

#### 依赖项

将 **中心天体** 参数设置为 `Earth`。

#### 编程用法

|  |
| --- |
| **模块参数**：`includeMoon` |
| **类型**：character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'on'` |

### **反射率系数来源** — 航天器反射率系数的来源 `'Dialog'`（默认） | `'Port'`

航天器反射率系数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此复选框：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 选中 **包括太阳辐射压力 (SRP)** 复选框。

#### 编程用法

|  |
| --- |
| **模块参数**：`reflectivityCoeffSrc` |
| **类型**：character vector |
| **值：** `'Dialog'` | `'Port'` |
| **默认值：** `'on'` |

### **反射率系数** — 航天器反射率系数 `1.8`（默认） | 标量 | 大小为 *numSat* 的二维数组 | 介于 `[1,2]` 之间

用于太阳辐射压力计算的航天器反射率系数，指定为标量或大小为 *numSat* 的二维数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括太阳辐射压力 (SRP)** 参数设置为 `on`。
- 将 **反射率系数来源** 参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数**：`reflectivityCoeff` |
| **类型**：character vector |
| **值：** `'1.8'` | 标量 | 大小为 *numSat* 的二维数组 | 介于 `[1,2]` 之间 |
| **默认值：** `'1.8'` |

### **SRP 面积来源** — 航天器太阳辐射压力面积的来源 `Dialog`（默认） | `Port`

航天器太阳辐射压力 (SRP) 面积的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括太阳辐射压力 (SRP)** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数**：`srpAreaSrc` |
| **类型**：character vector |
| **值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **SRP 面积** — 太阳所见的航天器横截面积 `1.0`（默认） | 标量 | 大小为 *numSat* 的二维数组

太阳所见的航天器横截面积，指定为标量或大小为 *numSat* 的二维数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括太阳辐射压力 (SRP)** 参数设置为 `on`。
- 将 **SRP 面积来源** 参数设置为 `Dialog`。

#### 编程用法

|  |
| --- |
| **模块参数**：`srpArea` |
| **类型**：character vector |
| **值：** `'1.0'` | 标量 | 大小为 *numSat* 的二维数组 |
| **默认值：** `'1.0'` |

### **太阳通量压力 (W\*s/m^3)** — 航天器太阳通量压力 `4.5344321e-6`（默认） | 标量

太阳通量压力，指定为标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **传播方法** 参数设置为 `Numerical (high precision)`。
- 将 **包括太阳辐射压力 (SRP)** 参数设置为 `on`。

#### 编程用法

|  |
| --- |
| **模块参数**：`fluxPressure` |
| **类型**：character vector |
| **值：** `4.5344321e-6` | 标量 |
| **默认值：** `'4.5344321e-6'` |

### 单位

### **单位** — 参数和端口单位 `Metric (m/s)`（默认） | `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

参数和端口单位，指定为：

| 单位 | 距离 | 速度 | 加速度 | 质量 | 面积 | 密度 |
| --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | meters | meters/sec | meters/sec2 | Kilograms | m2 | kg/m3, 某些密度输出 1/m3 |
| `Metric (km/s)` | kilometers | kilometers/sec | kilometers/sec2 | Kilograms | m2 | kg/m3, 某些密度输出 1/m3 |
| `Metric (km/h)` | kilometers | kilometers/hour | kilometers/hour2 | Kilograms | m2 | kg/m3, 某些密度输出 1/m3 |
| `English (ft/s)` | feet | feet/sec | feet/sec2 | Slugs | feet2 | lbm/ft3, 某些密度输出 1/ft3 |
| `English (kts)` | nautical mile | knots | knots/sec | Slugs | feet2 | lbm/ft3, 某些密度输出 1/ft3 |

#### 编程用法

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **默认值：** `'Metric (m/s)'` |

### **角度单位** — 角度单位 `Degrees`（默认） | `Radians`

角度参数和端口单位，指定为 `Degrees` 或 `Radians`。

#### 编程用法

|  |
| --- |
| **模块参数：** `angleUnits` |
| **类型：** character vector |
| **值：** `'Degrees'` | `'Radians'` |
| **默认值：** `'Degrees'` |

### **时间格式** — 开始日期和时间输出的时间格式 `Julian date`（默认） | `Gregorian`

**开始日期/时间 (UTC Julian date)** 和输出端口 **tutc** 的时间格式，指定为 `Julian date` 或 `Gregorian`。

#### 编程用法

|  |
| --- |
| **模块参数：** `timeFormat` |
| **类型：** character vector |
| **值：** `'Julian date'` | `'Gregorian'` |
| **默认值：** `'Julian date'` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：Orbit Propagator Numerical (high precision) 模块支持第三体的高保真引力效应

Orbit Propagator Numerical (high precision) 模块现在支持使用新的第三体引力选项的高保真工作流。使用这些选项可以在航天器仿真中更准确地建模轨道传播。

要访问这些效应，请在 **第三体** 选项卡上选中 **包括第三体引力** 参数。**包括第三体引力** 参数取代了 **包括第三体点质量引力** 参数。

选中 **包括第三体引力** 后，您可以配置太阳、水星、金星、月球、地球、火星、木星、土星、天王星、海王星、冥王星和自定义的引力选项。

### R2023b：Orbit Propagator 模块变更

Orbit Propagator 模块已更新以考虑：

- 第三体引力对轨道传播的影响。
- 来自 `aeroReadSpaceWeatherData` 函数生成的数据文件的太空天气数据。
- 太阳辐射压力 (SRP)。

## 描述

使用 Kepler 通用变量公式传播一个或多个航天器的轨道

Orbit Propagator 模块通过传播方法来传播一个或多个航天器的轨道。Orbit Propagator Numerical (high precision) 和 Orbit Propagator Kepler (unperturbed) 模块是同一模块的替代配置。

- Orbit Propagator Kepler (unperturbed) — Kepler 通用变量公式（更快）
- Orbit Propagator Kepler Numerical (high precision) — 更准确

所提供的初始条件的大小决定了所建模的航天器数量。如果为 **轨道** 选项卡中的某个参数提供多个值，该模块会输出一个卫星星座。任何只提供一个值的参数都会被扩展并应用于星座中的所有卫星。例如，如果为模块上除 **真近点角** 之外的所有参数都提供一个值，而 **真近点角** 包含六个值，则该模块会创建一个由六颗卫星组成的星座，仅改变真近点角。

该模块对输入端口 **A\_icrf**（施加的加速度）应用相同的扩展行为。此端口接受单个值（扩展至所有建模的航天器），或接受用于每个航天器的单独值。

有关 Orbit Propagator 模块使用的传播方法的详细信息，请参阅 Orbit Propagation Methods。

您可以在 **轨道** 选项卡中将初始轨道状态定义为：

- 一组轨道要素
- International Celestial Reference Frame (ICRF) 或固定坐标系中的位置和速度状态向量。

该模块使用四元数，这些四元数使用标量在前约定定义。

有关 Orbit Propagator 模块使用的坐标系的详细信息，请参阅 Coordinate Systems。

### 大气阻力

为帮助在高精度轨道传播中对航天器的阻力进行建模，Orbit Propagator Numerical (high precision) 模块支持阻力。大气阻力影响在低地球轨道 (LEO) 飞行的航天器；离地球越远，其相关性越低。有关大气阻力方程，请参阅 Atmospheric Drag。

### 第三体引力效应

要包含点质量第三体引力的效应，请选择要包含哪些第三体。这些计算需要 **Ephemeris model** 和数据。有关第三体贡献方程，请参阅 Third Body Gravity。

### 太阳辐射压力

要包含太阳辐射压力 (SRP) 对航天器的影响，请提供 eclipse fraction，或指定 shadow model 来计算该比例。当大气阻力可忽略且指向精度要求严格时，请考虑计入太阳辐射压力。有关太阳辐射压力方程，请参阅 Solar Radiation Pressure。
