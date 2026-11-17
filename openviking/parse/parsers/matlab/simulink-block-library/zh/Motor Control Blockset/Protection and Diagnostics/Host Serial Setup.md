---
type: simulink-block
title: 'Host Serial Setup'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialsetup'
documentation_source_path: 'ref/hostserialsetup.html'
language: zh-CN
chinese_source: worker-translation
---

# Host Serial Setup

## 端口

R2025b 中未记录。

## 参数

### **Port name** — 要配置的端口 `'Please_select_a_port'`（默认）| `'COM3'`

选择要配置的可用串行端口。默认情况下未选择端口，此字段显示 `'Please_select_a_port'`。在 Host Serial Transmit 和 Host Serial Receive 模块中使用已配置的端口。发送和接收模块都必须使用通过 Host Serial Setup 模块配置的串行端口。

### **Baud rate** — 串行通信的波特率 `115200`（默认）| 标量

输入模型通过串行接口传输位的速率。

### **Number of stop bits** — 停止位的数量 `1`（默认）| `2`

输入模型用于指示字节结束的位数。

### **Parity mode** — 用于校验奇偶校验位的方法 `none`（默认）| `odd` | `even`

指定希望如何校验模型通过串行端口传输的数据位中的奇偶校验位。

- `none` — 模型不执行奇偶校验。
- `odd` — 如果给定一组位中 1 的个数为偶数，则模型将奇偶校验位设置为 0。
- `even` — 如果给定一组位中 1 的个数为奇数，则模型将奇偶校验位设置为 1。

### **Timeout** — 单向通信超时前的时间间隔 `1.0`（默认）| 标量

输入大于或等于零的值（秒）。当所涉及的 COM 端口使用协议模式时，此值表示发送方等待接收方确认的时间，或接收方等待数据的时间。

当发送或接收模块超过 *n* 秒的 **Timeout** 值时，系统每隔 *n* 秒显示一条警告消息。

### **Byte order** — 串行通信的字节顺序 `LittleEndian`（默认）| `BigEndian`

将字节顺序指定为 `LittleEndian` 或 `BigEndian`。如果字节顺序为 `LittleEndian`，则模型将第一个字节存储在第一内存地址中。如果字节顺序为 `BigEndian`，则模型将最后一个字节存储在第一内存地址中。在执行读取或写入操作之前，应将字节顺序配置为适当的值。

## 所属库

Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

配置 Host Serial Receive 和 Host Serial Transmit 模块使用的通信端口

Host Serial Setup 模块是一个独立模块，用于标准化 Host Serial Receive 和 Host Serial Transmit 模块使用的串行通信（COM）端口设置。

通过使用 Host Serial Setup 模块全局设置 COM 端口配置可以避免冲突。例如，Host Serial Transmit 模块无法使用设置与 Host Serial Receive 模块的 COM1 端口不同的 COM1 端口。每个 COM 端口只需设置一次端口配置。
