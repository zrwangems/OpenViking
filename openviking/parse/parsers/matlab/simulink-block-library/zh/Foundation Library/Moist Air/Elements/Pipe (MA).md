---
type: simulink-block
title: 'Pipe (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'pipema'
documentation_source_path: 'ref/pipema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (MA)

## 端口

### 输出

### **W** — 离开系统的冷凝速率，kg/s，物理信号

物理信号输出端口，用于测量离开系统的冷凝速率。如果选择 **Condensation on wall surface**，则该端口报告水蒸气冷凝的总速率，其中包括来自饱和湿空气体积的冷凝以及管壁上的冷凝。该值不包括以水滴形式夹带的冷凝部分。

### **F** — 包含压力、温度、湿度和微量气体水平数据的矢量物理信号，物理信号矢量

物理信号输出端口，输出矢量信号。该矢量包含组件内部的压力（单位为 Pa）、温度（单位为 K）、湿度水平和微量气体水平测量值。使用 Measurement Selector (MA) 模块来解包该矢量信号。
### 守恒

### **A** — 入口或出口湿空气

与管道入口或出口相关联的湿空气守恒端口。该模块没有固有方向性。

### **B** — 入口或出口湿空气

与管道入口或出口相关联的湿空气守恒端口。该模块没有固有方向性。

### **H** — 管壁温度，热

与管壁温度相关联的热守恒端口。该模块包括管道内湿空气混合物与管壁之间的对流传热。

### **S** — 注入或抽出湿气和微量气体，湿空气源

将该端口连接到 Moisture & Trace Gas Sources 库中某个模块的端口 **S**，以添加或移除湿气和微量气体。有关详细信息，请参阅 Using Moisture and Trace Gas Sources。

#### 依赖关系

仅当将 **Moisture and trace gas source** 参数设置为 `Controlled` 时，该端口才可见。

## 参数

### 主要

### **Pipe length** — 管道长度 `5 m`（默认值）

沿流动方向的管道长度。

### **Cross-sectional area** — 管道内部面积 `0.01 m^2`（默认值）

垂直于流动方向的管道内部面积。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱形管道直径 `0.1 m`（默认值）

具有相同横截面积的等效圆柱形管道直径。

### 摩擦与传热

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的总长度 `0.1 m`（默认值）

管道中所有局部阻力的总长度。局部阻力包括弯头、管件、附件以及管道入口和出口。局部阻力的作用是增加管段的等效长度。该长度仅在摩擦计算中加到管道几何长度上。湿空气体积仅取决于由 **Pipe length** 参数定义的管道几何长度。

### **Internal surface absolute roughness** — 管道内表面所有表面缺陷的平均深度 `15e-6 m`（默认值）

管道内表面所有表面缺陷的平均深度，这会影响湍流流态下的压力损失。

### **Laminar flow upper Reynolds number limit** — 流动开始从层流过渡到湍流时的雷诺数上限 `2000`（默认值）

流动开始从层流过渡到湍流时的雷诺数上限。该数值等于完全发展层流所对应的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 流动开始从湍流过渡到层流时的雷诺数下限 `4000`（默认值）

流动开始从湍流过渡到层流时的雷诺数下限。该数值等于完全发展湍流所对应的最小雷诺数。

### **层流黏性摩擦的形状因子** — 管道几何形状对黏性摩擦损失的影响 `64`（默认值）

无量纲因子，用于表征管道横截面几何形状对层流流态下黏性摩擦损失的影响。
典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### **层流换热努塞尔数** — 对流传热与导热传热之比 `3.66`（默认值）

层流流态下对流传热与导热传热之比。其值取决于管道横截面几何形状和管壁热边界条件，例如恒定温度或恒定热通量。典型值为 3.66，适用于恒定壁温的圆形横截面 [2]。

### 湿度和微量气体

### **壁面冷凝** — 对与湿空气体积接触的冷管表面上的壁面冷凝效应进行建模 `Off`（默认值）| `On`

选中此复选框可对与湿空气体积接触的冷管表面上的壁面冷凝效应进行建模。有关详细信息，请参阅壁面冷凝效应。
在默认配置下，该模块不对该效应进行建模，仅在 100% 相对湿度下考虑水蒸气冷凝，如对流换热和饱和与冷凝中所述。

### **饱和时的相对湿度** — 发生冷凝时高于该值的相对湿度 `1`（默认值）

发生冷凝时高于该值的相对湿度。

