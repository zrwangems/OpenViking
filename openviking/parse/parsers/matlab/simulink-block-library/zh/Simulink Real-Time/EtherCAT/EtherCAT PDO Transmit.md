---
type: simulink-block
title: 'EtherCAT PDO Transmit'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatpdotransmit'
documentation_source_path: 'io_ref/ethercatpdotransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT PDO Transmit

## 端口
```yaml
ports:
- name: D
  summary: 要传输到从站设备的数据 [double]
  direction: input
```

### 输入

### **D** — 要传输到从站设备的数据 [double]

要传输到 EtherCAT 从站设备的数据向量。
## 参数
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT 网络标识符 0（默认）| 0-15
  group: ''
  block_parameter: device_id
- name: Signal name
  summary: EtherCAT 设备变量名称 字符向量
  group: ''
  block_parameter: sig_name
- name: Signal Offset
  summary: 信号数据在过程中的位置 只读：整数
  group: ''
  block_parameter: sig_offset
- name: Signal Type
  summary: EtherCAT 数据的数据类型 只读：字符向量
  group: ''
  block_parameter: sig_type
- name: Type Size (bits)
  summary: EtherCAT 数据类型的大小 只读：整数
  group: ''
  block_parameter: type_size
- name: Signal Dimension
  summary: 信号的维度 只读：整数
  group: ''
  block_parameter: sig_dim
- name: Sample Time
  summary: 此模块执行的速率 只读：数值
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT 网络标识符 `0`（默认）| `0-15`

要将模块与某个 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Device index** 值复制到该模块的 **Device index** 中。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **Signal name** — EtherCAT 设备变量名称 字符向量

从列表中选择 EtherCAT 设备变量名称。

模块参数对话框会更新只读信号信息，以反映您所选择的设备变量。

有关 EtherCAT 配置器组件到 Simulink® Real-Time™ 模块及模块属性的映射，请参阅 EtherCAT Configurator Component Mapping。

有关 Simulink 数据类型到 EtherCAT 数据类型的映射，请参阅 EtherCAT Data Types。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_name` |

### **Signal Offset** — 信号数据在过程中的位置 只读：整数

此参数为只读。

在执行 EtherCAT Init 模块之后，数据在过程映像中可用的位置。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_offset` |

### **Signal Type** — EtherCAT 数据的数据类型 只读：字符向量

此参数为只读。

EtherCAT 数据的 Simulink 数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_type` |

### **Type Size (bits)** — EtherCAT 数据类型的大小 只读：整数

此参数为只读。

EtherCAT 数据类型的大小（以位为单位）。

#### 编程使用

|  |
| --- |
| **模块参数**：`type_size` |

### **Signal Dimension** — 信号的维度 只读：整数

此参数为只读。

EtherCAT 模块支持向量和标量（维度为 `1` 的向量）。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_dim` |

### **Sample Time** — 此模块执行的速率 只读：数值

此参数为只读。

此速率是 EtherCAT 任务的执行速率，如 ENI 文件中所指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

向由过程数据对象表示的从站设备发送数据

EtherCAT PDO Transmit 模块将计算得到的数据传输到 EtherCAT® 从站设备中的特定变量。

模块参数对话框包含两个部分：参数和信号信息。当您指定 EtherCAT 网络和设备变量名称时：

- EtherCAT PDO Receive 模块掩码会更新为所选的信号名称。
- 模块参数对话框中的信号信息会更新，以反映该设备变量。

**注意**

如果软件在解析 EtherCAT Init 模块中指定的配置文件时发生错误，此模块将显示错误消息。
