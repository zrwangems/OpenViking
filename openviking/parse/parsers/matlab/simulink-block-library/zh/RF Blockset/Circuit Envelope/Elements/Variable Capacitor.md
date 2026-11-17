---
type: simulink-block
title: 'Variable Capacitor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variablecapacitor'
documentation_source_path: 'ref/variablecapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Capacitor

## 端口

### 输入

### **C** — Simulink 控制信号标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

Variable Capacitor 模块没有参数。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

### R2021b：Variable Capacitor 模块图标已更新

从 R2021b 开始，Variable Capacitor 模块图标现已更新。当您打开在 R2021b 之前创建的包含 Variable Capacitor 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

建模可变电容器

Variable Capacitor 模块使用 Simulink® 控制的电容（以法拉为单位）来控制 RF Blockset™ 反馈电路的输出。电容的最小值（*Cmin*）是 RF Blockset 定义的常数，与 Simulink 控制信号无关。该模块有两个电气端子。一个端子用于 Simulink 控制信号，一个端子用于 RF Blockset 信号。
