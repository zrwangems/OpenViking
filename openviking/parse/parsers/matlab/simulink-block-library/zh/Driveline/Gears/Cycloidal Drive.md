---
type: simulink-block
title: 'Cycloidal Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'cycloidaldrive'
documentation_source_path: 'ref/cycloidaldrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Cycloidal Drive

## 端口
```yaml
ports:
- name: B
  summary: 基轴机械旋转
  direction: conserving
- name: F
  summary: 从动轴机械旋转
  direction: conserving
- name: R
  summary: 齿圈机械旋转
  direction: conserving
- name: H
  summary: 热流热端口
  direction: conserving
```

### 守恒端口

### **B** — 基轴机械旋转

与基轴关联的机械旋转守恒端口。

### **F** — 从动轴机械旋转

与从动轴关联的机械旋转守恒端口。

### **R** — 齿圈机械旋转

与齿圈关联的机械旋转守恒端口。

#### 依赖关系

要显示此端口，请选择 **Ring gear rotation**。

### **H** — 热流热端口

与热流关联的热守恒端口。

#### 依赖关系

要显示此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 参数
```yaml
parameters:
- name: Ring gear rotation
  summary: 模拟齿圈运动的选项 off（默认）| on
  group: 主要
- name: Number of teeth on cycloid disc
  summary: 摆线盘齿数 20（默认）| 正标量整数
  group: 主要
- name: Number of teeth on ring gear
  summary: 齿圈齿数 24（默认）| 正标量整数
  group: 主要
- name: Friction model
  summary: 啮合损失模型 No meshing losses - Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: 啮合损失
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 向量
  group: 啮合损失
- name: Efficiency from base shaft to follower shaft
  summary: 基轴到从动轴效率 0.90 或 [0.95, 0.85, 0.80]（默认）| 区间 (0,1] 内的标量或元素向量
  group: 啮合损失
- name: Efficiency from follower shaft to base shaft
  summary: 从动轴到基轴效率 0.05 或 [0.10, 0.05, 0.03]（默认）| 区间 (0,1] 内的标量或元素向量
  group: 啮合损失
- name: Power threshold
  summary: 最小效率功率阈值 0.001 W（默认）| 标量
  group: 啮合损失
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 标量
  group: 热端口
```

### 主要

### **Ring gear rotation** — 模拟齿圈运动的选项 `off`（默认）| `on`

模拟齿圈旋转的选项。选择此参数将启用端口 **R**。

### **Number of teeth on cycloid disc** — 摆线盘齿数 `20`（默认）| 正标量整数

从摆线盘周边向外突出的齿的总数。此参数的值应小于 **Number of teeth on ring gear** 参数的值。齿轮齿数比定义了基轴和从动轴的相对角速度。

### **Number of teeth on ring gear** — 齿圈齿数 `24`（默认）| 正标量整数

从齿圈壳体向内突出的齿或销的总数。此参数的值应大于 **Number of teeth on cycloid disc** 参数的值。两个齿轮齿数比定义了基轴和从动轴的相对角速度。

### 啮合损失

### **Friction model** — 啮合损失模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

包含摩擦啮合损失的选项：

- `No meshing losses - Suitable for HIL simulation` — 模块忽略啮合损失。
- `Constant efficiency` — 您指定一个在整个仿真过程中保持恒定的组件效率。
- `Temperature-dependent efficiency` — 模块根据端口 **H** 的输入确定扭矩传递效率。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素的值必须从左到右递增。向量中的元素数量必须与 **Efficiency from base shaft to follower shaft** 和 **Efficiency from follower shaft to base shaft** 参数指定的向量中的元素数量匹配。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Efficiency from base shaft to follower shaft** — 基轴到从动轴效率 `0.90` 或 `[0.95, 0.85, 0.80]`（默认）| 区间 (0,1] 内的标量或元素向量

基轴驱动从动轴时的扭矩传递效率。效率值必须落在区间 (0,1] 内。较大的效率值对应于基轴和从动轴之间更大的扭矩传递。接近 1 的值是典型的。

如何指定此参数取决于 **Friction model** 参数的设置：

- `Constant efficiency` — 将值指定为标量。
- `Temperature-dependent efficiency` — 将值指定为向量，其中每个元素是温度向量中对应温度元素处的输出功率与输入功率之比。向量中的元素数量必须与 **Temperature** 参数指定的向量中的元素数量匹配。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### **Efficiency from follower shaft to base shaft** — 从动轴到基轴效率 `0.05` 或 `[0.10, 0.05, 0.03]`（默认）| 区间 (0,1] 内的标量或元素向量

