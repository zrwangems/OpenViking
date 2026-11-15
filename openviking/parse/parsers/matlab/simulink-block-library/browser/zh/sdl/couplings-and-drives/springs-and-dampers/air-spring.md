---
type: simulink-block
title: 'Air Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Springs and Dampers'
documentation_page: 'airspring'
documentation_source_path: 'ref/airspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Air Spring

## 端口

### 守恒

### **C** — 从动端口 mechanical translational

与空气弹簧从动端关联的 mechanical translational 守恒端口。正物理信号从 **R** 流向 **C**。

### **R** — 基座端口 mechanical translational

与空气弹簧基座端关联的 mechanical translational 守恒端口。正物理信号从 **R** 流向 **C**。

## 参数

### 弹簧

### **Parameterization** — 有效力参数化 `Load as a function of height`（默认） | `Stiffness as a function of height`

用于按高度或载荷进行参数化的选项。从制造商提供的规格或实验结果中获取空气弹簧的数据。

### **Height vector** — 与载荷或刚度数据对应的高度断点 `[5, 7, 11, 14, 17, 20]` `cm`（默认） | 非负向量

弹簧高度向量。这些值对应于载荷或刚度值，具体取决于您选择的弹簧参数化方式。必须指定一个至少包含三个元素的向量。

### **Load vector** — 给定高度断点处的载荷 `[3000, 2000, 1500, 1200, 800, 100]` `N`（默认） | 正向量

弹簧载荷向量。此向量长度必须与 **Height vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Load as a function of height`。

### **Stiffness vector** — 给定高度断点处的刚度 `[600, 300, 100, 80, 40, 5]` `N/cm`（默认） | 正向量

弹簧刚度值向量。此向量长度必须与 **Height vector** 参数相同。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Stiffness as a function of height`。

### **Damping vector** — 给定高度断点处的弹簧阻尼 `[100, 60, 30, 15, 10, 10]` `s*N/cm`（默认） | 非负向量

弹簧阻尼值向量。此向量长度必须与 **Height vector** 参数相同。

### **Interpolation method** — 断点值之间的插值方法 `Smooth`（默认） | `Linear`

查找表断点插值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可获得最低计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关更多信息，请参见 `tablelookup`。

### **Extrapolation method** — 处理落在断点数据集范围之外的输入值的方法 `Linear`（默认） | `Nearest` | `Error`

查找表断点外插。此方法确定当输入值超出参数列表中指定范围时的输出值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可生成在外插区域以及在与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不会高于数据中最高点或低于数据中最低点的外插。
- `Error` — 当您希望数据位于表格范围内时，选择此选项可避免外插。如果输入信号超出表格范围，仿真将停止并生成错误。

有关更多信息，请参见 `tablelookup`。

### 硬停止

### **Hard stop at full extension** — 在最大弹簧高度处模拟硬停止 `off`（默认） | `on`

用于在空气弹簧完全伸展时启用硬停止的选项。当弹簧达到 **Maximum height** 参数的值时发生硬停止。有关更多信息，请参见 Translational Hard Stop。

### **Maximum height** — 完全伸展硬停止的位置 `25` `cm`（默认） | 正标量

最大弹簧高度。此参数确定完全伸展硬停止的位置。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension**。

### **Stiffness at full extension** — 完全伸展硬停止刚度 `1e8` `N/cm`（默认） | 正标量

当弹簧达到完全伸展时应用的刚度。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension**。

### **Damping at full extension** — 完全伸展硬停止阻尼 `1e8` `s*N/cm`（默认） | 正标量

当弹簧达到完全伸展时应用的阻尼。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension**。

### **Hard stop at full compression** — 在最小弹簧高度处模拟硬停止 `off`（默认） | `on`

用于在空气弹簧完全伸展时启用硬停止的选项。当弹簧达到 **Minimum height** 参数的值时发生硬停止。有关更多信息，请参见 Translational Hard Stop。

### **Minimum height** — 完全压缩硬停止的位置 `5` `cm`（默认） | 正标量

最小弹簧高度。此参数确定完全压缩硬停止的位置。

#### 依赖项

要启用此参数，请选择 **Hard stop at full compression**。

### **Stiffness at full compression** — 完全压缩硬停止刚度 `1e8` `N/cm`（默认） | 正标量

当弹簧达到完全压缩时应用的刚度。

#### 依赖项

要启用此参数，请选择 **Hard stop at full compression**。

