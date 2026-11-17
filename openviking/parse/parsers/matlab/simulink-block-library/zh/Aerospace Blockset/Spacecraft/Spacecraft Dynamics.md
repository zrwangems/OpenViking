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
```yaml
ports:
- name: Fb
  summary: 施加的力 三元向量 | *numSat*×3 数组
  direction: input
  data_types: double
- name: Mb
  summary: 施加的力矩 三元向量 | *numSat*×3 数组
  direction: input
  data_types: double
- name: A
  summary: 外部加速度 三元向量 | *m*×3 数组
  direction: input
  data_types: double
- name: φθψ
  summary: 月球天平动角 三元向量
  direction: input
  data_types: double
- name: αδW
  summary: 赤经、赤纬和旋转角 三元向量
  direction: input
  data_types: double
- name: m
  summary: 航天器质量 标量 | 大小为 *numSat* 的一维数组
  direction: input
  data_types: double
- name: dm/dt
  summary: 质量变化率 标量 | 大小为 *numSat* 的一维数组
  direction: input
  data_types: double
- name: I
  summary: 航天器惯性张量 3×3 数组 | 3×3×*numSat* 数组
  direction: input
  data_types: double
- name: dI/dt
  summary: 惯性张量矩阵变化率 3×3 数组 | 3×3×*numSat* 数组
  direction: input
  data_types: double
- name: Vre
  summary: 相对速度 三元向量 | *numSat*×3 数组
  direction: input
  data_types: double
- name: ρ
  summary: 大气密度 标量
  direction: input
  data_types: double
- name: F107a
  summary: 81 天平均 Ottawa F10.7 cm 太阳通量 标量
  direction: input
  data_types: double
- name: F107
  summary: 每日 Ottawa F10.7 cm 太阳通量 标量
  direction: input
  data_types: double
- name: aph
  summary: 每日磁指数信息 *N*×7 数组
  direction: input
  data_types: double
- name: Flags
  summary: 变化标志 23 元数组
  direction: input
  data_types: double
- name: Cd
  summary: 大气阻力系数 标量 | 大小为 *numSat* 的向量
  direction: input
  data_types: double
- name: Ad
  summary: 大气阻力面积 标量 | 大小为 *numSat* 的向量
  direction: input
  data_types: double
- name: Rcb, 3
  summary: 一个或多个自定义天体的位置 三元向量 | *numCustom3rdBodies*×3 元向量
  direction: input
  data_types: double
- name: Fraction
  summary: 太阳圆盘比例，介于 0（全食）和 1（全日照）之间 | 标量 | *numSat*
  direction: input
  data_types: double
- name: RC
  summary: 反射系数 标量或 *numSat* 个值，范围 1≤*RC*≤2
  direction: input
  data_types: double
- name: Asrp
  summary: 航天器横截面积 标量 | *numSat*
  direction: input
  data_types: double
- name: X
  summary: 航天器位置 三元向量 | *numSat*×3 数组
  direction: output
  data_types: double
- name: V
  summary: 速度 三元向量 | *numSat*×3 数组
  direction: output
  data_types: double
- name: A
  summary: 总惯性加速度 三元向量 | *numSat*×3 数组
  direction: output
  data_types: double
- name: qbody2icrf
  summary: 航天器姿态四元数 四元四元数 | *numSat*×4 数组
  direction: output
  data_types: double
- name: DCM
  summary: 航天器姿态方向余弦矩阵 3×3 数组 | *numSat*×3×3 数组
  direction: output
  data_types: double
- name: R1,R2,R3
  summary: 航天器姿态欧拉角 三元向量 | *numSat*×3 数组
  direction: output
  data_types: double
- name: ω
  summary: 航天器角速率 三元向量 | *numSat*×3 数组
  direction: output
  data_types: double
- name: dω/dt
  summary: 体角加速度 三元数组 | *numSat*×3 数组
  direction: output
  data_types: double
- name: qicrf2ff
  summary: 坐标系变换 四元数组
  direction: output
  data_types: double
- name: tutc
  summary: 当前时间步的时间标量 | 6 元素数组
  direction: output
  data_types: double
- name: Fuel Status
  summary: 燃料状态标量 | *numSat* 元素数组
  direction: output
  data_types: double
```

### 输入

### **Fb** — 施加的力 三元向量 | *numSat*×3 数组

在当前时间步施加到航天器质心的体坐标系力，指定为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Input body forces** 参数设置为 `on`。

**数据类型：** `double`

### **Mb** — 施加的力矩 三元向量 | *numSat*×3 数组

在当前时间步施加到航天器相对于质心的体坐标系力矩，指定为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Input body moments** 参数设置为 `on`。

**数据类型：** `double`

### **A** — 外部加速度 三元向量 | *m*×3 数组

在当前时间步施加到航天器相对于 ICRF 或固定坐标系的外部加速度，指定为三元向量或 *m*×3 数组。

#### 依赖

要启用此端口，请将 **Input external accelerations** 参数设置为 `on`。

要指定加速度坐标系，请设置 **External acceleration coordinate frame** 参数。

**数据类型：** `double`

### **φθψ** — 月球天平动角 三元向量

用于在 ICRF 和以月球为中心的固定坐标系之间进行变换的月球天平动角，使用以月球为中心的主轴（PA）系统，指定为三元向量。要获取这些值，请使用 Moon Libration 模块。

**注意**

当 **Central body** 设置为 `Moon` 时，此模块使用的固定坐标系是平地球/极轴（ME）系统。有关详细信息，请参阅算法。

#### 依赖

要启用此端口：

- 将 **Central body** 设置为 `Moon`。
- 将 **Input Moon libration angles** 参数设置为 `on`。

**数据类型：** `double`

### **αδW** — 赤经、赤纬和旋转角 三元向量

中心天体自转轴的瞬时赤经、赤纬和旋转角，指定为三元向量。此端口仅适用于自定义中心天体。

#### 依赖

要启用此端口：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Port`。

**数据类型：** `double`

### **m** — 航天器质量 标量 | 大小为 *numSat* 的一维数组

当前时间步的航天器质量。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dm/dt** — 质量变化率 标量 | 大小为 *numSat* 的一维数组

当前时间步的质量变化率（吸积为正，烧蚀为负），指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Mass type** 设置为 `Simple Variable`。

**数据类型：** `double`

### **I** — 航天器惯性张量 3×3 数组 | 3×3×*numSat* 数组

当前时间步的航天器惯性张量，指定为 3×3 数组或 3×3×*numSat* 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵变化率 3×3 数组 | 3×3×*numSat* 数组

当前时间步的惯性张量矩阵变化率，指定为 3×3 数组或 3×3×*numSat* 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Mass type** 设置为 `Custom Variable`。

**数据类型：** `double`

### **Vre** — 相对速度 三元向量 | *numSat*×3 数组

质量在体坐标系中被吸积到机体或从机体烧蚀的相对速度，指定为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口：

- 将 **Mass type** 设置为 `Custom Variable` 或 `Simple Variable`。
- 将 **Include mass flow relative velocity** 参数设置为 `on`。

**数据类型：** `double`

### **ρ** — 大气密度 标量

用于计算大气阻力加速度的大气密度。

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Port`。

**数据类型：** `double`

### **F107a** — 81 天平均 Ottawa F10.7 cm 太阳通量 标量

以 **Start date/time** 中指定的当前日期为中心的 81 天平均 Ottawa F10.7 cm 太阳通量。这些 F107 平均值对应于地球到太阳实际距离处的 10.7 cm 射电通量。此网站提供两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **F107** — 每日 Ottawa F10.7 cm 太阳通量 标量

以 **Start date/time** 中指定的当前日期为中心的每日 Ottawa F10.7 cm 太阳通量。f107Daily 值不对应于 1 AU 处的射电通量。此网站提供两类值：

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-radio/noontime-flux/penticton/

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **aph** — 每日磁指数信息 *N*×7 数组

每日磁指数信息（aph），指定为 *N*×7 数组。磁指数信息包括：

|  |
| --- |
| 每日磁指数（AP） |
| 当前时间的 3 小时 AP |
| 当前时间前 3 小时的 3 小时 AP |
| 当前时间前 6 小时的 3 小时 AP |
| 当前时间前 9 小时的 3 小时 AP |
| 当前时间前 12 至 33 小时的八个 3 小时 AP 指数的平均值 |
| 当前时间前 36 至 57 小时的八个 3 小时 AP 指数的平均值 |

每日磁指数的影响在 80,000 m 以下不大或不明确。有关详细信息，请参阅 NRLMSISE-00 Atmosphere Model 的限制。

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

**数据类型：** `double`

### **Flags** — 变化标志 23 元数组

变化标志，指定为 23 元数组，用于启用或禁用输出的特定变化。您可以为字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0

  移除该值对输出的影响。
- 1.0

  将该值的主效应和交叉项效应应用于输出。
- 2.0

  仅将该值的交叉项效应应用于输出。

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
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，模块将使用完整的磁指数信息矩阵（APH）而不是 `APH(:,1)` |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度 |
| `Flags(12)` | UT 和混合 UT、经度 |
| `Flags(13)` | 混合 AP、UT、经度 |
| `Flags(14)` | 三分之一日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 所有来自 120,000 米温度（TLB）的变化 |
| `Flags(18)` | 所有低热层（TN1）温度变化 |
| `Flags(19)` | 所有 120,000 米梯度（S）变化 |
| `Flags(20)` | 所有上平流层（TN2）温度变化 |
| `Flags(21)` | 所有来自 120,000 米值（ZLB）的变化 |
| `Flags(22)` | 所有低中间层温度（TN3）变化 |
| `Flags(23)` | 湍流层顶标高变化 |

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Flags source** 参数设置为 `Port`。

**数据类型：** `double`

### **Cd** — 大气阻力系数 标量 | 大小为 *numSat* 的向量

大气阻力系数，指定为标量或大小为 *numSat* 的向量。

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag coefficient source** 参数设置为 `Port`。

**数据类型：** `double`

### **Ad** — 大气阻力面积 标量 | 大小为 *numSat* 的向量

大气阻力面积，指定为标量或大小为 *numSat* 的向量。

#### 依赖

要启用此端口：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Drag area source** 参数设置为 `Port`。

**数据类型：** `double`

### **Rcb, 3** — 一个或多个自定义天体的位置 三元向量 | *numCustom3rdBodies*×3 元向量

一个或多个自定义天体相对于当前中心天体的位置，在 ICRF 坐标系中。*numCustom3rdBodies* 是自定义天体数量。有关详细信息，请参阅 **Custom gravitational parameter (m^3/s^2)**。

#### 依赖

要启用此端口：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Custom** 参数设置为 `on`。

**数据类型：** `double`

### **Fraction** — 太阳圆盘比例，介于 `0`（全食）和 `1`（全日照）之间 | 标量 | *numSat*

从航天器位置可见的太阳圆盘比例。*numSat* 是航天器数量。

#### 依赖

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Eclipse fraction source** 设置为 `Port`。

**数据类型：** `double`

### **RC** — 反射系数 标量或 *numSat* 个值，范围 `1`≤*RC*≤`2`

反射系数，指定为标量或 *numSat* 个值，范围 `1`≤*RC*≤`2`。*numSat* 是航天器数量。

#### 依赖

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Reflectivity coefficient source** 参数设置为 `Port`。

**数据类型：** `double`

### **Asrp** — 航天器横截面积 标量 | *numSat*

太阳可见的航天器横截面积，指定为标量或 *numSat*。模块使用此值计算太阳辐射压引起的加速度。

#### 依赖

要启用此端口：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **SRP area source** 参数设置为 `Port`。

**数据类型：** `double`
### 输出

### **X** — 航天器位置 三元向量 | *numSat*×3 数组

航天器相对于 ICRF 或固定坐标系输出端口坐标系的位置，在当前时间步返回为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

- 要更改此端口的输出坐标系，请设置 **State vector output coordinate frame** 参数。
- **Mass**、**Orbit** 或 **Attitude** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **V** — 速度 三元向量 | *numSat*×3 数组

航天器相对于 ICRF 或固定坐标系输出端口坐标系的速度，在当前时间步返回为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

- 要更改此端口的输出坐标系，请设置 **State vector output coordinate frame** 参数。
- **Mass**、**Orbit** 或 **Attitude** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **A** — 总惯性加速度 三元向量 | *numSat*×3 数组

航天器相对于 ICRF 的总惯性加速度，在当前时间步返回为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

- 要启用此端口，请将 **Output total inertial acceleration** 参数设置为 `on`。
- **Orbit** 选项卡中提供的初始条件大小控制端口维度。

**数据类型：** `double`

### **qbody2icrf** — 航天器姿态四元数 四元四元数 | *numSat*×4 数组

航天器姿态四元数，返回为从体轴到输出端口坐标系的（标量在前）四元数旋转，作为四元四元数或 *numSat*×4 数组（标量在前），在当前时间步。*numSat* 是航天器数量。

