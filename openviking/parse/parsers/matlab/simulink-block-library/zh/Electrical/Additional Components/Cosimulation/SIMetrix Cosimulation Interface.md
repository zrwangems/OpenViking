---
type: simulink-block
title: 'SIMetrix Cosimulation Interface'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / Cosimulation'
documentation_page: 'simetrixcosimulationinterface'
documentation_source_path: 'ref/simetrixcosimulationinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# SIMetrix Cosimulation Interface

## 端口

### 输入

### **Uk** — 输入电压或电流 标量 | 向量

Simulink 输入端口，用于测量 Simulink 发送到 SIMetrix 的电压或电流。SIMetrix Cosimulation Interface 模块将此信号发送到 SIMetrix 模型中的第 *k* 个 Cosimulation Interface，即 `Uk`。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则关联的信号为标量。如果将 **Number of ports** 参数设置为大于 `1` 的值，则关联的信号为向量。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Output only`。
### 输出

### **Uk** — 输出电压或电流 标量 | 向量

Simulink 输出端口，用于测量 SIMetrix 发送到 Simulink 的电压或电流。SIMetrix Cosimulation Interface 模块从 SIMetrix 模型中的第 *k* 个 Cosimulation Interface，即 `Uk`，接收此信号。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则关联的信号为标量。如果将 **Number of ports** 参数设置为大于 `1` 的值，则关联的信号为向量。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Input only`。
### 守恒

### **UkI** — 用于接收电流值的单端端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的正端子关联的电气守恒端口。Simscape 将相应的负端子接地并隐藏。Simscape 向 SIMetrix 发送电压值并从 SIMetrix 接收电流值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Single-ended Current`。

### **UkI+** — 用于接收电流值的正端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的正端子关联的电气守恒端口。Simscape 向 SIMetrix 发送电压值并从 SIMetrix 接收电流值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Differential Current`。

### **UkI-** — 用于接收电流值的负端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的负端子关联的电气守恒端口。Simscape 向 SIMetrix 发送电压值并从 SIMetrix 接收电流值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Differential Current`。

### **UkV** — 用于接收电压值的单端端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的正端子关联的电气守恒端口。Simscape 将相应的负端子接地并隐藏。Simscape 向 SIMetrix 发送电流值并从 SIMetrix 接收电压值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Single-ended Voltage`。

### **UkV+** — 用于接收电压值的正端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的正端子关联的电气守恒端口。Simscape 向 SIMetrix 发送电流值并从 SIMetrix 接收电压值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Differential Voltage`。

### **UkV-** — 用于接收电压值的负端子 electrical | electrical array-of-nodes

与 SIMetrix 模型中第 *k* 个 Cosimulation Interface，即 `Uk`，的负端子关联的电气守恒端口。Simscape 向 SIMetrix 发送电流值并从 SIMetrix 接收电压值。

如果将 SIMetrix 中 Cosimulation Interface 的 **Number of ports** 参数设置为 `1`，则此端口为电气守恒端口。如果将 **Number of ports** 参数设置为大于 `1` 的值，则此端口为电气节点数组守恒端口。

#### 依赖关系

要启用此端口，请在 SIMetrix 的 Cosimulation Interface 中将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，并将 **Output Connections** 设置为 `Differential voltage`。

## 参数

### **Netlist file path** — SPICE 网表 `net.net`（默认值）| 文本的文件路径

SPICE 网表的文件路径。

### **Browse** — 使用系统浏览器按钮选择网表

浏览按钮。单击此按钮可使用系统浏览器选择 SPICE 网表文件。

### **Build I/O** — 构建输入/输出设备按钮

构建输入/输出设备。单击此按钮可创建或更新 SIMetrix Cosimulation Interface 模块与 SIMetrix 网表之间的虚拟连接。

### **Sample time (s)** — 采样时间 `2e-5`（默认值）| 正标量

采样时间，以秒为单位。此值描述 SIMetrix 向 Simulink 提供输出的固定速率。必须将此参数设置为足够小的值，以便 Simulink 能够从 SIMetrix 仿真中捕获重要的动态特性。

