---
type: simulink-block
title: 'Constant Volume Chamber (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'constantvolumechamberma'
documentation_source_path: 'ref/constantvolumechamberma.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Volume Chamber (MA)

## 端口

### 输出

### **W** — 离开系统的冷凝速率，kg/s 物理信号

物理信号输出端口，用于测量离开系统的冷凝速率。此值不包括作为水滴夹带的那部分冷凝物。

### **F** — 包含压力、温度、湿度和微量气体水平数据的向量物理信号 physical signal vector

物理信号输出端口，输出一个向量信号。该向量包含组件内部的压力（单位 Pa）、温度（单位 K）、湿度水平和微量气体水平测量值。使用 Measurement Selector (MA) 模块解包此向量信号。

### 守恒

### **A** — 腔室入口湿空气

与腔室入口关联的湿空气守恒端口。

### **B** — 腔室入口湿空气

与第二个腔室入口关联的湿空气守恒端口。

#### 依赖关系

如果将 **Number of ports** 参数设置为 `2`、`3` 或 `4`，则此端口可见。

### **C** — 腔室入口湿空气

与第三个腔室入口关联的湿空气守恒端口。

#### 依赖关系

如果将 **Number of ports** 参数设置为 `3` 或 `4`，则此端口可见。

### **D** — 腔室入口湿空气

与第四个腔室入口关联的湿空气守恒端口。如果腔室有四个入口端口，您可以将其用作交叉连接中的连接点。

#### 依赖关系

仅当将 **Number of ports** 参数设置为 `4` 时，此端口才可见。

### **H** — 腔室内部温度 thermal

与腔室内空气混合物温度关联的热守恒端口。

### **S** — 注入或抽取湿度和微量气体的湿空气源

将此端口连接到 Moisture & Trace Gas Sources 库中模块的端口 **S**，以添加或移除湿度和微量气体。有关详细信息，请参阅 Using Moisture and Trace Gas Sources。

#### 依赖关系

仅当将 **Moisture and trace gas source** 参数设置为 `Controlled` 时，此端口才可见。

## 参数

### 主

### **Chamber volume** — 腔室内湿空气的体积 `0.001 m^3`（默认）

腔室内湿空气的体积。腔室是刚性的，因此其体积在仿真期间恒定。假设腔室始终完全充满湿空气。

### **Number of ports** — 腔室中入口端口的数量 `1`（默认）| `2` | `3` | `4`

腔室中入口端口的数量。腔室可以有一个到四个端口，标记为 **A** 到 **D**。修改参数值时，相应端口将在模块图标中显示或隐藏。

### **Cross-sectional area at port A** — 腔室入口处垂直于流路径的面积 `0.01 m^2`（默认）

端口 **A** 处腔室入口的横截面积，方向垂直于空气流路径。

### **Cross-sectional area at port B** — 腔室入口处垂直于流路径的面积 `0.01 m^2`（默认）

端口 **B** 处腔室入口的横截面积，方向垂直于空气流路径。

#### 依赖关系

当端口 **B** 可见时启用，即当 **Number of ports** 参数设置为 `2`、`3` 或 `4` 时。

### **Cross-sectional area at port C** — 腔室入口处垂直于流路径的面积 `0.01 m^2`（默认）

端口 **C** 处腔室入口的横截面积，方向垂直于空气流路径。

#### 依赖关系

当端口 **C** 可见时启用，即当 **Number of ports** 参数设置为 `3` 或 `4` 时。

### **Cross-sectional area at port D** — 腔室入口处垂直于流路径的面积 `0.01 m^2`（默认）

端口 **D** 处腔室入口的横截面积，方向垂直于空气流路径。

#### 依赖关系

当端口 **D** 可见时启用，即当 **Number of ports** 参数设置为 `4` 时。

### 湿度和微量气体

### **Relative humidity at saturation** — 发生冷凝所超过的相对湿度 `1`（默认）

发生冷凝所超过的相对湿度。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| positive scalar

过饱和湿空气体积通过冷凝出多余水分返回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| positive scalar

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 冷凝物中作为水滴夹带的比例 `1`（默认）| scalar in the range [0,1]

湿空气中作为水滴夹带的冷凝物比例。

### **Moisture and trace gas source** — 为湿度和微量气体水平建模 `None`（默认）| `Constant` | `Controlled`

此参数控制端口 **S** 的可见性，并提供以下用于为组件内部湿度和微量气体水平建模的选项：

