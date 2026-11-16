---
type: simulink-block
title: 'Spacecraft Dynamics'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Spacecraft'
documentation_page: 'spacecraftdynamics'
documentation_source_path: 'spacecraftdynamics.html'
language: zh-CN
chinese_source: worker-translation
---

# Spacecraft Dynamics

## 端口

### 输入

### **Fb** — 施加力 3 元素向量 | *numSat*-by-3 数组

在当前时间步施加到航天器质心的本体坐标系中的力，指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Input body forces** 参数设置为 `on`。

**数据类型：** `double`

### **Mb** — 施加力矩 3 元素向量 | *numSat*-by-3 数组

在当前时间步施加到航天器的相对于质心的本体坐标系中的力矩，指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Input body moments** 参数设置为 `on`。

**数据类型：** `double`

### **A** — 外部加速度 3 元素向量 | *m*-by-3 数组

在当前时间步要施加到航天器的相对于 ICRF 或固定坐标系的外部加速度，指定为 3 元素向量或 *m*-by-3 数组。

#### 依赖项

要启用此端口，将 **Input external accelerations** 参数设置为 `on`。

要指定加速度坐标系，设置 **External acceleration coordinate frame** 参数。

**数据类型：** `double`

### **φθψ** — 月球天平动角 3 元素向量

使用月心主轴 (PA) 系统在 ICRF 与月心固定坐标系之间进行变换的月球天平动角，指定为 3 元素向量。要获取这些值，请使用 Moon Libration 模块。

**注意**

当 **Central body** 设置为 `Moon` 时，此模块使用的固定坐标系是平均地球/极轴 (ME) 系统。有关更多信息，请参阅算法。

#### 依赖项

要启用此端口：

- 将 **Central body** 设置为 `Moon`。
- 将 **Input Moon libration angles** 参数设置为 `on`。

**数据类型：** `double`

### **αδW** — 赤经、赤纬和旋转角 3 元素向量

中心天体自转轴瞬时赤经、赤纬和旋转角，指定为 3 元素向量。此端口仅适用于自定义中心天体。

#### 依赖项

要启用此端口：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Port`。

**数据类型：** `double`

### **m** — 航天器质量 标量 | 大小为 *numSat* 的一维数组

当前时间步的航天器质量。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dm/dt** — 质量变化率 标量 | 大小为 *numSat* 的一维数组

当前时间步的质量变化率（吸积为正，消融为负），指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **I** — 航天器惯性张量 3-by-3 数组 | 3-by-3-by-*numSat* 数组

当前时间步的航天器惯性张量，指定为 3-by-3 数组或 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵变化率 3-by-3 数组 | 3-by-3-by-*numSat* 数组

当前时间步的惯性张量矩阵变化率，指定为 3-by-3 数组或 3-by-3-by-*numSat* 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **Vre** — 相对速度 3 元素向量 | *numSat*-by-3 数组

质量在本体固定轴上吸积到本体或从本体消融的相对速度，指定为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口：

- 将 **Mass type** 设置为 `Custom Variable` 或 `Simple Variable`。
- 将 **Include mass flow relative velocity** 参数设置为 `on`。

**数据类型：** `double`

### **ρ** — 大气密度 标量

用于计算大气阻力加速度的大气密度。

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Port`。

**数据类型：** `double`

### **F107a** — 81 天平均 Ottawa F10.7 cm 太阳通量 标量

以 **Start date/time** 中指定的当前日为中心的 81 天平均 Ottawa F10.7 cm 太阳通量。这些 F107 Average 值对应于地球与太阳实际距离处的 10.7 cm 射电通量。此站点提供两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **F107** — 每日 Ottawa F10.7 cm 太阳通量 标量

以 **Start date/time** 中指定的当前日为中心的每日 Ottawa F10.7 cm 太阳通量。f107Daily 值不对应 1 AU 处的射电通量。此站点提供两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **aph** — 每日磁指数信息 *N*-by-7 数组

每日磁指数信息 (aph)，指定为 *N*-by-7 数组。磁指数信息包括：

|  |
| --- |
| 每日磁指数 (AP) |
| 当前时间的 3 小时 AP |
| 当前时间前 3 小时的 3 小时 AP |
| 当前时间前 6 小时的 3 小时 AP |
| 当前时间前 9 小时的 3 小时 AP |
| 当前时间前 12 到 33 小时八个 3 小时 AP 指数的平均值 |
| 当前时间前 36 到 57 小时八个 3 小时 AP 指数的平均值 |

每日磁指数在 80,000 m 以下的影响不大或尚未确定。有关更多信息，请参阅 NRLMSISE-00 Atmosphere Model 的限制。

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Flags** — 变化标志 23 的数组

变化标志，指定为 23 的数组，用于启用或禁用输出的特定变化。可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0

  移除该值对输出的影响。
- 1.0

  应用该值对输出的主要影响和交叉项影响。
- 2.0

  仅应用该值对输出的交叉项影响。

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
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，模块将使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)` |
| `Flags(10)` | 所有 UT、纵向效应 |
| `Flags(11)` | 纵向 |
| `Flags(12)` | UT 及混合 UT、纵向 |
| `Flags(13)` | 混合 AP、UT、纵向 |
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

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Flags source** 参数设置为 `Port`。

**数据类型：** `double`

### **Cd** — 大气阻力系数 标量 | 大小为 *numSat* 的向量

大气阻力系数，指定为标量或大小为 *numSat* 的向量。

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag coefficient source** 参数设置为 `Port`。

**数据类型：** `double`

### **Ad** — 大气阻力面积 标量 | 大小为 *numSat* 的向量

大气阻力面积，指定为标量或大小为 *numSat* 的向量。

#### 依赖项

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag area source** 参数设置为 `Port`。

**数据类型：** `double`

### **Rcb, 3** — 一个或多个自定义天体的位置 3 元素向量 | *numCustom3rdBodies*x3 元素向量

一个或多个自定义天体相对于当前中心天体的位置，位于 ICRF 坐标系中。*numCustom3rdBodies* 是自定义天体数量。有关更多信息，请参阅 **Custom gravitational parameter (m^3/s^2)**。

#### 依赖项

要启用此端口：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Custom** 参数设置为 `on`。

**数据类型：** `double`

### **Fraction** — 太阳圆盘的比例，介于 `0`（全食）和 `1`（全日照）之间 | 标量 | *numSat*

从航天器位置可见的太阳圆盘比例。*numSat* 是航天器数量。

#### 依赖项

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Eclipse fraction source** 设置为 `Port`。

**数据类型：** `double`

### **RC** — 反射率系数 标量或 *numSat* 个值，范围为 `1`≤*RC*≤`2`

反射率系数，指定为标量或 *numSat* 个值，范围为 `1`≤*RC*≤`2`。*numSat* 是航天器数量。

#### 依赖项

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Reflectivity coefficient source** 参数设置为 `Port`。

**数据类型：** `double`

### **Asrp** — 航天器横截面积 标量 | *numSat*

太阳看到的航天器横截面积，指定为标量或 *numSat*。模块使用此值计算太阳辐射压引起的加速度。

#### 依赖项

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **SRP area source** 参数设置为 `Port`。

**数据类型：** `double`

### 输出

### **X** — 航天器位置 3 元素向量 | *numSat*-by-3 数组

在当前时间步，航天器相对于 ICRF 或固定坐标系输出端坐标系的的位置，返回为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

- 要更改此端口的输出坐标系，设置 **State vector output coordinate frame** 参数。
- **Mass**、**Orbit** 或 **Attitude** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **V** — 速度 3 元素向量 | *numSat*-by-3 数组

在当前时间步，航天器相对于 ICRF 或固定坐标系输出端坐标系的速度，返回为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

- 要更改此端口的输出坐标系，设置 **State vector output coordinate frame** 参数。
- **Mass**、**Orbit** 或 **Attitude** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **A** — 总惯性加速度 3 元素向量 | *numSat*-by-3 数组

在当前时间步，航天器相对于 ICRF 的总惯性加速度，返回为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

- 要启用此端口，将 **Output total inertial acceleration** 参数设置为 `on`。
- **Orbit** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **qbody2icrf** — 航天器姿态四元数 4 元素四元数 | *numSat*-by-4 数组

在当前时间步，航天器姿态四元数，返回为从本体轴到输出端坐标系的（标量在前）四元数旋转，作为 4 元素四元数或 *numSat*-by-4 数组（标量在前）。*numSat* 是航天器数量。

#### 依赖项

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Quaternion`。

