---
type: simulink-block
title: 'Reluctance Force Actuator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Elements'
documentation_page: 'reluctanceforceactuator'
documentation_source_path: 'ref/reluctanceforceactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Reluctance Force Actuator

## 端口
```yaml
ports: []
```

该模块具有以下端口：

`N`
:   与模块 North 端子关联的磁守恒端口。

`S`
:   与模块 South 端子关联的磁守恒端口。

`R`
:   与杆关联的机械平移守恒端口。

`C`
:   与壳体关联的机械平移守恒端口。
## 参数
```yaml
parameters: []
```

**Initial air gap**
:   仿真开始时的气隙厚度或长度。默认值为 `2` mm。

**Minimum air gap**
:   气隙的最小值，磁阻力作用于闭合气隙。该参数值必须大于 0。默认值为 `1e-4` mm。

**Cross-sectional area**
:   所建模截面的面积。默认值为 `0.01` m^2。

**Relative permeability of material**
:   截面材料的相对磁导率。默认值为 `1`。

**Contact stiffness**
:   用于模拟最小气隙位置处硬限位的刚度。默认值为 `10e6` N/m。

**Contact damping**
:   用于模拟最小气隙位置处硬限位的阻尼。默认值为 500 N/(m/s)。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

基于磁阻力的磁动设备

Reluctance Force Actuator 模块对基于磁阻力的通用磁动设备进行建模。

该模块基于以下方程：

F=−0.5⋅Φ2⋅dℜdx

ℜ(x)=xμ0⋅μr⋅A

u=dx

其中

|  |  |
| --- | --- |
| *F* | 磁阻力 |
| *Φ* | 磁路中的磁通量 |
| ℜ | 磁阻 |
| *x* | 气隙的厚度或长度 |
| *μ*0 | 磁导率常数 |
| *μ*r | 材料的相对磁导率 |
| *A* | 所建模截面的面积 |
| *u* | 速度 |

连接 N 和 S 为磁守恒端口，连接 C 和 R 为机械平移守恒端口。执行器产生的磁力作用于闭合气隙，因此当该力从 C 作用到 R 时，所产生的力为负值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