- `None` — 不向模块中注入或从模块中抽取湿气或微量气体。端口 **S** 隐藏。这是默认值。
- `Constant` — 以恒定速率向模块中注入或从模块中抽取湿气和微量气体。Moisture Source (MA) 和 Trace Gas Source (MA) 模块中的相同参数将在模块界面的 **Moisture and Trace Gas** 部分中可用。端口 **S** 隐藏。
- `Controlled` — 以时变速率向模块中注入或从模块中抽取湿气和微量气体。端口 **S** 显示。将 Controlled Moisture Source (MA) 和 Controlled Trace Gas Source (MA) 模块连接到此端口。

### **Moisture added or removed** — 选择模块是作为水蒸气还是水滴添加或移除湿气 `Water vapor`（默认）| `Water droplets`

选择模块是作为水蒸气还是水滴添加或移除湿气。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Water vapor evaporated from liquid or condensed to liquid** — 模块如何添加或移除水蒸气 `off`（默认）| `on`

选择模块如何添加或移除水蒸气。如果清除此复选框，则添加或移除的湿气的焓对应于水蒸气的焓，该焓大于液态水的焓。

如果选中此复选框，则添加或移除的湿气的焓对应于液态水的焓，该焓小于水蒸气的焓。添加水蒸气时，它从液体蒸发，潜热由连接的流体体积提供。移除水蒸气时，它冷凝为液体，潜热释放到连接的流体体积。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`，并将 **Moisture added or removed** 设置为 `Water vapor`。

### **Rate of moisture added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的水蒸气或水滴质量流量。正值向连接的湿空气体积添加湿气。负值从该体积抽取湿气。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added moisture temperature specification** — 选择添加湿气温度的规定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择湿气温度的规定方法：

- `Atmospheric temperature` — 使用与回路连接的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **Temperature of added moisture** 参数指定值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added moisture** — 湿气温度 `293.15 K`（默认）

输入添加湿气的所需温度。此温度在仿真期间保持恒定。模块仅使用此值计算添加湿气的比焓。移除湿气的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`，并将 **Added moisture temperature specification** 设置为 `Specified temperature`。

### **Rate of trace gas added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的微量气体质量流量。正值向连接的湿空气体积添加微量气体。负值从该体积抽取微量气体。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added trace gas temperature specification** — 选择添加微量气体温度的规定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择微量气体温度的规定方法：

- `Atmospheric temperature` — 使用与回路连接的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` — 使用 **Temperature of added trace gas** 参数指定值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added trace gas** — 微量气体温度 `293.15 K`（默认）

输入添加微量气体的所需温度。此温度在仿真期间保持恒定。模块仅使用此值计算添加微量气体的比焓。移除微量气体的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`，并将 **Added trace gas temperature specification** 设置为 `Specified temperature`。

### 初始条件

### **Initial pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时的湿空气压力。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial pressure** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| positive scalar

初始湿空气温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial temperature** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial humidity specification** — 湿度规格 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

用于指定初始湿空气湿度的方法。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| scalar in the range of [0,1]

仿真开始时湿空气中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial relative humidity priority** — 相对湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial relative humidity** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿 `0.01`（默认）| scalar in the range of [0,1]

仿真开始时湿空气中的比湿。比湿是水蒸气质量与总质量（水蒸气、微量气体和干空气的总和）的质量分数。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial specific humidity priority** — 比湿参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial specific humidity** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial water vapor mole fraction** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认）| scalar in the range [0,1]

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、微量物种和干空气的组合摩尔量。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial water vapor mole fraction priority** — 水蒸气摩尔分数湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial water vapor mole fraction** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| scalar in the range [0,1]

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和微量气体质量之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial humidity ratio priority** — 湿度比参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时为 **Initial humidity ratio humidity** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| scalar in the range [0,1]

仿真开始时的湿球温度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial wet-bulb temperature priority** — 湿球温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时为 **Initial wet-bulb temperature** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 示踪气体的测量类型 `Mass fraction`（默认） | `Mole fraction`

示踪气体的测量类型。

### **Initial trace gas mass fraction** — 湿空气通道中示踪气体的量 `0.001`（默认） | scalar，范围为 [0,1]

仿真开始时湿空气中示踪气体的质量分数量。质量分数相对于水蒸气、示踪气体和干空气的组合总质量。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则该模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mass fraction priority** — 示踪气体质量分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时为 **Initial trace gas mass fraction priority** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mole fraction** — 仿真开始时示踪气体的摩尔分数 `0.001`（默认） | scalar，范围为 [0,1]

仿真开始时湿空气通道中示踪气体的摩尔分数量。摩尔分数相对于水蒸气、示踪气体和干空气的组合摩尔总量。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则该模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial trace gas mole fraction priority** — 示踪气体摩尔分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时为 **Initial trace gas mole fraction priority** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的比率 `0`（默认） | positive scalar

