---
type: simulink-block
title: 'Wideband LOS Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'widebandloschannelblock'
documentation_source_path: 'ref/widebandloschannelblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband LOS Channel

## 端口
```yaml
ports:
- name: X
  summary: 辐射信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵
  direction: input
  data_types: double
- name: Pos1
  summary: 信号源位置 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Pos2
  summary: 信号目的地 3×1 实值列向量 | 3×*N* 实值矩阵
  direction: input
  data_types: double
- name: Vel1
  summary: 源速度 3×1 实值列向量 | 3×*N* 实值矩阵 | *N*×3 实值矩阵
  direction: input
  data_types: double
- name: Vel2
  summary: 目的地速度 3×1 实值列向量 | 3×*N* 实值矩阵 | *N*×3 实值矩阵
  direction: input
  data_types: double
- name: Port_1
  summary: 传播信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵
  direction: output
  data_types: double
```

### 输入

### **X** — 辐射信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵

辐射信号，指定为复值 *M*×1 向量或复值 *M*×*N* 矩阵。*M* 是信号的长度，*N* 是阵列元素的数量（或支持子阵列时的子阵列数量）。

**X 的维度**

| 维度 | 信号 |
| --- | --- |
| *M*×1 向量 | 同一信号从所有阵列元素（或支持子阵列时的所有子阵列）辐射。 |
| `M-by-N matrix` | 每一列对应于相应阵列元素（或支持子阵列时的相应子阵列）辐射的信号。 |

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Pos1** — 信号源位置 3×1 实值列向量 | 3×*N* 实值矩阵

信号源位置，指定为实值 3×1 列向量或 3×*N* 实值矩阵。量 *N* 是源位置的数量。源位置的示例包括发射器、阵列元素位置或子阵列位置。位置单位为米。

如果 **Pos1** 是列向量，其形式为 `[x;y;z]`。如果 **Pos1** 是矩阵，每一列指定不同的信号源，其形式为 `[x;y;z]`。

如果 **Pos1** 有多列，**Pos2** 只能有一列。不能同时将 **Pos1** 和 **Pos2** 指定为矩阵。

**示例：** `[1000;100;500]`

**数据类型：** `double`

### **Pos2** — 信号目的地 3×1 实值列向量 | 3×*N* 实值矩阵

信号目的地位置，指定为实值 3×1 列向量或 3×*N* 实值矩阵。量 *N* 是目的地的数量，例如阵列元素位置或子阵列位置。位置单位为米。

如果 **Pos2** 是列向量，其形式为 `[x;y;z]`。如果 **Pos2** 是矩阵，每一列指定不同的信号目的地。每一行的形式为 `[x;y;z]`。位置单位为米。

如果 **Pos2** 有多列，**Pos1** 只能有一列。不能同时将 **Pos2** 和 **Pos1** 指定为矩阵。

**示例：** `[1000;100;500]`

**数据类型：** `double`

### **Vel1** — 源速度 3×1 实值列向量 | 3×*N* 实值矩阵 | *N*×3 实值矩阵

源速度，指定为与 **Pos1** 大小相同的实值向量或矩阵。

**示例：** `[20;20;50]`

**数据类型：** `double`

### **Vel2** — 目的地速度 3×1 实值列向量 | 3×*N* 实值矩阵 | *N*×3 实值矩阵

目的地速度，指定为与 **Pos2** 大小相同的实值向量或矩阵。

**示例：** `[0;0;100]`

**数据类型：** `double`
### 输出

### **Port\_1** — 传播信号 复值 *M*×1 向量 | 复值 *M*×*N* 矩阵

传播信号，返回为复值 *M*×1 向量或复值 *M*×*N* 矩阵。**Port\_1** 的大小与输入端口 **X** 相同。*M* 是信号的长度，*N* 是信号的数量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: ''
- name: Signal carrier frequency (Hz)
  summary: 信号载波频率 3e8（默认）| 正标量
  group: ''
