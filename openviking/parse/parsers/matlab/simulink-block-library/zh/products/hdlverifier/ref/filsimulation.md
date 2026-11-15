---
type: simulink-block
title: 'FIL Simulation'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'Algorithm Verification / FPGA-in-the-Loop'
documentation_page: 'filsimulation'
documentation_source_path: 'ref/filsimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# FIL Simulation

## 端口

### 输入

### **HDL\_input\_port\_name** — 从 Simulink 传递到 FPGA 的信号 标量 | 向量

模块上的端口与您的 HDL 设计上的端口相对应。您可以配置 **采样时间** 和 **数据类型**。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

### 输出

### **HDL\_output\_port\_name** — 从 FPGA 传递到 Simulink 的信号 标量 | 向量

模块上的端口与您的 HDL 设计上的端口相对应。您可以配置 **采样时间** 和 **数据类型**。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## 参数

在 **硬件信息** 部分中显示的参数反映您从子系统生成 FIL Simulation 模块时所做的选择。这些参数仅供参考。

- **连接**：Ethernet 或 PCI Express®。
  有些开发板只能使用其中一种连接类型；对于其他
  开发板，您可以选择使用任一连接。生成模块时，您需要配置
  开发板的 **MAC 地址** 和 **IP 地址**。
- **开发板**：FPGA 开发板的制造商和型号。有关支持的开发板，请参阅“用于 FPGA 验证的受支持 FPGA 设备”。
- **FPGA 器件**：芯片标识号。
- **FPGA 工程文件**：为您的设计生成的 FPGA 工程文件的位置。

要将生成的 FPGA 编程文件下载到 FPGA，请在 **FPGA 编程文件** 中设置参数。在运行 FIL 仿真之前，必须执行此步骤。请参阅“将编程文件加载到 FPGA”。

要配置数据速率参数，请在 **运行时选项** 组中设置选项。

在 **信号属性** 窗格中，您可以为每个输出端口配置 **采样时间** 和 **数据类型**。信号的方向和位宽，以及输入端口的采样时间和数据类型，仅供参考。

#### FPGA 编程文件

### **文件名** — 编程文件的位置 string

为您的设计生成的 FPGA 编程文件的位置。要将此设计加载到 FPGA 进行仿真，请点击 **加载**。

#### 运行时选项

### **超频因子** — FPGA 采样率相对于 Simulink 时钟 1（默认） | integer

FPGA 时钟速率与 Simulink 时钟速率之比。对于每个 Simulink 时间步，FPGA 时钟会对输入到 FPGA 的信号采样这么多次。

### **输出帧大小** — 返回到 Simulink 的数据量 `Inherit: auto`（默认）

输出信号以 **输出帧大小**×1 列向量形式返回。增大帧大小可以通过减少 Simulink 与 FPGA 开发板之间的通信时间来加速仿真。

请注意以下关于帧大小的限制：

- 输入帧大小必须是输出帧大小的整数倍。
- 输出帧大小必须小于输入帧大小。
- 输入帧大小和输出帧大小在仿真期间不能变化。

#### 信号属性

### **采样时间** — 每个端口的采样时间 `Inherit: Inherit via internal rule`（默认）

显式设置输出信号的采样时间，或使用 `Inherit: Inherit via internal rule`。内部规则是将输出采样时间设置为输入基本采样时间除以缩放因子。

### **数据类型** — 每个端口的数据类型 `fixdt(0,N,0)`（默认） | 数据类型表达式

Simulink 如何解释来自 FPGA 的输出信号中的位。您可以显式设置输出数据类型，使用默认的非缩放无符号类型，或指定 `Inherit: auto` 以从上下文继承数据类型。

## 所属库

生成的

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012b 中引入**

## 描述

使用 Simulink 在 FPGA 硬件上仿真 HDL 代码

生成的 FPGA 在环 (FIL) 仿真模块是 FPGA 与您的 Simulink® 模型之间的通信接口。它将硬件集成到仿真循环中，并允许其像任何其他模块一样参与仿真。

您可以使用 FPGA-in-the-Loop Wizard 从现有 HDL 代码生成 FIL Simulation 模块，或者使用 HDL Workflow Advisor 生成 HDL 代码及随附的 FIL Simulation 模块。生成 HDL 代码需要 HDL Coder™ 许可证。

有关生成和仿真工作流，请参阅“使用 FIL Wizard 生成模块”。如果在 FIL 仿真期间遇到任何问题，请参阅“FIL 故障排除”以帮助诊断问题。

您可以在以 Normal、Accelerator 或 Rapid Accelerator 仿真模式运行的模型中使用 FIL Simulation 模块。FIL Simulation 参数在任何仿真模式下都不可调。有关这些模式的详细信息，请参阅“加速模式的工作原理 (Simulink)”。
