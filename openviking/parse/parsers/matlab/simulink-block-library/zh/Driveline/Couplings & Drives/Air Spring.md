---
type: simulink-block
title: 'Air Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'airspring'
documentation_source_path: 'ref/airspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Air Spring

## 端口
```yaml
ports:
- name: C
  summary: 从动端口 机械平移
  direction: conserving
- name: R
  summary: 基座端口 机械平移
  direction: conserving
```

### 守恒端口

### **C** — 从动端口 机械平移

与空气弹簧从动端关联的机械平移守恒端口。正物理信号从 **R** 流向 **C**。

### **R** — 基座端口 机械平移

与空气弹簧基座端关联的机械平移守恒端口。正物理信号从 **R** 流向 **C**。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 有效力参数化方式 Load as a function of height（默认）| Stiffness as a function of height
  group: 弹簧
- name: Height vector
  summary: 与载荷或刚度数据对应的高度断点 [5, 7, 11, 14, 17, 20] cm（默认）| 非负向量
  group: 弹簧
- name: Load vector
  summary: 给定高度断点处的载荷 [3000, 2000, 1500, 1200, 800, 100] N（默认）| 正向量
  group: 弹簧
- name: Stiffness vector
  summary: 给定高度断点处的刚度 [600, 300, 100, 80, 40, 5] N/cm（默认）| 正向量
  group: 弹簧
- name: Damping vector
  summary: 给定高度断点处的弹簧阻尼 [100, 60, 30, 15, 10, 10] s*N/cm（默认）| 非负向量
  group: 弹簧
- name: Interpolation method
  summary: 断点值之间的插值方法 Smooth（默认）| Linear
  group: 弹簧
- name: Extrapolation method
  summary: 处理超出断点数据集范围的输入值的方法 Linear（默认）| Nearest | Error
  group: 弹簧
- name: Hard stop at full extension
  summary: 模拟最大弹簧高度处的硬限位 off（默认）| on
  group: 硬限位
- name: Maximum height
  summary: 完全伸展硬限位的位置 25 cm（默认）| 正标量
  group: 硬限位
- name: Stiffness at full extension
  summary: 完全伸展硬限位刚度 1e8 N/cm（默认）| 正标量
  group: 硬限位
- name: Damping at full extension
  summary: 完全伸展硬限位阻尼 1e8 s*N/cm（默认）| 正标量
  group: 硬限位
- name: Hard stop at full compression
  summary: 模拟最小弹簧高度处的硬限位 off（默认）| on
  group: 硬限位
- name: Minimum height
  summary: 完全压缩硬限位的位置 5 cm（默认）| 正标量
  group: 硬限位
- name: Stiffness at full compression
  summary: 完全压缩硬限位刚度 1e8 N/cm（默认）| 正标量
  group: 硬限位
- name: Damping at full compression
  summary: 完全压缩硬限位阻尼 1e8 s*N/cm（默认）| 正标量
  group: 硬限位
- name: Hard stop model
  summary: 硬限位过渡行为 Stiffness and damping applied smoothly through transition region, damped rebound（默认）| ...
  group: 硬限位
- name: Transition region
  summary: 部分硬限位效应区域 0.1 mm（默认）| 正标量
  group: 硬限位
- name: Coefficient of restitution
  summary: 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 0.7（默认）| 0 到 1 之间的无单位值
  group: 硬限位
- name: Static contact speed threshold
  summary: 碰撞前滑块与限位之间的阈值相对速度 0.001 m/s（默认）| 非负标量
  group: 硬限位
- name: Static contact release force threshold
  summary: 从接触模式过渡到自由模式所需的阈值力 0.001 N（默认）
  group: 硬限位
```

### 弹簧

### **Parameterization** — 有效力参数化方式 `Load as a function of height`（默认）| `Stiffness as a function of height`

选择按高度或载荷进行参数化的选项。请从制造商提供的规格或实验结果中获取空气弹簧的数据。

### **Height vector** — 与载荷或刚度数据对应的高度断点 `[5, 7, 11, 14, 17, 20]` `cm`（默认）| 非负向量

弹簧高度向量。这些值对应于载荷值或刚度值，具体取决于您选择的弹簧参数化方式。您必须指定一个至少包含三个元素的向量。

### **Load vector** — 给定高度断点处的载荷 `[3000, 2000, 1500, 1200, 800, 100]` `N`（默认）| 正向量

弹簧载荷向量。此向量的长度必须与 **Height vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Load as a function of height`。

### **Stiffness vector** — 给定高度断点处的刚度 `[600, 300, 100, 80, 40, 5]` `N/cm`（默认）| 正向量

