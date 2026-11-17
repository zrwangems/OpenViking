---
type: simulink-block
title: 'Audio Capture Interface'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'audiocaptureinterface'
documentation_source_path: 'ref/audiocaptureinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Capture Interface

## 端口
```yaml
ports:
- name: data
  summary: 来自捕获音频的数据帧 *M* 元素向量 | *M*×*C* 矩阵
  direction: input
  data_types: int8 | int16 | int32
- name: event
  summary: 任务事件信号 标量
  direction: output
  data_types: rteEvent
- name: msg
  summary: SoC 消息数据 标量
  direction: output
  data_types: SoCData
```

### 输入

### **data** — 来自捕获音频的数据帧 *M* 元素向量 | *M*×*C* 矩阵

要提供单个音频通道，请将此数据指定为 *M* 元素音频数据帧，其中 *M* 定义每帧音频数据的采样数。要提供多个音频通道，请将数据指定为 *M*×*C* 矩阵，其中 *C* 定义通道数。

#### 依赖关系

要启用此端口，请将 **Input** 参数设置为 `From input port`。

**数据类型：** `int8` | `int16` | `int32`
### 输出

### **event** — 任务事件信号 标量

此端口在捕获所有通道的一帧音频采样后发送消息。此输出连接到 Task Manager 模块的输入，以执行关联的事件驱动任务。

#### 依赖关系

要启用此端口，请选择 **Show event port** 参数。

**数据类型：** `rteEvent`

### **msg** — SoC 消息数据 标量

此端口将包含音频数据的数据消息输出到连接的 Audio Capture 模块。

**数据类型：** `SoCData`
## 参数
```yaml
parameters:
- name: Input
  summary: 仿真音频数据的来源 From dialog（默认）| From input port | From timeseries object
  group: ''
- name: Value
  summary: 要输出的音频数据 int16([1 2 3 4 5 6 7 8])（默认）| *CN* 长度向量
  group: ''
- name: Object name
  summary: timeseries 对象 [ ]（默认）| MATLAB workspace variable
  group: ''
- name: Sample time
  summary: 采样时间，以秒为单位 -1（默认）| 正标量
  group: ''
- name: Show event port
  summary: 启用任务事件端口的选项 off（默认）| on
  group: ''
```

### **Input** — 仿真音频数据的来源 `From dialog`（默认）| `From input port` | `From timeseries object`

指定仿真音频数据的来源。

### **Value** — 要输出的音频数据 `int16([1 2 3 4 5 6 7 8])`（默认）| *C**N* 长度向量

将音频数据指定为 *C**N* 长度向量，表示所有通道的音频帧，其中 *N* 是每帧的采样数，*C* 是音频通道数。每个通道的采样是连续的。

### **Object name** — timeseries 对象 [ ]（默认）| `MATLAB workspace variable`

将音频数据指定为在 MATLAB® 工作区中定义的 timeseries 对象。

### **Sample time** — 采样时间，以秒为单位 `-1`（默认）| 正标量

输入采样时间，定义输出包含音频数据的消息的速率。

### **Show event port** — 启用任务事件端口的选项 `off`（默认）| `on`

选择此参数以启用事件端口，当连接到 Task Manager 模块时，可以执行事件驱动任务。
## 所属库

SoC Blockset / Peripherals

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的更多信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，高级 Linux 声音架构（ALSA）驱动框架在设备上执行音频捕获。相关的 Audio Capture 模块代表 ALSA 驱动。有关 ALSA 驱动框架的更多信息，请参阅 Advanced Linux Sound Architecture 网站。

## 版本历史

**在 R2021a 中引入**

## 描述

仿真从硬件上的音频流捕获采样

Audio Capture Interface 模块仿真音频输入设备的行为。该模块将音频采样作为消息输出到连接的 Audio Capture 模块，该模块仿真音频驱动代码并连接到您的算法。该模块还可以发出事件，当连接到 Task Manager 模块时，可以触发包含 Audio Capture 模块的任务。
