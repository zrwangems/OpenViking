---
type: simulink-block
title: 'Analog Input (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'analoginputsinglesample'
documentation_source_path: 'analoginputsinglesample.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input (Single Sample)

## 端口

### 输出

### **Data** — 采集的模拟输入 double

采集的模拟输入数据，以 double 形式返回。如果所有通道仅使用一个输出端口，则输出为数据数组。如果为每个通道使用一个端口，则每次扫描在每个端口上产生单个值。多个端口按通道名称或设备指定的通道 ID 命名。

**数据类型：** `double`

### **Timestamp** — 扫描的时间戳

扫描的时间戳，以 double 形式返回。当您选中 Output timestamp 参数时，此端口可用。

**数据类型：** `double`

## 参数

使用“模块参数”对话框选择您的设备并设置其他配置选项。

### **Device** — 要从中采集数据的设备

要从中采集数据的设备。列表中的项因连接到系统的设备而异。列表中的设备由适配器或供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认情况下选择第一个可用设备。CompactDAQ 机箱将显示为单个设备，由供应商名称、机箱 ID 和机箱型号标识；例如 `ni cDAQ2 (cDAQ-9172)`。

### **Channels** — 设备通道选择和配置选项取决于设备

设备通道选择和配置表。通道配置表列出设备的硬件通道，并允许您选择和配置它们。指定要从中采集数据的通道（默认情况下所有通道均被选中）。为每个选中的通道指定以下参数：

**Channel ID** — 由设备指定的硬件通道 ID。Channel ID 列是只读的，参数在选定设备时定义。

**Name** — 通道名称。默认情况下，表格显示硬件提供的任何名称，但您可以编辑这些名称。例如，如果设备是带有两个通道的声卡，您可以将它们命名为 `Left` 和 `Right`。

**Module** — 通道所属的设备 ID。Module 列是只读的。如果选择了 CompactDAQ 机箱，则显示通道所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

**Measurement Type** — 通道的测量类型。此模块仅支持电压测量类型。（对于其他测量类型，请在 MATLAB® 中使用 DataAcquisition 对象。）

**Input Range** — 硬件支持的每个通道可用的输入范围，在选定设备时定义。

**Terminal Configuration** — 指定硬件端子配置，例如单端、差分等。端子配置选项由所选通道的功能定义。

**Coupling** — 硬件耦合配置，例如 AC 或 DC。耦合类型在选定设备时定义。

### **Number of ports** — 输出数据端口数 **1 for all channels** | **1 per channel**

输出数据端口数，指定为：

**1 for all channels** — 从单个端口输出采集的数据，为 1×N 向量，长度等于所选通道数。

**1 per channel** — 从 N 个端口输出采集的数据，其中 N 等于所选通道数。每个端口输出为 1×1 double。对于命名，每个输出端口使用通道名称（如果已指定），否则使用通道 ID，例如 `ai0`。

### **Sample time** — 模块执行速率 1（默认值）

指定仿真期间模块的采样时间。这是仿真期间模块执行的速率。默认值为 1（仿真秒）。有关详细信息，请参阅 Timing in Hardware Interface Models 和 What Is Sample Time? (Simulink)。

### **Output timestamp** — 添加时间戳输出端口

选择此选项以输出扫描的绝对时间戳。此选项为模块添加新的输出端口。此端口的数据类型为 double（datenum），对应于序列日期数字。您可以使用 `datetime` 函数将 datenum 转换为 datetime 值。

## 所属库

Data Acquisition Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从数据采集设备的多个模拟通道采集单个样本

Analog Input (Single Sample) 模块打开、初始化、配置和控制模拟数据采集设备。设备的打开、初始化和配置在模型执行开始时发生一次。该模块在模型运行期间每个时间步从设备同步采集单个样本。

该模块没有输入端口。它有一个或多个输出端口，具体取决于您在其对话框中选择的配置。

使用 Analog Input (Single Sample) 模块将实时测量数据纳入 Simulink®，用于：

- 系统表征
- 算法验证
- 系统和算法建模
- 模型和设计验证
- 控制器设计

模拟输入采集按以下图示同步完成。

同步模拟输入的时序

在第一个时间步（T1），从选定的硬件通道采集数据。在从所有通道读取数据之前，仿真不会继续。

**注意事项**

要使用此模块，您需要 Data Acquisition Toolbox™ 和 Simulink 软件。

某些设备不受 Data Acquisition Toolbox 中 Simulink 模块的支持。要查看您的设备是否支持 Simulink，请参阅 Supported Hardware。

您只能将 Analog Input (Single Sample) 模块与支持单样本采集的设备一起使用。如果设备不支持单样本采集，模型将生成错误。要从支持单样本采集的设备（例如为声音和振动设计的设备）采集数据，请使用 Analog Input 模块。

### 其他支持的功能

- 如果您有 DSP System Toolbox™，可以将此模块用于信号应用。
- 此模块支持使用文本加速模式，但不支持 Rapid Accelerator 或代码生成。
- 此模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
