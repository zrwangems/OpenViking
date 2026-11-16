---
type: simulink-block
title: 'Pressure Source (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Sources'
documentation_page: 'pressuresourceil'
documentation_source_path: 'ref/pressuresourceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Source (IL)

## 端口

### 输入

### **P** — 压差控制信号，Pa 物理信号

输入物理信号，用于指定源两端的压差。

#### 依赖项

如果将 **源类型** 参数设置为 `Controlled`，则此端口可见。

### 守恒

### **A** — 源入口等温液体

等温液体守恒端口。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

### **B** — 源出口等温液体

等温液体守恒端口。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

## 参数

### **源类型** — 选择压差是否可以在仿真期间变化 `Controlled` (默认) | `Constant`

选择源生成的压差是否可以在仿真期间变化：

- `Controlled` — 压差是可变的，由输入物理信号控制。选择此选项会显示输入端口 **P**。
- `Constant` — 压差在仿真期间恒定，由模块参数指定。选择此选项会启用 **压差** 参数。

### **压差** — 源两端的恒定压差 `0 MPa` (默认) | 标量

源两端的期望压差。

#### 依赖项

当将 **源类型** 参数设置为 `Constant` 时启用。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

在等温液体网络中生成指定的压差

Pressure Source (IL) 模块表示等温液体网络中的理想机械能量源。无论通过源的质量流量如何，源都可以在其端口两端保持指定的压差。没有流动阻力，也不与环境进行热交换。

端口 **A** 和 **B** 表示源的入口和出口。端口 **P** 处的输入物理信号指定压差。或者，可以将恒定压差指定为模块参数。正压差会使端口 **B** 处的压力大于端口 **A** 处的压力。

模块计算对流体所做的功，并将结果包含在仿真数据日志中，以供参考：

Wmech=m˙pB−pAρ¯

ρ¯=ρA+ρB2

其中：

- *W*mech 是源所做的机械功。
- m˙ 是源生成的质量流量。
- *p*A 和 *p*B 分别是端口 **A** 和 **B** 处的压力。
- ρ¯ 是平均流体混合物密度。
- *ρ*A 和 *ρ*B 分别是端口 **A** 和 **B** 处的流体混合物密度值。用于计算流体混合物密度的方程取决于所选的等温液体模型。有关详细信息，请参阅等温液体建模选项。

有关查看记录的仿真数据的信息，请参阅数据记录。

### 假设和限制

- 不存在由于摩擦造成的损失。
- 不与环境进行热交换。
