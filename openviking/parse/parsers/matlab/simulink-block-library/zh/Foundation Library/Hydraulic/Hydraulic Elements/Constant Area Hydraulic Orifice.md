---
type: simulink-block
title: 'Constant Area Hydraulic Orifice'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'constantareahydraulicorifice'
documentation_source_path: 'ref/constantareahydraulicorifice.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Area Hydraulic Orifice

## 端口

该模块具有以下端口：

`A`
:   与节流孔入口关联的液压守恒端口。

`B`
:   与节流孔出口关联的液压守恒端口。

## 参数

**Orifice area**
:   节流孔通道面积。默认值为 `1e-4`
    m^2。

**Flow discharge coefficient**
:   用于表征节流孔容量的半经验参数。其值
    取决于节流孔的几何特性，通常由教科书或制造商数据手册
    提供。默认值为
    `0.7`。

**Laminar transition specification**
:   选择模块在层流和湍流
     regime 之间过渡的方式：

    - `Pressure ratio` — 从层流到湍流 regime 的过渡
      是平滑的，取决于
      **Laminar flow pressure ratio** 参数的值。
      此方法提供更好的仿真鲁棒性。
    - `Reynolds number` — 假定从层流到湍流 regime 的过渡
      在雷诺数达到
      **Critical Reynolds number** 参数指定的值时
      发生。

**Laminar flow pressure ratio**
:   流动在层流和湍流
    regime 之间过渡时的压力比。默认值为 `0.999`。此参数
    仅在 **Laminar transition specification**
    参数设置为 `Pressure ratio` 时可见。

**Critical Reynolds number**
:   层流的最大雷诺数。该参数的值
    取决于节流孔几何轮廓。您可以在
    水力学教科书中找到有关该参数值的建议。默认值为
    `12`，对应于薄材料中带锐边的圆形节流孔。此参数仅在
    **Laminar transition specification** 参数设置为
    `Reynolds number` 时可见。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和
数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）具有恒定横截面积的液压节流孔

Constant Area Hydraulic Orifice 模块对锐边
恒定面积节流孔进行建模。通过节流孔的流量与节流孔两端的压差
成正比，并根据以下方程确定：

q=CD⋅A2ρ⋅p(p2+pcr2)1/4

p=pA−pB

其中

|  |  |
| --- | --- |
| *q* | 流量 |
| *p* | 压差 |
| *p*A, *p*B | 模块端子处的表压 |
| *C*D | 流量系数 |
| *A* | 节流孔通道面积 |
| *ρ* | 流体密度 |
| *p*cr | 湍流的最小压力，此时模块从层流 regime 过渡到湍流 regime |

湍流的最小压力
*p*cr 根据层流过渡指定方法计算：

- 按压力比 — 从层流到湍流 regime 的过渡由以下方程
  定义：

  *p*cr =
  (*p*avg +
  *p*atm)(1 –
  *B*lam)

  *p*avg =
  (*p*A +
  *p*B)/2

  其中

  |  |  |
  | --- | --- |
  | *p*avg | 模块端子之间的平均压力 |
  | *p*atm | 大气压，101325 Pa |
  | *B*lam | 层流和湍流 regime 之间过渡时的压力比（**Laminar flow pressure ratio** 参数值） |
- 按雷诺数 — 从层流到湍流 regime 的过渡由以下方程
  定义：

  pcr=ρ2(Recr⋅νCD⋅DH)2

  DH=4Aπ

  其中

  |  |  |
  | --- | --- |
  | *D*H | 节流孔水力直径 |
  | *ν* | 流体运动粘度 |
  | *Re*cr | 临界雷诺数（**Critical Reynolds number** 参数值） |

模块正方向为从端口 A 到端口 B。这意味着如果流量
从 A 流向 B，则流量为正，并且压差确定为 p=pA−pB。
