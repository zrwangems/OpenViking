---
type: simulink-block
title: 'Variable Inertia'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'variableinertia'
documentation_source_path: 'ref/variableinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Inertia

## 端口
```yaml
ports:
- name: LConn 1
  summary: 惯量，kg/m2 物理信号
  direction: input
- name: LConn 2
  summary: 旋转连接 机械旋转
  direction: input
```

### 输入

### **LConn 1** — 惯量，kg/m2 物理信号

与惯量相关联的物理输入信号，单位为
kg/m2。
### 守恒

### **LConn 2** — 旋转连接 机械旋转

机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Minimum inertia
  summary: 最小惯量 0.1 kg*m^2（默认）| 正标量
  group: ''
```

### **Minimum inertia** — 最小惯量 `0.1` `kg*m^2`（默认）| 正标量

可变惯量在仿真期间可以取的最小值。物理信号输入在该值处饱和。如果输入低于最小惯量，则将其设置为等于最小惯量值。
## 所属库

Simscape / Driveline / Inertias & Loads

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

以物理信号输入指定的时变惯量

Variable Inertia 模块表示时变惯量的效果。具有可变惯量的组件包括展开太阳能电池板阵列的卫星。物理信号输入端口在每个时间步提供整个仿真期间的瞬时惯量。为最小化求解器误差，请避免输入信号中的不连续性和突变。

随着组件惯量的变化，作用在该组件上的惯性力矩也会变化：

TI=Iω˙，

其中：

- *TI* 是惯性
  力矩。
- *I* 是可变惯量。
- *ω* 是惯量的角速度。

物理信号输入在模块属性检查器中指定的最小惯量处饱和。每当输入低于最小惯量时，模块改为基于最小惯量执行计算。惯性力矩变为：

TI=IMinω˙，

其中 *IMin* 是允许的最小
惯量。

可变惯量的角动量是守恒的。在没有外部力矩的情况下，转动惯量的减小会导致角速度成比例增加。角动量保持恒定，直到净外部力矩使其发生变化。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
