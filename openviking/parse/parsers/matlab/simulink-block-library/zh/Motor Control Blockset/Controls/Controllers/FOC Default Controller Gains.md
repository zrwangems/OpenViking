---
type: simulink-block
title: 'FOC Default Controller Gains'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'focdefaultcontrollergains'
documentation_source_path: 'ref/focdefaultcontrollergains.html'
language: zh-CN
chinese_source: worker-translation
---

# FOC Default Controller Gains

## 端口
```yaml
ports:
- name: Rs
  summary: 定子电阻标量
  direction: input
  data_types: single | double
- name: Ld
  summary: '*d* 轴电感标量'
  direction: input
  data_types: single | double
- name: Lq
  summary: '*q* 轴电感标量'
  direction: input
  data_types: single | double
- name: Lm
  summary: 励磁电感标量
  direction: input
  data_types: single | double
- name: Lls
  summary: 定子漏电感标量
  direction: input
  data_types: single | double
- name: Llr
  summary: 转子漏电感标量
  direction: input
  data_types: single | double
- name: J
  summary: 电机惯量标量
  direction: input
  data_types: single | double
- name: Ts
  summary: 电流控制器采样时间标量
  direction: input
  data_types: single | double
- name: Tsc
  summary: 速度控制器采样时间标量
  direction: input
  data_types: single | double
- name: SlowdownFactor
  summary: 用于减慢系统响应的因子标量，范围为 [1, 20]
  direction: input
  data_types: single | double
- name: IMax
  summary: 最大可测峰值-中性点电流标量
  direction: input
  data_types: single | double
- name: Vdc
  summary: 直流母线电压标量
  direction: input
  data_types: single | double
- name: Nbase
  summary: 电机额定转速标量
  direction: input
  data_types: single | double
- name: Rs
  summary: 定子电阻标量
  direction: input
  data_types: single | double
- name: Ld
  summary: '*d* 轴电感标量'
  direction: input
  data_types: single | double
- name: Lq
  summary: '*q* 轴电感标量'
  direction: input
  data_types: single | double
- name: J
  summary: 电机惯量标量
  direction: input
  data_types: single | double
- name: p
  summary: 电机中可用的极对数标量
  direction: input
  data_types: single | double
- name: FluxPM
  summary: 峰值永磁磁链标量
  direction: input
  data_types: single | double
- name: Ts
  summary: 电流控制器采样时间标量
  direction: input
  data_types: single | double
- name: Tsc
  summary: 速度控制器采样时间标量
  direction: input
  data_types: single | double
- name: CurrLoopDelay
  summary: 反馈路径中存在的电流延迟的总时间常数值标量
  direction: input
  data_types: single | double
- name: SpeedLoopDelay
  summary: 反馈路径中存在的速度延迟的总时间常数值标量
  direction: input
  data_types: single | double
- name: Vbase
  summary: 基准电压标量
  direction: input
  data_types: single | double
- name: Ibase
  summary: 基准电流标量
  direction: input
  data_types: single | double
- name: Nbase
  summary: 电机额定转速标量
  direction: input
  data_types: single | double
- name: PI Gains
  summary: PI 控制器增益总线
  direction: output
  data_types: single | double
- name: Status
  summary: PI 增益计算状态 true | false
  direction: output
  data_types: Boolean
```

### 输入

输入端口的显示取决于模块中选择的是 **Empirical method** 还是 **Based on Optimum theory**。有关输入端口的信息，请参阅以下部分：Empirical method 或 Optimum Theory。

#### Empirical method

### **Rs** — 定子电阻标量

电机的定子电阻（单位为欧姆）。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡的 **Block Output** 部分中选择以下参数中的一个或两个：

- **Current controller (d,q-axes)**
- **Field-weakening controller**

**数据类型：** `single` | `double`

### **Ld** — *d* 轴电感标量

永磁同步电机 (PMSM) 的 *d* 轴电感（单位为亨利）。

#### 依赖关系

要启用此端口：

- 将 **Motor selection** 参数设置为 `PMSM`。
- 选择 **Parameters** 选项卡的 **Block Output** 部分中提供的 **Current controller (d,q-axes)** 参数。

**数据类型：** `single` | `double`

### **Lq** — *q* 轴电感标量

永磁同步电机 (PMSM) 的 *q* 轴电感（单位为亨利）。

#### 依赖关系

要启用此端口：

- 将 **Motor selection** 参数设置为 `PMSM`。
- 在 **Parameters** 选项卡的 **Block Output** 部分中选择以下参数中的一个或两个：

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**数据类型：** `single` | `double`

### **Lm** — 励磁电感标量

交流感应电机 (ACIM) 的励磁电感（单位为亨利）。

#### 依赖关系

要启用此端口：