## 所属库

Simscape / Electrical / Additional Components / Cosimulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

使用 SIMetrix 模型连接 Simulink 信号与 Simscape Electrical 节点

SIMetrix Cosimulation Interface 模块在 Simulink® 信号与 Simscape™ Electrical™ 节点以及 SIMetrix 网表之间创建虚拟连接。使用此模块可通过 Simscape 和 SIMetrix 运行协同仿真。通过运行协同仿真，您可以将不同工具中开发的设计集成到 Simscape 模型中。例如，您可以：

- 使用器件制造商提供的模型在 SIMetrix 中对电子电路进行建模。
- 使用 Simscape 设计电气、机电及其他多域系统。
- 使用 Simulink 设计控制系统。

协同仿真可以改善团队集成。您可以使用 Simulink 和 Simscape 构建一个系统级模型，用理想开关对半导体器件进行建模。然后，为了验证该模型，您可以使用在 SIMetrix 中开发的电子电路详细设计来运行协同仿真。您还可以使用协同仿真来测试在 SIMetrix 中开发的电路在真实负载（例如 Simscape Electrical 中的电机）下的表现。

协同仿真是 `subcircuit2ssc` 函数的替代方案，该函数将 SPICE 子电路转换为等效的 Simscape 组件。对于在 SIMetrix 中开发的 SPICE 模型，协同仿真通常是更好的选择。`subcircuit2ssc` 函数仅适用于转换包含少量 R、L、C 和晶体管器件的电路。大型半导体器件网络仿真难度更大，只有使用其最初编写时所针对的 SPICE 仿真引擎才能可靠仿真。

要运行协同仿真，您还需要在 SIMetrix 原理图中使用 Cosimulation Interface。下图展示了 SIMetrix 中的 Cosimulation Interface 如何与 Simscape 中的 SIMetrix Cosimulation Interface 模块交换信息。

图展示了 SIMetrix 和 Simulink 如何交换信息。SIMetrix 电路与 SIMetrix 中的 Cosimulation Interface 交换电压和电流值。SIMetrix 之间的虚拟连接将电流值从 SIMetrix 中的 Cosimulation Interface 传递到 Simscape 中的模块，并将电压值从 Simscape 中的模块传递到 SIMetrix 中的 Cosimulation Interface。Simscape 中的模块与 Simscape Electrical 电路交换电压和电流值。

在您的 Simscape 模型中，SIMetrix Cosimulation Interface 模块代表您希望在 SIMetrix 中仿真的那部分电气网络。您可以使用信号线将此模块连接到 Simulink 模块图，或使用物理连接线将其连接到 Simscape 中的电气网络。您还可以选择 SIMetrix 向 Simscape 发送电压值还是电流值。

您可以独立构建 SIMetrix 原理图和 Simscape 模型。但是，SIMetrix Cosimulation Interface 模块的端口数量、名称和类型取决于您在 SIMetrix 中为 Cosimulation Interface 选择的选项。因此，要为协同仿真准备模型，您需要先更新 SIMetrix 原理图。要在 Simscape 模型中使用 SIMetrix Cosimulation Interface 模块，您首先需要将带有预定义 Simulink 接口的 SIMetrix 原理图保存为网表：

1. 构建您要在 SIMetrix 中仿真的电子电路原理图。
2. 在 SIMetrix 原理图中创建 Cosimulation Interface — 在 Command Shell 中，输入 `Simulink_create_interface_symbol`。
3. 配置 Cosimulation Interface 并将其连接到您的电路 — 具体操作方式取决于您希望 SIMetrix 和 Simscape 交换哪些信息。有关完成此步骤的更多信息，请参阅 Create Virtual Connections。
4. 将原理图转换为网表 — 在 SIMetrix Command Shell 中，输入 `netlist`，后跟网表名称。例如，`netlist yourNetlistName.net`。

