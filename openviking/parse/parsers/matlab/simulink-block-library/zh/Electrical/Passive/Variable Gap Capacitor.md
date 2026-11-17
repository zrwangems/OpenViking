---
type: simulink-block
title: 'Variable Gap Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'variablegapcapacitor'
documentation_source_path: 'ref/variablegapcapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Gap Capacitor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: R
  summary: 从动板机械平移
  direction: conserving
- name: C
  summary: 基板机械平移
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电容器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电容器负极端子关联的电气守恒端口。

### **R** — 从动板机械平移

与从动板关联的机械平移守恒端口。

### **C** — 基板机械平移

与基板关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Capacitor plate area
  summary: 电容器板面积 1e-3 m^2（默认）| 正标量
  group: ''
- name: Dielectric medium thickness
  summary: 电介质厚度 1e-4 m（默认）| 正标量
  group: ''
- name: Specify properties of dielectric medium
  summary: 指定电介质属性的选项 Off（默认）| On
  group: ''
- name: Relative permittivity of dielectric medium
  summary: 电介质的相对介电常数 1.0（默认）| 正标量
  group: ''
- name: Young's modulus of dielectric material
  summary: 电介质材料的杨氏模量 0 Pa（默认）| 非负标量
  group: ''
```

### **Capacitor plate area** — 电容器板面积 `1e-3` `m^2`（默认）| 正标量

板的面积。

### **Dielectric medium thickness** — 电介质厚度 `1e-4` `m`（默认）| 正标量

电介质的厚度。

### **Specify properties of dielectric medium** — 指定电介质属性的选项 `Off`（默认）| `On`

用于指定电介质属性的选项。如果清除此参数，模块将假定电介质为真空，且弹性力为零。

### **Relative permittivity of dielectric medium** — 电介质的相对介电常数 `1.0`（默认）| 正标量

电介质相对于真空介电常数的介电常数。

#### 依赖关系

要启用此参数，请选中 **Specify properties of dielectric medium** 参数。

### **Young's modulus of dielectric material** — 电介质材料的杨氏模量 `0` `Pa`（默认）| 非负标量

电介质材料的杨氏模量。

#### 依赖关系

要启用此参数，请选中 **Specify properties of dielectric medium** 参数。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

具有平行板和可变间隙的电容器

Variable Gap Capacitor 模块对具有平行板和可变间隙的电容器进行建模。当向模块施加电压时，电压在板之间产生电场，从而产生吸引性静电力的电容器。

您可以通过选中 **Specify properties of dielectric medium** 参数来指定电介质的属性。如果您指定电介质材料的杨氏模量，板之间的位移会使电介质变形，从而产生弹性力。如果您不指定电介质的属性，模块将假定电介质为真空，且位移不会产生弹性力。

当电容器充电时，平移力也会影响电容器的电容、电流和电压。

### 方程

电容由以下方程定义：

C=ε0εAd+x，

其中：

- ε0 是真空介电常数。
- *ε* 是 **Relative permittivity of dielectric medium** 参数。
- *A* 是 **Capacitor plate area** 参数。
- *d* 是 **Dielectric medium thickness** 参数。
- *x* 是板的位移。

吸引性静电力由以下方程给出：

F=C2V22Aε0ε，

其中 *V* 是电容器两端的电压。

弹性力由以下方程给出：

Fdef=EAxd，

其中 *E* 是 **Young's modulus of dielectric material** 参数。

通过模块的总力是吸引性静电力和弹性力之和。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
