---
type: simulink-block
title: 'On-board EEPROM Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'onboardeepromread'
documentation_source_path: 'supportpkg/arduino_ref/onboardeepromread.html'
language: zh-CN
chinese_source: worker-translation
---

# On-board EEPROM Read

## 端口

### 输出

### **Data** — 来自 Arduino EEPROM 矩阵的数据

该模块输出其从 Arduino EEPROM 读取的 *N*×1 或 1×*N* 数据矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **起始地址** — EEPROM 起始地址 `1`（默认）| positive integer

输入板载 Arduino EEPROM 的起始内存地址，读取操作必须从此地址开始。

**注意**

所读取数据类型的总大小不得超过从本参数指定的起始地址开始的可寻址板载 Arduino EEPROM 内存位置的最大数量。例如，对于 Arduino Uno 开发板和 `uint8` 输入数据类型，EEPROM 的起始地址不得超过 1021。

### **数据类型** — 要从 EEPROM 读取的数据的数据类型 `uint8`（默认）| `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择要从板载 Arduino EEPROM 读取的数据的数据类型。

### **数据大小 (N)** — 要从 EEPROM 读取的数据大小 `1`（默认）| positive integer

根据 **数据类型** 参数中指定的数据类型，指定要从板载 Arduino EEPROM 读取的数据大小。

### **采样时间** — 模块读取数据的频率 `0.1`（默认）| scalar

指定模块从板载 Arduino EEPROM 读取数据的频率。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从板载 Arduino EEPROM 读取数据

使用 On-board EEPROM Read 模块从板载 Arduino® 电可擦除可编程只读存储器 (EEPROM) 读取非易失性数据。该模块一次从板载 Arduino EEPROM 读取并输出一个字节的数据。

下表列出了这些 Arduino 开发板的板载 EEPROM 的内存大小和可访问地址范围。

| Arduino 开发板 | 板载 EEPROM 大小 | 可访问地址范围 |
| --- | --- | --- |
| Arduino Mega 2560 和 Mega ADK | 4096 bytes | 0 到 4095 |
| Arduino Uno | 1024 bytes | 0 到 1023 |
| Arduino Leonardo | 1024 bytes | 0 到 1023 |
| Arduino Micro | 1024 bytes | 0 到 1023 |
| Arduino Nano 3.0 | 1024 bytes | 0 到 1023 |
