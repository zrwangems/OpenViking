---
type: simulink-block
title: 'SM Governor with Droop'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smgovernorwithdroop'
documentation_source_path: 'ref/smgovernorwithdroop.html'
language: zh-CN
chinese_source: worker-translation
---

# SM Governor with Droop

## 端口

### 输入

### **P\_ref** — 期望的标幺值发电机负载标量

以标幺值表示的参考发电机负载。调速器在其参考转速下运行时的稳态输出等于该值。

**数据类型：** `single` | `double`

### **speed\_ref** — 期望的标幺值发电机转速标量

以标幺值表示的参考发电机转速。

**数据类型：** `single` | `double`

### **speed** — 实际标幺值发电机转速标量

以标幺值表示的测量发电机转速。

**数据类型：** `single` | `double`
### 输出

### **throttle** — 节气门位置标量

调速器的节气门位置，以标幺值表示。

**数据类型：** `single` | `double`

## 参数

### **Percentage droop, (%)** — 下垂率 `5` `%`（默认值）

调速器转速从 `0`% 到 `100`% 负载的百分比变化。如果多台调速器驱动的发电机并联连接，下垂百分比越低的对负载变化越敏感。

### **Time constant of governor, (s)** — 一阶滞后时间常数 `0.2`（默认值）

调速器一阶滞后时间常数，表示节气门惯性动态。

### **Initial throttle position, (pu)** — 初始节气门输出 `0.5`（默认值）

节气门的初始状态。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带下垂特性的同步电机调速器

SM Governor with Droop 模块实现了一个带下垂特性的同步电机（SM）调速器。使用此模块来调节或控制驱动同步发电机的原动机的节气门输入。

该模块使用测量转速与期望发电机转速之间的误差来设定原动机节气门位置。例如，当原动机旋转过慢时，节气门打开以增加发电机的能量输入并提高其转速。

### 工作原理

当多台调速器驱动的发电机并联连接时，下垂特性确保电网的整体稳定性。下垂定义为发电机从空载到满载的转速百分比变化。下图显示了具有 5% 下垂率的调速器的转速-负载关系。

其中，

- *ωref* 是调速器的参考转速。使用 **speed\_ref** 端口将该值设为标幺值。
- *Pref* 是调速器的参考负载。使用 **P\_ref** 端口将该值设为标幺值。
- `droop` 是调速器的下垂百分比。使用 **Percentage droop, (%)** 参数将该值设为百分比。

该模块计算参考节气门位置（以标幺值表示）如下：

uthrottle,ref=Pref−100droop(ω−ωref)

其中 *ω* 是实际的标幺值发电机转速。

阀门的惯性在参考节气门位置与实际节气门位置之间引入延迟，该延迟建模为一阶滞后：

uthrottle=(1Tss+1)uthrottle,ref

其中 *Ts* 是时间常数。使用 **Time constant of governor, (s)** 参数设置该值。
