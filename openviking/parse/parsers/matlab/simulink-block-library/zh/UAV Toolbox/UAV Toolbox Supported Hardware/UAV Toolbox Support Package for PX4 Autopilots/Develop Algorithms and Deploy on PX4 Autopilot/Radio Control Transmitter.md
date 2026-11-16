---
type: simulink-block
title: 'Radio Control Transmitter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'radiocontroltransmitter'
documentation_source_path: 'px4/ref/radiocontroltransmitter.html'
language: zh-CN
chinese_source: worker-translation
---

# Radio Control Transmitter

## 端口

### 输出

### **Ch *`x`*** — 来自指定无线电通信信道的测量脉冲宽度值 标量 | 时间，范围为 [1, 2] ms

从 Radio Control Transmitter 的所选信道获取的脉冲宽度值。将这些输出值连接到 Simulink 模型中的飞控逻辑。

**数据类型：** `uint16`

### **Num Ch** — 实际可见的信道计数 标量

基于与 Radio Control Transmitter 的通信，实际可见的信道计数

#### 依赖关系

仅当您选择 **实际可见的信道数** 参数时，才会出现此输出。

**数据类型：** `uint32`

### **RSSI** — 来自 RC Transmitter 的 RSSI 值 负 | `0` | 正

从 Radio Control Transmitter 获取的 RSSI（接收信号强度指示器）值。

对于未定义信号，该值为负；对于无信号，该值为 0；对于完全接收，该值为正。

#### 依赖关系

仅当您选择 **接收信号强度指示器 (RSSI)** 参数时，才会出现此输出。

**数据类型：** `int32`

### **RC Source** — RC 通信的输入源 标量

标识 RC 通信的输入源。该值范围为 `0` 到 `13`（这些值对应于 `Firmare/msg` 目录中 `input_rc.msg` 文件提到的相同值）。

#### 依赖关系

仅当您选择 **无线电控制输入源** 参数时，才会出现此输出。

**数据类型：** `uint8`

### **Last valid time** — 最后一次有效接收的时间戳

来自 Radio Control Transmitter 的最后一次有效接收的时间戳。

#### 依赖关系

仅当您选择 **最后一次有效接收时间** 参数时，才会出现此输出。

**数据类型：** `uint64`

### **Timestamp** — 当前时间戳

从 Radio Control Transmitter 接收到的值的当前时间戳。

#### 依赖关系

仅当您选择 **Timestamp** 参数时，才会出现此输出。

**数据类型：** `double`

### **Status** — 从 input\_rc uORB 主题读取的数据的状态 [`0,7`] 中的整数

Status 输出指示数据是否在之前的时间步中接收。值 `0` 表示 `Ch` 输出处的数据是最新的，并且与 Radio Control Transmitter 的通信有效。

介于 1 和 7 之间的值表示以下情况：

- 在当前时间步中，uORB 主题未读取到任何值
- 与 Radio Control Transmitter 的通信丢失
- Radio Control Transmitter 进入 failsafe 模式

此输出可用于触发子系统，以处理从 RC Transmitter 接收的新数据。

**数据类型：** `uint8`

## 参数

#### 主选项卡

### **通道选择** — 您希望从中接收值的无线电信道 信道

选择您希望从中接收值的信道，这些值是从 Radio Control Transmitter 读取的。模块的 `Ch` 输出会根据此参数列表中的选择而出现。

### **实际可见的信道数** — 实际可见的信道计数 `off`（默认） | `on`

选择此选项可获取基于与 Radio Control Transmitter 的通信而实际可见的信道计数。

### **接收信号强度指示器 (RSSI)** — 来自 RC Transmitter 的 RSSI 值 `off`（默认） | `on`

选择此选项可获取从 Radio Control Transmitter 接收到的 RSSI 值

### **无线电控制输入源** — RC 通信的输入源 `off`（默认） | `on`

选择此选项可标识 RC 通信的输入源。

### **最后一次有效接收时间** — 最后一次有效接收的时间戳 `off`（默认） | `on`

选择此选项可获取来自 Radio Control Transmitter 的最后一次有效接收的时间戳。

### **Timestamp** — 当前时间戳 `off`（默认） | `on`

选择此选项可获取来自 Radio Control Transmitter 的信道值的当前时间戳。

### **采样时间** — 模块读取值的时间间隔 `1/250` seconds（默认） | 任何非负值，且为 1/250 的倍数 | -1

输入模块从 RC Transmitter 读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **等待直到接收到数据** — 等待直到请求的数据可用 off（默认） | on

- 当您选择此选项时，读取操作以阻塞模式运行。读取操作在等待请求的数据可用时会被阻塞。

  如果当计划开始下一次读取操作时，目标硬件仍在等待数据可用，则会发生任务超限。

  要解决超限，请使用 **采样时间** 参数增大时间步。
- 当您清除此选项时，读取操作以非阻塞模式运行。在此模式下，模块不会等待请求的数据可用。

### **超时（秒）** — 等待直到接收到数据的时间 `5`（默认） | (0, 2^32/1000]

如果选择了 **等待直到接收到数据** 参数，请指定模块在每个时间步等待数据的时间量。如果发生超时，读取操作将被中止。

#### 依赖关系

仅当您选择 **等待直到接收到数据** 参数时，才会出现此参数。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取 input\_rc uORB 主题以从 Radio Control Transmitter 获取数据

Radio Control Transmitter 模块读取 input\_rc uORB 主题，以获取从 Radio Control Transmitter 在指定信道发送的信号。

在正常模式仿真期间，该模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
