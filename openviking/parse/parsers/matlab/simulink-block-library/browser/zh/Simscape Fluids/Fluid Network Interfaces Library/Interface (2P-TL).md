---
type: simulink-block
title: 'Interface (2P-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces Library'
documentation_page: 'interface2ptl'
documentation_source_path: 'ref/interface2ptl.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (2P-TL)

## 端口

### 守恒

### **2P** — 两相端口 两相流体

与接口处的两相流体相关联的两相流体守恒端口。

### **TL** — 流体端口 热液体

与接口处的热液体相关联的热液体守恒端口。

## 参数

### **端口 2P 和 TL 的横截面积** — 端口面积 `0.01` `m^2` (默认) | 正标量

热液体和两相流体端口的横截面积。

### **两相流体过冷液体检查** — 两相流体过冷条件检查 `None` (默认) | `Warning` | `Error`

当端口 **2P** 处的流体不满足过冷条件时要执行的操作。

## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

两相流体和热液体网络接口

Interface (2P-TL) 模块表示两相流体网络与热液体网络之间的流动连接。在接口处，压力、温度和质量流量相等。该模块不跨接口传递各流体网络的流体属性。为保持流体属性一致，确保 Thermal Liquid Properties (TL) 模块和 Two-Phase Fluid Properties (2P) 模块具有相同的设置。

**2P** 端口处的流体必须保持过冷。可以使用 **两相流体过冷液体检查** 参数来选择当流体不满足此条件时该模块执行的操作。

### 质量和动量平衡

该模块满足质量守恒：

m˙TL+m˙2P=0,

其中：

- m˙TL 是流入端口 **TL** 的质量流量。
- m˙2P 是流入端口 **2P** 的质量流量。

端口压力相等：

PTL=P2P.

### 能量平衡

两个流体端口之间的温度恒定。该模块按如下方式计算接口处的能量平衡：

ΦTL+Φ2P=m˙TLuTL+pTLvTL+wTL22+m˙2Pu2P+p2Pv2P+w2P22,

其中：

- *ΦTL* 是流入端口 **TL** 的能量流率。
- *Φ2P* 是流入端口 **2P** 的能量流率。
- *hTL* 是端口 **TL** 处的比内能。
- *h2P* 是端口 **2P** 处的比内能。
- *vTL* 是端口 **TL** 处的比容。
- *v2P* 是端口 **2P** 处的比容。
- *wTL* 是端口 **TL** 处的流速

  wTL=m˙TLvTLS,
- *w2P* 是端口 **2P** 处的流速

  w2P=m˙2Pv2PS.
- *S* 是 **端口 2P 和 TL 的横截面积** 参数的值。