**数据类型：** `double`

### **DCM** — 航天器姿态方向余弦矩阵 3-by-3 数组 | *numSat*-by-3-by-3 数组

航天器姿态方向余弦矩阵 (DCM)，返回为 3-by-3 数组或 *numSat*-by-3-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `DCM`。

**数据类型：** `double`

### **R1,R2,R3** — 航天器姿态欧拉角 3 元素向量 | *numSat*-by-3 数组

航天器姿态欧拉角，返回为 3 元素向量或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Euler angles`。

**数据类型：** `double`

### **ω** — 航天器角速率 3 元素向量 | *numSat*-by-3 数组

航天器相对于姿态参考坐标系的角速率，返回为 3 元素向量或 *numSat*-by-3 数组，表示为本体轴角速率 PQR。*numSat* 是航天器数量。

#### 依赖项

姿态参考坐标系取决于 **Attitude reference coordinate frame** 参数。

**数据类型：** `double`

### **dω/dt** — 本体角加速度 3 元素数组 | *numSat*-by-3 数组

相对于 ICRF 坐标系的本体角加速度，返回为 3 元素数组或 *numSat*-by-3 数组。*numSat* 是航天器数量。

#### 依赖项

要启用此端口，将 **Output total inertial angular acceleration** 参数设置为 `on`。

姿态参考坐标系取决于 **Attitude reference coordinate frame** 参数。

**数据类型：** `double`

### **qicrf2ff** — 坐标系变换 4 元素数组

在当前时间步，ICRF 与固定坐标系之间的坐标系变换，返回为 4 元素数组。

#### 依赖项

要启用此端口，将 **Output quaternion (ICRF to Fixed-frame)** 参数设置为 `on`。

**数据类型：** `double`

### **tutc** — 当前时间步的时间 标量 | 6 元素数组

当前时间步的时间，返回为：

- 标量 — 如果将 **Start data/time** 参数指定为儒略日。
- 6 元素数组 — 如果将 **Start data/time** 参数指定为包含六个元素（年、月、日、小时、分钟、秒）的格里高利日期。

此值等于 **Start date/time** 参数值加上经过的仿真时间。

#### 依赖项

要启用此参数，将 **Output current date/time (UTC Julian date)** 参数设置为 `on`。

**数据类型：** `double`

### **Fuel Status** — 燃料状态 标量 | *numSat* 元素数组

当前时间步的燃料箱状态，返回为标量或 *numSat* 元素数组，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱未满或未空。
- `-1` — 燃料箱已空。

*numSat* 是航天器数量。

#### 依赖项

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable`。
- 将 **Output fuel tank status** 参数设置为 `on`。

**数据类型：** `double`

## 参数

### 主要

### **Input body forces** — 启用外部力的选项 on（默认）| off

要启用外部力包含在本体坐标系中航天器运动方程的积分中，请选中此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `forcesin` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Input body moments** — 启用外部力矩的选项 on（默认）| off

要启用外部力矩包含在本体坐标系中航天器运动方程的积分中，请选中此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `momentsIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Input external accelerations** — 输入附加力加速度的选项 off（默认）| on

要启用附加外部加速度包含在航天器运动方程的积分中，请选中此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `accelIn` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **External acceleration coordinate frame** — 加速度输入端口坐标系 `ICRF`（默认）| `Fixed-frame`

加速度输入端口 **A** 的坐标系，指定为 `ICRF` 或 `Fixed-frame`。

#### 依赖项

要启用此参数，将 **Input external accelerations** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `accelFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **State vector output coordinate frame** — 位置和速度状态输出端口坐标系 `ICRF`（默认）| `Fixed-frame`

位置和速度状态输出端口坐标系设置，指定为 `ICRF` 或 `Fixed-frame`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `outportFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` |
| **Default:** `'ICRF'` |

### **Output total inertial acceleration** — 启用总加速度端口的选项 off（默认）| on

启用模块计算的相对于 ICRF 或固定坐标系输出端坐标系的总加速度输出。此加速度包括作用在航天器上的所有外部加速度、力以及内部环境加速度。

**注意**

不要将此端口用作仿真循环的一部分（换句话说，不要将此输出反馈到模块中）。

**可调：** 是

#### 依赖项

要更改此端口的输出坐标系，设置 ****State vector output coordinate frame**** 参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `AccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Start date/time (UTC Julian date)** — 仿真的初始开始时间 `juliandate (2020, 1, 1, 12, 0, 0)`（默认）| 有效标量儒略日 | 有效格里高利日期，包括年、月、日、小时、分钟、秒，作为一维数组或 6 元素数组

仿真的初始开始日期和时间，指定为儒略日或格里高利日期。模块使用此值定义初始条件。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

**可调：** 是

#### 依赖项

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `startDate` |
| **Type:** character vector |
| **Values:** `'juliandate(2020, 1, 1, 12, 0, 0)'` | 有效标量儒略日 | 有效格里高利日期，包括年、月、日、小时、分钟、秒，作为一维数组或 6 元素数组 |
| **Default:**  `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — 添加输出端口 tutc 的选项 on（默认）| off

要输出当前日期或时间，请选中此参数。否则，清除此参数。

#### 依赖项

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `dateOut` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Action for out-of-range input** — 超出范围输入的模块行为 `Warning`（默认）| `Error` | `None`

超出范围输入的模块行为操作。指定以下选项之一。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | Diagnostic Viewer 中出现警告，模型仿真继续。 |
| `Error`（默认） | Diagnostic Viewer 中出现错误，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |

### 质量

### **Mass type** — 航天器质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

航天器质量类型，指定为：

- `Fixed` — 质量和惯性在整个仿真过程中恒定。
- `Simple Variable` — 质量和惯性作为质量变化率的函数线性变化。
- `Custom Variable` — 瞬时质量、惯性和惯性变化率是模块的输入。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `massType` |
| **Type**: character vector |
| **Values**: `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **Default**: `'Fixed'` |

### **Mass** — 刚体航天器的初始质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

刚体航天器的初始质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 参数设置为 **Fixed** 或 **Simple variable**。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `mass` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'4.0'` |

### **Empty mass** — 航天器空质量 `3.5`（默认）| 标量 | 大小为 *numSat* 的向量

航天器空（干）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `emptyMass` |
| **Type:** character vector |
| **Values:** 1D array of size *numSat* | 1D array of size *numSat* |
| **Default:** `'3.5'` |

### **Full mass** — 航天器满质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

航天器满（湿）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fullMass` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'4.0'` |

### **Inertia tensor** — 惯性张量矩阵 `[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

航天器的初始惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `inertia` |
| **Type:** character vector |
| **Values:** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` | 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` |

### **Empty inertia tensor** — 空惯性张量矩阵 `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

