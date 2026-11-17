---
type: simulink-block
title: 'Current-Controlled Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Passives'
documentation_page: 'currentcontrolledswitch'
documentation_source_path: 'ref/currentcontrolledswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Current-Controlled Switch

## 端口
```yaml
ports:
- name: 1+
  summary: 正输入端口（电气）
  direction: conserving
- name: 1-
  summary: 负输入端口（电气）
  direction: conserving
- name: 2+
  summary: 正输出端口（电气）
  direction: conserving
- name: 2-
  summary: 负输出端口（电气）
  direction: conserving
```

### 守恒端口

### **1+** — 正输入端口（电气）

与电流控制开关正输入关联的电气守恒端口。

### **1-** — 负输入端口（电气）

与电流控制开关负输入关联的电气守恒端口。

### **2+** — 正输出端口（电气）

与电流控制开关正输出关联的电气守恒端口。

### **2-** — 负输出端口（电气）

与电流控制开关负输出关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Switch model
  summary: 开关模型 Abrupt transition after delay（默认）| Smooth transition between Ion and Ioff
  group: ''
- name: Threshold current, IT
  summary: 阈值电流 0 A（默认）
  group: ''
- name: Hysteresis current, IH
  summary: 迟滞电流 0 A（默认）
  group: ''
- name: Control current for on state, ION
  summary: 导通状态的控制电流 1e-3 A（默认）
  group: ''
- name: Control current for off state, IOFF
  summary: 关断状态的控制电流 0 A（默认）
  group: ''
- name: On resistance, RON
  summary: 闭合开关电阻 1 Ohm（默认）
  group: ''
- name: Use 1/GMIN as Off resistance
  summary: 是否使用 1/GMIN 作为关断电阻 No（默认）| Yes
  group: ''
- name: Off resistance, ROFF
  summary: 断开开关电阻 1e12 Ohm（默认）| 1e6
  group: ''
- name: Time delay, TD
  summary: 时间延迟 0 s（默认）
  group: ''
```

### **Switch model** — 开关模型 `Abrupt transition after delay`（默认）| `Smooth transition between Ion and Ioff`

导通状态与关断状态电流之间的转换是否为瞬时转换。要将此模块建模为可变电阻开关，请选择 `Smooth transition between Ion and Ioff`。要将此模块建模为短转换开关，请选择 `Abrupt transition after delay`。

### **Threshold current, IT** — 阈值电流 `0` `A`（默认）

高于此电流时，模块将控制电流解释为高电平。

**注意**

控制电流与阈值电流之差必须至少为 **Hysteresis current, IH** 参数值，才能改变开关的状态。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Abrupt transition after delay`。

### **Hysteresis current, IH** — 迟滞电流 `0` `A`（默认）

控制电流必须超出或低于 **Threshold current, IT** 参数值的量，才能改变开关的状态。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Abrupt transition after delay`。

### **Control current for on state, ION** — 导通状态的控制电流 `1e-3` `A`（默认）

导通状态下的开关控制电流。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Smooth transition between Ion and Ioff`。

### **Control current for off state, IOFF** — 关断状态的控制电流 `0` `A`（默认）

关断状态下的开关控制电流。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Smooth transition between Ion and Ioff`。

### **On resistance, RON** — 闭合开关电阻 `1` `Ohm`（默认）

开关闭合时的电阻。

### **Use 1/GMIN as Off resistance** — 是否使用 1/GMIN 作为关断电阻 `No`（默认）| `Yes`

是否自动将此开关的关断电阻计算为 `1/GMIN`。

**注意**

并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 1e–12。要更改 *GMIN*，请向您的模型添加一个 Environment Parameters 模块，并将 **GMIN** 参数设置为所需的值。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Abrupt transition after delay`。

### **Off resistance, ROFF** — 断开开关电阻 `1e12` `Ohm`（默认）| `1e6`

开关断开时的电阻。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Switch model** 设置为 `Abrupt transition after delay`，并将 **Use 1/GMIN as Off resistance** 设置为 `No`。默认值为 `1e12`。
- 将 **Switch model** 设置为 `Smooth transition between Ion and Ioff`。默认值为 `1e6`。

### **Time delay, TD** — 时间延迟 `0` `s`（默认）

开关转换发生之后的时间延迟。

#### 依赖关系

要启用此参数，请将 **Switch model** 设置为 `Abrupt transition after delay`。
## 所属库

Simscape / Electrical / Additional Components / SPICE Passives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

带迟滞的电流控制开关

Current-Controlled Switch 模块表示其状态由流过输入端口的电流（*控制电流*）控制的开关的电气特性。

此模块可建模为可变电阻开关或短转换开关。对于可变电阻开关，请将 **Switch model** 参数设置为 `Smooth transition between Ion and Ioff`。对于短转换开关，请将 **Switch model** 设置为 `Abrupt transition after delay`。

### 短转换开关

在短转换开关中，关断状态与导通状态之间的转换是瞬时的：

- 当控制电流大于或等于 **Threshold current, IT** 与 **Hysteresis current, IH** 参数值之和时，开关闭合，其电阻等于 **On resistance, RON** 参数值。
- 当控制电流小于 **Threshold current, IT** 参数值减去 **Hysteresis current, IH** 参数值时，开关断开，其电阻等于 **Off resistance, ROFF** 参数值。
- 当控制电流大于或小于 **Threshold current, IT** 参数值的量小于或等于 **Hysteresis current, IH** 参数值时，电流处于*交叉区域*，开关的状态保持不变。

**注意**

如果 **Hysteresis current, IH** 参数值小于 `0`，则无论 **Switch model** 参数设置为何值，模块都会建模为可变电阻开关。

### 可变电阻开关

在可变电阻开关中，关断状态与导通状态之间的转换是指数形式的：

- 当 **Control current for on state, ION** 大于 **Control current for off state, IOFF** 时：

  - 如果控制电流大于 **Control current for on state, ION** 参数值，则开关闭合，其电阻等于 **On resistance, RON** 参数值。
  - 如果控制电流小于 **Control current for off state, IOFF** 参数值，则开关断开，其电阻等于 **Off resistance, ROFF** 参数值。
  - 如果控制电流大于 **Control current for off state, IOFF** 参数值或小于 **Control current for on state, ION** 参数值，则电阻定义为：

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]

    其中：

    - *Rs* 是开关电阻。
    - Lm=ln[(RON\*ROFF)12] 是电阻值的对数均值。
    - Lr=ln(RONROFF) 是电阻值的对数比。
    - *Ic* 是控制电流。
    - Im=ION+IOFF2 是控制电流的均值。
    - Id=ION−IOFF 是控制电流之差。
- 当 **Control current for on state, ION** 小于 **Control current for off state, IOFF** 时：

  - 如果控制电流小于 **Control current for on state, ION** 参数值，则开关闭合，其电阻等于 **On resistance, RON** 参数值。
  - 如果控制电流大于 **Control current for off state, IOFF** 参数值，则开关断开，其电阻等于 **Off resistance, ROFF** 参数值。
  - 如果控制电流小于 **Control current for off state, IOFF** 参数值或大于 **Control current for on state, ION** 参数值，则电阻定义为：

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]
