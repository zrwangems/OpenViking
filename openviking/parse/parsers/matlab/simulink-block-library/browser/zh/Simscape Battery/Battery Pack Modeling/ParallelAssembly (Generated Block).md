---
type: simulink-block
title: 'ParallelAssembly (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'parallelassemblygeneratedblock'
documentation_source_path: 'ref/parallelassemblygeneratedblock.html'
language: zh-CN
chinese_source: worker-translation
---

# ParallelAssembly (Generated Block)

## 端口

### 输入

### **CB** — 电芯均衡，无量纲物理信号

电芯均衡端口，指定为物理信号。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `BalancingStrategy` 属性设置为 `"Passive"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `BalancingStrategy` 属性设置为 `"Passive"`。

### 输出

**注意**

此模块的输出端口取决于用于创建与此模块关联的电池对象的 Simscape 电芯模型模块。如果 Simscape 电芯模型模块具有输出端口，则 Battery Builder 会将这些输出端口转发到电池对象作为其子组件的所有父级生成模块。

例如，如果创建一个具有 **Voltage** 输出端口的自定义 Simscape 电芯模型模块，并最终使用它创建此模块，则此模块将具有 **Voltage** 输出端口。有关自定义电芯模型模块的详细信息，请参阅 `CellModelBlock` 对象的 `CellModelBlockPath` 属性。

### **SOC** — 荷电状态，无量纲物理信号

*自 R2024b 起*

电芯级荷电状态，指定为物理信号。

#### 依赖关系

要启用此端口，请将此模块的 `Cell` 子对象的组件模型模块设置为 Battery (Table-Based) 模块，并启用 **SOC** 端口。

### 守恒

### **+** — 正极端子 电气

与电池并联组件正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与电池并联组件负极端子关联的电气守恒端口。

### **AmbH** — 环境热端口 热

与环境热路径关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **ClntH** — 冷却液热端口 热

与冷却液热路径关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

**注意**

如果在 `ParallelAssembly` 对象内部，或在 `ParallelAssembly` 对象作为其子组件的顶级父对象内部，将 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`，则不会启用此端口。

### **XminH** — Xmin 边界处的热端口 热 | `N`-by-`1` 向量 | 标量

*自 R2024a 起*

与最小 X 轴表面边界关联的热守恒端口，指定为 `N`-by-`1` 向量或标量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **XmaxH** — Xmax 边界处的热端口 热 | `N`-by-`1` 向量 | 标量

*自 R2024a 起*

与最大 X 轴表面边界关联的热守恒端口，指定为 `N`-by-`1` 向量或标量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **YminH** — Ymin 边界处的热端口 热 | `N`-by-`1` 向量 | 标量

*自 R2024a 起*

与最小 Y 轴表面边界关联的热守恒端口，指定为 `N`-by-`1` 向量或标量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **YminH** — Ymax 边界处的热端口 热 | `N`-by-`1` 向量 | 标量

*自 R2024a 起*

与最大 Y 轴表面边界关联的热守恒端口，指定为 `N`-by-`1` 向量或标量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **SP** — 蛇形边界处的热端口 热

*自 R2024a 起*

与蛇形冷却板边界关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。

### **ICH** — 电芯间热端口 热

*自 R2023a 起*

与电芯间热路径关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `InterCellThermalPath` 或 `InterCellRadiativeThermalPath` 属性设置为 `"on"`。

### **CPT** — 冷却板顶部端口 热节点数组

用于将模块顶部与冷却板连接的热守恒端口。此端口的大小取决于系统中的模型数量。如果将 `ModelResolution` 属性设置为 `“Lumped”`，则此端口输出标量。如果将 `ModelResolution` 属性设置为 `“Detailed”`，则此端口输出大小等于系统中电芯数量的向量。如果将 `ModelResolution` 属性设置为 `“Grouped”`，则此端口输出大小取决于分组策略的向量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `CoolingPlate` 属性设置为 `"Top"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `CoolingPlate` 属性设置为 `"Top"`。

### **CPB** — 冷却板底部端口 热节点数组

用于将模块底部与冷却板连接的热守恒端口。此端口的大小取决于系统中的模型数量。如果将 `ModelResolution` 属性设置为 `“Lumped”`，则此端口输出标量。如果将 `ModelResolution` 属性设置为 `“Detailed”`，则此端口输出大小等于系统中电芯数量的向量。如果将 `ModelResolution` 属性设置为 `“Grouped”`，则此端口输出大小取决于分组策略的向量。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `CoolingPlate` 属性设置为 `"Bottom"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `CoolingPlate` 属性设置为 `"Bottom"`。

