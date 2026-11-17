---
type: simulink-block
title: 'Nonlinear Rotational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlinearrotationalspring'
documentation_source_path: 'ref/nonlinearrotationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Rotational Spring

## 端口

`C`
:   旋转守恒端口

`R`
:   旋转守恒端口

## 参数

**Parameterization**
:   选择弹簧参数化方式。选项为 `By
    polynomial` 和 `By table
    lookup`。

     By Polynomial

    以多项式系数形式指定非线性弹簧函数。

    **Symmetry**
    :   在对称和双侧多项式参数化之间选择。

        - `Symmetric` —
          指定一组多项式系数，用于控制拉伸和压缩时的弹簧扭矩。

          **Vector of spring coefficients**
          :   输入包含多项式弹簧系数的五元素向量。最高非零阶次必须为正。物理单位用于第一个系数。

              默认向量为 `[1 0 0.1 0
              0.01]`。默认单位为
              `N*m/rad`。
        - `Two-sided` —
          指定两组多项式系数，用于控制弹簧扭矩，一组用于正变形，另一组用于负变形。

          **Vector of spring tension coefficients**
          :   输入包含多项式弹簧*拉伸*函数系数的五元素向量。最高阶非零系数必须为正。指定的物理单位为第一个多项式系数的单位。

          **Vector of spring compression coefficients**
          :   输入包含多项式弹簧*压缩*函数系数的五元素向量。最高阶非零系数必须为正。指定的物理单位为第一个多项式系数的单位。

     By table lookup

    **Deformation vector**
    :   输入包含用于表格查找的变形值的向量。该向量必须包含基于插值方法的最少元素数量：`Linear` 为两个，`Smooth` 为三个。该向量还必须包含与扭矩向量相同数量的元素。

    **Torque vector**
    :   输入包含与变形向量值对应的扭矩值的向量。该向量必须包含基于插值方法的最少元素数量：`Linear` 为两个，`Smooth` 为三个。该向量还必须包含与变形向量相同数量的元素。如果向量中未包含，模块会自动在 (0,0) 变形–扭矩坐标处添加一个点。

    **Interpolation method**
    :   选择用于计算表格查找数据点之间变形–扭矩值的方法。

        - `Linear` — 选择此选项以获得最佳性能。
        - `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

        有关插值算法的更多信息，请参阅 PS Lookup Table
        (1D) 模块参考页。

    **Extrapolation method**
    :   选择用于计算表格查找数据范围之外的变形–扭矩值的方法。

        - `Linear` — 选择此选项以生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
        - `Nearest` — 选择此选项以生成不高于数据中最高点或不低于数据中最低点的外推。

        有关外推算法的更多信息，请参阅 PS Lookup Table
        (1D) 模块参考页。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

基于多项式或表格查找参数化的扭转弹簧

该模块表示具有非线性扭矩-位移曲线的扭转弹簧。弹簧扭矩大小为位移的一般函数。它无需满足胡克定律。多项式参数化和表格查找参数化提供了两种指定扭矩-位移关系的方式。弹簧扭矩可以关于零变形对称或不对称。

对称多项式参数化根据以下表达式定义弹簧扭矩：

T=k1θ+sign(θ)⋅k2θ2+k3θ3+sign(θ)⋅k4θ4+k5θ5,

其中：

- *T* — 弹簧力
- *k*1、
  *k*2、
  ...、*k*5 — 弹簧系数
- *θ* — 端口 R 和 C 之间的相对位移，θ=θinit+θR−θC
- *θ*init — 初始弹簧变形
- *θ*R — 端口 R 的绝对角位置
- *θ*C — 端口 C 的绝对角位置

在仿真开始时 (t=0)，*θ*R 和
*θ*C 为零，使 *θ*
等于 *θ*init。

为避免减慢仿真的零穿越，通过指定奇多项式（*b*2、*b*4
= 0）来消除多项式表达式中的符号函数。

双侧多项式参数化根据以下表达式定义弹簧扭矩：

T={k1tθ+k2tθ2+k3tθ3+k4tθ4+k5tθ5,θ≥0k1cθ−k2cθ2+k3cθ3−k4cθ4+k5cθ5,θ<0,

其中：

- *k*1t、
  *k*2t、...、
  *k*5t — 弹簧拉伸系数
- *k*1c、
  *k*2c、...、
  *k*5c — 弹簧压缩系数

两种多项式参数化均使用五阶多项式表达式。要使用较低阶多项式，请将不需要的高阶系数设置为零。要使用较高阶多项式，请拟合为较低阶多项式或使用表格查找参数化。

表格查找参数化基于一组扭矩和角速度向量定义弹簧扭矩。如果未指定，模块会自动在原点（零角速度和零扭矩）处添加一个数据点。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期大小的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。
