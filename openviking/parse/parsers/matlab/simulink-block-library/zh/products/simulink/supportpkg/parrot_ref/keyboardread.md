---
type: simulink-block
title: 'Keyboard Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Parrot Minidrones / Modeling'
documentation_page: 'keyboardread'
documentation_source_path: 'supportpkg/parrot_ref/keyboardread.html'
language: zh-CN
chinese_source: worker-translation
---

# Keyboard Read

## 端口

### 输出

### **Port\_1** — 键盘上按下的基本字符的 ASCII 码 ASCII

支持的基本字符包括键盘上存在的所有可打印字符——字母、数字、标点符号和常见符号。

**数据类型：** `uint8`

## 参数

### **采样时间** — 模块读取数据的时间间隔 `0.005`（默认）| 任意非负值，且为 0.005 (5 ms) 的倍数 | -1

输入接收数据的时间间隔。

当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Parrot Minidrones

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

从主计算机键盘接收按键并输出 ASCII 码

Keyboard Read 模块接收主计算机键盘上任意基本字符的按键，并输出该字符对应的 ASCII 码。

此模块可用于使用 Simulink Support Package for Parrot® Minidrones 创建的 Simulink® 模型中，以使用键盘按键对 Parrot minidrone 执行实时飞行控制。

**注意**

整个 Simulink 模型中只允许有一个 Keyboard Read 模块。可以从该模块的输出信号中引出任意数量的连接。

在 Simulink 模型中，您可以将多个 Compare to Constant 模块连接到 Keyboard Read 模块的输出，以映射不同的 ASCII 码。

在 Simulink 模型开始在无人机上运行后，您可以使用飞行控制界面上的 `Keyboard Control Panel` 键入已映射到控制逻辑的基本字符。
