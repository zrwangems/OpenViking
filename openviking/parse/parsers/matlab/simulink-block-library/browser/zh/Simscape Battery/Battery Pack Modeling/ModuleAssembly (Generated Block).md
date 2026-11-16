---
type: simulink-block
title: 'ModuleAssembly (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'moduleassemblygeneratedblock'
documentation_source_path: 'ref/moduleassemblygeneratedblock.html'
language: zh-CN
chinese_source: worker-translation
---

# ModuleAssembly (Generated Block)

## 端口

### 输入

### **balancing** — 平衡开关控制，unitless scalar

用于平衡策略的开关控制端口，指定为 scalar。

#### 依赖关系

要启用此端口，请将 `ModuleAssembly` 对象的 `BalancingStrategy` 属性设置为 `"Passive"`。或者，在 `ModuleAssembly` 对象作为子组件的父对象内，将 `BalancingStrategy` 属性设置为 `"Passive"`。

### 输出

**注意**

输出端口的名称取决于你在构成此模块装配的底层 `Cell` 对象的 `CellModelOptions` 属性中指定的模块。

此页中的输出端口名称指的是以 Battery (Table-Based) 模块作为电芯组件模型模块的 `Cell` 对象。如果你为电芯组件模型指定自定义模块，输出端口的名称可能会有所不同。

**注意**

此模块的输出端口取决于你用来创建与此模块关联的电池对象所使用的 Simscape 电芯模型模块。如果 Simscape 电芯模型模块具有输出端口，Battery Builder 会将这些输出端口转发到该电池对象作为子组件的所有父级生成模块。

例如，如果你创建一个带有 **Voltage** 输出端口的自定义 Simscape 电芯模型模块，并最终用它创建此模块，那么此模块具有一个 **Voltage** 输出端口。有关自定义电芯模型模块的更多信息，请参阅 `CellModelBlock` 对象的 `CellModelBlockPath` 属性。

### **iCell** — 电芯级电流，Ampere scalar | vector

电芯级电流。来自 Module 模块的原始信号单位为 Amperes。此信号的大小等于系统中电气模型的总数。

### **numCyclesCell** — 电芯级循环次数，unitless scalar | vector

与电池老化相关的电芯级循环次数。来自 Module 模块的原始信号单位为 unitless。此信号的大小等于系统中电气模型的总数。

### **socCell** — 电芯级荷电状态，unitless scalar | vector

电芯级的荷电状态。来自 Module 模块的原始信号单位为 unitless，值通常在 0 和 1 之间变化。此信号的大小等于系统中电气模型的总数。

### **socParallelAssembly** — 并联装配级的荷电状态，unitless scalar | vector

并联装配级的荷电状态。来自 Module 模块的原始信号单位为 unitless，值通常在 0 和 1 之间变化。此信号的大小等于模块装配中并联装配的总数。

### **temperatureCell** — 电芯级温度，kelvin scalar | vector

电芯级温度。来自 Module 模块的原始信号单位为 Kelvin。此信号的大小等于系统中电气模型的总数。

#### 依赖关系

要启用此端口，请启用构成 pack 的电芯的热端口。要对电芯的热端口建模，请在电芯的 `CellModelBlock` 属性中，将 `BlockParameters` 属性的 **thermal\_port** 参数设置为 `"Model"`。

### **vCell** — 电芯级电压，volts scalar | vector

电芯级电压。来自 Module 模块的原始信号单位为 volts。此信号的大小等于系统中电气模型的总数。

### **vParallelAssembly** — 并联装配级电压，volts scalar | vector

并联装配级电压。来自 Module 模块的原始信号单位为 volts。此信号的大小等于模块装配中并联装配的总数。将此信号用作 Simscape Battery 的电池管理系统 (BMS) 模块的输入。

### **CP\_Out** — 模型中每个冷却板的输出 vector of physical signals

*自 R2023a 起*

包含模型中每个冷却板的板温度、流体压降和流体温度变化的向量。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口：

- `ModuleAssembly` 对象不能是 `Pack` 对象的子组件。
- 将 `ModuleAssembly` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **SOC** — 荷电状态，unitless scalar | vector

*自 R2024b 起*

电芯级的荷电状态，指定为 scalar 或 vector。

#### 依赖关系

要启用此端口，请使用 Battery (Table-Based) 模块作为此模块的 `Cell` 子对象的组件模型模块，并启用 **SOC** 端口。

### 守恒

### **+** — 正极端子 electrical

与电池模块装配正极端子关联的 electrical 守恒端口。

### **-** — 负极端子 electrical

与电池模块装配负极端子关联的 electrical 守恒端口。

### **AmbH** — 环境热端口 thermal

与环境热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请将 `ModuleAssembly` 对象的 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ModuleAssembly` 对象作为子组件的顶层父对象内，将 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **ClntH** — 冷却剂热端口 thermal

与冷却剂热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请将 `ModuleAssembly` 对象的 `CoolantThermalPort` 属性设置为 `"CellBasedThermalResistance"`。或者，在 `ModuleAssembly` 对象作为子组件的顶层父对象内，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

**注意**

如果你在 `ModuleAssembly` 对象内，或在 `ModuleAssembly` 对象作为子组件的顶层父对象内，将 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`，则不会启用此端口。

### **CPT** — 冷却板顶部端口 thermal array-of-nodes

*自 R2023a 起*

用于将模块装配顶部与冷却板连接的 thermal 守恒端口。此端口的大小取决于系统中电池模型的总数。

#### 依赖关系

要启用此端口：

