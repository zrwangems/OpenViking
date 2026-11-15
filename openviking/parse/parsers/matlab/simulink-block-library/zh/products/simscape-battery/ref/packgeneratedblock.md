---
type: simulink-block
title: 'Pack (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'packgeneratedblock'
documentation_source_path: 'ref/packgeneratedblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Pack (Generated Block)

## 端口

### 输入

### **balancing** — 平衡开关控制，unitless scalar

用于平衡策略的开关控制端口，指定为 scalar。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `BalancingStrategy` 属性设置为 `"Passive"`。

### 输出

**注意**

输出端口的名称取决于你在构成此 Pack 的基础 `Cell` 对象的 `CellModelOptions` 属性中指定的模块。

本页中的输出端口名称指的是一个 `Cell` 对象，其电池组件模型模块为 Battery (Table-Based) 模块。如果你为电池组件模型指定自定义模块，则输出端口的名称可能会不同。

**注意**

此模块的输出端口取决于你用来创建与此模块关联的 battery 对象的 Simscape cell model 模块。如果 Simscape cell model 模块具有输出端口，则 Battery Builder 会将这些输出端口转发到 battery 对象作为其子组件的所有父级生成模块。

例如，如果你创建了一个具有 **Voltage** 输出端口的自定义 Simscape cell model 模块，并最终使用它来创建此模块，则此模块具有 **Voltage** 输出端口。有关自定义 cell model 模块的详细信息，请参阅 `CellModelBlock` 对象的 `CellModelBlockPath` 属性。

### **iCell** — 电芯级电流，Ampere scalar | vector

电芯级电流。来自 Module 模块的原始信号单位是 Amperes。此信号的大小等于系统中电气模型的总数。

### **numCyclesCell** — 电芯级循环次数，unitless scalar | vector

与电池老化相关的电芯级循环次数。来自 Module 模块的原始信号单位是 unitless。此信号的大小等于系统中电气模型的总数。

### **socCell** — 电芯级荷电状态，unitless scalar | vector

电芯级荷电状态。来自 Module 模块的原始信号单位是 unitless，且该值通常在 0 到 1 之间变化。此信号的大小等于系统中电气模型的总数。

### **socParallelAssembly** — 并联组件级荷电状态，unitless scalar | vector

并联组件级荷电状态。来自 Module 模块的原始信号单位是 unitless，且该值通常在 0 到 1 之间变化。此信号的大小等于 module assembly 中并联组件的总数。

### **temperatureCell** — 电芯级温度，kelvin scalar | vector

电芯级温度。来自 Module 模块的原始信号单位是 kelvin。此信号的大小等于系统中电气模型的总数。

#### 依赖关系

要启用此端口，请启用构成 pack 的电芯的热端口。要对电芯的热端口建模，请在电芯的 `CellModelBlock` 属性中，将 `BlockParameters` 属性的 **thermal\_port** 参数设置为 `"Model"`。

### **vCell** — 电芯级电压，volts scalar | vector

电芯级电压。来自 Module 模块的原始信号单位是 volts。此信号的大小等于系统中电气模型的总数。

### **vParallelAssembly** — 并联组件级电压，volts scalar | vector

并联组件级电压。来自 Module 模块的原始信号单位是 volts。此信号的大小等于 pack 中并联组件的总数。将此信号用作 Simscape Battery 的电池管理系统 (BMS) 模块的输入。

### **CP\_Out** — 模型中每个冷却板的输出 vector of physical signals

*自 R2023a 起*

包含模型中每个冷却板的板温、流体压降和流体温度变化的向量。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **SOC** — 荷电状态，unitless scalar | vector

*自 R2024b 起*

电芯级荷电状态，指定为 scalar 或 vector。

#### 依赖关系

要启用此端口，请将 Battery (Table-Based) 模块用作此模块的 `Cell` 子对象的组件模型模块，并启用 **SOC** 端口。

### 守恒端口

### **+** — 正极端子 electrical

与电池包正极端子关联的 electrical 守恒端口。

### **-** — 负极端子 electrical

与电池包负极端子关联的 electrical 守恒端口。

### **AmbH** — 环境热端口 thermal

与环境保护热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `AmbientThermalPath` 属性设置为 `"CellBasedThermalResistance"`。

### **ClntH** — 冷却液热端口 thermal

与冷却液热路径关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，请在 `Pack` 对象中，将 `CoolantThermalPath` 属性设置为 `"CellBasedThermalResistance"`，并将 `CoolingPlate` 属性设置为 `"None"`。

