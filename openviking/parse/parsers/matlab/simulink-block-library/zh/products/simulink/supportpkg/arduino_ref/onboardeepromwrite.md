---
type: simulink-block
title: 'On-board EEPROM Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'onboardeepromwrite'
documentation_source_path: 'supportpkg/arduino_ref/onboardeepromwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# On-board EEPROM Write

## 端口

### 输入

### **Data** — 要写入 Arduino EEPROM 的数据矩阵

该模块输入一个 *N*×1 或 1×*N* 的数据矩阵，该矩阵会被写入 Arduino EEPROM。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Write enable** — 使能 Arduino EEPROM 写操作的正非零值

该模块输入一个正非零值，以允许在板载 Arduino EEPROM 上执行写操作。

**数据类型：** `Boolean`

## 参数

### **Start address** — EEPROM 起始地址 `1`（默认）| 正整数

输入板载 Arduino EEPROM 的起始内存地址，写操作必须从该地址开始。

**注意**

输入数据类型的总大小不得超过从该参数指定的起始地址开始的可寻址板载 Arduino EEPROM 内存位置的最大数量。例如，对于 Arduino Uno 板和 `uint8` 输入数据类型，EEPROM 的起始地址不得超过 1021。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

将数据写入板载 Arduino EEPROM

使用 On-board EEPROM Write 模块将非易失性数据写入板载 Arduino® 电可擦除可编程只读存储器（EEPROM）。EEPROM 上的每个内存位置可存储一个 byte 的数据。该模块比较 Arduino 板载 EEPROM 上的现有数据，仅在数据发生变化时写入。

下表列出了这些 Arduino 板的板载 EEPROM 的内存大小和可访问地址范围。

| Arduino 板 | 板载 EEPROM 大小 | 可访问地址范围 |
| --- | --- | --- |
| Arduino Mega 2560 和 Mega ADK | 4096 bytes | 0 到 4095 |
| Arduino Uno | 1024 bytes | 0 到 1023 |
| Arduino Leonardo | 1024 bytes | 0 到 1023 |
| Arduino Micro | 1024 bytes | 0 到 1023 |
| Arduino Nano 3.0 | 1024 bytes | 0 到 1023 |
