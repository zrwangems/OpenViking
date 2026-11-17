---
type: simulink-block
title: 'Register Channel'
family: 'memory'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'registerchannel'
documentation_source_path: 'ref/registerchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Register Channel

## 端口

### 输入

### ***`regN`*** — 寄存器输入标量

每个寄存器分配一个端口对：一个输入和一个输出。您可以将处理器配置为写入方或读取方。如果该寄存器是读寄存器，则输入来自硬件 (HW) 侧。如果该寄存器是写寄存器，则输入来自软件 (SW) 侧。默认情况下，第 N 个寄存器端口命名为 reg*`N`*。您可以通过点击 **Registers** 参数对话框中的 **Edit** 来更改寄存器名称。

#### 依赖关系

输入端口数量取决于寄存器表中的寄存器数量。

### 输出

### ***`regN`*** — 寄存器输出标量

每个寄存器分配一个端口对：一个输入和一个输出。您可以将处理器配置为写入方或读取方。如果该寄存器配置为读寄存器，则输出送往软件 (SW) 侧。如果该寄存器是写寄存器，则输出送往硬件 (HW) 侧。默认情况下，第 N 个寄存器端口命名为 reg*`N`*。您可以通过点击 **Registers** 参数对话框中的 **Edit** 来更改寄存器名称。

#### 依赖关系

输出端口数量取决于寄存器表中的寄存器数量。

## 参数

### **Registers** — 编辑寄存器名称、方向、数据类型、维度和初始值表

此参数包含一个表，其中每一行对应您 IP 中的一个寄存器。编辑该表以添加或编辑寄存器配置，最多 32 个寄存器。

对于每个寄存器，您可以编辑以下值：

- **Register Name** – 指定寄存器名称。这会更改该寄存器的输入和输出端口。
- **Direction** – 如果处理器写入寄存器，则选择 `write`。如果处理器读取寄存器，则选择 `read`。
- **Data Type** – 选择寄存器的数据类型。支持的数据类型有

  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `int64`
  - `uint32`
  - `uint64`
  - `boolean`
  - `fixdt(1,16,0)`
  - `fixdt(1,16,2^0,0)`
  - `fixed point`
- **Dimension** – 选择寄存器的向量大小。默认值为 1。
- **Initial Value** – 设置寄存器的初始值。默认值为 0。仅当 **Direction** 设置为 `write` 时，该值适用。

### **Register write sample time** — 寄存器访问的采样时间 `-1`（默认）| 二元素向量

此采样时间表示硬件侧的时钟周期。对于离散模块或可配置子系统，通过输入二元素向量来指定偏移时间。第一个元素是采样时间，第二个元素是偏移时间。例如，输入 [1.0 0.1] 指定 1.0-second 采样时间和 0.1-second 偏移。如果未指定偏移，则默认偏移为零。

当值为 `-1` 时，模块从模型继承其采样时间值。

**注意**

当寄存器的 **Direction** 设置为 `Write` 时，它意味着软件是写入方，硬件是读取方，但 **Register write sample time** 确定硬件侧信号的采样时间。

## 所属库

SoC Blockset / Memory

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

### R2025a：设置初始值

通过编辑 **Registers** 表中的 **Initial Value** 字段，为寄存器设置初始值。

## 描述

寄存器值传输的时序模型

Register Channel 模块为处理器与硬件逻辑之间的寄存器值传输提供时序模型。寄存器通道表示处理器与硬件 IP 之间通过公共配置总线的数据通路。将模块配置为包含一个或多个寄存器，并将每个寄存器的方向配置为：如果处理器写入该寄存器，则为 write；如果处理器从该寄存器读取，则为 read。