- 将 **Motor selection** 参数设置为 `ACIM`。
- 在 **Parameters** 选项卡的 **Block Output** 部分中选择以下参数中的一个或两个：

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**数据类型：** `single` | `double`

### **Lls** — 定子漏电感标量

交流感应电机 (ACIM) 的定子漏电感（单位为亨利）。

#### 依赖关系

要启用此端口：

- 将 **Motor selection** 参数设置为 `ACIM`。
- 在 **Parameters** 选项卡的 **Block Output** 部分中选择以下参数中的一个或两个：

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**数据类型：** `single` | `double`

### **Llr** — 转子漏电感标量

交流感应电机 (ACIM) 的转子漏电感（单位为亨利）。

#### 依赖关系

要启用此端口：

- 将 **Motor selection** 参数设置为 `ACIM`。
- 在 **Parameters** 选项卡的 **Block Output** 部分中选择以下参数中的一个或两个：

  - **Current controller (d,q-axes)**
  - **Field-weakening controller**

**数据类型：** `single` | `double`

### **J** — 电机惯量标量

电机的惯量（单位为 kg.m2）。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡的 **Block Output** 部分中选择 **Speed controller** 参数。

**数据类型：** `single` | `double`

### **Ts** — 电流控制器采样时间标量

基于 FOC 的电机控制算法中使用的电流 PI 控制器的采样时间（单位为秒）。

**数据类型：** `single` | `double`

### **Tsc** — 速度控制器采样时间标量

基于 FOC 的电机控制算法中使用的速度 PI 控制器的采样时间（单位为秒）。

#### 依赖关系

要启用此端口，请在 **Parameters** 选项卡的 **Block Output** 部分中选择 **Speed controller** 参数。

**数据类型：** `single` | `double`

### **SlowdownFactor** — 用于减慢系统响应的因子标量，范围为 [1, 20]

一个范围为 [1, 20] 的因子，您可以提供该因子来修改输出 PI 增益。较高的值会使控制器参数不那么激进，并减慢系统响应。

#### 依赖关系

要启用此端口，请清除 **Delays** 选项卡中提供的 **Specify filter and sensor delays** 参数。

**数据类型：** `single` | `double`

### **IMax** — 最大可测峰值-中性点电流标量

基于逆变器的电机驱动系统中的最大交流电流幅值（峰值）（单位为安培）。

#### 依赖关系

要启用此端口，需满足以下任一条件：

- 在 **参数** 选项卡的 **模块输出** 区域中选择 **速度控制器** 参数。

或

- 在 **参数** 选项卡的 **模块输出** 区域中选择 **电流控制器（d,q 轴）** 参数。
- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压标量

逆变器的直流母线电压（单位为伏特）。当您将 **输出单位** 参数设置为 `Per-Unit` 时，该模块使用 Vdc3 作为标幺值计算的基准值。

#### 依赖关系

要启用此端口：

- 在 **参数** 选项卡的 **模块输出** 区域中选择 **电流控制器（d,q 轴）** 参数。
- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`

### **Nbase** — 电机额定转速标量

用于标幺值计算的电机转速基准值（单位为 rpm）。

- 在 **参数** 选项卡的 **模块输出** 区域中选择 **速度控制器** 参数。
- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`

#### 最优理论

### **Rs** — 定子电阻标量

电机的定子电阻（单位为欧姆）。

**数据类型：** `single` | `double`

### **Ld** — *d* 轴电感标量

永磁同步电机（PMSM）的 *d* 轴电感（单位为亨利）。

**数据类型：** `single` | `double`

### **Lq** — *q* 轴电感标量

永磁同步电机（PMSM）的 *q* 轴电感（单位为亨利）。

**数据类型：** `single` | `double`

### **J** — 电机惯量标量

电机的惯量（单位为 kg.m2）。

**数据类型：** `single` | `double`

### **p** — 电机中可用的极对数标量

电机中可用的极对数。

**数据类型：** `single` | `double`

### **FluxPM** — 峰值永磁磁链标量

峰值永磁磁链，单位为韦伯。

**数据类型：** `single` | `double`

### **Ts** — 电流控制器采样时间标量

基于 FOC 的电机控制算法中使用的电流 PI 控制器的采样时间（单位为秒）。

**数据类型：** `single` | `double`

### **Tsc** — 速度控制器采样时间标量

基于 FOC 的电机控制算法中使用的速度 PI 控制器的采样时间（单位为秒）。

**数据类型：** `single` | `double`

### **CurrLoopDelay** — 反馈路径中存在的电流延迟的总时间常数值标量

反馈路径中存在的电流延迟的总时间常数值（单位为秒）。

**数据类型：** `single` | `double`

### **SpeedLoopDelay** — 反馈路径中存在的速度延迟的总时间常数值标量

反馈路径中存在的速度延迟的总时间常数值（单位为秒）。