空（干）惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `emptyInertia` |
| **Type:** character vector |
| **Values:** 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]` |

### **Full inertia tensor** — 满惯性张量矩阵 `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]`（默认）| 3-by-3 数组 | 3-by-3-by-*numSat* 数组

满（湿）惯性张量矩阵，指定为单个航天器的 3-by-3 数组或多个航天器的 3-by-3-by-*numSat* 数组。

**可调：** 是

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fullInertia` |
| **Type:** character vector |
| **Values:** 3-by-3 array | 3-by-3-by-*numSat* array |
| **Default:** `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]` |

### **Include mass flow relative velocity** — 启用质量流速度的选项 off（默认）| on

要向模块启用质量流速度，请选中此参数。质量流速度是质量吸积或消融时的本体坐标系相对速度。要禁用模块的质量流速度，请清除此参数。

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable` 或 `Custom variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useMassFlowRelativeVelocity` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Limit mass flow when mass is empty or full** — 限制质量流的选项 on（默认）| off

要在航天器质量已满或为空时限制质量流，请选中此参数。否则，清除此参数。

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `limitMassFlow` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Output fuel tank status** — 启用燃料箱状态的选项 on（默认）| off

要启用燃料箱状态，请选中此参数。否则，清除此参数。

#### 依赖项

要启用此参数，将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `outputFuelStatus` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### 轨道

定义航天器的初始状态。

### **Initial state format** — 轨道初始状态的输入方法 `Orbital elements`（默认）| `ICRF state vector` | `Fixed-frame state vector`

轨道初始状态的输入方法，指定为 `Orbital elements`、`ICRF state vector` 或 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **Block Parameter** `stateFormatNum` when `propagator` is set to `High precision (numerical)` |
| **Type:** character vector |
| **Values:**  `'Orbital elements'` | `'Orbital elements'` | `'ICRF state vector'` | `'Fixed-frame state'` when `propagator` is set to `'High precision (numerical)'` |
| **Default:** `'Orbital elements'` |

### **Orbit type** — 轨道分类 `Keplerian`（默认）| `Elliptical equatorial` | `Circular` | `Circular equatorial`

轨道分类，指定为：

- `Keplerian` — 使用六个标准开普勒轨道元素对椭圆、抛物线和双曲线轨道建模。
- `Elliptical equatorial` — 完整定义赤道轨道，其中倾角为 0 或 180 度，升交点赤经未定义。
- `Circular` — 定义圆轨道，其中偏心率为 0，近地点幅角未定义。要完整定义圆轨道，请选择 `Circular equatorial`。
- `Circular equatorial` — 完整定义圆轨道，其中偏心率为 0，近地点幅角未定义。

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `orbitType` |
| **Type:** character vector |
| **Values:** `'Keplerian'` | `'Elliptical equatorial'` | `'Circular inclined'` | `'Circular equatorial'` |
| **Default:** `'Keplerian'` |

### **Semi-major axis** — 椭圆长轴的一半 6786000（默认）| 标量 | 大小为 *numSat* 的一维数组

椭圆长轴的一半，指定为大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

- 对于抛物线轨道，此模块将此参数解释为近地点半径（从近地点到轨道焦点的距离）。
- 对于双曲线轨道，此模块将此参数解释为从近地点到双曲线中心的距离。

**可调：** 是

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `semiMajorAxis` |
| **Type:** character vector |
| **Values:** scalar | 1D array of size *numSat* |
| **Default:** `'6786000'` |

### **Eccentricity** — 轨道偏离度 0.01（默认）| 标量 | `0` 到 `1` 之间的值，或对于 Keplerian 轨道类型大于 `1` | 大小为 *numSat* 的一维数组

轨道偏离完美圆的程度，指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

如果 **Orbit** 类型设置为 `Keplerian`，此值可以是：

- `1`，用于抛物线轨道
- 大于 `1`，用于双曲线轨道

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Elliptical equatorial`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `eccentricity` |
| **Type:** character vector |
| **Values:** `0.01` | scalar | value between `0` and `1`, or greater than `1` for Keplerian orbit type | 1D array of size *numSat* |
| **Default:** `'0.01'` |

### **Inclination** — 轨道平面倾角 50（默认）| 标量 | 大小为 *numSat* 的一维数组 | 0 到 180 度 | 0 到 pi 弧度

在升交点处测量的椭圆相对于参考平面的垂直倾斜，指定为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`
- 将 **Orbit type** 设置为 `Keplerian` 或 `Circular inclined`

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `inclination` |
| **Type:** character vector |
| **Values:** 50 | scalar | 1D array of size *numSat* | degrees between 0 and 180 | radians between 0 and pi |
| **Default:** `'50'` |

### **RAAN** — 赤道平面中的角距离 95（默认）| `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组

升交点赤经 (RAAN)，指定为 `0` 到 `360` 之间的值，作为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。RAAN 是沿参考平面从国际天球参考系 (ICRF) *x*-轴到升交点位置的角距离——航天器从南向北穿过参考平面的点。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Circular inclined`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `raan` |
| **Type:** character vector |
| **Values:** `'95'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'95'` |

### **Argument of periapsis** — 从航天器升交点到近地点的角度 93（默认）| `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

从航天器升交点到近地点（轨道最靠近中心天体的点）的角度，指定为大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`
- 将 **Orbit type** 设置为 `Keplerian`

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `argPeriapsis` |
| **Type:** character vector |
| **Values:** 93 | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'93'` |

### **True anomaly** — 近地点与航天器初始位置之间的角度 203（默认）| `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组

在 **Start date/time** 时，近地点（轨道最靠近中心天体的点）与航天器沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Elliptical inclined`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `trueAnomaly` |
| **Type:** character vector |
| **Values:** `'203'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'203'` |

### **Argument of latitude** — 升交点与航天器初始位置之间的角度 200（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

在 **Start date/time** 时，升交点与航天器沿其轨道的初始位置之间的角度，指定为标量或 3 元素向量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit Type** 设置为 `Circular inclined`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `argLat` |
| **Type:** character vector |
| **Values:** `'200'` | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'200'` |

### **Longitude of periapsis** — ICRF *x*-轴与偏心率向量之间的角度 100（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

ICRF *x*-轴与偏心率向量之间的角度，指定为标量或 3 元素向量或大小为 *numSat* 的一维数组，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Elliptical equatorial`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `lonPeriapsis` |
| **Type:** character vector |
| **Values:** 100 | scalar value between `0` and `360` | 1D array of size *numSat* |
| **Default:** `'100'` |

### **True longitude** — ICRF *x*-轴与航天器初始位置之间的角度 150（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组 | *numSat*-by-3 向量

在 **Start date/time** 时，ICRF *x*-轴与航天器沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组或 *numSat*-by-3 向量，使用指定单位。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Circular equatorial`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `trueLon` |
| **Type:** character vector |
| **Values:** `'150'` | scalar value between `0` and `360` | 1D array of size *numSat* | *numSat*-by-3 vector |
| **Default:** `'150'` |

### **ICRF position** — 航天器的笛卡尔位置向量 `[3649700.0 3308200.0 -4676600.0]`（默认）| 3 元素向量 | | *numSat*-by-3 数组

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔位置向量，指定为单个航天器的 3 元素向量或多个航天器的 *numSat*-by-3 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `ICRF state vector`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `inertialPosition` |
| **Type:** character vector |
| **Values:** `[3649700.0 3308200.0 -4676600.0]` | 3-element vector | *numSat*-by-3 array |
| **Default:** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF velocity** — 航天器的笛卡尔速度向量 `[-2750.8 6666.4 2573.4]`（默认）| 3 元素向量 | *numSat*-by-3 数组

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔速度向量，指定为单个航天器的 3 元素向量或多个航天器的 *numSat*-by-3 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `ICRF state vector`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `inertialVelocity` |
| **Type:** character vector |
| **Values:** `[-2750.8 6666.4 2573.4]` | 3-element vector | 2-D array of size *numSat*-by-3 array |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame position** — 航天器位置向量 [-4142689.0 -2676864.7 -4669861.6]（默认）| 3 元素向量 | *numSat*-by-3 数组

