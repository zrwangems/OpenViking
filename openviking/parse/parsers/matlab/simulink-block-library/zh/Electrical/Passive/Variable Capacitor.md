---
type: simulink-block
title: 'Variable Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'variablecapacitor'
documentation_source_path: 'ref/variablecapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Capacitor

## 端口

### 输入

### **C** — 电容物理信号

与电容关联的物理信号输入端口。C 必须为有限值且大于零
### 守恒

### **+** — 正极端子电气

与电容器正电压关联的电气守恒端口。

### **-** — 负极端子电气

与电容器负电压关联的电气守恒端口。

## 参数

### **Equation** — 模块电容方程 `I = C*dV/dt`（默认）| `I = C*dV/dt + dC/dt*V`

为模块电容选择以下选项之一：

- `I = C*dV/dt` — 此方程假设电容定义为给定电压下电荷-电压曲线的局部梯度。此选项为默认值。
- `I = C*dV/dt + dC/dt*V` — 此方程假设电容定义为电荷与稳态电压之比。

### **Minimum capacitance C>0** — 最小电容 `1e-9` `F`（默认）

端口 C 处信号值的下限。此限制可防止信号达到无物理意义的值。默认值为 `1e-09` F。

### **Series resistance** — 串联电阻 `1e-6` `Ohm`（默认）

与可变电容器串联的电阻值。默认值为 `1e-06` Ohm。

### **Initial voltage** — 初始输出电压 `0` `V`（默认）

仿真开始时的输出电压。

#### 依赖关系

仅当为 **Equation** 参数选择 `I =
C*dV/dt` 时，此参数才可见。

### **Initial charge** — 初始电荷 `0` `C`（默认）

仿真开始时的电荷。

#### 依赖关系

仅当为 **Equation** 参数选择 `I =
C*dV/dt + dC/dt*V` 时，此参数才可见。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

线性时变电容器

Variable Capacitor 模块表示线性时变电容器。当端口 **C** 处的电容为 *C* 时，该模块为通过电容器的电流 *i* 与器件两端电压 *v* 之间的关系提供两种选项。**Equation** 参数决定该模块使用以下哪个方程：

- i=Cdvdt

  当电容定义为给定电压下电荷-电压曲线的局部梯度时，使用上述方程：

  C(v)=dQ(v)dv
- i=dCdtv+Cdvdt

  当电容定义为电荷 *Q* 与稳态电压之比时，使用上述方程：

  C(v)=Q(v)v

该模块包含一个与可变电容器串联的电阻器。您可以使用此电阻器表示电容器的总欧姆连接电阻。在某些电路拓扑中，您可能需要使用此电阻器来防止数值问题，例如 Variable Capacitor 模块与另一个没有串联电阻的电容器模块并联连接时。
