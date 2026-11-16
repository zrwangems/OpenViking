---
type: simulink-block
title: 'Rotational Mechanical Converter (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Elements'
documentation_page: 'rotationalmechanicalconverterma'
documentation_source_path: 'ref/rotationalmechanicalconverterma.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Mechanical Converter (MA)

## 端口

### 输入

### **q** — 端口 R 相对于端口 C 的旋转，rad 物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到该关节的位置传感端口 **q**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

#### 依赖项

要启用此端口，请将 **界面旋转** 参数设置为 `Provide input signal from Multibody joint`。

### 输出

### **W** — 离开系统的冷凝速率，kg/s 物理信号

物理信号输出端口，用于测量离开系统的冷凝速率。此值不包括以水滴形式夹带的冷凝部分。

### **F** — 包含压力、温度、湿度和示踪气体水平数据的向量物理信号 物理信号向量

物理信号输出端口，输出向量信号。该向量包含组件内部的压力（单位 Pa）、温度（单位 K）、湿度水平和示踪气体水平测量值。使用 Measurement Selector (MA) 模块解包此向量信号。

### 守恒

### **A** — 转换器入口湿空气

与转换器入口关联的湿空气守恒端口。

### **H** — 转换器内部温度 热

与转换器内部湿空气混合物温度关联的热守恒端口。

### **R** — 杆机械旋转

与移动界面关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与转换器外壳关联的机械旋转守恒端口。

### **S** — 注入或提取湿气和示踪气体 湿空气源

将此端口连接到 Moisture & Trace Gas Sources 库中某个模块的端口 **S**，以添加或移除湿气和示踪气体。有关详细信息，请参阅使用 Moisture and Trace Gas Sources。

#### 依赖项

仅当将 **湿度和示踪气体源** 参数设置为 `Controlled` 时，此端口才可见。

## 参数

### 主要

### **机械方向** — 选择转换器方向 `Pressure at A causes positive rotation of R relative to C`（默认） | `Pressure at A causes negative rotation of R relative to C`

选择移动界面相对于转换器内部湿空气体积的对齐方式：

- `Pressure at A causes positive rotation of R relative to C` — 湿空气体积增加会导致端口 **R** 相对于端口 **C** 产生正旋转。
- `Pressure at A causes negative rotation of R relative to C` — 湿空气体积增加会导致端口 **R** 相对于端口 **C** 产生负旋转。

### **界面旋转** — 选择确定相对端口位置的方法 `Calculate from angular velocity of port R relative to port C`（默认） | `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 旋转的方法：

- `Calculate from angular velocity of port R relative to port C` — 基于模块方程，根据相对端口角速度计算旋转。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

### **初始界面旋转** — 仿真开始时端口 R 相对于端口 C 的旋转偏移 `0 m`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移。值 0 对应于初始湿空气体积等于 **死容积**。

#### 依赖项

当 **界面旋转** 参数设置为 `Calculate from angular velocity of port R relative to port C` 时启用。

- 如果 **机械方向** 为 `Pressure at A causes positive rotation of R relative to C`，则参数值必须大于或等于 0。
- 如果 **机械方向** 为 `Pressure at A causes negative rotation of R relative to C`，则参数值必须小于或等于 0。

### **界面体积排量** — 单位旋转所排开的湿空气体积 `0.01 m^3/rad`（默认）

移动界面每单位旋转所排开的湿空气体积。

### **死容积** — 界面旋转为 0 时的湿空气体积 `1e-5 m^3`（默认）

界面旋转为 0 时的湿空气体积。

### **端口 A 处的横截面积** — 转换器入口处垂直于流动路径的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于湿空气流动路径。

### **环境压力设定** — 选择环境压力的设定方法 `Atmospheric pressure`（默认） | `Specified pressure`

选择环境压力的设定方法：

- `Atmospheric pressure` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气压力。
- `Specified pressure` — 使用 **环境压力** 参数指定值。

### **环境压力** — 转换器外部压力 `0.101325 MPa`（默认）

转换器外部作用于转换器湿空气体积压力的压力。值为 0 表示转换器向真空膨胀。

#### 依赖项

当 **环境压力设定** 参数设置为 `Specified pressure` 时启用。

### 湿度和示踪气体

### **饱和时的相对湿度** — 高于该相对湿度时发生冷凝 `1`（默认）

高于该相对湿度时发生冷凝。

### **水蒸气冷凝时间常数** — 冷凝时间尺度 `1e-3 s`（默认） | positive scalar

