---
type: simulink-block
title: 'RC Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'rcreceive'
documentation_source_path: 'ardupilot/ref/rcreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# RC Receive

## 端口

### 输出

### **Failsafe** — 失效保护状态标量

RC Receive 模块默认输出失效保护状态。如果 RC 发射器在运行期间关闭或丢失信号，失效保护输出会切换为 `1`。使用此输出在模型中触发安全机制。

**数据类型：** `double`

### **Ch *`x`* Raw** — 来自指定 RC 通道向量的原始数据

每个所选通道的原始数据。当您启用归一化时，它会使用指定的 trim 和 deadzone 设置调整输出值。

**数据类型：** `double`

### **Mode** — 当前飞行模式标量

该模块根据您的 Mission Planner 配置输出飞行模式索引（从 0 开始）。该值指示当前映射的飞行模式。

#### 依赖关系

要启用此端口，请选择 **Output flight mode** 参数。

**数据类型：** `uint8`

### **RSSI** — 无线电信号强度标量

该模块输出 RC 发射器的无线电信号强度。在您的模型中使用此值进行监测或实现安全机制。

#### 依赖关系

要启用此端口，请选择 **Output radio signal strength indicator(RSSI)** 参数。

**数据类型：** `int32`

### **Arm** — 载具解锁状态标量

该模块在已解锁时输出 `1`，在未解锁时输出 `0`。

#### 依赖关系

要启用此端口，请选择 **Output arming status** 参数。

**数据类型：** `uint8`

### **Estop** — 紧急停止状态标量

该模块输出一个信号，指示电机紧急停止是否已触发。

#### 依赖关系

要启用此端口，请选择 **Output motor emergency stop status** 参数。

**数据类型：** `uint8`

## 参数

#### 通道选项卡

### **Channel Selection** — 用于原始数据通道的通道

选择您要从发射器读取哪些 RC 通道。使用界面添加或移除通道。该模块根据您在此参数列表中的选择显示 `Ch x Raw` 输出。最多可以添加 `16` 个通道。

### **Normalize output for channels using trim and deadzone** — 将 trim 和 deadzone 应用于原始 RC 数据 `off`（默认）| `on`

选择此参数可使用指定的 trim 和 deadzone 设置对所选通道的输出进行归一化。

### **Sample time** — 模块读取数值的时间间隔 `-1`（默认）

该模块从 ArduPilot 自动驾驶仪获取数值的时间间隔。

#### 高级选项卡

### **Output flight mode** — 启用飞行模式的输出端口 off（默认）| on

选择此参数以启用 **Port** 输出端口。要查看飞行模式到通道值的映射信息，请参阅 Flight Mode Mapping。

### **Output radio signal strenght indicator(RSSI)** — 启用 RSSI 的输出端口 off（默认）| on

选择此参数以启用 **RSSI** 输出端口。

### **Output arming status** — 启用解锁状态的输出端口 off（默认）| on

选择此参数以启用 **Arm** 输出端口。

### **Output motor emergency stop status** — 启用电机紧急停止状态的输出端口 off（默认）| on

选择此参数以启用 **Estop** 输出端口。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Peripheral Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2025b 中引入**

## 描述

读取无线电控制通道数据

RC Receive 模块从 RC 发射器的选定通道获取原始输入数据。该模块提供用于应用 trim 和 deadzone 调整以进行输出归一化的选项。此外，该模块可以输出辅助信息，例如飞行模式、无线电信号强度指示器 (RSSI)、解锁状态和电机紧急停止状态。
