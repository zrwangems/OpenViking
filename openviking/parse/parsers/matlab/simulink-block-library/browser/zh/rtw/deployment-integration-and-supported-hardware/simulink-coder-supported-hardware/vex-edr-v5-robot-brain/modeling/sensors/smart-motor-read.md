---
type: simulink-block
title: 'Smart Motor Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'smartmotorread'
documentation_source_path: 'vexv5/ref/smartmotorread.html'
language: zh-CN
chinese_source: worker-translation
---

# Smart Motor Read

## 端口

### 输入

### **Reset** — 用于复位编码器读数（integer）的信号（0 = no reset；integer ≥ 1 = reset）

连接到可复位 V5 Smart Motor 内置编码器的信号。

#### 依赖关系

仅当将 **Reset mode** 参数设置为 `Reset by external signal` 时，此输入才会出现。

**数据类型：** `double`
### 输出

### **Position** — 来自 V5 Smart Motor 的编码器值 tick count | rotations | degrees

从 V5 Smart Motor 内置编码器读取的值，具体取决于所选的 `Encoder unit`。

例如，如果电机已完成两个 rotations（假设齿轮比为 36:1）：

- tick count = `3600`
- degrees = `720`
- rotations = `2`

#### 依赖关系

此输出取决于为 **Encoder unit** 参数选择的值。

**数据类型：** `double`

### **Velocity** — V5 Smart Motor 的速度 RPM

从内置编码器读取的 V5 Smart Motor 速度。符号决定电机的旋转方向，幅值决定以 RPM 表示的速度。正值表示电机沿顺时针方向旋转，负值表示沿逆时针方向旋转。输出值为 `0` 表示电机静止。

#### 依赖关系

此输出仅当选择 **Output velocity and fault** 复选框时才会出现。

**数据类型：** `double`

### **Fault** — 来自 V5 Smart Motor 的故障指示 `1` | l`2` | `3`

从 V5 Smart Motor 解码得到的故障指示。输出值表示以下类型的故障：

- `1`: 过流故障
- `2`: 过温故障
- `3`: 过流和过温故障

#### 依赖关系

此输出仅当选择 **Output velocity and fault** 复选框时才会出现。

**数据类型：** `double`

## 参数

### **Smart Port** — 选择 V5 Smart Motor 连接到的 Smart Port 1（默认）| `1` 到 `21`

选择 VEX EDR V5 Robot Brain 上 V5 Smart Motor 连接到的 Smart Port。VEX EDR V5 Robot Brain 上有 21 个 Smart Ports，可连接到 V5 Smart Motor。

模型中的每个模块的 Smart Port 必须唯一。如果使用多个具有相同端口的 Smart Motor Read 模块，则可能只有最后执行的 Smart Motor Read 模块处于活动状态。对于 Vex Robotics Competition，您可以在 driver mode 或 autonomous mode 中使用具有相同 Smart Port 的同一个 Smart Motor Read 模块。

### **Encoder unit** — 选择用于从编码器读取电机位置的单位 `Counts`（默认）| `Rotations` | `Degrees`

选择用于从 V5 Smart Motor 内置编码器读取其位置的单位。位置可按 tick counts、rotations 数量或 degrees 读取。

### **Reset mode** — 选择用于读取值的复位模式 `Reset at each sample time`（默认）| `No reset` | `Reset by external signal`

选择用于从 V5 Smart Motor 内置编码器读取值的复位模式。

当选择 `Reset by external signal` 时，模块会添加一个附加输入 – `Reset` – 该输入可连接到复位信号。

### **Sample time** — 模块读取值的时间间隔 `0.2`（默认）| positive scalar | -1

输入模块从 V5 Smart Motor 内置编码器读取值的时间间隔。

将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示已连接的 V5 Smart Motor 并读取编码器值

Smart Motor Read 模块表示连接到 VEX® EDR V5 Robot Brain 上指定端口的 V5 Smart Motor，并读取 V5 Smart Motor 内置编码器的值。
