---
type: simulink-block
title: 'Longitudinal Driver'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Vehicle Dynamics and Scenarios'
documentation_page: 'longitudinaldriver'
documentation_source_path: 'ref/longitudinaldriver.html'
language: zh-CN
chinese_source: worker-translation
---

# Longitudinal Driver

## 端口

### 输入

### **VelRef** — 参考车辆速度 `scalar`

参考速度，*vref*，单位 m/s。

### **EnblAccelOvr** — 启用加速度命令覆盖 `scalar`

启用加速度命令覆盖。

#### 依赖关系

要启用此端口，请选择 **Acceleration override**。

**数据类型：** `Boolean`

### **AccelOvrCmd** — 加速度覆盖命令 `scalar`

加速度覆盖命令，归一化为 0 到 1。

#### 依赖关系

要启用此端口，请选择 **Acceleration override**。

**数据类型：** `double`

### **AccelHld** — 加速度保持 `scalar`

将加速度命令保持为当前值的布尔信号。

#### 依赖关系

要启用此端口，请选择 **Acceleration hold**。

**数据类型：** `Boolean`

### **AccelZero** — 禁用加速度命令 `scalar`

禁用加速度命令。

#### 依赖关系

要启用此端口，请选择 **Acceleration disable**。

**数据类型：** `Boolean`

### **EnblDecelOvr** — 启用减速度命令覆盖 `scalar`

启用减速度命令覆盖。

#### 依赖关系

要启用此端口，请选择 **Deceleration override**。

**数据类型：** `Boolean`

### **DecelOvrCmd** — 减速度覆盖命令 `scalar`

减速度覆盖命令，归一化为 0 到 1。

#### 依赖关系

要启用此端口，请选择 **Deceleration override**。

**数据类型：** `double`

### **DecelHld** — 减速度保持 `scalar`

将减速度命令保持为当前值的布尔信号。

#### 依赖关系

要启用此端口，请选择 **Deceleration hold**。

**数据类型：** `Boolean`

### **DecelZero** — 禁用减速度命令 `scalar`

禁用减速度命令。

#### 依赖关系

要启用此端口，请选择 **Deceleration disable**。

**数据类型：** `Boolean`

### **ExtGear** — 挡位 `scalar`

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### 依赖关系

要启用此端口，请将 **Shift type, shftType** 设置为 `External`。

### **VelFdbk** — 纵向车辆速度 `scalar`

纵向车辆速度，*U*，在车辆固定坐标系中，单位 m/s。

### **Grade** — 道路坡度角 `scalar`

道路坡度角，*θ* 或 *γ*，单位 deg。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | 变量 | 描述 |
| --- | --- | --- | --- |
| `Accel` | | *yacc* | 命令的车辆加速度，归一化为 0 到 1 |
| `Decel` | | *ydec* | 命令的车辆减速度，归一化为 0 到 1 |
| `Gear` | | | 命令挡位的整数值 |
| `Clutch` | | | 离合器命令 |
| `Err` | | *eref* | 参考车辆速度和车辆速度之差 |
| `ErrSqrSum` | | ∫0teref2dt | 误差的积分平方 |
| `ErrMax` | | max(eref(t)) | 仿真期间的最大误差 |
| `ErrMin` | | min(eref(t)) | 仿真期间的最小误差 |
| `ExtActions` | `EnblAccelOvr` | | 用输入加速度命令覆盖加速命令 |
| `AccelOvrCmd` | | 输入加速覆盖命令 |
| `AccelHld` | | 将加速度命令保持为当前值 |
| `AccelZero` | | 禁用加速度命令 |
| `EnblDecelOvr` | | 用输入减速度命令覆盖减速命令 |
| `DecelOvrCmd` | | 输入减速度覆盖命令 |
| `DecelHld` | | 将减速命令保持为当前值 |
| `DecelZero` | | 禁用减速命令 |

### **AccelCmd** — 命令的车辆加速度 `scalar`

命令的车辆加速度，*yacc*，归一化为 0 到 1。

### **DecelCmd** — 命令的车辆减速度 `scalar`

命令的车辆减速度，*ydec*，归一化为 0 到 1。

### **GearCmd** — 命令的车辆挡位 `scalar`

命令的车辆挡位的整数值。

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### 依赖关系

要启用此端口，请选择 **Output gear signal**。

## 参数

#### 外部操作

