---
type: simulink-block
title: 'Memory Controller'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'memorycontroller'
documentation_source_path: 'ref/memorycontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory Controller

## 端口

### 输入

### **burstReq*`N`*** — 内存访问请求 标量

此端口以消息形式接收内存访问请求。将此输入端口连接到 Memory Channel 或 Memory Traffic Generator 模块的突发请求消息端口（`wrBurstReq` 或 `rdBurstReq`）之一。有关消息的详细信息，请参阅 Messages。

**burstReq***`N`* 输入端口的数量由 **Number of masters** 参数定义。**burstReq***`N`* 表示第 *`N`* 个输入端口。

**数据类型：** `BurstRequest2BusObj`

### 输出

### **burstDone*`N`*** — 发往主设备的信号 标量

在主设备被授予内存访问权限且突发事务完成后，此端口发送一条表示事务已完成的消息。然后根据仲裁方案将内存访问权授予下一个主设备。有关消息的详细信息，请参阅 Messages。

**burstDone***`N`* 输出端口的数量由 **Number of masters** 参数定义。**burstDone***`N`* 表示第 *`N`* 个输入端口

**数据类型：** `BurstRequest2BusObj`

## 参数

### **Hardware board** — 查看或修改当前硬件设置 只读：当前硬件板的名称

此参数为只读。

此参数显示指向所选硬件板的链接。单击该链接可打开配置参数，调整设置或选择其他硬件板。

要了解有关内存控制器配置参数的更多信息，请参阅 FPGA design (PS mem controllers)。

### 主要

### **Memory selection** — 在内存区域之间选择 `PS memory`（默认）| `PL memory`

在处理子系统（PS）或可编程逻辑（PL）内存之间选择。

- 如果所选硬件板仅支持 PL 内存，则默认值为 `PL memory`。
- 如果所选硬件板仅支持 PS 内存或仅支持 PL 内存，则此参数为只读。
- 如果所选硬件板不是受支持的 SoC 板，则此参数不可见。

### **Number of masters** — 连接到此控制器的主设备数量 `2`（默认）| 从 `1` 到 `12` 的正整数

设置此参数以相应地生成接口，并指定有多少个主设备连接到内存。主设备的最大数量为 16。

#### 高级

### **Interconnect arbitration** — 仲裁策略 `Round robin`（默认）| `Fixed port priority`

设置内存互连模块的仲裁策略。当多个主设备请求内存访问时，策略由此参数的值决定。

- `Round robin` 基于上次服务时间设置公平仲裁。
- `Fixed port priority` 设置 **burstReq1**、**burstReq2**、**burstReq3** 等的固定优先级，其中 **burstReq1** 获得最高优先级。

### **Use hardware board settings** — 使用配置参数中的硬件实现设置 `off`（默认）| `on`

选择此参数以使用与配置参数中设置的相同的模型级设置。清除此参数以自定义此内存控制器的设置。使用自定义设置时，值仍会根据硬件特定约束进行检查。有关更多信息，请参阅 FPGA design (mem channels)。

### **Bandwidth** — 发往外部内存的事务带宽 只读：标量

此参数为只读。

此值显示内存控制器与外部内存之间计算得出的带宽。其计算方式为 **Frequency (MHz)** 乘以 **Data width (bits)**。

### **Frequency (MHz)** — 控制器时钟频率，单位为 MHz `200`（默认）| 标量

用于驱动与外部内存交互的总线的时钟速率。控制器频率决定了外部内存的整体系统带宽，该带宽必须在模型中的所有主设备之间共享。

#### 依赖关系

要启用此参数，请清除 **Use hardware board settings** 参数。

### **Data width (bits)** — 数据路径的位宽 `64`（默认）| 正整数

设置内存控制器与内存互连之间数据路径的宽度（以位为单位）。

#### 依赖关系

要启用此参数，请清除 **Use hardware board settings** 参数。

### **Bandwidth derating (%)** — 内存事务低效 0-100

对由降额百分比值指定的内存事务低效进行建模。每 100 个时钟，内存事务执行暂停的时钟数等于 **Bandwidth derating**。要设置此参数，请测量您板卡上的最大带宽，并在该参数中反映您板卡的带宽降额。请参阅 Analyze Memory Bandwidth Using Traffic Generators 中的示例。

#### 依赖关系

要启用此参数，请清除 **Use hardware board settings** 参数。

### **Request to first transfer (in clocks)** — 请求与传输开始之间的时钟周期数 非负整数

指定读或写请求与传输开始之间的延迟（以时钟周期为单位）。在 **Write** 和 **Read** 框中指定非负整数值。

此延迟是向内存控制器发出请求到其返回响应之间的时钟周期数。它在 Logic Analyzer 波形中反映为内存控制器状态保持为 `BurstAccepted` 的时间。有关在仿真中查看波形的更多信息，请参阅 Buffer and Burst Waveforms。

要设置此值，请测量您板卡上突发请求与传输开始之间的时钟周期。有关从硬件执行中提取此信息的说明，请参阅 Configuring and Querying the AXI Interconnect Monitor。

#### 依赖关系

要启用此参数，请清除 **Use hardware board settings** 参数。

### **Last transfer to transaction complete (in clocks)** — 传输结束与事务完成之间的时钟周期数 非负整数

指定内存传输结束与事务结束之间的延迟（以时钟周期为单位）。在 **Write** 和 **Read** 框中指定非负整数值。

要设置此值，请测量您板卡上突发结束与事务完成之间的时钟周期。有关从硬件执行中提取此信息的说明，请参阅 Configuring and Querying the AXI Interconnect Monitor。

#### 依赖关系

要启用此参数，请清除 **Use hardware board settings** 参数。

### 性能

点击 **Launch performance app** 以打开 Performance Metrics 窗口。有关更多信息，请参阅 Simulation Performance Plots。

## 所属库

SoC Blockset / Memory

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

为一个或多个 Memory Channel 模块仲裁内存事务

Memory Controller 模块在主设备之间进行仲裁，并授予它们对共享内存的独占访问权限。配置此模块以支持具有各种仲裁协议的多通道。Memory Controller 模块还经过插桩以记录和显示性能数据，使您能够在仿真时调试和理解系统的性能。

下图显示了 Memory Controller 模块的实现。

图中的数字代表该模块的不同延迟阶段。

1. 突发请求进入该模块。
2. 该请求可能会因仲裁而延迟，直到被授予总线访问权限。在 Interconnect arbitration 中设置仲裁策略。
3. 如果您的模型需要在第一次传输开始前增加额外延迟，请在 Request to first transfer (in clocks) 中设置该值。
4. 突发执行延迟由突发大小、数据宽度、时钟频率和 Bandwidth derating (%) 值计算得出。
5. 如果您的模型需要从突发完成到向通道发出突发响应的延迟，请在 Last transfer to transaction complete (in clocks) 中设置该值。

内存控制器具有内部状态，在使用 Logic Analyzer 查看仿真和执行指标时可见。状态值为：

- `BurstIdle`：仿真开始时，在模块接收到突发请求之前。
- `BurstRequest`：突发请求进入该模块。
- `BurstAccepted`：仲裁器接受了该突发进行处理。
- `BurstExecuting`：突发正在执行。
- `BurstDone`：突发请求执行完毕。
- `BurstComplete`：突发响应完成，突发结束。此时 **burstDone** 信号发送到主设备。

有关可视化内存控制器延迟的信息，请参阅 Memory Controller Latency Plots。
