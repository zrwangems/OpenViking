---
type: simulink-block
title: 'Module (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'modulegeneratedblock'
documentation_source_path: 'ref/modulegeneratedblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Module (Generated Block)

## 端口

### 输入

### **CB** — 电芯均衡，unitless physical signal

电芯均衡端口，指定为 physical signal。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `BalancingStrategy` 属性设置为 `"Passive"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `BalancingStrategy` 属性设置为 `"Passive"`。

### 输出

**注意**

此模块的输出端口取决于用于创建与此模块关联的电池对象的 Simscape 电芯模型模块。如果 Simscape 电芯模型模块具有输出端口，Battery Builder 会将这些输出端口转发到电池对象作为其子组件的所有父级生成模块。

例如，如果您创建一个带有 **Voltage** 输出端口自定义 Simscape 电芯模型模块，并最终使用它创建此模块，则此模块具有 **Voltage** 输出端口。有关自定义电芯模型模块的详细信息，请参阅 `CellModelBlock` 对象的 `CellModelBlockPath` 属性。

### **SOC** — 荷电状态，unitless physical signal

*自 R2024b 起*

电芯级荷电状态，指定为 physical signal。

#### 依赖关系

要启用此端口，请将 Battery (Table-Based) 模块用作此模块的 `Cell` 子对象的组件模型模块，并启用 **SOC** 端口。

### 守恒

### **+** — 正极端口 electrical

与电池模块正极端子关联的 electrical 守恒端口。

### **-** — 负极端口 electrical

与电池模块负极端子关联的 electrical 守恒端口。

### **AmbH** — 环境热端口 thermal

与环境热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **ClntH** — 冷却液热端口 thermal

与冷却液热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

**注意**

如果在 `Module` 对象内部或将 `Module` 对象作为其子组件的顶级父对象内部，将 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`，则不启用此端口。

### **XminH** — Xmin 边界处的热端口 thermal | `N`-by-`1` vector | scalar

*自 R2024a 起*

与最小 X 轴表面边界关联的 thermal 守恒端口，指定为 `N`-by-`1` vector 或 scalar。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **XmaxH** — Xmax 边界处的热端口 thermal | `N`-by-`1` vector | scalar

*自 R2024a 起*

与最大 X 轴表面边界关联的 thermal 守恒端口，指定为 `N`-by-`1` vector 或 scalar。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **YminH** — Ymin 边界处的热端口 thermal | `N`-by-`1` vector | scalar

*自 R2024a 起*

与最小 Y 轴表面边界关联的 thermal 守恒端口，指定为 `N`-by-`1` vector 或 scalar。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **YminH** — Ymax 边界处的热端口 thermal | `N`-by-`1` vector | scalar

*自 R2024a 起*

与最大 Y 轴表面边界关联的 thermal 守恒端口，指定为 `N`-by-`1` vector 或 scalar。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **SP** — 蛇形边界处的热端口 thermal

*自 R2024a 起*

与蛇形冷却板边界关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。

### **CPT** — 冷却板顶部端口 thermal array-of-nodes

用于将模块顶部与冷却板连接的 thermal 守恒端口。此端口的大小取决于系统中的模型数量。如果将 `ModelResolution` 属性设置为 `“Lumped”`，则此端口输出 scalar。如果将 `ModelResolution` 属性设置为 `“Detailed”`，则此端口输出大小等于系统中电芯数量的 vector。如果将 `ModelResolution` 属性设置为 `“Grouped”`，则此端口输出大小取决于分组策略的 vector。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `CoolingPlate` 属性设置为 `"Top"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `CoolingPlate` 属性设置为 `"Top"`。

### **CPB** — 冷却板底部端口 thermal array-of-nodes

用于将模块底部与冷却板连接的 thermal 守恒端口。此端口的大小取决于系统中的模型数量。如果将 `ModelResolution` 属性设置为 `“Lumped”`，则此端口输出 scalar。如果将 `ModelResolution` 属性设置为 `“Detailed”`，则此端口输出大小等于系统中电芯数量的 vector。如果将 `ModelResolution` 属性设置为 `“Grouped”`，则此端口输出大小取决于分组策略的 vector。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `CoolingPlate` 属性设置为 `"Bottom"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `CoolingPlate` 属性设置为 `"Bottom"`。

### **+BUS** — 正极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此模块内并联组件的正极端子关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此模块内一个并联组件的正极端子。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `Module` 对象作为其子组件的任何父电池对象内部，将 `BalancingStrategy` 属性设置为 `"External"`。

