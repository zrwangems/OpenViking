---
type: simulink-block
title: 'SM Governor with Droop'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Other'
documentation_page: 'smgovernorwithdroop'
documentation_source_path: 'ref/smgovernorwithdroop.html'
language: zh-CN
chinese_source: worker-translation
---

# SM Governor with Droop

## 端口

### 输入

### **P\_ref** — 期望的标幺发电机负载标量

参考发电机负载，以标幺值表示。调速器在其参考速度下运行时的稳态输出等于该值。

**数据类型：** `single` | `double`

### **speed\_ref** — 期望的标幺发电机速度标量

参考发电机速度，以标幺值表示。

**数据类型：** `single` | `double`

### **speed** — 实际标幺发电机速度标量

测量的发电机速度，以标幺值表示。

**数据类型：** `single` | `double`
### 输出

### **throttle** — 节流阀位置标量

调速器的节流阀位置，以标幺值表示。

**数据类型：** `single` | `double`

## 参数

### **Percentage droop, (%)** — 下垂 `5` `%`（默认）

调速器速度从 `0`% 到 `100`% 负载的百分比变化。如果多台调速器驱动的发电机并联连接，则具有较低下垂百分比的发电机对负载变化更敏感。

### **Time constant of governor, (s)** — 一阶滞后时间常数 `0.2`（默认）

表示节流阀惯性动态的调速器一阶滞后时间常数。

### **Initial throttle position, (pu)** — 初始节流阀输出 `0.5`（默认）

节流阀的初始状态。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

具有下垂特性的同步机调速器

SM Governor with Droop 模块实现具有下垂特性的同步机 (SM) 调速器。使用此模块调节或控制驱动同步发电机的原动机的节流阀输入。

该模块使用测量的发电机速度与期望发电机速度之间的误差来设置原动机节流阀位置。例如，当原动机旋转过慢时，节流阀打开，以增加发电机的能量输入并提高其速度。

### 运行

当多台调速器驱动的发电机并联连接时，下垂特性确保电网的整体稳定性。下垂定义为发电机从空载到满载的速度百分比变化。此图显示了具有 5% 下垂的调速器的速度-负载关系。

这里，

- *ωref* 是调速器的参考速度。使用 **speed\_ref** 端口将此值设置为标幺值。
- *Pref* 是调速器的参考负载。使用 **P\_ref** 端口将此值设置为标幺值。
- `droop` 是调速器的下垂百分比。使用 **Percentage droop, (%)** 参数将此值设置为百分比。

该模块计算参考节流阀位置，以标幺值表示，如下：

uthrottle,ref=Pref−100droop(ω−ωref)

其中 *ω* 是实际标幺发电机速度。

阀门的惯性在参考节流阀位置与实际节流阀位置之间引入延迟，该延迟建模为一阶滞后：

uthrottle=(1Tss+1)uthrottle,ref

这里，*Ts* 是时间常数。使用 **Time constant of governor, (s)** 参数设置此值。
