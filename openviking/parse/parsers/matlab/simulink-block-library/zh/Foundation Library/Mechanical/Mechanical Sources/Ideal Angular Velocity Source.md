---
type: simulink-block
title: 'Ideal Angular Velocity Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sources'
documentation_page: 'idealangularvelocitysource'
documentation_source_path: 'ref/idealangularvelocitysource.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Angular Velocity Source

## 端口
```yaml
ports:
- name: S
  summary: 控制信号，rad/s 物理信号
  direction: input
- name: R
  summary: 杆机械旋转
  direction: input
- name: C
  summary: 壳体机械旋转
  direction: input
```

### 输入

### **S** — 控制信号，rad/s 物理信号

物理信号输入端口，通过该端口施加驱动源的控制信号。
### 守恒

### **R** — 杆机械旋转

与源运动部件（杆）关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与源参考点（壳体）关联的机械旋转守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械旋转系统中的理想角速度源

Ideal Angular Velocity Source 模块表示一个理想角速度源，它在其端子处生成与输入物理信号成比例的速度差。该源是理想的，因为它被假定具有足够的功率，无论系统上施加的扭矩如何，都能维持指定的速度。

连接 R 和 C 是机械旋转守恒端口。端口 S 是物理信号端口，通过该端口施加驱动源的控制信号。源两端的相对速度（速度差）与控制端口 S 处的信号直接成比例。可以使用 Simulink® 信号源的各种类型来生成所需的速度变化曲线。

模块正方向是从端口 R 到端口 C。这意味着速度测量为 *ω* = *ω*R –
*ω*C，其中
*ω*R、
*ω*C 分别是端口 R 和 C 处的绝对角速度，通过源的扭矩如果从 R 指向 C 则为正。如果源向端口 R 提供能量，则源产生的功率为负。
