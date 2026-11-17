---
type: simulink-block
title: 'Wideband Two-Ray Channel'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'widebandtworaychannel'
documentation_source_path: 'ref/widebandtworaychannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband Two-Ray Channel

## 端口

### 输入

### **X** — 宽带输入信号 *M*×*N* 复值矩阵 | *M*×*2N* 复值矩阵

- 宽带非极化标量信号，指定为

  - *M*×*N*
    复值矩阵。量
    *M* 是信号中的样本数，*N* 是
    两径信道数。每个信道对应一个
    源-目的地对。每一列包含一个
    相同的信号，该信号沿
    视距路径和反射路径传播。
  - *M*×*2N*
    复值矩阵。量
    *M* 是信号的样本数，*N* 是
    两径信道数。每个信道对应一个
    源-目的地对。每对相邻的
    列表示不同的信道。在
    每一对中，第一列表示沿
    视距路径传播的信号，第二列表示沿
    反射路径传播的信号。

量 *M* 是信号的样本数，*N* 是两径信道数。每个
信道对应一个源-目的地对。

输入矩阵第一维的大小可以变化，以
模拟变化的信号长度。例如，在脉冲
波形具有可变脉冲重复频率的情况下，大小可能会发生变化。

**示例：** `[1,1;j,1;0.5,0]`

**数据类型：** `double`
**复数支持：** 是

### **Pos1** — 信号源位置 3×1 实值列向量 | 3×*N* 实值矩阵

信号源的位置，指定为 3×1 实值
列向量或 3×*N* 实值矩阵。量
*N* 是两径信道数。如果 **Pos1** 是
列向量，其形式为 `[x;y;z]`。如果 **Pos1** 是
矩阵，每一列指定不同的信号源，其
形式为 `[x;y;z]`。位置单位为米。

**Pos1** 和 **Pos2** 不能
同时指定为矩阵——至少一个必须是 3×1
列向量。

**示例：** `[1000;100;500]`

**数据类型：** `double`

### **Pos2** — 信号目的地位置 3×1 实值列向量 | 3×*N* 实值矩阵

信号源的位置，指定为 3×1 实值
列向量或 3×*N* 实值矩阵。量
*N* 是两径信道数。如果 **Pos2** 是
列向量，其形式为 `[x;y;z]`。如果 **Pos2** 是
矩阵，每一列指定不同的信号源，其
形式为 `[x;y;z]`。位置单位为米。

**Pos1** 和 **Pos2** 不能
同时指定为矩阵——至少一个必须是 3×1
列向量。

**示例：** `[-100;300;50]`

**数据类型：** `double`

### **Vel1** — 信号源速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号源速度，指定为 3×1 实值
列向量或 3×*N* 实值矩阵。
**Vel1** 的维度必须与 **Pos1** 的维度
匹配。如果 **Vel1** 是列
向量，其形式为 `[Vx;Vy;Vz]`。如果 **Vel1** 是
3×*N* 矩阵，每一列指定不同的
源速度，其形式为 `[Vx;Vy;Vz]`。速度
单位为米每秒。

**示例：** `[-10;3;5]`

**数据类型：** `double`

### **Vel2** — 信号目的地速度 3×1 实值列向量 | 3×*N* 实值矩阵

信号源速度，指定为 3×1 实值
列向量或 3×*N* 实值矩阵。
**Vel2** 的维度必须与 **Pos2** 的维度
匹配。如果 **Vel2** 是列
向量，其形式为 `[Vx;Vy;Vz]`。如果 **Vel2** 是
3×*N* 矩阵，每一列指定不同的
源速度，其形式为 `[Vx;Vy;Vz]`。速度
单位为米每秒。

**示例：** `[-1000;300;550]`

**数据类型：** `double`
### 输出

### **Out** — 传播信号 *M*×*N* 复值矩阵 | *M*×*2N* 复值矩阵

- *M*×*N* 复值矩阵。要返回此格式，请将 `CombinedRaysOutput` 属性设置为 `true`。每列包含来自视距路径和反射路径的相干合并信号。
- *M*×*2N* 复值矩阵。要返回此格式，请将 `CombinedRaysOutput` 属性设置为 `false`。矩阵的交替列包含来自视距路径和反射路径的信号。

输出 **Out** 包含在当前输入时间帧内到达信号目的地的信号采样。当信号从起点传播到目的地所需时间超过当前时间帧时，输出可能不包含当前时间帧输入的所有贡献。剩余输出将出现在模块的下一次执行中。

## 参数

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 信号载波频率 `300e6`（默认）| 正实值标量

信号载波频率，指定为正实值标量。单位为赫兹。

**数据类型：** `double`

### **Number of subbands** — 处理子带数量 `64`（默认）| 正整数

处理子带数量，指定为正整数。

**示例：** `128`

### **Specify atmospheric parameters** — 启用大气衰减模型 off（默认）| on

选择此参数以启用由大气气体、雨、雾或云引起的信号衰减。选择此参数后，对话框中会出现 **Temperature (degrees Celsius)**、**Dry air pressure (Pa)**、**Water vapour density (g/m^3)**、**Liquid water density (g/m^3)** 和 **Rain rate (mm/hr)** 参数。

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

**数据类型：** `double`

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

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Ground reflection coefficient** — 地面反射系数 -1（默认）| 复值标量 | 复值 1×*N* 行向量

反射点处场的地面反射系数，指定为复值标量或复值 1×*N* 行向量。系数的绝对值小于或等于一。量 *N* 是两径信道的数量。单位无量纲。

**示例：** `-0.5`

### **Combine two rays at output** — 在输出端合并两条射线的选项 on（默认）| off

选择此参数以在信道输出端合并两条射线。相干地合并两条射线会将视距传播信号和反射路径信号相加，形成输出信号。当您不需要在仿真中包含天线或阵列的方向增益时，可以使用此模式。

**示例：** on

### **Maximum one-way propagation distance (m)** — 最大单向传播距离 `10.0e3`（默认）| 正实值标量

最大单向传播距离，指定为实值正标量。单位为米。任何传播距离超过最大单向距离的信号都会被忽略。最大距离必须大于或等于最大的位置到位置距离。

**示例：** `5000.0`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

宽带两径信道环境

宽带两径信道模块通过直射路径和地面反射路径，将宽带信号从空间中的一点传播到多个点，或从多个点传播回一点。该模块通过以下方式传播宽带信号：(1) 将其分解为子带，(2) 独立传播子带，(3) 重新组合传播后的子带。该模块对传播时间、传播损耗和多普勒频移进行建模。该模块假设传播速度远大于物体速度，在这种情况下停跳模型是有效的。