### **Accelerator override** — 覆盖加速度命令 `off`（默认） | `on`

选择以用输入加速度命令覆盖加速度命令。

#### 依赖关系

选择此参数会创建 `EnblAccelOvr` 和 `AccelOvrCmd` 输入端口。

### **Accelerator hold** — 保持加速度命令 `off`（默认） | `on`

选择以保持加速度命令。

#### 依赖关系

选择此参数会创建 `AccelHld` 输入端口。

### **Accelerator disable** — 禁用加速度命令 `off`（默认） | `on`

选择以禁用加速度命令。

#### 依赖关系

选择此参数会创建 `AccelZero` 输入端口。

### **Decelerator override** — 覆盖减速度命令 `off`（默认） | `on`

选择以用输入减速度命令覆盖减速度命令。

#### 依赖关系

选择此参数会创建 `EnblDecelOvr` 和 `DecelOvrCmd` 输入端口。

### **Decelerator hold** — 保持减速度命令 `off`（默认） | `on`

选择以保持减速度命令。

#### 依赖关系

选择此参数会创建 `DecelHld` 输入端口。

### **Decelerator disable** — 禁用减速度命令 `off`（默认） | `on`

选择以禁用减速度命令。

#### 依赖关系

选择此参数会创建 `DecelZero` 输入端口。

#### 配置

### **Control type, cntrlType** — 纵向控制 `PI`（默认） | `Scheduled PI` | `Predictive`

纵向控制类型。

| 设置 | 模块实现 |
| --- | --- |
| `PI` | 带跟踪抗积分饱和和前馈增益的比例积分（PI）控制。 |
| `Scheduled PI` | 带跟踪抗积分饱和和前馈增益的 PI 控制，这些增益是车辆速度的函数。 |
| `Predictive` | 由 C. C. MacAdam1, 2, 3 开发的最优单点预览（前视）控制模型。该模型表示路径跟随和避障机动期间的驾驶员转向控制行为。驾驶员进行预览（前视）以跟随预定义路径。为实现 MacAdam 模型，模块：  - 将动力学表示为线性单轨（自行车）车辆 - 最小化提前 *T\** 秒的单点预览误差信号 - 考虑由感知和神经肌肉机制引起的驾驶员滞后 |

### **Shift type, shftType** — 换挡类型 `None`（默认） | `Reverse, Neutral, Drive` | `Scheduled` | `External`

换挡类型。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 无变速器。模块输出恒定挡位 1。 使用此设置可最大程度减少生成加速和制动命令以跟踪前进车辆运动所需的参数数量。此设置不允许车辆倒车。 |
| `Reverse, Neutral, Drive` | 模块使用 Stateflow 图对倒挡、空挡和前进挡换挡调度进行建模。 使用此设置可通过简单的倒挡、空挡和前进挡换挡调度生成加速和制动命令，以跟踪前进和倒车车辆运动。根据车辆状态和车辆速度反馈，模块使用初始挡位和换挡所需时间将车辆升挡至前进挡或降挡至倒挡或空挡。 对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |
| `Scheduled` | 模块使用 Stateflow 图对倒挡、空挡、驻车挡和 N 速挡换挡调度进行建模。 使用此设置可通过倒挡、空挡、驻车挡和 N 速挡换挡调度生成加速和制动命令，以跟踪前进和倒车车辆运动。根据车辆状态和车辆速度反馈，模块使用这些参数确定：  - 初始挡位 - 升挡和降挡加速踏板位置 - 升挡和降挡速度 - 从空挡换挡和接合前进挡与倒挡的时机   对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |
| `External` | 模块使用输入挡位、车辆状态和速度反馈生成加速和制动命令，以跟踪前进和倒车车辆运动。 对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |

### **Reference and feedback units, velUnits** — 速度单位 m/s（默认）

车辆速度参考和反馈单位。

#### 依赖关系

如果将 **Control type, cntrlType** 控制类型设置为 `Scheduled` 或 `Scheduled PI`，模块将 **Reference and feedback units, velUnits** 用于 **Nominal speed, vnom** 参数维度。

如果将 **Shift Type, shftType** 设置为 `Scheduled`，模块将 **Longitudinal velocity units, velUnits** 用于这些参数维度：

- **Upshift velocity data table, upShftTbl**
- **Downshift velocity data table, dwnShftTbl**

