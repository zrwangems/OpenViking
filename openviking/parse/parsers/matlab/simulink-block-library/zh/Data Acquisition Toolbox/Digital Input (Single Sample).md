---
type: simulink-block
title: 'Digital Input (Single Sample)'
family: 'data-acquisition-toolbox'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: 'Data Acquisition Toolbox'
documentation_page: 'digitalinputsinglesample'
documentation_source_path: 'digitalinputsinglesample.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input (Single Sample)

## 端口

### 输出

### **Data** — 采集的数字输入 boolean 值

采集的数字输入数据，以 booleans 形式返回。如果对所有线路仅使用一个输出端口，则输出为 N 个通道的 1-by-N 向量。如果为每条线路使用一个端口，则每次扫描都会在每个端口上产生单个 boolean。多个端口按线路名称或设备指定的线路 ID 命名。

**数据类型：** `Boolean`

### **Timestamp** — 扫描的时间戳 double

扫描的时间戳，以 double 形式返回。当您选中 Output timestamp 参数时，此端口可用。

**数据类型：** `double`

## 参数

### **Device** — 要从中采集数据的设备

要从中采集数据的设备。列表中的项因您系统所连接的设备而异。列表中的设备由适配器或供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认选择第一个可用设备。CompactDAQ 机箱会显示为单个设备，由供应商名称、机箱 ID 和机箱型号标识；例如 `ni cDAQ2 (cDAQ-9172)`。

### **Lines** — 设备线路选择和配置选项取决于设备

**Line ID** — 硬件线路的 ID（例如 port0/line0）。这由所选设备自动检测并填写，并且为只读。

**Name** — 硬件线路名称。这会从硬件自动检测并填写，不过您可以编辑该名称。

**Module** — 该线路所属的设备 ID。Module 列为只读。如果选择了 CompactDAQ 机箱，它会显示该线路所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

### **Number of ports** — 输出数据端口数 **1 for all lines** | **1 per line**

输出数据端口数，指定为：

**1 for all lines** — 该模块对于表中选中的所有线路只有一个输出端口。采集的数据以 boolean 值的 1-by-N 向量返回，其大小等于线路数。

**1 per line** — 该模块为每条选定线路提供一个输出端口。每个端口上的数据以 1-by-1 boolean 值返回。每个输出端口的名称是表中为每条线路指定的名称。如果未提供名称，则名称为 Line ID。例如，如果选择了硬件端口 3 的线路 2，并且您未在线路表中指定名称，则 `port3/line2` 会出现在该模块中。每条线路的数据大小为 1-by-1。

### **Sample time** — 模块执行速率 1（默认）

指定模块在仿真期间的采样时间。这是仿真期间执行模块的速率。默认值为 1（simulation seconds）。有关详细信息，请参阅硬件接口模型中的时序和什么是采样时间？(Simulink)。

### **Output timestamp** — 添加时间戳输出端口

选择此选项可输出扫描的绝对时间戳。此选项会向该模块添加一个新的输出端口。此端口的数据类型为 double (datenum)，对应串行日期数字。您可以使用 `datetime` 函数将 datenum 转换为 datetime 值。

## 所属库

Data Acquisition Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从数据采集设备的多个数字线路采集单个样本

Digital Input (Single Sample) 模块在每个仿真时间步同步输出从所选数字线路可获取的最新扫描数据。它采集无缓冲数字数据，并将其作为 boolean 值向量提供。

该模块没有输入端口。根据您在其对话框中选择的选项，它有一个或多个输出端口。

该模块继承模型的采样时间。数字输入采集按下图同步完成。

同步数字输入的时序

在第一个时间步 (T1)，从所选硬件线路采集数据。直到从所有线路读取数据后，仿真才会继续。

**注意**

要使用此模块，您需要同时拥有 Data Acquisition Toolbox™ 和 Simulink® 软件。

某些设备不受 Data Acquisition Toolbox 中的 Simulink 模块支持。要查看您的设备是否支持 Simulink，请参阅支持的硬件。

### 其他支持的功能

- 此模块支持使用 text accelerator mode，但不支持 Rapid Accelerator 或代码生成。
- 此模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