### **水蒸气冷凝时间常数** — 冷凝的时间尺度 `1e-3 s`（默认值）| 正标量

过饱和湿空气体积通过冷凝多余水分恢复至饱和状态的特征时间尺度。

### **水滴蒸发时间常数** — 蒸发的时间尺度 `1e-3 s`（默认值）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **以水滴形式夹带的冷凝液比例** — 水滴中冷凝液的比例 `1`（默认值）| 范围 [0,1] 内的标量

湿空气中以水滴形式夹带的冷凝液比例。

### **湿度和微量气体源** — 对湿度和微量气体水平进行建模 `None`（默认值）| `Constant` | `Controlled`

此参数控制端口 **S** 的可见性，并提供以下选项用于对组件内部的湿度和微量气体水平进行建模：

- `None` — 不向模块中注入或从模块中提取湿气或微量气体。端口 **S** 隐藏。此为默认值。
- `Constant` — 以恒定速率向模块中注入或从模块中提取湿气和微量气体。与湿气源 (MA) 和微量气体源 (MA) 模块中相同的参数将在模块界面的 **湿度和微量气体** 部分中可用。端口 **S** 隐藏。
- `Controlled` — 以时变速率向模块中注入或从模块中提取湿气和微量气体。端口 **S** 暴露。将受控湿气源 (MA) 和受控微量气体源 (MA) 模块连接到此端口。

### **添加或移除湿气** — 选择模块以水蒸气还是水滴的形式添加或移除湿气 `Water vapor`（默认值）| `Water droplets`

选择模块以水蒸气还是水滴的形式添加或移除湿气。

#### 依赖关系

要启用此参数，请将 **湿度和微量气体源** 设置为 `Constant`。

### **Water vapor evaporated from liquid or condensed to liquid** — 模块如何添加或移除水蒸气 `off`（默认）| `on`

选择模块如何添加或移除水蒸气。如果清除此复选框，则添加或移除的水分的焓对应于水蒸气的焓，其大于液态水的焓。

如果选中此复选框，则添加或移除的水分的焓对应于液态水的焓，其小于水蒸气的焓。当添加水蒸气时，它从液体中蒸发，潜热由连接的流体体积提供。当移除水蒸气时，它凝结为液体，潜热释放到连接的流体体积。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`，并将 **Moisture added or removed** 设置为 `Water vapor`。

### **Rate of moisture added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的水蒸气或水滴质量流量。正值向连接的湿空气体积添加水分。负值从该体积中提取水分。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added moisture temperature specification** — 选择添加水分的温度指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择水分温度的指定方法：

- `Atmospheric temperature` —
  使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` —
  使用 **Temperature of added moisture** 参数指定一个值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added moisture** — 水分温度 `293.15 K`（默认）

输入所需的添加水分温度。该温度在仿真期间保持恒定。模块仅使用此值来计算添加水分的比焓。移除水分的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Added moisture temperature specification** 设置为 `Specified temperature`。

### **Rate of trace gas added** — 通过模块的恒定质量流量 `0 kg/s`（默认）

通过模块的示踪气体质量流量。正值向连接的湿空气体积添加示踪气体。负值从该体积中提取示踪气体。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Added trace gas temperature specification** — 选择添加示踪气体的温度指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

选择示踪气体温度的指定方法：

- `Atmospheric temperature` —
  使用由连接到回路的 Moist Air Properties (MA) 模块指定的大气温度。
- `Specified temperature` —
  使用 **Temperature of added trace gas** 参数指定一个值。

#### 依赖关系

要启用此参数，请将 **Moisture and trace gas source** 设置为 `Constant`。

### **Temperature of added trace gas** — 示踪气体温度 `293.15 K`（默认）

输入所需的添加示踪气体温度。该温度在仿真期间保持恒定。模块仅使用此值来计算添加示踪气体的比焓。移除示踪气体的比焓基于连接的湿空气体积的温度。

#### 依赖关系

要启用此参数，请将 **Added trace gas temperature specification** 设置为 `Specified temperature`。

### 初始条件

### **Initial pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气压力。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量

初始湿空气温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

### **Initial humidity specification** — 湿度指定方式 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

指定初始湿空气湿度的方法。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial relative humidity priority** — 相对湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial relative humidity** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中的比湿度。比湿度是水蒸气质量与水蒸气、微量气体和干空气总质量之比。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial specific humidity priority** — 比湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial specific humidity** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、微量组分和干空气的总摩尔量而言的。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **初始水蒸气摩尔分数优先级** — 水蒸气摩尔分数湿度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给**初始水蒸气摩尔分数**参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将**初始湿度设定**设置为 `Mole fraction`。

