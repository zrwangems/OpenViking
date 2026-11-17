---
type: simulink-block
title: 'Fault'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'fault'
documentation_source_path: 'ref/fault.html'
language: zh-CN
chinese_source: worker-translation
---

# Fault

## 端口

### 输入

### **F** — 外部故障触发信号 physical

与外部故障触发信号关联的物理信号输入端口。
### 输出

### **X** — 故障状态 physical

与故障状态关联的物理信号输出端口。如果模块处于故障状态，则输出 `1`，
否则输出 `0`。
### 守恒

### **+** — 正极端子 electrical

与故障正极端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与故障负极端子关联的电气守恒端口。

## 参数

### 主要

### **Unfaulted resistance** — 无故障时的电阻 `inf` `Ohm`（默认值）

当没有故障时，**+** 和
**–** 端口之间的电阻。

### **Faulted resistance** — 故障时的电阻 `1e-3` `Ohm`（默认值）

当模块处于故障状态时，**+** 和
**–** 端口之间的电阻。

### **Reporting when a fault occurs** — 故障发生报告 `None`（默认值）| `Warn` | `Error`

选择故障发生时是否发出断言：

- `None` — 模块不发出断言。
- `Warn` — 模块发出警告。
- `Error` — 仿真因错误而停止。

### 时间触发器

### **Enable temporal fault trigger** — 时间故障触发选项 `No`（默认值）| `Yes`

选择 `Yes` 以启用基于时间的故障触发。

### **Simulation time for fault event** — 故障事件的仿真时间 `1` `s`（默认值）

设置模块进入故障状态的仿真时间。

#### 依赖关系

仅当您将 **Enable temporal fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Fault duration** — 故障持续时间 `inf` `s`（默认值）

设置故障的仿真持续时间。当持续时间结束后，模块退出故障状态。

#### 依赖关系

仅当您将 **Enable temporal fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### 行为触发器

### **Enable behavioral fault trigger** — 行为故障触发选项 `No`（默认值）| `Yes`

选择 `Yes` 以启用行为故障触发。

### **Permissible voltage range** — 允许电压范围 `[-100, 100]` `V`（默认值）

指定一个长度为 2 的向量，用于定义允许电压范围。如果电压超出此范围的时间超过
**Time to fail when exceeding voltage range**
参数值，则模块进入故障状态。

#### 依赖关系

仅当您将 **Enable behavioral fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Time to fail when exceeding voltage range** — 超出电压范围时的失效时间 `1` `s`（默认值）

设置电压可以超出允许电压范围而不触发故障的最长时间。

#### 依赖关系

仅当您将 **Enable behavioral fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Permissible current range** — 允许电流范围 `[-1, 1]` `A`（默认值）

指定一个长度为 2 的向量，用于定义允许电流范围。如果电流超出此范围的时间超过
**Time to fail when exceeding current range**
参数值，则模块进入故障状态。

#### 依赖关系

仅当您将 **Enable behavioral fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Time to fail when exceeding current range** — 超出电流范围时的失效时间 `1` `s`（默认值）

设置电流可以超出允许电流范围而不触发故障的最长时间。

#### 依赖关系

仅当您将 **Enable behavioral fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### 外部触发器

### **Enable external fault trigger** — 外部故障触发选项 `No`（默认值）| `Yes`

选择 `Yes` 以启用外部故障触发。物理信号输入 F 提供外部故障触发信号。

### **External fault trigger** — 外部故障触发条件 `Faulted if F >= Fault threshold`（默认值）| `Faulted if F <= Fault threshold`

选择故障条件：

- `Faulted if F >= Fault threshold`
  — 当外部信号值变得大于或等于 **Fault
  threshold** 参数值时，发生故障。
- `Faulted if F <= Fault threshold`
  — 当外部信号值变得小于或等于 **Fault threshold**
  参数值时，发生故障。

#### 依赖关系

仅当您将 **Enable external fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Fault threshold** — 故障阈值 `0.5`（默认值）

当外部信号按故障条件所指定的方向越过该阈值时，触发故障的阈值。

#### 依赖关系

仅当您将 **Enable external fault trigger** 参数设置为
`Yes` 时，此参数才可见。

### **Fault resets when fault trigger reverts** — 故障触发恢复时故障复位 `No`（默认值）| `Yes`

选择 `Yes`，以便在触发信号恢复时复位故障。

#### 依赖关系

仅当您将 **Enable external fault trigger** 参数设置为
`Yes` 时，此参数才可见。

## 所属库

Simscape / Electrical / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

具有时间、行为或外部触发的电气故障

Fault 模块允许您将电气故障表示为电阻的瞬时变化。您可以使用它来复现
开路和短路故障行为。该模块可以触发故障事件：

- 在特定时间。该模块还可以在指定的持续时间后停止施加时间故障。
- 当超出预定义的电压范围或电流范围时
- 当外部触发信号变为高电平或低电平时

可选地，外部触发选项还允许在触发信号恢复时复位故障。您可以分别启用或禁用所有三种触发机制。如果仿真中需要多个触发机制，可以将它们一起使用。

当未触发故障时，两个电气端口之间的电阻由 **Unfaulted resistance** 参数值定义。
此参数的默认值为 `inf` 欧姆，即端口为开路。当
触发故障时，模块将两个电气端口之间的电阻更改为 **Faulted resistance** 值。此
参数的默认值为 `1e-3` 欧姆，即端口为短路。

您可以使用 **Reporting when a fault occurs** 参数选择故障发生时是否发出
断言。断言可以采用警告或错误的形式。默认情况下，模块不发出
断言。

物理输出 *X* 表示故障状态；如果模块处于故障状态，则输出为 `1`，否则为 `0`。物理
信号输入 *F* 是外部故障触发信号，仅当 **Enable external fault trigger** 设置为
`Yes` 时使用。