过饱和湿空气体积通过冷凝析出多余水分而返回到饱和状态的特征时间尺度。

### **水滴蒸发时间常数** — 蒸发时间尺度 `1e-3 s`（默认） | positive scalar

水滴蒸发为蒸气的特征时间尺度。

### **以水滴形式夹带的冷凝物比例** — 水滴中冷凝物的比例 `1`（默认） | scalar in the range [0,1]

湿空气中以水滴形式夹带的冷凝物比例。

### **湿度和示踪气体源** — 对湿度和示踪气体水平建模 `None`（默认） | `Constant` | `Controlled`

此参数控制端口 **S** 的可见性，并提供以下选项用于对组件内部的湿度和示踪气体水平建模：

- `None` — 不向模块中注入湿气或示踪气体，也不从模块中提取湿气或示踪气体。端口 **S** 隐藏。这是默认值。
- `Constant` — 以恒定速率向模块中注入湿气和示踪气体，或从模块中提取湿气和示踪气体。Moisture Source (MA) 和 Trace Gas Source (MA) 模块中的相同参数将在模块界面的 **湿度和示踪气体** 部分中可用。端口 **S** 隐藏。
- `Controlled` — 以随时间变化的速率向模块中注入湿气和示踪气体，或从模块中提取湿气和示踪气体。端口 **S** 暴露。将 Controlled Moisture Source (MA) 和 Controlled Trace Gas Source (MA) 模块连接到此端口。

### **添加或移除的湿气** — 选择模块是以水蒸气还是水滴形式添加或移除湿气 `Water vapor`（默认） | `Water droplets`

选择模块是以水蒸气还是水滴形式添加或移除湿气。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`。

### **水蒸气从液体蒸发或冷凝为液体** — 模块添加或移除水蒸气的方式 `off`（默认） | `on`

选择模块添加或移除水蒸气的方式。如果清除此复选框，则所添加或移除湿气的焓对应于水蒸气的焓，该焓大于液态水的焓。

如果选中此复选框，则所添加或移除湿气的焓对应于液态水的焓，该焓小于水蒸气的焓。添加水蒸气时，水蒸气从液体蒸发，潜热由连接的流体体积提供。移除水蒸气时，水蒸气冷凝为液体，潜热释放到连接的流体体积。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`，并将 **添加或移除的湿气** 设置为 `Water vapor`。

### **湿气添加速率** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的水蒸气或水滴质量流量。正值向连接的湿空气体积添加湿气。负值从该体积中提取湿气。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`。

### **所添加湿气的温度设定** — 选择所添加湿气温度的设定方法 `Atmospheric temperature`（默认） | `Specified temperature`

选择湿气温度的设定方法：

- `Atmospheric temperature` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **所添加湿气的温度** 参数指定值。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`。

### **所添加湿气的温度** — 湿气温度 `293.15 K`（默认）

输入所需的所添加湿气温度。此温度在仿真期间保持恒定。模块仅使用此值计算所添加湿气的比焓。所移除湿气的比焓基于连接的湿空气体积的温度。

#### 依赖项

要启用此参数，请将 **所添加湿气的温度设定** 设置为 `Specified temperature`。

### **示踪气体添加速率** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的示踪气体质量流量。正值向连接的湿空气体积添加示踪气体。负值从该体积中提取示踪气体。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`。

### **所添加示踪气体的温度设定** — 选择所添加示踪气体温度的设定方法 `Atmospheric temperature`（默认） | `Specified temperature`

选择示踪气体温度的设定方法：

- `Atmospheric temperature` — 使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **所添加示踪气体的温度** 参数指定值。

#### 依赖项

要启用此参数，请将 **湿度和示踪气体源** 设置为 `Constant`。

### **所添加示踪气体的温度** — 示踪气体温度 `293.15 K`（默认）

输入所需的所添加示踪气体温度。此温度在仿真期间保持恒定。模块仅使用此值计算所添加示踪气体的比焓。所移除示踪气体的比焓基于连接的湿空气体积的温度。

#### 依赖项

要启用此参数，请将 **所添加示踪气体的温度设定** 设置为 `Specified temperature`。

### 初始条件

### **初始压力** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认） | positive scalar

仿真开始时的湿空气压力。

### **初始压力优先级** — 压力参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始压力** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **初始温度** — 仿真开始时的温度 `293.15 K`（默认） | positive scalar

初始湿空气温度。

