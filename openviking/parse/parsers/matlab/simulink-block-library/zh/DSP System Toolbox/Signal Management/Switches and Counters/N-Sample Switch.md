---
type: simulink-block
title: 'N-Sample Switch'
family: 'signal-management'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Switches and Counters'
documentation_page: 'nsampleswitch'
documentation_source_path: 'ref/nsampleswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Sample Switch

## 端口

### 输入

### **Input 1** — 第一个输入信号 标量 | 向量 | 矩阵

将第一个输入信号指定为标量、向量或矩阵。

两个输入必须具有相同的维度，但以下两种情况除外：

- 当一个输入为标量时，模块会扩展该标量输入以匹配另一个输入的大小。
- 当一个输入是无定向向量，而另一个输入是具有相同元素数量的行向量或列向量时，模块会重塑该无定向向量以匹配另一个输入的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Input 2** — 第二个输入信号 标量 | 向量 | 矩阵

将第二个输入信号指定为标量、向量或矩阵。

两个输入必须具有相同的维度，但以下两种情况除外：

- 当一个输入为标量时，模块会扩展该标量输入以匹配另一个输入的大小。
- 当一个输入是无定向向量，而另一个输入是具有相同元素数量的行向量或列向量时，模块会重塑该无定向向量以匹配另一个输入的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Rst** — 复位信号 标量

将复位信号指定为标量。在计数期间的任何时刻，**Rst** 端口上的触发事件都会将计数器复位为零。复位采样时间必须是输入采样时间的正整数倍。

有关复位触发类型的详细信息，请参阅 **Trigger type** 参数的描述。

#### 依赖关系

要启用此端口，请选中 **Reset input** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **Output** — 开关的输出 标量 | 向量 | 矩阵

开关的输出，以标量、向量或矩阵形式返回。模块在经过指定数量的采样周期 *N* 后在两个输入之间切换。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

## 参数

### **Switch count, N** — 开关计数 `8`（默认）| 非负整数

将输出在切换到下方输入之前连接到上方输入的采样周期数 *N* 指定为非负整数。

**可调：** Yes

### **Reset input** — 重置输入 `off`（默认）| `on`

选中此复选框以启用 **Rst** 输入端口。复位信号的速率必须是数据信号输入速率的正整数倍。

选中 **Reset input** 复选框时，此模块支持触发子系统。

### **Trigger type** — 触发类型 `Rising edge`（默认）| `Falling edge` | `Either edge` | `Non-zero sample`

使用 **Rst** 端口上的事件类型复位模块的计数器。

您在 **Trigger type** 弹出菜单中指定触发事件，它可以是以下之一：

- `Rising edge` — 当 **Rst** 输入执行以下任一操作时触发复位操作：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续（见下图）
- `Falling edge` — 当 `Rst` 输入执行以下任一操作时触发复位操作：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续（见下图）
- `Either edge` — 当 `Rst` 输入为 `Rising edge` 或 `Falling edge`（如上所述）时触发复位操作。
- `Non-zero sample` — 在每个 `Rst` 输入非零的采样时间触发复位操作。

**可调：** Yes

#### 依赖关系

要启用此参数，请选中 **Reset input** 复选框。

### **Sample time** — 采样时间 `0.1`（默认）| 正标量

将模块计数器的采样周期 *Ts* 指定为正标量。模块在 *t* = *Ts*×(*N*+1) 时切换输入。

您在 **Sample time** 参数中指定输出的采样周期，也就是说，输出采样周期不会从任一输入的采样周期继承。

模块在输入端口应用零阶保持，因此模块在输入采样时间之间从给定端口读取的值是该端口最近一次输入的值。

## 所属库

DSP System Toolbox / Signal Management / Switches and Counters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

在指定数量的采样周期后，在两个输入之间切换

N-Sample Switch 模块在仿真开始或模块复位后的前 *N* 个采样时间输出连接到上方输入端口的信号，其中您在 **Switch count** 参数中指定 *N*。从输出采样 *N*+1 开始，模块输出连接到下方输入的信号，直到下一次复位事件或仿真结束。
