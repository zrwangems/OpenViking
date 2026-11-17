---
type: simulink-block
title: 'Pulsating High Freq Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'pulsatinghighfreqobserver'
documentation_source_path: 'ref/pulsatinghighfreqobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulsating High Freq Observer

## 端口
```yaml
ports:
- name: Iab hf
  summary: PHF 电流响应向量
  direction: input
  data_types: single | double | fixed point
- name: Enable
  summary: 触发模块操作的输入标量
  direction: input
  data_types: Boolean
- name: θin
  summary: 初始转子位置标量
  direction: input
  data_types: single | double | fixed point
- name: IPEEn
  summary: 启用阶段 1 初始位置估计（IPE）操作的标量
  direction: input
  data_types: Boolean
- name: Vαβ hf
  summary: PHF 输出标量
  direction: output
  data_types: single | double | fixed point
- name: θest
  summary: 估计转子位置标量
  direction: output
  data_types: single | double | fixed point
- name: PosEn
  summary: '*θest* 端口状态标量'
  direction: output
  data_types: single | double | fixed point
- name: Info
  summary: 总线信号 总线
  direction: output
```

### 输入

### **Iab hf** — PHF 电流响应向量

电机响应 PHF 电压注入的高频（a 相和 b 相）电流反馈，单位为安培或标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 触发模块操作的输入标量

在此端口指定以下输入之一：

- `1` — 启用模块操作
- `0` — 禁用模块操作

**数据类型：** `Boolean`

### **θin** — 初始转子位置标量

当模块跳过阶段 1 初始位置估计（IPE）操作时的初始转子位置输入。位置以弧度、度或标幺值表示。有关模块运行的两个阶段的详细信息，请参阅算法。

单位取决于 **Position unit** 参数。

**数据类型：** `single` | `double` | `fixed point`

### **IPEEn** — 启用阶段 1 初始位置估计（IPE）操作的标量

用于启用阶段 1 IPE 操作的信号端口。它支持以下输入之一：

- `1` — 启用模块运行阶段 1 IPE 操作，随后运行阶段 2 闭环脉振高频（PHF）注入操作。
- `0` — 启用模块跳过阶段 1，直接运行阶段 2 闭环 PHF 注入。

有关模块运行的两个阶段的详细信息，请参阅算法。

**数据类型：** `Boolean`
### 输出

### **Vαβ hf** — PHF 输出标量

脉振高频电压（在 *αβ* 参考坐标系中）输出，单位为标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **θest** — 估计转子位置标量

模块估计的转子位置，以弧度、度或标幺值表示。

单位取决于 **Position unit** 参数。

**数据类型：** `single` | `double` | `fixed point`

### **PosEn** — *θest* 端口状态标量

该端口提供以下输出之一：

- `1` — 表示模块已成功完成阶段 1 初始位置估计（IPE），且 **θest** 端口显示准确的转子位置。
- `0` — 表示阶段 1 IPE 操作仍在进行中（*θest* 端口输出尚不准确）或估计已失败。

**数据类型：** `single` | `double` | `fixed point`

### **Info** — 总线信号 总线

总线信号包含以下模块计算结果。

