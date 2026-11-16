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

### 守恒

### **A** — 入口或出口等温液体

与流动阻力的入口或出口关联的等温液体守恒端口。该模块没有固有方向性。

### **B** — 入口或出口等温液体

与流动阻力的入口或出口关联的等温液体守恒端口。该模块没有固有方向性。

## 参数

### **额定压降** — 已知工况下的压降 0.001 MPa（默认）| 正标量

在已知工况下从入口到出口的压降。该模块使用额定参数计算压降与质量流量之间的比例常数。

### **额定质量流量** — 已知工况下的质量流量 0.1 kg/s（默认）| 正标量

在已知工况下通过组件的质量流量。该模块使用额定参数计算压降与质量流量之间的比例常数。

### **层流流动的额定质量流量分数** — 阈值与额定质量流量的比值 1e-3（默认）| [0,1] 范围内的标量

阈值质量流量与额定质量流量的比值。该模块使用此参数计算阈值质量流量——并最终设置压降线性化的限值。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体支路中的通用阻力

Flow Resistance (IL) 模块对等温液体网络支路中的通用压降进行建模。压降与质量流量的平方成正比。比例常数根据模块对话框中指定的额定工况确定。

当组件唯一可用的数据是典型压降和流量时，可使用此模块。此模块适用于表示复杂组件，因为对于此类组件，很难根据几何结构确定理论压力损失。

假定流动阻力内部的流体体积可忽略不计。因此，通过一个端口流入的质量流量必须精确等于通过另一个端口流出的质量流量：

m˙A+m˙B=0,

其中 m˙A 和 m˙B 分别定义为通过端口 **A** 和 **B** 流入组件的质量流量。

假定压降与质量流量的平方成正比。质量流量的平方在零流量附近的小层流区域内线性化，得到

pA−pB=Km˙Am˙A2+m˙lam2,

其中：

- *p*A 和
  *p*B 分别是端口 **A** 和 **B** 处的压力。
- m˙lam 是层流过渡的质量流量阈值。

*K* 是比例常数，

K=Δpnomm˙nom2,

其中 *Δp*nom 是 **额定压降** 参数值，m˙nom 是 **额定质量流量** 参数值。