从动轴驱动基轴时（即反向运行）的扭矩传递效率。效率值必须落在区间 (0,1] 内。较大的效率值对应于基轴和从动轴之间更大的扭矩传递。接近 0 的值是典型的。

如何指定此参数取决于 **Friction model** 参数的设置：

- `Constant efficiency` — 将值指定为标量。
- `Temperature-dependent efficiency` — 将值指定为向量，其中每个元素是温度向量中对应温度元素处的输出功率与输入功率之比。向量中的元素数量必须与 **Temperature** 参数指定的向量中的元素数量匹配。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### **Power threshold** — 最小效率功率阈值 `0.001` `W`（默认）| 标量

摆线盘功率的绝对值，高于此值时应用完整效率因子。低于此值时，模块对效率因子进行平滑处理。当您将 **Friction model** 设置为：

- `Constant efficiency` 时，模块使用双曲正切函数将效率因子平滑至 1，使得效率损失在静止状态下趋于零。
- `Temperature-dependent efficiency` 时，模块使用双曲正切函数在静止时的零值与指定功率阈值下温度-效率查找表提供的值之间平滑效率因子。

功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损失。然而，非常低的值可能会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

### R2025a：枚举更新

**Ring gear rotation** 参数现在使用复选框。此参数在之前的版本中使用下拉菜单。

## 描述

基于摆线盘运动的高传动比减速器

Cycloidal Drive 模块表示一种紧凑型高传动比减速机构，包含四个关键组件：

- 一个摆线盘
- 一个偏心凸轮
- 齿圈壳体
- 销滚子

从基轴延伸的偏心凸轮位于摆线盘内部。该盘与齿圈壳体啮合。从从动轴延伸的销滚子位于摆线盘上的匹配孔中。

在正常运行期间，基轴驱动偏心凸轮。凸轮在摆线盘内部旋转，使其围绕偏移轴线以偏心模式旋转。当其移动时，摆线盘与齿圈壳体的内齿啮合。内部啮合反转了旋转速度方向。

穿过摆线盘孔的销滚子将旋转运动传递到从动轴。该轴以非常低的速度与基轴反向旋转。高减速比源于摆线盘和齿圈齿数接近相等。模块计算有效齿轮减速比如下

r=nR−nCnC，

其中：

- *r* 是齿轮减速比。
- *nR* 是齿圈上的齿数。
- *nC* 是摆线盘上的齿数。

齿轮减速比根据以下表达式约束基轴和从动轴的角速度

ωF=−rωB，

其中：

- *ωF* 是从动轴的角速度。
- *ωC* 是基轴的角速度。

齿轮减速比还根据以下表达式约束作用在基轴和从动轴上的扭矩

TB=rTF+Tf，

其中：

- *TB* 是基轴上的净扭矩。
- *TF* 是从动轴上的净扭矩。
- *Tf* 是由于摩擦引起的扭矩损失。有关更多信息，请参阅 Model Gears with Losses。

该图显示了摆线驱动器的正视图和侧视图。驱动系统的运动学导致基轴和从动轴角速度反转，使得两个轴沿相反方向旋转。

摆线驱动器可以在反向模式下运行，即功率从从动轴流向基轴。在反向模式下，扭矩传递效率通常可以忽略不计。您可以通过更改 **Efficiency from follower shaft to base shaft** 参数的值来调整效率。

### 齿圈旋转

当您选择 **Ring gear rotation** 时，模块显示端口 **R**，允许您通过使用机械旋转输入信号来模拟齿圈的旋转运动。模块将此运动实现为

ωF=−rωB+(1+r)ωR

τB=rτF+τf

rτR=−(1+r)τB+τf

其中 *τr* 是齿圈上的净扭矩。这些图展示了向齿圈施加正弦波如何在保持基轴速度恒定的同时引起从动轴的小幅调整。

### 摩擦模型

您可以将 **Friction model** 设置为：

- `No meshing losses - suitable for HIL simulation`，忽略损失以保持适合 HIL 仿真的计算时间。
- `Constant efficiency`，允许您指定一个在仿真过程中保持恒定的组件效率。这是 R2020b 之前模块版本的默认摩擦设置。
- `Temperature-dependent efficiency`，通过基于 **Temperature** 向量和给定的组件效率向量创建一维查找表来模拟温度相关的组件效率。此设置还显示热守恒端口 **H**。端口 **H** 接收进入模块的热流，根据 **Thermal mass** 参数的值将其转换为模块温度。

### 热模型

您可以通过启用可选热端口来模拟热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 变量

使用 **Variables** 设置在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。
