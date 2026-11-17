---
type: simulink-block
title: 'Distance Constraint'
family: 'constraints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Constraints'
documentation_page: 'distanceconstraint'
documentation_source_path: 'ref/distanceconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Distance Constraint

## 端口

该模块提供两个坐标系端口：

- B — 基础坐标系端口
- F — 从动坐标系端口

此外，该模块还提供两个物理信号输出端口：

- f — 距离约束力矢量
- fm — 距离约束力的带符号幅值

## 参数

**距离**
:   基础坐标系原点和从动坐标系原点之间的约束距离。
    该距离必须大于零。如果距离为零，请改用 Spherical Joint 或 Gimbal
    Joint 模块。默认值为 `1` m。

### 约束力检测

选择是否计算并输出距离约束力矢量及其带符号幅值。距离约束力是该模块为保持您在基础端口坐标系与从动端口坐标系之间指定的距离而必须施加的力。

**方向**
:   约束力成对作用。根据牛顿第三运动定律，如果基础端口坐标系对从动端口坐标系施加约束力，则从动端口坐标系必须对基础端口坐标系施加大小相等、方向相反的力。选择要检测两个约束力中的哪一个：

    - `Follower on Base` —
      检测从动端口坐标系施加在基础端口坐标系上的约束力。
    - `Base on Follower` —
      检测基础端口坐标系施加在从动端口坐标系上的约束力。

**分解坐标系**
:   该模块用约束力矢量的笛卡尔矢量分量来表示该矢量。将矢量拆分为矢量分量的过程称为矢量分解。其轴定义矢量分量方向的坐标系称为分解坐标系。选择是在基础端口坐标系还是从动端口坐标系中分解约束力矢量。

**力矢量**
:   计算并输出距离约束力矢量的笛卡尔分量。输出信号是三维矢量 [*f*x, *f*y, *f*z]。

**带符号力幅值**
:   计算并输出距离约束力的大小，包括其符号。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中推出**

## 描述

两个坐标系原点之间的固定距离

该模块使基础端口坐标系和从动端口坐标系的原点之间保持固定距离。这些坐标系相对于彼此失去一个平移自由度。坐标系原点之间的约束距离（图中标记为 *D*）必须大于零。

该模块以矢量或带符号幅值的形式提供约束力检测。这些量包含在模块通过 Simscape™ PS 端口输出的物理信号中。约束力是保持端口坐标系原点之间指定距离所需的力。
