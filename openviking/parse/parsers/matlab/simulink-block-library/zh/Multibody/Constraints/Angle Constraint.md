---
type: simulink-block
title: 'Angle Constraint'
family: 'sm'
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
```yaml
ports: []
```

该模块提供两个坐标系端口：

- B — 基座坐标系端口
- F — 从动坐标系端口

此外，该模块还提供两个物理信号输出端口：

- t — 角度约束力矩向量
- tm — 角度约束力矩的带符号幅值
## 参数
```yaml
parameters: []
```

**类型**：角度约束类型。默认设置为
    `General`。

    | Type | 用途 |
    | --- | --- |
    | `Parallel` | 对齐基座和从动坐标系的 +Z 轴。 |
    | `Anti-Parallel` | 将基座坐标系 +Z 轴与从动坐标系 -Z 轴对齐。 |
    | `Perpendicular` | 使基座和从动坐标系的 Z 轴相互垂直。 |
    | `General` | 保持基座和从动端口坐标系 Z 轴之间的指定角度。 |

**Angle**
:   基座和从动坐标系 Z 轴之间的约束角度。该角度
    必须位于 0 < θ < 180 deg 范围内。对于 `0` 或
    `180` deg 的角度，请将 **Type** 设置为
    `Parallel` 或
    `Anti-Parallel`。默认值为
    `45` deg。

### 约束力矩感测

选择是否计算并输出距离约束力矩向量及其
幅值。距离约束力矩是该模块为保持基座和从动端口
坐标系之间指定的角度而必须施加的力矩。

**Direction**
:   约束力矩成对作用。如牛顿第三运动定律
    所述，如果基座端口坐标系对
    从动端口坐标系施加约束力矩，则从动端口坐标系必须对基座端口坐标系施加大小相等
    且方向相反的力矩。选择要感测的两个
    约束力矩中的哪一个：

    - `Follower on Base` — 感测
      从动端口坐标系对
      基座端口坐标系施加的约束力矩。
    - `Base on Follower` — 感测
      基座端口坐标系对
      从动端口坐标系施加的约束力矩。

**Resolution Frame**
:   该模块以其笛卡尔向量分量表示约束力矩向量。将向量
    分解为向量
    分量称为向量分解。其坐标轴定义
    向量分量方向的坐标系称为分解坐标系。选择
    在基座还是从动
    端口坐标系中分解约束力矩向量。

**Torque Vector**
:   计算并输出角度约束
    力矩向量的笛卡尔分量。输出信号是一个三维向量，其
    分量以分解坐标系的 X、Y 和 Z 轴表示。

**Signed Torque Magnitude**
:   计算并输出角度约束力矩的幅值，
    包括其符号。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

两个坐标系 Z 轴之间的固定角度