### **Output gear signal** — 创建 `GearCmd` 输出端口 `off`（默认） | `on`

指定以创建输出端口 `GearCmd`。

### 控制

#### 纵向

### **Proportional gain, Kp** — 增益 `10`（默认） | `scalar`

比例增益，*Kp*，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI`。

### **Integral gain, Ki** — 增益 `5`（默认） | `scalar`

积分增益，*Ki*，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI`。

### **Velocity feed-forward, Kff** — 增益 `.1`（默认） | `scalar`

速度前馈增益，*Kff*，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI`。

### **Grade angle feed-forward, Kg** — 增益 `0`（默认） | `scalar`

坡度角前馈增益，*Kg*，单位 1/deg。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI`。

### **Velocity gain breakpoints, VehVelVec** — 断点 `[0 100]`（默认） | `vector`

速度增益断点，*VehVelVec*，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `Scheduled PI`。

### **Velocity feed-forward gain values, KffVec** — 增益 `[.1 .1]`（默认） | `vector`

速度前馈增益值，*KffVec*，作为车辆速度的函数，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `Scheduled PI`。

### **Proportional gain values, KpVec** — 增益 `[10 10]`（默认） | `vector`

比例增益值，*KpVec*，作为车辆速度的函数，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `Scheduled PI`。

### **Integral gain values, KiVec** — 增益 `[5 5]`（默认） | `vector`

积分增益值，*KiVec*，作为车辆速度的函数，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `Scheduled PI`。

### **Grade angle feed-forward values, KgVec** — 坡度增益 `[0 0]`（默认） | `vector`

坡度角前馈值，*KgVec*，作为车辆速度的函数，单位 1/deg。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `Scheduled PI`。

### **Nominal speed, vnom** — 标称车辆速度 `5`（默认） | `scalar`

标称车辆速度，*vnom*，单位由 **Reference and feedback units, velUnits** 参数指定。模块使用标称速度对控制器增益进行归一化。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI` 或 `Scheduled PI`。

### **Anti-windup, Kaw** — 增益 `1`（默认） | `scalar`

抗积分饱和增益，*Kaw*，无量纲。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI` 或 `Scheduled PI`。

### **Error filter time constant, tauerr** — 滤波器 `.01`（默认） | `scalar`

误差滤波器时间常数，*τerr*，单位 s。要禁用滤波器，请输入 0。

#### 依赖关系

要创建此参数，请将 **Control type** 设置为 `PI` 或 `Scheduled PI`。

#### 预测

### **Vehicle mass, m** — 质量 `1500`（默认） | `scalar`

车辆质量，*m*，单位 kg。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Effective vehicle total tractive force, Kpt** — 牵引力 `3000`（默认） | `scalar`

有效车辆总牵引力，*Kpt*，单位 N。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Driver response time, tau** — Tau `.1`（默认） | `scalar`

驾驶员响应时间，*τ*，单位 s。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Preview distance, L** — 距离 `2`（默认） | `scalar`

驾驶员预览距离，*L*，单位 m。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Rolling resistance coefficient, aR** — 阻力 `200`（默认） | `scalar`

静态滚动和传动系阻力系数，*aR*，单位 N。模块使用该参数估计恒定加速度或制动力。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Rolling and driveline resistance coefficient, bR** — 阻力 `2.5`（默认） | `scalar`

滚动和传动系阻力系数，*bR*，单位 N·s/m。模块使用该参数估计线性速度相关加速度或制动力。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Aerodynamic drag coefficient, cR** — 阻力 `.5`（默认） | `scalar`

空气阻力系数，*cR*，单位 N·s^2/m^2。模块使用该参数估计二次速度相关加速度或制动力。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### **Gravitational constant, g** — 重力常数 `9.81`（默认） | `scalar`

重力常数，g，单位 m/s^2。

#### 依赖关系

要创建此参数，请将 **Longitudinal control type, cntrlType** 设置为 `Predictive`。

### 换挡

#### Reverse, Neutral, Drive

### **Initial gear, GearInit** — 初始挡位 `0`（默认） | `scalar`

初始挡位的整数值。模块使用初始挡位生成加速和制动命令，以跟踪前进和倒车车辆运动。

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Reverse, Neutral, Drive` 或 `Scheduled`。如果指定 `Reverse, Neutral, Drive`，**Initial Gear, GearInit** 参数值只能是 `-1`、`0` 或 `1`。

### **Time required to shift, tShift** — 时间 `.1`（默认） | `scalar`

换挡所需时间，*tShift*，单位 s。模块使用换挡所需时间生成加速和制动命令，以通过倒挡、空挡和前进挡换挡调度跟踪前进和倒车车辆运动。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Reverse, Neutral, Drive`。