### **初始含湿量** — 仿真开始时的含湿量 `0.01`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中的含湿量。含湿量是水蒸气质量与干空气和微量气体质量之比。

#### 依赖关系

要启用此参数，请将**初始湿度设定**设置为 `Humidity ratio`。

### **初始含湿量优先级** — 含湿量参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给**初始含湿量湿度**参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将**初始湿度设定**设置为 `Humidity ratio`。

### **初始湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的标量

仿真开始时的湿球温度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请将**初始湿度设定**设置为 `Wet-bulb temperature`。

### **初始湿球温度优先级** — 湿球温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给**初始湿球温度**参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将**初始湿度设定**设置为 `Wet-bulb temperature`。

### **初始微量气体设定** — 微量气体的测量类型 `Mass fraction`（默认）| `Mole fraction`

微量气体的测量类型。

### **初始微量气体质量分数** — 湿空气通道中的微量气体量 `0.001`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气中微量气体的质量分数。质量分数是相对于水蒸气、微量气体和干空气的总质量而言的。

如果 Moist Air Properties (MA) 模块中的**微量气体模型**参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将**初始微量气体设定**设置为 `Mass fraction`。

### **初始微量气体质量分数优先级** — 微量气体质量分数参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给**初始微量气体质量分数优先级**参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将**初始微量气体设定**设置为 `Mass fraction`。

### **初始痕量气体摩尔分数** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

仿真开始时湿空气通道中痕量气体的摩尔分数。该摩尔分数是相对于水蒸气、痕量气体和干空气的总摩尔量而言的。

如果湿空气属性 (MA) 模块中的 **Trace gas model** 参数为 `None`，则该模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **初始痕量气体摩尔分数优先级** — 痕量气体摩尔分数参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial trace gas mole fraction priority** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气的比值 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **水滴与湿空气的初始质量比优先级** — 水滴与湿空气的质量比参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial mass ratio of water droplets to moist air priority** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：更新了初始条件选项

您现在可以将模块的初始条件指定为参数。

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的湿空气属性 (MA) 模块中选择 **Enable entrained water droplets**。

### R2024a：管道低流量计算的数值改进

为了提高管道内低速流动时压降的精度，Pipe (MA) 模块中的动量平衡计算已略有更改。与之前的版本相比，仿真结果可能会有细微差异，尤其是在马赫数较低时。

### R2022b：对壁面冷凝效应进行建模

该模块新增了一个参数 **Condensation on wall surface**，可让您对与湿空气体积接触的冷管表面上的壁面冷凝效应进行建模。有关详细信息，请参阅 Effect of Condensation on Wall Surface。在默认配置中，此参数设置为 `Off`，模块的功能与之前版本相同。

在 R2023b 中，此参数已替换为复选框。默认值和模块功能与之前版本相同。

## 描述

湿空气流动的刚性管道

Pipe (MA) 模块对湿空气网络中的管道流动动力学进行建模，考虑粘性摩擦损失以及与管壁的对流传热。管道内包含恒定体积的湿空气。压力和温度基于该湿空气体积的可压缩性和热容量演化。当湿空气体积达到饱和时，液态水会凝结析出。当出口达到声速条件时，发生阻塞流。

**注意**

通过该模块的空气流动可能发生阻塞。如果连接到 Pipe (MA) 模块的 Mass Flow Rate Source (MA) 模块或 Controlled Mass Flow Rate Source (MA) 模块指定的质量流量大于可能的阻塞质量流量，仿真将产生错误。有关详细信息，请参阅 Choked Flow。

模块方程使用以下符号。下标 `a`、`w`、`g` 和 `d` 分别表示干空气、水蒸气、微量气体和水滴的性质。下标 `ws` 表示饱和状态下的水蒸气。下标 `A`、`H` 和 `S` 表示相应的端口。下标 `I` 表示内部湿空气体积的性质。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流量 |
| *Q* | 热流量 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *V* | 转换器内部湿空气的体积 |
| *c*p | 定容比热 |
| *h* | 比焓 |
| *u* | 比内能 |
| *x* | 质量分数（*x*w 为比湿度，即水蒸气质量分数的另一种表述） |
| *y* | 摩尔分数 |
| *φ* | 相对湿度 |
| *r* | 湿度比 |
| *r*d | 水滴与湿空气的质量比 |
| *T* | 温度 |
| *t* | 时间 |

