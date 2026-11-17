---
type: simulink-block
title: 'Rack & Pinion'
family: 'gears'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Rotational- Translational'
documentation_page: 'rackpinion'
documentation_source_path: 'ref/rackpinion.html'
language: zh-CN
chinese_source: worker-translation
---

# Rack & Pinion

## 端口

R2025b 中未记录。

## 参数

### 主要

### **Parameterize by** — 齿条和齿轮参数化方法 `Pinion radius`（默认）| `Tooth parameters`

齿条和小齿轮传动装置的参数化方法。

- `Pinion radius` — 传动比由小齿轮的有效半径定义。
- `Tooth parameters` — 传动比由小齿轮的齿数和齿条齿距定义。

### **Pinion radius** — 小齿轮有效半径 `100` mm（默认）| positive scalar

小齿轮的有效半径 *r*P。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Pinion radius`。

### **Number of pinion teeth** — 小齿轮齿数 `20`（默认）| positive scalar

小齿轮上的齿数 *N*P。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Tooth parameters`。

### **Rack tooth spacing** — 齿条上齿之间的间距 `5` mm（默认）| positive scalar

齿条上各齿之间的间距 *x*R。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Tooth parameters`。

### **Rack direction** — 齿条旋转方向 `Positive for positive pinion rotation`（默认）| `Negative for positive pinion rotation`

选择当小齿轮沿正方向旋转时，齿条轴沿正方向还是负方向平移。

### 啮合损失

### **Friction model** — 齿轮齿非理想啮合造成的摩擦损失 `No meshing losses — Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿条和小齿轮之间的扭矩传递因摩擦而降低。
- `Temperature-dependent efficiency` — 扭矩传递根据用户提供的效率和温度数据确定。

### **Efficiency** — 扭矩传递效率 `0.8`（默认）| positive scalar in the range of (0,1]

齿条-小齿轮啮合的扭矩传递效率 *η*，其对于正向和反向功率流相同。必须大于零且小于或等于一。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 用于效率表格化参数化的数组 `[280 300 320]` K（默认）| vector

用于构建一维温度-效率查找表的温度数组。数组值必须从左到右递增。温度数组的大小必须与 **Efficiency** 数组相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Efficiency** — 效率数组 `[0.95 0.9 0.85]`（默认）| vector

用于构建一维温度-效率查找表的部件效率数组。数组值是 **Temperature** 数组中各温度下的效率。两个数组必须大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Rack power threshold** — 应用数值平滑的功率下限 `0.001` W（默认）| positive scalar

功率阈值，高于该值时完整效率因子生效。低于此值时，双曲正切函数会平滑效率因子，当未传递功率时将效率损失降至零。

### 粘性损失

### **Pinion rotational viscous friction coefficient** — 小齿轮流体动力摩擦系数 `0` N\*m/(rad/s)（默认）| positive scalar

小齿轮轴的粘性摩擦系数 *μ*P。

### **Rack translational viscous friction coefficient** — 数值常量 `0` N/(m/s)（默认）| positive scalar

齿条运动的粘性摩擦系数 *μ*R。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| positive scalar

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗越强。

### **Initial temperature** — 初始温度 `300` `K`（默认）| positive scalar

仿真开始时的组件温度。初始温度会根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

## 所属库

Simscape / Driveline / Gears / Rotational- Translational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

齿条和小齿轮传动装置耦合平移和旋转运动，具有可调的小齿轮半径和摩擦损失

Rack & Pinion 模块表示在平移运动和旋转运动之间转换的齿条和小齿轮传动装置。该旋转-平移齿轮约束小齿轮 (P) 和齿条 (R) 分别以您指定的固定传动比一起旋转和平移。您可以使用 **Rack direction** 参数选择当小齿轮沿正方向旋转时，齿条轴平移的方向是正方向还是负方向。

### 模型变量

|  |  |
| --- | --- |
| *R*RP | 齿条-小齿轮传动比 |
| *ω*P | 小齿轮轴的角速度 |
| *v*R | 齿条的平移速度 |
| *r*P | 小齿轮的有效半径 |
| *N*P | 小齿轮齿数 |
| *x*R | 齿条齿距 |
| *τ*P | 小齿轮轴扭矩 |
| *F*R | 齿条力 |
| *F*loss | 总损失力 |
| *F*Coul | 摩擦力 |
| *η* | 扭矩传递效率 |
| *p*th | 功率阈值 |
| *μ*P | 小齿轮轴的粘性摩擦系数 |
| *μ*R | 齿条运动的粘性摩擦系数 |

### 理想齿轮约束和传动比

Rack & Pinion 对两个相连轴施加一个运动学约束：

|  |  |
| --- | --- |
| *ω*P = *R*RP*v*R. | **(1)** |

传动比为：

|  |  |
| --- | --- |
| *R*RP = 1 / *r*P = *ω*P / *v*N = ± 2*π* / *N*P*v*R. | **(2)** |

两个自由度被简化为一个独立自由度。正向传递齿轮对约定为 (1,2) = (P,R)。

扭矩-力传递为：

|  |  |
| --- | --- |
| *R*RP*τ*P + *F*R – *F*loss = 0, | **(3)** |

在理想情况下，*F*loss = 0。

### 非理想齿轮约束

在非理想情况下，*F*loss ≠ 0。关于非理想齿轮建模的一般注意事项，请参见 Model Gears with Losses。

在非理想小齿轮-齿条对 (P,R) 中，角速度和几何约束不变。但传递的扭矩、力和功率会因以下因素而降低：

- P 和 R 上齿面之间的库仑摩擦，由恒定效率 *η* 表征
- 驱动轴与轴承的粘性耦合，由粘性摩擦系数 *μ* 参数化

### 啮合效率

小齿轮和齿条之间啮合的效率 *η* 仅在传递功率大于功率阈值时完全生效。

如果功率小于阈值，实际效率会在零速度时自动正则化为 1。

对于正向和反向功率流，效率假设相等。

### 粘性摩擦力

粘性摩擦系数 *μ*P 和 *μ*R 控制齿条和小齿轮因润滑的非理想轴承而承受的粘性摩擦力矩和力。小齿轮轴上的粘性摩擦力矩为 –*μ*P*ω*P。齿条运动上的粘性摩擦力为 –*μ*R*v*R。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 硬件在环仿真

为获得实时仿真的最佳性能，请在 **Meshing Losses** 选项卡上将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation`。

### 变量

使用 **Variables** 设置来在仿真前为模块变量设置优先级和初始目标值。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。
