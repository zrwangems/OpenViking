---
type: simulink-block
title: 'Leadscrew'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Rotational- Translational'
documentation_page: 'leadscrew'
documentation_source_path: 'ref/leadscrew.html'
language: zh-CN
chinese_source: worker-translation
---

# Leadscrew

## 端口

### 守恒

### **S** — 丝杠机械旋转

与丝杠关联的机械旋转守恒端口。

### **N** — 螺母机械平移

与螺母关联的机械平移守恒端口。

### **H** — 热流

与热流关联的热守恒端口。

## 参数

### 主要

### **Screw lead** — 每转的螺母位移 `0.015` m（默认）| positive scalar

丝杠每转一圈时螺母的平移位移 *L*。

### **Screw helix type** — 旋转方向 `Right-hand`（默认）| `Left-hand`

选择与正螺母平移相对应的丝杠旋转方向。对于 `Right-hand` 方向，丝杠角速度与螺母速度具有相同的符号。

### 啮合损失

### **Friction model** — 丝杠摩擦模型 `No meshing losses — Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL simulation` — 丝杠啮合是理想的。
- `Constant efficiency` — 丝杠与螺母之间的扭矩传递因摩擦而降低。
- `Temperature-dependent efficiency` — 扭矩传递由用户提供的丝杠-螺母效率、螺母-丝杠效率和温度数据确定。

### **Friction parametrization** — 来自齿轮螺纹非理想啮合的摩擦损失 `Friction coefficient and geometrical parameters`（默认）| `Efficiencies`

- `Friction coefficient and geometrical parameters` — 摩擦由表面之间的接触摩擦确定。
- `Efficiencies` — 摩擦由常量效率 0 < *η* < 1 确定。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Lead angle** — 螺纹螺旋角 `15` deg（默认）| positive scalar

螺纹螺旋角 *λ* = arctan[*L*/(*π**d*)]，其中：

- *L* 是丝杠导程。
- *d* 是丝杠中径。

该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Acme thread half angle** — 螺纹半角 `14.5` deg（默认）| positive scalar

法向平面中 Acme 螺纹的半角 *α*。对于方螺纹，*α* = 0。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Friction coefficient** — 螺纹摩擦系数 `0.08`（默认）| positive scalar

螺纹中法向摩擦的无量纲系数。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Screw-nut efficiency** — 从丝杠到螺母的效率 `0.75`（默认）| positive scalar in the range of (0,1]

从丝杠到螺母功率传递的效率 *η*SN。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Nut-screw efficiency** — 从螺母到丝杠的效率 `0.45`（默认）| positive scalar in the range of (0,1]

从螺母到丝杠功率传递的效率 *η*NS。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Temperature** — 用于效率表格参数化的数组 `[280 300 320]` K（默认）| vector

用于构造一维温度-效率查找表的温度数组。数组值必须从左到右递增。温度数组的大小必须与 **Screw-nut efficiency** 和 **Nut-screw efficiency** 数组相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Screw-nut efficiency** — 丝杠到螺母效率数组 `[0.75 0.7 0.65]`（默认）| vector

以丝杠为驱动件（即功率从丝杠流向螺母）的组件效率数组。数组值是 **Temperature** 数组中温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Nut-screw efficiency** — 螺母到丝杠效率数组 `[0.5 0.45 0.4]`（默认）| vector

以螺母为驱动件（即功率从螺母流向丝杠）的组件效率数组。数组值是 **Temperature** 数组中温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Power threshold** — 低于此功率时应用数值平滑 `0.001` W（默认）| positive scalar

高于此功率阈值时，完整效率因子生效。双曲正切函数在静止时的零与当前效率设定点之间平滑效率因子。

### 粘性损失

### **Viscous friction coefficient** — 流体动力摩擦系数 `0` N\*m/(rad/s)（默认）| positive scalar

丝杠的粘性摩擦系数 *μ*S。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| positive scalar

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗越强。

### **Initial temperature** — 初始温度 `300` `K`（默认）| positive scalar

仿真开始时的组件温度。初始温度根据您指定的效率向量改变组件效率，从而影响起始啮合损失或摩擦损失。

## 所属库

Simscape / Driveline / Gears / Rotational- Translational

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

Leadscrew 齿轮组：螺纹旋转丝杠和平移螺母，具有可调螺纹和摩擦损失

Leadscrew 模块表示一个螺纹旋转-平移齿轮，它将两个连接的动力传动轴——丝杠 (S) 和螺母 (N)——约束为分别以您指定的固定比率一起旋转和平移。当丝杠沿正右旋方向旋转时，您可以选择螺母轴沿正方向还是负方向平移。如果丝杠螺旋为右旋，则 *ω*S 和 *v*N 具有相同的符号。如果丝杠螺旋为左旋，则 *ω*S 和 *v*N 具有相反的符号。

### 理想螺母约束与传动比

该模块对两个连接轴施加一个运动学约束：

|  |  |
| --- | --- |
| *ω*S*L* = 2*π**v*N. | **(1)** |

传动比为 *R*NS = 2*π*/*L*。*L* 是丝杠导程，即丝杠转一圈时螺母的平移位移。用该比率表示，运动学约束为：

|  |  |
| --- | --- |
| *ω*S = *R*NS*v*N. | **(2)** |

两个自由度减少为一个独立自由度。正向传递齿轮对约定为 (1,2) = (S,N)。

扭矩-力传递为：

|  |  |
| --- | --- |
| *R*NS*τ*S + *F*N – *F*loss = 0, | **(3)** |

在理想情况下 *F*loss = 0。

### 非理想螺母约束与损失

在非理想情况下，*F*loss ≠ 0。有关非理想齿轮建模的一般考虑，请参阅 Model Gears with Losses。

**几何表面接触摩擦**

在接触摩擦情况下，*η*SN 和 *η*NS 由以下因素确定：

- 丝杠-螺母螺纹几何，由导程角 *λ* 和 Acme 螺纹半角 *α* 指定。
- 表面接触摩擦系数 *k*。

|  |  |
| --- | --- |
| *η*SN = (cos*α* – *k*·tan*α*)/(cos*α* + *k*/tan*λ*), | **(4)** |

|  |  |
| --- | --- |
| *η*NS = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*α*). | **(5)** |

**常量效率**

在常量效率情况下，您指定 *η*SN 和 *η*NS，与几何细节无关。

**自锁与负效率**

*η*NS 有两个不同区域，取决于导程角 *λ*，由 *self-locking point* 分隔，在该点 *η*NS = 0 且 cos*α* = *k*/tan*λ*。

- 在 *overhauling regime* 中，*η*NS > 0。作用在螺母上的力可以使丝杠旋转。
- 在 *self-locking regime* 中，*η*NS < 0。必须对丝杠施加外部扭矩才能释放原本锁定的机构。*η*NS 越负，释放机构所需的扭矩越大。

*η*SN 通常为正。

### 啮合效率

仅当传递功率大于功率阈值时，丝杠与螺母之间啮合的效率 *η* 才完全生效。

如果功率小于阈值，则实际效率会在零速度时自动正则化为 1。

### 粘性摩擦力

粘性摩擦系数 *μ* 控制丝杠因润滑的非理想齿轮螺纹而承受的粘性摩擦力矩。丝杠动力传动轴上的粘性摩擦力矩为 –*μ*S*ω*S。*ω*S 是丝杠相对于其安装座的角速度。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 硬件在环仿真

为获得实时仿真的最佳性能，请在 **Meshing Losses** 选项卡上将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation`。

### 变量

使用 **Variables** 设置可在仿真前为模块变量设置优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