**数据类型：** `single` | `double`

### **Vbase** — 基准电压标量

施加到电机的电压基准值（单位为伏特），用于标幺值计算。

#### 依赖关系

要启用此端口：

- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`

### **Ibase** — 基准电流标量

施加到电机的电流基准值（单位为伏特），用于标幺值计算。

#### 依赖关系

要启用此端口：

- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`

### **Nbase** — 电机额定转速标量

用于标幺值计算的电机转速基准值（单位为 rpm）。

#### 依赖关系

要启用此端口：

- 将 **输出单位** 参数设置为 `Per-Unit`。

**数据类型：** `single` | `double`
### 输出

### **PI Gains** — PI 控制器增益总线

用于 FOC 电机控制算法中的一个或多个 PI 控制器的控制增益，适用于经验法或最优理论。

如果选择 **Empirical method**，该值还基于 **Block output** 参数选择：

- *d* 轴和 *q* 轴电流控制器
- 速度控制器
- 弱磁控制器

下表总结了 **Empirical method** 下 **PI Gains** 输出总线的组成部分：

| 为经验法选择的 PI 控制器类型 | 总线组件 | | | 描述 |
| --- | --- | --- | --- | --- |
| *d* 轴电流 PI 控制器 | *Daxis\_Kp* | | | *d* 轴电流 PI 控制器的控制增益 *Kp* |
| *Daxis\_Ki* | | | *d* 轴电流 PI 控制器的控制增益 *Ki* |
| *Daxis\_Ki\*Ts* | | | *d* 轴电流 PI 控制器的控制增益 *Ki* 乘以电流控制器采样时间（*TS*） |
| *q* 轴电流 PI 控制器 | *Qaxis\_Kp* | | | *q* 轴电流 PI 控制器的控制增益 *Kp* |
| *Qaxis\_Ki* | | | *q* 轴电流 PI 控制器的控制增益 *Ki* |
| *Qaxis\_Ki\*Ts* | | | *q* 轴电流 PI 控制器的控制增益 *Ki* 乘以电流控制器采样时间（*TS*） |
| 速度 PI 控制器 | *Speed\_Kp* | | | 速度 PI 控制器的控制增益 *Kp* |
| *Speed\_Ki* | | | 速度 PI 控制器的控制增益 *Ki* |
| *Speed\_Ki\*Tsc* | | | 速度 PI 控制器的控制增益 *Ki* 乘以速度控制器采样时间（*TSC*） |
| 弱磁 PI 控制器 | *FWC\_Kp* | | | 弱磁 PI 控制器的控制增益 *Kp* |
| *FWC\_Ki* | | | 弱磁 PI 控制器的控制增益 *Ki* |
| *FWC\_Ki\*Ts* | | | 弱磁 PI 控制器的控制增益 *Ki* 乘以电流控制器采样时间（*TS*） |

**数据类型：** `single` | `double`

### **Status** — PI 增益计算状态 true | false

PI 增益的计算状态，返回以下值之一：

- True 表示模块已成功计算 **PI Gains** 输出端口可用的 PI 控制器增益。
- False 表示由于一个或多个输入的值不正确，模块无法计算 PI 控制器增益。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Motor selection
  summary: 电机类型 PMSM（默认）| ACIM
  group: ''
- name: Output unit
  summary: 模块输出的单位 SI Unit（默认）| Per-Unit
  group: ''
- name: Block Output
  summary: 模块的输出 Current controller (d,q-axes) | Field-weakening controller | Speed controller
  group: ''
- name: Specify filter and sensor delays
  summary: 启用滤波器和传感器延迟的添加 off（默认）| on
  group: Delays
- name: Current sensor delay (s)
  summary: 电流传感器引起的延迟 50e-6（默认）| 标量
  group: Delays
- name: Speed sensor delay (s)
  summary: 速度传感器引起的延迟 50e-6（默认）| 标量
  group: Delays
- name: Speed filter delay (s)
  summary: 速度滤波引起的延迟 0.02（默认）| 标量
  group: Delays
