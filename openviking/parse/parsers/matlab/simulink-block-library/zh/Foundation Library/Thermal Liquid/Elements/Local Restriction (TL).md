---
type: simulink-block
title: 'Local Restriction (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'localrestrictiontl'
documentation_source_path: 'ref/localrestrictiontl.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Restriction (TL)

## 端口

### 输入

### **AR** — 限制面积控制信号，m^2 物理信号

控制流动限制面积的输入物理信号。当其值超出模块参数指定的最小和最大限制面积限值时，信号会饱和。

#### 依赖关系

仅当您将 **Restriction type** 参数设置为 `Variable` 时，此端口可见。

### 守恒

### **A** — 入口或出口热液体

与局部限制的入口或出口关联的热液体守恒端口。此模块没有固有方向性。

### **B** — 入口或出口热液体

与局部限制的入口或出口关联的热液体守恒端口。此模块没有固有方向性。

## 参数

### **Restriction type** — 指定限制面积是否可以在仿真期间变化 `Variable`（默认）| `Fixed`

选择限制面积是否可以在仿真期间变化：

- `Variable` — 端口 **AR** 处的输入物理信号指定限制面积，该面积可以在仿真期间变化。**Minimum restriction area** 和 **Maximum restriction area** 参数指定限制面积的下限和上限。
- `Fixed` — 由 **Restriction area** 模块参数值指定的限制面积在仿真期间保持恒定。端口 **AR** 隐藏。

### **Minimum restriction area** — 限制横截面积的下限 `1e-10 m^2`（默认）

限制横截面积的下限。您可以使用此参数表示泄漏面积。输入信号 AR 在此值处饱和，以防止限制面积进一步减小。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Maximum restriction area** — 限制横截面积的上限 `0.005 m^2`（默认）

限制横截面积的上限。输入信号 AR 在此值处饱和，以防止限制面积进一步增大。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Restriction area** — 限制处垂直于流路的面积 `1e-3 m^2`（默认）

限制处垂直于流路的面积。

#### 依赖关系

当 **Restriction type** 参数设置为 `Fixed` 时启用。

### **Cross-sectional area at ports A and B** — 端口处垂直于流路的面积 `0.01 m^2`（默认）

端口 **A** 和 **B** 处垂直于流路的面积。假定两个端口的该面积相同。

### **Discharge coefficient** — 通过限制的实际质量流量与理论质量流量之比 `0.64`（默认）

流量系数是一个半经验参数，通常用于表征孔口的流通能力。此参数定义为通过孔口的实际质量流量与理想质量流量之比。

### **Pressure recovery** — 指定是否考虑压力恢复 `On`（默认）| `Off`

选中此复选框可考虑局部限制出口处的压力恢复。

### **Critical Reynolds number** — 层流和湍流状态之间过渡的雷诺数 `12`（默认）

层流和湍流状态之间过渡的雷诺数。默认值对应锐边孔口。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

热液体网络中的流动面积限制

Local Restriction (TL) 模块对热液体网络中因局部流动面积减小（例如阀门或孔口）而产生的压降进行建模。

端口 **A** 和 **B** 表示限制的入口和出口。端口 **AR** 处的输入物理信号指定限制面积。或者，您可以将固定限制面积指定为模块参数。

模块图标根据 **Restriction type** 参数的值而变化。

| 限制类型 | 模块图标 |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

限制是绝热的。它不与环境交换热量。

限制由流动面积的收缩以及随后的突然扩张组成。流体在收缩期间加速，导致压力下降。在扩张区域，如果清除 **Pressure recovery** 复选框，则加速流体的动量损失。如果选中 **Pressure recovery** 复选框，则突然扩张会恢复部分动量，并允许压力在限制之后略微上升。

**局部限制示意图**

### 质量平衡

限制中的质量平衡为

0=m˙A+m˙B,

其中：

- m˙A 是通过端口 **A** 进入限制的质量流量。
- m˙B 是通过端口 **B** 进入限制的质量流量。

### 动量平衡

端口 **A** 和 **B** 之间的压差由限制中的动量平衡得出：

Δp=ρ2(1−SR2S2)vRvR2+vRc2vR=m˙ACdρSRvRc=RecμCdρπ4SR

其中：

- *Δp* 是压差。
- *ρ* 是液体密度。
- *μ* 是液体动力粘度。
- *S* 是端口 **A** 和 **B** 处的横截面积。
- *S*R 是限制处的横截面积。
- *v*R 是限制处的流体速度。
- *v*Rc 是临界流体速度。
- *Re*c 是临界雷诺数。
- *C*d 是流量系数。

如果压力恢复关闭，则

pA−pB=Δp,

其中：

- *p*A 是端口 **A** 处的压力。
- *p*B 是端口 **B** 处的压力。

如果压力恢复开启，则

pA−pB=Δp1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

### 能量平衡

限制中的能量平衡为

ϕA+ϕB=0,

其中：

- *ϕ*A 是通过端口 **A** 进入限制的能量流率。
- *ϕ*B 是通过端口 **B** 进入限制的能量流率。

### 假设和限制

- 限制是绝热的。它不与周围环境交换热量。
- 限制中液体的动态可压缩性和热容量可忽略不计。
