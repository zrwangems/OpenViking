---
type: simulink-block
title: 'Translational Mechanical Converter (MA)'
family: 'moist-air'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'translationalmechanicalconverterma'
documentation_source_path: 'ref/translationalmechanicalconverterma.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Mechanical Converter (MA)

## 端口

### 输入

### **p** — 端口 R 相对于端口 C 的位移，m 物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **p**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

#### 依赖关系

要启用此端口，请将 **Interface displacement** 参数设置为 `Provide input signal from Multibody joint`。

### 输出

### **W** — 离开系统的冷凝速率，kg/s 物理信号

物理信号输出端口，用于测量离开系统的冷凝速率。此值不包括以水滴形式夹带的冷凝部分。

### **F** — 包含压力、温度、湿度和痕量气体水平数据的向量物理信号 物理信号向量

物理信号输出端口，用于输出向量信号。该向量包含组件内部的压力（单位为 Pa）、温度（单位为 K）、湿度水平和痕量气体水平测量值。使用 Measurement Selector (MA) 模块解包此向量信号。

### 守恒

### **A** — 转换器入口湿空气

与转换器入口关联的湿空气守恒端口。

### **H** — 转换器内部温度 热

与转换器内湿空气混合物的温度关联的热守恒端口。

### **R** — 杆 机械平移

与运动界面关联的机械平移守恒端口。

### **C** — 壳体 机械平移

与转换器壳体关联的机械平移守恒端口。

### **S** — 注入或抽出湿气和痕量气体 湿空气源

将此端口连接到 Moisture & Trace Gas Sources 库中某个模块的端口 **S**，以添加或移除湿气和痕量气体。有关详细信息，请参阅使用湿气和痕量气体源。

#### 依赖关系

仅当您将 **Moisture and trace gas source** 参数设置为 `Controlled` 时，此端口才可见。

## 参数

### 主要

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

选择转换器相对于转换器内湿空气体积的相对方向：

- `Pressure at A causes positive displacement of R relative to C` — 湿空气体积增加会导致端口 **R** 相对于端口 **C** 产生正位移。
- `Pressure at A causes negative displacement of R relative to C` — 湿空气体积增加会导致端口 **R** 相对于端口 **C** 产生负位移。

### **Interface displacement** — 选择确定相对端口位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 的位移的方法：

- `Calculate from velocity of port R relative to port C` — 根据模块方程，从相对端口速度计算位移。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **p**，以传递来自 Multibody 关节的位移信息。仅当您使用 Translational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

### **Initial interface displacement** — 仿真开始时端口 R 相对于端口 C 的平移偏移量 `0 m`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的平移偏移量。值 0 对应于初始湿空气体积等于 **Dead volume**。

#### 依赖关系

当 **Interface displacement** 参数设置为 `Calculate from velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive displacement of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative displacement of R relative to C`，则参数值必须小于或等于 0。

### **Interface cross-sectional area** — 湿空气施加压力以产生平移力的面积 `0.01 m^2`（默认）

湿空气施加压力以产生平移力的面积。

### **Dead volume** — 当界面位移为 0 时的湿空气体积 `1e-5 m^3`（默认）

当界面位移为 0 时的湿空气体积。

### **Cross-sectional area at port A** — 转换器入口处垂直于流路的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于空气流路。

### **Environment pressure specification** — 选择环境压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择环境压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气压。
- `Specified pressure` — 使用 **Environment pressure** 参数指定值。

### **Environment pressure** — 转换器外部压力 `0.101325 MPa`（默认）

转换器外部作用于转换器湿空气体积压力的压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。

### 湿气和痕量气体

### **Relative humidity at saturation** — 发生冷凝所高于的相对湿度 `1`（默认）

发生冷凝所高于的相对湿度。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝析出多余水分而恢复到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 冷凝物中水滴形式夹带的比例 `1`（默认）| 范围 [0,1] 内的标量

湿空气中以水滴形式夹带的冷凝物的比例。

### **Moisture and trace gas source** — 对湿气和痕量气体水平建模 `None`（默认）| `Constant` | `Controlled`

此参数控制端口 **S** 的可见性，并提供以下选项来对组件内部的湿气和痕量气体水平建模：

- `None` — 不会向模块注入湿气或痕量气体，也不会从模块抽出湿气或痕量气体。端口 **S** 隐藏。这是默认设置。
- `Constant` — 以恒定速率向模块注入湿气和痕量气体，或从模块抽出湿气和痕量气体。Moisture Source (MA) 和 Trace Gas Source (MA) 模块中的相同参数将在模块界面的 **Moisture and Trace Gas** 部分中可用。端口 **S** 隐藏。
- `Controlled` — 以随时间变化的速率向模块注入湿气和痕量气体，或从模块抽出湿气和痕量气体。端口 **S** 会显示。将 Controlled Moisture Source (MA) 和 Controlled Trace Gas Source (MA) 模块连接到此端口。

### **Moisture added or removed** — 选择模块是以水蒸气还是水滴形式添加或移除湿气 `Water vapor`（默认）| `Water droplets`