#### 依赖

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Quaternion`。

**数据类型：** `double`

### **DCM** — 航天器姿态方向余弦矩阵 3×3 数组 | *numSat*×3×3 数组

航天器姿态方向余弦矩阵（DCM），返回为 3×3 数组或 *numSat*×3×3 数组。*numSat* 是航天器数量。

#### 依赖

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `DCM`。

**数据类型：** `double`

### **R1,R2,R3** — 航天器姿态欧拉角 三元向量 | *numSat*×3 数组

航天器姿态欧拉角，返回为三元向量或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

此端口的坐标系和姿态格式取决于以下设置：

- 要指定姿态参考坐标系，请设置 **Attitude reference coordinate frame** 参数。
- 将 **Attitude representation** 设置为 `Euler angles`。

**数据类型：** `double`

### **ω** — 航天器角速率 三元向量 | *numSat*×3 数组

航天器相对于姿态参考坐标系的角速率，返回为三元向量或 *numSat*×3 数组，表示为体轴角速率 PQR。*numSat* 是航天器数量。

#### 依赖

姿态参考坐标系取决于 **Attitude reference coordinate frame** 参数。

**数据类型：** `double`

### **dω/dt** — 体角加速度 三元数组 | *numSat*×3 数组

相对于 ICRF 坐标系的体角加速度，返回为三元数组或 *numSat*×3 数组。*numSat* 是航天器数量。

#### 依赖

要启用此端口，请将 **Output total inertial angular acceleration** 参数设置为 `on`。

姿态参考坐标系取决于 **Attitude reference coordinate frame** 参数。

**数据类型：** `double`

### **qicrf2ff** — 坐标系变换 四元数组

当前时间步 ICRF 和固定坐标系之间的坐标系变换，返回为四元数组。

#### 依赖

要启用此端口，请将 **Output quaternion (ICRF to Fixed-frame)** 参数设置为 `on`。

**数据类型：** `double`

### **tutc** — 当前时间步的时间标量 | 6 元素数组

当前时间步的时间，返回为：

- 标量 — 如果将 **Start data/time** 参数指定为儒略日。
- 6 元素数组 — 如果将 **Start data/time** 参数指定为包含六个元素（年、月、日、小时、分钟、秒）的格里高利日期。

此值等于 **Start date/time** 参数值加上经过的仿真时间。

#### 依赖关系

要启用此参数，请将 **Output current date/time (UTC Julian date)** 参数设置为 `on`。

**数据类型：** `double`

### **Fuel Status** — 燃料状态标量 | *numSat* 元素数组

当前时间步的燃料箱状态，返回为标量或 *numSat* 元素数组，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱未满或未空。
- `-1` — 燃料箱已空。

*numSat* 是航天器数量。

#### 依赖关系

要启用此端口：

- 将 **Mass type** 设置为 `Simple Variable`。
- 将 **Output fuel tank status** 参数设置为 `on`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Input body forces
  summary: 启用外部力的选项 on（默认）| off
  group: 主要
  block_parameter: forcesin
  type: 字符向量
  values: '''off'' | ''on'''
- name: Input body moments
  summary: 启用外部力矩的选项 on（默认）| off
  group: 主要
  block_parameter: momentsIn
  type: 字符向量
  values: '''off'' | ''on'''
- name: Input external accelerations
  summary: 输入附加力加速度的选项 off（默认）| on
  group: 主要
  block_parameter: accelIn
  type: 字符向量
  values: '''off'' | ''on'''
- name: External acceleration coordinate frame
  summary: 加速度输入端口坐标系 ICRF（默认）| Fixed-frame
  group: 主要
  block_parameter: accelFrame
  type: 字符向量
  values: '''ICRF'' | ''Fixed-frame'''
- name: State vector output coordinate frame
  summary: 位置和速度状态输出端口坐标系 ICRF（默认）| Fixed-frame
  group: 主要
  block_parameter: outportFrame
  type: 字符向量
  values: '''ICRF'' | ''Fixed-frame'''
- name: Output total inertial acceleration
  summary: 启用总加速度端口的选项 off（默认）| on
  group: 主要
  block_parameter: AccelOut
  type: 字符向量
  values: '''on'' | ''off'''
- name: Start date/time (UTC Julian date)
  summary: 仿真的初始开始时间 juliandate (2020, 1, 1, 12, 0, 0)（默认）| 有效的标量儒略日 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，作为一维或六元素数组
  group: 主要
  block_parameter: startDate
  type: 字符向量
  values: '''juliandate(2020, 1, 1, 12, 0, 0)'' | 有效的标量儒略日 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，作为一维或六元素数组'
- name: Output current date/time (UTC Julian date)
  summary: 添加输出端口 tutc 的选项 on（默认）| off
  group: 主要
  block_parameter: dateOut
  type: 字符向量
  values: '''off'' | ''on'''
- name: Action for out-of-range input
  summary: 超出范围时的模块行为 Warning（默认）| Error | None
  group: 主要
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
- name: Mass type
  summary: 航天器质量类型 Fixed（默认）| Simple Variable | Custom Variable
  group: 质量
  block_parameter: massType
  type: 字符向量
  values: '''Fixed'' | ''Simple Variable'' | ''Custom Variable'''
- name: Mass
  summary: 刚体航天器的初始质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量
  group: 质量
  block_parameter: mass
  type: 字符向量
  values: 标量 | 大小为 *numSat* 的向量
- name: Empty mass
  summary: 航天器空载质量 3.5（默认）| 标量 | 大小为 *numSat* 的向量
  group: 质量
  block_parameter: emptyMass
  type: 字符向量
  values: 大小为 *numSat* 的一维数组 | 大小为 *numSat* 的一维数组
- name: Full mass
  summary: 航天器满载质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量
  group: 质量
  block_parameter: fullMass
  type: 字符向量
  values: 标量 | 大小为 *numSat* 的向量
- name: Inertia tensor
  summary: 惯量张量矩阵 [0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]（默认）| 3×3 数组 | 3×3×*numSat* 数组
  group: 质量
  block_parameter: inertia
  type: 字符向量
  values: '''[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'' | 3×3 数组 | 3×3×*numSat* 数组'
- name: Empty inertia tensor
  summary: 空载惯量张量矩阵 [0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]（默认）| 3×3 数组 | 3×3×*numSat* 数组
  group: 质量
  block_parameter: emptyInertia
  type: 字符向量
  values: 3×3 数组 | 3×3×*numSat* 数组
- name: Full inertia tensor
  summary: 满载惯量张量矩阵 [0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]（默认）| 3×3 数组 | 3×3×*numSat* 数组
  group: 质量
  block_parameter: fullInertia
  type: 字符向量
  values: 3×3 数组 | 3×3×*numSat* 数组
- name: Include mass flow relative velocity
  summary: 启用质量流速度的选项 off（默认）| on
  group: 质量
  block_parameter: useMassFlowRelativeVelocity
  type: 字符向量
  values: '''on'' | ''off'''
- name: Limit mass flow when mass is empty or full
  summary: 限制质量流的选项 on（默认）| off
  group: 质量
  block_parameter: limitMassFlow
  type: 字符向量
  values: '''on'' | ''off'''
- name: Output fuel tank status
  summary: 启用燃料箱状态的选项 on（默认）| off
  group: 质量
  block_parameter: outputFuelStatus
  type: 字符向量
  values: '''on'' | ''off'''
- name: Initial state format
  summary: 轨道初始状态的输入方法 Orbital elements（默认）| ICRF state vector | Fixed-frame state vector
  group: 轨道
  block_parameter: stateFormatNum，当 propagator 设置为 High precision (numerical) 时
  type: 字符向量
  values: '''Orbital elements'' | ''Orbital elements'' | ''ICRF state vector'' | ''Fixed-frame state''，当 propagator 设置为 ''High
    precision (numerical)'' 时'
- name: Orbit type
  summary: 轨道分类 Keplerian（默认）| Elliptical equatorial | Circular | Circular equatorial
  group: 轨道
  block_parameter: orbitType
  type: 字符向量
  values: '''Keplerian'' | ''Elliptical equatorial'' | ''Circular inclined'' | ''Circular equatorial'''
- name: Semi-major axis
  summary: 椭圆长轴的一半 6786000（默认）| 标量 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: semiMajorAxis
  type: 字符向量
  values: 标量 | 大小为 *numSat* 的一维数组
- name: Eccentricity
  summary: 轨道偏离度 0.01（默认）| 标量 | 0 到 1 之间的值，或对于 Keplerian 轨道类型大于 1 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: eccentricity
  type: 字符向量
  values: 0.01 | 标量 | 0 到 1 之间的值，或对于 Keplerian 轨道类型大于 1 | 大小为 *numSat* 的一维数组
- name: Inclination
  summary: 轨道平面的倾斜角 50（默认）| 标量 | 大小为 *numSat* 的一维数组 | 0 到 180 度 | 0 到 pi 弧度
  group: 轨道
  block_parameter: inclination
  type: 字符向量
  values: 50 | 标量 | 大小为 *numSat* 的一维数组 | 0 到 180 度 | 0 到 pi 弧度
- name: RAAN
  summary: 赤道面内的角距离 95（默认）| 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: raan
  type: 字符向量
  values: '''95'' | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组'
- name: Argument of periapsis
  summary: 从航天器升交点到近拱点的角度 93（默认）| 0 到 360 之间的值 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: argPeriapsis
  type: 字符向量
  values: 93 | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组
- name: True anomaly
  summary: 近拱点与航天器初始位置之间的角度 203（默认）| 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: trueAnomaly
  type: 字符向量
  values: '''203'' | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组'
- name: Argument of latitude
  summary: 升交点与航天器初始位置之间的角度 200（默认）| 标量 | 0 到 360 之间的值 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: argLat
  type: 字符向量
  values: '''200'' | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组'
- name: Longitude of periapsis
  summary: ICRF *x* 轴与偏心率向量之间的角度 100（默认）| 标量 | 0 到 360 之间的值 | 大小为 *numSat* 的一维数组
  group: 轨道
  block_parameter: lonPeriapsis
  type: 字符向量
  values: 100 | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组
- name: True longitude
  summary: ICRF *x* 轴与航天器初始位置之间的角度 150（默认）| 标量 | 0 到 360 之间的值 | 大小为 *numSat* 的一维数组 | *numSat*×3 向量
  group: 轨道
  block_parameter: trueLon
  type: 字符向量
  values: '''150'' | 0 到 360 之间的标量值 | 大小为 *numSat* 的一维数组 | *numSat*×3 向量'
- name: ICRF position
  summary: 航天器的笛卡尔位置向量 [3649700.0 3308200.0 -4676600.0]（默认）| 3 元素向量 | | *numSat*×3 数组
  group: 轨道
  block_parameter: inertialPosition
  type: 字符向量
  values: '[3649700.0 3308200.0 -4676600.0] | 3 元素向量 | *numSat*×3 数组'
- name: ICRF velocity
  summary: 航天器的笛卡尔速度向量 [-2750.8 6666.4 2573.4]（默认）| 3 元素向量 | *numSat*×3 数组
  group: 轨道
  block_parameter: inertialVelocity
  type: 字符向量
  values: '[-2750.8 6666.4 2573.4] | 3 元素向量 | 大小为 *numSat*×3 数组的二维数组'
- name: Fixed-frame position
  summary: 航天器的位置向量 [-4142689.0 -2676864.7 -4669861.6]（默认）| 3 元素向量 | *numSat*×3 数组
  group: 轨道
  block_parameter: fixedPosition
  type: 字符向量
  values: '''[-4142689.0 -2676864.7 -4669861.6]'' | 单个航天器的 3 元素向量 | *numSat*×3 数组'
- name: Fixed-frame velocity
  summary: 航天器的速度向量 [1452.7 -6720.7 2568.1]（默认）| 3 元素向量 | *numSat*×3 数组
  group: 轨道
  block_parameter: fixedVelocity
  type: 字符向量
  values: '''[1452.7 -6720.7 2568.1]'' | 3 元素向量 | *numSat*×3 数组'
- name: Attitude reference coordinate frame
  summary: 姿态和角速率坐标系 ICRF（默认）| Fixed-frame | NED | LVLH
  group: 姿态
  block_parameter: attitudeFrame
  type: 字符向量
  values: '''ICRF'' | ''Fixed-frame'' | ''NED'' | ''LVLH'''
- name: Attitude representation
  summary: 方向格式 Quaternion（默认）| DCM | Euler angles
  group: 姿态
  block_parameter: attitudeFrame
  type: 字符向量
  values: '''Quaternion'' | ''DCM'' | ''Euler angles'''
- name: Initial body attitude
  summary: 航天器初始姿态 [1, 0, 0, 0]（默认）| 4 元素向量 | *numSat*×4 数组 | 3×3 数组 | *numSat*×3×3 数组
  group: 姿态
  block_parameter: attitude
  type: 字符向量
  values: 4 元素向量 | *numSat*×4 数组 | 3×3 数组 | *numSat*×3×3 数组 | 3 元素数组 | *numSat*×3 数组
- name: Angle rotation order
  summary: 角度旋转顺序 ZYX（默认）| ZYX | ZYZ | ZXY | ZXZ | YXZ | YXY | YZX | YZY | XYZ | XYX | XZY | XZX
  group: 姿态
  block_parameter: rotationOrder
  type: 字符向量
  values: '''ZYX'' | ''ZYZ'' |''ZXY'' | ''ZXZ'' | ''YXZ'' | ''YXY'' | ''YZX'' | ''YZY'' | ''XYZ'' | ''XYX'' | ''XZY'' | ''XZX'''
- name: Initial body angular rates PQR
  summary: 初始体坐标系角速率 [0, 0, 0]（默认）| 3 元素向量 | *numSat*×3 数组
  group: 姿态
  block_parameter: attitudeRate
  type: 字符向量
  values: 3 元素向量 | *numSat*×3 数组
- name: Output total inertial angular acceleration
  summary: 启用总飞行器加速度输出的选项 off（默认）| on
  group: 姿态
  block_parameter: angAccelOut
  type: 字符向量
  values: '''on'' | ''off'''
- name: Include gravity gradient torque
  summary: 启用重力梯度力矩的选项 on（默认）| off
  group: 姿态
  block_parameter: angAccelOut
  type: 字符向量
  values: '''on'' | ''off'''
- name: Central body
  summary: 航天器环绕的天体 Earth（默认）| Moon | Mercury | Venus | Mars | Jupiter | Saturn | Uranus | Neptune | Sun | Custom
  group: 中心天体
  block_parameter: centralBody
  type: 字符向量
  values: '''Earth'' | ''Moon'' |''Mercury'' | ''Venus'' | ''Mars'' | ''Jupiter'' | ''Saturn'' | ''Uranus'' | ''Neptune''
    | ''Sun'' | ''Custom'' |'
- name: Gravitational potential model
  summary: 中心天体的重力模型 当 Central body 设置为 Earth、Moon、Mars 或 Custom 时为 Spherical harmonics，当 Central body 设置为 Mercury、Venus、Jupiter、Saturn、Uranus
    或 Neptune 时为 Oblate ellipsoid（默认）| Point-mass | Oblate ellipsoid (J2)
  group: 中心天体
  block_parameter: 当 centralBody 设置为 'Earth'、'Moon'、'Mars' 或 'Custom' 时为 gravityModel | 当 centralBody 设置为 Mercury、Venus、Jupiter、Saturn、Uranus
    或 Neptune 时为 gravityModelnoSH
  type: 字符向量
  values: 当 centralBody 设置为 'Earth'、'Moon'、'Mars' 或 'Custom' 时为 'Spherical harmonics' | 'Point-mass' | 'Oblate ellipsoid (J2)'；当
    centralBody 设置为 Mercury、Venus、Jupiter、Saturn、Uranus 或 Neptune 时为 'Point-mass' | 'Oblate ellipsoid (J2)'
- name: Spherical harmonic model
  summary: 球谐模型 当 Central body 设置为 Earth 时为 EGM2008，当 Central body 设置为 Moon 时为 LP-100K，当 Central body 设置为 Mars 时为 GMM2B，（默认）|
    EGM96 | EIGEN-GL04C | LP-165P
  group: 中心天体
  block_parameter: 当 centralBody 设置为 'Earth' 时为 'earthSH' | 当 centralBody 设置为 'Moon' 时为 'moonSH' | 当 centralBody 设置为 'Mars'
    时为 'marsSH'
  type: 字符向量
  values: 当 centralBody 设置为 'earthSH' 时为 'EGM2008' | 'EGM96' | 'EIGEN-GL04C'；当 centralBody 设置为 'moonSH' 时为 'LP-100K' | 'LP-165P'；当
    centralBody 设置为 'marsSH' 时为 'GMM2B'
- name: Rotational rate
  summary: 旋转速率 4.06124975e-3（默认）| 标量
  group: 中心天体
  block_parameter: '''customOmega'''
  type: 字符向量
  values: '''4.06124975e-3'' | 标量'
- name: Spherical harmonic coefficient file
  summary: 谐波系数 MAT 文件 aerogmm2b.mat（默认）| 谐波系数 MAT 文件
  group: 中心天体
  block_parameter: shFile
  type: 字符向量
  values: '''aerogmm2b.mat'' | 谐波系数 MAT 文件'
- name: Degree
  summary: 谐波模型的阶数 120（默认）| 标量 | 最大值 2159
  group: 中心天体
  block_parameter: shDegree
  type: 字符向量
  values: '''80'' | 标量'
- name: Use Earth orientation parameters (EOPs)
  summary: 使用地球定向参数的选项 on（默认）| off
  group: 中心天体
  block_parameter: useEOPs
  type: 字符向量
  values: '''on'' | ''off'''
- name: IERS EOP data file
  summary: 地球定向数据 aeroiersdata.mat（默认）| MAT 文件
  group: 中心天体
  block_parameter: eopFile
  type: 字符向量
  values: '''aeroiersdata.mat'' | MAT-file'
- name: Input Moon libration angles
  summary: 月球天平动欧拉角速率 off（默认）| on
  group: 中心天体
  block_parameter: useMoonLib
  type: 字符向量
  values: '''off'' | ''on'''
- name: Output quaternion (ICRF to Fixed-frame)
  summary: 添加输出变换四元数端口的选项 off（默认）| on
  group: 中心天体
  block_parameter: outputTransform
  type: 字符向量
  values: '''off'' | ''on'''
- name: Central body spin axis source
  summary: 中心天体自旋轴来源 Port（默认）| Dialog
  group: 中心天体
  block_parameter: cbPoleSrc
  type: 字符向量
  values: '''Port'' | ''Dialog'''
- name: Spin axis right ascension (RA) at J2000
  summary: J2000 时中心天体自旋轴的赤经 317.68143（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbRA
  type: 字符向量
  values: '''317.68143'' | 双精度标量'
- name: Spin axis RA rate (deg/century)
  summary: 中心天体自旋轴的赤经速率 -0.1061（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbRARate
  type: 字符向量
  values: '''-0.1061'' | 双精度标量'
- name: Spin axis declination (Dec) at J2000
  summary: J2000 时中心天体自旋轴的赤纬 52.88650（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbDec
  type: 字符向量
  values: '''52.88650'' | 双精度标量'
- name: Spin axis Dec rate (deg/century)
  summary: 中心天体自旋轴的赤纬速率 -0.0609（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbDecRate
  type: 字符向量
  values: '''-0.0609'' | 双精度标量'
- name: Initial rotation angle at J2000
  summary: 中心天体 *x* 轴的旋转角 176.630（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbRotAngle
  type: 字符向量
  values: '''176.630'' | 双精度标量'
- name: Rotation rate (deg/day)
  summary: 中心天体 *x* 轴的旋转速率 350.89198226（默认）| 双精度标量
  group: 中心天体
  block_parameter: cbRotRate
  type: 字符向量
  values: '''350.89198226'' | 双精度标量'
- name: Equatorial radius
  summary: 赤道半径 3.3962e6（默认）| 双精度标量
  group: 中心天体
  block_parameter: customR
  type: 字符向量
  values: '''3.3962e6'' | 双精度标量'
- name: Flattening
  summary: 行星扁率 0.00589（默认）| 双精度标量
  group: 中心天体
  block_parameter: customF
  type: 字符向量
  values: '''0.00589'' | 双精度标量'
- name: Gravitational parameter
  summary: 引力参数 4.305e13（默认）| 双精度标量
  group: 中心天体
  block_parameter: customMu
  type: 字符向量
  values: '''4.305e13'' | 双精度标量'
- name: Second degree zonal harmonic (J2)
  summary: 最显著或最大的球谐项 1.0826269e-03（默认）| 双精度标量
  group: 中心天体
  block_parameter: customJ2
  type: 字符向量
  values: '''1.0826269e-03'' | 双精度标量'
- name: Include atmospheric drag
  summary: 包含大气阻力的选项 off（默认）| on
  group: Drag
  block_parameter: useDrag
  type: 字符向量
  values: '''off'' | ''on'''
- name: Atmospheric density source
  summary: 大气密度值的来源 Dialog（默认）| Port
  group: Drag
  block_parameter: atmosSrc
  type: 字符向量
  values: '''Dialog'' | ''Port'''
- name: Atmospheric model
  summary: 大气模型 NRLMSISE-00（默认）
  group: Drag
  block_parameter: atmosModel
  type: 字符向量
  values: '''NRLMSISE-00'''
- name: Flux source
  summary: 空间天气数据的来源 Dialog（默认）| Port
  group: Drag
  block_parameter: fluxSrc
  type: 字符向量
  values: '''Dialog'' | ''Port'''
- name: Space weather data file
  summary: 空间天气数据的 MAT 文件 aeroSpaceWeatherData.mat（默认）| MAT 文件名
  group: Drag
  block_parameter: SpaceWeatherDataFile
  type: 字符向量
  values: '''aeroSpaceWeatherData.mat'' | MAT 文件名'
- name: F10.7 extrapolation method
  summary: f107Average 和 f107Daily 的外推方法 None - clip（默认）| Constant | Least squares fit
  group: Drag
  block_parameter: F107ExtrapMethod
  type: 字符向量
  values: '''None - clip'' | ''Constant'' | ''Least squares fit'''
- name: Magnetic index extrapolation method
  summary: 磁指数信息的外推方法 None - clip（默认）| Constant | IGRF
  group: Drag
  block_parameter: MagneticIndexExtrapMethod
  type: 字符向量
  values: '''None - clip'' | ''Constant'' | ''IGRF'''
  default: '''None - clip'''
- name: Flags source
  summary: 变化标志源 Dialog（默认）| Port
  group: Drag
  block_parameter: fluxFlagsSrc
  type: 字符向量
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: Flags
  summary: 变化标志 ones(1,23)（默认）
  group: Drag
  block_parameter: fluxFlags
  type: 字符向量
  values: '''ones(1,23)'''
  default: '''ones(1,23)'''
- name: Include anomalous oxygen in density calculation
  summary: 在密度计算中包含异常氧的选项 off（默认）| on
  group: Drag
  block_parameter: useOxygen
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Drag coefficient source
  summary: 阻力系数来源 Dialog（默认）| Port
  group: Drag
  block_parameter: dragCoeffSrc
  type: 字符向量
  values: '''Dialog'' | ''Source'''
  default: '''Dialog'''
- name: Drag coefficient
  summary: 航天器阻力系数 2.179（默认）| 标量 | 大小为 *numSat* 的向量
  group: Drag
  block_parameter: dragCoeff
  type: 字符向量
  values: 标量 | 大小为 *numSat* 的向量
  default: '''2.179'''
- name: Drag area source
  summary: 阻力面积来源 Dialog（默认）| Port
  group: Drag
  block_parameter: dragAreaSrc
  type: 字符向量
  values: '''Dialog'' | ''Source'''
  default: '''Dialog'''
- name: Drag area
  summary: 用于计算大气阻力加速度的面积 1.0（默认）| 标量 | 大小为 *numSat* 的向量
  group: Drag
  block_parameter: dragArea
  type: 字符向量
  values: 标量 | 大小为 *numSat* 的向量
  default: '''1.0'''
- name: Ephemeris model
  summary: 星历模型 DE405（默认）| DE421 | DE423 | DE430 | DE432t
  group: Third Body
  block_parameter: ephemerisModel
  type: 字符向量
  values: DE405 | DE421 | DE423 | DE430
  default: '''DE405'''
- name: Limit ephemerides date range
  summary: 启用星历数据范围起始和结束的选项 off（默认）| on
  group: Third Body
  block_parameter: useDateRange
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Start date (JD)
  summary: 星历日期范围的起始日期 juliandate(2020, 1, 1)（默认）| 儒略日
  group: Third Body
  block_parameter: startDate
  type: 字符向量
  values: '''juliandate(2020, 1, 1)'' | 儒略日'
  default: '''juliandate(2020, 1, 1)'''
- name: End date (JD)
  summary: 星历日期范围的结束日期 juliandate(2050, 1, 1)（默认）| 儒略日
  group: Third Body
  block_parameter: endDate
  type: 字符向量
  values: '''juliandate(2050, 1, 1)'' | 儒略格式日期'
  default: '''juliandate(2050, 1, 1)'''
- name: Include third body gravity
  summary: 第三体引力引起的加速度 off（默认）| on
  group: Third Body
  block_parameter: useThirdBodyGravity
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Sun
  summary: 包含太阳引起的引力加速度 on（默认）| off
  group: Third Body
  block_parameter: includeSunGravity
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''on'''
- name: Sun gravity model
  summary: 太阳的第三体引力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: sunThirdBodyGravityModel
  type: 字符向量
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Mercury
  summary: 包含水星引起的引力加速度 off（默认）| on
  group: Third Body
  block_parameter: includeMercuryGravity
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Mercury gravity model
  summary: 水星引力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: mercuryThirdBodyGravityModel
  type: 字符向量
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Venus
  summary: 包含金星引起的引力加速度 off（默认）| on
  group: Third Body
  block_parameter: includeVenusGravity
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Venus gravity model
  summary: 金星引力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: venusThirdBodyGravityModel
  type: 字符向量
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Earth
  summary: 包含地球引起的引力加速度 on（默认）| off
  group: Third Body
  block_parameter: includeEarthGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 地球重力模型
  summary: 地球重力模型 Point-mass（默认）| Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: earthThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Moon
  summary: Include gravitational acceleration due to Moon on (default) | off
  group: Third Body
  block_parameter: includeMoonGravity
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''on'''
- name: 月球重力模型
  summary: 月球重力模型 Point-mass（默认）| Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: moonThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Mars
  summary: Include gravitational acceleration due to Mars off (default) | on
  group: Third Body
  block_parameter: includeMarsGravity
  type: character vector
  values: '''off'' | ''on'' |'
  default: '''off'''
- name: 火星重力模型
  summary: 火星重力模型 Point-mass（默认）| Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: marsThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'' | ''Spherical harmonics'''
  default: '''Point-mass'''
- name: Jupiter
  summary: Include gravitational acceleration due to Jupiter off (default) | on
  group: Third Body
  block_parameter: includeJupiterGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 木星重力模型
  summary: 木星重力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: jupiterThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Saturn
  summary: Include gravitational acceleration due to Saturn off (default) | on
  group: Third Body
  block_parameter: includeSaturnGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 土星重力模型
  summary: 土星重力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: saturnThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Uranus
  summary: Include gravitational acceleration due to Uranus off (default) | on
  group: Third Body
  block_parameter: includeUranusGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 天王星重力模型
  summary: 天王星重力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: uranusThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Neptune
  summary: Include gravitational acceleration due to Neptune off (default) | on
  group: Third Body
  block_parameter: includeNeptuneGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 海王星重力模型
  summary: 海王星重力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: neptuneThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Pluto
  summary: Include gravitational acceleration due to Pluto off (default) | on
  group: Third Body
  block_parameter: includePlutoGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 冥王星重力模型
  summary: 冥王星重力模型 Point-mass（默认）| Oblate ellipsoid (J2)
  group: Third Body
  block_parameter: plutoThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: Custom
  summary: Include gravitational acceleration due to custom planet off (default) | on
  group: Third Body
  block_parameter: includeCustomGravity
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: 自定义重力模型
  summary: 自定义重力模型 Point-mass（默认）| Oblate ellipsoid (J2) | Spherical harmonics
  group: Third Body
  block_parameter: customThirdBodyGravityModel
  type: character vector
  values: '''Point-mass'' | ''Oblate ellipsoid (J2)'''
  default: '''Point-mass'''
- name: 引力参数 (m^3/s^2)
  summary: 自定义引力加速度 42.828314258067e12（默认）| 标量 | 长度为 *numCustom3rdBodies* 的向量
  group: Third Body
  block_parameter: customThirdBodyMu
  type: character vector
  values: '''42.828314258067e12'' | scalar | vector of length *numCustom3rdBodies*'
  default: '''42.828314258067e12'''
- name: Include solar radiation pressure (SRP)
  summary: Acceleration due to solar radiation pressure off (default) | on
  group: SRP
  block_parameter: useSRP
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Eclipse fraction source
  summary: Source of eclipse fraction Dialog (default) | Port
  group: SRP
  block_parameter: useSRP
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: 阴影模型
  summary: 阴影模型 Dual cone（默认）| Cylindrical
  group: SRP
  block_parameter: shadowModel
  type: character vector
  values: '''Dual cone'' | ''Cylindrical'''
  default: '''Dual cone'''
- name: Include Earth
  summary: Option to include Earth on (default) | off
  group: SRP
  block_parameter: includeEarth
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Include Moon
  summary: Option to include Moon on (default) | off
  group: SRP
  block_parameter: includeMoon
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: 反射率系数来源
  summary: 航天器反射率系数的来源 'Dialog'（默认）| 'Port'
  group: SRP
  block_parameter: reflectivityCoeffSrc
  type: character vector
  values: '''Dialog'' | ''Port'''
  default: '''on'''
- name: Reflectivity coefficient
  summary: Spacecraft coefficient of reflectivity 1.8 (default) | scalar | 2D array of size *numSat* | between [1,2]
  group: SRP
  block_parameter: reflectivityCoeff
  type: character vector
  values: '''1.8'' | scalar | 2D array of size *numSat* | between [1,2]'
  default: '''1.8'''
- name: SRP 面积来源
  summary: 航天器太阳辐射压力面积的来源 Dialog（默认）| Port
  group: SRP
  block_parameter: srpAreaSrc
  type: 字符向量
  values: '''Dialog'' | ''Port'''
  default: '''Dialog'''
- name: SRP area
  summary: 航天器被太阳照射的横截面积 1.0（默认值）| 标量 | 大小为 *numSat* 的二维数组
  group: SRP
  block_parameter: srpArea
  type: 字符向量
  values: '''1.0'' | 标量 | 大小为 *numSat* 的二维数组'
  default: '''1.0'''
- name: Solar flux pressure (W\*s/m^3)
  summary: 航天器太阳通量压力 4.5344321e-6（默认值）| 标量
  group: SRP
  block_parameter: fluxPressure
  type: 字符向量
  values: 4.5344321e-6 | 标量
  default: '''4.5344321e-6'''
- name: Units
  summary: 参数和端口单位 Metric (m/s)（默认值）| Metric (km/s) | Metric (km/h) | English (ft/s) | English (kts)
  group: 单位
  block_parameter: units
  type: 字符向量
  values: '''Metric (m/s)'' | ''Metric (km/s)'' | ''Metric (km/h)'' | ''English (ft/s)'' | ''English (kts)'''
  default: '''Metric (m/s)'''
- name: Angle units
  summary: 角度单位 Degrees（默认值）| Radians
  group: 单位
  block_parameter: angleUnits
  type: 字符向量
  values: '''Degrees'' | ''Radians'''
  default: '''Degrees'''
- name: Time format
  summary: 起始日期和时间输出的时间格式 Julian date（默认值）| Gregorian
  group: 单位
  block_parameter: timeFormat
  type: 字符向量
  values: '''Julian date'' | ''Gregorian'''
  default: '''Julian date'''
```