### **-BUS** — 负极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此模块内并联组件的负极端子关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此模块内一个并联组件的负极端子。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `Module` 对象作为其子组件的任何父电池对象内部，将 `BalancingStrategy` 属性设置为 `"External"`。

## 参数

**注意**

这些参数和变量的名称取决于您在构成此模块的基础 `Cell` 对象的 `CellModelOptions` 属性中指定的模块。

本页中的参数和变量名称指的是以 Battery (Table-Based) 模块作为电芯组件模型模块的 `Cell` 对象。如果您为电芯组件模型指定自定义模块，则参数和变量名称可能不同。

此模块的参数需要针对电芯级设置，并且取决于您如何定义用于生成此自定义模型的 `Module` 对象。模块参数分为以下几节：

- 主要
- 动态
- 衰减
- 日历老化
- 热
- 电芯均衡

每个节的可见性还取决于生成的 `Module` 对象。

有关 **主要**、**动态**、**衰减** 和 **日历老化** 节中的参数列表，请参阅 Battery (Table-Based) 模块的文档页面。

如果在用于生成此自定义模型的 `Module` 对象中，将 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`，则每个电芯参数（不是枚举或布尔值）都有一个关联的 **偏差百分比** 参数：

### **k 的偏差百分比** — 特定电芯参数的偏差百分比 vector of scalars | matrix

*自 R2023b 起*

电池中每个电芯模型对应电芯参数 *k* 的值的偏差百分比。*k* 是与该偏差百分比关联的电芯参数的名称。

此类型的参数数量等于此模块中的电芯参数数量。枚举和布尔类型的参数没有关联的 **偏差百分比** 参数。

应用偏差后，相应电芯参数的值等于：

cellParameter=1+(cellParameterDeviation100)∗exposedCellParameter.

对于此参数，您可以指定以下任一内容：

- 一个 vector，其中电池中的每个电芯模型对应一个元素。这些元素垂直串联。例如，对于具有两个并联组件、三个电芯且 `ModelResolution` 属性设置为 `"Detailed"` 的 `Module` 对象，此 vector 需要六个元素。对于 `ModelResolution` 属性设置为 `"Grouped"` 的 `Module` 对象，此 vector 的大小取决于模块中建模的电芯数量。建模的电芯数量等于 `Parallel grouping simulation strategy` 属性的元素之和。您可以在 Module 模块的 **属性检查器** 的 **描述** 选项卡中找到此属性。
- 一个 matrix，其中矩阵的每个元素要么是 scalar，要么是大小与底层关联电芯参数相同的 matrix。参数偏差元素垂直串联。例如，如果一个电芯参数的大小为 `[2,7]`，并且一个详细并联组件包含两个电芯，则此参数的 **偏差百分比** 大小等于 `[4,7]`。

有关电芯间参数变化的详细信息，请参阅 Apply Temperature-Dependent Cell Parameter Variations to Battery Module 示例。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`。

### 热

### **热质量** — 电芯级热质量 `100` `J/K` (default) | positive scalar

单个电池电芯的热惯性。此值表示将热端口温度升高一度所需的能量。

Module 模块会自动将此值按比例放大到系统级别。

### **电芯级冷却液热路径电阻** — 电芯级冷却液热路径电阻 `1.2` `K/W` (default) | positive scalar | row vector of positive scalars

电芯级冷却液热路径的电阻。此参数的大小等于系统中的电气模型总数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **电芯级环境热路径电阻** — 电芯级环境热路径电阻 `25` `K/W` (default) | positive scalar | row vector of positive scalars

电芯级环境热路径的电阻。此参数的大小等于系统中的电气模型总数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **电芯间热路径电阻** — 电芯之间的热路径电阻 `1` `K/W` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内电芯之间的热路径电阻。此参数的大小必须等于此模块建模的电芯间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `InterCellThermalPath` 属性设置为 `"On"`。

### **并联组件间热路径电阻** — 并联组件之间的热路径电阻 `1` `K/W` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内并联组件之间的热路径电阻。此参数的大小必须等于此模块建模的并联组件间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `InterCellThermalPath` 属性设置为 `"On"`。

### **电芯间辐射传热面积** — 电芯之间的辐射传热面积 `1e-3` `m^2` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内电芯之间的辐射传热面积。此参数的大小必须等于此模块建模的电芯间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **电芯间辐射传热系数** — 电芯之间的辐射传热系数 `1e-6` `W/(K^4*m^2)` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内电芯之间的辐射传热系数。此参数的大小必须等于此模块建模的电芯间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **并联组件间辐射传热面积** — 并联组件之间的辐射传热面积 `1e-3` `m^2` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内并联组件之间的辐射传热面积。此参数的大小必须等于此模块建模的并联组件间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内部，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **并联组件间辐射传热系数** — 并联组件之间的辐射传热系数 `1e-6` `W/(K^4*m^2)` (default) | scalar | row vector of scalars