| 信号 | | | | 描述 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Sin *θest* 和 cos *θest* | | | | 估计转子位置的正弦和余弦 | - |
| *Id* 和 *Iq* | | | | 定子直轴和交轴电流 | A |
| Convergence | | | | *θest* 输出的当前采样值与前一采样值之间的差值。值越接近零表示 *θest* 越饱和。 | rad |
| Status | | | 0 | 模块未启用（**Enable** 输入端口为 0） | - |
| 1 | 模块正在寻找最佳可能的初始估计（阶段 1 部分 A） | - |
| 2 | 模块正在运行 PHF 方法（阶段 1 部分 B） | - |
| 3 | 模块正在运行 DP 方法（阶段 1 部分 C） | - |
| 4 | 模块已成功完成阶段 1，并已开始阶段 2 闭环 PHF 注入 | - |
| 5 | 阶段 1 部分 B 因估计转子位置误差过大而失败 | - |
## 参数
```yaml
parameters:
- name: Discrete step size (s)
  summary: 模块再次执行的采样时间 50e-6（默认）| 标量
  group: ''
- name: Input units
  summary: 模块输入的单位 Per-unit（默认）| SI
  group: ''
- name: Datatype
  summary: 输入和输出数据类型 single（默认）| double | fixed point
  group: ''
- name: 使用电机参数自动计算 PHF 参数
  summary: 自动计算 PHF 参数 off（默认）| on
  group: ''
- name: 使用电机参数自动计算 DP 参数
  summary: 自动计算 DP 参数 off（默认）| on
  group: ''
- name: Stator resistance (ohm)
  summary: 电机电阻 0.1458（默认）| 标量
  group: 电机参数
- name: Stator d-axis inductance (H)
  summary: 电机电感 0.00013016（默认）| 标量
  group: 电机参数
- name: Stator q-axis inductance (H)
  summary: 电机电感 0.00014098（默认）| 标量
  group: 电机参数
- name: Base voltage (V)
  summary: 额定电压 13.8564（默认）| 标量
  group: 电机参数
- name: Base current (A)
  summary: 额定电流 21.4286（默认）| 标量
  group: 电机参数
- name: Compute PHF parameters
  summary: 手动计算 PHF 参数 button
  group: 电机参数
- name: Compute DP parameters
  summary: 手动计算 DP 参数 button
  group: 电机参数
- name: PHF peak voltage (PU)
  summary: PHF 峰值电压 0.2（默认）| 标量
  group: PHF 参数
- name: PHF frequency (Hz)
  summary: PHF 电压频率 2000（默认）| 标量
  group: PHF 参数
- name: LP filter cutoff frequency (Hz)
  summary: PHF 低通滤波器截止频率 131.9037（默认）| 标量
  group: PHF 参数
- name: Select tuning parameters
  summary: 为手动整定选择控制参数 Controller gains（默认）| Time response variables
  group: PHF 参数
- name: Proportional gain
  summary: PHF 的 PI 控制器比例增益 1954.6647（默认）| 标量
  group: PHF 参数
- name: Integral gain
  summary: PHF 的 PI 控制器积分增益 7392.5303（默认）| 标量
  group: PHF 参数
- name: Expected settling time (s)
  summary: 估计位置的预期调节时间 0.66794（默认）| 标量
  group: PHF 参数
- name: Expected damping ratio
  summary: 模块输出 *θest* 的预期阻尼比 0.99（默认）| 标量
  group: PHF 参数
- name: Compute Control Parameters
  summary: 计算已禁用控制参数按钮
  group: PHF 参数
- name: Open loop duration (s)
  summary: 阶段 1 部分 A 期间开环 PHF 注入的持续时间 0.0066794（默认）| 标量
  group: PHF 参数
- name: Closed loop duration (s)
  summary: 阶段 1 部分 B 期间闭环 PHF 注入的持续时间 0.66794（默认）| 标量
  group: PHF 参数
- name: Idle time (s)
  summary: 算法步之间的持续时间 0.0066794（默认）| 标量
  group: PHF 参数
- name: Error threshold (rad)
  summary: '*θerr* 的最小误差阈值 4e-4（默认）| 标量'
  group: PHF 参数
- name: Pulse voltage (PU)
  summary: 注入脉冲的幅值 0.5（默认）| 标量
  group: DP Parameters
- name: Pulse duration (s)
  summary: 注入脉冲的持续时间 0.00066955（默认）| 标量
  group: DP Parameters
- name: Idle time (s)
  summary: 双脉冲注入期间两个脉冲之间的持续时间 50e-3（默认）| 标量
  group: DP Parameters
```

### **Discrete step size (s)** — 模块再次执行的采样时间 `50e-6`（默认）| 标量

两次连续模块执行实例之间的时间。

### **Input units** — 模块输入的单位 `Per-unit`（默认）| `SI`

模块输入的测量单位。

### **Datatype** — 输入和输出数据类型 `single`（默认）| `double` | `fixed point`

模块输入和输出的数据类型。

### **使用电机参数自动计算 PHF 参数** — 自动计算 PHF 参数 `off`（默认）| `on`

选择此参数可使模块使用指定的电机参数自动计算以下 PHF 参数（可在 **PHF Parameters** 选项卡中找到）：

- **PHF frequency (Hz)**
- **LP filter cutoff frequency (Hz)**
- **Proportional gain**
- **Integral gain**
- **Expected settling time (s)**
- **Expected damping ratio**
- **Open loop duration (s)**
- **Closed loop duration (s)**
- **Idle time (s)**

