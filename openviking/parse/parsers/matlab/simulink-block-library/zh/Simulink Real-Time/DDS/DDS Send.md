---
type: simulink-block
title: 'DDS Send'
family: 'dds'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'DDS'
documentation_page: 'ddssend'
documentation_source_path: 'io_ref/ddssend.html'
language: zh-CN
chinese_source: worker-translation
---

# DDS Send

## 端口

### 输入

### **DDS Msg** — DDS 消息，Bus 类型的 Simulink 消息

输入要发送到目标的 DDS 消息。

**示例：** `message`

## 参数

### **Data Dictionary** — 关联一个数据字典 string | char

关联一个包含 DDS 数据定义的 Simulink 数据字典，或为模型创建新的数据字典。

#### 程序化使用

|  |
| --- |
| **模块参数：** `datadict` |

### **Topic** — 选择主题名称 string scalar | char vector

从下拉菜单中为数据选择主题。

#### 程序化使用

|  |
| --- |
| **模块参数：** `topic` |

### **Writer XML Path** — 数据写入器 XML 路径 string (default)

选择数据写入器 XML 路径。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xmlPath` |

### **Writer QoS** — 服务质量 string (default)

从下拉菜单中选择服务质量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `qos` |

### **Sample time** — 采样时间 -1（默认）| numeric

输入基本采样时间或基本采样时间的倍数。
`-1` 表示采样时间被继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampletime` |

## 所属库

Simulink Real-Time / DDS

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

发送 DDS 消息

DDS Receive 和 DDS Send 模块让 Simulink®
Real-Time™ 应用通过共享的 Simulink 数据字典与 Data Distribution Service (DDS) 中间件
应用通信。这些模块与 DDS Blockset 兼容，后者包含一个 DDS 字典，使您可以在 Simulink 中管理、创建和编辑 DDS
定义。您可以将 DDS 规范作为 XML 文件导入，以创建骨架 Simulink
模型，作为为 DDS 应用开发算法的起点。有关
详细信息，请参阅 How Does DDS Blockset Work? (DDS Blockset)。

DDS Send 模块为实时应用中的选定主题发送 DDS 消息。您可以将包含 DDS 数据
定义的 Simulink 数据字典附加到该模块。您可以为该模块创建新的数据字典或关联现有数据
字典，并从数据字典中选择主题、数据写入器路径和服务质量 (QoS)。

DDS Receive 模块和 DDS Send 模块有一些限制：

- 您可以在模型的顶层使用这些模块。这些模块不能在
  引用模型中使用。
- 您可以在实时应用中使用这些模块。这些模块不能用于
  正常模式、加速模式或快速加速模式下的仿真。
- 您不能在受保护模型中使用这些模块。
