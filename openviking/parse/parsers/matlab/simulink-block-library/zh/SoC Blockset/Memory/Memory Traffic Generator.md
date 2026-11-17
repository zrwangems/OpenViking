---
type: simulink-block
title: 'Memory Traffic Generator'
family: 'memory'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'memorytrafficgenerator'
documentation_source_path: 'ref/memorytrafficgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory Traffic Generator

## 端口

### 输入

### **burstDone** — 突发结束和内存访问 scalar

此消息端口接收来自所连接的 Memory Controller 模块的控制消息，指示请求的突发事务已完成。将 Memory Controller 模块的 **burstDone** 输出信号连接到此端口。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

当您选中 **Show Memory Controller ports** 参数时，此端口可见。

**数据类型：** `BurstRequest2BusObj`
### 输出

### **burstReq** — 向内存控制器请求内存访问 scalar

此消息端口发送一条消息，请求从内存控制器进行突发访问。将此端口连接到 Memory Controller 模块的 **burstReq** 输入端口。有关消息的详细信息，请参阅 Messages。

#### 依赖关系

当您选中 **Show Memory Controller ports** 参数时，此端口可见。

**数据类型：** `BurstRequest2BusObj`

## 参数

### **Show Memory Controller ports** — 显示输入和输出端口 `on`（默认）| `off`

当在包含 Memory Channel 模块和 Memory Controller 模块的系统中使用 Memory Traffic Generator 模块时，选择此选项。

当将 Memory Traffic Generator 模块与以下专用内存模块之一一起使用时，清除此选项：

- AXI4 Random Access Memory
- Software to AXI4-Stream
- AXI4-Stream to Software
- AXI4 Video Frame Buffer

当在设计中使用专用内存模块时，该模块包含一个内存控制器，Memory Traffic Generator 模块会隐式地与其通信，因此不需要端口。

### **Memory selection** — 在内存区域之间选择 `PS memory`（默认）| `PL memory`

在处理子系统 (PS) 内存或编程逻辑 (PL) 内存之间进行选择。

- 如果所选开发板仅支持 PL 内存，则默认值为 `PL memory`。
- 如果所选开发板仅支持 PS 内存或仅支持 PL 内存，则此参数为只读。
- 如果所选开发板不是受支持的 SoC 开发板，则此参数不可见。

#### 依赖关系

要启用此参数，请清除 **Show Memory Controller ports** 参数。

### **Request type** — 在写请求或读请求之间选择 `Writer`（默认）| `Reader`

选择模块要生成的请求类型为写请求或读请求。分别指定 `Writer` 或 `Reader`。

### **Total burst requests** — 要生成的突发请求数 `100`（默认）| integer greater than 1

将此值设置为大于 1 的整数，以生成重复的流量模式。

### **Burst size (bytes)** — 生成的突发事务大小 `256`（默认）| scalar

以字节为单位指定每个突发事务的大小。此参数与数据通路宽度（在配置参数中配置）共同控制突发长度。

例如，如果突发大小为 256 字节，并且 Memory Channel 模块配置为 **Data width (bits)** 设为 64（8 字节），则 **Burst length** 计算为 256/8 = 32。

### **Time between bursts (s)** — 突发请求之间的仿真时间 `1e-6`（默认）| time, in seconds

指定突发请求之间的仿真时间，以秒为单位。

#### 依赖关系

要启用此参数，请清除 **Allow simulation only parameters** 参数。

**提示**

如果您清除了 **Allow simulation only parameters** 且此参数不可见，请单击 Block Parameters 对话框底部的 **Apply**。

### **Allow simulation only parameters** — 仅为仿真配置附加参数 `on`（默认）| `off`

选择此参数以启用仅仿真参数的配置。

### **First burst time** — 初始突发请求的仿真时间 `10e-6`（默认）| time, in seconds

指定发送初始突发请求的仿真时间，以秒为单位。此值必须为正实数标量。

#### 依赖关系

要启用此参数，请选择 **Allow simulation only parameters** 参数。

### **Random time between bursts (s)** — 重复请求的仿真时间范围 `[1e-6 1e-6]`（默认）| vector of the form [*min* *max*]

使用形式为 [*min* *max*] 的向量指定突发请求之间的仿真时间范围。

- *min* 是重复请求之间的最小时间，以秒为单位。
- *max* 是重复请求之间的最大时间，以秒为单位。

*min* 和 *max* 必须为非负值，并且 *max* 必须大于 *min*。

要指定确定性速率，请将请求之间的最小时间和最大时间设置为相同值。如果需要可重复的随机化，请在配置参数的 **Hardware Implementation** 窗格中指定种子。有关设置种子值的详细信息，请参阅 Simulation settings。

#### 依赖关系

要启用此参数，请选择 **Allow simulation only parameters** 参数。

### **Wait for burst done** — 在生成下一个请求之前等待 burst-done 信号 `off`（默认）| `on`

选择此参数以在生成下一个突发请求之前等待来自上一个突发的 burst-done 信号。清除此参数可在不考虑其他主设备流量的情况下生成突发请求。要获得已知数据速率，请清除此参数。

### **Enable assertion** — 启用详细诊断信息 `off`（默认）| `on`

选择此参数可查看 Traffic Generator 模块丢弃数据包时的诊断消息。清除此参数可提高仿真性能。

### **View performance plots** — 显示性能指标按钮

单击该按钮将打开 **Performance Plots for Memory Controller** 窗口。然后，您可以选择绘制带宽、突发或延迟。有关性能图的详细信息，请参阅 Memory Controller Latency Plots。

#### 依赖关系

要启用此参数，请清除 **Show Memory Controller ports** 参数。

## 所属库

SoC Blockset / Memory

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成

使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换

使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

生成发往内存控制器的流量

当连接到内存控制器时，Memory Traffic Generator 模块会生成对内存的读或写请求，充当主设备。使用此模块可对主设备的内存访问对算法造成的影响进行建模，而无需显式仿真该主设备的行为。您还可以使用 Memory Traffic Generator 模块来表征内存子系统在不同内存访问争用程度下的性能。

**注意**

为了对内存争用建模，Memory Traffic Generator 模块会获取内存访问权、参与仲裁并释放访问权。Memory Traffic Generator 模块不会主动从内存读取或写入。
