---
type: simulink-block
title: 'Host Serial Setup'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Protection and Diagnostics'
documentation_page: 'hostserialsetup'
documentation_source_path: 'ref/hostserialsetup.html'
language: zh-CN
chinese_source: official
---

# Host Serial Setup

## 端口

R2025b 官方文档未提供。

## 参数

### **端口名称** — 要配置的端口 **'Please\_select\_a\_port'** (默认) | **'COM3'**

选择一个要配置的可用串行端口。默认情况下未选择任何端口，此字段显示的是 **'Please\_select\_a\_port'**。请使用 Host Serial Transmit 和 Host Serial Receive 模块中的一个已配置端口。传输模块和接收模块都必须使用一个通过 Host Serial Setup 模块配置的串行端口。

### **波特率** — 串行通信的波特率 `115200` (默认) | 标量

输入模型通过串行接口传输位的速率。

### **停止位数** — 停止位数 **1** (默认) | **2**

输入模型用于指示字节结尾的位数。

### **奇偶校验模式** — 用于检查奇偶校验位的方法 **无** (默认) | **奇数** | **偶数**

指定您要如何检查模型通过串行端口传输的数据位中的奇偶校验位。

- **无** - 模型不执行奇偶校验检查。
- **奇数** - 如果给定的一组位中 1 的数量为偶数，则模型会将奇偶校验位设置为 0。
- **偶数** - 如果给定的一组位中 1 的数量为奇数，则模型会将奇偶校验位设置为 1。

### **超时** — 单向通信超时前的时间间隔 `1.0` (默认) | 标量

输入大于或等于零的值（以秒为单位）。当涉及的 COM 端口使用协议模式时，此值表示传输端等待接收端确认的时间，或接收端等待数据的时间。

当传输模块或接收模块超出 *n* 秒的**超时**值时，系统将每隔 *n* 秒显示一条警告消息。

### **字节顺序** — 串行通信的字节顺序 **LittleEndian** (默认) | **BigEndian**

将字节顺序指定为 **LittleEndian** 或 **BigEndian**。如果字节顺序为 **LittleEndian**，则模型将第一个字节存储在第一个内存地址中。如果字节顺序为 **BigEndian**，则模型将最后一个字节存储在第一个内存地址中。在执行读取或写入操作之前，您应将字节顺序配置为适当的值。

## 所属库

Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

配置 Host Serial Receive 和 Host Serial Transmit 模块使用的通信端口

Host Serial Setup 是一个独立模块，用于标准化 Host Serial Receive 和 Host Serial Transmit 模块所使用的串行通信 (COM) 端口设置。

使用 Host Serial Setup 模块以全局方式设置 COM 端口配置可以避免冲突。例如，Host Serial Transmit 模块无法使用与 Host Serial Receive 模块 COM1 端口设置不同的 COM1 端口。您只需为每个 COM 端口设置一次端口配置。
