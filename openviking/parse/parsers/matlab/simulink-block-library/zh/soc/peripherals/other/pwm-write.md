---
type: simulink-block
title: 'PWM Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Other'
documentation_page: 'pwmwrite'
documentation_source_path: 'ref/pwmwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Write

## 端口

### 输入

### **Compare** — 比较器触发值 正标量 | *N* 长度正向量

指定触发脉冲宽度调制波形变化的比较器值。当 *N* 为 `1` 时，比较器值定义 PWM 波形的占空比。使用 `2` 个比较器以及 PWM Interface 模块中提供的设置，可以实现对输出波形更细粒度的控制。

**数据类型：** `single` | `double`

### **Period** — PWM 波形周期 正标量

指定 PWM 波形的总周期。

#### 依赖关系

仅当启用 **Show period as input** 参数时，此参数才可用。

**数据类型：** `single` | `double`

### **Phase** — 波形的相位偏移 从 `0` 到 PWM 周期的标量

指定 PWM 波形相对于波形周期的相位。相位表示为 `0` 与 PWM 周期之间的标量。

#### 依赖关系

仅当启用 **Show phase as input** 参数时，此参数才可用。

**数据类型：** `single` | `double`
### 输出

### **msg** — PWM 占空比值 标量

此消息端口将占空比值作为消息发送到连接的 PWM Interface 模块。有关消息的详细信息，请参阅消息。

**注意**

此输出仅在仿真期间使用，在代码生成和外部模式仿真中会被忽略。

**数据类型：** `SoCData`

## 参数

### **Show period as input** — 显示 Period 输入端口 `off` (默认) | `on`

在模块上显示一个 **Period** 输入端口。此端口接受 PWM 波形的动态周期值，允许在执行期间修改波形周期。

### **Show phase as input** — 显示 Phase 输入端口 `off` (默认) | `on`

在模块上显示一个 **Phase** 输入端口。此端口接受 PWM 波形的动态相位值，允许在执行期间修改波形的相位偏移。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当部署到支持的硬件板时，此模块生成的代码会为指定的 PWM 模块写入 MCU 中的 PWM 寄存器。有关配置寄存器设置的详细信息，请参阅硬件映射。

## 版本历史

**在 R2020b 中引入**

## 描述

将脉冲宽度调制 (PWM) 信号配置发送到 PWM Interface 模块

PWM Write 模块设置 PWM 外设的占空比。在仿真中，该模块直通占空比输入，以驱动 PWM Interface 模块，该模块仿真硬件产生的 PWM 开关信号。部署到硬件时，PWM Write 模块会写入硬件上相应的 PWM 驱动程序。