选择模块是以水蒸气还是水滴形式添加或移除湿气。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Water vapor evaporated from liquid or condensed to liquid** — 模块如何添加或移除水蒸气 `off`（默认）| `on`

选择模块如何添加或移除水蒸气。如果清除此复选框，则添加或移除的湿度的焓对应于水蒸气的焓，该焓大于液态水的焓。

如果选中此复选框，则添加或移除的湿度的焓对应于液态水的焓，该焓小于水蒸气的焓。添加水蒸气时，水蒸气从液体蒸发，潜热由连接的流体体积提供。移除水蒸气时，水蒸气冷凝为液体，潜热释放到连接的流体体积。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`，并将 **Moisture added or removed** 设置为 `Water vapor`。

### **Rate of moisture added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的水蒸气或水滴质量流量。正值会向连接的湿空气体积添加湿气。负值会从该体积抽出湿气。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added moisture temperature specification** — 选择添加湿气的温度的指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择湿气温度的指定方法：

- `Atmospheric temperature` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **Temperature of added moisture** 参数指定值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added moisture** — 湿气温度 `293.15 K`（默认）

输入添加湿气的所需温度。此温度在仿真期间保持恒定。模块仅使用此值计算添加湿气的比焓。移除湿气的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Added moisture temperature specification** 设置为 `Specified temperature`。

### **Rate of trace gas added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的痕量气体质量流量。正值会向连接的湿空气体积添加痕量气体。负值会从该体积抽出痕量气体。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added trace gas temperature specification** — 选择添加痕量气体的温度的指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择痕量气体温度的指定方法：

- `Atmospheric temperature` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **Temperature of added trace gas** 参数指定值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added trace gas** — 痕量气体温度 `293.15 K`（默认）

输入添加痕量气体的所需温度。此温度在仿真期间保持恒定。模块仅使用此值计算添加痕量气体的比焓。移除痕量气体的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Added trace gas temperature specification** 设置为 `Specified temperature`。

### 初始条件

### **Initial pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气压力。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial pressure** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量

初始湿空气温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial temperature** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial humidity specification** — 湿度指定 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

指定初始湿空气湿度的方法。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial relative humidity priority** — 相对湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial relative humidity** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中的比湿。比湿是水蒸气质量与水蒸气、痕量气体和干空气总质量之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial specific humidity priority** — 比湿参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial specific humidity** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、痕量组分和干空气的总摩尔量而言的。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **初始水蒸气摩尔分数优先级** — 水蒸气摩尔分数湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **初始水蒸气摩尔分数** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度指定** 设置为 `Mole fraction`。

### **初始湿度比** — 仿真开始时的湿度比 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和微量气体质量之比。

#### 依赖关系

要启用此参数，请将 **初始湿度指定** 设置为 `Humidity ratio`。

### **初始湿度比优先级** — 湿度比参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **初始湿度比湿度** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度指定** 设置为 `Humidity ratio`。

### **初始湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的标量

仿真开始时的湿球温度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请将 **初始湿度指定** 设置为 `Wet-bulb temperature`。

### **初始湿球温度优先级** — 湿球温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **初始湿球温度** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度指定** 设置为 `Wet-bulb temperature`。

### **初始微量气体指定** — 微量气体的测量类型 `Mass fraction`（默认）| `Mole fraction`

微量气体的测量类型。

### **初始微量气体质量分数** — 湿空气通道中微量气体的量 `0.001`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中微量气体按质量分数的量。质量分数相对于水蒸气、微量气体和干空气的组合总质量。

如果 Moist Air Properties (MA) 模块中的 **微量气体模型** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始微量气体指定** 设置为 `Mass fraction`。

### **初始微量气体质量分数优先级** — 微量气体质量分数参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **初始微量气体质量分数优先级** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始微量气体指定** 设置为 `Mass fraction`。

### **初始微量气体摩尔分数** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中微量气体按摩尔分数的量。摩尔分数相对于水蒸气、微量气体和干空气的组合摩尔总量。

如果 Moist Air Properties (MA) 模块中的 **微量气体模型** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始微量气体指定** 设置为 `Mole fraction`。

### **初始微量气体摩尔分数优先级** — 微量气体摩尔分数参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **初始微量气体摩尔分数优先级** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始微量气体指定** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **水滴与湿空气的初始质量比优先级** — 水滴与湿空气质量比参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时赋予 **水滴与湿空气的初始质量比优先级** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，则可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b: 更新了初始条件选项

现在可以将模块的初始条件指定为参数。

### R2024b: 对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

## 描述

湿空气与机械平移网络之间的接口

Translational Mechanical Converter (MA) 模块对湿空气网络与机械平移网络之间的接口进行建模。该模块将湿空气压力转换为机械力，反之亦然。您可以将其用作线性执行器的构建块。

转换器包含可变体积的湿空气。压力和温度基于该湿空气体积的可压缩性和热容量演化。当湿空气体积达到饱和时，液态水会从中冷凝析出。**机械方向** 参数允许您指定转换器内湿空气体积的增加是否导致端口 **R** 相对于端口 **C** 的正位移或负位移。

模块方程使用这些符号。下标 `a`、`w`、`g` 和 `d` 分别表示干空气、水蒸气、微量气体和水滴的属性。下标 `ws` 表示饱和水蒸气。下标 `A`、`H` 和 `S` 表示相应的端口。下标 `I` 表示内部湿空气体积的属性。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流量 |
| *Q* | 热流量 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *V* | 转换器内湿空气的体积 |
| *c*p | 定容比热 |
| *h* | 比焓 |
| *u* | 比内能 |
| *x* | 质量分数（*x*w 是比湿度，这是水蒸气质量分数的另一种说法） |
| *y* | 摩尔分数 |
| *φ* | 相对湿度 |
| *r* | 湿度比 |
| *r*d | 水滴与湿空气的质量比 |
| *T* | 温度 |
| *t* | 时间 |

转换器内湿空气体积的净流量为

m˙net=m˙A−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

其中：

- m˙condense 是冷凝速率。
- m˙d,evap 是水滴蒸发速率。
- *Φ*condense 是冷凝水能量损失速率。
- *λd* 是 **夹带为水滴的冷凝物比例** 参数的值。
- *Φ*S 是由水分和微量气体源添加的能量速率。m˙wS 和 m˙gS 分别是通过端口 **S** 的水和气体的质量流量。m˙wS、m˙gS 和 *Φ*S 的值由连接到转换器端口 **S** 的水分和微量气体源决定。

水蒸气质量守恒将水蒸气质量流量与内部湿空气体积中湿度水平的动态变化联系起来

dxwIdtρIV+xwIm˙net=m˙w,net

类似地，微量气体质量守恒将微量气体质量流量与内部湿空气体积中微量气体水平的动态变化联系起来

dxgIdtρIV+xgIm˙net=m˙g,net

水滴质量守恒方程将水滴质量流量与内部湿空气体积中夹带水滴的动态变化联系起来

drdIdtρIV+rdIm˙net=m˙d,net.

混合物质量守恒将混合物质量流量与内部湿空气体积的压力、温度和质量的动态变化联系起来：

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)+ρIV˙=m˙net

其中 V˙ 是转换器体积的变化率。

最后，能量守恒将能量流量与内部湿空气体积的压力、温度和质量的动态变化联系起来：

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet−pIV˙

状态方程将混合物密度与压力和温度联系起来：

pI=ρIRITI

混合物比气体常数为

RI=xaIRa+xwIRw+xgIRg

转换器体积为

V=Vdead+Sintdintεint

其中：

- *V*dead 是死体积。
- *S*int 是接口横截面积。
- *d*int 是接口位移。
- *ε*int 是机械方向系数。如果 **机械方向** 为 `Pressure at A causes positive displacement of R relative to C`，则 *ε*int = 1。如果 **机械方向** 为 `Pressure at A causes negative displacement of R relative to C`，则 *ε*int = –1。

如果将转换器连接到 Multibody joint，请使用物理信号输入端口 **p** 指定端口 **R** 相对于端口 **C** 的位移。否则，模块根据相对端口速度计算接口位移。当转换器内的湿空气体积等于死体积时，接口位移为零。然后，根据 **机械方向** 参数值：

- 如果 `Pressure at A causes positive displacement of R relative to C`，则当湿空气体积从死体积增加时，接口位移增加。
- 如果 `Pressure at A causes negative displacement of R relative to C`，则当湿空气体积从死体积增加时，接口位移减少。

机械接口上的力平衡为

Fint=(penv−pI)Sintεint

其中：

- *F*int 是从端口 **R** 到端口 **C** 的力。
- *p*env 是环境压力。

转换器中未对流动阻力和热阻力建模：

pA=pITH=TI

当湿空气体积达到饱和时，可能发生冷凝。饱和时的比湿度为

xwsI=φwsRIRwpwsIpI

其中：

- *φ*ws 是饱和时的相对湿度（通常为 1）。
- *p*wsI 是在 *T*I 处计算的水蒸气饱和压力。

冷凝速率为

m˙condense={0,if xwI≤xwsIxwI−xwsIτcondenseρIV,if xwI>xwsI

其中 *τ*condense 是 **水蒸气冷凝时间常数** 参数的值。

蒸发速率为

m˙d,evap=xwsI−xwIxwsIτevaprdIρIV,

其中 *τ*evap 是 **水滴蒸发时间常数** 参数的值。

### 假设和限制

- 转换器外壳完全刚性。
- 未对转换器入口与湿空气体积之间的流动阻力建模。将 Local Restriction (MA) 模块或 Flow Resistance (MA) 模块连接到端口 **A**，以对与入口相关的压力损失建模。
- 未对端口 **H** 与湿空气体积之间的热阻力建模。使用 Thermal 库模块对湿空气混合物与环境之间的热阻力建模，包括腔壁的任何热效应。
- 移动接口完全密封。
- 模块不对移动接口的机械效应建模，例如硬限位、摩擦和惯性。