### 主要

### **Input body forces** — 启用外部力的选项 on（默认）| off

要启用外部力以包含在体坐标系中航天器运动方程的积分中，请选择此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `forcesin` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Input body moments** — 启用外部力矩的选项 on（默认）| off

要启用外部力矩以包含在体坐标系中航天器运动方程的积分中，请选择此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `momentsIn` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Input external accelerations** — 输入附加力加速度的选项 off（默认）| on

要启用附加外部加速度以包含在航天器运动方程的积分中，请选择此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `accelIn` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **External acceleration coordinate frame** — 加速度输入端口坐标系 `ICRF`（默认）| `Fixed-frame`

加速度输入端口 **A** 的坐标系，指定为 `ICRF` 或 `Fixed-frame`。

#### 依赖关系

要启用此参数，请将 **Input external accelerations** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `accelFrame` |
| **类型：** 字符向量 |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认：** `'ICRF'` |

### **State vector output coordinate frame** — 位置和速度状态输出端口坐标系 `ICRF`（默认）| `Fixed-frame`

位置和速度状态输出端口坐标系设置，指定为 `ICRF` 或 `Fixed-frame`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outportFrame` |
| **类型：** 字符向量 |
| **值：** `'ICRF'` | `'Fixed-frame'` |
| **默认：** `'ICRF'` |

### **Output total inertial acceleration** — 启用总加速度端口的选项 off（默认）| on

启用模块计算的相对于 ICRF 或固定坐标系输出端口坐标系的总加速度输出。此加速度包括作用在航天器上的所有外部加速度、力和内部环境加速度。

**注意**

不要将此端口用作仿真环路的一部分（换句话说，不要将此输出反馈到模块中）。

**可调：** 是

#### 依赖关系

要更改此端口的输出坐标系，请设置 **State vector output coordinate frame** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `AccelOut` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Start date/time (UTC Julian date)** — 仿真的初始开始时间 `juliandate (2020, 1, 1, 12, 0, 0)`（默认）| 有效的标量儒略日 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，作为一维或六元素数组

仿真的初始开始日期和时间，指定为儒略日或格里高利日期。模块使用此值定义初始条件。

**提示**

要计算儒略日，请使用 `juliandate` 函数。

**可调：** 是

#### 依赖关系

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **模块参数：** `startDate` |
| **类型：** 字符向量 |
| **值：** `'juliandate(2020, 1, 1, 12, 0, 0)'` | 有效的标量儒略日 | 有效的格里高利日期，包括年、月、日、小时、分钟、秒，作为一维或六元素数组 |
| **默认：** `'juliandate(2020, 1, 1, 12, 0, 0)'` |

### **Output current date/time (UTC Julian date)** — 添加输出端口 tutc 的选项 on（默认）| off

要输出当前日期或时间，请选择此参数。否则，清除此参数。

#### 依赖关系

此参数的数据格式由 **Time format** 参数控制。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dateOut` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `Warning`（默认）| `Error` | `None`