- `ModuleAssembly` 对象必须是 `Pack` 对象的子组件。
- 将 `ModuleAssembly` 或父级 `Pack` 对象的 `CoolingPlate` 属性设置为 `"Top"`。

### **CPB** — 冷却板底部端口 thermal array-of-nodes

*自 R2023a 起*

用于将模块装配底部与冷却板连接的 thermal 守恒端口。此端口的大小取决于系统中电池模型的总数。

#### 依赖关系

要启用此端口：

- `ModuleAssembly` 对象必须是 `Pack` 对象的子组件。
- 将 `ModuleAssembly` 或父级 `Pack` 对象的 `CoolingPlate` 属性设置为 `"Bottom"`。

### **Fluid\_In** — 冷却板中的流体 thermal fluid

*自 R2023a 起*

与进入模型中每个冷却板的流体关联的 thermal fluid 守恒端口。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口：

- `ModuleAssembly` 对象不能是 `Pack` 对象的子组件。
- 将 `ModuleAssembly` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **Fluid\_Out** — 冷却板流出的流体 thermal fluid

*自 R2023a 起*

与从模型中每个冷却板流出的流体关联的 thermal fluid 守恒端口。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口：

- `ModuleAssembly` 对象不能是 `Pack` 对象的子组件。
- 将 `ModuleAssembly` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **+BUS** — 正极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此模块装配内部并联装配的正极端子关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此模块装配内部一个并联装配的正极端子。

#### 依赖关系

要启用此端口，请将 `ModuleAssembly` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `ModuleAssembly` 对象作为子组件的 `Pack` 父对象内，将 `BalancingStrategy` 属性设置为 `"External"`。

### **-BUS** — 负极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此模块装配内部并联装配的负极端子关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此模块装配内部一个并联装配的负极端子。

#### 依赖关系

要启用此端口，请将 `ModuleAssembly` 对象的 `BalancingStrategy` 属性设置为 `"External"`。或者，在 `ModuleAssembly` 对象作为子组件的 `Pack` 父对象内，将 `BalancingStrategy` 属性设置为 `"External"`。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024b：在父级电池模块中公开电芯级输出端口

此模块现在公开你在与此模块关联的 `CellModelBlock` 对象的 `CellModelBlockPath` 属性中指定的电芯模型模块的相同输出端口。

### R2024a：为外部电芯平衡策略公开 electrical array-of-nodes 端口

你现在可以公开两个 electrical array-of-nodes 端口 **+BUS** 和 **-BUS**，用于指定并建模桌面仿真和 hardware-in-the-loop 电池仿真硬件的外部电芯平衡策略。将此选项与 Passive Balancing Interface 模块结合使用。

要指定并建模外部电芯平衡策略，请在你用于生成此自定义模型的 `ModuleAssembly` 对象中将 `BalancingStrategy` 属性设置为 `"External"`。

## 描述

电池模块装配的生成 Simscape 模型

ModuleAssembly 模块是电池模块装配的自定义生成子系统模型。你可以通过将 `ModuleAssembly` 对象作为输入参数传递给 `buildBattery` 函数来创建此 Simscape™ 子系统。ModuleAssembly 子系统模块位于你在 `buildBattery` 函数的 `LibraryName` 参数中指定的 Simulink 库中。

**注意**

为了允许结构更改和进一步自定义，当你从父库中将 ModuleAssembly (Generated Block) 掩码库模块添加到 Simulink® 模型时，链接模块不包含指向父库模块的链接或路径。如果你修改任何电池结构属性，例如 `NumSeriesAssemblies` 或 `NumParallelCells`，则必须重新构建原始父库，并再次将模块复制到你的模型中。

有关父模块和链接模块的更多信息，请参阅 Linked Blocks。

ModuleAssembly 子系统模型包含六个主要部分。

- 电池模块部分显示 `Module` 对象中定义的所有 Module 子系统。此部分包含模块之间的所有串联和并联电路连接，以及对主电气端子的附加连接和模块到热域的边界条件。如果你需要额外的非模块电阻，则该函数会在此处添加并连接两个额外的电气电阻。
- 输出信号部分将每个 Module 模块的输出分组为 ModuleAssembly 子系统的一个单一多路复用输出信号。
- 热边界条件部分包含每个 Module 模块的热边界条件。`buildBattery` 函数从热域添加一个连接器端口，并根据指定的热边界条件将其路由到每个 Module 子系统。此部分是可选的，仅当你在 `ModuleAssembly` 对象中定义环境或冷却剂热路径时才会出现。
- 平衡信号部分包含从电池管理系统到每个 Module 子系统的电芯平衡控制信号的路由。Selector 模块将控制信号的正确元素路由到模块内其对应的 ParallelAssembly 模块。
- 冷却剂热液体部分包含用于在电池冷却板内部循环的冷却剂的热液体网络歧管。此部分是可选的，仅当你在 `ModuleAssembly` 对象中定义冷却板时才会出现。
- 电芯输出部分将电芯模型模块的每个输出分组为 ModuleAssembly 子系统对应的多路复用输出信号。

### 电池模块

此图显示由两个电池模块构成的 ModuleAssembly 子系统的电池模块部分。

### 输出信号

此图显示由两个电池模块构成的 ModuleAssembly 子系统的输出信号部分。

### 热边界条件

此图显示由两个电池模块构成的 ModuleAssembly 子系统的热边界条件部分。

### 平衡信号

此图显示由两个电池模块构成的 ModuleAssembly 子系统的平衡信号部分。

### 冷却剂热液体

此图显示由两个电池模块构成的 ModuleAssembly 子系统的冷却剂热液体部分。
