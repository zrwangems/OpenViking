---
type: simulink-block
title: 'Semiconductor Switch Selector'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'semiconductorswitchselector'
documentation_source_path: 'ref/semiconductorswitchselector.html'
language: zh-CN
chinese_source: worker-translation
---

# Semiconductor Switch Selector

## 端口

### 输入

### **Control** — 栅极端子物理信号

与栅极端子关联的物理信号端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`，并将 **Library block** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `MOSFET (Ideal, Switching)`
- `IGBT (Ideal, Switching)`
- `Thyristor (Piecewise, Linear)`
- `GTO`

### 守恒

### **Control** — 栅极端子电气

与栅极端子关联的电气守恒端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

#### 依赖关系

要启用此端口，请选择以下选项之一：

- 将 **Gate-control port** 设置为 `Electrical`，并将 **Library block** 设置为以下选项之一：

  - `Ideal Semiconductor Switch`
  - `MOSFET (Ideal, Switching)`
  - `IGBT (Ideal, Switching)`
  - `Thyristor (Piecewise, Linear)`
  - `GTO`
- 将 **Library block** 设置为以下选项之一：

  - `N-Channel MOSFET`
  - `P-Channel MOSFET`
  - `N-Channel IGBT`
  - `Thyristor`

### **A** — 阳极端子电气

与 GTO 或晶闸管的阳极端子、MOSFET 的漏极端子或 IGBT 的集电极端子关联的电气守恒端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

### **K** — 阴极端子电气

与 GTO 或晶闸管的阴极端子、MOSFET 的源极端子或 IGBT 的发射极端子关联的电气守恒端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

### **B** — 体端子电气

与四端子 MOSFET 的体端子关联的电气守恒端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

#### 依赖关系

要启用此端口，请将 **Number of terminals** 设置为 `Four`，并将 **Library block** 设置为以下选项之一：

- `N-Channel MOSFET`
- `P-Channel MOSFET`
- `N-Channel IGBT`

### **H** — 热质量热

与热质量关联的热守恒端口。

端口名称在模块图标中不可见，但将指针暂停在端口上可以看到此名称。

#### 依赖关系

要启用此端口，请选择以下选项之一：

- 将 **Modeling option** 设置为 `Show thermal port`，并将 **Library block** 设置为以下选项之一：

  - `MOSFET (Ideal, Switching)`
  - `IGBT (Ideal, Switching)`
  - `Thyristor (piecewise, Linear)`
  - `Thyristor`
  - `GTO`
- 将 **Library block** 设置为 `N-Channel MOSFET` 或 `P-Channel MOSFET`，并将 **Modeling option** 设置为 `threshold-based with thermal` 或 `surface-potential-based with thermal`。
- 将 **Library block** 设置为 `N-Channel IGBT`，并将 **Modeling option** 设置为 `Full I-V and capacitance characteristics | Show thermal port` 或 `Simplified I-V characteristics and event-based timing | Show thermal port`。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Switching device** — 半导体开关器件的类型 `MOSFET`（默认）| `IGBT` | `Thyristor` | `GTO`

半导体开关器件的类型。

### **Library block** — 基础库模块 `Ideal Semiconductor Switch`（默认）| `MOSFET (Ideal, Switching)` | `N-Channel MOSFET` | `P-Channel MOSFET` | ...

来自 **Simscape** > **Electrical** > **Semiconductors & Converters** > **Semiconductors** 库的基础模块。可用选项取决于 **Switching Device** 参数的值。

### **Gate-control port** — 用于指定物理或电气控制端口的选项 `PS`（默认）| `Electrical`

用于为开关栅极指定物理信号或电气守恒端口的选项。对于更简单的控制方法，请将此参数设置为 `PS`。对于更通用且高保真的控制方法，请将此参数设置为 `Electrical`。所有半导体模块都支持电气栅极，但只有部分模块支持物理信号。如果使用电气端口，并将 Semiconductor Switch Selector 模块连接到 Gate Driver 模块，则只需更改 **Library block** 参数即可轻松更改保真度级别，而无需更改栅极驱动器。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `MOSFET`，并将 **Library block** 设置为 `Ideal Semiconductor Switch` 或 `MOSFET (Ideal, Switching)`。
- 将 **Switching device** 设置为 `IGBT`，并将 **Library block** 设置为 `Ideal Semiconductor Switch` 或 `IGBT (Ideal, Switching)`。
- 将 **Switching device** 设置为 `Thyristor`，并将 **Library block** 设置为 `Thyristor (Piecewise, Linear)`。
- 将 **Switching device** 设置为 `GTO`。

### **Modeling option** — 建模选项 `No thermal port`（默认）| `Show thermal port` | `Threshold-based` | `Surface-potential based` | ...

用于确定是否公开热端口 **H**，并定义基础库模块所使用的数学模型的建模选项。可用选项取决于 **Library block** 参数的值。有关 **Modeling option** 参数值的详细信息，请参阅基础库模块的参考页。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `MOSFET`，并将 **Library block** 设置为 `MOSFET (Ideal, Switching)`、`N-Channel MOSFET` 或 `P-Channel MOSFET`。
- 将 **Switching device** 设置为 `IGBT`，并将 **Library block** 设置为 `IGBT (Ideal, Switching)` 或 `N-Channel IGBT`。
- 将 **Switching device** 设置为 `Thyristor` 或 `GTO`。

### **Number of terminals** — 端子数 `Three`（默认）| `Four`

N-Channel MOSFET、P-Channel MOSFET 或 N-Channel IGBT 模块的端子数。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `MOSFET`，并将 **Library block** 设置为 `N-Channel MOSFET` 或 `P-Channel MOSFET`。
- 将 **Switching device** 设置为 `IGBT`，并将 **Library block** 设置为 `N-Channel IGBT`。

### **Edit parameters** — 用于编辑库模块参数的按钮选项

用于编辑库模块参数的选项。单击此按钮可打开基础库模块的对话框。

### **Remove Semiconductor Switch Selector block mask** — 用于移除 Semiconductor Switch Selector 模块封装的按钮选项

用于移除 Semiconductor Switch Selector 模块封装的选项。单击此按钮可仅保留基础库模块。如果双击该模块封装，现在将打开基础库模块的对话框，并且模块图标上的端口名称将与基础库模块匹配。此操作还会启用基础模块中仅在 Semiconductor Switch Selector 模块对话框中启用的参数。此操作不可逆。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2025a 中引入**

## 描述

多保真度级别的受控半导体开关

Semiconductor Switch Selector 模块对受控开关建模，该开关表示金属氧化物半导体场效应晶体管 (MOSFET)、绝缘栅双极晶体管 (IGBT)、晶闸管或门极可关断晶闸管 (GTO)。

Simscape™ Electrical™ 包含的模块可以对同一类型的半导体器件在不同保真度级别下建模。例如，MOSFET (Ideal, Switching) 和 N-Channel MOSFET 模块都对 MOSFET 建模。要使用合适的复杂度级别开发模型，你需要根据设计过程所处阶段采用不同的保真度级别。Semiconductor Switch Selector 模块将这些不同的库模块组合在单个顶层模块封装下。使用 Semiconductor Switch Selector 模块可以更改保真度级别，而无需替换模块或重新输入已指定的参数值。

要选择和参数化基础库模块：

1. 使用 **Switching device** 参数指定半导体器件的类型。
2. 使用 **Library block** 参数指定基础库模块。
3. 使用 **Modeling option**、**Gate-control port** 和 **Number of terminals** 参数选择要在基础库模块中启用哪些端口。**Modeling option** 参数确定是否公开热端口 **H**，并定义基础库模块所使用的数学模型。这些参数的可见性取决于 **Switching device** 和 **Library block** 参数。
4. 单击 **Edit parameters** 按钮，打开基础库模块的模块对话框并指定模块参数。

要切换到不同的基础库模块，请重复步骤 2 和 4。两个模块共有的参数值会延续到你新选择的模块。Semiconductor Switch Selector 模块还会存储特定于基础库模块的参数值，因此你可以轻松返回到之前的选择。

如果你不再希望在保真度之间切换，请单击 **Remove Semiconductor Switch Selector block mask** 按钮。此按钮会移除 Semiconductor Switch Selector 模块并将其替换为基础模块。此操作不可逆。

此表显示了 Semiconductor Switch Selector 模块针对 **Switching device** 参数的每个值所支持的基础库模块。通常，你将较简单的模块用于系统级设计，将较复杂的模块用于详细组件设计。有关为应用选择正确保真度级别的详细信息，请参阅《选择用于对半导体器件建模的模块》。有关基础库模块的详细信息，请参阅此表中相关的模块参考页。

| Switching Device | Library Block | |
| --- | --- | --- |
| 低或中等保真度 | 高保真度 |
| MOSFET | - Ideal Semiconductor   Switch - MOSFET (Ideal,   Switching) | - N-Channel MOSFET - P-Channel MOSFET |
| IGBT | - Ideal Semiconductor   Switch - IGBT (Ideal, Switching) | - N-Channel IGBT |
| Thyristor | - Thyristor (Piecewise   Linear) | - Thyristor |
| GTO | - GTO | 不支持 |

如果更改 **Library block** 参数，Semiconductor Switch Selector 模块图标会更新为基础库模块的图标。

**Gate-control port**、**Modeling option** 和 **Number of terminals** 参数是 Semiconductor Switch Selector 模块和基础库模块共有的参数。但是，你必须在 Semiconductor Switch Selector 模块封装中设置这些参数的值。如果单击 **Edit parameters** 按钮，基础库模块不会启用这些参数。只有在移除 Semiconductor Switch Selector 模块封装后，才能在基础库模块中启用这些参数。

如果更改 **Library block** 参数，两个模块共有的所有参数（包括初始目标和标称值）的值都会延续到新模块。在不同模块中名称不同的等效参数的值也会延续。此表显示了 MOSFET 的等效参数。

| 等效参数 | Library Block | | | |
| --- | --- | --- | --- | --- |
| Ideal Semiconductor Switch | MOSFET (Ideal, Switching) | N-Channel IGBT | P-Channel MOSFET |
| 阈值电压 | **Threshold voltage, Vth** | | **Gate-source threshold voltage, Vth** | |
| 导通电阻 | **On-state resistance** | **Drain-source on resistance, R\_DS(on)** | | |

此表显示了 IGBT 的等效参数。

| 等效参数 | Library Block | | |
| --- | --- | --- | --- |
| Ideal Semiconductor Switch | IGBT (Ideal, Switching) | N-Channel IGBT Block |
| 阈值电压 | **Threshold voltage, Vth** | | **Gate-emitter threshold voltage, Vge(th)** |

如果更改 **Switching device** 参数，参数值不会延续。因此，你还可以使用 Semiconductor Switch Selector 模块将优化的 MOSFET 与优化的 IGBT、晶闸管或 GTO 进行比较。