超出范围时的模块行为操作。指定以下选项之一。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中发出警告，模型仿真继续。 |
| `Error`（默认） | 在诊断查看器中报错，模型仿真停止。 |

#### 程序化使用

|  |
| --- |
| **模块参数**： `action` |
| **类型**： 字符向量 |
| **值**： `'None'` | `'Warning'` | `'Error'` |
| **默认**： `'Warning'` |

### 质量

### **Mass type** — 航天器质量类型 `Fixed`（默认）| `Simple Variable` | `Custom Variable`

航天器质量类型，指定为：

- `Fixed` — 质量和惯量在整个仿真过程中恒定。
- `Simple Variable` — 质量和惯量作为质量变化率的线性函数变化。
- `Custom Variable` — 瞬时质量、惯量和惯量变化率是模块的输入。

#### 程序化使用

|  |
| --- |
| **模块参数**： `massType` |
| **类型**： 字符向量 |
| **值**： `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认**： `'Fixed'` |

### **Mass** — 刚体航天器的初始质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

刚体航天器的初始质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 参数设置为 **Fixed** 或 **Simple variable**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass` |
| **类型：** 字符向量 |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认：** `'4.0'` |

### **Empty mass** — 航天器空载质量 `3.5`（默认）| 标量 | 大小为 *numSat* 的向量

航天器空载（干）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `emptyMass` |
| **类型：** 字符向量 |
| **值：** 大小为 *numSat* 的一维数组 | 大小为 *numSat* 的一维数组 |
| **默认：** `'3.5'` |

### **Full mass** — 航天器满载质量 4.0（默认）| 标量 | 大小为 *numSat* 的向量

航天器满载（湿）质量，指定为标量或大小为 *numSat* 的向量。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fullMass` |
| **类型：** 字符向量 |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认：** `'4.0'` |

### **Inertia tensor** — 惯量张量矩阵 `[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]`（默认）| 3×3 数组 | 3×3×*numSat* 数组

航天器的初始惯量张量矩阵，对于单个航天器指定为 3×3 数组，对于多个航天器指定为 3×3×*numSat* 数组。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** 字符向量 |
| **值：** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` | 3×3 数组 | 3×3×*numSat* 数组 |
| **默认：** `'[0.2273, 0, 0; 0 0.2273 0; 0 0 .0040]'` |

### **Empty inertia tensor** — 空载惯量张量矩阵 `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]`（默认）| 3×3 数组 | 3×3×*numSat* 数组

空载（干）惯量张量矩阵，对于单个航天器指定为 3×3 数组，对于多个航天器指定为 3×3×*numSat* 数组。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `emptyInertia` |
| **类型：** 字符向量 |
| **值：** 3×3 数组 | 3×3×*numSat* 数组 |
| **默认：** `[0.1989, 0, 0; 0 0.1989 0; 0 0 .0035]` |

### **Full inertia tensor** — 满载惯量张量矩阵 `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]`（默认）| 3×3 数组 | 3×3×*numSat* 数组

满载（湿）惯量张量矩阵，对于单个航天器指定为 3×3 数组，对于多个航天器指定为 3×3×*numSat* 数组。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fullInertia` |
| **类型：** 字符向量 |
| **值：** 3×3 数组 | 3×3×*numSat* 数组 |
| **默认：** `[0.2273, 0, 0; 0, 0.2273, 0; 0, 0, .0040]` |

### **Include mass flow relative velocity** — 启用质量流速度的选项 off（默认）| on

要启用质量流速度到模块，请选择此参数。质量流速度是质量在体坐标系中被积聚或烧蚀时的相对速度。要禁用质量流速度到模块，请清除此参数。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable` 或 `Custom variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useMassFlowRelativeVelocity` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Limit mass flow when mass is empty or full** — 限制质量流的选项 on（默认）| off

要在航天器质量已满或已空时限制质量流，请选择此参数。否则，清除此参数。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `limitMassFlow` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **Output fuel tank status** — 启用燃料箱状态的选项 on（默认）| off

要启用燃料箱状态，请选择此参数。否则，清除此参数。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Simple variable`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outputFuelStatus` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### 轨道

定义航天器的初始状态。

### **Initial state format** — 轨道初始状态的输入方法 `Orbital elements`（默认）| `ICRF state vector` | `Fixed-frame state vector`

轨道初始状态的输入方法，指定为 `Orbital elements`、`ICRF state vector` 或 `Fixed-frame state vector`。

#### 程序化使用

|  |
| --- |
| **模块参数** `stateFormatNum`，当 `propagator` 设置为 `High precision (numerical)` 时 |
| **类型：** 字符向量 |
| **值：** `'Orbital elements'` | `'Orbital elements'` | `'ICRF state vector'` | `'Fixed-frame state'`，当 `propagator` 设置为 `'High precision (numerical)'` 时 |
| **默认：** `'Orbital elements'` |

### **Orbit type** — 轨道分类 `Keplerian`（默认）| `Elliptical equatorial` | `Circular` | `Circular equatorial`

轨道分类，指定为：

- `Keplerian` — 使用六个标准开普勒轨道元素对椭圆、抛物线和双曲线轨道进行建模。
- `Elliptical equatorial` — 完全定义赤道轨道，其中倾角为 0 或 180 度，升交点赤经未定义。
- `Circular` — 定义圆轨道，其中偏心率为 0，近地点幅角未定义。要完全定义圆轨道，请选择 `Circular equatorial`。
- `Circular equatorial` — 完全定义圆轨道，其中偏心率为 0，近地点幅角未定义。

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `orbitType` |
| **类型：** 字符向量 |
| **值：** `'Keplerian'` | `'Elliptical equatorial'` | `'Circular inclined'` | `'Circular equatorial'` |
| **默认：** `'Keplerian'` |

