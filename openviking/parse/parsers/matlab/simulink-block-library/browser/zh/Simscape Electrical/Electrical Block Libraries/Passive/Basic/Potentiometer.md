---
type: simulink-block
title: 'Potentiometer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'potentiometer'
documentation_source_path: 'ref/potentiometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Potentiometer

## 端口

### 输入

### **x** — 滑动端位置控制物理信号

控制滑动端位置的物理信号输入端口。

### 守恒

### **L** — 左引脚电气

与电位器左引脚关联的电气守恒端口。

### **R** — 右引脚电气

与电位器右引脚关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of visible ports** 设置为 `Three: left, right, and wiper`。

### **W** — 滑动端引脚电气

与电位器滑动端引脚关联的电气守恒端口。

## 参数

### **Number of visible ports** — 端口可见性选项 `Three: left, right, and wiper`（默认）| `Two: left and wiper`

是否启用电位器的右端端口 **R**。

### **Total resistance** — 总电阻 `1000` `Ohm`（默认）

当端口 **W** 开路时，端口 **L** 与端口 **R** 之间的电阻。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Three: left, right, and wiper`。

### **Residual resistance** — 残余电阻 `1` `Ohm`（默认）| 正标量

当滑动端位于端端口时，在滑动端与相邻端端口（**L** 或 **R**）之间测得的电阻。您可以使用此参数表示由于机械挡块而滑动端无法到达轨道末端的情况。此值必须大于或等于零。典型值为总电阻的 `5e-3` 倍。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Three: left, right, and wiper`。

### **PS input for wiper at L** — PS input for wiper at L `0`（默认）

端口 **x** 处输入物理信号的值，该值对应于滑动端位于端口 **L**。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Three: left, right, and wiper`。

### **PS input for wiper at R** — PS input for wiper at R `1`（默认）

端口 x 处输入物理信号的值，该值对应于滑动端位于端口 `R`。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Three: left, right, and wiper`。

### **Minimum resistance** — 最小电阻 `1` `Ohm`（默认）

当滑动端位于左端口时，在滑动端与左端口 **L** 之间测得的最小允许电阻。此参数的值必须大于 `0` 且小于 **Maximum resistance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Two: left and wiper`。

### **Maximum resistance** — 最大电阻 `999` `Ohm`（默认）

在滑动端与左端口 **L** 之间测得的最大允许电阻。此参数的值必须大于 `0` 且大于 **Minimum resistance** 参数的值。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Two: left and wiper`。

### **PS input for wiper at minimum resistance** — PS input for wiper at minimum resistance `0`（默认）

端口 **x** 处输入物理信号的值，该值对应于滑动端位于端口 **L**。默认值为 `0`。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Two: left and wiper`。

### **PS input for wiper at maximum resistance** — PS input for wiper at maximum resistance `1`（默认）

端口 **x** 处输入物理信号的值，该值对应于滑动端位于距端口 **L** 最远处。

#### 依赖关系

要启用此参数，请将 **Number of visible ports** 设置为 `Two: left and wiper`。

### **Taper** — 电阻锥度行为 `Linear`（默认）| `Logarithmic`

电位器的电阻锥度行为。

**注意**

`Linear` 和 `Logarithmic` 选项不会对相同的锥度建模。不能将对数电位器参数化为线性电位器，因为对数锥度是非线性的。

如果将此参数设置为 `Linear`，该图显示滑动端控制位置与 **L** 和 **W** 端口之间电阻的关系。

如果将此参数设置为 `Logarithmic`，该图显示滑动端控制位置与 **L** 和 **W** 端口之间电阻的关系。

### **Resistance when centered** — 居中时的电阻 `200` `Ohm`（默认）

如果将 **Resistance gradient** 参数设置为 `Higher at L`，则此参数是滑动端居中时端口 **L** 与端口 **W** 之间的电阻。否则，如果将 **Resistance gradient** 设置为 `Higher at R`，则此参数是滑动端居中时端口 **R** 与端口 **W** 之间的电阻。由于电阻锥度呈指数形状，**Resistance when centered** 参数的值必须小于 **Total resistance** 参数值的一半。

#### 依赖关系

要启用此参数，请将 **Taper** 设置为 `Logarithmic`。

### **Resistance gradient** — 电阻梯度 `Higher at R`（默认）| `Higher at L`

电位器电阻在左端还是右端变化更快。

#### 依赖关系

要启用此参数，请将 **Taper** 设置为 `Logarithmic`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

由物理信号控制的旋转式或直线行程电位器

Potentiometer 模块表示一个旋转式或直线行程电位器，其滑动端位置由输入物理信号控制。

如果电位器电阻根据滑动端位置线性变化，则滑动端位置与端口 **L** 之间的电阻为：

RWL=R0−2rxmax−xmin(x−xmin)+r

其中

- *RWL* 是滑动端位置与端口 **L** 之间的电阻。
- *R0* 是端口 **L** 与 **R** 之间的总电阻。
- *x* 是滑动端位置。
- *xmin* 是当滑动端位于端口 **L** 时滑动端位置的值。
- *xmax* 是当滑动端位于端口 **R** 时滑动端位置的值。
- *r* 是残余电阻。这是当 *x* 等于 *xmin* 时滑动端与端口 **L** 之间的电阻。这也是当 *x* 等于 *xmax* 时滑动端与端口 **R** 之间的电阻。

如果为电位器电阻 **Taper** 参数指定 `Logarithmic`，则滑动端位置与端口 **L** 之间的电阻为：

RWL={A(eλ(x−xmin)−1)+r如果电阻梯度在 R 处更高R0−A(eλ(x−xmin)−1)−r如果电阻梯度在 L 处更高

其中 *A* 和 λ 的选择使得在 *xmax* 处的 *RWL* 为 *R0 - r*，并且在 *x* = (*xmax* + *xmin*) / 2 处的 *RWL* 等于 *Rav*，即滑动端居中时的电阻。

**注意**

通常被描述为 LOG 或对数锥度的电位器实际上是指数锥度。也就是说，滑动端与左侧端口之间电阻的梯度随电阻增加而增加。Potentiometer 模块实现此行为。

对于线性锥度和对数锥度两者，滑动端位置与端口 **R** 之间的电阻为：

RWR=R0−RWL

其中

- *RWR* 是滑动端位置与端口 **R** 之间的电阻。
- *R0* 是端口 **L** 与 **R** 之间的总电阻。
- *RWL* 是滑动端位置与端口 **L** 之间的电阻。
