---
type: simulink-block
title: 'Invoke AUTOSAR Server Operation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Communication'
documentation_page: 'invokeautosarserveroperation'
documentation_source_path: 'ref/invokeautosarserveroperation.html'
language: zh-CN
chinese_source: worker-translation
---

# Invoke AUTOSAR Server Operation

## 端口

### 输入

### **Input argument** — 输入参数的输入信号 标量 | 向量 | 矩阵

发送到模块的输入参数的输入信号。

**Operation prototype** 参数决定模块上出现的输入端口数量和名称。将信号线连接到输入端口。
### 输出

### **Output argument** — 输出参数的输出信号 标量 | 向量 | 矩阵

函数返回的输出参数的输出信号。

**Operation prototype** 参数决定模块上出现的输出端口数量和名称。将信号线连接到输出端口。

## 参数

### **Client port name** — AUTOSAR 客户端端口短名称 character vector

为客户端端口指定有效的 AUTOSAR 短名称标识符。

### **Operation prototype** — 控制模块的输入端口和输出端口的类型和数量 character vector

按以下格式指定操作原型：

`operation(prt1
datatype1
arg1, prt2
datatype2
arg2, ... prtN
datatypeN
argN, ...)`

- *`operation`* — 操作的名称
- *`prtN`*。`IN` 或 `OUT`，指示数据是传入还是传出函数。
- *`datatypeN`* — 指示数据类型的文本，可以是 AUTOSAR 基本数据类型或记录、Simulink 数据类型或数组。
- *`argN`* — 参数的名称

### **Interface path** — 客户端-服务器接口 XML 文件的路径 character vector

指定您提供的客户端-服务器接口 XML 文件的引用路径。

### **Server type** — 服务器类型值 `Application software`（默认）| `Basic software`

选择服务器类型：

- `Application software` — 用于与应用程序软件组件通信。
- `Basic software` — 用于与 AUTOSAR Basic Software 通信。

### **Show error status** — 客户端端口是否接收客户端-服务器通信的错误状态 `off` | `on`

如果选中此复选框，客户端端口将接收客户端-服务器通信的错误状态。

### **Sample time (-1 for inherited)** — 模块采样时间 -1（默认）| 标量

模块采样时间。默认设置使模块从模型继承其采样时间。

## 所属库

AUTOSAR Blockset

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

配置 AUTOSAR 客户端端口以访问 Basic Software 或应用程序软件组件

使用此模块为您的 Simulink® 模型配置 AUTOSAR 客户端端口，该端口提供对 Basic Software 或应用程序软件组件的访问。要配置此模块：

1. 将此模块从 AUTOSAR 库复制或拖动到您的模型中。
2. 双击该模块以打开 Invoke AUTOSAR Server Operation 对话框。
3. 指定参数并点击 **OK**。此操作会更新输入端口和输出端口的数量，以匹配操作原型。
4. 根据需要将此模块连接到模型中的其他模块。
5. 保存并构建模型，以生成符合 AUTOSAR 的代码和 XML 文件。

如果使用包含 Invoke AUTOSAR Server 模块的模型运行 SIL 仿真，软件会将该模块的返回参数设置为接地值。

Simulink 不支持指针数据类型。如果要将 `NULL` 指针作为输入参数传递给您的操作：

1. 将该参数的数据类型指定为 `uint8`。
2. 将数据类型为 `uint8` 且值为 0 的常量信号连接到该模块的对应输入端口。
3. 检查您的客户端-服务器接口 XML 文件是否将该参数指定为数据类型为 `uint8` 的数组。