### **Semi-major axis** — 椭圆长轴的一半 6786000（默认）| 标量 | 大小为 *numSat* 的一维数组

椭圆长轴的一半，指定为大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

- 对于抛物线轨道，此模块将此参数解释为近地点半径（从近地点到轨道焦点的距离）。
- 对于双曲线轨道，此模块将此参数解释为从近地点到双曲线中心的距离。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Initial state format** 设置为 `Orbital elements`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `semiMajorAxis` |
| **类型：** 字符向量 |
| **值：** 标量 | 大小为 *numSat* 的一维数组 |
| **默认：** `'6786000'` |

### **Eccentricity** — 轨道偏离度 0.01（默认）| 标量 | `0` 到 `1` 之间的值，或对于 Keplerian 轨道类型大于 `1` | 大小为 *numSat* 的一维数组

轨道偏离完美圆的程度，指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

如果 **Orbit** 类型设置为 `Keplerian`，此值可以是：

- `1` 表示抛物线轨道
- 大于 `1` 表示双曲线轨道

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`。
- 将 **Orbit type** 设置为 `Keplerian` 或 `Elliptical equatorial`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eccentricity` |
| **类型：** 字符向量 |
| **值：** `0.01` | 标量 | `0` 到 `1` 之间的值，或对于 Keplerian 轨道类型大于 `1` | 大小为 *numSat* 的一维数组 |
| **默认：** `'0.01'` |

### **Inclination** — 轨道平面的倾斜角 50（默认）| 标量 | 大小为 *numSat* 的一维数组 | 0 到 180 度 | 0 到 pi 弧度

在升交点处测量的椭圆相对于参考平面的垂直倾斜角，以指定单位指定为标量或大小为 *numSat* 的一维数组。*numSat* 是航天器数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital elements`
- 将 **Orbit type** 设置为 `Keplerian` 或 `Circular inclined`

#### 程序化使用

|  |
| --- |
| **模块参数：** `inclination` |
| **类型：** 字符向量 |
| **值：** 50 | 标量 | 大小为 *numSat* 的一维数组 | 0 到 180 度 | 0 到 pi 弧度 |
| **默认：** `'50'` |

### **RAAN** — 赤道面内的角距离 95（默认）| `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组

升交点赤经（RAAN），指定为 `0` 到 `360` 之间的值，指定为标量或大小为 *numSat* 的一维数组，使用指定的单位。*numSat* 是航天器的数量。RAAN 是沿参考平面从国际天球参考框架（ICRF）*x* 轴到升交点位置的角距离——升交点是航天器从南向北穿过参考平面的点。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`。
- 将 **Orbit type** 设置为 `Keplerian`
  或 `Circular inclined`。

#### 编程使用

|  |
| --- |
| **模块参数：** `raan` |
| **类型：** 字符向量 |
| **值：** `'95'` | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 |
| **默认：** `'95'` |

### **Argument of periapsis** — 从航天器升交点到近拱点的角度 93（默认）| `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

从航天器升交点到近拱点（轨道上距中心天体最近的点）的角度，指定为大小为 *numSat* 的一维数组，使用指定的单位。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`
- 将 **Orbit type** 设置为
  `Keplerian`

#### 编程使用

|  |
| --- |
| **模块参数：** `argPeriapsis` |
| **类型：** 字符向量 |
| **值：** 93 | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 |
| **默认：** `'93'` |

### **True anomaly** — 近拱点与航天器初始位置之间的角度 203（默认）| `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组

在 **Start date/time** 时，近拱点（轨道上距中心天体最近的点）与航天器沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组，使用指定的单位。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`。
- 将 **Orbit type** 设置为 `Keplerian`
  或 `Elliptical inclined`。

#### 编程使用

|  |
| --- |
| **模块参数：** `trueAnomaly` |
| **类型：** 字符向量 |
| **值：** `'203'` | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 |
| **默认：** `'203'` |

### **Argument of latitude** — 升交点与航天器初始位置之间的角度 200（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

在 **Start date/time** 时，升交点与航天器沿其轨道的初始位置之间的角度，指定为标量或 3 元素向量或大小为 *numSat* 的一维数组，使用指定的单位。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`。
- 将 **Orbit Type** 设置为 `Circular
  inclined`。

#### 编程使用

|  |
| --- |
| **模块参数：** `argLat` |
| **类型：** 字符向量 |
| **值：** `'200'` | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 |
| **默认：** `'200'` |

### **Longitude of periapsis** — ICRF *x* 轴与偏心率向量之间的角度 100（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组

ICRF *x* 轴与偏心率向量之间的角度，指定为标量或 3 元素向量或大小为 *numSat* 的一维数组，使用指定的单位。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`。
- 将 **Orbit type** 设置为 `Elliptical
  equatorial`。

#### 编程使用

|  |
| --- |
| **模块参数：** `lonPeriapsis` |
| **类型：** 字符向量 |
| **值：** 100 | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 |
| **默认：** `'100'` |

### **True longitude** — ICRF *x* 轴与航天器初始位置之间的角度 150（默认）| 标量 | `0` 到 `360` 之间的值 | 大小为 *numSat* 的一维数组 | *numSat*×3 向量

在 **Start date/time** 时，ICRF *x* 轴与航天器沿其轨道的初始位置之间的角度，指定为标量或大小为 *numSat* 的一维数组或 *numSat*×3 向量，使用指定的单位。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Initial state format** 设置为 `Orbital
  elements`。
- 将 **Orbit type** 设置为 `Circular
  equatorial`。

#### 编程使用

|  |
| --- |
| **模块参数：** `trueLon` |
| **类型：** 字符向量 |
| **值：** `'150'` | `0` 到 `360` 之间的标量值 | 大小为 *numSat* 的一维数组 | *numSat*×3 向量 |
| **默认：** `'150'` |

### **ICRF position** — 航天器的笛卡尔位置向量 `[3649700.0 3308200.0 -4676600.0]`（默认）| 3 元素向量 | | *numSat*×3 数组

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔位置向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为 *numSat*×3 数组。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Initial state format** 设置为
`ICRF state vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `inertialPosition` |
| **类型：** 字符向量 |
| **值：** `[3649700.0 3308200.0 -4676600.0]` | 3 元素向量 | *numSat*×3 数组 |
| **默认：** `'[3649700.0 3308200.0 -4676600.0]'` |

### **ICRF velocity** — 航天器的笛卡尔速度向量 `[-2750.8 6666.4 2573.4]`（默认）| 3 元素向量 | *numSat*×3 数组

在 **Start date/time** 时，航天器在 ICRF 坐标系中的笛卡尔速度向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为 *numSat*×3 数组。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Initial state format** 设置为
`ICRF state vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `inertialVelocity` |
| **类型：** 字符向量 |
| **值：** `[-2750.8 6666.4 2573.4]` | 3 元素向量 | 大小为 *numSat*×3 数组的二维数组 |
| **默认：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame position** — 航天器的位置向量 [-4142689.0 -2676864.7 -4669861.6]（默认）| 3 元素向量 | *numSat*×3 数组

在 **Start date/time** 时，航天器在固定坐标系中的笛卡尔位置向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为 *numSat*×3 数组。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Initial state format** 设置为
`Fixed-frame state vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `fixedPosition` |
| **类型：** 字符向量 |
| **值：** `'[-4142689.0 -2676864.7 -4669861.6]'` | 单个航天器的 3 元素向量 | *numSat*×3 数组 |
| **默认：** `'[-2750.8 6666.4 2573.4]'` |

### **Fixed-frame velocity** — 航天器的速度向量 [1452.7 -6720.7 2568.1]（默认）| 3 元素向量 | *numSat*×3 数组

在 **Start date/time** 时，航天器在固定坐标系中的笛卡尔速度向量，对于单个航天器指定为 3 元素向量，对于多个航天器指定为 *numSat*×3 数组。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Initial state format** 设置为
`Fixed-frame state vector`。

#### 编程使用

|  |
| --- |
| **模块参数：** `fixedVelocity` |
| **类型：** 字符向量 |
| **值：** `'[1452.7 -6720.7 2568.1]'` | 3 元素向量 | *numSat*×3 数组 |
| **默认：** `'[1452.7 -6720.7 2568.1]'` |

### 姿态

### **Attitude reference coordinate frame** — 姿态和角速率坐标系 `ICRF`（默认）| `Fixed-frame` | `NED` | `LVLH`

相对于姿态和角速率初始条件的姿态和角速率坐标系，指定为：

- `ICRF`
- `Fixed-frame`
- `NED`
- `LVLH`

#### 编程使用

|  |
| --- |
| **模块参数：** `attitudeFrame` |
| **类型：** 字符向量 |
| **值：** `'ICRF'` | `'Fixed-frame'` | `'NED'` | `'LVLH'` |
| **默认：** `'ICRF'` |

### **Attitude representation** — 方向格式 `Quaternion`（默认）| `DCM` | `Euler angles`

航天器姿态（初始条件和输出端口）的方向格式，指定为 `Quaternion`、`DCM` 或
`Euler angles`。

#### 编程使用

|  |
| --- |
| **模块参数：** `attitudeFrame` |
| **类型：** 字符向量 |
| **值：** `'Quaternion'` | `'DCM'` | `'Euler angles'` |
| **默认：** `'Quaternion'` |

### **Initial body attitude** — 航天器初始姿态 `[1, 0, 0, 0]`（默认）| 4 元素向量 | *numSat*×4 数组 | 3×3 数组 | *numSat*×3×3 数组

航天器的初始姿态（方向），以四元数、DCM 或欧拉角集的形式提供，相对于 **Attitude
representation**。

**可调：** 是

#### 依赖关系

此参数名称和值格式根据 **Attitude
representation** 参数而变化。

| 参数名称 | 姿态表示设置 | 值格式 |
| --- | --- | --- |
| **Initial quaternion** | `Quaternion` | - 4 元素向量 - *numSat*×4 数组 |
| **Initial DCM** | `DCM` | - 3×3 数组 - *numSat*×3×3 数组 |
| **Initial Euler angles** | `Euler angles` | - 3 元素向量 - *numSat*×3 数组 |

#### 编程使用

|  |
| --- |
| **模块参数：** `attitude` |
| **类型：** 字符向量 |
| **值：** 4 元素向量 | *numSat*×4 数组 | 3×3 数组 | *numSat*×3×3 数组 | 3 元素数组 | *numSat*×3 数组 |
| **默认：** `'[1, 0, 0, 0]'` |

### **Angle rotation order** — 角度旋转顺序 `ZYX`（默认）| `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

欧拉角姿态表示的旋转角度序列。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Attitude representation** 设置为
`Euler angles`。

#### 编程使用

|  |
| --- |
| **模块参数**： `rotationOrder` |
| **类型**： 字符向量 |
| **值**： `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认**： `'ZYX'` |

### **Initial body angular rates PQR** — 初始体坐标系角速率 `[0, 0, 0]`（默认）| 3 元素向量 | *numSat*×3 数组

相对于 **Attitude
reference coordinate frame** 的初始体坐标系角速率（PQR）。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `attitudeRate` |
| **类型：** 字符向量 |
| **值：** | 3 元素向量 | *numSat*×3 数组 |
| **默认：** `[0, 0, 0]` |

### **Output total inertial angular acceleration** — 启用总飞行器加速度输出的选项 off（默认）| on

启用模块计算的相对于 ICRF 姿态参考坐标系的总飞行器加速度输出。此加速度包括作用在航天器上的所有力矩。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `angAccelOut` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'off'` |

### **Include gravity gradient torque** — 启用重力梯度力矩的选项 on（默认）| off

选择此参数以在模块旋转动力学方程中启用重力梯度力矩。否则，清除此参数。

**可调：** 是

#### 编程使用

|  |
| --- |
| **模块参数：** `angAccelOut` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### 中心天体

### **Central body** — 航天器环绕的天体 `Earth`（默认）| `Moon` | `Mercury` | `Venus` | `Mars` | `Jupiter` | `Saturn` | `Uranus` | `Neptune` | `Sun` | `Custom`

天体，指定为 `Earth`、
`Moon`、`Mercury`、
`Venus`、`Mars`、
`Jupiter`、`Saturn`、
`Uranus`、`Neptune`、
`Sun` 或 `Custom`，**Orbit** 选项卡中定义的航天器环绕该天体运行。

#### 编程使用

|  |
| --- |
| **模块参数：** `centralBody` |
| **类型：** 字符向量 |
| **值：** `'Earth'` | `'Moon'` |`'Mercury'` | `'Venus'` | `'Mars'` | `'Jupiter'` | `'Saturn'` | `'Uranus'` | `'Neptune'` | `'Sun'` | `'Custom'` | |
| **默认：** `'Earth'` |

### **Gravitational potential model** — 中心天体的重力模型 当 **Central body** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom` 时为 `Spherical harmonics`，当 **Central body** 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 `Oblate ellipsoid`（默认）| `Point-mass` | `Oblate ellipsoid (J2)`

通过指定为 `Spherical harmonics`、
`Point-mass` 或 `Oblate ellipsoid
(J2)` 来控制中心天体的重力模型。

#### 依赖关系

可用选项基于 **Central body**
设置。

