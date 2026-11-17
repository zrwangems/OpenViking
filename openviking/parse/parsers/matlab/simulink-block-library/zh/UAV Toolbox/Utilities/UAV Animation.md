---
type: simulink-block
title: 'UAV Animation'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'uavanimation'
documentation_source_path: 'ref/uavanimation.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Animation

## 端口
```yaml
ports:
- name: Translation
  summary: UAV 的 *xyz* 位置矩阵
  direction: input
- name: Rotation
  summary: UAV 机体坐标系旋转矩阵 | *m*×4 矩阵
  direction: input
- name: UAV Type
  summary: UAV 网格类型向量
  direction: input
- name: UAV Mesh Configuration
  summary: UAV 网格配置向量 | 矩阵
  direction: input
- name: Marker
  summary: 无人机标记配置矩阵
  direction: input
```

### 输入

### **Translation** — UAV 的 *xyz* 位置矩阵

UAV 的 *xyz* 位置，指定为 *m*×3 矩阵，其中 *m* 是您想要动画显示的 UAV 总数。矩阵的每一行指定一个 UAV 在 **Inertial frame z-axis direction** 属性中指定的坐标系中的 *xyz* 位置。

**示例：** `[1 1 1]`

### **Rotation** — UAV 机体坐标系旋转矩阵 | *m*×4 矩阵

UAV 机体坐标系相对于惯性坐标系的旋转，指定为 *m*×3 或 *m*×4 矩阵。

- 如果您将 **Rotation format** 参数指定为 `Euler ZYX`，请将此输入指定为 *m*×3 矩阵，其中 *m* 是您想要动画显示的 UAV 总数。矩阵的每一行表示一个 UAV 相对于惯性坐标系 *z* 轴、*y* 轴和 *x* 轴的旋转角度，以弧度为单位。
- 如果您将此 **Rotation format** 参数指定为 `Quaternion`，请将输入指定为 *m*×4 矩阵，其中 *m* 是您想要动画显示的 UAV 总数。矩阵的每一行表示一个 UAV 的四元数向量。

### **UAV Type** — UAV 网格类型向量

UAV 网格类型，指定为 *m* 元素整数向量，其中 *m* 是您想要动画显示的 UAV 总数。每个元素指定一个 UAV 的网格类型，其中 `1` 是四旋翼网格，`2` 是固定翼网格。

#### 依赖关系

要启用此端口，请选择 **Enable dynamic UAV mesh configuration** 参数。

### **UAV Mesh Configuration** — UAV 网格配置向量 | 矩阵

UAV 网格配置，指定为 *m* 元素列向量或 *m*×4 或 *m*×5 矩阵。*m* 是您想要动画显示的 UAV 总数，每一行对应一个 UAV 的网格配置。此输入的大小取决于您要为 UAV 配置的参数：

- *m* 元素列向量 — 每个元素指定一个 UAV 的网格大小，必须为正值。每个 UAV 具有默认颜色 `[1 0 0]` 和 alpha 值 `1`。
- *m*×4 矩阵 — 每一行指定一个 UAV 的网格大小和颜色，其中第一个元素是大小，其余三个元素以 RGB 三元组指定颜色。
- *m*×5 矩阵 — 每一行指定一个 UAV 的网格大小、颜色和透明度，其中第一个元素是大小，接下来三个元素指定颜色，最后一个元素指定 UAV 网格的 alpha 值，范围为 `[0, 1]`。值为 `0` 表示完全透明，值为 `1` 表示完全不透明。

**示例：** `[10 1 0 0 0.5; 20 0 1 0 0.5]` 将第一个 UAV 网格大小设置为 10，颜色设置为红色，第二个 UAV 网格大小设置为 20，颜色设置为绿色。两个 UAV 网格的透明度均为 0.5。

#### 依赖关系

要启用此端口，请选择 **Enable dynamic UAV mesh configuration** 参数。

### **Marker** — 无人机标记配置矩阵

标记配置，指定为一个 *n* 行矩阵。
*n* 是您想要绘制的标记总数，每一行对应一个标记的配置。输入的大小取决于您要为标记配置的参数：

- *n*×3 矩阵 — 每一行指定一个标记的 *xyz* 位置。每一行使用默认的大小、颜色、类型和填充状态。
- *n*×4 矩阵 — 每一行指定一个标记的 *xyz* 位置和大小，其中前 3 个元素指定位置，最后一个元素指定大小。
- *n*×7 矩阵 — 前三个元素指定 *xyz* 位置，下一个元素指定大小，其余三个元素以 RGB 三元组指定标记的颜色。
- *n*×8 矩阵 — 前三个元素指定 *xyz* 位置，下一个元素指定大小，再接下来的三个元素指定颜色，最后一个元素按如下方式指定标记的类型：

  - 1 — 圆形标记
  - 2 — 方形标记
  - 3 — 三角形标记
- *n*×9 矩阵 — 前三个元素指定 *xyz* 位置，下一个元素指定大小，再接下来的三个元素指定颜色，下一个元素指定标记类型，最后一个元素以正整数指定标记的填充状态，1 表示填充，0 表示未填充。

#### 依赖关系

