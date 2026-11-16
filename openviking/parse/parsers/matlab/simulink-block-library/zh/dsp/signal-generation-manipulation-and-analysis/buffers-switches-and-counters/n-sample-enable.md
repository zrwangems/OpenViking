---
type: simulink-block
title: 'N-Sample Enable'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'nsampleenable'
documentation_source_path: 'ref/nsampleenable.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Sample Enable

## 端口

### 输入

### **Rst** — 复位信号标量

复位输入信号，指定为标量。在计数期间的任何时刻，输入端口上的触发事件会将计数器复位到其初始状态。

**提示**

当您选中 **Reset input** 复选框以启用 **Rst** 输入端口时，N-Sample Enable 模块支持触发子系统。

#### 依赖关系

要启用此输入端口，请选中 **Reset input** 复选框。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 输出信号标量

标量输出，在前 *N* 个采样时间内包含非激活值（`0` 或 `1`，即在 **Active level** 参数中未选择的值），其中 *N* 为 **Trigger count** 值。从输出采样 *N*+1 开始，模块输出激活值（`1` 或 `0`，即您在 **Active level** 参数中选择的值），直到发生复位事件或仿真终止。

**数据类型：** `Boolean`

## 参数

### **Trigger count, N** — 输出激活值的采样数 `8`（默认） | 标量整数

将模块输出激活值的采样数指定为大于或等于零的标量整数。

**可调：** 是

### **Active level** — 激活电平 `Low (0)`（默认） | `High (1)`

将前 *N* 个采样时间之后要输出的值指定为 `0` 或 `1`。

**可调：** 是

### **Reset input** — 启用复位输入端口 `off`（默认） | `on`

要启用复位（**Rst**）输入端口，请选中此复选框。清除此复选框时，**Rst** 输入端口被禁用。

**提示**

当您选中 **Reset input** 复选框时，N-Sample Enable 模块支持触发子系统。

### **Trigger type** — 触发事件类型 `Rising edge`（默认） | `Falling edge` | `Either edge` | `Non-zero sample`

当 **Rst** 端口启用时，选择触发复位的事件类型。

您可以将触发事件指定为：

- `Rising edge` — 当 `Rst` 输入执行以下操作之一时触发复位操作：

  - 从负值上升到正值或零
  - 从零上升到正值，且该上升不是从负值上升到零的延续（见下图）
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发复位操作：

  - 从正值下降到负值或零
  - 从零下降到负值，且该下降不是从正值下降到零的延续（见下图）
- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位操作。
- `Non-zero sample` — 在每个采样时间，当 **Rst** 输入不为零时触发复位操作。

#### 依赖关系

要启用此参数，请选中 **Reset input** 复选框。

### **Sample time** — 输出采样周期 `1`（默认） | 正标量

将模块计数器的采样周期 Ts 指定为正有限标量。模块在 *t*`=`Ts(*N*+1) 处从激活值切换到非激活值。

### **Output data type** — 输出数据类型 `Logical`（默认） | `Boolean`

将输出数据类型指定为 `Logical` 或 `Boolean`。

## 所属库

DSP System Toolbox / Sources DSP System Toolbox / Signal Management / Switches and Counters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

在指定数量的采样时间内输出 1 或 0

N-Sample Enable 模块在前 *N* 个采样时间内输出非激活值（`0` 或 `1`，即在 **Active level** 参数中未选择的值），其中 *N* 为 **Trigger count** 值。从输出采样 *N*+1 开始，模块输出激活值（`1` 或 `0`，即您在 **Active level** 参数中选择的值），直到发生复位事件或仿真终止。

该模块的输出始终为标量。

**Reset input** 复选框启用 **Rst** 输入端口。在计数期间的任何时刻，输入端口上的触发事件会将计数器复位到其初始状态。您可以使用 **Trigger type** 参数指定触发事件的类型。当您选中 **Reset input** 复选框时，此模块支持触发子系统。