### **初始温度优先级** — 温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始温度** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **初始湿度设定** — 湿度设定 `Relative humidity`（默认） | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

指定初始湿空气湿度的方法。

### **初始相对湿度** — 仿真开始时的相对湿度 `0.5`（默认） | scalar in the range of [0,1]

仿真开始时湿空气中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Relative humidity`。

### **初始相对湿度优先级** — 相对湿度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始相对湿度** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Relative humidity`。

### **初始比湿** — 仿真开始时的比湿 `0.01`（默认） | scalar in the range of [0,1]

仿真开始时湿空气中的比湿。比湿是水蒸气质量与水蒸气、示踪气体和干空气总质量之比。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Specific humidity`。

### **初始比湿优先级** — 比湿参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始比湿** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Specific humidity`。

### **初始水蒸气摩尔分数** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认） | scalar in the range [0,1]

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、示踪物质和干空气的总摩尔量而言的。

#### 依赖项

要启用此参数，请将 **初始湿度设定** 设置为 `Mole fraction`。

### **初始水蒸气摩尔分数优先级** — 水蒸气摩尔分数湿度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始水蒸气摩尔分数** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Mole fraction`。

### **初始湿度比** — 仿真开始时的湿度比 `0.01`（默认） | 范围 [0,1] 内的标量

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和痕量气体质量之比。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Humidity ratio`。

### **初始湿度比优先级** — 湿度比参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始湿度比** 参数的优先级。

将此参数设置为 `High` 可定义初始条件。如果此初始条件与另一个模块的初始条件冲突，你可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Humidity ratio`。

### **初始湿球温度** — 仿真开始时的湿球温度 `287 K`（默认） | 范围 [0,1] 内的标量

仿真开始时的湿球温度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Wet-bulb temperature`。

### **初始湿球温度优先级** — 湿球温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始湿球温度** 参数的优先级。

将此参数设置为 `High` 可定义初始条件。如果此初始条件与另一个模块的初始条件冲突，你可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Wet-bulb temperature`。

### **初始痕量气体规格** — 痕量气体的测量类型 `Mass fraction`（默认） | `Mole fraction`

痕量气体的测量类型。

### **初始痕量气体质量分数** — 湿空气通道中的痕量气体量 `0.001`（默认） | 范围 [0,1] 内的标量

仿真开始时按质量分数计的湿空气中痕量气体量。该质量分数相对于水蒸气、痕量气体和干空气的总质量。

如果 Moist Air Properties (MA) 模块中的 **痕量气体模型** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始痕量气体规格** 设置为 `Mass fraction`。

### **初始痕量气体质量分数优先级** — 痕量气体质量分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始痕量气体质量分数优先级** 参数的优先级。

将此参数设置为 `High` 可定义初始条件。如果此初始条件与另一个模块的初始条件冲突，你可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始痕量气体规格** 设置为 `Mass fraction`。

### **初始痕量气体摩尔分数** — 仿真开始时的痕量气体摩尔分数 `0.001`（默认） | 范围 [0,1] 内的标量

仿真开始时按摩尔分数计的湿空气通道中痕量气体量。该摩尔分数相对于水蒸气、痕量气体和干空气的总摩尔量。

如果 Moist Air Properties (MA) 模块中的 **痕量气体模型** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始痕量气体规格** 设置为 `Mole fraction`。

### **初始痕量气体摩尔分数优先级** — 痕量气体摩尔分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **初始痕量气体摩尔分数优先级** 参数的优先级。

将此参数设置为 `High` 可定义初始条件。如果此初始条件与另一个模块的初始条件冲突，你可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **初始痕量气体规格** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认） | 正标量

水滴与湿空气的初始质量比。

### **水滴与湿空气的初始质量比优先级** — 水滴与湿空气的质量比参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **水滴与湿空气的初始质量比优先级** 参数的优先级。

将此参数设置为 `High` 可定义初始条件。如果此初始条件与另一个模块的初始条件冲突，你可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：更新了初始条件选项

现在可以将模块的初始条件指定为参数。

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

## 描述

湿空气网络与机械旋转网络之间的接口

Rotational Mechanical Converter (MA) 模块对湿空气网络与机械旋转网络之间的接口进行建模。该模块将湿空气压力转换为机械扭矩，反之亦然。可将其用作旋转执行器的构建模块。

