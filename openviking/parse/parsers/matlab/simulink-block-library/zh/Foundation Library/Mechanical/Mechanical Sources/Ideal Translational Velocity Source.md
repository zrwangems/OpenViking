---
type: simulink-block
title: 'Ideal Translational Velocity Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sources'
documentation_page: 'idealtranslationalvelocitysource'
documentation_source_path: 'ref/idealtranslationalvelocitysource.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Translational Velocity Source

## 端口
```yaml
ports:
- name: S
  summary: 控制信号，m/s 物理信号
  direction: input
- name: R
  summary: 杆机械平移
  direction: input
- name: C
  summary: 壳体机械平移
  direction: input
```

### 输入

### **S** — 控制信号，m/s 物理信号

物理信号输入端口，通过该端口施加驱动该源的控信号。
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

机械平移系统中的理想速度源

Ideal Translational Velocity Source 模块表示一个理想速度源，它在其端子处生成与输入物理信号成比例的速度差。该源是理想的，因为它被假定为足够强大，无论施加在系统上的力如何，都能维持指定的速度。

连接 R 和 C 是机械平移守恒端口。端口 S 是物理信号端口，通过该端口施加驱动该源的控信号。源两端的相对速度（速度差）与控端口 S 处的信号直接成比例。可以使用 Simulink® 信号源的完整种类来生成所需的速度变化曲线。

该模块的正方向是从端口 R 到端口 C。这意味着速度测量为 *v* = *v*R – *v*C，其中 *v*R、*v*C 分别是端口 R 和 C 处的绝对速度，并且如果力从 C 作用到 R，则通过该源的力为负。如果源向端口 R 提供能量，则源产生的功率为负。