有关模块如何计算这些 PHF 参数的详细信息，请参阅 Compute PHF Parameters。

如果选择此参数，模块将禁用 **Compute PHF parameters** 按钮。

### **使用电机参数自动计算 DP 参数** — 自动计算 DP 参数 `off`（默认）| `on`

选择此参数可使模块使用指定的电机参数自动计算 DP 参数 **Pulse duration (s)**（可在 **DP Parameters** 选项卡中找到）。

有关模块如何计算 DP 参数的详细信息，请参阅 Compute DP Parameters。

如果选择此参数，模块将禁用 **Compute DP parameters** 按钮。

### 电机参数

### **Stator resistance (ohm)** — 电机电阻 `0.1458`（默认）| 标量

定子电阻（单位：欧姆）。

### **Stator d-axis inductance (H)** — 电机电感 `0.00013016`（默认）| 标量

定子沿 *d-q* 参考坐标系 *d* 轴方向的电感。

### **Stator q-axis inductance (H)** — 电机电感 `0.00014098`（默认）| 标量

定子沿 *d-q* 参考坐标系 *q* 轴方向的电感。

### **Base voltage (V)** — 额定电压 `13.8564`（默认）| 标量

电机额定电压（单位：伏特）。

### **Base current (A)** — 额定电流 `21.4286`（默认）| 标量

电机额定电流（单位：安培）。

### **Compute PHF parameters** — 手动计算 PHF 参数 `button`

单击此按钮时，模块将使用指定的电机参数手动计算以下 PHF 参数（可在 **PHF Parameters** 选项卡中找到）：

- **PHF frequency (Hz)**
- **LP filter cutoff frequency (Hz)**
- **Proportional gain**
- **Integral gain**
- **Expected settling time (s)**
- **Expected damping ratio**
- **Open loop duration (s)**
- **Closed loop duration (s)**
- **Idle time (s)**

有关模块如何计算这些 PHF 参数的详细信息，请参阅 Compute PHF Parameters。

#### 依赖关系

要启用此参数，请清除 **Compute PHF parameters automatically using motor parameters** 参数。

### **Compute DP parameters** — 手动计算 DP 参数 button

单击此按钮时，模块将使用指定的电机参数手动计算 DP 参数 **Pulse duration (s)**（可在 **PHF Parameters** 选项卡中找到）：

有关模块如何计算 DP 参数的详细信息，请参阅 Compute DP Parameters。

#### 依赖关系

要启用此参数，请清除 **Compute DP parameters automatically using motor parameters** 参数。

### PHF 参数

### **PHF peak voltage (PU)** — PHF 峰值电压 `0.2`（默认）| 标量

模块施加的 PHF 电压峰值幅度，单位为伏特。

### **PHF frequency (Hz)** — PHF 电压频率 `2000`（默认）| 标量

模块施加的 PHF 电压频率，单位为 Hz。

### **LP filter cutoff frequency (Hz)** — PHF 低通滤波器截止频率 `131.9037`（默认）| 标量

模块施加的 PHF 低通滤波器截止频率，单位为 Hz。

### **Select tuning parameters** — 为手动整定选择控制参数 `Controller gains`（默认）| `Time response variables`

选择要手动整定的控制参数。

- `Controller gains` — 选择此选项以启用以下控制参数：

  - **Proportional gain**
  - **Integral gain**

  **注意**

  选择 `Control gains` 会禁用时间响应变量。
- `Time response variables` — 选择此选项以启用以下控制参数：

  - **Expected settling time (s)**
  - **Expected damping ratio**

  **注意**

  选择 `Time response variables` 会禁用控制增益变量。

要查看整定后的参数对已禁用控制参数的影响，可以点击 **Compute Control Parameters** 按钮。有关详细信息，请参阅 Compute Control Parameters。

### **Proportional gain** — PHF 的 PI 控制器比例增益 `1954.6647`（默认）| 标量

该模块所施加 PHF 的比例 PI 控制器增益，*Kp*。

#### 依赖关系

要启用此参数，请将 **Select tuning parameters** 参数设置为 `Controller gains`。

### **Integral gain** — PHF 的 PI 控制器积分增益 `7392.5303`（默认）| 标量

