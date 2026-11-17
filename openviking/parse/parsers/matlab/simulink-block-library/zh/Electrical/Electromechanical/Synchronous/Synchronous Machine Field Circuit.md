---
type: simulink-block
title: 'Synchronous Machine Field Circuit'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinefieldcircuit'
documentation_source_path: 'ref/synchronousmachinefieldcircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Field Circuit

## 端口

### 输入

### **Efd** — 励磁电压物理

与励磁电压关联的物理输入端口。

#### 依赖关系

仅当您将 **PS input and output unit** 参数设置为 `SI` 时，此端口可见。

### **Efd\_pu** — 标幺值励磁电压物理

与励磁电压关联的物理输入端口，以标幺值表示。

#### 依赖关系

仅当您将 **PS input and output unit** 参数设置为 `Per unit` 时，此端口可见。

### 输出

### **Ifd** — 励磁电流物理

与励磁电流关联的物理输入端口。

#### 依赖关系

仅当您将 **PS input and output unit** 参数设置为 `SI` 时，此端口可见。

### **Ifd\_pu** — 标幺值励磁电流物理

与励磁电流关联的物理输入端口，以标幺值表示。

#### 依赖关系

仅当您将 **PS input and output unit** 参数设置为 `Per unit` 时，此端口可见。

### 守恒

### **fd+** — 励磁绕组正极端子电气

与励磁绕组正极端子关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子电气

与励磁绕组负极端子关联的电气守恒端口。

## 参数

仅当您将 **PS input and output unit** 参数设置为 `Per unit` 时，此模块的附加参数才可见。

### 主要

### **PS input and output unit** — 单位制配置 `SI`（默认）| `Per unit`

模块的单位制配置。

选择：

- `SI` 会显示 SI 端口。
- `Per unit` 会显示标幺值端口和参数。

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认）

所连接电机的额定视在功率。

### **Rated electrical frequency** — 标称电气频率 `60` `Hz`（默认）

所连接电机的额定视在功率对应的标称电气频率。

### **Specify field circuit input required to produce rated terminal voltage at no load by** — 指定空载时产生额定端电压所需的励磁电路输入，所依据的值为 `Field circuit current`（默认）| `Field circuit voltage`

在 `Field circuit voltage` 和 `Field circuit current` 之间选择。

### **Field circuit current** — 励磁电路电流 `1300` `A`（默认）

此值用于计算励磁电路的标幺值基值（非互易标幺值系统）。

#### 依赖关系

仅当您将 **Specify field circuit input required to produce rated terminal voltage at no load by** 参数设置为 `Field circuit current` 时，此参数可见。

### **Field circuit voltage** — 励磁电路电压 `92.95` `V`（默认）

此值用于计算励磁电路的标幺值基值（非互易标幺值系统）。

#### 依赖关系

仅当您将 **Specify field circuit input required to produce rated terminal voltage at no load by** 参数设置为 `Field circuit voltage` 时，此参数可见。

### 电机参数

### **Specify parameterization by** — 电机参数化 `Fundamental Parameters`（默认）| `Standard Parameters`

在 `Fundamental Parameters` 和 `Standard Parameters` 之间选择。

### **Stator d-axis mutual inductance (unsaturated), Ladu** — 未饱和定子 d 轴互感 `1.66`（默认）

未饱和定子 d 轴互感。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Fundamental Parameters` 时，此参数可见。

### **Rotor field circuit resistance, Rfd** — 转子励磁电路电阻 `0.0006`（默认）

转子励磁电路电阻。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Fundamental Parameters` 时，此参数可见。

### **Stator leakage reactance, Xl** — 定子漏电抗 `0.15`（默认）

定子漏电抗。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters` 时，此参数可见。

### **d-axis synchronous reactance, Xd** — *d* 轴同步电抗 `1.81`（默认）

*d* 轴同步电抗。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters` 时，此参数可见。

### **d-axis transient reactance, Xd'** — *d* 轴暂态电抗 `0.3`（默认）

*d* 轴暂态电抗。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters` 时，此参数可见。

### **d-axis subtransient reactance, Xd''** — *d* 轴次暂态电抗 `0.23`（默认）

*d* 轴次暂态电抗。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters` 时，此参数可见。

### **Specify d-axis time constant** — *d* 轴时间常数指定 `Open-circuit value`（默认）| `Short-circuit value`

在 `Open-circuit value` 和 `Short-circuit value` 之间选择。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters` 时，此参数可见。

### **d-axis transient open-circuit, Td0'** — *d* 轴暂态开路 `8` `s`（默认）

*d* 轴暂态开路时间常数。
此参数仅当 **Specify d-axis transient time constant** 设置为 `Open-circuit value` 时可见。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters`，并将 **Specify d-axis transient time constant** 设置为 `Open-circuit value` 时，此参数可见。

### **d-axis transient short-circuit, Td'** — *d* 轴暂态短路 `1.3260` `s`（默认）

*d* 轴暂态短路时间常数。
此参数仅当 **Specify d-axis transient time constant** 设置为 `Short-circuit value` 时可见。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters`，并将 **Specify d-axis transient time constant** 设置为 `Short-circuit value` 时，此参数可见。

### **d-axis subtransient open-circuit, Td0''** — *d* 轴次暂态开路 `0.03`（默认）

*d* 轴次暂态开路。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters`，并将 **Specify d-axis transient time constant** 设置为 `Open-circuit value` 时，此参数可见。

### **d-axis subtransient short-circuit, Td''** — *d* 轴次暂态短路 `0.0230`（默认）

*d* 轴次暂态短路。

#### 依赖关系

仅当您将 **Specify parameterization by** 参数设置为 `Standard Parameters`，并将 **Specify d-axis transient time constant** 设置为 `Short-circuit value` 时，此参数可见。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

同步电机励磁电路标幺值接口，具有电压输入和电流输出

Synchronous Machine Field Circuit 模块将指定电压施加到其所连接同步电机的励磁电路，并测量流过该电路的电流。

SI 模型会将您在对话框中输入的 SI 值转换为用于仿真的标幺值。有关 SI 与标幺值电机参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

该模块包含一个电气参考。物理信号输入 **Efd\_pu** 定义电压，物理信号输出 **Ifd\_pu** 提供电流，二者均以标幺值表示。物理信号输入 **Efd** 定义电压，单位为 V；物理信号输出 **Ifd** 提供电流，单位为 A。

标幺值基值采用非互易标幺值系统，即 *Efd* 和 *Ifd*，而不是互易标幺值系统，即 *efd* 和 *ifd*。

下图显示了 Synchronous Machine Field Circuit 模块的标幺值模型。

下图显示了 Synchronous Machine Field Circuit 模块的 SI 模型。
