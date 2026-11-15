---
type: simulink-block
title: 'Find Delay'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Signal Operations'
documentation_page: 'finddelay'
documentation_source_path: 'ref/finddelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Find Delay

## 端口

### 输入

### **sRef** — 参考信号 向量 | 矩阵

原始参考信号，指定为向量或矩阵。**sRef** 和 **sDel** 的维度和采样时间必须匹配。

**数据类型：** `double`

### **sDel** — 延迟信号 向量 | 矩阵

参考信号的延迟或失真版本，指定为向量或矩阵。**sRef** 和 **sDel** 的维度和采样时间必须匹配。

**数据类型：** `double`
### 输出

### **delay** — 延迟输出 标量 | 向量

延迟输出，以标量或向量形式返回，指示 **sRef** 和 **sDel** 输入之间的延迟信号采样数。

对于矩阵输入，输出为行向量，并独立地查找输入矩阵每个通道中的延迟

延迟输出是一个小于 **Correlation window length (samples)** 参数值的非负整数。

**数据类型：** `double`

### **chg** — 延迟标志 `0` | `1`

延迟标志，以 `0` 或 `1` 返回。当与上一采样点计算出的延迟相比发生变化时，**chg** 端口输出 `1`；没有变化时输出 `0`。

#### 依赖关系

要启用此端口，请选中 **Include "change signal" output port** 参数。

**数据类型：** `Boolean`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，从 **Prepare** 库中选择 **Property Inspector**。

### **Correlation window length (samples)** — 采样数 `200`（默认）| 正整数

模块用于计算两个信号的互相关所用的采样数。增大相关窗口长度会提高所计算延迟的可靠性，但也会增加计算延迟的处理时间。

### **Include "change signal" output port** — 向模块添加 chg 端口 `off`（默认）| `on`

选中此参数可添加 **chg** 输出端口。当与上一采样点计算出的延迟相比发生变化时，**chg** 端口输出 `1`；没有变化时输出 `0`。

### **Disable recurring updates** — 选择以设置延迟计算的停止条件 `off`（默认）| `on`

选择以设置延迟计算的停止条件。选中后，当同一延迟值被计算的次数达到 **Number of constant delay outputs to disable updates** 参数指定的次数时，模块将停止更新延迟。

### **Number of constant delay outputs to disable updates** — 在计算出不变延迟值达到此次数后禁用更新 `3`（默认）| 正整数

在计算出不变延迟值达到此次数后禁用更新，指定为正整数。此参数的值指示模块在停止更新之前必须计算出同一延迟的次数。

#### 依赖关系

要启用此参数，请选中 **Disable recurring updates** 参数。

## 所属库

Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `enumerated` | `integera` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
|  |  |
| --- | --- |
| a 仅限有符号整数。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

查找两个信号之间的延迟

Find Delay 模块查找信号与其自身延迟且可能失真的版本之间的延迟。当您想要比较发送信号和接收信号以求出误码率，但不知道接收信号中的延迟时，此功能很有用。此模块接受列向量或矩阵输入信号。对于矩阵输入，模块输出行向量，并独立地查找矩阵每个通道中的延迟。有关信号延迟的详细信息，请参阅 Delays in Communication Systems。

此图标显示带有可选 **chg** 端口的模块。Find Delay 模块显示可选的 'chg' 端口。
