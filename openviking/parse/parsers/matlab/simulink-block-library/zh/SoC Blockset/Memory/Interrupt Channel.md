---
type: simulink-block
title: 'Interrupt Channel'
family: 'memory'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'interruptchannel'
documentation_source_path: 'ref/interruptchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Interrupt Channel

## 端口

### 输入

### ***`interruptN`*** — 来自硬件的中断请求 `True` | `False`

每个中断都分配有一个端口对：一个输入端口和一个输出端口。默认情况下，第 *N* 个中断端口命名为 interrupt*`N`*。您可以通过在 **Interrupts** 参数中点击 **Edit** 来更改中断名称。

将此端口连接到来自 FPGA 逻辑的 Boolean 信号，或来自 Memory Channel 或 Event Source 模块的事件。

#### 依赖项

输入端口数取决于中断表中的中断数。

**数据类型：** `rteEvent` | `Boolean`
### 输出

### ***`interruptN`*** — 发送到处理器的中断请求信号标量

每个中断都分配有一个端口对：一个输入端口和一个输出端口。默认情况下，第 *N* 个中断端口命名为 interrupt*`N`*。您可以通过在 **Interrupts** 参数中点击 **Edit** 来更改中断名称。

将此端口连接到 Task Manager 模块中的任务事件输入端口。

#### 依赖项

输出端口数取决于中断表中的中断数。

**数据类型：** `rteEvent`

## 参数

### **Interrupts** — 中断名称、触发类型和优先级表

此参数包含一个表，其中每一行对应于 Interrupt Channel 模块中的一个中断。编辑该表以添加或编辑中断。中断通道最多可具有 16 个中断。

对于每个中断，您可以编辑以下值。

- **Interrupt Name** – 指定中断名称。此值会更改此中断的输入和输出端口名称。
- **Trigger Type** – 通过选择以下任一选项，为中断选择触发类型。

  - `Rising edge` – 当中断源自 FPGA 逻辑时
  - `SoC event` – 当中断源自 Memory Channel 模块或 Event Source 模块时
- **Priority** – 每个中断的优先级在 **Priority** 列中设置。此值保持静态。顶行表示最高优先级的中断。点击 **Move Up** 可提高中断的优先级。点击 **Move Down** 可降低中断的优先级。

### **Interrupt processing time** — 中断访问的处理时间 `100e-6`（默认） | 正标量

此采样时间表示中断通道仲裁并执行中断请求所需的时间。它定义为中断控制器仲裁、内核 ISR 执行以及设备驱动额外延迟所需的时间。

通过输入一个数字（以秒为单位）来指定处理时间。

## 所属库

SoC Blockset / Memory

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。参见使用 SoC Builder 生成 SoC 设计。

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

## 描述

从硬件向处理器发送中断

Interrupt Channel 模块接收来自 FPGA 逻辑或 Memory Channel 模块的中断请求，仲裁这些请求，并向 Task Manager 模块触发事件驱动的软件任务。您最多可以将 16 个设备连接到中断控制器，每个设备一个中断。该模块由以下三个部分组成：

- 中断控制器 – 此部分接受中断请求 (IRQ)，并根据用户指定的优先级对其进行仲裁。当中断控制器存在并发请求时，优先级较高的请求会先于优先级较低的请求处理。
- 内核中断服务例程 (ISR) – 此部分从中断控制器接收中断请求，服务该中断，并向中断控制器发回确认信号，以便其处理下一个 IRQ。
- IPCore 驱动程序（每个中断一个）– 此部分从内核 ISR 接收请求，并在处理器中触发事件驱动任务。

即使中断通道可以具有多个发往处理器的中断输出，它在任何给定时间发送给处理器的活动中断事件也不超过一个。

此图显示了 Interrupt Channel 模块的概念视图，该模块接受来自 FPGA 算法的中断请求。仲裁后，内核服务该请求并向处理器算法触发一个事件。

Interrupt Channel 结构
