---
type: simulink-block
title: 'LOS Channel'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'loschannel'
documentation_source_path: 'ref/loschannel.html'
language: zh-CN
chinese_source: worker-translation
---

# LOS Channel

## 端口

### 输入

### **X** — 窄带信号 *M* 元复值列向量、*M*×*N* 复值矩阵。

窄带信号，指定为 *M* 元复值列向量或 *M*×*N* 复值矩阵。量 *M* 是信号的采样值数量，*N* 是要传播的信号数量。当您指定 *N* 个信号时，需要指定 *N* 个信号源或 *N* 个信号目的地。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

### **Pos1** — 信号源 3×1 实值列向量 | 3×*N* 实值矩阵

信号源，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于信号输入端口 `X` 中指定的维度。如果 `Pos1` 是列向量，则其形式为 `[x; y; z]`。如果 `Pos1` 是矩阵，则每一列指定不同的信号源，形式为 `[x; y; z]`。`Pos1` 和 `Pos2` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Pos2** — 信号目的地 3×1 实值列向量 | 3×*N* 实值矩阵

信号目的地，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于输入端口 `X` 中信号指定的维度。如果 `Pos2` 是列向量，则其形式为 `[x; y; z]`。如果 `Pos2` 是矩阵，则每一列指定不同的信号源，形式为 `[x; y; z]`。`Pos2` 和 `Pos1` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Vel1** — 信号源速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号源速度，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于端口 `X` 中信号指定的维度。如果 `Vel1` 是列向量，则其形式为 `[Vx; Vy; zV]`。如果 `Vel1` 是矩阵，则每一列指定不同的信号源，形式为 `[Vx; Vy; Vz]`。`Vel1` 的维度必须与 `Pos1` 的维度一致。`Vel1` 和 `Vel2` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`

### **Vel2** — 信号目的地速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号目的地速度，指定为 3×1 实值列向量或 3×*N* 实值矩阵。量 *N* 是传播信号的数量，等于端口 `X` 中信号指定的维度。如果 `Vel2` 是列向量，则其形式为 `[Vx; Vy; zV]`。如果 `Vel2` 是矩阵，则每一列指定不同的信号源，形式为 `[Vx; Vy; Vz]`。`Vel2` 的维度必须与 `Pos2` 的维度一致。`Vel2` 和 `Vel1` 不能同时指定为矩阵——至少一个必须是 3×1 列向量。位置单位为米。

**数据类型：** `double`
### 输出

### **Port\_1** — 传播的窄带信号 *M* 元复值列向量，*M*×*N* 复值矩阵。

传播信号，返回为 *M* 元复值列向量、*M*×*N* 复值矩阵。`Y` 将与 `X` 具有相同的维度。

输出 `Y` 包含在当前时间帧内到达信号目的地的信号样本。当前时间帧定义为当前输入所跨越的时间。每当信号从起点传播到目的地所需时间超过当前时间帧时，输出不包含当前时间帧输入的贡献。

## 参数

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 信号载波频率 `3e8`（默认）| 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **Specify atmospheric parameters** — 启用大气衰减模型 off（默认）| on

选择此参数以启用由大气气体、雨、雾或云引起的信号衰减。当您选择此参数时，**Temperature (degrees Celsius)**、**Dry air pressure (Pa)**、**Water vapour density (g/m^3)**、**Liquid water density (g/m^3)** 和 **Rain rate (mm/hr)** 参数将出现在对话框中。

**数据类型：** `Boolean`

### **Temperature (degrees Celsius)** — 环境温度 `15`（默认）| 实值标量

环境温度，指定为实值标量。单位为摄氏度。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Dry air pressure (Pa)** — 大气干空气压力 `101.325e3`（默认）| 正实值标量

大气干空气压力，指定为正实值标量。单位为帕斯卡（Pa）。此参数的默认值对应一个标准大气压。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Water vapour density (g/m^3)** — 大气水蒸气密度 `7.5`（默认）| 正实值标量

大气水蒸气密度，指定为正实值标量。单位为 g/m3。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `datetime`

### **Liquid water density (g/m^3)** — 液态水密度 `0.0`（默认）| 非负实值标量

雾或云的液态水密度，指定为非负实值标量。单位为 g/m3。液态水密度的典型值为：中雾 0.05，浓雾 0.5。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Rain rate (mm/hr)** — 降雨率 `0.0`（默认）| 非负实值标量

降雨率，指定为非负实值标量。单位为 mm/hr。

#### 依赖关系

要启用此参数，请选中 **Specify atmospheric parameters** 复选框。

**数据类型：** `double`

### **Perform two-way propagation** — 启用双向传播 `off`（默认）| `on`

选中此复选框以执行起点与目的地之间的往返传播。否则，该模块执行从起点到目的地的单向传播。

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号的采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Maximum one-way propagation distance (m)** — 最大单向传播距离 `10e3`（默认）| 正实值标量

将信号源与目的地之间的最大距离指定为正标量。单位为米。任何传播距离超过此距离的信号的幅度将被设置为零。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

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

窄带视距传播信道

LOS Channel 模块通过视距（LOS）信道将信号从空间中的一点传播到空间中的另一点。该模块还可以将信号从一点传播到多点，或从多点传播回一点。该模块对传播时间、自由空间传播损耗、多普勒频移以及大气和天气损耗进行建模。该模块假设传播速度远大于物体速度，在这种情况下停跳模型是有效的。

当在 LOS 信道中将信号传播到物体并返回时，您可以使用单个模块来计算双向 LOS 信道传播延迟，或使用两个模块在每个方向上执行两个单向传播延迟。由于 LOS 信道传播延迟不一定是采样间隔的整数倍，因此当您使用双向传播模块时，以采样为单位的往返总延迟可能与使用两个单向传播模块时的以采样为单位的延迟不同。因此，建议在可能的情况下使用单个双向传播模块。
