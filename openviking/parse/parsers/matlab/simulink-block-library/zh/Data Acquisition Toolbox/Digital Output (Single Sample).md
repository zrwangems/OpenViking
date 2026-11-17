---
type: simulink-block
title: 'Digital Output (Single Sample)'
family: 'daq'
product_id: 'daq'
product_name: 'Data Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'digitaloutputsinglesample'
documentation_source_path: 'digitaloutputsinglesample.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Output (Single Sample)

## 端口

### 输入

### **Data** — 生成的数字输出数据 boolean

生成的数字输出数据，指定为布尔值。如果所有线路仅使用一个输入端口，则提供 1×N 的数据向量。如果每条线路使用一个端口，则在每个端口上提供单个值。多个端口按线路名称或设备指定的线路 ID 命名。

**数据类型：** `Boolean`

## 参数

### **Device** — 用于生成数据的设备

要从中采集数据的设备。列表中的项因连接到系统的设备而异。列表中的设备由适配器或供应商名称和唯一设备 ID 指定，后跟设备的型号名称，例如 `ni Dev1 (USB-6255)`。默认选择第一个可用设备。CompactDAQ 机箱将显示为单个设备，由供应商名称、机箱 ID 和机箱型号标识；例如 `ni cDAQ2 (cDAQ-9172)`。

### **Lines** — 设备线路选择和配置选项取决于设备

**Line ID** — 硬件线路的 ID（例如 port0/line0）。这由所选设备自动检测并填充，且为只读。

**Name** — 硬件线路名称。这从硬件自动检测并填充，但您可以编辑该名称。

**Module** — 线路所属的设备 ID。Module 列为只读。如果选择了 CompactDAQ 机箱，则显示线路所属的 CompactDAQ 模块的 ID；否则显示设备的 ID。

### **Number of ports** — 输入数据端口数 **1 for all lines** | **1 per line**

输入数据端口数，指定为：

**1 for all lines** — 该模块对于表中选中的所有线路只有一个输入端口。生成的数据定义为 1×N 的布尔值行向量，其大小为线路数。

**1 per line** — 该模块为每条选中的线路提供一个输入端口。每个输入端口的名称是表中为每条线路指定的名称。如果未提供名称，则名称为 Line ID。例如，如果选中硬件端口 3 的线路 2，且未在线路表中指定名称，则模块中显示 `port3/line2`。每条线路的数据大小为 1×1。

### **Sample time** — 模块执行速率 1（默认值）

指定模块在仿真期间的采样时间。这是模块在仿真期间执行的速率。默认值为 1（仿真秒）。有关详细信息，请参阅 Timing in Hardware Interface Models 和 What Is Sample Time? (Simulink)。

## 所属库

Data Acquisition Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将单个样本输出到数据采集设备的多个数字线路

Digital Output (Single Sample) 模块在每个仿真时间步同步将最新一组数据输出到硬件。它输出无缓冲的数字数据。将输出数据指定为布尔值向量。

该模块没有输出端口。它可以有一个或多个输入端口，具体取决于在其对话框中选定的选项。输入端口处信号的数据类型必须为布尔数据类型。

Digital Output (Single Sample) 模块从连接到输入端口的驱动模块继承采样时间。数字输出按以下图示同步完成。

同步数字输出的时序

在第一个时间步 (T1)，数据输出到选定的硬件线路。在数据输出到所有线路之前，仿真不会继续。

**注意**

要使用此模块，您需要 Data Acquisition Toolbox™ 和 Simulink® 软件。

某些设备不受 Data Acquisition Toolbox 中 Simulink 模块的支持。要查看您的设备是否支持 Simulink，请参阅 Supported Hardware。

### 其他支持的功能

- 此模块支持使用文本加速模式，但不支持 Rapid Accelerator 或代码生成。
- 此模块支持使用模型引用，因此您的模型可以将其他 Simulink 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
