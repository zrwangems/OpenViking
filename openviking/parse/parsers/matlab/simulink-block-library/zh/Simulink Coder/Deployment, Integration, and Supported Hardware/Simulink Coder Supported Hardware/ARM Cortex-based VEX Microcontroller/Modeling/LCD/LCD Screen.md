---
type: simulink-block
title: 'LCD Screen'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / LCD'
documentation_page: 'lcdscreen'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/lcdscreen.html'
language: zh-CN
chinese_source: worker-translation
---

# LCD Screen

## 端口

### 输入

### **Bklgt** — 用于打开或关闭 LCD 背光的标量信号

当您向此端口发送 0 时，LCD 背光关闭。否则，它会打开。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Val** — 标量输入值

要在 LCD 屏幕上显示的值。

对于标签及其值的组合，最多显示 16 个字符。LCD 屏幕上超过 16 个字符的任何输出都会被截断。

#### 依赖关系

仅当清除 **仅显示文本** 参数时，此端口才可用。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **UART 端口** — UART 端口号 `1`（默认）| `2`

选择 LCD Display Module 连接到的微控制器上的 UART 端口号。

### **仅显示文本** — 指定是否仅显示标签 `off`（默认）| `on`

- `off`— 在 LCD 屏幕上显示标签及其值的组合。
- `on`— 在 LCD 屏幕上仅显示标签。

  选择此参数时，`Val` 端口不可用，且 **精度** 参数会隐藏。

### **标签** — 要显示的标签 Value（默认）

指定要在 LCD 屏幕上显示的标签。该模块将标签显示在输入值的左侧。例如，如果要显示 LCD 按钮的状态，请指定 `Button:`。

标签最多显示 16 个字符。LCD 屏幕上超过 16 个字符的任何输出都会被截断。

### **显示行** — 用于显示标签或标签及其值组合的 LCD 行 `1`（默认）| `2`

选择用于显示标签或标签及其值组合的行。

### **精度** — 小数点后的位数 `2`（默认）| `0` | `1` | `3` | `4` | `5` | `6`

选择要为输入值显示的小数点后的位数。

#### 依赖关系

仅当清除 **仅显示文本** 参数时，此参数才会出现。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/LCD

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

在 LCD 屏幕的指定行显示文本和数值

LCD Screen 模块在 LCD 屏幕上显示静态标签和来自模块输入的值。您也可以选择仅显示标签而不显示值。

对于标签或标签及其值的组合，最多显示 16 个字符。LCD 屏幕上超过 16 个字符的任何输出都会被截断。

例如，如果选择仅显示标签，则该标签的最大长度可以为 16 个字符。如果选择标签及其值的组合，则两者显示的字符最大长度为 16。

使用此模块，选择要在其中显示标签和值的行，然后打开或关闭 LCD 背光。
