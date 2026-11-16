---
type: simulink-block
title: 'Resolver'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'resolver'
documentation_source_path: 'infineonaurix/ref/resolver.html'
language: zh-CN
chinese_source: worker-translation
---

# Resolver

## 端口

### 输出

### **θₘ** — 旋转变压器传感器的角度 `scalar` | `vector`

该模块以 radians（默认）或 degrees 为单位输出旋转变压器传感器的位置。θₘ 输出的大小取决于 **启用时间戳** 参数。

选择 **启用时间戳** 参数会使 θₘ 的大小为 2x1，禁用 **启用时间戳** 参数会使 θₘ 的大小为 1x1。

**数据类型：** `single`

### **timestamp** — 16-bit 计数器值的时间戳 `scalar`

该端口输出时间戳，指示自上次转换以来经过的时间（以 seconds 为单位）。

#### 依赖项

要启用此端口，请选择 **启用时间戳** 参数。

**数据类型：** `single`

## 参数

### **角度输入** — 角度的测量单位 `Radians`（默认） | `Degrees`

选择旋转变压器传感器的位置测量单位。

### **启用时间戳** — 选择以启用时间戳 `off`（默认） | `on`

选择以启用时间戳。

当您选择 `Enable timestamp` 参数时，该模块会配置一个额外的输出端口 **timestamp**。

选择此参数会启用 Resolver 外设配置窗口中的 **时间戳** 选项卡以及 **事件** 选项卡下的时间戳事件中的选项。

### **采样时间** — 模块读取位置的频率 `-1`（默认） | `scalar`

以 seconds 为单位指定该模块读取旋转变压器传感器位置的频率。

当您将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2024a 中引入**

## 描述

测量旋转变压器传感器的位置

Resolver 模块测量旋转变压器传感器的位置，并且还能够为旋转变压器传感器生成励磁载波信号。

Resolver 模块以 radians（默认）或 degrees 为单位输出旋转变压器传感器的角度。该模块基于旋转变压器传感器感测到的正弦和余弦电压输出测量值。

启用时间戳选项会创建一个额外的输出端口，该端口以有符号值的形式输出自上次转换以来的时间戳（以 seconds 为单位）。
