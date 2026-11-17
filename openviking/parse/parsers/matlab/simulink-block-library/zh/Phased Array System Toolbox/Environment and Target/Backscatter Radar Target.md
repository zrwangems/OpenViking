---
type: simulink-block
title: 'Backscatter Radar Target'
family: 'environment-and-target'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'backscatterradartarget'
documentation_source_path: 'ref/backscatterradartarget.html'
language: zh-CN
chinese_source: worker-translation
---

# Backscatter Radar Target

## 端口

### 输入

### **X** — 窄带信号 *N*×*1* 复数值向量 | *N*×*M* 复数值矩阵

窄带非极化信号，指定为 *N*×*1* 复数值向量或 *N*×*M* 复数值矩阵。量 *N* 是信号样本数，*M* 是从目标反射的信号数。每一列对应于以不同反射角入射的独立信号。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`

### **Ang** — 入射信号方向 2×1 实数值列向量 | 2×*M* 实数值列矩阵

入射信号方向，指定为 2×1 实数值列向量或 2×*M* 实数值列矩阵。*M* 是从目标反射的信号数。`Ang` 的每一列以 `[AzimuthAngle;ElevationAngle]` 对的形式指定对应信号的入射方向。单位是 degrees。`Ang` 中的列数必须与 `X` 中的独立信号数匹配。

**示例：** `[30;45]`

**数据类型：** `double`

### **Update** — 用于更新 RCS 的开关 `false` | `true`

用于更新 RCS 起伏模型值的开关，指定为 `false` 或 `true`。当 `Update` 为 `true` 时，RCS 值会更新。如果 `Update` 为 `false`，则 RCS 保持不变。

#### 依赖关系

要启用此端口，请将 **起伏模型** 下拉菜单设置为 `Swerling1`、`Swerling2`、`Swerling3` 或 `Swerling4`。

### 输出

### **Port\_1** — 窄带反射信号 1×*M* 复数值向量 | *N*×*M* 复数值矩阵

窄带非极化信号，指定为 1×*M* 复数值向量或 *N*×*M* 复数值矩阵。每一列包含从目标反射的独立信号。

量 *N* 是信号样本数，*M* 是从目标反射的信号数。每一列对应于不同的反射角。

输出端口包含在当前输入时间帧内到达信号目的地的信号样本。当从源到目的地的传播时间超过当前时间帧持续时间时，输出不包含当前时间帧输入的所有贡献。

## 参数

### **方位角 (deg)** — 方位角 `[-180:180]` (默认) | 1×*P* 实数值行向量 | *P*×1 实数值列向量

指定用于定义 **RCS 方向图 (m^2)** 参数角坐标的方位角。将方位角指定为长度为 *P* 的向量。单位是 degrees。*P* 必须大于二。此参数确定散射截面方向图任一元素的入射方位到达角。

**数据类型：** `double`

### **俯仰角 (deg)** — 俯仰角 `[-90:90]` (默认) | 1×*Q* 实数值行向量 | *Q*×1 实数值列向量

指定用于定义 **RCS 方向图 (m^2)** 参数角坐标的俯仰角。将俯仰角指定为长度为 *Q* 的向量。单位是 degrees。*Q* 必须大于二。此参数确定散射截面方向图任一元素的入射俯仰到达角。

### **RCS 方向图 (m^2)** — 雷达散射截面方向图 `ones(181,361)` (默认) | *Q*×*P* 实数值矩阵 | *Q*×*P*×*M* 实数值数组 | 1×*P* 实数值向量 | *M*×*P* 实数值矩阵

雷达散射截面方向图，指定为 *Q*×*P* 实数值矩阵或 *Q*×*P*×*M* 实数值数组。

- *Q* 是 **俯仰角 (deg)** 参数中向量的长度。
- *P* 是 **方位角 (deg)** 参数中向量的长度。
- *M* 是目标方向图的数量。方向图的数量对应于传递到输入端口 `X` 的信号数量。然而，您可以使用单个方向图来对从单个目标反射的多个信号进行建模。

然而，您可以使用单个方向图来对从单个目标反射的多个信号进行建模。方向图单位是 square-meters。

方向图单位是 square-meters。

### **起伏模型** — 目标起伏模型 `Nonfluctuating` (默认) | `Swerling1` | `Swerling2` | `Swerling3` | `Swerling4`

将目标的统计模型指定为 `Nonfluctuating`、`Swerling1`、`Swerling2`、`Swerling3` 或 `Swerling4`。当您将此参数设置为 `Nonfluctuating` 以外的值时，您随后使用 `Update` 输入端口设置雷达散射截面参数。

### **传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。单位是 meters per second。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率 (Hz)** — 工作频率 `3e8` (默认) | 正标量

从目标反射的信号的载波频率，指定为正标量。单位是 hertz。

**数据类型：** `double`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，随后可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

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
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

反向散射雷达目标

Backscatter Radar Target 模块对来自目标的非极化电磁信号的单站雷达反射进行建模。目标模型包括所有四种 Swerling 目标起伏模型和非起伏模型。您可以通过指定多个雷达散射截面 (RCS) 矩阵来同时建模多个目标。
