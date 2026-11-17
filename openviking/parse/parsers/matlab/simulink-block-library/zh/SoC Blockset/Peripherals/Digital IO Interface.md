---
type: simulink-block
title: 'Digital IO Interface'
family: 'peripherals'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'digitaliointerface'
documentation_source_path: 'ref/digitaliointerface.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital IO Interface

## 端口

### 输入

### **msg** — SoC 消息数据标量

此端口从连接的 IO Data Source 模块的 **msg** 端口接收逻辑信号。

#### 依赖关系

要启用此端口，请将 **IO direction** 参数设置为 `Output`。

**数据类型：** `SoCData`

### **in** — 输入数字信号标量

此端口指定要转换为数字逻辑测量的输入数字电压信号。

#### 依赖关系

要启用此端口，请将 **IO direction** 参数设置为 `Input`。

**数据类型：** `single` | `double`

### 输出

### **out** — 输出数字信号标量

此端口输出从 **msg** 输入端口提供的逻辑信号值。

#### 依赖关系

要启用此端口，请将 **IO direction** 参数设置为 `Output`。

**数据类型：** `single` | `double`

### **event** — 任务事件信号标量

此端口在每次数字 IO 阈值事件时发送消息。此输出连接到 Task Manager 模块的输入，以在执行 IO 事件后执行关联的事件驱动任务。

#### 依赖关系

要启用此端口，请将 **IO direction** 参数设置为 `Input`，并选择 **Enable event** 参数。

**数据类型：** `rteEvent`

### **message** — SoC 消息数据标量

此端口将 Digital IO Interface 输入信号数据作为消息发送到 IO Data Sink 模块的 **msg** 输入端口。

#### 依赖关系

要启用此端口，请将 **IO direction** 参数设置为 `Input`。

**数据类型：** `SoCData`

## 参数

### **IO direction** — 将模块配置为数字输入或输出 `Input`（默认）| `Output`

为 Digital IO Interface 模块选择一个值，使其充当数字输入或数字输出。

### **Low input voltage** — 低输入电压阈值 `0.2`（默认）| nonnegative scalar

指定输入信号的下阈值电压。当信号值向下穿越阈值时，模块会将此穿越记录为输入变化，生成一个事件以及数字值为 `0` 的新消息。

**示例：**
`0.3`

### **High input voltage** — 高输入电压阈值 `2.5`（默认）| nonnegative scalar

指定输入信号的上阈值电压。当信号值向上穿越阈值时，模块会将此穿越记录为输入变化，生成一个事件以及数字值为 `1` 的新消息。

**示例：**
`0.3`

### **Enable event** — 启用事件生成的选项 `on`（默认）| `off`

选择此参数可使 Digital IO Interface 模块在数字跳变事件之后生成事件。选择此参数还会启用 **event** 输出端口，您可以将其连接到 Task Manager 以模拟异步数字读取操作。

### **Condition** — 何时触发事件的条件 `Rising edge`（默认）| `Falling edge` | `Both`

选择何时生成数字输入事件的条件。

- `Rising edge` — 当 **in** 输入端口上的输入信号大于 **High input voltage** 参数值时，生成事件。
- `Falling edge` — 当 **in** 输入端口上的输入信号小于 **Low input voltage** 参数值时，生成事件。
- `Both` — 在 `Rising edge` 和 `Falling edge` 两个选项的条件下均生成事件。

### **Sample time** — 采样时间 `-1`（默认）| positive scalar

指定采样时间（以 seconds 为单位），以定义输出包含数字输入数据的消息的速率。

## 所属库

SoC Blockset / Peripherals Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

模拟处理器上的数字输入和输出引脚

Digital IO Interface 模块模拟硬件板上 GPIO 处理器引脚的行为。您可以将该模块配置为数字输入模块或数字输出模块。

当您将此模块配置为输入时，该模块会捕获引脚上输入信号的穿越事件。当穿越事件发生时，该模块会将引脚的逻辑状态作为信号发出，并向 Task Manager 模块发送事件。然后，任务可以使用 IO Data Sink 模块读取逻辑值。

当您将此模块配置为输出时，该模块会发出连接的 IO Data Source 模块的逻辑信号。
