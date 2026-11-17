---
type: simulink-block
title: 'Backscatter Bicyclist'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'backscatterbicyclistblock'
documentation_source_path: 'ref/backscatterbicyclistblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Backscatter Bicyclist

## 端口

### 输入

### **X** — 入射雷达信号 复值 *M*×*N* 矩阵

每个骑行者散射体上的入射雷达信号，指定为复值 *M*×*N* 矩阵。*M* 是信号中的采样数。*N* 是骑行者上的点散射体数量，部分由每个车轮中的辐条数量 *N*ws 决定。关于表示每个散射体处入射信号的列，请参见 Bicyclist Scatterer Indices。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** 是

### **AngH** — 骑行者航向 `0.0` | 标量

骑行者的航向，指定为标量。航向在 *xy* 平面内从 *x* 轴朝向 *y* 轴测量。单位为度。

**示例：** `-34`

**数据类型：** `double`

### **Ang** — 入射信号方向 实值 2×*N* 向量

散射体上入射信号的方向，指定为实值 2×*N* 矩阵。`Ang` 的每一列指定信号到对应散射体的入射方向。每一列的形式为 *[AzimuthAngle;ElevationAngle]* 对。单位为度。关于表示每个散射体处入射到达角的列，请参见 Bicyclist Scatterer Indices。

**数据类型：** `double`

### **Speed** — 骑行者速度 非负标量

骑行者的速度，指定为非负标量。运动模型将速度限制为 60 m/s。单位为米每秒。

**示例：** `8`

**数据类型：** `double`

### **Coast** — 骑行者滑行状态 `false`（默认）| `true`

骑行者的滑行状态，指定为 `false` 或 `true`。此属性控制骑行者的滑行。如果设置为 `true`，骑行者不踩踏板，但车轮仍在旋转（自由滑行）。如果设置为 `false`，骑行者正在踩踏板，`Gear transmission ratio` 参数决定车轮旋转与踏板旋转的比率。

**可调：** 是

**数据类型：** `Boolean`
### 输出

### **Y** — 合并反射雷达信号 复值 *M*×1 列向量

合并反射雷达信号，返回为复值 *M*×1 列向量。*M* 等于输入信号 `X` 中的采样数。

**数据类型：** `double`
**复数支持：** 是

### **Pos** — 散射体位置 实值 3×*N* 矩阵

散射体的位置，返回为实值 3×*N* 矩阵。*N* 是骑行者上的散射体数量。每一列表示其中一个散射体的笛卡尔位置 [*x*;*y*;*z*]。单位为米。关于表示每个散射体位置的列，请参见 Bicyclist Scatterer Indices。

**数据类型：** `double`

### **Vel** — 散射体速度 实值 3×*N* 矩阵

散射体的速度，返回为实值 3×*N* 矩阵。*N* 是骑行者上的散射体数量。每一列表示其中一个散射体的笛卡尔速度 [*vx*;*vy*;*vz*]。单位为米每秒。关于表示每个散射体速度的列，请参见 Bicyclist Scatterer Indices。

**数据类型：** `double`

### **Ax** — 散射体方向 实值 3×3 矩阵

散射体的方向轴，返回为实值 3×3 矩阵。

**数据类型：** `double`

## 参数

### **Number of wheel spokes** — 每个车轮的辐条数量 `20`（默认）| 正整数

自行车每个车轮的辐条数量，指定为从 3 到 50（含）的正整数。单位无量纲。

**数据类型：** `double`

### **Gear transmission ratio** — 车轮转数与踏板转数之比 `1.5`（默认）| 正标量

车轮转数与踏板转数之比，指定为正标量。传动比必须在 0.5 到 6 的范围内。单位为无量纲。

**数据类型：** `double`

### **Signal carrier frequency (Hz)** — 载波频率 `77e9`（默认）| 正标量

窄带入射信号的载波频率，指定为正标量。单位为 Hz。