在 **Start date/time** 时，航天器在固定坐标系中的笛卡尔位置向量，指定为单个航天器的 3 元素向量或多个航天器的 *numSat*-by-3 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fixedPosition` |
| **Type:** character vector |
| **Values:** `'[-4142689.0 -2676864.7 -4669861.6]'` | 3-element vector for single spacecraft | *numSat*-by-3 array |
| **Default:** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame velocity** — 航天器速度向量 [1452.7 -6720.7 2568.1]（默认）| 3 元素向量 | *numSat*-by-3 数组

在 **Start date/time** 时，航天器在固定坐标系中的笛卡尔速度向量，指定为单个航天器的 3 元素向量或多个航天器的 *numSat*-by-3 数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Initial state format** 设置为 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fixedVelocity` |
| **Type:** character vector |
| **Values:** `'[1452.7 -6720.7 2568.1]'` | 3-element vector | *numSat*-by-3 array |
| **Default:** `'[1452.7 -6720.7 2568.1]'` |

### 姿态

### **Attitude reference coordinate frame** — 姿态和角速率坐标系 `ICRF`（默认）| `Fixed-frame` | `NED` | `LVLH`

相对于姿态和角速率初始条件的姿态和角速率坐标系，指定为：

- `ICRF`
- `Fixed-frame`
- `NED`
- `LVLH`

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `attitudeFrame` |
| **Type:** character vector |
| **Values:** `'ICRF'` | `'Fixed-frame'` | `'NED'` | `'LVLH'` |
| **Default:** `'ICRF'` |

### **Attitude representation** — 姿态格式 `Quaternion`（默认）| `DCM` | `Euler angles`

航天器姿态（初始条件和输出端口）的姿态格式，指定为 `Quaternion`、`DCM` 或 `Euler angles`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `attitudeFrame` |
| **Type:** character vector |
| **Values:** `'Quaternion'` | `'DCM'` | `'Euler angles'` |
| **Default:** `'Quaternion'` |

### **Initial body attitude** — 航天器初始姿态 `[1, 0, 0, 0]`（默认）| 4 元素向量 | *numSat*-by-4 数组 | 3-by-3 数组 | *numSat*-by-3-by-3 数组

航天器的初始姿态（方向），提供为相对于 **Attitude representation** 的四元数、DCM 或欧拉角集。

**可调：** 是

#### 依赖项

此参数名称和值格式随 **Attitude representation** 参数变化。

| 参数名称 | Attitude Representation 设置 | 值格式 |
| --- | --- | --- |
| **Initial quaternion** | `Quaternion` | - 4 元素向量 - *numSat*-by-4 数组 |
| **Initial DCM** | `DCM` | - 3-by-3 数组 - *numSat*-by-3-by-3 数组 |
| **Initial Euler angles** | `Euler angles` | - 3 元素向量 - *numSat*-by-3 数组 |

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `attitude` |
| **Type:** character vector |
| **Values:** 4-element vector | *numSat*-by-4 array | 3-by-3 array | *numSat*-by-3-by-3 array | 3-element array | *numSat*-by-3 array |
| **Default:** `'[1, 0, 0, 0]'` |

### **Angle rotation order** — 角度旋转顺序 `ZYX`（默认）| `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

用于欧拉角姿态表示的旋转角顺序。

**可调：** 是

#### 依赖项

要启用此参数，将 **Attitude representation** 设置为 `Euler angles`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `rotationOrder` |
| **Type**: character vector |
| **Values**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **Default**: `'ZYX'` |

### **Initial body angular rates PQR** — 初始本体固定角速率 `[0, 0, 0]`（默认）| 3 元素向量 | *numSat*-by-3 数组

相对于 **Attitude reference coordinate frame** 的初始本体固定角速率 (PQR)。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `attitudeRate` |
| **Type:** character vector |
| **Values:** | 3-element vector | *numSat*-by-3 array |
| **Default:** `[0, 0, 0]` |

### **Output total inertial angular acceleration** — 启用总飞行器加速度的选项 off（默认）| on

启用模块计算的相对于 ICRF 姿态参考坐标系的总飞行器加速度输出。此加速度包括作用在航天器上的所有力矩。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `angAccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Include gravity gradient torque** — 启用重力梯度力矩的选项 on（默认）| off

选中此参数可在模块旋转动力学方程中使用重力梯度力矩。否则，清除此参数。

**可调：** 是

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `angAccelOut` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### 中心天体

### **Central body** — 航天器环绕的天体 `Earth`（默认）| `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

天体，指定为 `Earth`、`Moon`、`Mercury`、`Venus`、`Mars`、`Jupiter`、`Saturn`、`Uranus`、`Neptune`、`Sun` 或 `Custom`，**Orbit** 选项卡中定义的航天器环绕其运行。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `centralBody` |
| **Type:** character vector |
| **Values:** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Sun'` | `'Custom'` | |
| **Default:** `'Earth'` |

### **Gravitational potential model** — 中心天体的引力模型 当 **Central body** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom` 时为 `Spherical harmonics`；当 **Central body** 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 `Oblate ellipsoid`（默认）| `Point-mass` | `Oblate ellipsoid (J2)`

通过指定 `Spherical harmonics`、`Point-mass` 或 `Oblate ellipsoid (J2)` 控制中心天体的引力模型。

#### 依赖项

可用选项基于 **Central body** 设置。

| Earth, Moon, Mars, or Custom | Mercury, Venus, Jupiter, Saturn, Uranus, or Neptune |
| --- | --- |
| `Spherical harmonics` | `Oblate ellipsoid (J2)` |
| `Point-mass` | `Point-mass` |
| `Oblate ellipsoid (J2)` | — |

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `gravityModel` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'` | `gravityModelnoSH` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Type:** character vector |
| **Values:** `'Spherical harmonics'` | `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Point-mass'` | `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |
| **Default:** `'Spherical harmonics'` when `centralBody` set to `'Earth'`, `'Moon'`, `'Mars'`, or `'Custom'`; `'Oblate ellipsoid (J2)'` when `centralBody` set to `Mercury`, `Venus`, `Jupiter`, `Saturn`, `Uranus`, or `Neptune` |

### **Spherical harmonic model** — 球谐模型 对于 **Central body** 设置为 `Earth` 时为 `EGM2008`，对于 **Central body** 设置为 `Moon` 时为 `LP-100K`，对于 **Central body** 设置为 `Mars` 时为 `GMM2B`（默认）| `EGM96` | `EIGEN-GL04C` | `LP-165P`

根据指定的 **Central body** 指定的球谐引力势模型。

#### 依赖项

可用选项基于 **Central body** 设置：

| 中心天体 | 球谐模型选项 |
| --- | --- |
| Earth | EGM2008, EGM96, or EIGEN-GL04C |
| Moon | LP-100K or LP-165P |
| Mars | GMM2B |

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `'earthSH'` when `centralBody` set to `'Earth'` | `'moonSH'` when `centralBody` set to `'Moon'` | `'marsSH'` when `centralBody` set to `'Mars'` |
| **Type:** character vector |
| **Values:** `'EGM2008'` | `'EGM96'` | `'EIGEN-GL04C'` when `centralBody` set to `'earthSH'`; `'LP-100K'` | `'LP-165P'` when `centralBody` set to `'moonSH'`; `'GMM2B'` when `centralBody` set to `'marsSH'` |
| **Default:** `'Spherical harmonics'` |

### **Rotational rate** — 旋转速率 4.06124975e-3（默认）| 标量

自定义中心天体的旋转速率，指定为标量。

#### 依赖项

要启用此参数，将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `'customOmega'` |
| **Type:** character vector |
| **Values:** `'4.06124975e-3'` | scalar |
| **Default:** `'4.06124975e-3'` |

### **Spherical harmonic coefficient file** — 谐波系数 MAT 文件 `aerogmm2b.mat`（默认）| 谐波系数 MAT 文件

包含自定义行星模型定义的谐波系数 MAT 文件，指定为字符向量或字符串。

此文件必须包含以下变量：

| 变量 | 描述 |
| --- | --- |
| *Re* | 行星赤道半径的标量，单位为 meters (m)。 |
| *GM* | 行星引力参数的标量，单位为 meters cubed per second squared (m3/s2)。 |
| *degree* | 最大阶数的标量。 |
| *C* | (*degree*+1)-by-(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *C*。 |
| *S* | (*degree*+1)-by-(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *S*。 |

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `shFile` |
| **Type:** character vector |
| **Values:** `'aerogmm2b.mat'` | harmonic coefficient MAT file |
| **Default:** `'aerogmm2b.mat'` |

### **Degree** — 谐波模型的阶数 `120`（默认）| 标量 | 最大 2159

谐波模型的阶数，指定为标量。

| 行星模型 | 推荐阶数 | 最大阶数 |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom`。
- 将 **Gravitational potential model** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `shDegree` |
| **Type:** character vector |
| **Values:** `'80'` | scalar |
| **Default:** `'80'` |