弹簧刚度值向量。此向量的长度必须与 **Height vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Stiffness as a function of height`。

### **Damping vector** — 给定高度断点处的弹簧阻尼 `[100, 60, 30, 15, 10, 10]` `s*N/cm`（默认）| 非负向量

弹簧阻尼值向量。此向量的长度必须与 **Height vector** 参数相同。

### **Interpolation method** — 断点值之间的插值方法 `Smooth`（默认）| `Linear`

查找表断点插值。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可获得最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

查找表断点外推。此方法确定当输入值超出参数列表中指定的范围时的输出值。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点也不低于数据中最低点的外推。
- `Error` — 当您希望数据位于表格范围内时，选择此选项可避免外推。如果输入信号超出表格范围，仿真将停止并生成错误。

有关详细信息，请参阅 `tablelookup`。

### 硬限位

### **Hard stop at full extension** — 模拟最大弹簧高度处的硬限位 `off`（默认）| `on`

启用空气弹簧完全伸展时硬限位的选项。当弹簧达到 **Maximum height** 参数的值时，硬限位发生。有关详细信息，请参阅 Translational Hard Stop。

### **Maximum height** — 完全伸展硬限位的位置 `25` `cm`（默认）| 正标量

最大弹簧高度。此参数确定完全伸展硬限位的位置。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension**。

### **Stiffness at full extension** — 完全伸展硬限位刚度 `1e8` `N/cm`（默认）| 正标量

弹簧达到完全伸展时施加的刚度。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension**。

### **Damping at full extension** — 完全伸展硬限位阻尼 `1e8` `s*N/cm`（默认）| 正标量

弹簧达到完全伸展时施加的阻尼。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension**。

### **Hard stop at full compression** — 模拟最小弹簧高度处的硬限位 `off`（默认）| `on`

启用空气弹簧完全压缩时硬限位的选项。当弹簧达到 **Minimum height** 参数的值时，硬限位发生。有关详细信息，请参阅 Translational Hard Stop。

### **Minimum height** — 完全压缩硬限位的位置 `5` `cm`（默认）| 正标量

最小弹簧高度。此参数确定完全压缩硬限位的位置。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full compression**。

### **Stiffness at full compression** — 完全压缩硬限位刚度 `1e8` `N/cm`（默认）| 正标量

弹簧达到完全压缩时施加的刚度。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full compression**。

### **Damping at full compression** — 完全压缩硬限位阻尼 `1e8` `s*N/cm`（默认）| 正标量

弹簧达到完全压缩时施加的阻尼。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full compression**。

### **Hard stop model** — 硬限位过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬限位模型的刚度和回弹选项。该模块使用 Translational Hard Stop 模块的复合实现。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`
- `Based on coefficient of restitution`

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension** 或 **Hard stop at full compression**。

### **Transition region** — 部分硬限位效应区域 `0.1` `mm`（默认）| 正标量

距完全压缩或完全伸展的距离，在该距离内刚度和阻尼效应部分施加。当您将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，该模块将在弹簧接近完全伸展或完全压缩时平滑过渡刚度和阻尼的起始。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **Coefficient of restitution** — 碰撞后滑块与限位之间的最终相对速度与初始相对速度之比 `0.7`（默认）| 0 到 1 之间的无单位值

滑块弹跳后滑块与限位之间的最终相对速度与初始相对速度之比。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact speed threshold** — 碰撞前滑块与限位之间的阈值相对速度 `0.001` `m/s`（默认）| 非负标量

碰撞前滑块与限位之间的阈值相对速度。当滑块以小于此参数值的速度撞击壳体时，它们保持接触。否则，滑块弹跳。为避免对滑块与壳体之间的静态接触进行建模，请将此参数设置为 `0`。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001` `N`（默认）

将滑块从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请选中 **Hard stop at full extension** 或 **Hard stop at full compression**，并将 **Hard stop model** 设置为 `Based on coefficient of restitution`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

### R2025a：枚举更新

**Hard stop at full extension** 和 **Hard stop at full compression** 参数现在使用复选框。这些参数在之前的版本中使用下拉菜单。

### R2023a：复合硬限位更新

由于 Translational Hard Stop 模块的更新，**Hard stop model** 参数现在具有 `Coefficient of restitution` 选项。

## 描述

密封式平移空气弹簧

Air Spring 模块表示一个通用的密封式平移气动弹簧，用于将设备与冲击和振动隔离。气体的可压缩性赋予空气弹簧理想的隔振性能。空气弹簧在汽车和工业应用中很常见，在这些应用中低弹簧刚度和低固有频率是有益的。空气弹簧可以帮助您：

- 减少簧载质量的磨损。
- 减少非簧载质量对基础设施造成的磨损。
- 减轻悬架系统重量以允许更大的总质量。
- 滤除特定的不需要的频率。

空气弹簧由限制压缩空气或其他气体柱的波纹管组成。空气承受载荷的力，波纹管保持空气。密封式空气弹簧维持恒定的空气质量，因此增加的载荷会降低空气体积和由此产生的弹簧刚度。反之亦然。密封式空气弹簧系统的固有频率也取决于这种关系。由于空气弹簧要求和性能存在大量可变性，制造商通常为每种型号提供压力特性表。

根据您拥有的数据，您可以将 **Parameterization** 设置为 `Load as a function of height` 或 `Stiffness as a function of height`。Air Spring 模块使用您输入的信息创建查找表。查找表允许该模块模拟任意空气弹簧的非线性力响应。这是达到给定高度的有效力，等效于 **Load vector** 参数或 **Stiffness vector** 参数与 **Height vector** 参数的逐元素乘积。有关在 Simscape™ 中使用查找表的详细信息，请参阅 `tablelookup`。

该模块获取端口 **R** 和端口 **C** 之间的相对平移运动，以评估空气弹簧的高度和速度，并使用此信息查找相应的查找表条目。该模块计算非线性有效力响应 *ΣF(x(t),t)*，使得：

∑F(x(t),t)=−c(x(t))x˙(t)−k(x(t))x(t)+Fexternal,

其中

- *x(t)* 是弹簧相对于未扰动位置的高度。
- *ẋ(t)* 是弹簧的速度。
- *-c(x(t))ẋ(t)* 是粘性阻尼力。阻尼系数 *c* 随弹簧高度变化。
- *-k(x(t))x(t)* 是刚度力。弹簧系数 *k* 随弹簧高度变化。
- *Fexternal* 是通过端口传递的力。

您可以在 **Hard Stops** 选项卡上选择是否在模型中实现硬限位。当您将 **Hard stop at full extension** 或 **Hard stop at full compression** 设置为 `On` 时，您可以指定边界高度、该高度处的刚度和阻尼以及过渡区域的长度。硬限位等效于 Translational Hard Stop 模块。

### 变量

使用 **Variables** 选项卡在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

当载荷为正时，**Force** 变量的符号为负。