### **+BUS** — 正极端子总线 电气节点数组

*自 R2024a 起*

与并联组件正极端子关联的电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `ParallelAssembly` 对象作为其子组件的任一父电池对象内部，将 `BalancingStrategy` 属性设置为 `"External"`。

### **-BUS** — 负极端子总线 电气节点数组

*自 R2024a 起*

与并联组件正极端子关联的电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `ParallelAssembly` 对象作为其子组件的任一父电池对象内部，将 `BalancingStrategy` 属性设置为 `"External"`。

## 参数

**注意**

这些参数和变量的名称取决于你在构成此并联组件的底层 `Cell` 对象的 `CellModelOptions` 属性中指定的模块。

此页面中的参数和变量名称指的是以 Battery (Table-Based) 模块作为电芯组件模型模块的 `Cell` 对象。如果为电芯组件模型指定自定义模块，则参数和变量的名称可能有所不同。

此模块的参数需要针对电芯级设置，并取决于你如何定义用于生成此自定义模型的 `ParallelAssembly` 对象。模块参数分为以下部分：

- 主要
- 动态
- 衰减
- 日历老化
- 热
- 电芯均衡

每个部分的可见性还取决于生成它的 `ParallelAssembly` 对象。

有关 **主要**、**动态**、**衰减** 和 **日历老化** 部分中的参数列表，请参阅 Battery (Table-Based) 模块的文档页面。

如果在用于生成此自定义模型的 `ParallelAssembly` 对象中，将 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`，则每个电芯参数（非枚举或布尔值）都有一个关联的 **百分比偏差** 参数：

### **k 的百分比偏差** — 特定电芯参数的百分比偏差 标量向量 | 矩阵

*自 R2023b 起*

电池中每个电芯模型对应电芯参数 *k* 的值的百分比偏差。*k* 是与此百分比偏差关联的电芯参数的名称。

此类参数的数量等于此模块中电芯参数的数量。枚举和布尔类型的参数没有关联的 **百分比偏差** 参数。

应用偏差后的对应电芯参数值等于：

cellParameter=1+(cellParameterDeviation100)∗exposedCellParameter.

对于此参数，可以指定以下任一项：

- 一个向量，其中为电池中的每个电芯模型包含一个元素。这些元素垂直串联。例如，对于一个具有两个并联组件、三个电芯且 `ModelResolution` 属性设置为 `"Detailed"` 的 `Module` 对象，此向量需要六个元素。
- 一个矩阵，其中矩阵的每个元素要么是标量，要么是与底层关联电芯参数大小相同的矩阵。参数偏差元素垂直串联。例如，如果一个电芯参数的大小为 `[2,7]`，并且一个详细并联组件包含两个电芯，则此参数的 **百分比偏差** 大小等于 `[4,7]`。

有关电芯间参数变化的详细信息，请参阅 Apply Temperature-Dependent Cell Parameter Variations to Battery Module 示例。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`。

### 热

### **热质量** — 电芯级热质量 `100` `J/K`（默认） | 正标量

单个电池电芯的热惯性。此值表示将热端口温度提高一度所需的能量。

ParallelAssembly 模块会自动将此值按比例放大到系统级。

### **电芯级冷却液热路径电阻** — 电芯级冷却液热路径电阻 `1.2` `K/W`（默认） | 正标量 | 正标量行向量

电芯级冷却液热路径的电阻。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **电芯级环境热路径电阻** — 电芯级环境热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量行向量

电芯级环境热路径的电阻。此参数的大小等于系统中电气模型的总数。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **电芯间热路径电阻** — 电芯之间的热路径电阻 `1` `K/W`（默认） | 标量 | 标量行向量

*自 R2023a 起*

