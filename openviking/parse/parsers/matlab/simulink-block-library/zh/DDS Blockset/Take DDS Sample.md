---
type: simulink-block
title: 'Take DDS Sample'
family: 'dds'
product_id: 'dds'
product_name: 'DDS Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'takeddssample'
documentation_source_path: 'ref/takeddssample.html'
language: zh-CN
chinese_source: worker-translation
---

# Take DDS Sample

## 端口

### 输入

### **Port\_1** — 输入 DDS 样本 标量 | 向量 | 矩阵

从 DDS 网络接收样本。样本会转换为可在 Simulink 环境中使用的信号。转换会保留原始 DDS 样本的值和数据类型。

**数据类型：** `bus`
### 输出

### **Port\_S** — 显示是否接收到 DDS 样本 标量

显示是否成功从 DDS 网络接收到样本。如果成功接收到样本，模块输出 1，否则输出 0。

#### 依赖关系

要启用此端口，请选中标记为 **显示接收状态** 的复选框。

**数据类型：** `double`

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

可在 Simulink 环境中使用的转换后信号。

**数据类型：** `bus`

## 参数

### **显示接收状态** — 显示是否接收到 DDS 样本 `off`（默认） | `on`

选择此参数可显示是否从 DDS 网络接收到样本。如果成功接收到样本，模块输出 1，否则输出 0。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowQueueStatus` |
| **类型：** character vector |
| **值：** `'on' | 'off'` |
| **默认值：** `'off'` |

### **连接到实时网络** — 将 DDS 仿真连接到实时网络 `off`（默认） | `on`

*自 R2025a 起*

选择此参数可在仿真期间连接到实时 DDS 网络。选中 **连接到实时网络** 时：

- 模块图像会更改。

  已启用连接到实时网络的 Take DDS Sample 模块。
- 在仿真期间，模块基于模型设置连接到实时 DDS 网络，从已定义主题读取 DDS 消息，并提供订阅者样本数据，以供在 Simulink 模型算法中处理。

#### 编程用法

|  |
| --- |
| **模块参数：** `ConnectToLive` |
| **类型：** character vector |
| **值：** `'on' | 'off'` |
| **默认值：** `'off'` |

## 所属库

DDS Blockset

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

DDS 模块的代码生成需要 Embedded Coder 许可证。

## 版本历史

**在 R2021a 中引入**

### R2025a: 添加了对在仿真期间连接到 DDS 网络的支持

您可以将 DDS 应用程序模型配置为在仿真期间直接向实时 DDS 网络订阅和发布主题。选择模块参数 **连接到实时网络** 以启用仿真与 DDS 网络之间的通信。

## 描述

从 DDS 网络接收数据样本

DDS Blockset 提供 Take DDS Sample 和 Write DDS Sample 模块，以帮助对 DDS 应用程序建模。Take DDS Sample 模块从 DDS 网络接收样本，并将其转换为可在 Simulink® 环境中使用的信号。Write DDS Sample 模块从 Simulink 环境获取信号，并将其转换为样本，以将数据发送到 DDS 网络中。这些模块已预配置为与 DDS 网络兼容，并提供类型检查功能。

DDS Blockset 的代码生成需要 Embedded Coder® 许可证。
