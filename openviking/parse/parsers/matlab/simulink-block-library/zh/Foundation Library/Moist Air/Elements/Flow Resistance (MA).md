---
type: simulink-block
title: 'Flow Resistance (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'flowresistancema'
documentation_source_path: 'ref/flowresistancema.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Resistance (MA)

## 端口

### 守恒端口

### **A** — 入口或出口湿空气

与流动阻力入口或出口相关联的湿空气守恒端口。该模块没有固有的方向性。

### **B** — 入口或出口湿空气

与流动阻力入口或出口相关联的湿空气守恒端口。该模块没有固有的方向性。

## 参数

### **Nominal pressure drop** — 已知工况下的压降 `0.001 MPa`（默认值）

已知工况下从入口到出口的压降。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Nominal mixture mass flow rate** — 已知工况下的质量流量 `0.1 kg/s`（默认值）

已知工况下通过该模块的空气混合物质量流量。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Nominal mixture density** — 已知工况下的密度 `0 kg/m^3`（默认值）

已知工况下流动阻力内部湿空气混合物的质量密度。该模块使用标称参数来计算压降与质量流量之间的比例常数。将此参数设置为零以忽略压降对空气混合物密度的依赖性。

### **Cross-sectional area at ports A and B** — 流动阻力端口处的流通面积 `0.01 m^2`（默认值）

流动阻力端口处的流通面积。假设各端口尺寸相同。

### **Fraction of nominal mixture mass flow rate for laminar flow transition** — 阈值与标称质量流量之比 `1e-3`（默认值）

空气混合物阈值质量流量与标称质量流量之比。该模块使用此参数来设置压降线性化的阈值。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要模拟水滴，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气支路中的通用阻力

Flow Resistance (MA) 模块用于对湿空气网络支路中的通用压降进行建模。压降与混合物流量的平方成正比，与混合物密度成反比。比例常数由模块对话框中指定的额定工况确定。将 **Nominal mixture density** 参数设置为零可忽略密度依赖性。

当拥有通过某个组件的压力损失和流量的经验数据，但缺少详细的几何信息时，可使用此模块。

模块方程使用以下符号。

|  |  |
| --- | --- |
| m˙ | 质量流量 |
| *Φ* | 能量流量 |
| *p* | 压力 |
| *ρ* | 密度 |
| *R* | 比气体常数 |
| *S* | 横截面积 |
| *K* | 比例常数 |
| *h* | 比焓 |
| *T* | 温度 |

下标 `a`、`w`、`d` 和 `g` 分别表示干空气、水蒸气、水滴和微量气体的属性。下标 `A` 和 `B` 表示相应的端口。

质量平衡：

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

能量平衡：

ΦA+ΦB=0

如果 **Nominal mixture density** 参数值 *ρ*nom 大于零，则模块按如下方式计算压降

pA−pB=K1m˙Am˙A2+(flamm˙nom)2RTinpin

其中：

- *f*lam 是层流过渡的额定混合物质量流量分数。
- *p*in 是入口压力（*p*A 或 *p*B，取决于流动方向）。
- *T*in 是入口温度（*T*A 或 *T*B，取决于流动方向）。

比例常数由额定流动条件计算得出

K1=Δpnomρnomm˙nom2

如果 **Nominal mixture density** 参数设置为零，则模块按如下方式计算压降

pA−pB=K2m˙Am˙A2+(flamm˙nom)2

其中比例常数由额定流动条件计算得出

K2=Δpnomm˙nom2

假设流动阻力是绝热的，因此混合物比总焓相等

hA+12(m˙ARTASpA)2=hB+12(m˙BRTBSpB)2

### 假设和限制

- 阻力是绝热的。它不与环境交换热量。
- 假设压降与混合物流量的平方成正比，与混合物密度成反比。