| Earth、Moon、Mars 或 Custom | Mercury、Venus、Jupiter、Saturn、Uranus 或 Neptune |
| --- | --- |
| `Spherical harmonics` | `Oblate ellipsoid (J2)` |
| `Point-mass` | `Point-mass` |
| `Oblate ellipsoid (J2)` | — |

#### 编程使用

|  |
| --- |
| **模块参数：** 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时为 `gravityModel` | 当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 `gravityModelnoSH` |
| **类型：** 字符向量 |
| **值：** 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时为 `'Spherical harmonics'` | `'Point-mass'` | `'Oblate ellipsoid (J2)'`；当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 `'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认：** 当 `centralBody` 设置为 `'Earth'`、`'Moon'`、`'Mars'` 或 `'Custom'` 时为 `'Spherical harmonics'`；当 `centralBody` 设置为 `Mercury`、`Venus`、`Jupiter`、`Saturn`、`Uranus` 或 `Neptune` 时为 `'Oblate ellipsoid (J2)'` |

### **Spherical harmonic model** — 球谐模型 当 **Central body** 设置为 `Earth` 时为 `EGM2008`，当 **Central body** 设置为 `Moon` 时为 `LP-100K`，当 **Central body** 设置为 `Mars` 时为 `GMM2B`，（默认）| `EGM96` | `EIGEN-GL04C` | `LP-165P`

球谐重力势模型，根据指定的 **Central body** 指定。

#### 依赖关系

可用选项基于 **Central body**
设置：

| 中心天体 | 球谐模型选项 |
| --- | --- |
| Earth | EGM2008、EGM96 或 EIGEN-GL04C |
| Moon | LP-100K 或 LP-165P |
| Mars | GMM2B |

#### 编程使用

|  |
| --- |
| **模块参数：** 当 `centralBody` 设置为 `'Earth'` 时为 `'earthSH'` | 当 `centralBody` 设置为 `'Moon'` 时为 `'moonSH'` | 当 `centralBody` 设置为 `'Mars'` 时为 `'marsSH'` |
| **类型：** 字符向量 |
| **值：** 当 `centralBody` 设置为 `'earthSH'` 时为 `'EGM2008'` | `'EGM96'` | `'EIGEN-GL04C'`；当 `centralBody` 设置为 `'moonSH'` 时为 `'LP-100K'` | `'LP-165P'`；当 `centralBody` 设置为 `'marsSH'` 时为 `'GMM2B'` |
| **默认：** `'Spherical harmonics'` |

### **Rotational rate** — 旋转速率 4.06124975e-3（默认）| 标量

自定义中心天体的旋转速率，指定为标量。

#### 依赖关系

要启用此参数，将 **Central body** 设置为
`Custom`。

#### 编程使用

|  |
| --- |
| **模块参数：** `'customOmega'` |
| **类型：** 字符向量 |
| **值：** `'4.06124975e-3'` | 标量 |
| **默认：** `'4.06124975e-3'` |

### **Spherical harmonic coefficient file** — 谐波系数 MAT 文件 `aerogmm2b.mat`（默认）| 谐波系数 MAT 文件

包含自定义行星模型定义的谐波系数 MAT 文件，指定为字符向量或字符串。

此文件必须包含以下变量：

| 变量 | 描述 |
| --- | --- |
| *Re* | 行星赤道半径的标量，单位为米 (m)。 |
| *GM* | 行星引力参数的标量，单位为米的三次方每二次方秒 (m3/s2)。 |
| *degree* | 最大阶数的标量。 |
| *C* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *C*。 |
| *S* | (*degree*+1)×(*degree*+1) 矩阵，包含归一化球谐系数矩阵 *S*。 |

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `shFile` |
| **类型：** 字符向量 |
| **值：** `'aerogmm2b.mat'` | 谐波系数 MAT 文件 |
| **默认：** `'aerogmm2b.mat'` |

### **Degree** — 谐波模型的阶数 `120`（默认）| 标量 | 最大值 2159

谐波模型的阶数，指定为标量。

| 行星模型 | 推荐阶数 | 最大阶数 |
| --- | --- | --- |
| `EGM2008` | 120 | 2159 |
| `EGM96` | 70 | 360 |
| `LP100K` | 60 | 100 |
| `LP165P` | 60 | 165 |
| `GMM2B` | 60 | 80 |
| `EIGENGL04C` | 70 | 360 |

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Earth`、`Moon`、`Mars` 或 `Custom`。
- 将 **Gravitational potential model** 设置为 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `shDegree` |
| **类型：** 字符向量 |
| **值：** `'80'` | 标量 |
| **默认：** `'80'` |

### **Use Earth orientation parameters (EOPs)** — 使用地球定向参数的选项 on（默认）| off

选择此参数以使用地球定向参数进行 ICRF 与固定坐标系之间的变换。否则，清除此参数。

#### 依赖

要启用此参数，将 **Central body** 设置为 `Earth`。

此外，还必须满足以下条件之一：

- **Gravitational potential model** 设置为 `Spherical harmonics` 或 `Oblate ellipsoid (J2)`。
- **External acceleration coordinate frame** 设置为 `Fixed-frame`。
- **State vector output coordinate frame** 设置为 `Fixed-frame`。
- **Attitude reference coordinate frame** 设置为 `Fixed-frame` 或 `NED`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useEOPs` |
| **类型：** 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认：** `'on'` |

### **IERS EOP data file** — 地球定向数据 `aeroiersdata.mat`（默认）| MAT 文件

自定义的地球定向数据列表，在 MAT 文件中指定。

#### 依赖

要启用此参数：

- 将 **Use Earth orientation parameters (EOPs)** 参数设置为 `on`。
- 将 **Central body** 设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eopFile` |
| **类型：** 字符向量 |
| **值：** `'aeroiersdata.mat'` | `MAT-file` |
| **默认：** `'aeroiersdata.mat'` |

### **Input Moon libration angles** — 月球天平动欧拉角速率 off（默认）| on

要指定月球定向的欧拉天平动角 (φ θ ψ)，请选择此参数。

#### 依赖

要启用此参数，将 **Central body** 设置为 `Moon`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useMoonLib` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Output quaternion (ICRF to Fixed-frame)** — 添加输出变换四元数端口的选项 off（默认）| on

要添加从 ICRF 到固定坐标系的四元数变换的输出变换四元数端口，请选择此参数。否则，清除此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `outputTransform` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Central body spin axis source** — 中心天体自旋轴来源 `Port`（默认）| `Dialog`

中心天体自旋轴来源，指定为 `Port` 或 `Dialog`。模块使用自旋轴计算自定义中心天体从 ICRF 到固定坐标系的变换。

#### 依赖

要启用此参数，将 **Central body** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbPoleSrc` |
| **类型：** 字符向量 |
| **值：** `'Port'` | `'Dialog'` |
| **默认：** `'Port'` |

### **Spin axis right ascension (RA) at J2000** — J2000 时中心天体自旋轴的赤经 `317.68143`（默认）| 双精度标量

J2000（2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT）时中心天体自旋轴的赤经，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRA` |
| **类型：** 字符向量 |
| **值：** `'317.68143'` | 双精度标量 |
| **默认：** `'317.68143'` |

### **Spin axis RA rate (deg/century)** — 中心天体自旋轴的赤经速率 `-0.1061`（默认）| 双精度标量

中心天体自旋轴的赤经速率，指定为双精度标量，单位为指定的角度单位/世纪。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRARate` |
| **类型：** 字符向量 |
| **值：** `'-0.1061'` | 双精度标量 |
| **默认：** `'-0.1061'` |

### **Spin axis declination (Dec) at J2000** — J2000 时中心天体自旋轴的赤纬 `52.88650`（默认）| 双精度标量

J2000（2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT）时中心天体自旋轴的赤纬，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDec` |
| **类型：** 字符向量 |
| **值：** `'52.88650'` | 双精度标量 |
| **默认：** `'52.88650'` |

### **Spin axis Dec rate (deg/century)** — 中心天体自旋轴的赤纬速率 `-0.0609`（默认）| 双精度标量

中心天体自旋轴的赤纬速率，指定为双精度标量，单位为指定的角度单位/世纪。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbDecRate` |
| **类型：** 字符向量 |
| **值：** `'-0.0609'` | 双精度标量 |
| **默认：** `'-0.0609'` |

### **Initial rotation angle at J2000** — 中心天体 *x* 轴的旋转角 `176.630`（默认）| 双精度标量

J2000（2451545.0 JD，2000 年 1 月 1 日 12:00:00 TT）时中心天体 x 轴相对于 ICRF *x* 轴的旋转角，指定为双精度标量，单位为指定的角度单位。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotAngle` |
| **类型：** 字符向量 |
| **值：** `'176.630'` | 双精度标量 |
| **默认：** `'176.630'` |

### **Rotation rate (deg/day)** — 中心天体 *x* 轴的旋转速率 `350.89198226`（默认）| 双精度标量

中心天体 x 轴相对于 ICRF *x* 轴（2451545.0 JD，2000 年 1 月 1 日 12:00:00 UTC）的旋转速率，指定为双精度标量，单位为角度单位/天。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Central body spin axis source** 设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `cbRotRate` |
| **类型：** 字符向量 |
| **值：** `'350.89198226'` | 双精度标量 |
| **默认：** `'350.89198226'` |

### **Equatorial radius** — 赤道半径 `3.3962e6`（默认）| 双精度标量

自定义中心天体的赤道半径，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数，将 **Gravitational potential model** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customR` |
| **类型：** 字符向量 |
| **值：** `'3.3962e6'` | 双精度标量 |
| **默认：** `'3.3962e6'` |

### **Flattening** — 行星扁率 `0.00589`（默认）| 双精度标量

自定义中心天体的行星扁率，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Point-mass`、`Oblate ellipsoid (J2)` 或 `Spherical harmonics`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customF` |
| **类型：** 字符向量 |
| **值：** `'0.00589'` | 双精度标量 |
| **默认：** `'0.00589'` |

### **Gravitational parameter** — 引力参数 `4.305e13`（默认）| 双精度标量

自定义中心天体的引力参数，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `None`、`Point-mass` 或 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customMu` |
| **类型：** 字符向量 |
| **值：** `'4.305e13'` | 双精度标量 |
| **默认：** `'4.305e13'` |

### **Second degree zonal harmonic (J2)** — 最显著或最大的球谐项 `1.0826269e-03`（默认）| 双精度标量

最显著或最大的球谐项，用于表示天体的扁率，指定为双精度标量。

**可调：** 是

#### 依赖

要启用此参数：

- 将 **Central body** 设置为 `Custom`。
- 将 **Gravitational potential model** 设置为 `Oblate ellipsoid (J2)`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `customJ2` |
| **类型：** 字符向量 |
| **值：** `'1.0826269e-03'` | 双精度标量 |
| **默认：** `'1.0826269e-03'` |

### Drag

配置大气阻力环境。

### **Include atmospheric drag** — 包含大气阻力的选项 off（默认）| on

要包含大气阻力，请选中此复选框。

#### 依赖

要启用此参数，将 **Central Body** 参数设置为 `Earth`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `useDrag` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Atmospheric density source** — 大气密度值的来源 `Dialog`（默认）| `Port`

大气密度值的来源，指定为 `Dialog` 或 `Port`。

#### 依赖

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `atmosSrc` |
| **类型：** 字符向量 |
| **值：** `'Dialog'` | `'Port'` |
| **默认：** `'Dialog'` |

### **Atmospheric model** — 大气模型 `NRLMSISE-00`（默认）

用于大气阻力计算的大气模型，指定为 `NRLMSISE-00`。

#### 依赖

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `atmosModel` |
| **类型：** 字符向量 |
| **值：** `'NRLMSISE-00'` |
| **默认：** `'NRLMSISE-00'` |

### **Flux source** — 空间天气数据的来源 `Dialog`（默认）| `Port`

用于大气密度计算的历史和预测通量及地磁指数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `fluxSrc` |
| **类型：** 字符向量 |
| **值：** `'Dialog'` | `'Port'` |
| **默认：** `'Dialog'` |

### **Space weather data file** — 空间天气数据的 MAT 文件 `aeroSpaceWeatherData.mat`（默认）| MAT 文件名

空间天气数据的 MAT 文件。此文件是 `aeroReadSpaceWeatherData` 函数的输出。

Aerospace Blockset 包含默认的空间天气数据文件 `aeroSpaceWeatherData.mat`。要使用最新的可用数据，请使用 `aeroReadSpaceWeatherData` 生成新的 MAT 文件，并为该参数指定文件名。有关详细信息，请参阅 `aeroReadSpaceWeatherData`。

如果文件不在 MATLAB® 路径上，请指定完整路径名。MAT 文件必须包含空间天气数据文件中的以下变量：

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

#### 依赖

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `SpaceWeatherDataFile` |
| **类型**： 字符向量 |
| **值**： `'aeroSpaceWeatherData.mat'` | MAT 文件名 |
| **默认**： `'aeroSpaceWeatherData.mat'` |

### **F10.7 extrapolation method** — `f107Average` 和 `f107Daily` 的外推方法 `None - clip`（默认）| `Constant` | `Least squares fit`

`f107Average` 和 `f107Daily` 在 MAT 文件数据范围之外时间的外推方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将 `f107Average` 和 `f107Daily` 设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将 `f107Average` 和 `f107Daily` 设置为由 **Magnetic index extrapolation method** 参数值指定的常量值。 |
| `Least squares fit` | 使用 1957 年 10 月 1 日至 2040 年 12 月 1 日空间天气数据的最小二乘拟合来近似 `f107Average` 和 `f107Daily`。此方法使用以下形式的三角函数： `a + b*cos(c*t + d*sin(e*t))`，其中： - *a* 为 `128.2351780622538` - *b* 为 `54.3285872213434` - *c* 为 `0.0015460708364` - *d* 为 `0.2429462096495` - *e* 为 `0.0015563188188` - *t* 为 *jdCurrent* - *jdReftime* - *jdCurrent* 为当前儒略日 - *jdRef* 为 `2436112.5` |

**注意**

对于 `f107Average` 值，如果 81 天周期的一部分落在空间天气数据的 MAT 文件范围内，Solar Flux and Geomagnetic Index 模块使用重叠部分的实际每日值。对于非重叠部分，模块使用截断、常量或最小二乘每日值来计算平均值。

#### 依赖

要启用此参数：

- 将 **Central Body** 参数设置为 `Earth`。
- 将 **Include atmospheric drag** 参数设置为 `on`。
- 将 **Atmospheric density source** 参数设置为 `Dialog`。
- 将 **Atmospheric model** 设置为 `NRLMSISE-00`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `F107ExtrapMethod` |
| **类型**： 字符向量 |
| **值**： `'None - clip'` | `'Constant'` | `'Least squares fit'` |
| **默认**： `'None - clip'` |

### **Magnetic index extrapolation method** — 磁指数信息的外推方法 `None - clip`（默认）| `Constant` | `IGRF`

用于在 MAT 文件数据范围之外的时间对磁指数信息值进行外推的方法，指定为以下值之一。

| 方法 | 描述 |
| --- | --- |
| `None - clip` | 将磁指数信息的元素设置为 MAT 文件中可用的最近数据点。 |
| `Constant` | 将磁指数信息的元素设置为由 **Magnetic index extrapolation method** 参数指定的常量值。在这些时间限制之外的时间的磁指数元素基于这些时间限制处水平磁场强度的裁剪值。 |
| `IGRF` | 使用国际地磁参考场计算磁指数信息的元素。由于该模型定义的时间范围为 1900 年 1 月 1 日 12:00 AM UTC 至 2025 年 1 月 1 日 12:00 AM UTC，此范围之外时间的预测值将被裁剪为这些时间限制处的值。 |

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Atmospheric density source** 参数设置为
  `Dialog`。
- 将 **Atmospheric model** 设置为
  `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数**：`MagneticIndexExtrapMethod` |