要启用此端口，请选择 **Draw marker** 参数。
## 参数
```yaml
parameters:
- name: Number of UAVs
  summary: 要显示的无人机数量 1（默认）| 正整数
  group: ''
- name: Enable dynamic UAV mesh configuration
  summary: 动态无人机网格配置 off（默认）| on
  group: ''
- name: UAV Type
  summary: 要显示的无人机网格类型 Multirotor（默认）| FixedWing
  group: ''
- name: UAV size
  summary: 框架和附加网格的大小 1（默认）| 正数值标量
  group: ''
- name: UAV mesh color
  summary: 无人机网格的颜色 [1 0 0]（默认）| RGB 三元组
  group: ''
- name: UAV mesh and trajectory alpha
  summary: 无人机网格和轨迹的透明度 1（默认）| 正数值标量
  group: ''
- name: Inertial frame z-axis direction
  summary: 惯性坐标系 *z* 轴正方向 Down（默认）| Up
  group: ''
- name: Rotation format
  summary: 旋转输入格式 Quaternion（默认）| Euler ZYX
  group: ''
- name: Draw marker
  summary: 启用标记 off（默认）| on
  group: ''
- name: Sample time
  summary: 输出之间的间隔 –1（默认）| 标量
  group: ''
```

### **Number of UAVs** — 要显示的无人机数量 `1`（默认）| 正整数

要显示的无人机数量，指定为正整数。

### **Enable dynamic UAV mesh configuration** — 动态无人机网格配置 `off`（默认）| `on`

选择此参数以启用 **UAV Type** 和 **UAV Mesh Configuration** 输入端口，这些端口使您能够为仿真中的每架无人机配置不同的网格。

### **UAV Type** — 要显示的无人机网格类型 `Multirotor`（默认）| `FixedWing`

指定要为仿真的无人机显示的网格，可选值为 `FixedWing` 或 `Multirotor`。使用此参数为所有无人机设置统一的网格类型。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic UAV mesh configuration** 参数。

### **UAV size** — 框架和附加网格的大小 `1`（默认）| 正数值标量

使用此参数为所有仿真的无人机设置统一的网格大小。将该值指定为正数值标量。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic UAV mesh configuration** 参数。

### **UAV mesh color** — 无人机网格的颜色 `[1 0 0]`（默认）| RGB 三元组

将无人机网格的颜色指定为 RGB 三元组。使用此参数为仿真中的所有无人机设置统一的网格颜色。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic UAV mesh configuration** 参数。

### **UAV mesh and trajectory alpha** — 无人机网格和轨迹的透明度 `1`（默认）| 正数值标量

使用此参数为仿真中所有无人机的网格和轨迹设置统一的透明度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic UAV mesh configuration** 参数。

### **Inertial frame z-axis direction** — 惯性坐标系 *z* 轴正方向 `Down`（默认）| `Up`

将惯性坐标系 *z* 轴的正方向指定为 `Up` 或 `Down`。在绘图中，*z* 轴正方向始终指向上方。该参数定义了惯性坐标系与绘图坐标系之间的旋转。如果惯性坐标系遵循北-东-地（NED）配置，请将此参数设置为 `Down`。

### **Rotation format** — 旋转输入格式 `Quaternion`（默认）| `Euler ZYX`

将旋转输入格式指定为以下选项之一：

- `Euler ZYX` — 旋转输入必须是一个 *m*×3 的欧拉 *zyx* 角矩阵，单位为弧度，其中 *m* 是您想要动画显示的 UAV 总数。
- `Quaternion`— 旋转输入必须是一个 *m*×4 的四元数向量矩阵，其中每一行是一个四元数。*m* 是您想要动画显示的 UAV 总数。

### **Draw marker** — 启用标记 `off`（默认）| `on`

选择此参数以启用 **Marker** 输入端口，该端口使您能够在仿真中绘制标记。

### **Sample time** — 输出之间的间隔 `–1`（默认）| 标量

将输出之间的间隔指定为标量，单位为秒。在仿真中，采样时间遵循仿真时间而非实际挂钟时间。

默认值表示模块采样时间为*继承*。

有关继承采样时间类型的详细信息，请参阅 Specify Sample Time (Simulink)。
## 所属库

UAV Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于在生成代码的系统中对 UAV 飞行进行动画显示。但是，此模块不包含在生成的代码中。

## 版本历史

**在 R2018b 中引入**

### R2024b：对多个 UAV 进行动画显示、绘制标记以及动态配置网格

- UAV Animation 模块现在支持对多个 UAV 进行动画显示。使用 **Number of UAVs** 参数指定要动画显示的 UAV 数量。
- 您现在可以通过选择 **Draw marker** 参数并向 **Marker** 输入端口指定标记配置来绘制标记。使用标记可在航点跟随任务中可视化航点或前视距离。
- UAV Animation 模块现在支持动态网格配置，使您能够为仿真中的每个 UAV 指定不同的网格配置。要启用动态网格配置，请选择 **Enable dynamic UAV mesh configuration** 参数。

## 描述

使用平移和旋转对 UAV 飞行路径进行动画显示

UAV Animation 模块基于平移和旋转的输入数组对一个或多个无人机（UAV）飞行路径进行动画显示。输出图窗在给定位置和方向显示固定翼或多旋翼 UAV 的可视化网格。要在仿真后打开图窗，请点击模块封装中的 **Show animation**。