### 质量和能量平衡

转换器内部湿空气体积的净流量为

m˙net=m˙A−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

其中：

- m˙condense 是凝结速率。
- m˙d,evap 是水滴蒸发速率。
- *Φ*condense 是凝结水的能量损失速率。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。
- *Φ*S 是水分和微量气体源添加能量的速率。m˙wS 和 m˙gS 分别是水和气体通过端口 **S** 的质量流量。m˙wS、m˙gS 和 *Φ*S 的值由连接到转换器端口 **S** 的水分和微量气体源确定。

水蒸气质量守恒将水蒸气质量流量与内部湿空气体积中湿度水平的动力学联系起来

dxwIdtρIV+xwIm˙net=m˙w,net

类似地，微量气体质量守恒将微量气体质量流量与内部湿空气体积中微量气体水平的动力学联系起来

dxgIdtρIV+xgIm˙net=m˙g,net

水滴质量守恒方程将水滴质量流量与内部湿空气体积中夹带水滴的动力学联系起来

drdIdtρIV+rdIm˙net=m˙d,net.

混合物质量守恒将混合物质量流量与内部湿空气体积的压力、温度和质量分数的动力学联系起来：

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)+ρIV˙=m˙net

其中 V˙ 是转换器体积的变化率。

最后，能量守恒将能量流量与内部湿空气体积的压力、温度和质量分数的动力学联系起来：

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet−pIV˙

状态方程将混合物密度与压力和温度联系起来：

pI=ρIRITI

混合物比气体常数为

RI=xaIRa+xwIRw+xgIRg

### Momentum Balance

管道每一半的动量平衡用于建模由动量通量和黏性摩擦引起的压降：

pA−pI=(m˙AS)2⋅(TIpI−TApA)RI+ΔpAIpB−pI=(m˙BS)2⋅(TIpI−TBpB)RI+ΔpBI

其中：

- *p* 是端口 **A**、端口 **B** 或内部节点 I 处的压力，由下标指示。
- *ρ* 是端口 **A**、端口 **B** 或内部节点 I 处的密度，由下标指示。
- *S* 是管道的横截面积。
- *Δp*AI 和 *Δp*BI 是由黏性摩擦引起的压力损失。

由黏性摩擦引起的压力损失 *Δp*AI 和 *Δp*BI 取决于流态。管道每一半的雷诺数定义为：

ReA=|m˙A|⋅DhS⋅μIReB=|m˙B|⋅DhS⋅μI

其中：

- *D*h 是管道的水力直径。
- *μ*I 是内部节点处的动力黏度。

如果雷诺数小于 **Laminar flow upper Reynolds number limit** 参数的值，则流动处于层流流态。如果雷诺数大于 **Turbulent flow lower Reynolds number limit** 参数的值，则流动处于湍流流态。

在层流流态中，由黏性摩擦引起的压力损失为：

ΔpAIlam=fshapem˙A⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2ΔpBIlam=fshapem˙B⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2

其中：

- *f*shape 是 **Shape factor for laminar flow viscous friction** 参数的值。
- *L*eqv 是 **Aggregate equivalent length of local resistances** 参数的值。

在湍流流态中，由黏性摩擦引起的压力损失为：

ΔpAItur=fDarcyAm˙A⋅|m˙A|2ρI⋅Dh⋅S2⋅L+Leqv2ΔpBItur=fDarcyBm˙B⋅|m˙B|2ρI⋅Dh⋅S2⋅L+Leqv2

其中 *f*Darcy 是端口 **A** 或 **B** 处的 Darcy 摩擦因子，由下标指示。

Darcy 摩擦因子由 Haaland 关联式计算：

fDarcyA=[−1.8log10(6.9ReA+(εrough3.7Dh)1.11)]−2fDarcyB=[−1.8log10(6.9ReB+(εrough3.7Dh)1.11)]−2

其中 *ε*rough 是 **Internal surface absolute roughness** 参数的值。

当雷诺数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，流动处于层流与湍流之间的过渡状态。过渡区域中由黏性摩擦引起的压力损失在层流流态和湍流流态之间平滑连接。

通过端口 **H** 与管壁交换的热量通过能量守恒方程添加到由内部节点表示的湿空气体积的能量中（参见 Mass and Energy Balance）。因此，管道每一半的动量平衡，即端口 **A** 与内部节点之间以及端口 **B** 与内部节点之间的动量平衡，假定为绝热过程。绝热关系为：