- name: Number of subbands
  summary: 处理子带数量 64（默认）| 正整数
  group: ''
- name: Specify atmospheric parameters
  summary: 启用大气衰减模型 关（默认）| 开
  group: ''
- name: Temperature (degrees Celsius)
  summary: 环境温度 15 | 实值标量
  group: ''
- name: Dry air pressure (Pa)
  summary: 大气干空气压强 101325 | 正实值标量
  group: ''
- name: Water vapour density (g/m^3)
  summary: 大气水蒸气密度 7.5 | 正实值标量
  group: ''
- name: Liquid water density (g/m^3)
  summary: 液态水密度 0 | 非负实值标量
  group: ''
- name: Rain rate (mm/hr)
  summary: 降雨率 0 | 非负实值标量
  group: ''
- name: Perform two-way propagation
  summary: 启用双向传播 关（默认）| 开
  group: ''
- name: Inherit sample rate
  summary: 从上游模块继承采样率 开（默认）| 关
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认）| 正实值标量
  group: ''
- name: Maximum one-way propagation distance (m)
  summary: 最大单向传播距离 10e3（默认）| 正实值标量
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 信号载波频率 `3e8`（默认）| 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **Number of subbands** — 处理子带数量 `64`（默认）| 正整数

处理子带数量，指定为正整数。

**示例：** `128`

### **Specify atmospheric parameters** — 启用大气衰减模型 关（默认）| 开

选中此复选框以启用大气衰减建模。

### **Temperature (degrees Celsius)** — 环境温度 `15` | 实值标量

将环境大气温度指定为实值标量。单位为摄氏度。

#### 依赖关系

当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

### **Dry air pressure (Pa)** — 大气干空气压强 `101325` | 正实值标量

将大气干空气压强指定为正实值标量。单位为帕斯卡（Pa）。此属性的值 101325 对应一个标准大气压。

#### 依赖关系

当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

### **Water vapour density (g/m^3)** — 大气水蒸气密度 `7.5` | 正实值标量

将大气水蒸气密度指定为正实值标量。单位为 gm/m3。

#### 依赖关系

当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

### **Liquid water density (g/m^3)** — 液态水密度 `0` | 非负实值标量

将雾或云的液态水密度指定为非负实值标量。单位为 gm/m3。液态水密度的典型值为：中雾 0.05，浓雾 0.5。

#### 依赖关系

当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

### **Rain rate (mm/hr)** — 降雨率 `0` | 非负实值标量

将降雨率指定为非负实值标量。单位为 mm/hour。

#### 依赖关系

当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

### **Perform two-way propagation** — 启用双向传播 关（默认）| 开

选中此复选框以执行起点与终点之间的往返传播。否则，该模块执行从起点到终点的单向传播。

### **Inherit sample rate** — 从上游模块继承采样率 开（默认）| 关

选中此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Maximum one-way propagation distance (m)** — 最大单向传播距离 `10e3`（默认）| 正实值标量

将信号起点与终点之间的最大距离指定为正标量。单位为米。传播超过此距离的任何信号幅度将被设置为零。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行
更快。

当您开发和调整模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比在
解释执行中运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，则模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

宽带视距传播信道

Wideband LOS Channel 模块通过视距（LOS）信道将信号从空间中的一个点传播到多个点，或从多个点传播回一个点。该模块对传播时间、自由空间传播损耗、多普勒频移以及大气和天气损耗进行建模。该模块假设传播速度远大于物体速度，在这种情况下 stop-and-hop 模型是有效的。

当在 LOS 信道中将信号传播到物体并返回时，您可以使用单个
模块来计算双向 LOS 信道传播延迟，或使用两个模块来执行
每个方向上的单向传播延迟。由于 LOS 信道传播延迟
不一定是采样间隔的整数倍，因此当您使用双向传播模块时，以采样数表示的总往返延迟可能
与使用两个单向传播模块时的以采样数表示的延迟不同。因此，
建议在可能的情况下使用单个双向传播
模块。
