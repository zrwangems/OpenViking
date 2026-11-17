---
type: simulink-block
title: 'Rotational Detent'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Rotational'
documentation_page: 'rotationaldetent'
documentation_source_path: 'ref/rotationaldetent.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Detent

## 端口

**R** 和 **C** 分别是与杆和壳体相关联的旋转守恒端口。

## 参数

### Detent Characteristics

**Parameterization**
:   选择如何指定棘轮特性。默认值为
    `By peak torque and notch width`。

    - `By peak torque and notch width` —
      通过峰值扭矩和凹口宽度指定棘轮特性。

       Peak Torque and Notch Width

      **Peak torque**
      :   棘轮内部产生的峰值扭矩。
          默认值为 `0.25`。

          从下拉列表中选择单位。默认值为牛顿-米
          (`N*m`)。

      **Notch width**
      :   扭矩产生区域的宽度。默认值为
          `5`。

          从下拉列表中选择单位。默认值为度
          (`deg`)。
    - `By table lookup` — 基于滑块与壳体之间的
      相对位移，通过一维查表定义棘轮
      特性。如果选择此选项，面板将从其默认选项切换。

       Table Lookup

      **Relative rotation vector**
      :   指定与 **Torque
          vector** 中的值相对应的输入相对旋转
          向量。这两个向量必须具有
          相同的大小。角度必须按
          严格递增的顺序指定。默认值为
          `[-5.0 -4.0 -3.0 -1.0 1.0 3.0 4.0
          5.0]`。

          从下拉列表中选择单位。默认值为度
          (`deg`)。

      **Torque vector**
      :   指定与
          **Relative rotation vector** 中的值相对应的
          所产生的扭矩的输入值向量。默认值为
          `[0 0 -0.25 -0.10 0.10
          0.25 0 0]`。

          从下拉列表中选择单位。默认值为牛顿-米
          (`N*m`)。

      **Initial relative rotation**
      :   仿真开始时杆与壳体的相对角度。
          默认值为
          `0`。

          从下拉列表中选择单位。默认值为度
          (`deg`)。

      **Interpolation method**
      :   选择以下插值方法之一，用于
          在输入值介于两个连续网格
          点之间时近似输出值：

          - `Linear` —
            选择此默认选项以获得最佳
            性能。
          - `Smooth` —
            选择此选项以生成具有连续一阶
            导数的连续曲线。

          有关插值算法的更多信息，请参阅 PS Lookup
          Table (1D) 模块参考页。

### Spacing

**Detent spacing**
:   选择如何指定棘轮间距。默认值为
    `Regularly spaced`。

    - `Regularly spaced` — 通过规则间隔指定棘轮
      间距。

       Regular spacing

      **Number of detents**
      :   指定相同且规则间隔的棘轮数量。
          必须大于或等于
          1。默认值为 `1`。

          创建从 –180 度到 +180 度均匀间隔的
          若干棘轮，其中一个棘轮中心位于 0
          度。非整数值将舍入为
          最接近的整数。
    - `By angle vector` — 通过自定义间隔指定棘轮
      间距。如果选择此选项，面板将从其默认选项切换。

       Custom intervals

      **Vector of detent centers**
      :   将相同棘轮中心的位置指定为
          角度向量。这些值必须介于 –180 和 +180 度之间。
          棘轮之间的最小间距必须
          大于 **Notch width**
          参数。默认值为 `[-40 0
          30 85]`。

          从下拉列表中选择单位。默认值为度
          (`deg`)。

### Friction

**Viscous friction coefficient**
:   指定杆-壳体接触的粘性摩擦系数。
    必须大于或等于 0。默认值为
    `0.1`。

    从下拉列表中选择单位。默认值为
    牛顿-米/(弧度/秒) (`N*m/(rad/s)`)。

**Friction to peak torque ratio**
:   指定杆-壳体接触的动摩擦系数。
    必须大于或等于 0。默认值为
    `0.01`。

    动摩擦为该比值乘以峰值
    扭矩。

**Friction velocity threshold**
:   指定棘轮中达到峰值动摩擦所需的
    相对角速度。必须大于 0。默认值为
    `10`。

    从下拉列表中选择单位。默认值为
    转/分钟 (`rpm`)。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

双面弹簧加载旋转棘轮

Rotational Detent 模块表示双面弹簧加载旋转
棘轮。

棘轮杆在棘轮壳体上旋转。壳体具有凹口或磁体，当杆旋转时
与杆产生净相对扭矩。使用该模块，您可以
通过峰值扭矩和凹口宽度，或通过查表来建模旋转棘轮。该
模型还包括杆与壳体之间的粘性阻尼和动摩擦。您
可以将摩擦设置为零。
