---
type: simulink-block
title: 'Analog Output'
family: 'data-acquisition-toolbox'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: 'Data Acquisition Toolbox'
documentation_page: 'analog_output'
documentation_source_path: 'analog_output.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output

## 端口

### 输入

### **Data** — 要生成的模拟输出 double

要生成的模拟输出，指定为 doubles。如果对所有通道仅使用一个输入端口，请为 M 个扫描、N 个通道的 blocksize 指定一个 M-by-N 矩阵。每个扫描是跨 N 个通道的一行。每个通道输出 M 个扫描组成的一列。

如果为每个通道使用一个端口，请在每个端口上为每个通道指定一列数据。多个端口按通道名称或设备指定的通道 ID 命名。

**数据类型：** `double`

## 参数

### **Device** — 用于输出数据的设备，选择可用设备

要从中生成数据的设备。列表中的项会有所不同，具体取决于已连接到系统的设备。列表中的设备由适配器/供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认情况下会选择第一个可用设备。CompactDAQ 机箱显示为单个设备；列表中会显示供应商名称、机箱 ID 和机箱型号，例如 `ni cDAQ2 (cDAQ-9172)`。

### **Channels** — 设备通道选择和配置选项取决于设备

设备通道选择和配置表。通道配置表列出设备的硬件通道，并允许您选择和配置它们。指定要从哪些通道获取数据（默认情况下会选择所有通道）。为每个选定通道指定以下参数：

**Channel ID** — 由设备指定的硬件通道 ID。Channel ID 列是只读的，这些参数在选定设备时定义。

**Name** — 通道名称。默认情况下，表会显示硬件提供的任何名称，但您可以编辑这些名称。例如，如果设备是带两个通道的声卡，您可以将它们命名为 `Left` 和 `Right`。

**Module** — 该通道所属的设备 ID。Module 列是只读的。如果选择了 CompactDAQ 机箱，它会显示该通道所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

**Measurement Type** — 通道的测量类型。此模块仅支持电压测量类型。（对于其他测量类型，请在 MATLAB® 中使用 DataAcquisition 对象。）

**Output Range** — 硬件支持的每个通道可用的输出范围，在选定设备时定义。

### **Number of ports** — 输入数据端口数 **1 for all channels** | **1 per channel**

输入数据端口数，指定为：

**1 for all channels**（默认）— 模块上所有通道使用一个输入端口。以矩阵形式提供数据，大小为扫描 blocksize 乘通道数，即 M-by-N。

**1 per channel** — 模块上有 N 个输入端口，其中 N 等于所选通道数。为每个端口提供大小为 blocksize-by-1 的列向量数据。命名时，每个输出端口使用已指定的通道名称（如果指定了），否则使用通道 ID，例如 `ao1`。

### **Output sample rate** — 设备采样率数值

采样从 Simulink 输出到设备的速率，以 samples per second 为单位。这是硬件的采样率。默认值在选定设备时定义。采样率必须是所选硬件允许范围内的正实数。

## 所属库

Data Acquisition Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将数据输出到数据采集设备的多个模拟通道

Analog Output 模块会打开、初始化、配置并控制模拟数据采集设备。设备的打开、初始化和配置在模型执行开始时进行一次。在模型运行期间，该模块同步地将数据输出到硬件（在数据提供时输出该数据块）。在每个时间步，该模块对硬件执行阻塞式同步写入，输出整个输入数据。

下图显示了同步模拟输出的时序。

同步模拟输出的时序

在第一个时间步 (T1)，数据输出开始，并将对应的数据块 (B1) 输出到硬件。在 B1 完全输出之前，仿真不会继续。

该模块有一个或多个输入端口，具体取决于您在其参数对话框中选择的选项。它没有输出端口。

Analog Output 模块从连接到输入端口的驱动模块继承采样时间。输入端口处信号的有效数据类型为 double 或硬件支持的原生数据类型。

**注意**

要使用此模块，您需要 Data Acquisition Toolbox™ 和 Simulink® 软件。

只能将 Analog Output 模块与支持时钟控制生成的设备一起使用。要使用不支持时钟控制的设备生成数据，请使用 Analog Output (Single Sample) 模块。

Data Acquisition Toolbox 中的 Simulink 模块不支持某些设备。要查看您的设备是否支持 Simulink，请参阅支持的硬件。

### 其他支持的功能

- 此模块支持使用 text accelerator mode，但不支持 Rapid Accelerator 或代码生成。
- 该模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
