---
type: simulink-block
title: 'DBPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'dbpskmodulatorbaseband'
documentation_source_path: 'ref/dbpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DBPSK Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为元素值为 `0` 或 `1` 的标量或向量。有关详细信息，请参阅支持的数据类型。

此端口在模块上未命名。

**数据类型:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — DBPSK 调制基带信号 标量 | 列向量

DBPSK 调制基带信号，以复数值标量或列向量形式返回。

此端口在模块上未命名。

**数据类型:** `double` | `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡中，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **相位旋转 (rad)** — 附加相位偏移 `0` (默认) | 标量

前一个和当前已调制符号之间的附加相位偏移，以弧度为单位，指定为标量。当输入为零时，此值对应于前一个和当前已调制符号之间的相位差。

**示例:** `pi/4`

### **输出数据类型** — 输出数据类型 `double` (默认) | `single`

输出数据类型，指定为 `double` 或 `single`。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用差分二进制相移键控方法进行调制

DBPSK Modulator Baseband 模块使用差分二进制相移键控 (DBPSK) 方法对信号进行调制。输出是已调制信号的基带表示。有关详细信息，请参阅算法。
