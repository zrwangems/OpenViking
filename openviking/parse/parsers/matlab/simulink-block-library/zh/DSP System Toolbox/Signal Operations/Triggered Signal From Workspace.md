---
type: simulink-block
title: 'Triggered Signal From Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'triggeredsignalfromworkspace'
documentation_source_path: 'ref/triggeredsignalfromworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Triggered Signal From Workspace

## 端口

### 输入

### **trigger** — 触发信号 标量 | 向量 | 矩阵

触发输入信号，指定为标量、向量或矩阵。
此端口标记为 。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 从工作区导入的信号 标量 | 向量 | 矩阵 | 三维数组

当由输入端口处的控制信号触发时，该模块输出从工作区导入的信号。

当 **Signal** 参数指定一个
*M*×*N* 矩阵
（*M*≠1）时，*N* 列中的每一列
被视为一个独立的通道。您在
**Samples per frame** 参数中指定帧大小，
*M*o。当触发时，
该模块输出一个
*M*o×*N*
矩阵，包含来自每个信号通道的 *M*o
个连续采样。为方便起见，导入的行向量（*M*=1）被视为单个
通道，因此输出维度为
*M*o×1。

当 **Signal** 参数指定一个
*M*×*N*×*P*
数组时，该模块在每个触发
时刻生成数组的单个页（一个
*M*×*N* 矩阵）。**Samples per frame** 参数必须设置
为 `1`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **Signal** — 要导入的信号 `1:10`（默认）| MATLAB 工作区变量 | MATLAB 表达式

要从中导入信号的 MATLAB 工作区变量名称，或指定信号的有效
MATLAB 表达式。

当 **Signal** 参数指定一个
*M*×*N* 矩阵
（*M*≠1）时，*N* 列中的每一列
被视为一个独立的通道。您在
**Samples per frame** 参数中指定帧大小，
*M*o。当触发时，该模块
输出一个
*M*o×*N*
矩阵，包含来自每个信号通道的 *M*o 个连续
采样。为方便起见，导入的行向量
（*M*=1）被视为单个通道，因此输出
维度为 *M*o×1。

当 **Signal** 参数指定一个
*M*×*N*×*P*
数组时，该模块在每个触发
时刻生成数组的单个页（一个
*M*×*N* 矩阵）。**Samples per frame** 参数必须设置
为 `1`。

### **Trigger type** — 触发事件的类型 `Rising edge`（默认）| `Falling edge` | `Either edge`

触发模块执行的事件类型。

- `Rising edge` 在触发输入从负值上升到零或
  正值，或从零上升到正值时触发
  模块执行。
- `Falling edge` 在触发输入从正值下降到零或
  负值，或从零下降到负值时触发
  模块执行。
- `Either edge` 在上升沿或下降沿
  发生时触发模块执行。

### **Initial output** — 初始输出值 `0`（默认）| 标量 | 向量 | 矩阵

在收到第一个触发事件之前要输出的值。在
触发事件之间，该模块将输出值保持恒定在其最近
的值（即不进行线性插值）。对于单通道
信号，**Initial output** 可以是长度为
*M*o 的向量，或一个标量以在
初始输出帧的 *M*o 个元素中重复。对于矩阵输出
（*M*o×*N* 或
*M*×*N*），**Initial
output** 参数值可以是相同大小的矩阵，或一个
标量以在初始输出的所有元素中重复。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

要缓冲到每个输出帧中的采样数 *M*o，
指定为正整数标量。当您在
**Signal** 参数中指定三维数组时，此值必须为 `1`。

### **Form output after final data value by** — 最终导入信号值之后的输出值 `Setting to zero`（默认）| `Holding final value` | `Cyclic repetition`

指定在所有指定信号采样已生成之后的输出。

- 当您指定 `Setting To Zero` 时，该
  模块在生成信号的最后一帧后，在仿真期间
  生成零值输出。
- 当您指定 `Holding Final Value` 时，
  该模块在生成信号的最后一帧后，在仿真期间
  重复最终采样。
- 当您指定 `Cyclic Repetition` 时，该
  模块在生成最后一帧后从头开始重复信号。当
  信号末尾没有足够的采样来填充最终帧时，该模块
  根据需要零填充最终帧，以确保每个周期的输出
  相同。例如，一个周期的第 *i* 帧
  包含与任何其他周期的第 *i* 帧相同的采样。

该模块不会将导入信号外推到最后一个
采样之外。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

当触发时从 MATLAB 工作区导入信号采样

Triggered Signal From Workspace 模块在由输入端口处的控制信号触发时，将信号采样从
MATLAB® 工作区导入到 Simulink® 模型中（）。**Signal** 参数指定包含要导入的信号的
MATLAB 工作区变量名称，或定义矩阵或三维数组的任何有效
MATLAB 表达式。
