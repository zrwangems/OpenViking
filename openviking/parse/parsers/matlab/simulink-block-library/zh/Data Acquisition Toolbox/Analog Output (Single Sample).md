---
type: simulink-block
title: 'Analog Output (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'analogoutputsinglesample'
documentation_source_path: 'analogoutputsinglesample.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output (Single Sample)

## 端口
```yaml
ports:
- name: Data
  summary: 要生成的模拟输出 double
  direction: input
  data_types: double
```

### 输入

### **Data** — 要生成的模拟输出 double

要生成的模拟输出，指定为 double。如果对所有通道仅使用一个输入端口，请提供 1×N 向量，以便对所有 N 个通道执行单次扫描。

如果为每个通道使用一个端口，请为每个端口提供一个 double 值。多个端口按通道名称或设备指定的通道 ID 命名。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Device
  summary: 要通过其输出数据的设备 选择可用设备
  group: ''
- name: Channels
  summary: 设备通道选择和配置 选项取决于设备
  group: ''
- name: Number of ports
  summary: 输入数据端口数 1 for all channels | 1 per channel
  group: ''
- name: Sample time
  summary: 模块采样时间 数值
  group: ''
```

### **Device** — 要通过其输出数据的设备 选择可用设备

要从中生成数据的设备。列表中的项会有所不同，具体取决于已连接到系统的设备。列表中的设备由适配器/供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认情况下会选择第一个可用设备。CompactDAQ 机箱显示为单个设备；供应商名称、机箱 ID 和机箱型号会显示在列表中，例如 `ni cDAQ2 (cDAQ-9172)`。

### **Channels** — 设备通道选择和配置 选项取决于设备

设备通道选择和配置表。通道配置表列出设备的硬件通道，并允许您选择和配置它们。指定要从哪些通道采集数据（默认情况下会选择所有通道）。为每个选定通道指定以下参数：

**Channel ID** — 由设备指定的硬件通道 ID。Channel ID 列是只读的，并且这些参数在选定设备时定义。

**Name** — 通道名称。默认情况下，该表显示硬件提供的任何名称，但您可以编辑这些名称。例如，如果设备是带有两个通道的声卡，您可以将它们命名为 `Left` 和 `Right`。

**Module** — 通道所属的设备 ID。Module 列是只读的。如果选择了 CompactDAQ 机箱，它会显示该通道所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

**Measurement Type** — 通道的测量类型。此模块仅支持电压测量类型。（对于其他测量类型，请在 MATLAB® 中使用 DataAcquisition 对象。）

**Output Range** — 硬件支持的每个通道可用的输出范围，在选定设备时定义。

### **Number of ports** — 输入数据端口数 **1 for all channels** | **1 per channel**

输入数据端口数，指定为：

**1 for all channels**（默认）— 模块上的一个输入端口为所有通道提供数据。对于 N 个通道，以 1×N 向量形式提供数据。

**1 per channel** — 模块上的 N 个输入端口，其中 N 等于所选通道数。为每个端口提供一个 double 值。对于命名，每个输出端口使用通道名称（如果已指定），否则使用通道 ID，例如 `ao1`。

### **Sample time** — 模块采样时间 数值

模块采样时间，指定仿真期间模块的采样时间。这是仿真期间执行模块的速率。默认值为 1（仿真秒）。有关详细信息，请参阅 Timing in Hardware Interface Models 和 What Is Sample Time? (Simulink)。
## 所属库

Data Acquisition Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将单个样本输出到数据采集设备的多个模拟通道

Analog Output (Single Sample) 模块会打开、初始化、配置并控制模拟数据采集设备。设备的打开、初始化和配置在模型执行开始时发生一次。在模型运行期间，该模块每个时间步同步于硬件输出一个样本。

该模块有一个或多个输入端口，具体取决于您在其对话框中选择的选项。它没有输出端口。输入端口处信号的有效数据类型为 double。

Analog Output (Single Sample) 模块从连接到输入端口的驱动模块继承采样时间。模拟输出根据下图同步执行。

同步模拟输出的时序

在第一个时间步 (T1)，数据会输出到选定的硬件通道。在数据输出到所有通道之前，仿真不会继续。

**注意**

要使用此模块，您需要 Data Acquisition Toolbox™ 和 Simulink® 软件。

您只能将 Analog Output (Single Sample) 模块与支持单样本输出的设备一起使用。要使用不支持单样本采集的设备（例如为声音和振动设计的设备）发送数据，请使用 Analog Output 模块。

Data Acquisition Toolbox 中的 Simulink 模块不支持某些设备。要查看您的设备是否支持 Simulink，请参阅 Supported Hardware。

### 其他支持的功能

- 此模块支持使用文本加速模式，但不支持 Rapid Accelerator 或代码生成。
- 此模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
