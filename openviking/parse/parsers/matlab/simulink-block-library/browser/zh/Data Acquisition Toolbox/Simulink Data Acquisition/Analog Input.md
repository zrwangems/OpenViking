---
type: simulink-block
title: 'Analog Input'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: 'Simulink Data Acquisition'
documentation_page: 'analog_input'
documentation_source_path: 'analog_input.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Data** — 获取的模拟输入 double

获取的模拟输入数据，以 double 形式返回。如果所有通道仅使用一个输出端口，则每次扫描可作为大小为 blocksize × 通道数的矩阵，即 M-by-N。如果为每个通道使用一个端口，则每次扫描会在每个端口上生成一个 blocksize-by-1 列向量。多个端口根据通道名称或设备指定的通道 ID 命名。

**数据类型：** `double`

### **Relative timestamp** — 扫描的相对时间戳

每次扫描的相对时间戳，以 double 形式返回。当您选中 Output relative timestamps 参数时，此端口可用。

**数据类型：** `double`

## 参数

使用 Block Parameters 对话框选择采集模式并设置其他配置选项。

### **Device** — 要从中获取数据的设备

要从中获取数据的设备。列表中的项会有所不同，具体取决于您已连接到系统的设备。列表中的设备由适配器或供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认情况下，选择第一个可用设备。CompactDAQ 机箱将显示为单个设备，由供应商名称、机箱 ID 和机箱型号标识；例如，`ni cDAQ2 (cDAQ-9172)`。

### **Acquisition Mode** — 同步设置 **Asynchronous** | **Synchronous**

同步设置，指定为以下选项之一。

**Asynchronous** — 在异步模式下，设备的数据采集和仿真并行进行。当仿真开始时，模型会启动从设备采集数据。随着仿真运行，来自设备的数据会连续采集到 FIFO（先进先出）缓冲区中。在每个时间步，模型从 FIFO 缓冲区获取数据并输出一个数据块。FIFO 缓冲区中的数据根据硬件采集时钟是连续的。

**Synchronous** — 在同步模式下，从设备采集数据时会阻塞仿真。模型在每个时间步启动从设备采集，并立即进入等待状态，直到采集请求完成。这是无缓冲输入；模块在每个时间步输出最新的数据块。

以下图示显示了 Analog Input 模块的同步模式与异步模式之间的区别。

**Synchronous Analog Input**

同步模拟输入的时序

在第一个时间步（T1），针对所需数据块（B1）启动采集。在 B1 完全采集之前，仿真不会继续。

**Asynchronous Analog Input – 场景 1**

当必须阻塞更快的仿真时，异步模拟输入的时序

场景 1 显示仿真速度超过数据采集速度的情况。在第一个时间步（T1），所需数据块（B1）仍在采集中。因此，在 B1 完全采集之前，仿真不会继续。

**Asynchronous Analog Input – 场景 2**

不阻塞仿真的异步模拟输入时序

场景 2 显示数据采集速度超过仿真速度的情况。在第一个时间步（T1），所需数据块（B1）已完全采集。因此，仿真会连续运行。

**注意**

包括设备硬件和模型复杂度在内的若干因素可能会影响仿真速度，导致场景 1 和场景 2 在同一仿真中均可能出现。

### **Channels** — 设备通道选择和配置选项取决于设备

设备通道选择和配置表。通道配置表列出设备的硬件通道，并允许您选择和配置它们。指定要从哪些通道获取数据（默认情况下，所有通道均被选中）。为每个所选通道指定以下参数：

**Channel ID** — 由设备指定的硬件通道 ID。Channel ID 列是只读的，这些参数在选择设备时定义。

**Name** — 通道名称。默认情况下，该表显示硬件提供的任何名称，但您可以编辑这些名称。例如，如果设备是具有两个通道的声卡，您可以将它们命名为 `Left` 和 `Right`。

**Module** — 通道所属的设备 ID。Module 列是只读的。如果选择了 CompactDAQ 机箱，它会显示该通道所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

**Measurement Type** — 通道的测量类型。此模块仅支持电压测量类型。（对于其他测量类型，请在 MATLAB® 中使用 DataAcquisition 对象。）

**Input Range** — 硬件支持的每个通道可用的输入范围，在选择设备时定义。

**Terminal Configuration** — 指定硬件端子配置，例如单端、差分等。端子配置选项由所选通道的功能定义。

**Coupling** — 硬件耦合配置，例如 AC 或 DC。耦合类型在选择设备时定义。

### **Number of ports** — 输出数据端口数 **1 for all channels** | **1 per channel**

输出数据端口数，指定为：

**1 for all channels** — 从单个端口输出数据为矩阵，大小为 blocksize × 所选通道数。

**1 per channel** — 从 N 个端口输出数据，其中 N 等于所选通道数。每个输出端口是一个大小为 blocksize-by-1 的列向量。对于命名，每个输出端口使用通道名称（如果已指定），否则使用通道 ID，例如 `ai0`。

### **Input sample rate** — 设备采样率数值

从设备采集样本的速率，以每秒采样数表示。这是硬件的采样率。采样率必须是在所选硬件支持范围内的正实数。

### **Block size** — 每个时间步的扫描数整数值

每个时间步要为每个通道从模块输出读取的数据样本数。它必须是大于或等于 2 的正整数，且在所选硬件支持的范围内。

### **Output relative timestamps** — 添加时间戳输出端口

选择此选项可输出相对数据时间戳，每个样本一个。此选项会向模块添加一个新的输出端口。此端口的数据类型为 double，对应于样本相对于采集开始的时间偏移（秒）。对于异步采集，采集在模型执行开始时启动一次，相对时间戳是相对于仿真开始的单调递增值。对于同步采集，每个时间步都会启动一次采集；因此，每次启动采集时相对时间戳都会重置为零。

## 所属库

Data Acquisition Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从数据采集设备的多个模拟通道获取数据

Analog Input 模块会打开、初始化、配置并控制模拟数据采集设备。设备的打开、初始化和配置在模型执行开始时发生一次。在模型运行期间，模块以同步（提供设备当前正在提供的数据块）或异步（流式传输缓冲的传入数据）方式采集数据。

该模块没有输入端口。它有一个或多个输出端口，具体取决于您在其对话框中选择的配置。

使用 Analog Input 模块将实时测量数据纳入 Simulink®，用于：

- 系统表征
- 算法验证
- 系统和算法建模
- 模型和设计验证
- 控制器设计

下图显示了基本的模拟输入使用配置，使用该配置您可以：

- 在每个时间步或每次模型执行时读取获取的数据。
- 分析数据，或将其用作模型中系统的输入。
- 可选地显示结果。

模型中连接的 Analog Input 模块

**注意**

要使用此模块，您需要 Data Acquisition Toolbox™ 和 Simulink 软件。

Data Acquisition Toolbox 中的 Simulink 模块不支持某些设备。要查看您的设备是否支持 Simulink，请参阅 Supported Hardware。

只能将 Analog Input 模块用于支持时钟采集的设备。要使用不支持时钟采集的设备获取数据，请使用 Analog Input (Single Sample) 模块。

### 其他支持的功能

- 如果您拥有 DSP System Toolbox™，则可以将此模块用于信号应用。
- 此模块支持使用文本加速模式，但不支持 Rapid Accelerator 或代码生成。
- 该模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
