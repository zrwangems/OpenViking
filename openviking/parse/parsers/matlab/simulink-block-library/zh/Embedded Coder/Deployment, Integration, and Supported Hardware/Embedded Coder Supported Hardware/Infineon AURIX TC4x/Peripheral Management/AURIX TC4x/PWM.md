---
type: simulink-block
title: 'PWM'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'pwm'
documentation_source_path: 'infineonaurix/ref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口

### 输入

### **duty** — 确定占空比的输入值 `Float range between [0-100]`

发送到模块输入的值确定板卡在 PWM Peripheral Configuration 中指定的 PWM 引脚上输出的方波的占空比。

**数据类型：** `Float`

### **freq** — 输入端口确定 PWM 信号的频率 `scalar`

`freq` 端口确定所选通道的 PWM 信号频率。当您启用频率端口时，该端口接受标量输入值，并将其设置为定时器单元的频率。

#### 依赖关系

要启用此端口，请选择 **Enable frequency input** 参数。

### **phase** — 所选通道的相位 `scalar` | `vector`

`phase` 端口接受 `0 to 2`pi 范围内的输入值，并设置对应通道的相位。它接受对应于所选 **N** 个通道的 `N x 1` 个值。

#### 依赖关系

要启用此端口，请选择 **Enable phase input** 参数。

**数据类型：** `single` | `double`

### **dtm\_rise** — 上升死区时间模块 `scalar` | `vector`

dtm\_rise 端口接受以 seconds 为单位的上升死区时间值。在 PWM peripheral app 中选择的定时器单元应具有 DTM 子模块，才能使用此功能。它接受对应于所选 **N** 个通道的 `N x 1` 个值。

#### 依赖关系

要启用此端口，请选择 **Enable dead time properties input** 参数。

**数据类型：** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **dtm\_fall** — 下降死区时间模块 `scalar` | `vector`

dtm\_fall 端口接受以 seconds 为单位的下降死区时间值。在 PWM peripheral app 中选择的定时器单元应具有 DTM 子模块，才能使用此功能。它接受对应于所选 **N** 个通道的 `N x 1` 个值。

#### 依赖关系

要启用此端口，请选择 **Enable dead time properties input** 参数。

**数据类型：** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### 输出

### **Status** — PWM 模块的状态 `scalar`

模块将 PWM 模块的状态输出为以下值之一：

- `255—`未知状态
- `0—` 已初始化
- `1—` 正在运行
- `2—` 已停止
- `3—` 错误

#### 依赖关系

要查看此端口，请选择 **Enable status output** 参数。

**数据类型：** `uint8`

### **msg** — SoC Blockset 仿真消息 `bus`

在仿真期间，该端口以 SoC Blockset™ 仿真消息格式输出 PWM 总线对象。PWM 总线对象包含模块在输入端口处接收的信息。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

该端口在仿真期间输出 PWM 总线对象。PWM 总线对象包含模块在输入端口处接收的信息。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### 基本

### **Enable frequency input** — 选择以启用输入频率端口 `off`（默认）| `on`

选择此参数以设置 PWM 频率。

当您选择 **Enable frequency input** 参数时，模块会配置一个输入端口 `freq`。

### **Enable phase input** — 选择以启用输入相位端口 `off`（默认）| `on`

选择此参数以设置所选通道的相位。

当您选择 **Enable phase input** 参数时，模块会配置一个输入端口 `phase`。

### **Enable status output** — 选择以配置状态端口 `off`（默认）| `on`

当您选择 **Enable status output** 参数时，模块会配置 `Status` 输出端口。

### **Enable simulation port** — 在模块中启用外设仿真端口 `off`（默认）| `on`

选择此参数以启用外设仿真能力。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认）| `Signal`

选择此参数以配置兼容 SoC 的仿真端口或基于 Simulink® 信号的仿真端口，从而启用外设仿真能力。

#### 依赖关系

要查看此参数，请选择 **Enable simulation port** 参数。

### 高级

### **Number of channels** — 选择所需通道 `1`（默认）| `2` | `3` | `...`

选择要发送占空比的所需 PWM 通道数。通道数决定输入端口 `phase`、`dtm_rise` 和 `dtm_fall` 的大小。

所选通道数取决于 PWM peripheral configuration app 中的定时器模块选择。

- `TOM—`有 16 个通道可用
- `ATOM—`有 8 个通道可用

### **Enable dead time properties input** — 选择以启用上升和下降输入端口 `off`（默认）| `on`

选择此参数以确定 PWM 死区时间值，以 seconds 为单位。

有关标准死区时间生成的详细信息，请参阅 Dead-Time Module Properties。

**注意**

在模块中启用 dead time properties 参数会配置 `dtm_rise` 和 `dtm_fall` 输入端口。要使用死区时间功能，请转到 Hardware Mapping 窗口中的 PWM Peripheral Configuration，并在 **Module** 和 **Channel** 选项卡中配置相应的死区时间参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

生成脉宽调制波形

模块输入控制对应通道方波的占空比。输入值 `0` 产生 `0` percent 占空比，输入值 `100` 产生 `100` percent 占空比。它接受对应于所选 **N** 个通道的 `N x 1` 个占空比值。
