---
type: simulink-block
title: 'Variable Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'variableinductor'
documentation_source_path: 'ref/variableinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Inductor

## 端口

### 输入

### **L** — 电感物理信号

与电感关联的物理信号输入端口。L 必须有限、大于零且连续（无阶跃变化）。
### 守恒

### **+** — 正端子电气

与电感正电压关联的电气守恒端口。

### **-** — 负端子电气

与电感负电压关联的电气守恒端口。

## 参数

### **Equation** — 用于模块电感的方程 `V = L*dI/dt + dL/dt*I`（默认值） | `V = L*dI/dt`

为模块电感选择以下选项之一：

- `V = L*dI/dt + dL/dt*I` — 此方程假设电感定义为磁通量与稳态电流之比。此选项为默认值。
- `V = L*dI/dt` — 此方程假设电感定义为给定电流下磁通量-电流曲线的局部梯度。

### **Minimum inductance L>0** — 最小电感 `1e-6` `H`（默认值）

端口 L 处信号值的下限。此限制可防止信号达到没有物理意义的值。

### **Parallel conductance** — 并联电导 `1e-9` `1/Ohm`（默认值）

与可变电感并联放置的电导值。

### **Initial current** — 初始电流 `0` `A`（默认值）

仿真开始时的输出电流。

#### 依赖关系

仅当您为 **Equation** 参数选择 `V = L*dI/dt` 时，此参数才可见。

### **Initial magnetic flux** — 初始磁通 `0` `Wb`（默认值）

仿真开始时的磁通。

#### 依赖关系

仅当您为 **Equation** 参数选择 `V = L*dI/dt + dL/dt*I` 时，此参数才可见。

## 所属库

Simscape / Electrical / Passive

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

线性时变电感

Variable Inductor 模块表示一个线性时变电感。当端口 L 处的电感为 *L* 时，该模块为器件两端电压 *v* 与通过电感的电流 *i* 之间的关系提供两个选项。**Equation** 参数确定模块使用以下哪个方程：

- v=dLdti+Ldidt

  当电感定义为磁通量 Ф 与稳态电流之比时，使用上述方程：

  L(i)=Φ(i)i
- v=Ldidt

  当电感定义为给定电流下磁通量-电流曲线的局部梯度时，使用上述方程：

  L(i)=dΦ(i)di

该模块包括一个与可变电感并联的电导。您可以使用该电导来表示电感的总绝缘电导。对于某些电路拓扑，您可能需要使用该电导来防止数值问题，例如 Variable Inductor 模块与另一个不具有并联电导的电感模块串联连接时。
