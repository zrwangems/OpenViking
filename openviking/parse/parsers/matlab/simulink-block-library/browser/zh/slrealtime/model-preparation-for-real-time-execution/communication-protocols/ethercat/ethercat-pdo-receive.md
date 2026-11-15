---
type: simulink-block
title: 'EtherCAT PDO Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / EtherCAT'
documentation_page: 'ethercatpdoreceive'
documentation_source_path: 'io_ref/ethercatpdoreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT PDO Receive

## 端口

### 输出

### **D** — 从从站设备接收的数据 [double]

从 EtherCAT 从站设备接收的数据向量。

## 参数

### **网络设备索引** — EtherCAT 网络标识符 `0`（默认） | `0-15`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **设备索引** 值复制到该模块的 **设备索引** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **信号名称** — EtherCAT 设备变量名称字符向量

从列表中选择 EtherCAT 设备变量名称。

模块参数对话框会更新只读信号信息，以反映您选择的设备变量。

有关 EtherCAT 配置器组件到 Simulink® Real-Time™ 模块和模块属性的映射，请参阅 EtherCAT 配置器组件映射。

有关 Simulink 数据类型到 EtherCAT 数据类型的映射，请参阅 EtherCAT 数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_name` |

### **信号偏移量** — 信号数据在过程中的位置 只读：integer

此参数为只读。

执行 EtherCAT Init 模块后，数据可用的过程映像中的位置。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_offset` |

### **信号类型** — EtherCAT 数据的数据类型 只读：character vector

此参数为只读。

EtherCAT 数据的 Simulink 数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_type` |

### **类型大小 (bits)** — EtherCAT 数据类型的大小 只读：integer

此参数为只读。

EtherCAT 数据类型的大小，以 bits 为单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `type_size` |

### **信号维度** — 信号的维度 只读：integer

此参数为只读。

EtherCAT 模块支持向量和标量（维度为 `1` 的向量）。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_dim` |

### **采样时间** — 此模块的执行速率 只读：numeric

此参数为只读。

此速率是 ENI 文件中指定的 EtherCAT 任务执行速率。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020b 中引入**

## 描述

接收由过程数据对象表示的从站设备的数据

EtherCAT PDO Receive 模块从 EtherCAT® 从站设备接收数据。

模块参数对话框包含两个部分：参数和信号信息。
当您指定 EtherCAT 网络和设备变量名称时：

- EtherCAT PDO Receive 模块掩码会使用所选信号名称进行更新。
- 模块参数对话框中的信号信息会更新，以反映设备变量。

**注意**

如果软件在解析 EtherCAT Init 模块中指定的配置文件时发生错误，此模块将显示错误消息。