### **Use Earth orientation parameters (EOPs)** — 使用地球定向参数的选项 on（默认）| off

选中此参数可在 ICRF 与固定坐标系之间的变换中使用地球定向参数。否则，清除此参数。

#### 依赖项

要启用此参数，将 **Central body** 设置为 `Earth`。

此外，它必须满足以下条件之一：

- **Gravitational potential model** 设置为 `Spherical harmonics` 或 `Oblate ellipsoid (J2)`。
- **External acceleration coordinate frame** 设置为 `Fixed-frame`。
- **State vector output coordinate frame** 设置为 `Fixed-frame`。
- **Attitude reference coordinate frame** 设置为 `Fixed-frame` 或 `NED`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useEOPs` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **IERS EOP data file** — 地球定向数据 `aeroiersdata.mat`（默认）| MAT 文件

地球定向数据的自定义列表，在 MAT 文件中指定。

#### 依赖项

要启用此参数：

- 将 **Use Earth orientation parameters (EOPs)** 参数设置为 `on`。
- 将 **Central body** 设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `eopFile` |
| **Type:** character vector |
| **Values:** `'aeroiersdata.mat'` | `MAT-file` |
| **Default:** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — 月球天平动欧拉角速率 off（默认）| on

要指定月球定向的欧拉天平动角 (φ θ ψ)，请选中此参数。

#### 依赖项

要启用此参数，将 **Central body** 设置为 `Moon`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useMoonLib` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Output quaternion (ICRF to Fixed-frame)** — 添加输出变换四元数端口的选项 off（默认）| on

要添加从 ICRF 到固定坐标系的四元数变换的输出变换四元数端口，请选中此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `outputTransform` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Central body spin axis source** — 中心天体自转轴来源 `Port`（默认）| `Dialog`

中心天体自转轴来源，指定为 `Port` 或 `Dialog`。模块使用自转轴计算自定义中心天体的从 ICRF 到固定坐标系的变换。

#### 依赖项

要启用此参数，将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbPoleSrc` |
| **Type:** character vector |
| **Values:** `'Port'` | `'Dialog'` |
| **Default:** `'Port'` |

### **Spin axis right ascension (RA) at J2000** — J2000 时中心天体自转轴的赤经 `317.68143`（默认）| double 标量

J2000 时中心天体自转轴的赤经（2451545.0 JD，2000 Jan 1 12:00:00 TT），指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbRA` |
| **Type:** character vector |
| **Values:** `'317.68143'` | double scalar |
| **Default:** `'317.68143'` |

### **Spin axis RA rate (deg/century)** — 中心天体自转轴的赤经变化率 `-0.1061`（默认）| double 标量

中心天体自转轴的赤经变化率，指定为 double 标量，使用指定角度单位/世纪。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbRARate` |
| **Type:** character vector |
| **Values:** `'-0.1061'` | double scalar |
| **Default:** `'-0.1061'` |

### **Spin axis declination (Dec) at J2000** — J2000 时中心天体自转轴的赤纬 `52.88650`（默认）| double 标量

J2000 时中心天体自转轴的赤纬（2451545.0 JD，2000 Jan 1 12:00:00 TT），指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbDec` |
| **Type:** character vector |
| **Values:** `'52.88650'` | double scalar |
| **Default:** `'52.88650'` |

### **Spin axis Dec rate (deg/century)** — 中心天体自转轴的赤纬变化率 `-0.0609`（默认）| double 标量

中心天体自转轴的赤纬变化率，指定为 double 标量，使用指定角度单位/世纪。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbDecRate` |
| **Type:** character vector |
| **Values:** `'-0.0609'` | double scalar |
| **Default:** `'-0.0609'` |

### **Initial rotation angle at J2000** — 中心天体 *x*-轴的旋转角 `176.630`（默认）| double 标量

J2000 时中心天体 x 轴相对于 ICRF *x*-轴的旋转角（2451545.0 JD，2000 Jan 1 12:00:00 TT），指定为 double 标量，使用指定角度单位。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbRotAngle` |
| **Type:** character vector |
| **Values:** `'176.630'` | double scalar |
| **Default:** `'176.630'` |

### **Rotation rate (deg/day)** — 中心天体 *x*-轴的旋转速率 `350.89198226`（默认）| double 标量

中心天体 x 轴相对于 ICRF *x*-轴的旋转速率（2451545.0 JD，2000 Jan 1 12:00:00 UTC），指定为 double 标量，使用角度单位/天。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `cbRotRate` |
| **Type:** character vector |
| **Values:** `'350.89198226'` | double scalar |
| **Default:** `'350.89198226'` |

### **Equatorial radius** — 赤道半径 `3.3962e6`（默认）| double 标量

自定义中心天体的赤道半径，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Gravitational potential model** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customR` |
| **Type:** character vector |
| **Values:** `'3.3962e6'` | double scalar |
| **Default:** `'3.3962e6'` |

### **Flattening** — 行星扁率 `0.00589`（默认）| double 标量

自定义中心天体的行星扁率，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Point-mass`、`Oblate ellipsoid (J2)` 或 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customF` |
| **Type:** character vector |
| **Values:** `'0.00589'` | double scalar |
| **Default:** `'0.00589'` |

### **Gravitational parameter** — 引力参数 `4.305e13`（默认）| double 标量

自定义中心天体的引力参数，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customMu` |
| **Type:** character vector |
| **Values:** `'4.305e13'` | double scalar |
| **Default:** `'4.305e13'` |

### **Second degree zonal harmonic (J2)** — 最重要或最大的球谐项 `1.0826269e-03`（默认）| double 标量

最重要或最大的球谐项，用于说明天体的扁率，指定为 double 标量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customJ2` |
| **Type:** character vector |
| **Values:** `'1.0826269e-03'` | double scalar |
| **Default:** `'1.0826269e-03'` |

### 阻力

配置大气阻力环境。

### **Include atmospheric drag** — 包含大气阻力的选项 off（默认）| on

要包含大气阻力，请选中此复选框。

#### 依赖项

要启用此参数，将 **Central Body** 参数设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useDrag` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Atmospheric density source** — 大气密度值的来源 `Dialog`（默认）| `Port`