hA−hI=(RIm˙AS)2[(TIpI)2−(TApA)2]hB−hI=(RIm˙BS)2[(TIpI)2−(TBpB)2]

其中 *h* 是端口 **A**、端口 **B** 或内部节点 I 处的比焓，由下标指示。

### Convective Heat Transfer

管道壁面与内部湿空气体积之间的对流换热方程为：

QH=Qconv+kISsurfDh(TH−TI)

*S*surf 是管道表面积，
*S*surf =
4*S**L*/*D*h。
如果 **Condensation on wall surface** 为 off，并且假设沿管道的温度呈指数分布，则对流换热为

Qconv=|m˙avg|cpavg(TH−Tin)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

其中：

- *T*in 是入口温度，取决于流动方向。
- m˙avg=(m˙A−m˙B)/2 是从端口 **A** 到端口 **B** 的平均质量流量。
- cpavg 是在平均温度下计算的比热。

换热系数 *h*coeff 取决于 Nusselt 数：

hcoeff=NukavgDh

其中 *k*avg 是在平均温度下计算的热导率。Nusselt 数取决于流态。层流流态下的 Nusselt 数为常数，等于 **Nusselt number for laminar flow heat transfer** 参数的值。湍流流态下的 Nusselt 数由 Gnielinski 关联式计算：

Nutur=fDarcy8(Reavg−1000)Pravg1+12.7fDarcy8(Pravg2/3−1)

其中 *Pr*avg 是在平均温度下计算的 Prandtl 数。平均 Reynolds 数为

Reavg=|m˙avg|DhSμavg

其中 *μ*avg 是在平均温度下计算的动力粘度。当平均 Reynolds 数介于 **Laminar flow upper Reynolds number limit** 和 **Turbulent flow lower Reynolds number limit** 参数值之间时，Nusselt 数在层流和湍流 Nusselt 数值之间平滑过渡。

### Saturation and Condensation

本节中的方程考虑了湿空气体积达到饱和时发生的冷凝。关于当 **Condensation on wall surface** 复选框被选中时考虑壁面冷凝的附加方程，请参见 Effect of Condensation on Wall Surface。

当湿空气体积达到饱和时，可能发生冷凝。饱和时的比湿度为

xwsI=φwsRIRwpwsIpI

其中：

- *φ*ws 是饱和时的相对湿度（通常为 1）。
- *p*wsI 是在 *T*I 下计算的水蒸气饱和压力。

冷凝速率为

m˙condense={0,if xwI≤xwsIxwI−xwsIτcondenseρIV,if xwI>xwsI

其中 *τ*condense 是 **Water vapor condensation time constant** 参数的值。

蒸发速率为

m˙d,evap=xwsI−xwIxwsIτevaprdIρIV,

其中 *τ*evap 是 **Water droplets evaporation time constant** 参数的值。

### 冷凝对壁面的影响

含有内部流体体积的湿空气模块（例如腔室、转换器等）在该流体体积被水蒸气完全饱和时，即相对湿度为 100% 时，会对水蒸气冷凝进行建模。然而，即使空气整体尚未达到饱和，水蒸气也可能在冷表面上冷凝。在 Pipe (MA) 模块中对此效应进行建模的能力很重要，因为许多 HVAC 系统包含管道和风管。如果这些管道和风管隔热不良，其表面可能会变冷，从而发生壁面冷凝。请注意，此效应不会替代当大量湿空气体积达到 100% 相对湿度时发生的冷凝，两种效应可以同时发生。

要对与湿空气体积接触的冷管道表面上的壁面冷凝效应进行建模，请选中 **Condensation on wall surface** 复选框。在这种情况下，对流传热方程需要同时考虑显热和潜热，并且该模块还有一个附加方程来计算表面上的水蒸气冷凝速率。

如果 **Condensation on wall surface** 为 on，则组合对流传热为

Qcombinedconv=|m˙ag|(h¯H−h¯in)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

其中：

- m˙ag 是入口处干空气和微量气体的质量流量。
- h¯H 是壁面处每单位质量干空气和微量气体的混合物焓。
- h¯in 是入口处每单位质量干空气和微量气体的混合物焓。

该方程与 Convective Heat Transfer 中的方程类似，但温差已被混合物焓差替代。由于混合物焓同时取决于湿空气的温度和组成，因此混合物焓差同时考虑了温度变化和含湿量变化。换句话说，它同时捕捉了显热和潜热效应。指数项以及用于计算传热系数的关联式与之前保持相同，因为该模型是基于传热与传质之间的类比推导出来的。更多信息，请参见 [3]。

为简化推导，该方程使用每单位质量干空气和微量气体的混合物焓，而不是每单位质量混合物的混合物焓，因为在水蒸气冷凝过程中干空气和微量气体的量不会改变。为确保方程保持一致，混合物焓差乘以干空气和微量气体的质量流量 m˙ag，而不是总混合物质量流量 m˙。

入口处每单位质量干空气和微量气体的混合物焓为

h¯in=hagin+Winhwin

其中：

- hagin 是入口处干空气和微量气体的比焓。
- hwin 是入口处水蒸气的比焓。
- *W*in 是入口处的湿度比。

壁面处每单位质量干空气和微量气体的混合物焓为

h¯H=hagH+WHhwH

其中：

- hagH 是壁面处干空气和微量气体的比焓。
- hwH 是壁面处水蒸气的比焓。
- *W*H 是壁面处的湿度比，定义为

  WH=min{Win,WsH}

  其中 *W*sH 是基于壁面温度的饱和湿度比。

前一个方程中的 `min` 函数提供了“干”和“湿”传热之间的切换：

- 当壁面温度高于露点时，则
  *W*sH >
  *W*in，因此不会发生冷凝，并且 (h¯H−h¯in) 仅表示温度差。
- 当壁面温度低于露点时，则
  *W*sH <
  *W*in，因此会发生冷凝，并且 (h¯H−h¯in) 同时表示温度差和含湿量差。

壁面上的水蒸气冷凝速率为

ṁcondenseH=|ṁag|(Win−WH)(1−exp(−hcoeffSsurf|ṁavg|cpavg))

该方程与组合对流换热方程类似，因为凝结在管壁上的水蒸气量与从湿空气到管壁的对流传质质量相同。由于使用了传热与传质类比，指数项也相同。有关详细信息，请参阅 [3]。

与凝结在管壁上的水相关的能量为

ΦcondenseH=ṁcondenseH(hwH−ΔhvapH)

其中 *Δh*vapH 是壁温下的汽化比焓。

管壁与湿空气之间对流传热的显热部分为

Qconv=Qcombinedconv+ΦcondenseH

该方程使用加号，因为 *Q* 在冷却湿空气时为负值。因此，加上 ΦcondenseH（正值）会去除传热中的潜热部分。

然后，该模块在对流传热中的第一个方程中使用该 *Q*conv 值来计算热端口 **H** 处的传热。

### 阻塞流

端口 **A** 或 **B** 处的未阻塞压力是该端口对应 Across 变量的值：

pAunchoked=A.ppBunchoked=B.p

但是，动量平衡方程中使用的端口压力变量 *p*A 和 *p*B 不一定与压力 Across 变量 `A.p` 和 `B.p` 一致，因为管道出口可能发生阻塞。当下游压力足够低时，会发生阻塞流。此时，流量仅取决于入口处的条件。因此，当发生阻塞时，即使由 `A.p` 或 `B.p` 表示的下游压力继续降低，出口压力（*p*A 或 *p*B， whichever 为出口）也不能进一步降低。

阻塞可能发生在管道出口，但不会发生在管道入口。因此，如果端口 **A** 是入口，则 *p*A = `A.p`。如果端口 **A** 是出口，则

pA={A.p,if A.p≥pAchokedpAchoked,if A.p<pAchoked

类似地，如果端口 **B** 是入口，则 *p*B = `B.p`。如果端口 **B** 是出口，则

pB={B.p,if B.p≥pBchokedpBchoked,if B.p<pBchoked

端口 **A** 和 **B** 处的阻塞压力通过假设出口速度等于声速，由动量平衡推导得出：

pAchoked−pI=pAchoked(pAchokedTIpITA−1)cpAcvI+ΔpAIpBchoked−pI=pBchoked(pBchokedTIpITB−1)cpBcvI+ΔpBI

### 假设与限制

- 管壁完全刚性。
- 流动已充分发展。摩擦损失和传热不包括入口效应。
- 重力的影响可忽略不计。
- 流体惯性可忽略不计。
- 该模块不对超声速流建模。
- 壁面凝结方程基于传热与传质之间的类比，因此仅在 Lewis 数 (Le) 接近 1 时有效。对于湿空气混合物，这是一个合理的假设。有关详细信息，请参阅 [3]。