*自 R2023a 起*

模块内并联组件之间的辐射传热系数。此参数的大小必须等于此模块建模的并联组件间热连接数。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内，将 `InterCellRadiativeThermalPath` 属性设置为 `"On"`。

### **Xmin 边界处的电芯级热路径电阻** — Xmin 边界处电芯的热路径电阻 `25` `K/W` (默认) | positive scalar | row vector of positive scalars

*自 R2024a 起*

在最小 X 轴边界处，电芯级热路径的电阻。此参数的大小等于该模块建模的 Xmin 热连接总数。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `XminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Xmax 边界处的电芯级热路径电阻** — Xmax 边界处电芯的热路径电阻 `25` `K/W` (默认) | positive scalar | row vector of positive scalars

*自 R2024a 起*

在最大 X 轴边界处，电芯级热路径的电阻。此参数的大小等于该模块建模的 Xmax 热连接总数。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `XmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Ymin 边界处的电芯级热路径电阻** — Ymin 边界处电芯的热路径电阻 `25` `K/W` (默认) | positive scalar | row vector of positive scalars

*自 R2024a 起*

在最小 Y 轴边界处，电芯级热路径的电阻。此参数的大小等于该模块建模的 Ymin 热连接总数。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `YminThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **Ymax 边界处的电芯级热路径电阻** — Ymax 边界处电芯的热路径电阻 `25` `K/W` (默认) | positive scalar | row vector of positive scalars

*自 R2024a 起*

在最大 Y 轴边界处，电芯级热路径的电阻。此参数的大小等于该模块建模的 Ymax 热连接总数。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `YmaxThermalNodes` 属性设置为 `"Scalar"` 或 `"Vectorized"`。

### **蛇形边界处的电芯级热路径电阻** — 蛇形边界处电芯的热路径电阻 `25` `K/W` (默认) | positive scalar | row vector of positive scalars

*自 R2024a 起*

在蛇形边界处，电芯级热路径的电阻。此参数的大小等于该模块建模的蛇形热连接总数。

#### 依赖关系

要启用此端口，请将 `Module` 对象的 `SerpentineCoolingPlate` 属性设置为 `"SingleSidedAlongStackingAxis"` 或 `"DoubleSidedAlongStackingAxis"`。

### Parallel Assembly

### **非电芯电气电阻** — 并联组件非电芯电阻 `1 / 1000` `Ohm` (默认) | positive scalar

模块中每个并联组件的非电芯电气电阻。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `NonCellResistance` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内，将 `NonCellResistance` 属性设置为 `"On"`。

### Module

### **非电芯电气电阻** — Module 非电芯电阻 `1 / 1000` `Ohm` (默认) | positive scalar

Module 的非电芯电气电阻。

#### 依赖关系

要启用此参数，请将 `Module` 对象的 `NonCellResistance` 属性设置为 `"On"`。或者，在 `Module` 对象作为其子组件的父对象内，将 `NonCellResistance` 属性设置为 `"On"`。

### 电芯均衡

### **电芯均衡开关闭合电阻** — 电芯均衡开关的闭合电阻 `0.01` `Ohm` (默认) | positive scalar

电芯均衡开关的闭合电阻。

### **电芯均衡开关断开电导** — 电芯均衡开关的断开电导 `1e-8` `1/Ohm` (默认) | positive scalar

电芯均衡开关的断开电导。

### **电芯均衡开关操作阈值** — 电芯均衡开关操作的阈值 `0.5` (默认) | positive scalar

激活电芯均衡开关操作的阈值。

### **电芯均衡分流电阻** — 电芯均衡分流器的电阻 `50` `Ohm` (默认) | positive scalar

电芯均衡分流器的电阻。

### 初始目标（变量）

这些变量的大小等于系统中的电气模型总数。例如，在一个具有 2 个并联组件和 2 个串联电芯的 Module 模块中，变量的大小取决于 `Module` 对象的 `ModelResolution` 属性，并且对于 `Detailed` 等于 `4`，对于 `Lumped` 等于 `1`，或者当 `SeriesGrouping` 属性等于 `[1 1]` 且 `ParallelGrouping` 属性等于 `[1 2]` 时等于 `3`。

### **电芯电流（正方向为流入）** — 电芯级电流，iCell `0` `A` (默认) | scalar | vector

电芯级的电流。此变量的大小等于系统中的电气模型总数。

### **电芯端电压** — 电芯级电压，vCell `0` `V` (默认) | scalar | vector

电芯级的电压。此信号的大小等于系统中的电气模型总数。

### **电芯荷电状态** — 电芯级荷电状态，socCell `1` (默认) | scalar | vector

电芯级的荷电状态。此变量的值通常在 0 和 1 之间变化。此信号的大小等于系统中的电气模型总数。

### **电芯放电循环次数** — 电芯级循环次数，numCyclesCell `0` (默认) | scalar | vector

与电池老化相关的电芯级循环次数。此信号的大小等于系统中的电气模型总数。

### **电芯温度** — 电芯级温度，temperatureCell `298.15` `K` (默认) | positive scalar

电芯级的温度。此信号的大小等于系统中的电气模型总数。

### **Parallel Assembly 电压** — 并联组件级电压，vParallelAssembly `repmat(0,4,1)` `V` (默认) | scalar | vector

并联组件级的电压。此信号的大小等于模块中的并联组件总数。

### **Parallel Assembly 荷电状态** — 并联组件级荷电状态，socParallelAssembly `repmat(1,4,1)` (默认) | scalar | vector

并联组件级的荷电状态。此信号的大小等于模块中的并联组件总数。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024b: 在父电池模块中公开电芯级输出端口

此模块现在公开与此模块关联的 `CellModelBlock` 对象的 `CellModelBlockPath` 属性中指定的电芯模型模块的相同输出端口。

### R2024a: 为外部电芯均衡策略公开电气节点阵列端口

现在，您可以公开两个电气节点阵列端口，**+BUS** 和 **-BUS**，以便为桌面仿真和硬件在环电池仿真硬件指定并建模外部电芯均衡策略。将此选项与 Passive Balancing Interface 模块结合使用。

要指定并建模外部电芯均衡策略，请在用于生成此自定义模型的 `Module` 对象中将 `BalancingStrategy` 属性设置为 `"External"`。

### R2024a: 为位于特定表面边界的电芯公开热端口

为了对电池包环境中的电池电芯进行更详细的热建模，您现在可以公开与位于模块表面边界的电芯热节点关联的端口。要公开这些热端口，请在用于生成此自定义模型的 `Module` 对象中指定 `XminThermalNodes`、`XmaxThermalNodes`、`YminThermalNodes` 和 `YmaxThermalNodes` 属性。

对于采用六边形圆柱电芯的模块，您还可以启用模块电芯与蛇形冷却板之间的热传递。要公开与模块内蛇形冷却板关联的热端口，请指定 `SerpentineCoolingPlate` 属性。

### R2023b: 为系统中的每个电芯模型指定参数值

现在，您可以为电池系统内的每个电芯模型指定参数值。为支持特定电芯参数化，您必须在用于生成此自定义模型的 `Module` 对象中将 `CellParameterDeviation` 属性设置为 `"PercentDeviation"`。此操作会为生成的 Module 模块中的电芯参数启用 **百分比偏差** 参数，该参数指定电池中每个电芯模型对应电芯参数值的百分比偏差。

## 描述

生成的电池模块 Simscape 模型

Module 模块表示电池模块的自定义生成系统模型。您可以通过使用 `buildBattery` 函数并将 `Module` 对象作为输入参数来创建此 Simscape™ 模块。生成的 Module 模块位于您在使用 `buildBattery` 函数的 `LibraryName` 参数指定的 Simulink 库中。

**注意**

为了允许结构更改和进一步自定义，当您将来自父库的 Module (Generated Block) 掩码库模块添加到 Simulink® 模型时，链接模块不包含指向父库模块的链接或路径。如果您修改任何电池结构属性，例如 `NumSeriesAssemblies` 或 `NumParallelCells`，则必须重新构建原始父库，并再次将模块复制到您的模型中。

有关父模块和链接模块的详细信息，请参阅链接模块。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

有关 ParallelAssembly 模块中变量的详细列表，请参阅初始目标（变量）部分。

**注意**

电芯级组件的变量值指的是单个物理电芯的值，而不是电芯模型的值。*（自 R2023a 起）*

例如，考虑一个具有 10 个并联电芯且采用集中式模型分辨率的并联组件。生成的 ParallelAssembly 模块将电芯组件的变量 *v* 公开为 *vCell*。对于电压为 4.2 V 的电芯，*vCell* 等于 `4.2 V`。在 R2023a 之前，生成的模块公开带有后缀 *CellModel* 的电芯变量，并表示它们所表示的整个模型的变量。例如，使用先前的生成的 ParallelAssembly 模块，该模块公开了一个 *vCellModel* 变量，其值等于 *4.2\*10 = 42V*。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅基于标称值的系统缩放。
