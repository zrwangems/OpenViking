---
type: simulink-block
title: 'Backscatter Pedestrian'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'backscatterpedestrianblock'
documentation_source_path: 'ref/backscatterpedestrianblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Backscatter Pedestrian

## 端口
```yaml
ports:
- name: X
  summary: 入射雷达信号 复值 *M*×16 矩阵
  direction: input
  data_types: double
- name: Ang
  summary: 入射信号方向 实值 2×16 矩阵
  direction: input
  data_types: double
- name: AngH
  summary: 行人朝向 标量
  direction: input
  data_types: double
- name: Y
  summary: 合并的反射雷达信号 复值 *M*×1 列向量
  direction: output
  data_types: double
- name: Pos
  summary: 身体段位置 实值 3×16 矩阵
  direction: output
  data_types: double
- name: Vel
  summary: 身体段速度 实值 3×16 矩阵
  direction: output
  data_types: double
- name: Ax
  summary: 身体段方向 实值 3×3×16 数组
  direction: output
  data_types: double
```

### 输入

### **X** — 入射雷达信号 复值 *M*×16 矩阵

各身体段上的入射雷达信号，指定为复值 *M*×16 矩阵。*M* 是信号中的采样数。关于表示每个身体段入射信号的列，请参见 Body Segment Indices。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能会发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Ang** — 入射信号方向 实值 2×16 矩阵

身体段上的入射信号方向，指定为实值 2×16 矩阵。`ANG` 的每一列指定信号到对应身体部位的入射方向。每一列的形式为 `[AzimuthAngle;ElevationAngle]` 对。单位为度。关于表示每个身体段入射方向的列，请参见 Body Segment Indices。

**数据类型：** `double`

### **AngH** — 行人朝向 标量

行人的朝向，指定为标量。朝向在 *xy* 平面中从 *x* 轴朝向 *y* 轴测量。单位为度。

**示例：** `-34`

**数据类型：** `double`
### 输出

### **Y** — 合并的反射雷达信号 复值 *M*×1 列向量

合并的反射雷达信号，返回为复值 *M*×1 列向量。*M* 等于输入信号 `X` 中的相同采样数。

**数据类型：** `double`
**复数支持：** 是

### **Pos** — 身体段位置 实值 3×16 矩阵

身体段位置，返回为实值 3×16 矩阵。每一列表示 16 个身体段之一的笛卡尔位置 `[x;y;z]`。单位为米。关于表示每个身体段位置的列，请参见 Body Segment Indices。

**数据类型：** `double`

### **Vel** — 身体段速度 实值 3×16 矩阵

身体段速度，返回为实值 3×16 矩阵。每一列表示 16 个身体段之一的笛卡尔速度 `[vx;vy;vz]`。单位为米每秒。关于表示每个身体段速度的列，请参见 Body Segment Indices。

**数据类型：** `double`

### **Ax** — 身体段方向 实值 3×3×16 数组

身体段的方向轴，返回为实值 3×3×16 数组。每一页表示 16 个身体段之一的 3×3 方向轴。单位无量纲。关于表示每个身体段方向的页，请参见 Body Segment Indices。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Height (m)
  summary: 行人高度 1.65（默认）| 正标量
  group: ''
- name: Walking Speed (m/s)
  summary: 行人步行速度 1.4 倍行人高度（默认）| 非负标量
  group: ''
- name: Propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: ''
- name: Operating Frequency (Hz)
  summary: 载波频率 300e6（默认）| 正标量
  group: ''
- name: Initial Position (m)
  summary: 行人的初始位置 [0;0;0]（默认）| 3×1 实值向量
  group: ''
- name: Initial Heading (deg)
  summary: 行人的初始航向 0（默认）| 标量
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
```

### **Height (m)** — 行人高度 `1.65`（默认）| 正标量

行人高度，指定为正标量。单位为米。

**数据类型：** `double`

### **Walking Speed (m/s)** — 行人步行速度 `1.4` 倍行人高度（默认）| 非负标量

行人的步行速度，指定为非负标量。运动模型将步行速度限制为 **Height (m)** 参数中设置的行人高度的 1.4 倍。单位为米每秒。

**数据类型：** `double`

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Operating Frequency (Hz)** — 载波频率 `300e6`（默认）| 正标量

窄带入射信号的载波频率，指定为正标量。单位为 Hz。

**示例：** `1e9`

**数据类型：** `double`

### **Initial Position (m)** — 行人的初始位置 `[0;0;0]`（默认）| 3×1 实值向量

行人的初始位置，指定为 `[x;y;z]` 形式的 3×1 实值向量。单位为米。

**数据类型：** `double`

### **Initial Heading (deg)** — 行人的初始航向 `0`（默认）| 标量

行人的初始航向，指定为标量。航向在 *xy* 平面内从 *x* 轴朝向 *y* 轴测量。单位为度。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

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
## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

行人的后向散射信号

Backscatter Pedestrian 模块对行走行人产生的非极化电磁信号的单站反射进行建模。行人行走模型协调 16 个身体节段的运动以模拟自然运动。该模型还模拟每个身体节段的雷达反射率。通过该模型，您可以获得每个节段的位置和速度，以及身体移动时的总后向散射辐射。