并联组件内部电芯之间的热路径电阻。此参数的大小必须等于此模块建模的电芯间热连接数量。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `InterCellThermalPath` 属性设置为 `"On"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `InterCellThermalPath` 属性设置为 `"On"`。

### **电芯间辐射传热面积** — 电芯之间的辐射传热面积 `1e-3` `m^2`（默认） | 标量 | 标量行向量

*自 R2023a 起*

并联组件内部电芯之间的辐射传热面积。此参数的大小必须等于此模块建模的电芯间热连接数量。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **电芯间辐射传热系数** — 电芯之间的辐射传热系数 `1e-6` `W/(K^4*m^2)`（默认） | 标量 | 标量行向量

*自 R2023a 起*

并联组件内部电芯之间的辐射传热系数。此参数的大小必须等于此模块建模的电芯间热连接数量。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `ParallelAssembly` 对象作为其子组件的父对象内部，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **Xmin 边界处电芯级热路径电阻** — Xmin 边界处电芯的热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量行向量

*自 R2024a 起*

最小 X 轴边界处电芯级热路径的电阻。此参数的大小等于模块建模的 Xmin 热连接总数。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在 `ParallelAssembly` 对象作为其子组件的父 `Module` 对象内部，将 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Xmax 边界处的电芯级热路径电阻** — Xmax 边界处电芯的热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量的行向量

*自 R2024a 起*

最大 X 轴边界处电芯级热路径的电阻。此参数的大小等于模块建模的 Xmax 热连接总数。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在作为子组件的 `ParallelAssembly` 对象的父 `Module` 对象内，将 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Ymin 边界处的电芯级热路径电阻** — Ymin 边界处电芯的热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量的行向量

*自 R2024a 起*

最小 Y 轴边界处电芯级热路径的电阻。此参数的大小等于模块建模的 Ymin 热连接总数。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在作为子组件的 `ParallelAssembly` 对象的父 `Module` 对象内，将 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Ymax 边界处的电芯级热路径电阻** — Ymax 边界处电芯的热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量的行向量

*自 R2024a 起*

最大 Y 轴边界处电芯级热路径的电阻。此参数的大小等于模块建模的 Ymax 热连接总数。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。或者，在作为子组件的 `ParallelAssembly` 对象的父 `Module` 对象内，将 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **蛇形边界处的电芯级热路径电阻** — 蛇形边界处电芯的热路径电阻 `25` `K/W`（默认） | 正标量 | 正标量的行向量

*自 R2024a 起*

蛇形边界处电芯级热路径的电阻。此参数的大小等于模块建模的蛇形热连接总数。

#### 依赖关系

要启用此端口，请将 `ParallelAssembly` 对象的 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。或者，在作为子组件的 `ParallelAssembly` 对象的父 `Module` 对象内，将 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。

### Parallel Assembly

### **非电芯电阻** — 并联组件非电芯电阻 `1 / 1000` `Ohm`（默认） | 正标量

模块中每个并联组件的非电芯电阻。

#### 依赖关系

要启用此参数，请将 `ParallelAssembly` 对象的 `NonCellResistance` 属性设置为 `"On"`。或者，在作为子组件的 `ParallelAssembly` 对象的父对象内，将 `NonCellResistance` 属性设置为 `"On"`。

### 电芯均衡

### **电芯均衡开关闭合电阻** — 电芯均衡开关的闭合电阻 `0.01` `Ohm`（默认） | 正标量

电芯均衡开关的闭合电阻。

### **电芯均衡开关断开电导** — 电芯均衡开关的断开电导 `1e-8` `1/Ohm`（默认） | 正标量

电芯均衡开关的断开电导。

### **电芯均衡开关操作阈值** — 电芯均衡开关操作的阈值 `0.5`（默认） | 正标量

激活电芯均衡开关操作的阈值。

### **电芯均衡分流电阻** — 电芯均衡分流器的电阻 `50` `Ohm`（默认） | 正标量

电芯均衡分流器的电阻。

### 初始目标（变量）

这些变量的大小等于系统中电气模型的总数。例如，在一个具有 2 个并联组件和 2 个串联电芯的 Module 模块中，变量的大小取决于 `Module` 对象的 `ModelResolution` 属性，对于 `Detailed` 等于 `4`，对于 `Lumped` 等于 `1`，或者当 `SeriesGrouping` 属性等于 `[1 1]` 且 `ParallelGrouping` 属性等于 `[1 2]` 时等于 `3`。

### **电芯电流（正方向流入）** — 电芯级电流，iCell `0` `A`（默认） | 标量 | 向量

电芯级电流。此变量的大小等于系统中电气模型的总数。

### **电芯端电压** — 电芯级电压，vCell `0` `V`（默认） | 标量 | 向量

电芯级电压。此信号的大小等于系统中电气模型的总数。

### **电芯荷电状态** — 电芯级荷电状态，socCell `1`（默认） | 标量 | 向量

电芯级荷电状态。此变量的值通常在 0 和 1 之间变化。此信号的大小等于系统中电气模型的总数。

### **电芯放电循环次数** — 电芯级循环次数，numCyclesCell `0`（默认） | 标量 | 向量

与电池老化相关的电芯级循环次数。此信号的大小等于系统中电气模型的总数。

### **电芯温度** — 电芯级温度，temperatureCell `298.15` `K`（默认） | 正标量

电芯级温度。此信号的大小等于系统中电气模型的总数。

### **Parallel Assembly 电压** — 并联组件级电压，vParallelAssembly `0` `V`（默认） | 标量 | 向量

并联组件级电压。此信号的大小等于系统中电气模型的总数。

### **Parallel Assembly 荷电状态** — 并联组件级荷电状态，socParallelAssembly `1`（默认） | 标量 | 向量

并联组件级荷电状态。此信号的大小等于系统中电气模型的总数。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024b：在父电池模块中公开电芯级输出端口

此模块现在公开与此模块关联的 `CellModelBlock` 对象的 `CellModelBlockPath` 属性中指定的电芯模型模块的相同输出端口。

### R2024a：为外部电芯均衡策略公开电气节点阵列端口

您现在可以公开两个电气节点阵列端口 **+BUS** 和 **-BUS**，以指定并为桌面仿真和硬件在环电池仿真硬件建模外部电芯均衡策略。将此选项与 Passive Balancing Interface 模块结合使用。

要指定并为外部电芯均衡策略建模，请在用于生成此自定义模型的 `ParallelAssembly` 对象中将 `BalancingStrategy` 属性设置为 `"External"`。

### R2024a：为特定表面边界处的电芯公开热端口

为了对电池包环境中的电芯进行更详细的热建模，您现在可以公开与位于并联组件表面边界处的电芯热节点关联的端口。要公开这些热端口，请在用于生成此自定义模型的 `ParallelAssembly` 对象中指定 `XminThermalNodes`、`XmaxThermalNodes`、`YminThermalNodes` 和 `YmaxThermalNodes` 属性。

对于具有六边形圆柱电芯的并联组件，您还可以启用并联组件的电芯与蛇形冷却板之间的热传递。要公开与并联组件内部蛇形冷却板关联的热端口，请指定 `SerpentineCoolingPlate` 属性。

### R2023b：为系统中的每个电芯模型指定参数值

您现在可以为电池系统中的每个电芯模型指定参数值。要支持特定电芯参数化，必须在用于生成此自定义模型的 `ParallelAssembly` 对象中将 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`。此操作会在生成的 ParallelAssembly 模块中为电芯参数启用一个 **百分比偏差** 参数，该参数指定电池中每个电芯模型对应电芯参数值的百分比偏差。

