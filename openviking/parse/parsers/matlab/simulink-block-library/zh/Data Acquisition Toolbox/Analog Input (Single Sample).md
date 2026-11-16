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

### **Data** — 获取的模拟输入 double

获取的模拟输入数据，以 doubles 形式返回。如果对所有通道仅使用一个输出端口，则输出为数据数组。如果为每个通道使用一个端口，则每次扫描都会在每个端口上产生单个值。多个端口按通道名称或设备指定的通道 ID 命名。

**数据类型：** `double`

### **Timestamp** — 扫描的时间戳

扫描的时间戳，以 double 形式返回。当你勾选 Output timestamp 参数时，此端口可用。

**数据类型：** `double`

## 参数

使用“模块参数”对话框选择设备并设置其他配置选项。

### **Device** — 要从中获取数据的设备

要从中获取数据的设备。列表中的项取决于已连接到系统的设备。列表中的设备由适配器或供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认情况下选择第一个可用设备。CompactDAQ 机箱将显示为单个设备，由供应商名称、机箱 ID 和机箱型号标识；例如 `ni cDAQ2 (cDAQ-9172)`。

### **Channels** — 设备通道选择和配置选项取决于设备

设备通道选择和配置表。通道配置表列出设备的硬件通道，并允许你选择和配置它们。指定要从哪些通道获取数据（默认情况下所有通道都被选中）。为每个选中的通道指定以下参数：

**Channel ID** — 设备指定的硬件通道 ID。Channel ID 列是只读的，并且这些参数在选中设备时定义。

**Name** — 通道名称。默认情况下，表中显示硬件提供的任何名称，但你可以编辑这些名称。例如，如果设备是具有两个通道的声卡，你可以将它们命名为 `Left` 和 `Right`。

**Module** — 通道所属的设备 ID。Module 列是只读的。如果选择了 CompactDAQ 机箱，它会显示通道所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

**Measurement Type** — 通道的测量类型。此模块仅支持 voltage 测量类型。（对于其他测量类型，请在 MATLAB® 中使用 DataAcquisition 对象。）

**Input Range** — 硬件为每个通道支持的可用输入范围，在选中设备时定义。

**Terminal Configuration** — 指定硬件端子配置，例如 single-ended、differential 等。端子配置选项由所选通道的功能定义。

**Coupling** — 硬件耦合配置，例如 AC 或 DC。耦合类型在选中设备时定义。

### **Number of ports** — 输出数据端口数 **1 for all channels** | **1 per channel**

输出数据端口数，指定为：

**1 for all channels** — 从单个端口输出获取的数据，为 1-by-N 向量，其长度等于所选通道数。

**1 per channel** — 从 N 个端口输出获取的数据，其中 N 等于所选通道数。每个端口输出为 1-by-1 double。为便于命名，每个输出端口使用通道名称（如果已指定），否则使用通道 ID，例如 `ai0`。

### **Sample time** — 模块执行速率 1（默认）

指定模块在仿真期间的采样时间。这是模块在仿真期间执行的速率。默认值为 1（simulation seconds）。有关更多信息，请参阅硬件接口模型中的时序和什么是采样时间？(Simulink)。

### **Output timestamp** — 添加时间戳输出端口

选择此选项以输出扫描的绝对时间戳。此选项会向模块添加一个新的输出端口。此端口的数据类型为 double (datenum)，对应序列日期数字。你可以使用 `datetime` 函数将 datenum 转换为 datetime 值。

## 所属库

Data Acquisition Toolbox

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从数据采集设备的多个模拟通道获取单个采样

Analog Input (Single Sample) 模块打开、初始化、配置并控制模拟数据采集设备。设备的打开、初始化和配置在模型执行开始时发生一次。该模块在模型运行期间每个时间步从设备同步获取单个采样。

该模块没有输入端口。根据你在其对话框中选择的配置，它有一个或多个输出端口。

使用 Analog Input (Single Sample) 模块将实时测量数据并入 Simulink®，用于：

- 系统特性描述
- 算法验证
- 系统与算法建模
- 模型与设计验证
- 控制器设计

模拟输入采集根据下图同步完成。

同步模拟输入的时序

在第一个时间步 (T1)，从所选硬件通道获取数据。在从所有通道读取数据之前，仿真不会继续。

**说明**

要使用此模块，你需要同时具备 Data Acquisition Toolbox™ 和 Simulink 软件。

Data Acquisition Toolbox 中的 Simulink 模块不支持某些设备。要查看你的设备是否支持 Simulink，请参阅支持的硬件。

你只能对支持单采样采集的设备使用 Analog Input (Single Sample) 模块。如果设备不支持单采样采集，模型会生成错误。对于不支持单采样采集的设备（例如为声音和振动设计的设备），请使用 Analog Input 模块获取数据。

### 其他支持的功能

- 如果你有 DSP System Toolbox™，则可以将此模块用于信号应用。
- 此模块支持使用 text accelerator mode，但不支持 Rapid Accelerator 或代码生成。
- 该模块支持使用模型引用，因此你的模型可以将其他 Simulink 模型作为模块化组件包含进来。

有关这些功能的更多信息，请参阅 Simulink 文档。