在 SIMetrix 中保存网表后，您需要构建要在 Simscape 中仿真的模块图或电气网络。然后使用 SIMetrix Cosimulation Interface 模块在 SIMetrix 和 Simscape 模型之间创建虚拟连接。使用 SIMetrix Cosimulation Interface 模块的 **Netlist file path** 参数指定 SPICE 网表的文件路径，或点击 **Browse** 按钮使用系统浏览器选择 SPICE 网表。然后，要构建输入/输出设备，点击 **Build I/O** 按钮。此操作会创建 SIMetrix 和 Simscape 之间的虚拟连接，并在 SIMetrix Cosimulation Interface 模块中启用正确的端口。

您可以使用 **Sample time (s)** 参数设置 SIMetrix 向 Simulink 提供输出的固定速率。在采样时间之间，SIMetrix 使用可变步长求解器运行。您必须将 **Sample time (s)** 参数设置为足够小的值，以便 Simulink 能够捕获 SIMetrix 仿真中的重要动态特性。这种配置——SIMetrix 仿真使用可变时间步长，并在 Simulink 仿真中以固定速率采样——意味着当您在 SIMetrix 中对较快的动态特性进行建模，并在 Simulink 或 Simscape 中对较慢的动态特性进行建模时，协同仿真的效率最高。例如，当您通过在 SIMetrix 中对电力电子进行建模，并在 Simscape 中对电机和机械负载进行建模来对电机驱动进行建模时，协同仿真可以高效运行。

当您运行模型时，SIMetrix 和 Simscape 一起仿真。SIMetrix 和 Simscape 都可以存储结果。您可以使用任一软件对数据进行可视化和后处理。

SIMetrix Cosimulation Interface 模块支持 SIMetrix Pro 和 SIMetrix Elite 9.1 及更高版本。

### 创建虚拟连接

SIMetrix Cosimulation Interface 模块的端口数量、名称和类型取决于您在 SIMetrix 中为 Cosimulation Interface 选择的选项。要创建虚拟连接，您需要了解这些选项。

**Configuration** 参数决定 SIMetrix 是向 Simulink 或 Simscape 发送信息还是从 Simulink 或 Simscape 接收信息。**Input connections** 和 **Output connections** 参数决定这些信息的性质。您可以交换电流值、电压值或两者。您还可以选择是测量相对于地的电压值，还是对两个独立的连接进行建模。**Number of ports** 参数决定 SIMetrix 中 Cosimulation Interface 的端口数量。

您可以将 **Configuration** 参数设置为：

- `Input only` — SIMetrix 将电压或电流值作为输入发送到 Simulink。选择此选项会启用 **Input connections** 参数。相应的 SIMetrix Cosimulation Interface 模块具有一个 Simulink 输出端口。
- `Output only` — SIMetrix 从 Simulink 接收电压或电流值作为输出。选择此选项会启用 **Output connections** 参数。相应的 SIMetrix Cosimulation Interface 模块具有一个 Simulink 输入端口。
- `Combined Input Output V/I or I/V` — SIMetrix 向 Simscape 发送电压或电流值，并从 Simscape 接收电流或电压值。选择此选项会启用 **Output connections** 参数。SIMetrix 会自动为 **Input connections** 参数选择适当的值。相应的 SIMetrix Cosimulation Interface 模块具有一个或两个 Simscape 守恒端口。

您可以将 **Input connections** 或 **Output connections** 参数设置为：

- `Single-ended Voltage`
- `Differential Voltage`
- `Single-ended Current`
- `Differential Current`

选择 `Single-ended Voltage` 或 `Single-ended Current` 会有效地将负极端子接地并隐藏。

