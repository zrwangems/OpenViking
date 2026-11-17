---
type: simulink-block
title: 'Angle Constraint'
family: 'constraints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Constraints'
documentation_page: 'angleconstraint'
documentation_source_path: 'ref/angleconstraint.html'
language: zh-CN
chinese_source: worker-translation
---

# Angle Constraint

## 端口

该模块提供两个坐标系端口：

- B — 基础坐标系端口
- F — 从动坐标系端口

此外，该模块还提供两个物理信号输出端口：

- t — 角度约束力矩矢量
- tm — 角度约束力矩的带符号幅值

## 参数

**类型**
:   角度约束类型。默认设置为
    `General`。

    | 类型 | 用途 |
    | --- | --- |
    | `Parallel` | 对齐基础坐标系和从动坐标系的 +Z 轴。 |
    | `Anti-Parallel` | 将基础坐标系的 +Z 轴与从动坐标系的 -Z 轴对齐。 |
    | `Perpendicular` | 使基础坐标系和从动坐标系的 Z 轴相互垂直。 |
    | `General` | 使基础端口坐标系和从动端口坐标系的 Z 轴之间保持指定角度。 |

**角度**
:   基础坐标系和从动坐标系 Z 轴之间的约束角度。该角度
    必须位于 0 < θ < 180 deg 范围内。对于 `0` 或
    `180` deg 的角度，请分别将**类型**设置为
    `Parallel` 或
    `Anti-Parallel`。默认值为
    `45` deg。

### 约束力矩检测

选择是否计算并输出距离约束力矩矢量及其
幅值。距离约束力矩是该模块为保持您在基础端口坐标系和从动端口
坐标系之间指定的角度而必须施加的力矩。

**方向**
:   约束力矩成对作用。根据牛顿第三运动定律，
    如果基础端口坐标系对从动端口坐标系施加约束力矩，
    则从动端口坐标系必须对基础端口坐标系施加大小相等、
    方向相反的力矩。选择要检测两个约束力矩中的哪一个：

    - `Follower on Base` — 检测从动端口坐标系对
      基础端口坐标系施加的约束力矩。
    - `Base on Follower` — 检测基础端口坐标系对
      从动端口坐标系施加的约束力矩。

**分解坐标系**
:   该模块以笛卡尔矢量分量的形式表示约束力矩矢量。
    将矢量拆分为矢量分量称为矢量分解。其轴定义
    矢量分量方向的坐标系称为分解坐标系。选择
    在基础端口坐标系还是从动端口坐标系中分解约束力矩矢量。

**力矩矢量**
:   计算并输出角度约束力矩矢量的笛卡尔分量。
    输出信号为三维矢量，其分量分别对应于分解
    坐标系的 X、Y 和 Z 轴。

**带符号力矩幅值**
:   计算并输出角度约束力矩的幅值，
    包括其符号。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中推出**

## 描述

两个坐标系 Z 轴之间的固定角度
