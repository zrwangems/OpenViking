---
type: simulink-block
title: 'Flow Resistance (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'flowresistanceil'
documentation_source_path: 'ref/flowresistanceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Resistance (IL)

## 端口
```yaml
ports:
- name: A
  summary: 入口或出口等温液体
  direction: unspecified
- name: B
  summary: 入口或出口等温液体
  direction: unspecified
```

### 守恒

### **A** — 入口或出口等温液体

与流动阻力入口或出口相关联的等温液体守恒端口。该模块没有固有方向性。

### **B** — 入口或出口等温液体

与流动阻力入口或出口相关联的等温液体守恒端口。该模块没有固有方向性。
## 参数
```yaml
parameters:
- name: Nominal pressure drop
  summary: 已知工况下的压降 0.001 MPa（默认）| 正标量
  group: ''
- name: Nominal mass flow rate
  summary: 已知工况下的质量流量 0.1 kg/s（默认）| 正标量
  group: ''
- name: Fraction of nominal mass flow rate for laminar flow
  summary: 阈值与标称质量流量之比 1e-3（默认）| [0,1] 范围内的标量
  group: ''
```

### **Nominal pressure drop** — 已知工况下的压降 0.001 MPa（默认）| 正标量

已知工况下从入口到出口的压降。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Nominal mass flow rate** — 已知工况下的质量流量 0.1 kg/s（默认）| 正标量

已知工况下通过组件的质量流量。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Fraction of nominal mass flow rate for laminar flow** — 阈值与标称质量流量之比 1e-3（默认）| [0,1] 范围内的标量

阈值质量流量与标称质量流量之比。该模块使用此参数计算阈值质量流量——并最终确定压降的线性化限值。
## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体支路中的通用阻力

Flow Resistance (IL) 模块对等温液体网络支路中的通用压降进行建模。压降与质量流量的平方成正比。比例常数由模块对话框中指定的标称工况确定。

当组件唯一可用的数据是典型压降和流量时，请使用此模块。该模块适用于表示复杂组件，即难以根据几何形状确定理论压力损失的情况。

假设流动阻力内部的流体体积可忽略不计。则通过一个端口流入的质量流量必须恰好等于通过另一个端口流出的质量流量：

m˙A+m˙B=0，

其中 m˙A 和 m˙B 分别定义为通过端口 **A** 和 **B** 流入组件的质量流量。

假设压降与质量流量的平方成正比。质量流量的平方在零流量附近的小层流区域内线性化，结果为

pA−pB=Km˙Am˙A2+m˙lam2，

其中：

- *p*A 和 *p*B 分别是端口 **A** 和 **B** 处的压力。
- m˙lam 是层流过渡的质量流量阈值。

*K* 是比例常数，

K=Δpnomm˙nom2，

其中 *Δp*nom 是 **Nominal pressure drop** 参数值，m˙nom 是 **Nominal mass flow rate** 参数值。
