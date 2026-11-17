---
type: simulink-block
title: 'Interface (2P-G)'
family: 'fluid-network-interfaces'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interface2pg'
documentation_source_path: 'ref/interface2pg.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (2P-G)

## 端口

### 守恒端口

### **2P** — 两相端口，两相流体

与接口处的两相流体关联的两相流体守恒端口。

### **G** — 流体端口，气体

与接口处的气体关联的气体守恒端口。

## 参数

### **端口 2P 和 G 的横截面积** — 端口面积 `0.01` `m^2` (默认) | 正标量

两相流体和气体端口的横截面积。

### **两相流体过热蒸气检查** — 两相流体过热条件检查 `None` (默认) | `Warning` | `Error`

当端口 **2P** 处的流体不满足过热条件时要执行的操作。

## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

两相流体和气体网络接口

Interface (2P-G) 模块表示两相流体网络和气体网络之间的流动连接。压力、温度和质量流量在接口处相等。该模块不会跨接口传递每个流体网络的流体属性。为守恒流体属性，确保 Gas Properties (G) 模块和 Two-Phase Fluid Properties (2P) 模块具有相对应的设置。

端口 **2P** 处的流体必须保持过热。如果流体不满足此条件，可以使用 **两相流体过热蒸气检查** 参数来选择该模块执行的操作。

### 质量和动量平衡

该模块守恒质量，使得

m˙2P+m˙G=0,

其中：

- m˙G 是流入端口
  **G** 的质量流量。
- m˙2P 是流入端口
  **2P** 的质量流量。

端口压力相等：

PG=P2P.

### 能量平衡

温度在两个流体端口之间保持恒定。该模块计算接口处的能量平衡如下：

ΦG+Φ2P=m˙GhG+wG22+m˙2Ph2P+w2P22,

其中：

- *ΦG* 是流入端口 **G** 的能量流量。
- *Φ2P* 是流入端口 **2P** 的能量流量。
- *hG* 是端口 **G** 处的比焓。
- *h2P* 是端口 **2P** 处的比焓。
- *vG* 是端口 **G** 处的比体积。
- *v2P* 是端口 **2P** 处的比体积。
- *wG* 是端口 **G** 处的流速，使得

  wG=m˙GvGS,

  其中 *S* 是
  **端口 2P 和 G 的横截面积**
  参数的值。
- *w2P* 是端口 **2P** 处的流速，使得

  w2P=m˙2Pv2PS.