该模块所施加 PHF 的积分 PI 控制器增益，*Ki*。

#### 依赖关系

要启用此参数，请将 **Select tuning parameters** 参数设置为 `Controller gains`。

### **Expected settling time (s)** — 估计位置的预期调节时间 `0.66794`（默认）| 标量

在阶段 1 部分 B 期间，模块输出 *θest* 达到饱和的预期时间。

#### 依赖关系

要启用此参数，请将 **Select tuning parameters** 参数设置为 `Time response variables`。

### **Expected damping ratio** — 模块输出 *θest* 的预期阻尼比 `0.99`（默认）| 标量

模块输出 *θest* 动态特性的预期阻尼比。

#### 依赖关系

要启用此参数，请将 **Select tuning parameters** 参数设置为 `Time response variables`。

### **Compute Control Parameters** — 计算已禁用控制参数按钮

计算 **Control Parameters** 部分中已禁用的控制参数。此参数可帮助您根据对已启用控制参数所做的编辑来更新已禁用的控制参数。下表描述了该模块用于计算已禁用控制参数的公式。

| **控制参数** | **表达式或值** | 备注 |
| --- | --- | --- |
| 比例增益，*kp* | ln(20000)G⋅Tsettling | 当您启用时间响应变量以进行手动编辑时，**Compute Control Parameters** 按钮会计算这些值。 |
| 积分增益，*ki* | G(kp)24δ2 |
| 预期调节时间 (s)，*Tsettling* | ln(20000)G⋅kp,when δ≤1ln(20000)G⋅kp(2δ(δ−δ2−1)),when δ>1 | 当您启用控制增益以进行手动编辑时，**Compute Control Parameters** 按钮会计算这些值。 |
| 预期阻尼比，*ẟ* | kp2Gki |

在表达式中：

- G=Vphf(Lq−Ld)4πfhLdLq
- *Vphf* 是注入的高频电压信号的峰值幅度值（单位为伏特）。
- *Ld* 和 *Lq* 是 *d* 轴和 *q* 轴定子电感（单位为亨利）。
- *fh* 是注入的高频电压的频率。

**注意**

此表中的表达式使用基于参考文献以及实验数据的元素和值。

### **Open loop duration (s)** — 阶段 1 部分 A 期间开环 PHF 注入的持续时间 `0.0066794`（默认）| 标量

阶段 1 部分 A 期间开环 PHF 注入的持续时间，单位为秒。

### **Closed loop duration (s)** — 阶段 1 部分 B 期间闭环 PHF 注入的持续时间 `0.66794`（默认）| 标量

阶段 1 部分 B 期间闭环 PHF 注入的持续时间，单位为秒。

### **Idle time (s)** — 算法步之间的持续时间 `0.0066794`（默认）| 标量

与 stage 1 part A 和 stage 1 part B 相关的算法中步与步之间的持续时间（以秒为单位），用于允许瞬态动态衰减。例如，该模块在每次 PHF 注入（开环或闭环）之间停止运行（持续该时长）。

### **Error threshold (rad)** — *θerr* 的最小误差阈值 `4e-4`（默认）| 标量

估计转子位置 *θest* 完成收敛时的最小误差值 *θerr*。

### DP Parameters

### **Pulse voltage (PU)** — 注入脉冲的幅值 `0.5`（默认）| 标量

注入脉冲的电压幅值，以伏特为单位。

### **Pulse duration (s)** — 注入脉冲的持续时间 `0.00066955`（默认）| 标量

注入脉冲的持续时间，以秒为单位。

### **Idle time (s)** — 双脉冲注入期间两个脉冲之间的持续时间 `50e-3`（默认）| 标量

双脉冲注入（stage 1 part C）期间两个脉冲之间的持续时间（以秒为单位）。
## 所属库

Motor Control Blockset / Sensorless Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

使用脉振高频（PHF）注入估计内置式 PMSM 的初始转子电位置

Pulsating High Frequency Observer 模块通过使用脉振高频（PHF）注入和双脉冲（DP）技术，估计静止内置式 PMSM 的初始位置（以电弧度为单位）。此外，当转子通过（低速）闭环控制运行时，该模块还会检测实时位置。

有关该模块算法的更多信息，请参阅 Algorithm。
