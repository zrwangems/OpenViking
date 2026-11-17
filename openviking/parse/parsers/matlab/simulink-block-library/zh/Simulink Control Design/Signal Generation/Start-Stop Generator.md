---
type: simulink-block
title: 'Start-Stop Generator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Signal Generation'
documentation_page: 'startstopgenerator'
documentation_source_path: 'ug/startstopgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Start-Stop Generator

## 端口
```yaml
ports:
- name: enable
  summary: 启用和禁用启停信号生成 标量
  direction: input
  data_types: single | double
- name: start times
  summary: 启动时间 标量 | 向量
  direction: input
  data_types: single | double
- name: y
  summary: 稳态值 标量 | 向量
  direction: input
  data_types: single | double
- name: start/stop
  summary: 启停信号 标量
  direction: output
  data_types: single | double
```

### 输入

### **enable** — 启用和禁用启停信号生成 标量

指定一个信号以启用 (`1`) 或禁用 (`0`) 模块动作。

**数据类型：** `single` | `double`

### **start times** — 启动时间 标量 | 向量

以标量或向量的形式指定信号的启动时间。

模块在指定的启动时间处生成一个从 0 变为 1 的信号，持续时间由 **Duration (sec)** 参数指定。持续时间过后，信号从 1 变为 0。

**数据类型：** `single` | `double`

### **y** — 稳态值 标量 | 向量

将被控对象的输出连接到此端口。模块根据此信号确定系统的当前运行状态并生成启停信号。

**数据类型：** `single` | `double`
### 输出

### **start/stop** — 启停信号 标量

启停信号。信号值的变化如下：

- 在使用 **start times** 指定的值处或使用 **Steady-state settings** 确定的稳态时间处，从负值或零变为正值。
- 在 **Duration (sec)** 中指定的持续时间过后，从正值变为负值或零。

通常，您使用此信号来启动和停止频率响应估计、信号生成或自动整定过程。当 **enable** 端口设置为 0 时，模块不生成启停信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Sample time (Ts)
  summary: 采样时间 0.1（默认）| 正标量
  group: ''
- name: Data Type
  summary: 浮点精度 double（默认）| single
  group: ''
- name: Source of start time points
  summary: 启动时间点来源 External time vector（默认）| Time after reaching steady-state
  group: ''
- name: Duration (sec)
  summary: 启停信号持续时间 10（默认）| 标量
  group: ''
- name: Number of samples after reaching steady-state to generate start-stop signal
  summary: 开始信号生成的延迟 2（默认）| 非负整数
  group: ''
- name: Settling time upper bounds
  summary: 调节时间上界 [1.1 2.1 3.1]（默认）| 向量
  group: ''
- name: Settling time lower bounds
  summary: 调节时间下界 [0.9 1.9 2.9]（默认）| 向量
  group: ''
- name: Settling time interval
  summary: 调节时间间隔 5（默认）| 标量 | 向量
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Sample time (Ts)** — 采样时间 `0.1`（默认）| 正标量

指定生成的启停信号的采样时间。

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

### **Source of start time points** — 启动时间点来源 `External time vector`（默认）| `Time after reaching steady-state`

将启动时间点的来源指定为以下之一：

- `External time vector` — 使用 **start times** 输出端口指定启动时间的显式值。
- `Time after reaching steady-state` — 使用被控对象输出信号 **y** 和 **Steady-state settings** 来确定开始生成启停信号的时间。

### **Duration (sec)** — 启停信号持续时间 `10`（默认）| 标量

指定启停信号的持续时间。

### **Number of samples after reaching steady-state to generate start-stop signal** — 开始信号生成的延迟 `2`（默认）| 非负整数

指定达到稳态后模块延迟生成启停信号的采样数。

### **Settling time upper bounds** — 调节时间上界 `[1.1 2.1 3.1]`（默认）| 向量

指定用于确定调节时间和工作点稳态的运行值上界。

此向量的每个值对应于该索引处工作点值的上界。

### **Settling time lower bounds** — 调节时间下界 `[0.9 1.9 2.9]`（默认）| 向量

指定用于确定调节时间和工作点稳态的运行值下界。

此向量的每个值对应于该索引处工作点值的下界。

### **Settling time interval** — 调节时间间隔 `5`（默认）| 标量 | 向量

指定运行条件保持稳态的时间间隔。

使用向量为不同工作点指定不同的时间间隔。
## 所属库

Simulink Control Design / Signal Generation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

生成用于信号生成、估计和自动整定模块的启停信号

使用此模块为 Simulink® Control Design™ 库中的信号生成、频率响应估计和 PID 自动整定模块的 **start/stop** 输入端口生成信号。该端口决定何时开始和停止在这些模块中生成扰动信号。Start-Stop Generator 模块生成一个信号，在指定的时间值处从 0 变为 1 以启用这些模块，并在指定持续时间过后从 1 变为 0 以禁用这些模块。

当您需要在不同工作条件下生成启停信号以启用估计或自动整定过程时，此模块非常有用。