#### Scheduled

### **Initial gear, GearInit** — 初始挡位 `0`（默认） | `scalar`

初始挡位的整数值。模块使用初始挡位生成加速和制动命令，以跟踪前进和倒车车辆运动。

| Gear | Integer |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Reverse, Neutral, Drive` 或 `Scheduled`。如果指定 `Reverse, Neutral, Drive`，**Initial Gear, GearInit** 参数值只能是 `-1`、`0` 或 `1`。

### **Up and down shift accelerator pedal positions, pdlVec** — 踏板位置断点 `[0.1 0.4 0.5 0.9]`（默认） | `[1-by-m] vector`

用于计算升挡和降挡速度的查找表踏板位置断点，无量纲。向量维度为 1 乘以踏板位置断点数量 `m`。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

### **Upshift velocity data table, upShftTbl** — 表 `[m-by-n] array`

升挡速度数据，作为踏板位置和挡位的函数，单位由 **Reference and feedback units, velUnits** 参数指定。升挡速度表示挡位应增加 1 时的车辆速度。

数组维度为 `m` 个踏板位置乘以 `n` 个挡位。当 `n` 等于 1 时，第一列数据是空挡的升挡速度。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

### **Downshift velocity data table, dwnShftTbl** — 表 `[m-by-n] array`

降挡速度数据，作为踏板位置和挡位的函数，单位由 **Reference and feedback units, velUnits** 参数指定。降挡速度表示挡位应减少 1 时的车辆速度。

数组维度为 `m` 个踏板位置乘以 `n` 个挡位。当 `n` 等于 1 时，第一列数据是空挡的降挡速度。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

### **Time required to shift, tClutch** — 时间 `.5`（默认） | `scalar`

换挡所需时间，*tClutch*，单位 s。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

### **Time required to engage reverse from neutral, tRev** — 时间 `.5`（默认） | `scalar`

从空挡接合倒挡所需时间，*tRev*，单位 s。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

### **Time required to engage park from neutral, tPark** — 时间 `120`（默认） | `scalar`

从空挡接合驻车挡所需时间，*tPark*，单位 s。

#### 依赖关系

要创建此参数，请将 **Shift type, shftType** 设置为 `Scheduled`。

## 所属库

Powertrain Blockset / Vehicle Scenario Builder Vehicle Dynamics Blockset / Vehicle Scenarios / Driver

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

纵向速度跟踪控制器

Longitudinal Driver 模块实现纵向速度跟踪控制器。基于参考速度和反馈速度，该模块生成归一化的加速和制动命令，这些命令可以从 0 到 1 变化。您可以使用该模块对驾驶员的动态响应进行建模，或生成跟踪纵向驾驶循环所需的命令。

### 配置

**外部操作**

使用 **External Actions** 参数为可以禁用、保持或覆盖闭环加速或减速命令的信号创建输入端口。模块对输入命令使用以下优先级顺序：禁用（最高）、保持、覆盖。

此表总结了外部操作参数。

| 目标 | 外部操作参数 | 输入端口 | 数据类型 |
| --- | --- | --- | --- |
| 用输入加速度命令覆盖加速命令。 | **Accelerator override** | `EnablAccelOvr` | `Boolean` |
| `AccelOvrCmd` | `double` |
| 将加速度命令保持为当前值。 | **Accelerator hold** | `AccelHld` | `Boolean` |
| 禁用加速度命令。 | **Accelerator disable** | `AccelZero` | `Boolean` |
| 用输入减速度命令覆盖减速命令。 | **Decelerator override** | `EnablDecelOvr` | `Boolean` |
| `DecelOvrCmd` | `double` |
| 将减速命令保持为当前值。 | **Decelerator hold** | `DecelHld` | `Boolean` |
| 禁用减速命令。 | **Decelerator disable** | `DecelZero` | `Boolean` |

**控制器**

使用 **Control type, cntrlType** 参数指定以下控制选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `PI` | 带跟踪抗积分饱和和前馈增益的比例积分（PI）控制。 |
| `Scheduled PI` | 带跟踪抗积分饱和和前馈增益的 PI 控制，这些增益是车辆速度的函数。 |
| `Predictive` | 由 C. C. MacAdam1, 2, 3 开发的最优单点预览（前视）控制模型。该模型表示路径跟随和避障机动期间的驾驶员转向控制行为。驾驶员进行预览（前视）以跟随预定义路径。为实现 MacAdam 模型，模块：  - 将动力学表示为线性单轨（自行车）车辆 - 最小化提前 *T\** 秒的单点预览误差信号 - 考虑由感知和神经肌肉机制引起的驾驶员滞后 |

**换挡**

使用 **Shift type, shftType** 参数指定以下换挡选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 无变速器。模块输出恒定挡位 1。 使用此设置可最大程度减少生成加速和制动命令以跟踪前进车辆运动所需的参数数量。此设置不允许车辆倒车。 |
| `Reverse, Neutral, Drive` | 模块使用 Stateflow® 图对倒挡、空挡和前进挡换挡调度进行建模。 使用此设置可通过简单的倒挡、空挡和前进挡换挡调度生成加速和制动命令，以跟踪前进和倒车车辆运动。根据车辆状态和车辆速度反馈，模块使用初始挡位和换挡所需时间将车辆升挡至前进挡或降挡至倒挡或空挡。 对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |
| `Scheduled` | 模块使用 Stateflow 图对倒挡、空挡、驻车挡和 N 速挡换挡调度进行建模。 使用此设置可通过倒挡、空挡、驻车挡和 N 速挡换挡调度生成加速和制动命令，以跟踪前进和倒车车辆运动。根据车辆状态和车辆速度反馈，模块使用这些参数确定：  - 初始挡位 - 升挡和降挡加速踏板位置 - 升挡和降挡速度 - 从空挡换挡和接合前进挡与倒挡的时机   对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |
| `External` | 模块使用输入挡位、车辆状态和速度反馈生成加速和制动命令，以跟踪前进和倒车车辆运动。 对于空挡，模块使用制动命令控制车辆速度。对于倒挡，模块使用加速度命令生成扭矩，并使用制动命令降低车辆速度。 |

**挡位信号**

使用 **Output gear signal** 参数创建 `GearCmd` 输出端口。`GearCmd` 信号包含命令的车辆挡位的整数值。

| 挡位 | 整数 |
| --- | --- |
| Park | `80` |
| Reverse | `-1` |
| Neutral | `0` |
| Drive | `1` |
| Gear | `Gear number` |

### 控制器：PI 速度跟踪

如果将控制类型设置为 `PI` 或 `Scheduled PI`，模块实现带跟踪抗积分饱和和前馈增益的比例积分（PI）控制。对于 `Scheduled PI` 配置，模块使用作为车辆速度函数的前馈增益。

要计算速度控制输出，模块使用这些方程。

| 设置 | 方程 |
| --- | --- |
| `PI` | y=Kffvnomvref+Kperefvnom+∫(Kierefvnom+Kaweout)dt+Kgγ |
| `Scheduled PI` | y=Kff(v)vnomvref+Kp(v)erefvnom+∫(Ki(v)erefvnom+Kaweout)dt+Kg(v)γ |

其中：eref=vref−veout=ysat−yysat={−1y<−1y−1≤y≤111<y

速度误差低通滤波器使用此传递函数。

H(s)=1τerrs+1   对于   τerr>0

要计算加速和制动命令，模块使用这些方程。

yacc={0ysat<0ysat0≤ysat≤111<ysatydec={0ysat>0−ysat−1≤ysat≤01ysat<−1

这些方程使用以下变量。

|  |  |
| --- | --- |
| *vnom* | 标称车辆速度 |
| *Kp* | 比例增益 |
| *Ki* | 积分增益 |
| *Kaw* | 抗积分饱和增益 |
| *Kff* | 速度前馈增益 |
| *Kg* | 坡度角前馈增益 |
| *γ* | 坡度角 |
| *τerr* | 误差滤波器时间常数 |
| *y* | 标称控制输出幅值 |
| *ysat* | 饱和控制输出幅值 |
| *eref* | 速度误差 |
| *eout* | 饱和控制输出与标称控制输出之差 |
| *yacc* | 加速度信号 |
| *ydec* | 制动信号 |
| *v* | 速度反馈信号 |
| *vref* | 参考速度信号 |

### 控制器：预测速度跟踪

如果将 **Control type, cntrlType** 参数设置为 `Predictive`，模块实现由 C. C. MacAdam1, 2, 3 开发的最优单点预览（前视）控制模型。该模型表示路径跟随和避障机动期间的驾驶员转向控制行为。驾驶员进行预览（前视）以跟随预定义路径。为实现 MacAdam 模型，模块：

- 将动力学表示为线性单轨（自行车）车辆
- 最小化提前 T* 秒的单点预览误差信号
- 考虑由感知和神经肌肉机制引起的驾驶员滞后

**车辆动力学**

对于纵向运动，模块实现这些线性动力学。

x1=vx˙1=x2=Kptm−gsin(γ)+Frx1

用矩阵表示法：

x˙=Fx+gu¯其中：x=[x1x2]F=[01Frm0]g=[0Kptm]u¯=u− m2Kptgsin(γ)

模块使用此方程计算滚动阻力。

Fr=−[tanh(x1)( arx1+crx1)+br]

单点模型假设提前 *T\** 秒的单点预览误差信号最小。*a\** 是驾驶员基于当前转向控制输入预测未来车辆响应的能力。*b\** 是驾驶员基于当前车辆状态预测未来车辆响应的能力。模块使用这些方程。

a\*=(T\*)mT[I+∑n=1∞Fn(T\*)n(n+1)!]geb\*=mT[I+∑n=1∞Fn(T\*)nn!]其中： mT=[11]

这些方程使用以下变量。

|  |  |
| --- | --- |
| *a*, *b* | 分别为前轮和后轮轮胎位置 |
| *m* | 车辆质量 |
| *I* | 车辆转动惯量 |
| *a\**, ***b**\** | 分别为驾驶员预测标量增益和向量增益 |
| ***x*** | 预测车辆状态向量 |
| *v* | 纵向速度 |
| ***F*** | 系统矩阵 |
| *Kpt* | 牵引力和制动限制 |
| *γ* | 坡度角 |
| ***g*** | 控制系数向量 |
| *g* | 重力常数 |
| *T\** | 预览时间窗口 |
| *ƒ(t+T\*)* | 提前 T* 秒的预览路径输入 |
| *U* | 前向车辆速度 |
| ***mT*** | 常数观测向量；提供车辆横向位置 |
| *Fr* | 滚动阻力 |
| *ar* | 静态滚动和传动系阻力 |
| *br* | 线性滚动和传动系阻力 |
| *cr* | 空气动力滚动和传动系阻力 |

**优化**

模块实现的单点模型在当前预览区间 (*t*, *t+T*) 上找到使局部性能指标 *J* 最小的转向命令。

J=1T∫tt+T[f(η)−y(η)]2dη

要使 *J* 相对于转向命令最小，必须满足此条件。

dJdu=0

您可以根据当前非最优和相应的非零预览输出误差 *T\** 秒前1, 2, 3 来表达最优控制解。

uo(t)=u(t)+e(t+T\*)a\*

模块使用预览距离和车辆纵向速度确定预览时间窗口。

T\*=LU

这些方程使用以下变量。

|  |  |
| --- | --- |
| *T\** | 预览时间窗口 |
| *ƒ(t+T\*)* | 提前 *T\** 秒的预览路径输入 |
| *y(t+T\*)* | 提前 *T\** 秒的预览被控对象输出 |
| *e(t+T\*)* | 提前 *T\** 秒的预览误差信号 |
| *u(t)*, *uo(t)* | 分别为转向角和最优转向角 |
| *L* | 预览距离 |
| *J* | 性能指标 |
| *U* | 前向（纵向）车辆速度 |

**驾驶员滞后**

模块实现的单点模型引入驾驶员滞后。驾驶员滞后考虑了驾驶员执行跟踪任务时的延迟。具体来说，它是由感知和神经肌肉机制引起的传递延迟。要计算驾驶员传递延迟，模块实现此方程。

H(s)=e−sτ

这些方程使用以下变量。

|  |  |
| --- | --- |
| *τ* | 驾驶员传递延迟 |
| *y(t+T\*)* | 提前 *T\** 秒的预览被控对象输出 |
| *e(t+T\*)* | 提前 *T\** 秒的预览误差信号 |
| *u(t)*, *uo(t)* | 分别为转向角和最优转向角 |
| *J* | 性能指标 |