```

### **Motor selection** — 电机类型 `PMSM`（默认）| `ACIM`

您正在为其实现控制算法的电机类型：

- ACIM — 交流感应电机
- PMSM — 永磁同步电机

#### 依赖关系

仅当选择 **Empirical method** 选项来计算控制器增益时，此参数才可编辑。

### **Output unit** — 模块输出的单位 `SI Unit`（默认）| `Per-Unit`

模块在 **PI Gains** 输出端口输出的总线中元素的单位。

### **Block Output** — 模块的输出 `Current controller (d,q-axes)` | `Field-weakening controller` | `Speed controller`

使模块能够通过 **PI Gains** 端口计算并输出以下一个或多个元素：

- `Current controller (d,q-axes)` — *d* 轴和 *q* 轴电流控制的 PI 控制器的控制增益（*Kp* 和 *Ki*）。
- `Field-weakening controller` — 在弱磁区域运行的 PI 控制器的控制增益（*Kp* 和 *Ki*）。
- `Speed controller` — 速度 PI 控制器的控制增益（*Kp* 和 *Ki*）。

#### 依赖关系

仅当选择 **Empirical method** 选项来计算控制器增益时，此参数才可编辑。

### Delays

### **Specify filter and sensor delays** — 启用滤波器和传感器延迟的添加 `off`（默认）| `on`

选择此选项以指定速度滤波器延迟以及电流和速度传感器延迟。当您选择此参数时，模块会启用 **Current sensor delay (s)**、**Speed sensor delay (s)** 和 **Speed filter delay (s)** 参数。

#### 依赖关系

仅当您选择 **Empirical method** 选项来计算控制器增益时，才会显示此参数选择。

### **Current sensor delay (s)** — 电流传感器引起的延迟 `50e-6`（默认）| 标量

电流传感器引起的时间延迟（以秒为单位）。

#### 依赖关系

要启用此参数，请选择 **Specify filter and sensor delays** 参数。

仅当您选择 **Empirical method** 选项来计算控制器增益时，才会显示 **Specify filter and sensor delays** 参数。

### **Speed sensor delay (s)** — 速度传感器引起的延迟 `50e-6`（默认）| 标量

速度传感器引起的时间延迟（以秒为单位）。

#### 依赖关系

要启用此参数，请选择 **Specify filter and sensor delays** 参数。

仅当您选择 **Empirical method** 选项来计算控制器增益时，才会显示 **Specify filter and sensor delays** 参数。

### **Speed filter delay (s)** — 速度滤波引起的延迟 `0.02`（默认）| 标量

速度滤波引入的时间延迟（以秒为单位）。

#### 依赖关系

要启用此参数，请选择 **Specify filter and sensor delays** 参数。

仅当您选择 **Empirical method** 选项来计算控制器增益时，才会显示 **Specify filter and sensor delays** 参数。
## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

在运行时基于经验法或最优理论为基于 FOC 的算法计算控制器增益

FOC Default Controller Gains 模块基于经验法或最优理论，为用于磁场定向控制（FOC）算法中的 PI 控制器计算控制器增益。

如果选择 **Empirical method** 选项：

- 该模块通过将控制回路近似为低阶线性时不变系统，并应用最优理论考虑系统中的固定延迟来计算控制器增益。
- 该模块使用基于 *d-q* 参考坐标系的电机模型，计算电流控制器、速度控制器和弱磁控制器中使用的 PI 控制器增益。该模块内部使用函数 `mcb.getPIControllerParameters` 来计算控制增益。有关此函数的更多详细信息，请参阅 Obtain Controller Gains Using Empirical Method。
- 该模块接受电机参数以及电流和速度控制器采样时间，生成包含比例和积分控制增益的总线，您可将其用于基于 FOC 算法中的 PI 控制器。
- 该模块使用您在 **SlowdownFactor** 输入端口指定的值来修改 PI 增益输出，使其不那么激进并减慢系统响应。

**注意**

- 该模块使用经验计算来计算控制增益。该模块计算出的增益可能不是最优的，可能需要额外整定以改善动态性能。
- 建议在触发子系统或慢速运行的控制回路中使用该模块。
- 该模块输入接受大于零的值。

如果选择 **Based on optimum theory** 选项：

- 该模块通过将控制回路近似为低阶线性时不变系统，并应用最优理论来计算控制器增益，能够考虑系统中存在的任意数量的延迟（例如，由硬件滤波器和观测器引起的延迟（在无传感器 FOC 的情况下））。
- 该模块使用：。

  - 模最优理论计算电流控制器增益
  - 对称最优理论计算速度控制器增益
- 该模块使用基于 *d-q* 参考坐标系的电机模型，计算电流控制器和速度控制器中使用的 PI 控制器增益。该模块内部使用函数 `mcb.CalcFOCGains` 来计算控制增益。有关此函数和该模块用法的更多详细信息，请参阅 Obtain Controller Gains to Run Motor Using Field-Oriented Control。
- 该模块接受电机参数以及电流和速度控制器采样时间，生成包含比例和积分控制增益的总线，可与 PI 控制器一起用于实现电机驱动系统的控制算法。
- 如果为 Output unit 参数选择 `Per-unit`，请通过相应端口提供 Vbase（单位为 Volts）、Ibase（单位为 Amperes）和 Nbase（单位为 RPM）作为输入。
- 使用输入端口 **CurrLoopDelay** 和 **SpeedLoopDelay** 分别提供电流环和速度环反馈路径中延迟的总体时间常数值。
