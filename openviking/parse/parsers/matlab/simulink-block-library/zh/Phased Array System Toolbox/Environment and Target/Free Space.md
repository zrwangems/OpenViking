---
type: simulink-block
title: 'Free Space'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'freespace'
documentation_source_path: 'ref/freespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Free Space

## 端口
```yaml
ports:
- name: X
  summary: 窄带信号 *M* 元复值列向量、*M*×*N* 复值矩阵。
  direction: input
- name: Pos1
  summary: 信号起点 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Pos2
  summary: 信号终点 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Vel1
  summary: 信号起点速度 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Vel2
  summary: 信号终点速度 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Port_1
  summary: 传播后的窄带信号 *M* 元复值列向量、*M*×*N* 复值矩阵。
  direction: output
```

### 输入

### **X** — 窄带信号 *M* 元复值列向量、*M*×*N* 复值矩阵。

窄带信号，指定为 *M* 元复值列向量或 *M*×*N* 复值矩阵。量 *M* 是信号的采样值数量，*N* 是要传播的信号数量。当您指定 *N* 个信号时，需要指定 *N* 个信号起点或 *N* 个信号终点。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

### **Pos1** — 信号起点 3×1 实值列向量 | 3×*N* 实值矩阵

信号起点，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于输入到端口 `X` 的信号中指定的维度。如果 `Pos1` 是列向量，其形式为 `[x; y; z]`。如果 `Pos1` 是矩阵，每一列指定不同的信号起点，形式为 `[x; y; z]`。`Pos1` 和 `Pos2` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Pos2** — 信号终点 3×1 实值列向量 | 3×*N* 实值矩阵

信号终点，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于输入到端口 `X` 的信号中指定的维度。如果 `Pos2` 是列向量，其形式为 `[x; y; z]`。如果 `Pos2` 是矩阵，每一列指定不同的信号起点，形式为 `[x; y; z]`。`Pos2` 和 `Pos1` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Vel1** — 信号起点速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号起点速度，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于输入到端口 `X` 的信号中指定的维度。如果 `Vel1` 是列向量，其形式为 `[Vx; Vy; zV]`。如果 `Vel1` 是矩阵，每一列指定不同的信号起点，形式为 `[Vx; Vy; Vz]`。`Vel1` 和 `Vel2` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Vel2** — 信号终点速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号终点速度，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于输入到端口 `X` 的信号中指定的维度。如果 `Vel2` 是列向量，其形式为 `[Vx; Vy; zV]`。如果 `Vel2` 是矩阵，每一列指定不同的信号起点，形式为 `[Vx; Vy; Vz]`。`Vel2` 和 `Vel1` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`
### 输出

### **Port\_1** — 传播后的窄带信号 *M* 元复值列向量、*M*×*N* 复值矩阵。

传播后的信号，返回为 *M* 元复值列向量、*M*×*N* 复值矩阵。

如果 `X` 是列向量或矩阵，`Y` 也是具有相同维度的列向量或矩阵。

输出 `Y` 包含在当前时间帧内到达信号终点的信号采样。当前时间帧定义为当前输入所跨越的时间。每当信号从起点传播到终点所需时间超过当前时间帧时，输出不包含当前时间帧输入的贡献。
## 参数
```yaml
parameters:
- name: Propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: ''
- name: Signal carrier frequency (Hz)
  summary: 信号载波频率 3e8（默认）| 正标量
  group: ''
- name: Perform two-way propagation
  summary: 执行双向传播 off（默认）| on
  group: ''
- name: Inherit sample rate
  summary: 从上游模块继承采样率 on（默认）| off
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认）| 正实值标量
  group: ''
- name: Maximum one-way propagation distance (m)
  summary: 最大单向传播距离 10e3（默认）
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
```

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 信号载波频率 `3e8`（默认）| 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **Perform two-way propagation** — 执行双向传播 off（默认）| on

选中此复选框可执行起点与终点之间的往返传播。否则，该模块执行从起点到终点的单向传播。

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数可从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Maximum one-way propagation distance (m)** — 最大单向传播距离 `10e3`（默认）

起点与终点之间的最大距离，以米为单位，指定为正标量。任何传播超过此距离的信号的幅度将被设置为零。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

自由空间环境

自由空间信道模块在空间中从一点向另一点传播信号。该模块对传播时间、自由空间传播损耗和多普勒频移进行建模。该模块假设传播速度远大于目标或阵列速度，在这种情况下停走模型是有效的。

当在自由空间中将信号传播到物体并返回时，您可以选择使用单个模块来计算双程自由空间传播延迟，或者使用两个模块在每个方向上执行单程传播延迟。由于自由空间传播延迟不一定是采样间隔的整数倍，因此当您使用双程传播模块时，以采样点为单位的总往返延迟可能与使用两个单程传播模块时的以采样点为单位的延迟不同。因此，建议在可能的情况下使用单个双程传播模块。