### **Damping at full compression** — 完全压缩硬停止阻尼 `1e8` `s*N/cm`（默认） | 正标量

当弹簧达到完全压缩时应用的阻尼。

#### 依赖项

要启用此参数，请选择 **Hard stop at full compression**。

### **Hard stop model** — 硬停止过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认） | ...

硬停止模型的刚度和回弹选项。该模块使用 Translational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`
- `Based on coefficient of restitution`

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension** 或 **Hard stop at full compression**。

### **Transition region** — 部分硬停止效果区域 `0.1` `mm`（默认） | 正标量

距完全压缩或完全伸展的距离，在该距离内部分应用刚度和阻尼效果。当您将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，该模块将在弹簧接近完全伸展或完全压缩时平滑过渡刚度和阻尼的起始。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与停止件之间最终相对速度与初始相对速度之比 `0.7`（默认） | 0 到 1 之间的无单位值

滑块弹回后，滑块与停止件之间的最终相对速度与初始相对速度之比。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与停止件之间的阈值相对速度 `0.001` `m/s`（默认） | 非负标量

碰撞前滑块与停止件之间的阈值相对速度。当滑块以小于此参数值的速度撞击外壳时，它们保持接触。否则，滑块弹回。为避免对滑块与外壳之间的静态接触建模，请将此参数设置为 `0`。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001` `N`（默认）

从静态接触模式释放滑块所需的最小力。

#### 依赖项

要启用此参数，请选择 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

### R2025a: 枚举更新

**Hard stop at full extension** 和 **Hard stop at full compression** 参数现在使用复选框。这些参数在之前的版本中使用下拉菜单。

### R2023a: 复合硬停止更新

由于 Translational Hard Stop 模块的更新，**Hard stop model** 参数现在具有 `Coefficient of restitution` 选项。

## 描述

密封平移空气弹簧

Air Spring 模块表示一个通用的密封平移气动弹簧，用于将设备与冲击和振动隔离。气体的可压缩性赋予空气弹簧理想的隔振性能。空气弹簧在汽车和工业应用中很常见，在这些应用中，低弹簧刚度和低固有频率是有益的。空气弹簧可以帮助您：

- 减少簧载质量的磨损。
- 减少非簧载质量对基础设施造成的磨损。
- 减轻悬架系统重量，以允许更大的总质量。
- 滤除特定的不需要频率。

空气弹簧由波纹管组成，波纹管限制一柱压缩空气或其他气体。空气承受载荷的力，波纹管容纳空气。密封空气弹簧保持空气质量恒定，因此增加的载荷会降低空气体积以及由此产生的弹簧刚度。反之亦然。密封空气弹簧系统的固有频率也取决于这种关系。由于空气弹簧要求和性能存在大量变化，制造商通常会为每种型号提供压力特性表。

根据您拥有的数据，您可以将 **Parameterization** 设置为 `Load as a function of height` 或 `Stiffness as a function of height`。Air Spring 模块使用您输入的信息创建查找表。查找表允许该模块模拟任意空气弹簧的非线性力响应。这是达到给定高度所需的有效力，它等同于 **Load vector** 参数，或者等同于 **Stiffness vector** 参数与 **Height vector** 参数的逐元素乘积。有关在 Simscape™ 中使用查找表的更多信息，请参见 `tablelookup`。

该模块采用端口 **R** 和端口 **C** 之间的相对平移运动来评估空气弹簧的高度和速度，并使用此信息查找适当的查找表条目。该模块计算非线性有效力响应 *ΣF(x(t),t)*，使得：

∑F(x(t),t)=−c(x(t))x˙(t)−k(x(t))x(t)+Fexternal,

其中

- *x(t)* 是弹簧相对于未受扰动位置的高度。
- *ẋ(t)* 是弹簧的速度。
- *-c(x(t))ẋ(t)* 是黏性阻尼力。阻尼系数 *c* 随弹簧高度变化。
- *-k(x(t))x(t)* 是刚度力。弹簧系数 *k* 随弹簧高度变化。
- *Fexternal* 是通过端口传递的力。

您可以选择是否在模型的 **Hard Stops** 选项卡中实现硬停止。当您将 **Hard stop at full extension** 或 **Hard stop at full compression** 设置为 `On` 时，可以指定边界高度、该高度处的刚度和阻尼，以及过渡区域的长度。硬停止等效于 Translational Hard Stop 模块。

### 变量

使用 **Variables** 选项卡在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。

当载荷为正时，**Force** 变量的符号为负。
