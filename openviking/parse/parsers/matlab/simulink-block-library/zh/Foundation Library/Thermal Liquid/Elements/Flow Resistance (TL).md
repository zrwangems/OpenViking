---
type: simulink-block
title: 'Flow Resistance (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'flowresistancetl'
documentation_source_path: 'ref/flowresistancetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Resistance (TL)

## 端口

### 守恒

### **A** — 热液体流动阻力端口

热液体通过该端口进入或离开流动阻力。

### **B** — 热液体流动阻力端口

热液体通过该端口进入或离开流动阻力。

## 参数

### **标称压降** — 已知工况下的压降 0.001 MPa（默认值）

已知工况下从入口到出口的压降。模块使用标称参数计算压降与质量流量之间的比例常数。

### **标称质量流量** — 已知工况下的质量流量 0.1 kg/s（默认值）

已知工况下通过组件的质量流量。模块使用标称参数计算压降与质量流量之间的比例常数。

### **端口 A 和 B 处的横截面积** — 流动阻力端口处的流通面积 0.01 m^2（默认值）

流动阻力端口处的流通面积。假定这些端口的尺寸相同。

### **层流流动的标称质量流量分数** — 阈值与标称质量流量的比率 1e-3（默认值）

阈值质量流量与标称质量流量的比率。模块使用此参数计算阈值质量流量——并最终设置压降的线性化限值。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

热液体支路中的通用阻力

Flow Resistance (TL) 模块对热液体网络支路中的一般压降进行建模。压降与质量流量的平方成正比。比例常数由模块对话框中指定的标称工况确定。

当组件唯一可用的数据是典型压降和流量时，可使用此模块。此模块可用于表示复杂组件，在这些组件中很难根据几何形状确定理论压力损失。

### 质量平衡

流动阻力内部流体的体积假定可忽略不计。因此，通过一个端口流入的质量流量必须精确等于通过另一个端口流出的质量流量：

m˙A+m˙B=0,

其中 m˙A 和 m˙B 分别定义为通过端口 **A** 和 **B** 流入组件的质量流量。

### 能量平衡

能量只能通过热液体端口进入和离开流动阻力。壁面与环境之间不发生热交换。此外，不对流体做功，也不由流体做功。因此，通过一个端口流入的能量流率必须精确等于通过另一个端口流出的能量流率：

ϕA+ϕB=0,

其中 *ϕ*A 和 *ϕ*B 是通过端口 **A** 和 **B** 流入流动阻力的能量流率。

### 动量平衡

假定压降与质量流量的平方成正比。质量流量的平方在零流量附近的微小层流区域中线性化，得到

pA−pB=Km˙Am˙A2+m˙lam2,

其中：

- *p*A 和 *p*B 分别是端口 **A** 和 **B** 处的压力。
- m˙lam 是层流过渡的质量流量阈值。

*K* 是比例常数，

K=Δpnomm˙nom2,

其中 *Δp*nom 是 **标称压降** 参数值，m˙nom 是 **标称质量流量** 参数值。