水滴与湿空气的初始质量比。

### **Initial mass ratio of water droplets to moist air priority** — 水滴与湿空气质量比参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时为 **Initial mass ratio of water droplets to moist air priority** 参数分配的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2018a 中引入**

### R2024b：更新了初始条件选项

现在可以将模块的初始条件指定为参数。

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

具有固定湿空气体积和可变端口数量的腔室

Constant Volume Chamber (MA) 模块对湿空气网络中的质量和能量存储进行建模。该腔室包含恒定体积的湿空气。它可以有一个到四个入口。该封闭空间可以与连接的湿空气网络交换质量和能量，并与环境交换热量，使其内部压力和温度随时间演变。压力和温度基于湿空气体积的可压缩性和热容量演变。当湿空气体积达到饱和时，液态水会从中冷凝出来。

模块方程使用以下符号。下标 `a`、`w`、`g` 和 `d` 分别表示干空气、水蒸气、示踪气体和水滴的属性。下标 `ws` 表示饱和状态下的水蒸气。下标 `A`、`H` 和 `S` 表示相应的端口。下标 `I` 表示内部湿空气体积的属性。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流量 |
| *Q* | 热流量 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *V* | 腔室内湿空气的体积 |
| *c*p | 定容比热 |
| *h* | 比焓 |
| *u* | 比内能 |
| *x* | 质量分数（*x*w 是比湿度，是水蒸气质量分数的另一个术语） |
| *y* | 摩尔分数 |
| *φ* | 相对湿度 |
| *r* | 含湿量 |
| *r*d | 水滴与湿空气的质量比 |
| *T* | 温度 |
| *t* | 时间 |

进入腔室内湿空气体积的净流量为

m˙net=m˙A+m˙B+m˙C+m˙D−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+ΦB+ΦC+ΦD+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA+m˙wB+m˙wC+m˙wD−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gB+m˙gC+m˙gD+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

其中：

- m˙condense 是冷凝速率。
- m˙d,evap 是水滴蒸发速率。
- *Φ*condense 是冷凝水能量损失速率。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。
- *Φ*S 是由水分和示踪气体源添加能量的速率。m˙wS 和 m˙gS 分别是水和气体通过端口 **S** 的质量流量。m˙wS、m˙gS 和 *Φ*S 的值由连接到腔室端口 **S** 的水分和示踪气体源确定，或由相应参数值确定。

如果某个端口不可见，则带有与该端口名称对应下标的各项均为 0。

水蒸气质量守恒将水蒸气质量流量与内部湿空气体积中湿度的动态变化相关联：

dxwIdtρIV+xwIm˙net=m˙w,net

类似地，示踪气体质量守恒将示踪气体质量流量与内部湿空气体积中示踪气体水平的动态变化相关联：

dxgIdtρIV+xgIm˙net=m˙g,net

水滴质量守恒方程将水滴质量流量与内部湿空气体积中被夹带水滴的动态变化相关联

drdIdtρIV+rdIm˙net=m˙d,net.

混合物质量守恒将混合物质量流量与内部湿空气体积的压力、温度和质量分数的动态变化相关联：

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)=m˙net

最后，能量守恒将能量流量与内部湿空气体积的压力、温度和质量分数的动态变化相关联：

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet

状态方程将混合物密度与压力和温度相关联：

pI=ρIRITI

混合物比气体常数为

RI=xaIRa+xwIRw+xgIRg

腔室中不建模流动阻力和热阻：

pA=pB=pC=pD=pITH=TI

当湿空气体积达到饱和时，可能发生冷凝。饱和时的比湿度为

xwsI=φwsRIRwpwsIpI

其中：

- *φ*ws 是饱和时的相对湿度（通常为 1）。
- *p*wsI 是在 *T*I 处计算的水蒸气饱和压力。

冷凝速率为

m˙condense={0,if xwI≤xwsIxwI−xwsIτcondenseρIV,if xwI>xwsI

其中 *τ*condense 是 **Water vapor condensation time constant** 参数的值。

蒸发速率为

m˙d,evap=xwsI−xwIxwsIτevaprdIρIV,

其中 *τ*evap 是 **Water droplets evaporation time constant** 参数的值。

### 假设与限制

- 腔室壁完全刚性。
- 不建模腔室入口与湿空气体积之间的流动阻力。将 Local Restriction (MA) 模块或 Flow Resistance (MA) 模块连接到端口 **A**，以建模与入口相关的压力损失。
- 不建模端口 **H** 与湿空气体积之间的热阻。使用 Thermal 库模块来建模湿空气混合物与环境之间的热阻，包括腔室壁的任何热效应。