## 描述

电池并联组件的生成 Simscape 模型

ParallelAssembly 模块表示电池并联组件的自定义生成系统模型。您可以使用 `buildBattery` 函数并以 `ParallelAssembly` 对象作为输入参数来创建此 Simscape™ 模块。ParallelAssembly 生成的模块位于您在 `buildBattery` 函数的 `LibraryName` 参数中指定的 Simulink 库中。

**注意**

为了允许结构更改和进一步自定义，当您将父库中的 ParallelAssembly（Generated Block）掩码库模块添加到 Simulink® 模型时，链接模块不包含指向父库模块的链接或路径。如果修改任何电池结构属性，例如 `NumSeriesAssemblies` 或 `NumParallelCells`，您必须重新构建原始父库，并再次将模块复制到您的模型中。

有关父模块和链接模块的详细信息，请参阅 Linked Blocks。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

有关 ParallelAssembly 模块中变量的详细列表，请参阅初始目标（变量）部分。

**注意**

电芯级组件的变量值指的是单个物理电芯的值，而不是电芯模型的值。*（自 R2023a 起）*

例如，考虑一个具有 10 个并联电芯且采用集中模型分辨率的并联组件。ParallelAssembly 生成的模块将电芯组件的变量 *v* 公开为 *vCell*。对于电压为 4.2 V 的电芯，*vCell* 等于 `4.2 V`。在 R2023a 之前，生成的模块使用后缀 *CellModel* 公开电芯变量，并表示它们所表示的整个模型的变量。例如，使用前面的 ParallelAssembly 生成的模块，该模块公开了一个 *vCellModel* 变量，其值等于 *4.2\*10 = 42V*。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