大气密度值的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `atmosSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Atmospheric model** — 大气模型 `NRLMSISE-00`（默认）

用于大气阻力计算的大气模型，指定为 `NRLMSISE-00`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `atmosModel` |
| **Type:** character vector |
| **Values:** `'NRLMSISE-00'` |
| **Default:** `'NRLMSISE-00'` |

### **Flux source** — 空间天气数据的来源 `Dialog`（默认）| `Port`

用于大气密度计算的历史和预测通量及地磁指数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fluxSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Space weather data file** — 空间天气数据的 MAT 文件 `aeroSpaceWeatherData.mat`（默认）| MAT 文件名

空间天气数据的 MAT 文件。此文件是 `aeroReadSpaceWeatherData` 函数的输出。

Aerospace Blockset 包含默认空间天气数据文件 `aeroSpaceWeatherData.mat`。要使用可用的最新数据，请使用 `aeroReadSpaceWeatherData` 生成新的 MAT 文件，并为该参数指定文件名。有关更多信息，请参阅 `aeroReadSpaceWeatherData`。

如果文件不在 MATLAB® 路径中，请指定完整路径名。MAT 文件必须包含来自空间天气数据文件的以下变量：

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

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `SpaceWeatherDataFile` |
| **Type**: character vector |
| **Values**: `'aeroSpaceWeatherData.mat'` | MAT file name |
| **Default**: `'aeroSpaceWeatherData.mat'` |

### **F10.7 extrapolation method** — `f107Average` 和 `f107Daily` 的外推方法 `None - clip`（默认）| `Constant` | `Least squares fit`

对于 MAT 文件数据范围之外的时间，`f107Average` 和 `f107Daily` 的外推方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将 `f107Average` 和 `f107Daily` 设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将 `f107Average` 和 `f107Daily` 设置为由 **Magnetic index extrapolation method** 参数值指定的常量值。 |
| `Least squares fit` | 使用从 October 1, 1957 到 December 1, 2040 的空间天气数据进行最小二乘拟合来近似 `f107Average` 和 `f107Daily`。此方法使用以下形式的三角函数：  `a + b*cos(c*t + d*sin(e*t))`，  其中：    - *a* 为   `128.2351780622538` - *b* 为 `54.3285872213434` - *c* 为 `0.0015460708364` - *d* 为 `0.2429462096495` - *e* 为 `0.0015563188188` - *t* 为 *jdCurrent* -   *jdReftime* - *jdCurrent* 是当前儒略日 - *jdRef* 为 `2436112.5` |

**注意**

对于 `f107Average` 值，如果 81 天周期的一部分落在空间天气数据的 MAT 文件范围内，Solar Flux and Geomagnetic Index 模块使用重叠部分的实际每日值。为了计算非重叠部分的平均值，模块使用 clip、constant 或 least squares 每日值。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `F107ExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **Default**: `'None - clip'` |

### **Magnetic index extrapolation method** — 磁指数信息的外推方法 `None - clip`（默认）| `Constant` | `IGRF`

对于 MAT 文件数据范围之外的时间，磁指数信息值的外推方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将磁指数信息元素设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将磁指数信息元素设置为由 **Magnetic index extrapolation method** 参数指定的常量值。  这些时间范围之外的磁指数元素基于这些时间限制处水平磁场强度的裁剪值。 |
| `IGRF` | 使用 International Geomagnetic Reference Field 计算磁指数信息元素。由于此模型定义的时间范围为 January 1, 1900, 12:00 AM UTC 到 January 1, 2025, 12:00 AM UTC，此范围之外的预测会裁剪到这些时间限制处的值。 |

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `MagneticIndexExtrapMethod` |
| **Type**: character vector |
| **Values**: `'None - clip'` | `'Constant'` | `'IGRF'` |
| **Default**: `'None - clip'` |

### **Flags source** — 变化标志来源 `Dialog`（默认）| `Port`

变化标志来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 参数设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fluxFlagsSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'Dialog'` |

### **Flags** — 变化标志 `ones(1,23)`（默认）

变化标志，指定为 23 的数组 (`ones(1,23)`)。可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0 — 移除该值对输出的影响。
- 1.0 — 应用该值对输出的主要影响和交叉项影响。
- 2.0 — 仅应用该值对输出的交叉项影响。

该数组具有以下字段。

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
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，模块将使用整个磁指数信息矩阵 (APH)，而不是 `APH(:,1)`。 |
| `Flags(10)` | 所有 UT、纵向效应 |
| `Flags(11)` | 纵向 |
| `Flags(12)` | UT 及混合 UT、纵向 |
| `Flags(13)` | 混合 AP、UT、纵向 |
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

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Flags source** 设置为 `Dialog`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 参数设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `fluxFlags` |
| **Type:** character vector |
| **Values:** `'ones(1,23)'` |
| **Default:** `'ones(1,23)'` |

### **Include anomalous oxygen in density calculation** — 在密度计算中包含异常氧的选项 off（默认）| on

要在密度计算中包含异常氧，请选中此复选框。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 参数设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useOxygen` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Drag coefficient source** — 阻力系数来源 `Dialog`（默认）| `Port`

阻力系数来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `dragCoeffSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag coefficient** — 航天器阻力系数 2.179（默认）| 标量 | 大小为 *numSat* 的向量

用于大气阻力计算的航天器阻力系数，指定为标量或大小为 *numSat* 的向量。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag coefficient source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `dragCoeff` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'2.179'` |

### **Drag area source** — 阻力面积来源 `Dialog`（默认）| `Port`

阻力面积来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `dragAreaSrc` |
| **Type:** character vector |
| **Values:** `'Dialog'` | `'Source'` |
| **Default:** `'Dialog'` |

### **Drag area** — 用于计算大气阻力加速度的面积 1.0（默认）| 标量 | 大小为 *numSat* 的向量

用于计算大气阻力加速度的面积，指定为标量或大小为 *numSat* 的向量。航天器的此面积垂直于航天器相对速度。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag area source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `dragArea` |
| **Type:** character vector |
| **Values:** scalar | vector of size *numSat* |
| **Default:** `'1.0'` |

### 第三体

配置用于引力加速度的第三体质点。

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择 Jet Propulsion Laboratory 定义的以下星历模型之一。模块使用星历数据计算第三体质点引力和太阳辐射压所需的相对天体位置。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 于 1998 年发布。此星历考虑的儒略日范围为 2305424.50（December 9, 1599）到 2525008.50（February 20, 2201）。  此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame version 1.0。 |
| `DE421` | 于 2008 年发布。此星历考虑的儒略日范围为 2414992.5（December 4, 1899）到 2469808.5（January 2, 2050）。  此模块实现这些星历相对于 1998 年采用的 International Celestial Reference Frame version 1.0。 |
| `DE423` | 于 2010 年发布。此星历考虑的儒略日范围为 2378480.5（December 16, 1799）到 2524624.5（February 1, 2200）。  此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame version 2.0。 |
| `DE430` | 于 2013 年发布。此星历考虑的儒略日范围为 2287184.5（December 21, 1549）到 2688976.5（January 25, 2650）。  此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame version 2.0。 |
| `DE432t` | 于 April 2014 发布。此星历考虑的儒略日范围为 2287184.5（December 21, 1549）到 2688976.5（January 25, 2650）。  此模块实现这些星历相对于 2010 年采用的 International Celestial Reference Frame version 2.0。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB Command Window 中键入 `aeroDataPackage`。在 MATLAB 桌面工具条中，单击 **Add-Ons**。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `ephemerisModel` |
| **Type**: character vector |
| **Values**: `DE405` | `DE421` | `DE423` | `DE430` |
| **Default**: `'DE405'` |

