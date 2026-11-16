---
type: simulink-block
title: 'Variable Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Simulink Controlled Elements'
documentation_page: 'variableinductor'
documentation_source_path: 'ref/variableinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Inductor

## 端口

### 输入

### **L** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

在 R2025b 中未记载。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

在 R2025b 中未记载。

## 扩展功能

在 R2025b 中未记载。

## 版本历史

**在 R2016b 中引入**

### R2021b：Variable Inductor 模块图标已更新

从 R2021b 开始，Variable Inductor 模块图标现已更新。当您打开在 R2021b 之前创建的包含 Variable Capacitor 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

对可变电感器建模

Variable Inductor 模块使用 Simulink® 控制电感（以 henries 为单位）来控制 RF Blockset™ 反馈电路的输出。电感的最小值 (*Lmin*) 是由 RF Blockset 定义的常量，与 Simulink 控制信号无关。该模块有两个电气端子。一个端子用于 Simulink 控制信号，另一个端子用于 RF Blockset 信号。
