---
type: simulink-block
title: 'Belt-Cable Spool'
family: 'belts-and-cables'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Belts and Cables'
documentation_page: 'beltcablespool'
documentation_source_path: 'ref/beltcablespool.html'
language: zh-CN
chinese_source: worker-translation
---

# Belt-Cable Spool

## 端口

### Frame

### **R** — 局部参考坐标系 frame

用于将卷筒连接到多体模型其余部分的参考坐标系。
### Belt-Cable

### **A** — 卷筒缆线连接点 belt-cable

绳索中心线与卷筒节圆之间的切点。

## 参数

### **Pitch Radius** — 从卷筒中心到绳索中心线的距离 `10 cm`（默认） | positive scalar in units of length

从卷筒中心到绳索运行轴线的距离，沿发生接触的圆弧测量。在复合滑轮系统中，节圆半径之差通常决定速度降低或扭矩增大的比率。

### **Sensing** — 选择要感测的运动学变量 `Unchecked`（默认） | Checked

选择要感测的运动学变量。选中复选框可显示对应变量的物理信号端口。可供感测的变量包括：

- **Spool Angle A** — 角度，在参考坐标系的 *xy* 平面内测量，从局部 *x* 轴到坐标系原点与接触点 **A** 之间连线的夹角。

  如果接触点位于 *xz* 平面之上（在参考坐标系的 +*y* 区域内），则该角度为正。如果接触点位于 *xz* 平面之下，则该角度为负。当接触点恰好位于 *xz* 平面内时，该角度为零。

  该角度不是模量化的。它不会被限制在 360 度范围内——在完成一圈后跳回范围起点——而是随着重复旋转，测量值连续变化。卷筒每转一圈，测量值都会增加（或减少）2π。

  使用端口 **qpa** 进行此测量。
- **Fleet Angle A** — 从参考坐标系的 *xy* 平面到接触点 **A** 处绳索的角度。*xy* 平面与卷筒的中心平面相同。

  如果绳索从 *xy* 平面之上（在参考坐标系的 +*z* 区域内）接近接触点，则该角度为正。如果绳索从下方接近，则该角度为负。当绳索在卷筒中心平面内接近接触点时，该角度为零。

  该角度是模量化的，也就是说它的值是有界的——这里介于 -π/2 到 +π/2 之间。该范围是开放的。测量值可以在 -π/2 和 +π/2 之间变化，但不能达到任一极限。

  请注意，如果 Belt-Cable Properties 模块的 **Drum Belt-Cable Alignment** 参数设置为 `Monitored Planar`，则滑轮组件必须是平面的，因此偏角始终为零。要对非平面组件建模，请使用该参数的默认设置：`Unrestricted`。

  使用端口 **qfa** 进行此测量。

## 所属库

Simscape / Multibody / Belts and Cables

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

滑轮系统中绳索的源和汇

Belt-Cable Spool 模块表示一个圆柱形卷筒，用于缠绕（以及从其上退绕）滑轮系统的绳索。卷筒标记绳索的一端，也标记电机或其他动力源通常拉动负载的点。Belt-Cable End 模块通常标记绳索的另一端，负载本身通常连接在该端。根据是缠绕还是退绕，卷筒可以表现为绳索的无限源，或绳索的无限汇。

卷筒用作滑轮系统特有的 belt-cable 域与所有其他多体组件通用的 frame 域之间的接口。belt-cable 端口（**A**）标识要缠绕到卷筒上的绳索端点，以及该端点在滑轮系统中的相对位置。frame 端口（**R**）标识卷筒的参考坐标系及其在更广泛多体模型中的位置。

卷筒的自由度取决于卷筒与其他组件连接的关节。通常由转动副提供这些自由度；在这种情况下，它们简化为绕单一轴（卷筒的轴）的旋转。通过关节直接以扭矩或运动信号指定的致动输入，用于驱动卷筒并缠绕（或退绕）绳索。

绳索在进入和离开卷筒时与卷筒圆周相切。按照右手定则，缠绕方向为绕卷筒旋转轴的逆时针方向。根据定义，该轴是局部参考坐标系（**R**）的 *z* 轴。要反转缠绕方向，必须翻转局部参考坐标系，使 *z* 轴指向相反方向——例如，通过 Rigid Transform 模块施加坐标系旋转。

模型中不考虑卷筒表面（光滑或带槽）。此外，假设绳索以恒定半径（*pitch* 圆半径）绕卷筒缠绕，并且与绞盘的横截面共面。忽略因缠绕引起的卷筒半径变化。

默认情况下，绳索可以与其中心平面成一定角度进入和离开卷筒（图中为 *θ*）。该角度可在仿真过程中变化——例如，由于卷筒在移动副上平移。虽然接触点始终位于卷筒的中心平面内，但卷筒安装在关节上时可以移动。也可以约束绳索在卷筒中心平面内进入和离开卷筒。是否强制执行此约束取决于 Belt-Cable Properties 模块的设置。

卷筒以及缠绕在其上的绳索的惯性也被忽略。要捕获固定质量卷筒的惯性，请使用 Cylindrical Solid 或 Inertia 模块。如果模型中实体几何很重要，请考虑使用 Cylindrical Solid 模块。要捕获绳索在缠绕到卷筒上以及从卷筒退绕时的可变质量属性，请使用 Variable Solids 库中的模块——例如 Variable Cylindrical Solid 或 General Variable Mass。
