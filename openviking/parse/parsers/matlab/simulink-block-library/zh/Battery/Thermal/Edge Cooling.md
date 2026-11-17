---
type: simulink-block
title: 'Edge Cooling'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Thermal'
documentation_page: 'edgecooling'
documentation_source_path: 'ref/edgecooling.html'
language: zh-CN
chinese_source: worker-translation
---

# Edge Cooling

## 端口

### 输出

### **Tp** — 冷却板温度，K physical signal

冷却板的温度，单位为开尔文。

### **dT** — 流体温度变化，K physical signal

流体的温度变化，单位为开尔文。

### **dP** — 流体压降，Pa physical signal

流体的压降，单位为帕斯卡。
### 守恒端口

### **fluid\_in** — 冷却板入口热流体

与进入冷却板的流体相关联的热流体守恒端口。

### **fluid\_out** — 冷却板出口热流体

与流出冷却板的流体相关联的热流体守恒端口。

### **Surf1** — 冷却板热表面 1

与冷却板表面 1 相关联的热守恒端口。此端口连接冷却板与电池包或模块之间的热节点阵列。

### **Surf2** — 冷却板热表面 2

与冷却板表面 2 相关联的热守恒端口。此端口连接冷却板与电池包或模块之间的热节点阵列。

## 参数

### Interface

### **Battery Connectivity** — 电池连接方式 `Single sided`（默认）| `Double sided`

用于选择电池连接方式的选项。

### **Number of battery thermal nodes (surface 1)** — 表面 1 上的电池热节点数量 `1`（默认）| 正标量

冷却板表面 1 上的电池热节点数量。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

### **Dimension of battery thermal nodes (surface 1)** — 表面 1 上的电池热节点尺寸 `ones(1, 2)`（默认）

冷却板表面 1 上的电池热节点尺寸。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

### **Coordinates of battery thermal nodes (surface 1)** — 表面 1 上的电池热节点坐标 `ones(1, 2)`（默认）| M×N 矩阵

冷却板表面 1 上的电池热节点坐标。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

### **Number of battery thermal nodes (surface 2)** — 表面 2 上的电池热节点数量 `1`（默认）| 正标量

冷却板表面 2 上的电池热节点数量。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

#### 依赖关系

要启用此参数，请将 **Battery Connectivity** 设置为 `Double sided`。

### **Dimension of battery thermal nodes (surface 2)** — 表面 2 上的电池热节点尺寸 `ones(1, 2)`（默认）| M×N 矩阵

冷却板表面 2 上的电池热节点尺寸。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

#### 依赖关系

要启用此参数，请将 **Battery Connectivity** 设置为 `Double sided`。

### **Coordinates of battery thermal nodes (surface 2)** — 表面 2 上的电池热节点坐标 `ones(1, 2)`（默认）| M×N 矩阵

冷却板表面 2 上的电池热节点坐标。

当手动将此冷却板连接到电池时，您可以通过查询与您所连接的电池模块相关联的电池对象的 `ThermalNodes` 属性来获取此信息。`ThermalNodes` 属性包含节点数量、节点的二维位置以及节点尺寸等信息。

#### 依赖关系

要启用此参数，请将 **Battery Connectivity** 设置为 `Double sided`。

### **Number of partitions in X dimension for the cooling plate** — 冷却板 X 方向分区数量 `2`（默认）| 正标量

冷却板在 X 方向上的分区数量。此参数影响冷却板的保真度。

### **Number of partitions in Y dimension for the cooling plate** — 冷却板 Y 方向分区数量 `5`（默认）| 正标量

冷却板在 Y 方向上的分区数量。此参数影响冷却板的保真度。

### Plate Material

### **Thickness of cooling plate material** — 冷却板材料厚度 `2e-3` `m`（默认）| 正标量

冷却板材料的厚度。

### **Thermal conductivity of cooling plate material** — 冷却板材料导热系数 `20` `W/(K*m)`（默认）| 正标量

冷却板材料的导热系数。

### **Density of cooling plate material** — 冷却板材料密度 `2500` `kg/m^3`（默认）| 正标量

冷却板材料的密度。

### **Specific heat of cooling plate material** — 冷却板材料比热容 `447` `J/(K*kg`（默认）| 正标量

冷却板材料的比热容。

### **Initial temperature of the cooling plate and the coolant fluid** — 零时刻冷却板和冷却液温度 `300` `K`（默认）| 正标量

仿真开始时冷却板和冷却液的温度。

### Fluid Properties

### **Reynolds number upper limit for laminar flow** — 流动开始从层流过渡到湍流时的雷诺数 `2000`（默认）| 大于 `1` 的标量

流动开始从层流过渡到湍流时的雷诺数。此数值等于完全发展层流对应的最大雷诺数。

### **Reynolds number lower limit for turbulent flow** — 流动开始从湍流过渡到层流时的雷诺数 `4000`（默认）| 正标量

流动开始从湍流过渡到层流时的雷诺数。此数值等于完全发展湍流对应的最小雷诺数。