**示例：** `1e9`

**数据类型：** `double`

### **Initial position (m)** — 骑行者初始位置 `[0;0;0]`（默认）| 3×1 实值向量

骑行者的初始位置，指定为 [*x*;*y*;*z*] 形式的 3×1 实值向量。单位为米。

**数据类型：** `double`

### **Initial heading direction (deg)** — 骑行者初始航向 `0`（默认）| 标量

骑行者的初始航向，指定为标量。航向在 *xy* 平面内从 *x* 轴朝向 *y* 轴测量。单位为度。

**数据类型：** `double`

### **Initial bicyclist speed (m/s)** — 骑行者初始速度 `4`（默认）| 非负标量

骑行者的初始速度，指定为非负标量。运动模型将速度限制为最大 60 m/s（216 kph）。单位为米每秒。

**可调：** 是

**数据类型：** `double`

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **RCS pattern** — RCS 方向图来源 `Auto`（默认）| `Property`

RCS 方向图的来源，指定为 `Auto` 或 `Property`。当指定 `Auto` 时，方向图为 1×361 矩阵，包含从 77 GHz 雷达测量中导出的值。

### **Azimuth angles (deg)** — 方位角 `[-180:180]`（默认）| 1×*P* 实值行向量 | *P*×1 实值列向量

用于定义 **Radar cross section pattern (square meters)** 参数所指定矩阵每一列角度坐标的方位角。将方位角指定为长度为 *P* 的向量。*P* 必须大于 2。角度单位为度。

**示例：** `[-45:0.1:45]`

#### 依赖关系

要启用此参数，请将 **RCS pattern** 参数设置为 `Property`。

**数据类型：** `double`

### **Elevation angles (deg)** — 俯仰角 `[-90:90]`（默认）| 1×*Q* 实值行向量 | *Q*×1 实值列向量

用于定义 **Radar cross section pattern (square meters)** 参数所指定矩阵每一行角度坐标的俯仰角。将俯仰角指定为长度为 *Q* 的向量。*Q* 必须大于 2。角度单位为度。

#### 依赖关系

要启用此参数，请将 **RCS pattern** 参数设置为 `Property`。

**数据类型：** `double`

### **Radar cross section pattern (square meters)** — 雷达截面积方向图 1×361 实值矩阵（默认）| *Q*×*P* 实值矩阵 | 1×*P* 实值向量

作为俯仰角和方位角函数的雷达截面积（RCS）方向图，指定为 *Q*×*P* 实值矩阵或 1×*P* 实值向量。*Q* 是由 `ElevationAngles` 属性定义的向量长度。*P* 是由 `AzimuthAngles` 属性定义的向量长度。单位为平方米。

您也可以将方向图指定为一个俯仰角对应的 1×*P* 实值方位角向量。

此属性的默认值为 1×361 矩阵，包含从 `backscatterBicyclist.defaultRCSPattern` 中 77 GHz 雷达测量导出的值。

#### 依赖关系

要启用此参数，请将 **RCS pattern** 参数设置为 `Property`。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真作为编译代码通常比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| **模块仿真** | **仿真行为** | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

来自骑行者的反向散射信号

Backscatter Bicyclist 模块仿真从移动骑行者反射的反向散射雷达信号。骑行者由自行车和骑行者组成。该对象对骑行者的运动进行建模，并计算来自骑行者上多个离散散射体的所有反射信号之和。该模型忽略骑行者内部的遮挡。反射信号使用基于 77 GHz 雷达系统开发的多散射体模型计算。

散射体位于五个主要骑行者组件上：

- 自行车车架和骑行者
- 自行车踏板
- 骑行者的上腿和下腿
- 前轮
- 后轮

除车轮外，骑行者上有 114 个散射体。车轮在轮辋和辐条上包含散射体。车轮上的散射体数量取决于每个车轮的辐条数量，可通过 `NumWheelSpokes` 属性指定。
