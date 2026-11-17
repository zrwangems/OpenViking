---
type: simulink-block
title: 'Write DDS Sample'
family: 'dds-blockset'
product_id: 'dds'
product_name: 'DDS Blockset'
documentation_release: R2025b
official_category: 'DDS Blockset'
documentation_page: 'writeddssample'
documentation_source_path: 'ref/writeddssample.html'
language: zh-CN
chinese_source: worker-translation
---

# Write DDS Sample

## 端口

### 输入

### **Port\_Enable** — 外部使能信号标量

使该模块能够将样本发送到 DDS 网络中。对于大于 0 的输入值，发送处于启用状态。对于小于或等于 0 的输入值，发送处于禁用状态。

#### 依赖关系

要显示此端口，请选中标记为 **显示使能端口** 的复选框。

**数据类型：** `double`

### **Port\_1** — 输入信号标量 | 向量 | 矩阵

Simulink 环境中的信号。信号会转换为应用程序用来将数据发送到 DDS 网络中的样本。转换会保留原始信号的值和数据类型。

**数据类型：** `bus`

### 输出

### **Port\_1** — 输出 DDS 样本标量 | 向量 | 矩阵

将样本发送到 DDS 网络中。

**数据类型：** `bus`

## 参数

### **显示使能端口** — 显示使能端口 `off`（默认）| `on`

选择此参数以显示使能端口。

#### 编程使用

|  |
| --- |
| **模块参数：** `ShowEnablePort` |
| **类型：** character vector |
| **值：** `'on' | 'off'` |
| **默认值：** `'off'` |

### **连接到实时网络** — 将 DDS 仿真连接到实时网络 `off`（默认）| `on`

*自 R2025a 起*

选择此参数以在仿真期间连接到实时 DDS 网络。选中 **连接到实时网络** 时：

- 模块图像会发生变化。

  启用连接到实时网络的 Write DDS Sample 模块。
- 在仿真期间，模块基于模型设置连接到实时 DDS 网络，并从定义的主题写入 DDS 消息。

#### 编程使用

|  |
| --- |
| **模块参数：** `ConnectToLive` |
| **类型：** character vector |
| **值：** `'on' | 'off'` |
| **默认值：** `'off'` |

## 所属库

DDS Blockset

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

DDS 模块的代码生成需要 Embedded Coder 许可证。

## 版本历史

**在 R2021a 中引入**

### R2025a：添加了在仿真期间连接到 DDS 网络的支持

您可以配置 DDS 应用程序模型，以在仿真期间直接向实时 DDS 网络订阅和发布主题。选择模块参数 **连接到实时网络** 以启用仿真与 DDS 网络之间的通信。

## 描述

将数据样本发送到 DDS 网络

DDS Blockset 库提供 Take DDS Sample 和 Write DDS Sample 模块，以帮助对 DDS 应用程序建模。Take DDS Sample 模块从 DDS 网络接收样本，并将其转换为可在 Simulink® 环境中使用的信号。Write DDS Sample 模块将 Simulink 环境中的信号转换为样本，以将数据发送到 DDS 网络中。这些模块已预配置为与 DDS 网络兼容，并提供类型检查功能。

DDS Blockset 的代码生成需要 Embedded Coder® 许可证。
