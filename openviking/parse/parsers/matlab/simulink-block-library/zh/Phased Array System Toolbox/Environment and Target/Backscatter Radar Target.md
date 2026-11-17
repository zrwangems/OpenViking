---
type: simulink-block
title: 'Backscatter Radar Target'
family: 'phased'
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

### **X** — 窄带信号 *N*×*1* 复值向量 | *N*×*M* 复值矩阵

窄带非极化信号，指定为
*N*×*1* 复值向量
或 *N*×*M* 复值
矩阵。量 *N* 是信号
样本数，*M* 是从目标反射的
信号数。每一列对应于以不同反射角度
入射的独立信号。

输入矩阵第一维的大小可以变化，以
模拟变化的信号长度。例如，在脉冲
重复频率可变的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `double`

### **Ang** — 入射信号方向 2×1 实值列向量 | 2×*M* 实值列矩阵

入射信号方向，指定为 2×1 实值列向量或
2×*M* 实值列矩阵。
*M* 是从目标反射的
信号数。`Ang` 的每一列以
`[AzimuthAngle;ElevationAngle]` 对的形式指定对应信号的入射
方向。单位为
度。`Ang` 中的列数必须与 `X` 中独立信号的数量
匹配。

**示例：** `[30;45]`

**数据类型：** `double`

### **Update** — 切换以更新 RCS `false` | `true`

切换以更新 RCS 起伏模型值，指定为
`false` 或 `true`。当
`Update` 为 `true` 时，RCS
值被更新。如果 `Update` 为
`false`，则 RCS 保持不变。

#### 依赖关系

要启用此端口，请将 **Fluctuation
model** 下拉菜单设置为
`Swerling1`、
`Swerling2`、
`Swerling3` 或
`Swerling4`。
### 输出

### **Port\_1** — 窄带反射信号 1×*M* 复值向量 | *N*×*M* 复值矩阵

窄带非极化信号，指定为
1×*M* 复值向量或
*N*×*M* 复值矩阵。
每一列包含从目标反射的独立
信号。

量 *N* 是信号样本数，
*M* 是从目标反射的
信号数。每一列对应于不同的反射角度。

输出端口包含在当前输入时间帧内到达信号
目的地的信号样本。当从源到目的地的传播
时间超过当前时间帧持续时间时，
输出不包含当前时间帧输入的所有贡献。

## 参数

### **Azimuth angles (deg)** — 方位角 `[-180:180]`（默认）| 1×*P* 实值行向量 | *P*×1 实值列向量

指定用于定义
**RCS pattern (m^2)** 参数角度坐标的方位角。将方位角
指定为长度为 *P* 的向量。单位为度。
*P* 必须大于二。此参数确定截面
方向图任何元素的入射方位到达角。

**数据类型：** `double`

### **Elevation angles (deg)** — 俯仰角 `[-90:90]`（默认）| 1×*Q* 实值行向量 | *Q*×1 实值列向量

指定用于定义
**RCS pattern (m^2)** 参数角度坐标的俯仰角。将俯仰角
指定为长度为 *Q* 的向量。单位为度。
*Q* 必须大于二。此参数确定截面
方向图任何元素的入射俯仰到达角。

### **RCS pattern (m^2)** — 雷达截面积方向图 `ones(181,361)`（默认）| *Q*×*P* 实值矩阵 | *Q*×*P*×*M* 实值数组 | 1×*P* 实值向量 | *M*×*P* 实值矩阵

雷达截面积方向图，指定为
*Q*×*P* 实值矩阵或
*Q*×*P*×*M*
实值数组。

- *Q* 是 **Elevation angles (deg)**
  参数中向量的长度。
- *P* 是 **Azimuth angles (deg)** 参数中向量的长度。
- *M* 是目标方向图的数量。方向图的数量对应于传递到输入端口 `X` 的信号数量。不过，您可以使用单个方向图来对从单个目标反射的多个信号进行建模。

不过，您可以使用单个方向图来对从单个目标反射的多个信号进行建模。方向图单位为平方米。

方向图单位为平方米。

### **Fluctuation model** — 目标起伏模型 `Nonfluctuating`（默认）| `Swerling1` | `Swerling2` | `Swerling3` | `Swerling4`

将目标的统计模型指定为
`Nonfluctuating`、
`Swerling1`、
`Swerling2`、
`Swerling3` 或
`Swerling4`。当您将此参数设置为
`Nonfluctuating` 以外的值时，您随后使用 `Update` 输入端口设置雷达截面积参数。

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是
`physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 工作频率 `3e8`（默认）| 正标量

从目标反射的信号载波频率，指定为正标量。单位为赫兹。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

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

#### 编程使用

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

**在 R2016a 中引入**

## 描述

后向散射雷达目标

后向散射雷达目标模块对来自目标的非极化电磁信号的单基地雷达反射进行建模。目标模型包括全部四种 Swerling 目标起伏模型以及非起伏模型。您可以通过指定多个雷达散射截面（RCS）矩阵来同时建模多个目标。
