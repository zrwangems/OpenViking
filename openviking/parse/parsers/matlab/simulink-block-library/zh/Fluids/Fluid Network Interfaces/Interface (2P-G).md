---
type: simulink-block
title: 'Interface (2P-G)'
family: 'hydro'
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
```yaml
ports:
- name: 2P
  summary: 两相端口 两相流体
  direction: conserving
- name: G
  summary: 流体端口 气体
  direction: conserving
```

### 守恒端口

### **2P** — 两相端口 两相流体

与界面处两相流体相关联的两相流体守恒端口。

### **G** — 流体端口 气体

与界面处气体相关联的气体守恒端口。
## 参数
```yaml
parameters:
- name: 端口 2P 和 G 的横截面积
  summary: 端口面积 0.01 m^2（默认）| 正标量
  group: ''
- name: 两相流体过热蒸汽检查
  summary: 两相流体过热条件检查 None（默认）| Warning | Error
  group: ''
```

### **端口 2P 和 G 的横截面积** — 端口面积 `0.01` `m^2`（默认）| 正标量

两相流体端口和气体端口的横截面积。

### **两相流体过热蒸汽检查** — 两相流体过热条件检查 `None`（默认）| `Warning` | `Error`

当端口 **2P** 处的流体不满足过热条件时要执行的操作。
## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

两相流体和气体网络接口

Interface (2P-G) 模块表示两相流体网络与气体网络之间的流动连接。界面处的压力、温度和質量流量相等。该模块不会在界面处传递各流体网络的流体属性。为保持流体属性守恒，请确保 Gas Properties (G) 模块和 Two-Phase Fluid Properties (2P) 模块具有相应的设置。

**2P** 端口处的流体必须保持过热状态。您可以使用 **Two-phase fluid superheated vapor check** 参数来选择当流体不满足此条件时模块执行的操作。

### 质量和动量平衡

该模块守恒质量，使得

m˙2P+m˙G=0，

其中：

- m˙G 是流入端口 **G** 的质量流量。
- m˙2P 是流入端口 **2P** 的质量流量。

端口压力相等：

PG=P2P。

### 能量平衡

两个流体端口之间的温度恒定。该模块计算界面上的能量平衡为

ΦG+Φ2P=m˙GhG+wG22+m˙2Ph2P+w2P22，

其中：

- *ΦG* 是流入端口 **G** 的能量流量。
- *Φ2P* 是流入端口 **2P** 的能量流量。
- *hG* 是端口 **G** 处的比焓。
- *h2P* 是端口 **2P** 处的比焓。
- *vG* 是端口 **G** 处的比体积。
- *v2P* 是端口 **2P** 处的比体积。
- *wG* 是端口 **G** 处的流速，使得

  wG=m˙GvGS，

  其中 *S* 是 **Cross-sectional area at ports 2P and G** 参数的值。
- *w2P* 是端口 **2P** 处的流速，使得

  w2P=m˙2Pv2PS。
