---
type: simulink-block
title: 'Digital Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'digitalinput'
documentation_source_path: 'vexv5/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

### 输出

### **Port\_1** — 从 3-wire 端口读取的逻辑值 0 | 1

从 3-wire 端口读取的逻辑值，以 boolean 值返回。

**数据类型：** `Boolean`

## 参数

### **3-Wire Expander（智能端口）** — 选择 3-Wire Expander 使用的智能端口 `None`（默认）| `1` 到 `21`

如果使用 3-Wire Expander，请指定扩展器连接到的 VEX EDR V5 Robot Brain 上的智能端口。

### **端口** — 选择用于读取逻辑值的 3-wire 端口 A（默认）| `A` 到 `H`

选择 VEX EDR V5 Robot Brain 上要从中读取数字信号的 3-wire 端口。

不要将同一端口分配给同一模型中的多个 Digital Input 模块。

### **采样时间** — 从 3-wire 端口获取值的采样时间 `0.2`（默认）| seconds

指定模块应从 3-wire 端口读取值的频率。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

从 VEX EDR V5 Robot Brain 上的 3-wire 端口读取逻辑值

Digital Input 模块从 VEX® EDR V5 Robot Brain 上选定的 3-wire 端口读取逻辑值。您最多可以使用 VEX EDR V5 Robot Brain 上的八个 3-wire 端口来读取逻辑值。
