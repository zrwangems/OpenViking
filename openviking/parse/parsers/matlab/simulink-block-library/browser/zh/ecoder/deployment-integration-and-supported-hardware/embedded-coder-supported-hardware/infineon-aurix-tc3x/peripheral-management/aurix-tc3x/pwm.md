---
type: simulink-block
title: 'PWM'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'pwm'
documentation_source_path: 'infineonaurixtc3x/ref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口

### 输入

### **duty** — 决定占空比的输入值 Float 范围在 [0-100] 之间

发送到模块输入的值决定开发板在 PWM Peripheral Configuration 中指定的 PWM 引脚上输出的方波的占空比。

**数据类型：** `Float`

### **freq** — 输入端口决定 PWM 信号频率 `scalar`

freq 端口决定所选通道的 PWM 信号频率。启用频率端口时，该端口接受标量输入值，并将其设置为定时器单元的频率。

#### 依赖项

要启用此端口，请选择 **Enable frequency input** 参数。

### **phase** — 所选通道的相位 `scalar` | `vector`

phase 端口接受范围为 `0 to 2`pi 的输入值，并设置对应通道的相位。它接受与所选 **N** 个通道对应的 `N x 1` 值。

#### 依赖项

要启用此端口，请设置 **Enable phase input** 参数。

**数据类型：** `single` | `double`

### **dtm\_rise** — 上升死区时间模块 `scalar` | `vector`

dtm\_rise 端口接受以秒为单位的上升死区时间值。为使用此功能，PWM 外设应用中选择的定时器单元应具有 DTM 子模块。它接受与所选 **N** 个通道对应的 `N x 1` 值。

#### 依赖项

要启用此端口，请设置 **Enable dead time properties input** 参数。

**数据类型：** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **dtm\_fall** — 下降死区时间模块 `scalar` | `vector`

dtm\_fall 端口接受以秒为单位的下降死区时间值。为使用此功能，PWM 外设应用中选择的定时器单元应具有 DTM 子模块。它接受与所选 **N** 个通道对应的 `N x 1` 值。

#### 依赖项

要启用此端口，请设置 **Enable dead time properties input** 参数。

**数据类型：** `Float` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **start/stop** — 在通道上启动或停止 PWM 的选项 `scalar`

此端口接受任意正整数，并根据该值启动或停止 PWM 生成。

- `0 —` 停止 PWM 生成
- `1 or any positive integer —` 启动 PWM 生成

#### 依赖项

要查看此端口，请禁用 **Enable dead time properties input** 参数。

**数据类型：** `double` | `uint8` | `uint16` | `uint32`

### 输出

### **Status** — PWM 模块的状态 `scalar`

该模块将 PWM 模块的状态输出为以下值之一：

- `255 —` 未知状态
- `0 —` 已初始化
- `1 —` 运行中
- `2 —` 已停止
- `3 —` 错误

#### 依赖项

要查看此端口，请设置 **Enable status output** 参数。

**数据类型：** `uint8`

### **msg** — SoC 仿真消息 `bus`

该端口在仿真期间以 SoC 仿真消息格式输出 PWM 总线对象。PWM 总线对象包含模块在输入端口接收到的信息。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

该端口在仿真期间输出 PWM 总线对象。PWM 总线对象包含模块在输入端口接收到的信息。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### 基本

### **Enable frequency input** — 选择此项以启用输入频率端口 `off`（默认） | `on`

选择此参数以设置 PWM 频率。

当您选择 **Enable frequency input** 参数时，该模块会配置一个输入端口 `freq`。

### **Enable phase input** — 选择此项以启用输入相位端口 `off`（默认） | `on`

选择此参数以设置所选通道的相位。

当您选择 **Enable phase input** 参数时，该模块会配置一个输入端口 `phase`。

### **Enable status output** — 选择此项以配置状态端口 `off`（默认） | `on`

当您选择 **Enable status output** 参数时，该模块会配置 `Status` 输出端口。

### **Enable simulation port** — 在模块中启用外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数以配置 SoC 兼容的仿真端口或基于 Simulink® 信号的仿真端口，以启用外设仿真功能。

#### 依赖项

要查看此参数，请选择 **Enable simulation port** 参数。

### 高级

### **Number of outputs** — 选择所需通道 `1`（默认） | `2` | `3` | `...`

选择要发送占空比所需的 PWM 通道数。通道数决定输入端口 `phase`、`dtm_rise` 和 `dtm_fall` 的大小。

所选通道数取决于 PWM 外设配置应用中的定时器模块选择。

- `TOM—` 有 16 个通道可用
- `ATOM—` 有 8 个通道可用

### **Start PWM after init** — 初始化后生成 PWM 的选项 `off`（默认） | `on`

选择此项可在初始化后生成 PWM，禁用此项可手动启动和停止通道上的 PWM 生成。

当您禁用 **Start PWM after init** 参数时，该模块会配置一个输入端口 `start/stop`。

### **Enable dead time properties input** — 选择此项以启用上升和下降输入端口 `off`（默认） | `on`

选择此参数以确定 PWM 死区时间值（以秒为单位）。

有关标准死区时间生成的详细信息，请参阅死区时间模块属性。

**注意**

在模块中启用 dead time properties 参数会配置 `dtm_rise` 和 `dtm_fall` 输入端口。要使用死区时间功能，请转到 Hardware Mapping 窗口中的 PWM Peripheral Configuration，并在 **Module** 和 **Channel** 选项卡中配置相应的死区时间参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

生成脉宽调制波形

该模块输入控制对应通道方波的占空比。输入值 `0` 产生 `0` 百分比占空比，输入值 `100` 产生 `100` 百分比占空比。它接受与所选 **N** 个通道对应的 `N x 1` 个占空比值。