### **Limit ephemerides date range** — 启用星历数据范围开始和结束的选项 `off`（默认）| `on`

控制仿真期间加载到内存中的数据量以及生成的代码中包含的数据量：

- 选中此复选框可将星历数据加载限制到指定的日期范围。
- 清除此复选框可包含 **Ephemeris model** 表中定义的完整日期范围的数据。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `useDateRange` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Start date (JD)** — 星历日期范围的开始日期 `juliandate(2020, 1, 1)`（默认）| 儒略日

星历日期范围的开始日期，指定为儒略日。

#### 依赖项

要启用此参数，将 **Limit ephemerides date range** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `startDate` |
| **Type**: character vector |
| **Values**: `'juliandate(2020, 1, 1)'` | Julian date |
| **Default**: `'juliandate(2020, 1, 1)'` |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)`（默认）| 儒略日

星历日期范围的结束日期，指定为儒略日。

#### 依赖项

要启用此参数，将 **Limit ephemerides date range** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `endDate` |
| **Type**: character vector |
| **Values**: `'juliandate(2050, 1, 1)'` | Julian format date |
| **Default**: `'juliandate(2050, 1, 1)'` |

### **Include third body gravity** — 第三体引力引起的加速度 `off`（默认）| `on`

要在轨道传播计算中包含第三体引力引起的加速度，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `useThirdBodyGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Sun** — 包含太阳引起的引力加速度 `on`（默认）| `off`

要包含太阳引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Sun gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeSunGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'on'` |

### **Sun gravity model** — 太阳的第三体引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Sun** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Sun** 第三体引力参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `sunThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Mercury** — 包含水星引起的引力加速度 `off`（默认）| `on`

要包含水星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Mercury gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Mercury` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeMercuryGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Mercury gravity model** — 水星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Mercury** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Mercury** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `mercuryThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Venus** — 包含金星引起的引力加速度 `off`（默认）| `on`

要包含金星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Venus gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Venus` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeVenusGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Venus gravity model** — 金星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Venus** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Venus** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `venusThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Earth** — 包含地球引起的引力加速度 `on`（默认）| `off`

要包含地球引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Earth gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Earth` 以外的任何值。
- 将 **Include third body gravity** 设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeEarthGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Earth gravity model** — 地球引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选中 **Earth** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Earth` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Earth** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `earthThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Moon** — 包含月球引起的引力加速度 `on`（默认）| `off`

要包含月球引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Moon gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Moon` 以外的任何值。
- 将 **Include third body gravity** 设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeMoonGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` | |
| **Default:** `'on'` |

### **Moon gravity model** — 月球引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选中 **Moon** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Moon` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Moon** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `moonThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Mars** — 包含火星引起的引力加速度 `off`（默认）| `on`

要包含火星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Mars gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Mars` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeMarsGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` | |
| **Default:** `'off'` |

### **Mars gravity model** — 火星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选中 **Mars** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Mars` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Mars** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `marsThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **Default:** `'Point-mass'` |

### **Jupiter** — 包含木星引起的引力加速度 `off`（默认）| `on`

要包含木星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Jupiter gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Jupiter` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeJupiterGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Jupiter gravity model** — 木星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Jupiter** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Jupiter` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 on。
- 将 **Jupiter** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `jupiterThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Saturn** — 包含土星引起的引力加速度 `off`（默认）| `on`

要包含土星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Saturn gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Saturn` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeSaturnGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Saturn gravity model** — 土星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Saturn** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Saturn` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Saturn** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `saturnThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Uranus** — 包含天王星引起的引力加速度 `off`（默认）| `on`

要包含天王星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Uranus gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Uranus` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeUranusGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Uranus gravity model** — 天王星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Uranus** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Uranus` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Uranus** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `uranusThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Neptune** — 包含海王星引起的引力加速度 `off`（默认）| `on`

要包含海王星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Neptune gravity model 中选择。

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Neptune` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeNeptuneGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Neptune gravity model** — 海王星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Neptune** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Central Body** 参数设置为除 `Neptune` 以外的任何值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Neptune** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `neptuneThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Pluto** — 包含冥王星引起的引力加速度 `off`（默认）| `on`

要包含冥王星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Pluto gravity model 中选择。

#### 依赖项

要启用此参数，将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includePlutoGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Pluto gravity model** — 冥王星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Pluto** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖项

要启用此参数：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Pluto** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `plutoThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Custom** — 包含自定义行星引起的引力加速度 `off`（默认）| `on`

要包含自定义行星引起的引力加速度，请选中此复选框。否则，清除它。要指定引力模型，请从 Custom gravity model 中选择。

#### 依赖项

要启用此参数，将 **Include third body gravity** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `includeCustomGravity` |
| **Type:** character vector |
| **Values**: `'off'` | `'on'` |
| **Default:** `'off'` |

### **Custom gravity model** — 自定义引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选中 **Custom** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖项

要启用此参数：

- 选择 **Include third body gravity** 参数。
- 选择 **Custom** 参数。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customThirdBodyGravityModel` |
| **Type:** character vector |
| **Values**: `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **Default:** `'Point-mass'` |

### **Gravitational parameter (m^3/s^2)** — 自定义引力加速度 `42.828314258067e12`（默认）| 标量 | 长度为 *numCustom3rdBodies* 的向量

自定义第三体的自定义引力加速度，指定为标量或长度为 *numCustom3rdBodies* 的向量。*numCustom3rdBodies* 是提供给 **R\_cb** 输入端的行数。提供多个值以包含多个自定义天体。

#### 依赖项

要启用此参数：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Custom** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `customThirdBodyMu` |
| **Type:** character vector |
| **Values**: `'42.828314258067e12'` | scalar | vector of length *numCustom3rdBodies* |
| **Default:** `'42.828314258067e12'` |

### SRP

### **Include solar radiation pressure (SRP)** — 太阳辐射压引起的加速度 `off`（默认）| `on`

要在轨道传播计算中包含太阳辐射压引起的加速度，请选中此复选框。否则，清除此复选框。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Eclipse fraction source** — 食分来源 `Dialog`（默认）| `Port`

食分（从航天器位置可见的太阳圆盘比例）的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数，将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `useSRP` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Port'` |
| **Default**: `'Dialog'` |

### **Shadow model** — 阴影模型 `Dual cone`（默认）| `Cylindrical`

用于食计算的阴影模型，指定为以下值之一。

- `Cylindrical` — 比例可以为 0.0（Umbra）或 1.0（Sunlight）。
- `Dual cone` — 比例可以为 0.0（Umbra）、介于 0.0 和 1.0 之间（Penumbra 或 Antumbra）或 1.0（Sunlight）。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `shadowModel` |
| **Type:** character vector |
| **Values:** `'Dual cone'` | `'Cylindrical'` |
| **Default:** `'Dual cone'` |

### **Include Earth** — 包含地球的选项 `on`（默认）| `off`

当中心天体为 Moon 时，在食计算中将地球作为次要掩食体包含的选项。

#### 依赖项

将 **Central body** 参数设置为 `Moon`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `includeEarth` |
| **Type**: character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Include Moon** — 包含月球的选项 `on`（默认）| `off`

当中心天体为 Earth 时，在食计算中将月球作为次要掩食体包含的选项。

#### 依赖项

将 **Central body** 参数设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `includeMoon` |
| **Type**: character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Reflectivity coefficient source** — 航天器反射率系数来源 `'Dialog'`（默认）| `'Port'`