### **Fluid\_In** — 进入冷却板的流体 thermal fluid

*自 R2023a 起*

与进入模型每个冷却板的流体关联的 thermal fluid 守恒端口。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **Fluid\_Out** — 流出冷却板的流体 thermal fluid

*自 R2023a 起*

与流出模型每个冷却板的流体关联的 thermal fluid 守恒端口。此端口的大小取决于模型中冷却板的数量。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `CoolingPlate` 属性设置为 `"Top"` 或 `"Bottom"`。

### **+BUS** — 正极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此 pack 内并联组件的正极关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此 pack 内一个并联组件的正极端子。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `BalancingStrategy` 属性设置为 `"External"`。

### **-BUS** — 负极端子总线 electrical array-of-nodes

*自 R2024a 起*

与此 pack 内并联组件的负极关联的 electrical array-of-nodes 守恒端口。此数组的每个元素对应于此 pack 内一个并联组件的负极端子。

#### 依赖关系

要启用此端口，将 `Pack` 对象的 `BalancingStrategy` 属性设置为 `"External"`。

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

此模块现在会公开你在与此模块关联的 `CellModelBlock` 对象的 `CellModelBlockPath` 属性中指定的 cell model 模块的相同输出端口。

### R2024a：为外部电芯平衡策略公开 electrical array-of-nodes 端口

现在，你可以公开两个 electrical array-of-nodes 端口 **+BUS** 和 **-BUS**，以便为桌面仿真和硬件在环电池仿真硬件指定并建模外部电芯平衡策略。将此选项与 Passive Balancing Interface 模块结合使用。

要指定并建模外部电芯平衡策略，请在你用于生成此自定义模型的 `Pack` 对象中，将 `BalancingStrategy` 属性设置为 `"External"`。

## 描述

生成的电池包 Simscape 模型

Pack 模块是电池包的自定义生成子系统模型。你可以通过将 `Pack` 对象作为输入参数并使用 `buildBattery` 函数来创建此 Simscape™ 子系统。Pack 子系统模块位于你在 `buildBattery` 函数的 `LibraryName` 参数中指定的 Simulink® 库中。

**注意**

为了允许结构更改和进一步自定义，当你将来自父库的 Pack (Generated Block) 掩码库模块添加到 Simulink 模型时，链接模块不包含指向父库模块的链接或路径。如果你修改任何电池结构属性，例如 `NumSeriesAssemblies` 或 `NumParallelCells`，则必须重新构建原始父库，并再次复制模型中的模块。

有关父级模块和链接模块的详细信息，请参阅 Linked Blocks。

Pack 子系统模型包含六个主要部分。

- 电池模块组件部分显示 `Pack` 对象中定义的所有 ModuleAssembly 子系统。此部分包含模块组件之间的所有串联和并联电路连接，以及对主电气端子和 ModuleAssembly 到热边界条件的附加连接。如果你需要额外的非 ModuleAssembly 电阻，则该函数会在此处添加并连接两个额外的电气电阻。
- 输出信号部分将每个 ModuleAssembly 子系统的输出分组为 Pack 子系统的单个多路复用输出信号。
- 热边界条件部分包含每个 ModuleAssembly 子系统的热边界条件。`buildBattery` 函数会从热域添加一个连接器端口，并根据指定的热边界条件将其路由到每个 ModuleAssembly 子系统。此部分是可选的，仅当你在此 `Pack` 对象中定义环境或冷却液热路径时才会出现。
- 平衡信号部分包含从电池管理系统到每个 ModuleAssembly 子系统的电芯平衡控制信号的路由。Selector 模块将控制信号的正确元素路由到其对应的 ParallelAssembly 模块。
- 冷却液 Thermal Liquid 部分包含用于在电池冷却板内部循环的冷却液的热液体网络歧管。此部分是可选的，仅当你在此 `Pack` 对象中定义冷却板时才会出现。
- Cell Outputs 部分将 cell model 模块的每个输出分组为 Pack 子系统对应的多路复用输出信号。

### 电池模块组件

此图显示了由四个电池模块组件构成的 Pack 子系统的电池模块组件部分。

### 输出信号

此图显示了由四个电池模块组件构成的 Pack 子系统的输出信号部分。

### 热边界条件

此图显示了由四个电池模块组件构成的 Pack 子系统的热边界条件部分。

### 平衡信号

此图显示了由四个电池模块组件构成的 Pack 子系统的平衡信号部分。

### 冷却液 Thermal Liquid

此图显示了由四个电池模块组件构成的 Pack 子系统的冷却液 Thermal Liquid 部分。
