---
type: simulink-block
title: 'Local Restriction (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'localrestrictionil'
documentation_source_path: 'ref/localrestrictionil.html'
language: zh-CN
chinese_source: worker-translation
---

# Local Restriction (IL)

## 端口

### 输入

### **AR** — 限制面积控制信号，m^2 物理信号

用于控制流动限制面积的输入物理信号。当信号值超出模块参数指定的最小和最大限制面积限制时，该信号饱和。

#### 依赖关系

仅当您将 **Restriction type** 参数设置为 `Variable` 时，此端口可见。

### 守恒

### **A** — 入口或出口等温液体

与局部限制的入口或出口关联的等温液体守恒端口。此模块没有固有方向性。

### **B** — 入口或出口等温液体

与局部限制的入口或出口关联的等温液体守恒端口。此模块没有固有方向性。

## 参数

### **Restriction type** — 指定限制面积在仿真期间是否可以变化 `Variable` （默认） | `Fixed`

选择限制面积在仿真期间是否可以变化：

- `Variable` — 端口 **AR** 处的输入物理信号指定限制面积，该面积可在仿真期间变化。**Minimum restriction area** 和 **Maximum restriction area** 参数指定限制面积的下限和上限。
- `Fixed` — 由 **Restriction area** 模块参数值指定的限制面积在仿真期间保持恒定。端口 **AR** 隐藏。

### **Minimum restriction area** — 限制横截面积的下限 `1e-10 m^2` （默认） | 正标量

限制横截面积的下限。您可以使用此参数表示泄漏面积。输入信号 AR 在此值处饱和，以防止限制面积进一步减小。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Maximum restriction area** — 限制横截面积的上限 `0.005 m^2` （默认） | 正标量

限制横截面积的上限。输入信号 AR 在此值处饱和，以防止限制面积进一步增大。

#### 依赖关系

当 **Restriction type** 参数设置为 `Variable` 时启用。

### **Restriction area** — 限制处垂直于流路的面积 `1e-3 m^2` （默认） | 正标量

限制处垂直于流路的面积。

#### 依赖关系

当 **Restriction type** 参数设置为 `Fixed` 时启用。

### **Cross-sectional area at ports A and B** — 端口处垂直于流路的面积 `inf m^2` （默认） | 正标量

端口 **A** 和 **B** 处垂直于流路的面积。假设两个端口的该面积相同。`inf` 值假设端口处的横截面积远大于限制面积，因此模块方程中的所有 *S*R/*S* 项均可忽略不计。

### **Discharge coefficient** — 通过限制的实际质量流量与理论质量流量之比 `0.64` （默认） | 正标量

流量系数是一个半经验参数，通常用于表征孔口的流通能力。该参数定义为通过孔口的实际质量流量与理想质量流量之比。

### **Critical Reynolds number** — 层流与湍流状态之间转换的雷诺数 `150` （默认） | 正标量

层流与湍流状态之间转换的雷诺数。

### **Pressure recovery** — 指定是否考虑压力恢复 `Off` （默认） | `On`

选中该复选框以考虑局部限制出口处的压力恢复。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的流通面积限制

Local Restriction (IL) 模块对等温液体网络中由于流通面积局部减小（例如阀门或孔口）引起的压降进行建模。

端口 **A** 和 **B** 表示限制的入口和出口。端口 **AR** 处的输入物理信号指定限制面积。或者，您可以将固定限制面积指定为模块参数。

模块图标根据 **Restriction type** 参数的值而变化。

| 限制类型 | 模块图标 |
| --- | --- |
| `Variable` |  |
| `Fixed` |  |

该限制是绝热的。它不与环境交换热量。

该限制由流通面积的收缩和随后的突然扩张组成。流体在收缩期间加速，导致压力下降。在扩张区域中，如果清除 **Pressure recovery** 复选框，则加速流体的动量会损失。如果选中 **Pressure recovery** 复选框，则突然扩张会恢复部分动量，并允许压力在限制之后略微上升。

**局部限制示意图**

模块方程以端口 **A** 和 **B** 之间的压差表示质量流量：

m˙A+m˙B=0m˙A=CdSRΔp(Δp2+Δpcr2)1/42ρ¯PRloss(1−(SRS)2)Δp=pA−pBΔpcr=π4⋅ρ¯2SR(RecrνatmCd)2

ρ¯=ρA+ρB2

其中：

- *Δp* 是压差。
- *p*A 和
  *p*B 分别是端口
  **A** 和 **B** 处的压力。
- *S*R 是限制处的横截面积。
- *S* 是端口 **A** 和
  **B** 处的横截面积。
- *Δp*cr 是层流与湍流流态之间转换的临界压差。
- *Re*cr 是临界雷诺数。
- *ν*atm 是大气压力下的液体运动粘度，它是由连接到回路的 Isothermal Liquid Properties (IL) 模块定义的全局参数。
- *C*d 是流量系数。
- ρ¯ 是平均流体混合物密度。
- *ρ*A 和
  *ρ*B 分别是端口
  **A** 和 **B** 处的流体混合物密度值。用于计算流体混合物密度的方程取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。
- *PR*loss 是压力损失比。

压力损失比 *PR*loss 取决于 **Pressure recovery** 复选框：

- 如果压力恢复为 off，则

  PRloss=1.
- 如果压力恢复为 on，则

  PRloss=1−(SRS)2(1−Cd2)−CdSRS1−(SRS)2(1−Cd2)+CdSRS.

限制处的横截面积 *S*R，
取决于 **Restriction type** 参数值：

- 对于可变限制，

  SR={Smin,AR≤SminSmax,AR≥SmaxAR,Smin<AR<Smax,

  其中 *AR* 是输入物理信号的值，*S*min 和
  *S*max 分别是 **Minimum restriction area** 和 **Maximum restriction area** 模块参数的值。
- 对于固定限制，*S*R 是 **Restriction area** 参数的值。

默认情况下，模块假设限制端口处的横截面积远大于限制面积，将 **Cross-sectional area at ports A and B** 参数值设置为 `inf`，并将方程中的所有 *S*R/*S* 项设置为 0，以提高计算效率。如果两个横截面积大小相当且其比率对流量计算有影响，请为 **Cross-sectional area at ports A and B** 参数指定实际值。
