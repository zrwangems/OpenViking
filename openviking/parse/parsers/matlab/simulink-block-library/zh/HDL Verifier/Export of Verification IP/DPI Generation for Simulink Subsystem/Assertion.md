---
type: simulink-block
title: 'Assertion'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'Export of Verification IP / DPI Generation for Simulink Subsystem'
documentation_page: 'assertion'
documentation_source_path: 'ref/assertion.html'
language: zh-CN
chinese_source: worker-translation
---

# Assertion

## 端口

### 输入

### **Port\_1** — 要检查非零值的信号 标量 | 向量 | 矩阵

Assertion 模块接受 Simulink 支持的任何维度和数值数据类型的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **启用断言** — 启用或禁用断言 on（默认）| off

选中此复选框可使模块显示仿真警告或错误。它还使模块能够在生成的代码中创建 SystemVerilog 断言。清除此复选框将在仿真中禁用断言，并且不会生成 SystemVerilog 断言。

### **断言失败时的仿真回调** — 断言失败时要计算的表达式 MATLAB 表达式

指定一个 MATLAB 表达式，供 Simulink 在断言失败时计算。该模块在生成的 DPI-C 断言中忽略此参数。

#### 依赖项

要启用此参数，请选择 **启用断言** 参数。

### **断言失败时停止仿真** — 断言失败时停止 Simulink 仿真 off（默认）| on

选中此复选框会导致 Simulink 在模块输入为零时停止仿真并显示错误。清除此复选框使 Simulink 在模块输入为零时继续仿真，并显示警告。该模块在生成的 DPI-C 断言中忽略此参数。

#### 依赖项

要启用此参数，请选择 **启用断言** 参数。

### DPI-C 断言选项

使用这些参数在 SystemVerilog 仿真环境中控制生成的 DPI-C 断言的行为。要启用 DPI-C 断言的生成，请选择 **启用断言**。

### **严重性** — 断言失败的严重性 `error`（默认）| `warning` | `custom`

选择 `error` 或 `warning`，使 DPI-C 断言发出 SystemVerilog 错误或警告消息。设置为 `custom` 以执行自定义命令。

#### 依赖项

要启用此参数，请选择 **启用断言** 参数。

### **断言失败消息** — 断言失败时的自定义消息 无默认值

指定当 SystemVerilog 断言失败时要发出的自定义 SystemVerilog 消息。此功能仅支持 ASCII 字符。

**示例：** `RX fail`

#### 依赖项

要启用此参数，请将 **严重性** 设置为 `error` 或 `warning`。

### **断言自定义命令** — 断言失败时要执行的自定义命令 SystemVerilog 命令

指定当断言失败时要执行的自定义 SystemVerilog 命令。您可以将此参数设置为显示语句、命令或脚本。此功能仅支持 ASCII 字符

**示例：** `$display("RX fail at %0t",
$time);`

#### 依赖项

要启用此参数，请将 **严重性** 设置为 `custom`。

## 所属库

HDL Verifier / For Use with DPI-C SystemVerilog

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

从 Simulink 断言生成 SystemVerilog 断言

Assertion 模块断言其输入信号为非零。如果其输入为零，模块默认停止仿真并显示错误消息。当您生成 DPI-C SystemVerilog 组件时，该模块会创建一个立即 SystemVerilog 断言。使用模块参数，您可以：

- 启用或禁用断言。
- 指定一个 MATLAB® 表达式，供 Simulink® 在断言失败时计算。
- 选择让 Simulink 在断言失败时停止仿真，或继续仿真但显示警告。

使用 DPI-C 参数控制运行时选项：

- 指定生成的断言的严重性。
- 指定断言失败时的自定义消息或操作。
