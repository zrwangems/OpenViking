---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'analoginput'
documentation_source_path: 'vexv5/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Port\_1** — 从 3-wire 端口读取的模拟值 [0 4095]

从 3-wire 端口读取的模拟值，以 double 返回。

**数据类型：** `double`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 所使用的 smart port `None`（默认）| `1` 至 `21`

如果使用 3-Wire Expander，请指定 VEX EDR V5 Robot Brain 上扩展器所连接的 smart port。

### **Port** — 选择要读取模拟值的 3-wire 端口 A（默认）

选择 VEX EDR V5 Robot Brain 上要从中读取模拟值的 3-wire 端口。

不要在同一模型中将同一端口分配给多个 Analog Input 模块。

### **Sample time** — 从 3-wire 端口获取值的采样时间 `0.2`（默认）| seconds

指定模块从 3-wire 端口读取值的频率。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

从 VEX EDR V5 Robot Brain 上的 3-wire 端口读取模拟值

Analog Input 模块从 VEX® EDR V5 Robot Brain 上选定的 3-wire 端口读取模拟值。使用该模块测量连接到 3-wire 端口的传感器（电压）的输出，例如电位器。12-bit 传感器值的范围为 0 至 4095，对应 0V 至 5V 的输入电压。在 VEX EDR V5 Robot Brain 上最多可以使用八个 3-wire 端口。
