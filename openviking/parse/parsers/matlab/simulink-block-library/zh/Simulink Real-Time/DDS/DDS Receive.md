---
type: simulink-block
title: 'DDS Receive'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'DDS'
documentation_page: 'ddsreceive'
documentation_source_path: 'io_ref/ddsreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# DDS Receive

## 端口

### 输出

### **DDS Msg** — Bus 类型的 DDS 消息 Simulink 消息

返回所发送的 DDS 消息。

## 参数

### **Data Dictionary** — 关联数据字典 string | char

关联包含 dds 数据定义的 Simulink 数据字典，或为模型创建新的数据字典。

#### 程序化使用

|  |
| --- |
| **模块参数：** `datadict` |

### **Topic** — 选择主题名称 string scalar | char vector

从下拉菜单中选择数据的主题。

#### 程序化使用

|  |
| --- |
| **模块参数：** `topic` |

### **Reader XML Path** — 数据写入器 XML 路径 string (default)

选择数据写入器 XML 路径。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xmlPath` |

### **Reader QoS** — 服务质量 string (default)

从下拉菜单中选择服务质量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `qos` |

### **Sample time** — 采样时间 -1 (default) | numeric

输入基本采样时间或基本采样时间的倍数。
`-1` 表示采样时间继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampletime` |

## 所属库

Simulink Real-Time / DDS

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

接收 DDS 消息

DDS Receive 模块在 Simulink®
Real-Time™ 模型中接收所选主题的 DDS 消息。该模块允许您将包含
DDS 数据定义的 Simulink 数据字典附加到模型。

DDS Receive 和 DDS Send 模块让 Simulink
Real-Time 应用程序能够通过共享的 Simulink 数据字典与数据分发服务 (DDS) 中间件
应用程序通信。这些模块与
DDS Blockset 兼容，后者包含一个 DDS 字典，可让您在 Simulink 中管理、创建和编辑 DDS
定义。您可以将 DDS 规范作为 XML 文件导入，以创建骨架 Simulink
模型，作为开发 DDS 应用程序算法的起点。有关更多
信息，请参阅 How Does DDS Blockset Work? (DDS Blockset)。

DDS Receive 模块在
实时应用程序中接收所选主题的 DDS 消息。您将包含 DDS 数据
定义的 Simulink 数据字典附加到该模块。您可以创建新的数据字典或将现有数据
字典关联到该模块，并从数据字典中选择主题、数据写入器路径和服务质量 (QoS)。

DDS Receive 模块和 DDS Send 模块有一些限制：

- 您可以在模型的顶层使用这些模块。这些模块不能用于
  被引用的模型。
- 您可以在实时应用程序中使用这些模块。这些模块不能用于
  正常模式、加速模式或快速加速模式下的仿真。
- 您不能在受保护的模型中使用这些模块。