| **类型**：字符向量 |
| **值**：`'None - clip'` | `'Constant'` | `'IGRF'` |
| **默认值**：`'None - clip'` |

### **Flags source** — 变化标志源 `Dialog`（默认）| `Port`

变化标志源，指定为 `Dialog` 或
`Port`。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Atmospheric density source** 参数设置为
  `Dialog`。
- 将 **Atmospheric model** 参数设置为
  `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数：** `fluxFlagsSrc` |
| **类型：** 字符向量 |
| **值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **Flags** — 变化标志 `ones(1,23)`（默认）

变化标志，指定为 23 个元素的数组（`ones(1,23)`）。您可以为每个字段指定以下值之一。每个字段的默认值为 `1`。

- 0.0 — 移除对输出的影响。
- 1.0 — 将该值的主效应和交叉项效应用于输出。
- 2.0 — 仅将该值的交叉项效应用于输出。

该数组包含以下字段。

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
| `Flags(9)` | 每日 AP。如果将此字段设置为 -1，模块将使用完整的磁指数信息矩阵（APH）而不是 `APH(:,1)`。 |
| `Flags(10)` | 所有 UT、经度效应 |
| `Flags(11)` | 经度效应 |
| `Flags(12)` | UT 及混合 UT、经度效应 |
| `Flags(13)` | 混合 AP、UT、经度效应 |
| `Flags(14)` | 三分之一日变化 |
| `Flags(15)` | 偏离扩散平衡 |
| `Flags(16)` | 所有外逸层温度变化 |
| `Flags(17)` | 所有来自 120,000 米温度（TLB）的变化 |
| `Flags(18)` | 所有低热层（TN1）温度变化 |
| `Flags(19)` | 所有 120,000 米梯度（S）变化 |
| `Flags(20)` | 所有上平流层（TN2）温度变化 |
| `Flags(21)` | 所有来自 120,000 米值（ZLB）的变化 |
| `Flags(22)` | 所有低中间层温度（TN3）变化 |
| `Flags(23)` | 湍流层顶标高变化 |

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Flags source** 设置为
  `Dialog`。
- 将 **Atmospheric density source** 参数设置为
  `Dialog`。
- 将 **Atmospheric model** 参数设置为
  `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数：** `fluxFlags` |
| **类型：** 字符向量 |
| **值：** `'ones(1,23)'` |
| **默认值：** `'ones(1,23)'` |

### **Include anomalous oxygen in density calculation** — 在密度计算中包含异常氧的选项 off（默认）| on

要在密度计算中包含异常氧，请选中此复选框。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Atmospheric density source** 参数设置为
  `Dialog`。
- 将 **Atmospheric model** 参数设置为
  `NRLMSISE-00`。

#### 编程使用

|  |
| --- |
| **模块参数：** `useOxygen` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **Drag coefficient source** — 阻力系数来源 `Dialog`（默认）| `Port`

阻力系数来源，指定为 `Dialog` 或
`Port`。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `dragCoeffSrc` |
| **类型：** 字符向量 |
| **值：** `'Dialog'` | `'Source'` |
| **默认值：** `'Dialog'` |

### **Drag coefficient** — 航天器阻力系数 2.179（默认）| 标量 | 大小为 *numSat* 的向量

用于大气阻力计算的航天器阻力系数，指定为标量或大小为 *numSat* 的向量。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Drag coefficient source** 参数设置为
  `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `dragCoeff` |
| **类型：** 字符向量 |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认值：** `'2.179'` |

### **Drag area source** — 阻力面积来源 `Dialog`（默认）| `Port`

阻力面积来源，指定为 `Dialog` 或
`Port`。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `dragAreaSrc` |
| **类型：** 字符向量 |
| **值：** `'Dialog'` | `'Source'` |
| **默认值：** `'Dialog'` |

### **Drag area** — 用于计算大气阻力加速度的面积 1.0（默认）| 标量 | 大小为 *numSat* 的向量

用于计算大气阻力加速度的面积，指定为标量或大小为 *numSat* 的向量。该航天器面积垂直于航天器相对速度。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为
  `Earth`。
- 将 **Include atmospheric drag** 参数设置为
  `on`。
- 将 **Drag area source** 参数设置为
  `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数：** `dragArea` |
| **类型：** 字符向量 |
| **值：** 标量 | 大小为 *numSat* 的向量 |
| **默认值：** `'1.0'` |

### Third Body

配置用于引力加速度的第三体点质量。

### **Ephemeris model** — 星历模型 `DE405`（默认）| `DE421` | `DE423` | `DE430` | `DE432t`

选择由喷气推进实验室定义的以下星历模型之一。模块使用星历数据来计算第三体点质量引力和太阳辐射压力所需的相对天体位置。

| **星历模型** | 描述 |
| --- | --- |
| `DE405` | 于 1998 年发布。该星历考虑的儒略日范围为 2305424.50（1599 年 12 月 9 日）至 2525008.50（2201 年 2 月 20 日）。该模块相对于 1998 年采用的国际天球参考框架 1.0 版实现这些星历。 |
| `DE421` | 于 2008 年发布。该星历考虑的儒略日范围为 2414992.5（1899 年 12 月 4 日）至 2469808.5（2050 年 1 月 2 日）。该模块相对于 1998 年采用的国际天球参考框架 1.0 版实现这些星历。 |
| `DE423` | 于 2010 年发布。该星历考虑的儒略日范围为 2378480.5（1799 年 12 月 16 日）至 2524624.5（2200 年 2 月 1 日）。该模块相对于 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |
| `DE430` | 于 2013 年发布。该星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。该模块相对于 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |
| `DE432t` | 于 2014 年 4 月发布。该星历考虑的儒略日范围为 2287184.5（1549 年 12 月 21 日）至 2688976.5（2650 年 1 月 25 日）。该模块相对于 2010 年采用的国际天球参考框架 2.0 版实现这些星历。 |

**注意**

此模块要求您使用 Add-On Explorer 下载星历数据。要启动 Add-On Explorer，请在 MATLAB 命令窗口中键入 `aeroDataPackage`。在 MATLAB 桌面工具栏中，点击 **Add-Ons**。

#### 编程使用

|  |
| --- |
| **模块参数**：`ephemerisModel` |
| **类型**：字符向量 |
| **值**：`DE405` | `DE421` | `DE423` | `DE430` |
| **默认值**：`'DE405'` |

### **Limit ephemerides date range** — 启用星历数据范围起始和结束的选项 `off`（默认）| `on`

控制仿真期间加载到内存中的数据量以及模块生成代码中包含的数据量：

- 选中此复选框以将星历数据的加载限制在指定的日期范围内。
- 清除此复选框以包含 **Ephemeris model** 表中定义的完整日期范围的数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`useDateRange` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Start date (JD)** — 星历日期范围的起始日期 `juliandate(2020, 1, 1)`（默认）| 儒略日

星历日期范围的起始日期，指定为儒略日。

#### 依赖关系

要启用此参数，请将 **Limit ephemerides date range** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`startDate` |
| **类型**：字符向量 |
| **值**：`'juliandate(2020, 1, 1)'` | 儒略日 |
| **默认值**：`'juliandate(2020, 1, 1)'` |

### **End date (JD)** — 星历日期范围的结束日期 `juliandate(2050, 1, 1)`（默认）| 儒略日

星历日期范围的结束日期，指定为儒略日。

#### 依赖关系

要启用此参数，请将 **Limit ephemerides date range** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`endDate` |
| **类型**：字符向量 |
| **值**：`'juliandate(2050, 1, 1)'` | 儒略格式日期 |
| **默认值**：`'juliandate(2050, 1, 1)'` |

### **Include third body gravity** — 第三体引力引起的加速度 `off`（默认）| `on`

要在轨道传播计算中包含第三体引力引起的加速度，请选中此复选框。否则，请清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数：** `useThirdBodyGravity` |
| **类型：** 字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **Sun** — 包含太阳引起的引力加速度 `on`（默认）| `off`

要包含太阳引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Sun gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `includeSunGravity` |
| **类型：** 字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值：** `'on'` |

### **Sun gravity model** — 太阳的第三体引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Sun** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。
- 将 **Sun** 第三体引力参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `sunThirdBodyGravityModel` |
| **类型：** 字符向量 |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **Mercury** — 包含水星引起的引力加速度 `off`（默认）| `on`

要包含水星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Mercury gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Mercury` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `includeMercuryGravity` |
| **类型：** 字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **Mercury gravity model** — 水星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Mercury** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。
- 将 **Mercury** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `mercuryThirdBodyGravityModel` |
| **类型：** 字符向量 |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **Venus** — 包含金星引起的引力加速度 `off`（默认）| `on`

要包含金星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Venus gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Venus` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `includeVenusGravity` |
| **类型：** 字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值：** `'off'` |

### **Venus gravity model** — 金星引力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选中 **Venus** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Sun` 以外的任何值。
- 将 **Include third body gravity** 参数设置为
  `on`。
- 将 **Venus** 参数设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数：** `venusThirdBodyGravityModel` |
| **类型：** 字符向量 |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值：** `'Point-mass'` |

### **Earth** — 包含地球引起的引力加速度 `on`（默认）| `off`

要包含地球引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Earth gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除
  `Earth` 以外的任何值。
- 将 **Include third body gravity** 设置为
  `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeEarthGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **地球重力模型** — 地球重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **Earth** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Earth` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Earth** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`earthThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值**：`'Point-mass'` |

### **Moon** — Include gravitational acceleration due to Moon `on` (default) | `off`

要包含由 Moon 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Moon gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Moon` 以外的任意值。
- 将 **Include third body gravity** 设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeMoonGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` | |
| **默认值**：`'on'` |

### **月球重力模型** — 月球重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **Moon** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Moon` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Moon** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`moonThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值**：`'Point-mass'` |

### **Mars** — Include gravitational acceleration due to Mars `off` (default) | `on`

要包含由 Mars 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Mars gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Mars` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeMarsGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` | |
| **默认值**：`'off'` |

### **火星重力模型** — 火星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **Mars** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Mars` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Mars** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`marsThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` | `'Spherical harmonics'` |
| **默认值**：`'Point-mass'` |

### **Jupiter** — Include gravitational acceleration due to Jupiter `off` (default) | `on`

要包含由 Jupiter 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Jupiter gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Jupiter` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeJupiterGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **木星重力模型** — 木星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选择 **Jupiter** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Jupiter` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 on。
- 将 **Jupiter** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`jupiterThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **Saturn** — Include gravitational acceleration due to Saturn `off` (default) | `on`

要包含由 Saturn 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Saturn gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Saturn` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeSaturnGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **土星重力模型** — 土星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选择 **Saturn** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Saturn` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Saturn** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`saturnThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **Uranus** — Include gravitational acceleration due to Uranus `off` (default) | `on`

