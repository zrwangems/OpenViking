---
type: simulink-block
title: 'Distance Constraint'
family: 'sm'
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

此外，该模块还提供两个物理信号
输出端口：

- f — 距离约束力向量
- fm — 距离约束力的
  带符号幅值

## 参数

**距离**
:   基础坐标系与从动坐标系原点之间的约束距离。
    该距离必须大于零。对于零距离，请改用
    Spherical Joint 或 Gimbal
    Joint 模块。默认值为 `1` m。

### 约束力传感

选择是否计算并输出距离约束力向量及其带符号的幅值。距离约束力是该模块为保持您指定的基座端口坐标系与从动端口坐标系之间的距离而必须施加的力。

**方向**
:   约束力成对出现。如牛顿第三运动定律所述，如果基座端口坐标系对从动端口坐标系施加约束力，则从动端口坐标系必须对基座端口坐标系施加大小相等、方向相反的力。选择要感测这两个约束力中的哪一个：

    - `Follower on Base` —
      感测从动端口坐标系对基座端口坐标系施加的约束力。
    - `Base on Follower` —
      感测基座端口坐标系对从动端口坐标系施加的约束力。

**分解坐标系**
:   该模块以约束力向量的笛卡尔向量分量来表示该向量。将向量拆分为向量分量的过程称为向量分解。其各轴定义向量分量方向的坐标系称为分解坐标系。选择是在基座端口坐标系还是从动端口坐标系中分解约束力向量。

**力向量**
:   计算并输出距离约束力向量的笛卡尔分量。输出信号为三维向量 [*f*x, *f*y, *f*z]。

**带符号的力幅值**
:   计算并输出距离约束力的幅值，包括其符号。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**于 R2012a 推出**

## 描述

两个坐标系原点之间的固定距离

此模块在基础端口和从动端口坐标系的原点之间施加固定距离约束。这两个坐标系相对于彼此失去一个平移自由度。图中标记为 *D* 的坐标系原点之间的约束距离必须大于零。

此模块以向量或带符号幅值的形式提供约束力感测。这些量包含在模块通过 Simscape™ PS 端口输出的物理信号中。约束力是维持端口坐标系原点之间指定距离所需的力。
