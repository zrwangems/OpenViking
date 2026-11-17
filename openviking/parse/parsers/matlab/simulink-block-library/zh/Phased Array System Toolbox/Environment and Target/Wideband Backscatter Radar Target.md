---
type: simulink-block
title: 'Wideband Backscatter Radar Target'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'widebandbackscatterradartarget'
documentation_source_path: 'ref/widebandbackscatterradartarget.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband Backscatter Radar Target

## 端口

### 输入

### **X** — 宽带入射非极化信号 *N*×*1* 复值向量 | *N*×*M* 复值矩阵

宽带入射非极化信号，指定为 *N*×*1* 复值向量或 *N*×*M* 复值矩阵。量 *N* 是信号采样数，*M* 是从目标反射的独立信号数。每一列包含一个要从目标反射的独立信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 入射信号方向 2×1 实值列向量 | 2×*M* 实值列矩阵

入射信号方向，指定为 2×1 实值列向量或 2×*M* 实值列矩阵。*M* 是从目标反射的信号数。`Ang` 的每一列以 `[AzimuthAngle;ElevationAngle]` 对的形式指定对应信号的入射方向。单位为度。`Ang` 的列数必须与 `X` 中独立信号的数量匹配。

**示例：** `[30;45]`

**数据类型：** `double`

### **Update** — 切换以更新 RCS `false` | `true`

切换以更新 RCS 起伏模型值，指定为 `false` 或 `true`。当 `Update` 为 `true` 时，RCS 值被更新。如果 `Update` 为 `false`，RCS 保持不变。

#### 依赖关系

要启用此端口，请将 **Fluctuation model** 下拉菜单设置为 `Swerling1`、`Swerling2`、`Swerling3` 或 `Swerling4`。
### 输出

### **Port\_1** — 窄带反射信号 1×*M* 复值向量 | *N*×*M* 复值矩阵

宽带非极化信号，指定为 1×*M* 复值向量或 *N*×*M* 复值矩阵。每一列包含一个从目标反射的独立信号。

量 *N* 是信号采样数，*M* 是从目标反射的信号数。每一列对应一个不同的反射角度。

输出端口包含在当前输入时间帧内到达信号目的地的信号采样。当从源到目的地的传播时间超过当前时间帧持续时间时，输出不包含当前时间帧输入的所有贡献。

## 参数

### **Backscatter pattern frequency vector (Hz)** — 宽带后向散射方向图频率 `[0,1e20]`（默认）| 严格递增的正值实值行向量

指定 RCS 矩阵中使用的频率。此向量的元素必须严格递增。目标在此频率范围之外没有响应。频率是相对于物理频带定义的，而不是基带。频率单位为 Hz。

**数据类型：** `double`

### **Azimuth angles (deg)** — 方位角 `[-180:180]`（默认）| 1×*P* 实值行向量 | *P*×1 实值列向量

用于定义由 **RCS pattern (m^2)** 参数指定的矩阵每一列的角度坐标的方位角。将方位角指定为长度为 *P* 的向量。*P* 必须大于二。角度单位为度。

**示例：** `[-45:0.1:45]`

**数据类型：** `double`

### **Elevation angles (deg)** — 俯仰角 `[-90:90]`（默认）| 1×*Q* 实值行向量 | *Q*×1 实值列向量

用于定义由 **RCS pattern (m^2)** 参数指定的矩阵每一行的角度坐标的俯仰角。将俯仰角指定为长度为 *Q* 的向量。*Q* 必须大于二。角度单位为度。

**示例：** `[-30:0.1:30]`

**数据类型：** `double`

### **RCS pattern (m^2)** — 雷达散射截面方向图 `ones(181,361)`（默认）| *Q*×*P* 实值矩阵 | *Q*×*P*×*K* 实值数组 | 1×*P*×*K* 实值数组 | *K*×*P* 实值矩阵

雷达散射截面方向图，指定为实值矩阵或数组。

| 维度 | 应用 |
| --- | --- |
| *Q*×*P* 矩阵 | 将 RCS 值矩阵指定为 *Q* 个仰角和 *P* 个方位角的函数。所有频率使用相同的 RCS 矩阵。 |
| *Q*×*P*×*K* 数组 | 将 RCS 方向图数组指定为 *Q* 个仰角、*P* 个方位角和 *K* 个频率的函数。如果 K = 1，则 RCS 方向图等效于 *Q*×*P* 矩阵。 |
| 1×*P*×*K* 数组 | 将 RCS 值矩阵指定为 *P* 个方位角和 *K* 个频率的函数。这些维度格式适用于只有一个仰角的情况。 |
| *K*×*P* 矩阵 |

- *Q* 是由 **Elevation angles (deg)** 参数指定的向量的长度。
- *P* 是由 **Azimuth angles (deg)** 参数指定的向量的长度。
- *K* 是由 **Backscatter pattern frequency vector (Hz)** 参数指定的频率数量。

您可以通过将 *L* 个方向图放入元胞数组来为 *L* 个目标指定方向图。所有方向图必须具有相同的维度。*L* 的值必须与传递到模块输入端的信号的列维度匹配。但是，您可以使用一个方向图来建模 *L* 个目标。

RCS 的单位为平方米。

**示例：** `[1,2;2,1]`

**数据类型：** `double`

### **Fluctuation model** — 目标起伏模型 `Nonfluctuating`（默认）| `Swerling1` | `Swerling2` | `Swerling3` | `Swerling4`

目标起伏模型，指定为 `Nonfluctuating`、`Swerling1`、`Swerling2`、`Swerling3` 或 `Swerling4`。如果将此参数设置为 `Nonfluctuating` 以外的值，则必须将 `true` 或 `false` 传递到 **Update** `Update` 端口。

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Operating frequency (Hz)** — 信号载波频率 `300.0e6`（默认）| 正实值标量

信号载波频率，指定为正实值标量。单位为赫兹。

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Number of subbands** — 处理子带数量 `64`（默认）| 正整数

处理子带数量，指定为正整数。

**示例：** `128`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间编译，但通常运行
更快。

在开发和调优模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比
解释执行运行得更快。您可以重复执行而无需重新编译，但如果
更改任何模块参数，模块会在
执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用
**Simulate using** 指定的模块模式会覆盖仿真模式。

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

**在 R2016b 中引入**

## 描述

来自雷达目标的宽带信号后向散射

Wideband Backscatter Radar Target 模块对来自雷达目标的非极化宽带电磁信号的单站反射进行建模。目标雷达截面积（RCS）模型包括四种 Swerling 目标起伏模型和一种非起伏模型。您可以通过指定多个雷达截面积 RCS 矩阵来同时建模多个目标。