如果您将 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`，则输入和输出配置必须具有相同的端口数量，并具有相同类型的连接，即单端或差分。如果您还将 **Output Connections** 参数设置为 `Single-ended Voltage` 或 `Single-ended Current`，则 SIMetrix Cosimulation Interface 模块具有一个守恒端口。如果您将 **Output Connections** 参数设置为 `Differential Voltage` 或 `Differential Current`，则 SIMetrix Cosimulation Interface 模块具有两个守恒端口。

下表总结了 SIMetrix 如何与 Simulink 或 Simscape 交换信息。该表还显示了相应的 SIMetrix Cosimulation Interface 所具有的端口类型以及这些端口的名称。

| Configuration 参数值 | Input Connections 参数值 | Output Connections 参数值 | 信息交换 | SIMetrix Cosimulation Interface 模块端口类型 | SIMetrix Cosimulation Interface Simulink 模块图 |
| --- | --- | --- | --- | --- | --- |
| `Input Only` | `Single-ended Voltage` | N/A | SIMetrix 将电压值作为输入发送到 Simulink。 | Simulink 输出端口 **U1** | 具有一个输出端口 U1 的模块的 Simulink 模块图。该端口通过 Simulink 信号线连接到 Outport 模块。 |
| `Differential Voltage` | N/A |
| `Single-ended Current` | N/A | SIMetrix 将电流值作为输入发送到 Simulink。 |
| `Differential Current` | N/A |
| `Output Only` | N/A | `Single-ended Voltage` | SIMetrix 从 Simulink 接收电压值作为输出。 | Simulink 输入端口 **U1** | 具有一个输入端口 U1 的模块的 Simulink 模块图。该端口通过 Simulink 信号线连接到 Inport 模块。 |
| N/A | `Differential Voltage` |
| N/A | `Single-ended Current` | SIMetrix 从 Simulink 接收电流值作为输出。 |
| N/A | `Differential Current` |
| `Combined Input Output V/I or I/V` | `Single-ended Current` | `Single-ended Voltage` | SIMetrix 向 Simscape 发送电流值，并从 Simscape 接收电压值。 | Simscape 守恒端口 **U1V** | 具有一个守恒端口 U1V 的模块的 Simscape 网络图。该端口通过物理连接线连接到 Connection Port 模块。 |
| `Differential Current` | `Differential Voltage` | Simscape 守恒端口 **U1V+** 和 **U1V-** | 具有两个守恒端口 U1V+ 和 U1V- 的模块的 Simscape 网络图。这些端口通过物理连接线连接到 Connection Port 模块。 |
| `Single-ended Voltage` | `Single-ended Current` | SIMetrix 向 Simscape 发送电压值，并从 Simscape 接收电流值。 | Simscape 守恒端口 **U1I** | 具有一个守恒端口 U1I 的模块的 Simscape 网络图。该端口通过物理连接线连接到 Connection Port 模块。 |
| `Differential Voltage` | `Differential Current` | Simscape 守恒端口 **U1I+** 和 **U1I-** | 具有两个守恒端口 U1I+ 和 U1I- 的模块的 Simscape 网络图。这些端口通过物理连接线连接到 Connection Port 模块。 |

**注意**

如果您在 SIMetrix 中只有一个 Cosimulation Interface，则此表中的端口数量、名称和类型始终适用。但是，一个 SIMetrix Cosimulation Interface 模块对应一个 SIMetrix 原理图或网表，而不是一个 Cosimulation Interface。您可以通过在 SIMetrix 中使用多个 Cosimulation Interface 来构建具有更多端口和多种端口类型的 SIMetrix Cosimulation Interface 模块。SIMetrix 将每个 Cosimulation Interface 标记为 `Uk`，其中 `k` 是介于 `1` 和原理图中 Cosimulation Interface 数量之间的整数。这些编号对应于 SIMetrix Cosimulation Interface 模块端口名称中的编号。

**Number of ports** 参数定义 SIMetrix 中 Cosimulation Interface 的端口数量。此参数不影响 Simscape 中 SIMetrix Cosimulation Interface 模块的端口数量。相反，端口类型会发生变化，以支持正确数量的电压或电流值。如果您将此参数设置为 `1`：

- Simulink 输入和输出端口承载标量信号。
- Simscape 端口是电气守恒端口。

如果您将此参数设置为大于 `1` 的值：

- Simulink 输入和输出端口承载向量信号。
- Simscape 端口是电气节点数组守恒端口。您可以使用 Array Connection 模块将 SIMetrix Cosimulation Interface 模块连接到您的电气网络。

**在 SIMetrix 原理图和 Simscape Electrical 网络之间创建虚拟连接**

要在 SIMetrix 原理图和 Simscape Electrical 网络之间创建连接，请将 SIMetrix 中 Cosimulation Interface 的 **Configuration** 参数设置为 `Combined Input Output V/I or I/V`。

要在 Simscape 中对感性负载或电流源进行建模，请将 **Output connections** 参数设置为 `Single-ended Voltage` 或 `Differential Voltage`。要在 Simscape 中对容性负载或电压源进行建模，请将 **Output connections** 参数设置为 `Single-ended Current` 或 `Differential Current`。要在 Simscape 中对纯电阻负载进行建模，您可以使用这些选项中的任意一个。

下表显示了用于协同仿真的相应 SIMetrix 原理图和 Simscape 网络的简单示例。该表还显示了完全在 Simscape 中建模的等效电气网络。Simscape 网络中的 Inductor 和 Capacitor 模块分别表示任何感性或容性负载。

| 目标 | 输入连接 | 输出连接 | 协同仿真示例 SIMetrix 原理图 | 协同仿真示例 Simscape 网络 | 等效 Simscape 网络 |
| --- | --- | --- | --- | --- | --- |
| 在 Simscape 中建模感性负载 | `Single-ended Current` | `Single-ended Voltage` | 一个电阻连接到具有一个端口的 Cosimulation Interface 的 SIMetrix 原理图 | 一个具有一个 conserving 端口的模块连接到一个 Inductor 模块的 Simscape 网络图 | 一个电阻和一个电感连接成闭合回路的 Simscape 网络图 |
| `Differential Current` | `Differential Voltage` | 一个电阻连接到具有两个端口并形成闭合回路的 Cosimulation Interface 的 SIMetrix 原理图 | 一个具有两个 conserving 端口的模块连接到一个 Inductor 模块并形成闭合回路的 Simscape 网络图 |
| 在 Simscape 中建模容性负载 | `Single-ended Voltage` | `Single-ended Current` | 一个电阻连接到具有一个端口的 Cosimulation Interface 的 SIMetrix 原理图 | 一个具有一个 conserving 端口的模块连接到一个 Capacitor 模块的 Simscape 网络图 | 一个电阻和一个电容连接成闭合回路的 Simscape 网络图 |
| `Differential Voltage` | `Differential Current` | 一个电阻连接到具有两个端口并形成闭合回路的 Cosimulation Interface 的 SIMetrix 原理图 | 一个具有两个端口的模块连接到一个 Capacitor 模块并形成闭合回路的 Simscape 网络图 |

**在 SIMetrix 原理图与 Simulink 模块图之间创建虚拟连接**

要在 SIMetrix 原理图与 Simulink 模块图之间创建虚拟连接，请将 SIMetrix 中 Cosimulation Interface 的 **Configuration** 参数设置为 `Input only` 或 `Output only`。这些图展示了一个同时具有输入和输出的简单示例。

一个具有输入和输出的模块的 Simulink 模块图

一个具有输入和输出的 Cosimulation Interface 的 SIMetrix 原理图

Simulink 输入端口 **U1** 将栅极-发射极电压信号发送到 SIMetrix 原理图中的 IGBT。此端口对应于 SIMetrix 中的 `U1` Cosimulation Interface。要创建虚拟连接，请在 Cosimulation Interface 中设置：

- **Configuration** 为 `Output only`
- **Output connections** 为 `Differential Voltage`
- **Number of ports** 为 `1`

Simulink 输出端口 **U2** 从 SIMetrix 中的 IGBT 接收单端集电极电压信号。此端口对应于 SIMetrix 中的 `U2` Cosimulation Interface。要创建虚拟连接，请在 Cosimulation Interface 中设置：

- **Configuration** 为 `Input only`
- **Input connections** 为 `Single-ended Voltage`
- **Number of ports** 为 `1`。
