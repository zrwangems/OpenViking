---
type: simulink-block
title: 'Variable Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableinductor'
documentation_source_path: 'ref/variableinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Inductor

## 端口

### 输入

### **L** — Simulink 控制信号 标量

Simulink 控制信号，指定为标量。

**数据类型：** `double`

## 参数

Variable Inductor 模块没有参数。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**R2016b 中推出**

### R2021b：Variable Inductor 模块图标已更新

从 R2021b 开始，Variable Inductor 模块图标现已更新。当您打开在 R2021b 之前创建的、包含 Variable Capacitor 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

对可变电感器建模

Variable Inductor 模块使用以 henries 为单位的 Simulink® 受控电感来控制 RF Blockset™ 反馈电路的输出。电感的最小值 (*Lmin*) 是由 RF Blockset 定义的常量，与 Simulink 控制信号无关。该模块有两个电气端子。一个端子用于 Simulink 控制信号，另一个端子用于 RF Blockset 信号。