此参数的值必须大于 **Reynolds number upper limit for laminar flow** 参数的值。

### **Nusselt number for laminar flow heat transfer** — 对流传热与导热传热之比 `3.66`（默认）| 正标量

层流状态下对流传热与导热传热之比。其值取决于管道横截面几何形状和管壁热边界条件，例如恒定温度或恒定热通量。典型值为 3.66，适用于恒定壁温的圆形横截面。

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的合计长度 `1e-3` `m`（默认）| 非负标量

管道中所有局部阻力的合计长度。局部阻力包括弯头、管件、附件以及管道进出口。局部阻力的作用是增加管段的等效长度。此长度仅在摩擦计算中加到管道几何长度上。管道内的液体体积仅取决于管道几何长度。

### **Laminar friction constant for Darcy friction factor** — 管道几何形状对粘性摩擦损失的影响 `64`（默认）| 正标量

无量纲因子，用于表征管道横截面几何形状对层流状态下粘性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96。

### Design

### **Select edge to be cooled** — 冷却边缘 `Edge cooling along Y axis at X = Xmin`（默认）| `Edge cooling along X axis at Y = Ymin` | `Edge cooling along Y axis at X = Xmax` | `Edge cooling along X axis at Y = Ymax`

用于选择您想要冷却的冷却板边缘的选项。

### **Cooling channel hydraulic diameter** — 冷却通道水力直径 `5e-3` `m`（默认）| 正标量

冷却通道的水力直径。

### **Cooling channel cross-sectional area** — 冷却通道横截面积 `2e-5` `m^2`（默认）| 正标量

冷却通道垂直于流动方向的内部面积。

### **Coolant channel roughness** — 冷却液通道粗糙度 `1.5e-05` `m`（默认）| 正标量

冷却液通道的粗糙度。

## 所属库

Simscape / Battery / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

带边缘冷却的冷却板

Edge Cooling 模块对带边缘冷却的电池冷却板进行建模。使用 `buildBattery` 函数创建电池的 Simscape 模型，并将其连接到冷却板的任一端。您可以冷却冷却板的四个边缘中的任意一个。要了解如何将冷却板模块连接到电池，请参阅 Connect Battery Block to Cooling Plate Block Automatically。

通常，冷却板由两块冲压平板连接而成。板的冲压部分形成流体可以流动的通道。Edge Cooling 模块通过使用一个或多个 Thermal Mass 模块来对板的平坦材料进行建模，并通过使用 Pipe (TL) 模块来对通过冷却通道的流体流动进行建模。Pipe (TL) 模块的数量及其与板的连接取决于离散化方式。有关 Pipe (TL) 模块的实现及其方程的更多信息，请参阅 Pipe (TL) 文档页面。

冷却板的热质量通过热传导相互交换热量，使用以下方程：

Q=K A dTdx，

其中 *T* 是温度，*K* 是板导热系数，*A* 和 *x* 取决于板厚度以及分区数量和方向，*x* 或 *y*。

流体通过这些热质量带走热量或加热电池包。未连接到管道的热质量只能根据您指定的热传导参数向电池添加或移除热量。

### 冷却板离散化

**Number of partitions in X direction** 和 **Number of partitions in Y direction** 参数控制冷却板的离散化。

如果您将 **Number of partitions in X direction** 和 **Number of partitions in Y direction** 参数设置为 1，则冷却板是具有单一热质量值的集中质量。软件根据 **Plate Material** 部分中参数的值计算此热质量。在此示例中，**Select edge to be cooled** 参数设置为 `Edge cooling along Y axis at X = Xmax`。然后，软件在最大 *X* 轴值处沿 *Y* 轴放置一个 Pipe (TL) 模块，并将其连接到冷却板。在仿真期间，冷却板在每个时间步具有一个温度值。因此，连接到此冷却板的电池包的每个电芯测量到相同的板温度值。

要提高模型保真度，请将 **Number of partitions in X direction** 的值更改为 2。软件现在将冷却板沿 X 维度分为两个区域。每个区域包含一个单独的热质量。在此配置下，Pipe (TL) 模块连接到板的两个区域。在仿真期间，冷却板具有两个不同的温度值，板的每个区域各一个。

要进一步提高模型保真度，请将 **Number of partitions in Y direction** 的值更改为 3。软件将冷却板沿 Y 维度离散为三个区域。冷却板中的区域总数现在为六个。由于 Y 方向也是冷却液流动的方向，软件也会对冷却管道进行离散化。此配置不是为 X 方向上的每对分区使用一个 Pipe (TL) 模块，而是为 X 方向上的每对分区包含一个 Pipe (TL) 模块。在仿真期间，此冷却板在每个时间步具有六个不同的温度值。因此，连接到此板的电池包的电芯测量到的温度值取决于电芯的位置。

有关冷却板及其与电池模块连接的更多信息，请参阅 Connect Cooling Plate to Battery Blocks。