航天器反射率系数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数，将 **Include solar radiation pressure (SRP)** 设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `reflectivityCoeffSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default:** `'on'` |

### **Reflectivity coefficient** — 航天器反射率系数 `1.8`（默认）| 标量 | 大小为 *numSat* 的二维数组 | 介于 `[1,2]`

用于太阳辐射压计算的航天器反射率系数，指定为标量、大小为 *numSat* 的二维数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Reflectivity coefficient source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `reflectivityCoeff` |
| **Type**: character vector |
| **Values:** `'1.8'` | scalar | 2D array of size *numSat* | between `[1,2]` |
| **Default:** `'1.8'` |

### **SRP area source** — 航天器太阳辐射压面积来源 `Dialog`（默认）| `Port`

航天器太阳辐射压 (SRP) 面积的来源，指定为 `Dialog` 或 `Port`。

#### 依赖项

要启用此参数，将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `srpAreaSrc` |
| **Type**: character vector |
| **Values:** `'Dialog'` | `'Port'` |
| **Default**: `'Dialog'` |

### **SRP area** — 太阳看到的航天器横截面积 `1.0`（默认）| 标量 | 大小为 *numSat* 的二维数组

太阳看到的航天器横截面积，指定为标量或大小为 *numSat* 的二维数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖项

要启用此参数

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **SRP area source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `srpArea` |
| **Type**: character vector |
| **Values:** `'1.0'` | scalar | 2D array of size *numSat* |
| **Default**: `'1.0'` |

### **Solar flux pressure (W\*s/m^3)** — 航天器太阳通量压力 `4.5344321e-6`（默认）| 标量

太阳通量压力，指定为标量。

**可调：** 是

#### 依赖项

要启用此参数，将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **Block Parameter**: `fluxPressure` |
| **Type**: character vector |
| **Values:** `4.5344321e-6` | scalar |
| **Default:** `'4.5344321e-6'` |

### 单位

### **Units** — 参数和端口单位 `Metric (m/s)`（默认）| `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

参数和端口单位，如下所示。

| 单位 | Forces | Moment | Mass | Inertia | Distance | Velocity | Acceleration | Area | Density |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | Newton | Newton-meter | Kilograms | Kilogram m2 | meters | meters/sec | meters/sec2 | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/s)` | Newton | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/sec | kilometers/sec2 | m2 | kg/m3, some density outputs 1/m3 |
| `Metric (km/h)` | Newton | Newton-meter | Kilograms | Kilogram m2 | kilometers | kilometers/hour | kilometers/hour2 | m2 | kg/m3, some density outputs 1/m3 |
| `English (ft/s)` | Pound-force | Foot-pound | Slugs | Slug ft2 | feet | feet/sec | feet/sec2 | feet2 | lbm/ft3, some density outputs 1/ft3 |
| `English (kts)` | Pound-force | Foot-pound | Slugs | Slug ft2 | nautical mile | knots | knots/sec | feet2 | lbm/ft3, some density outputs 1/ft3 |

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `units` |
| **Type:** character vector |
| **Values:** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **Default:** `'Metric (m/s)'` |

### **Angle units** — 角度单位 `Degrees`（默认）| `Radians`

参数和端口的角度单位，指定为 `Degrees` 或 `Radians`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:** `angleUnits` |
| **Type:** character vector |
| **Values:** `'Degrees'` | `'Radians'` |
| **Default:** `'Degrees'` |

### **Time format** — 开始日期和时间输出的时间格式 `Julian date`（默认）| `Gregorian`

**Start date/time (UTC Julian date)** 和输出端口 **tutc** 的时间格式，指定为 `Julian date` 或 `Gregorian`。

#### 程序化使用

|  |
| --- |
| **Block Parameter:**  `timeFormat` |
| **Type:** character vector |
| **Values:** `'Julian date'` | `'Gregorian'` |
| **Default:** `'Julian date'` |

## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2025a: Spacecraft Dynamics 模块支持第三体的高保真引力效应

Spacecraft Dynamics 模块现在使用新的第三体引力选项支持更高保真度的工作流。使用这些选项可在航天器仿真中更准确地建模轨道传播。

要访问这些效应，请在 **Third Body** 选项卡上选中 **Include third body gravity** 参数。**Include third body gravity** 参数取代了 **Include third body point-mass gravity** 参数。

选中 **Include third body gravity** 可配置 Sun、Mercury、Venus、Moon、Earth、Mars、Jupiter、Saturn、Uranus、Neptune、Pluto 和 Custom 的引力选项。

### R2023b: Spacecraft Dynamics 模块变更

Spacecraft Dynamics 模块已更新，以考虑：

- 第三体引力对轨道传播的影响。
- 来自 `aeroReadSpaceWeatherData` 函数生成的数据文件的空间天气数据。
- 太阳辐射压 (SRP)。

## 描述

对一个或多个航天器的动力学建模

Spacecraft Dynamics 模块使用数值积分对航天器的平移和旋转动力学进行建模。它计算一个或多个航天器随时间的位置、速度、姿态和角速度。为获得最准确的结果，请使用低容差设置（小于 1e-8）的变步长求解器。要以精度换取速度，可根据任务要求使用更大的容差。

您可以将初始轨道状态定义为

- 一组轨道元素。
- 位置和速度状态向量。

要传播轨道状态，模块使用为当前中心天体选择的引力模型。它还包括您作为模块输入提供的外部加速度和力。要定义初始姿态状态，请使用四元数、方向余弦矩阵 (DCM) 或欧拉角。

要传播姿态状态，模块使用作为模块输入提供的力矩以及模块上定义的质量属性。

Aerospace Blockset™ 使用按标量在前约定定义的四元数。

Spacecraft Dynamics 模块支持标量和向量扩展。模块参数和输入端口维度决定输出信号的数量和航天器数量。在标量和向量扩展之后，**Orbit**、**Mass** 和 **Attitude** 选项卡中的所有参数以及除 **φθψ**（月球天平动角）和 **αδW**（赤经、赤纬和旋转角）输入端口之外的所有输入端口，都会为每个航天器定义。

提供的初始条件大小决定所建模的航天器数量。如果您为 **Orbit**、**Attitude** 或 **Mass** 选项卡中的某个参数提供多个值，模块将输出卫星星座。任何提供单个值的参数都会扩展并应用于星座中的所有卫星。例如，如果您为模块上的所有参数提供单个值，但 **True anomaly** 包含六个值，则模块会创建一个由六颗卫星组成的星座，仅改变真近点角。

模块对模块输入端口应用相同的扩展行为。所有输入端口都支持扩展，但 **Moon libration angles**（当 **Central body** 为 `Moon` 时）以及 **Spin axis right ascension (RA) at J2000**、**Spin axis declination (Dec) at J2000** 和 **Initial rotation angle at J2000**（当 **Central body** 为 `Custom` 时）除外。所有其他端口接受单个值并扩展到所有正在建模的航天器，或者接受应用于每颗航天器的单独值。

有关 Spacecraft Dynamics 模块使用的坐标系以及旋转和平移动力学的更多信息，请参阅算法。

### 大气阻力

为帮助对航天器进行高精度轨道传播时的阻力建模，Spacecraft Dynamics 模块支持阻力。大气阻力会影响在低地球轨道 (LEO) 飞行的航天器；离地球越远，其相关性越低。有关大气阻力方程，请参阅平移动力学。

### 第三体引力效应

要包含质点第三体引力的效应，请选择要包含哪些第三体。这些计算需要 **Ephemeris model** 和数据。有关第三体贡献方程，请参阅平移动力学。

### 太阳辐射压

要包含太阳辐射压 (SRP) 对航天器的影响，请提供食分或指定阴影模型来计算该比例。当大气阻力可忽略且指向精度要求严格时，请考虑将太阳辐射压纳入考虑。有关太阳辐射压方程，请参阅平移动力学。
