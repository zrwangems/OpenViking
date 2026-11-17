---
type: simulink-block
title: 'Ideal Force Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sources'
documentation_page: 'idealforcesource'
documentation_source_path: 'ref/idealforcesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Force Source

## 端口
```yaml
ports:
- name: S
  summary: 控制信号，N 物理信号
  direction: input
- name: R
  summary: 杆机械平移
  direction: input
- name: C
  summary: 壳体机械平移
  direction: input
```

### 输入

### **S** — 控制信号，N 物理信号

物理信号输入端口，通过该端口施加驱动源的的控制信号。
### 守恒

### **R** — 杆机械平移

与源运动部件（杆）关联的机械平移守恒端口。

### **C** — 壳体机械平移

与源参考点（壳体）关联的机械平移守恒端口。
## 参数
```yaml
parameters: []
```

在 R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想机械能源，生成与输入信号成比例的力

Ideal Force Source 模块表示一个理想机械能源，生成与输入物理信号成比例的力。该源是理想的，因为它被假定为足够强大，无论源端子处的速度如何，都能在其输出端维持指定的力。

连接 R 和 C 是机械平移守恒端口。端口 S 是物理信号端口，通过该端口施加驱动源的的控制信号。您可以使用各种 Simulink® 信号源来生成所需的力变化曲线。端口 S 处的正信号生成从 C 作用到 R 的力。源生成的力与控制端口 S 处的信号成正比。

模块正方向是从端口 C 到端口 R。这意味着如果力沿从 C 到 R 的方向作用，则该力为正。相对速度定义为 *v* = *v*C – *v*R，其中 *v*R、*v*C 分别是端口 R 和 C 处的绝对速度，如果端口 R 处的速度大于端口 C 处的速度，则相对速度为负。如果源向端口 R 传递能量，则源生成的功率为负。