该转换器包含可变体积的湿空气。压力和温度根据该湿空气体积的可压缩性和热容演变。当湿空气体积达到饱和时，液态水会从中冷凝析出。**机械方向** 参数允许指定转换器内湿空气体积的增加是否导致端口 **R** 相对于端口 **C** 正向或负向旋转。

模块方程使用以下符号。下标 `a`、`w`、`g` 和 `d` 分别表示干空气、水蒸气、痕量气体和水滴的属性。下标 `ws` 表示饱和状态的水蒸气。下标 `A`、`H` 和 `S` 表示相应端口。下标 `I` 表示内部湿空气体积的属性。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流率 |
| *Q* | 热流率 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *V* | 转换器内湿空气的体积 |
| *c*p | 定容比热 |
| *h* | 比焓 |
| *u* | 比内能 |
| *x* | 质量分数（*x*w 是比湿度，它是水蒸气质量分数的另一种说法） |
| *y* | 摩尔分数 |
| *φ* | 相对湿度 |
| *r* | 湿度比 |
| *r*d | 水滴与湿空气的质量比 |
| *T* | 温度 |
| *t* | 时间 |

进入转换器内湿空气体积的净流率为

m˙net=m˙A−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

其中：

- m˙condense 是冷凝速率。
- m˙d,evap 是水滴蒸发速率。
- *Φ*condense 是冷凝水的能量损失率。
- *λd* 是 **冷凝物夹带为水滴的比例** 参数的值。
- *Φ*S 是水分和痕量气体源添加的能量率。m˙wS 和 m˙gS 分别是水和气体通过端口 **S** 的质量流率。m˙wS、m˙gS 和 *Φ*S 的值由连接到转换器端口 **S** 的水分和痕量气体源决定。

水蒸气质量守恒将水蒸气质量流率与内部湿空气体积中湿度水平的动态变化关联起来

dxwIdtρIV+xwIm˙net=m˙w,net

类似地，痕量气体质量守恒将痕量气体质量流率与内部湿空气体积中痕量气体水平的动态变化关联起来

dxgIdtρIV+xgIm˙net=m˙g,net

水滴质量守恒方程将水滴质量流率与内部湿空气体积中夹带水滴的动态变化关联起来

drdIdtρIV+rdIm˙net=m˙d,net.

混合物质量守恒将混合物质量流率与内部湿空气体积的压力、温度和质量分数的动态变化关联起来：

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)+ρIV˙=m˙net

其中 V˙ 是转换器体积的变化率。

最后，能量守恒将能量流率与内部湿空气体积的压力、温度和质量分数的动态变化关联起来：

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet−pIV˙

状态方程将混合物密度与压力和温度关联起来：

pI=ρIRITI

混合物比气体常数为

RI=xaIRa+xwIRw+xgIRg

转换器体积取决于运动界面的旋转：

V=Vdead+Dintθintεint

其中：

- *V*dead 是死区体积。
- *D*int 是界面体积位移。
- *θ*int 是界面旋转。
- *ε*int 是机械方向系数。如果 **机械方向** 为 `Pressure at A causes positive rotation of R relative to C`，则 *ε*int = 1。如果 **机械方向** 为 `Pressure at A causes negative rotation of R relative to C`，则 *ε*int = –1。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **q** 指定端口 **R** 相对于端口 **C** 的旋转。否则，模块根据相对端口角速度计算界面旋转。当转换器内的湿空气体积等于死区体积时，界面旋转为零。然后，根据 **机械方向** 参数值：

- 如果 `Pressure at A causes positive rotation of R relative to C`，则当湿空气体积从死区体积增加时，界面旋转增加。
- 如果 `Pressure at A causes negative rotation of R relative to C`，则当湿空气体积从死区体积增加时，界面旋转减小。

机械界面上的扭矩平衡为

τint=(penv−pI)Dintεint

其中：

- *τ*int 是从端口 **R** 到端口 **C** 的扭矩。
- *p*env 是环境压力。

转换器中未对流动阻力和热阻建模：

pA=pITH=TI

当湿空气体积达到饱和时，可能会发生冷凝。饱和状态下的比湿度为

xwsI=φwsRIRwpwsIpI

其中：

- *φ*ws 是饱和状态下的相对湿度（通常为 1）。
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
- 未对端口 **H** 与湿空气体积之间的热阻建模。使用 Thermal 库模块对湿空气混合物与环境之间的热阻建模，包括腔壁的任何热效应。
- 运动界面完全密封。
- 模块不对运动界面的机械效应建模，例如硬限位、摩擦和惯性。
