---
type: simulink-block
title: 'Switch'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'switch'
documentation_source_path: 'ref/switch.html'
language: zh-CN
chinese_source: worker-translation
---

# Switch

## 端口

### 输入

### **Vctl** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

### **On resistance** — 导通电阻 `10`（默认）| 正标量

开关的导通电阻值，指定为以欧姆为单位的正标量。

### **Off resistance** — 关断电阻 `1e-6`（默认）| 正标量

开关的关断电阻值，指定为以欧姆为单位的正标量。

### **Threshold voltage** — 阈值电压 `0`（默认）| 标量

开关的阈值电压，指定为以伏特为单位的标量。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

Simulink 控制的双端开关

该开关模块对双端开关进行建模。输入 Simulink® 信号 *Vctl* 控制 RF Blockset™ 信号从 `In` 端到 `Out` 端的传输。

如果控制电压小于阈值电压，则该模块使用 **Off resistance** 中指定的电阻值在输入端和输出端之间对信号进行衰减。如果控制电压大于阈值电压，则该模块使用 **On resistance** 中指定的电阻值在输入端和输出端之间传递信号。