要包含由 Uranus 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Uranus gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Uranus` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeUranusGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **天王星重力模型** — 天王星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选择 **Uranus** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Uranus` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Uranus** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`uranusThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **Neptune** — Include gravitational acceleration due to Neptune `off` (default) | `on`

要包含由 Neptune 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Neptune gravity model 中选择。

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Neptune` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeNeptuneGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **海王星重力模型** — 海王星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选择 **Neptune** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Central Body** 参数设置为除 `Neptune` 以外的任意值。
- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Neptune** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`neptuneThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **Pluto** — Include gravitational acceleration due to Pluto `off` (default) | `on`

要包含由 Pluto 引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Pluto gravity model 中选择。

#### 依赖关系

要启用此参数，请将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includePlutoGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **冥王星重力模型** — 冥王星重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)`

当选择 **Pluto** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`

#### 依赖关系

要启用此参数：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Pluto** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`plutoThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **Custom** — Include gravitational acceleration due to custom planet `off` (default) | `on`

要包含由自定义行星引起的引力加速度，请选中此复选框。否则，请清除它。要指定引力模型，请从 Custom gravity model 中选择。

#### 依赖关系

要启用此参数，请将 **Include third body gravity** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeCustomGravity` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **自定义重力模型** — 自定义重力模型 `Point-mass`（默认）| `Oblate ellipsoid (J2)` | `Spherical harmonics`

当选择 **Custom** 第三体引力参数时，从列表中选择要使用的引力势模型。

- `Point-mass`
- `Oblate ellipsoid (J2)`
- `Spherical harmonics`

#### 依赖关系

要启用此参数：

- 选择 **Include third body gravity** 参数。
- 选择 **Custom** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`customThirdBodyGravityModel` |
| **类型**：character vector |
| **值**：`'Point-mass'` | `'Oblate ellipsoid (J2)'` |
| **默认值**：`'Point-mass'` |

### **引力参数 (m^3/s^2)** — 自定义引力加速度 `42.828314258067e12`（默认）| 标量 | 长度为 *numCustom3rdBodies* 的向量

自定义第三体的自定义引力加速度，指定为标量或长度为 *numCustom3rdBodies* 的向量。*numCustom3rdBodies* 是提供给 **R\_cb** 输入端的行数。提供多个值以包含多个自定义天体。

#### 依赖关系

要启用此参数：

- 将 **Include third body gravity** 参数设置为 `on`。
- 将 **Custom** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`customThirdBodyMu` |
| **类型**：character vector |
| **值**：`'42.828314258067e12'` | scalar | vector of length *numCustom3rdBodies* |
| **默认值**：`'42.828314258067e12'` |

### SRP

### **Include solar radiation pressure (SRP)** — Acceleration due to solar radiation pressure `off` (default) | `on`

要在轨道传播计算中包含由太阳辐射压引起的加速度，请选中此复选框。否则，请清除该复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`useSRP` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Eclipse fraction source** — Source of eclipse fraction `Dialog` (default) | `Port`

日食分数（从航天器位置可见的太阳圆面比例）的来源，指定为 `Dialog` 或 `Port`。

#### 依赖关系

要启用此参数，请将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`useSRP` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Port'` |
| **默认值**：`'Dialog'` |

### **阴影模型** — 阴影模型 `Dual cone`（默认）| `Cylindrical`

用于日食计算的阴影模型，指定为以下值之一。

- `Cylindrical` — 分数可以为 0.0（Umbra）或 1.0（Sunlight）。
- `Dual cone` — 分数可以为 0.0（Umbra）、介于 0.0 和 1.0 之间（Penumbra 或 Antumbra），或 1.0（Sunlight）。

#### 编程使用

|  |
| --- |
| **模块参数**：`shadowModel` |
| **类型**：character vector |
| **值**：`'Dual cone'` | `'Cylindrical'` |
| **默认值**：`'Dual cone'` |

### **Include Earth** — Option to include Earth `on` (default) | `off`

当中心天体为 Moon 时，在日食计算中将 Earth 作为次要掩食天体包含在内的选项。

#### 依赖关系

将 **Central body** 参数设置为 `Moon`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeEarth` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Include Moon** — Option to include Moon `on` (default) | `off`

当中心天体为 Earth 时，在日食计算中将 Moon 作为次要掩食天体包含在内的选项。

#### 依赖关系

将 **Central body** 参数设置为 `Earth`。

#### 编程使用

|  |
| --- |
| **模块参数**：`includeMoon` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **反射率系数来源** — 航天器反射率系数的来源 `'Dialog'`（默认）| `'Port'`

航天器反射系数的来源，指定为 `Dialog` 或 `Port`。

#### 依赖关系

要启用此参数，请将 **Include solar radiation pressure (SRP)** 设置为 `on`。

#### 编程使用

|  |
| --- |
| **模块参数**：`reflectivityCoeffSrc` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Port'` |
| **默认值**：`'on'` |

### **Reflectivity coefficient** — Spacecraft coefficient of reflectivity `1.8` (default) | scalar | 2D array of size *numSat* | between `[1,2]`

用于太阳辐射压计算的航天器反射系数，指定为标量、大小为 *numSat* 的二维数组。*numSat* 是航天器数量。

**Tunable:** Yes

#### 依赖关系

要启用此参数：

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **Reflectivity coefficient source** 参数设置为 `Dialog`。

#### 编程使用

|  |
| --- |
| **模块参数**：`reflectivityCoeff` |
| **类型**：character vector |
| **值**：`'1.8'` | scalar | 2D array of size *numSat* | between `[1,2]` |
| **默认值**：`'1.8'` |

### **SRP 面积来源** — 航天器太阳辐射压力面积的来源 `Dialog`（默认）| `Port`

航天器太阳辐射压（SRP）面积的来源，指定为 `Dialog` 或 `Port`。

#### 依赖关系

要启用此参数，请将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`srpAreaSrc` |
| **类型**：字符向量 |
| **值：** `'Dialog'` | `'Port'` |
| **默认值：** `'Dialog'` |

### **SRP area** — 航天器被太阳照射的横截面积 `1.0`（默认值）| 标量 | 大小为 *numSat* 的二维数组

航天器被太阳照射的横截面积，指定为标量或大小为 *numSat* 的二维数组。*numSat* 是航天器的数量。

**可调：** 是

#### 依赖关系

要启用此参数

- 将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。
- 将 **SRP area source** 参数设置为 `Dialog`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`srpArea` |
| **类型**：字符向量 |
| **值：** `'1.0'` | 标量 | 大小为 *numSat* 的二维数组 |
| **默认值：** `'1.0'` |

### **Solar flux pressure (W\*s/m^3)** — 航天器太阳通量压力 `4.5344321e-6`（默认值）| 标量

太阳通量压力，指定为标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Include solar radiation pressure (SRP)** 参数设置为 `on`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`fluxPressure` |
| **类型**：字符向量 |
| **值：** `4.5344321e-6` | 标量 |
| **默认值：** `'4.5344321e-6'` |

### 单位

### **Units** — 参数和端口单位 `Metric (m/s)`（默认值）| `Metric (km/s)` | `Metric (km/h)` | `English (ft/s)` | `English (kts)`

参数和端口单位，如下所示指定。

| 单位 | 力 | 力矩 | 质量 | 惯量 | 距离 | 速度 | 加速度 | 面积 | 密度 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (m/s)` | 牛顿 | 牛顿-米 | 千克 | 千克·米² | 米 | 米/秒 | 米/秒² | m² | kg/m³，部分密度输出为 1/m³ |
| `Metric (km/s)` | 牛顿 | 牛顿-米 | 千克 | 千克·米² | 千米 | 千米/秒 | 千米/秒² | m² | kg/m³，部分密度输出为 1/m³ |
| `Metric (km/h)` | 牛顿 | 牛顿-米 | 千克 | 千克·米² | 千米 | 千米/小时 | 千米/小时² | m² | kg/m³，部分密度输出为 1/m³ |
| `English (ft/s)` | 磅力 | 英尺-磅 | 斯勒格 | 斯勒格·英尺² | 英尺 | 英尺/秒 | 英尺/秒² | 英尺² | lbm/ft³，部分密度输出为 1/ft³ |
| `English (kts)` | 磅力 | 英尺-磅 | 斯勒格 | 斯勒格·英尺² | 海里 | 节 | 节/秒 | 英尺² | lbm/ft³，部分密度输出为 1/ft³ |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** 字符向量 |
| **值：** `'Metric (m/s)'` | `'Metric (km/s)'` | `'Metric (km/h)'` | `'English (ft/s)'` | `'English (kts)'` |
| **默认值：** `'Metric (m/s)'` |

### **Angle units** — 角度单位 `Degrees`（默认值）| `Radians`

角度参数和端口单位，指定为 `Degrees` 或 `Radians`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `angleUnits` |
| **类型：** 字符向量 |
| **值：** `'Degrees'` | `'Radians'` |
| **默认值：** `'Degrees'` |

### **Time format** — 起始日期和时间输出的时间格式 `Julian date`（默认值）| `Gregorian`

**Start date/time (UTC Julian date)** 和输出端口 **tutc** 的时间格式，指定为 `Julian date` 或 `Gregorian`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `timeFormat` |
| **类型：** 字符向量 |
| **值：** `'Julian date'` | `'Gregorian'` |
| **默认值：** `'Julian date'` |
## 所属库

Aerospace Blockset / Spacecraft / Spacecraft Dynamics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2025a：Spacecraft Dynamics 模块支持第三体的高保真引力效应

Spacecraft Dynamics 模块现在通过新的第三体引力选项支持更高保真的工作流程。使用这些选项可以在航天器仿真中更精确地建模轨道传播。

要访问这些效应，请在 **Third Body** 选项卡上选择 **Include third body gravity** 参数。**Include third body gravity** 参数替代了 **Include third body point-mass gravity** 参数。

选择 **Include third body gravity** 后，您可以配置 Sun、Mercury、Venus、Moon、Earth、Mars、Jupiter、Saturn、Uranus、Neptune、Pluto 和 Custom 的引力选项。

### R2023b：Spacecraft Dynamics 模块变更

Spacecraft Dynamics 模块已更新，以考虑以下因素：

- 第三体引力对轨道传播的影响。
- 来自 `aeroReadSpaceWeatherData` 函数生成的数据文件的空间天气数据。
- 太阳辐射压力（SRP）。

## 描述

对一个或多个航天器进行动力学建模

Spacecraft Dynamics 模块使用数值积分对航天器的平移和旋转动力学进行建模。它计算一个或多个航天器随时间变化的位置、速度、姿态和角速度。为获得最准确的结果，请使用低容差设置（小于 1e-8）的变步长求解器。为在精度和速度之间进行权衡，可根据任务需求使用较大的容差。

您可以将初始轨道状态定义为

- 一组轨道根数。
- 位置和速度状态向量。

为传播轨道状态，该模块使用为当前中心天体选择的引力模型。它还包括您作为模块输入提供的外部加速度和力。要定义初始姿态状态，请使用四元数、方向余弦矩阵（DCM）或欧拉角。

为传播姿态状态，该模块使用作为模块输入提供的力矩以及模块上定义的质量属性。

Aerospace Blockset™ 使用标量在前的约定定义四元数。

Spacecraft Dynamics 模块支持标量和向量扩展。模块参数和输入端口维度决定了输出信号的数量和航天器的数量。在标量和向量扩展之后，**Orbit**、**Mass** 和 **Attitude** 选项卡中的所有参数以及除 **φθψ**（月球天平动角）和 **αδW**（赤经、赤纬和旋转角）输入端口之外的所有输入端口都针对每个航天器定义。

所提供的初始条件的大小决定了正在建模的航天器数量。如果您为 **Orbit**、**Attitude** 或 **Mass** 选项卡中的某个参数提供多个值，该模块将输出一个卫星星座。任何仅提供单个值的参数都会被扩展并应用于星座中的所有卫星。例如，如果您为模块上的所有参数提供单个值，但 **True anomaly** 包含六个值，则该模块将创建一个由六颗卫星组成的星座，仅改变真近点角。

该模块对模块输入端口应用相同的扩展行为。除 **Moon libration angles**（当 **Central body** 为 `Moon` 时）和 **Spin axis right ascension (RA) at J2000**、**Spin axis declination (Dec) at J2000** 以及 **Initial rotation angle at J2000**（当 **Central body** 为 `Custom` 时）之外，所有输入端口都支持扩展。所有其他端口接受扩展至正在建模的所有航天器的单个值，或应用于每个航天器的单独值。

有关 Spacecraft Dynamics 模块使用的坐标系以及旋转和平移动力学的更多信息，请参阅算法。

### 大气阻力

为帮助对高精度轨道传播中的航天器阻力进行建模，Spacecraft Dynamics 模块支持阻力。大气阻力影响在低地球轨道（LEO）飞行的航天器；距离地球越远，其相关性越低。有关大气阻力方程，请参阅平移动力学。

### 第三体引力效应

要包含点质量第三体引力的效应，请选择要包含哪些第三体。这些计算需要 **Ephemeris model** 和数据。有关第三体贡献方程，请参阅平移动力学。

### 太阳辐射压力

要包含太阳辐射压力（SRP）对航天器的影响，请提供食分或指定阴影模型来计算该食分。当大气阻力可忽略且指向精度要求严格时，请考虑将太阳辐射压力纳入考虑。有关太阳辐射压力方程，请参阅平移动力学。
