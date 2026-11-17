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
```yaml
ports:
- name: S
  summary: 丝杠机械旋转
  direction: conserving
- name: N
  summary: 螺母机械平移
  direction: conserving
- name: H
  summary: 热流热
  direction: conserving
```

### 守恒端口

### **S** — 丝杠机械旋转

与丝杠关联的机械旋转守恒端口。

### **N** — 螺母机械平移

与螺母关联的机械平移守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Screw lead
  summary: 每转螺母位移 0.015 m（默认）| 正标量
  group: 主要
- name: Screw helix type
  summary: 旋转方向感 Right-hand（默认）| Left-hand
  group: 主要
- name: Friction model
  summary: 丝杠摩擦模型 No meshing losses — Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: 啮合损耗
- name: Friction parametrization
  summary: 齿轮螺纹非理想啮合引起的摩擦损耗 Friction coefficient and geometrical parameters（默认）| Efficiencies
  group: 啮合损耗
- name: Lead angle
  summary: 螺纹螺旋角 15 deg（默认）| 正标量
  group: 啮合损耗
- name: Acme thread half angle
  summary: 螺纹半角 14.5 deg（默认）| 正标量
  group: 啮合损耗
- name: Friction coefficient
  summary: 螺纹摩擦系数 0.08（默认）| 正标量
  group: 啮合损耗
- name: Screw-nut efficiency
  summary: 从丝杠到螺母的效率 0.75（默认）| (0,1] 范围内的正标量
  group: 啮合损耗
- name: Nut-screw efficiency
  summary: 从螺母到丝杠的效率 0.45（默认）| (0,1] 范围内的正标量
  group: 啮合损耗
- name: Temperature
  summary: 用于效率表格化参数化的数组 [280 300 320] K（默认）| 向量
  group: 啮合损耗
- name: Screw-nut efficiency
  summary: 丝杠到螺母效率数组 [0.75 0.7 0.65]（默认）| 向量
  group: 啮合损耗
- name: Nut-screw efficiency
  summary: 螺母到丝杠效率数组 [0.5 0.45 0.4]（默认）| 向量
  group: 啮合损耗
- name: Power threshold
  summary: 低于此功率时应用数值平滑 0.001 W（默认）| 正标量
  group: 啮合损耗
- name: Viscous friction coefficient
  summary: 流体动摩擦系数 0 N\*m/(rad/s)（默认）| 正标量
  group: 粘性损耗
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 正标量
  group: 热端口
- name: Initial temperature
  summary: 初始温度 300 K（默认）| 正标量
  group: 热端口
```

### 主要

### **Screw lead** — 每转螺母位移 `0.015` m（默认）| 正标量

丝杠每转一圈螺母的平移位移 *L*。

### **Screw helix type** — 旋转方向感 `Right-hand`（默认）| `Left-hand`

选择对应于正螺母平移的丝杠旋转方向感。对于 `Right-hand` 方向，丝杠角速度和螺母速度具有相同的符号。

### 啮合损耗

### **Friction model** — 丝杠摩擦模型 `No meshing losses — Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL simulation` — 丝杠啮合是理想的。
- `Constant efficiency` — 丝杠和螺母之间的扭矩传递因摩擦而减小。
- `Temperature-dependent efficiency` — 扭矩传递由用户提供的丝杠-螺母效率、螺母-丝杠效率和温度数据确定。

### **Friction parametrization** — 齿轮螺纹非理想啮合引起的摩擦损耗 `Friction coefficient and geometrical parameters`（默认）| `Efficiencies`

- `Friction coefficient and geometrical parameters` — 摩擦由表面之间的接触摩擦确定。
- `Efficiencies` — 摩擦由常数效率 0 < *η* < 1 确定。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Lead angle** — 螺纹螺旋角 `15` deg（默认）| 正标量

螺纹螺旋角 *λ* = arctan[*L*/(*π**d*)]，其中：

- *L* 是丝杠导程。
- *d* 是丝杠中径。

该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Acme thread half angle** — 螺纹半角 `14.5` deg（默认）| 正标量

法向平面内梯形螺纹的半角 *α*。对于方螺纹，*α* = 0。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Friction coefficient** — 螺纹摩擦系数 `0.08`（默认）| 正标量

螺纹中法向摩擦的无量纲系数。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Screw-nut efficiency** — 从丝杠到螺母的效率 `0.75`（默认）| (0,1] 范围内的正标量

从丝杠到螺母的功率传递效率 *η*SN。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Nut-screw efficiency** — 从螺母到丝杠的效率 `0.45`（默认）| (0,1] 范围内的正标量

从螺母到丝杠的功率传递效率 *η*NS。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Temperature** — 用于效率表格化参数化的数组 `[280 300 320]` K（默认）| 向量

用于构建一维温度-效率查找表的温度数组。数组值必须从左到右递增。温度数组的大小必须与 **Screw-nut efficiency** 和 **Nut-screw efficiency** 数组相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Screw-nut efficiency** — 丝杠到螺母效率数组 `[0.75 0.7 0.65]`（默认）| 向量

以丝杠为主动件的组件效率数组——即功率从丝杠传递到螺母。数组值为 **Temperature** 数组中各温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Nut-screw efficiency** — 螺母到丝杠效率数组 `[0.5 0.45 0.4]`（默认）| 向量

以螺母为主动件的组件效率数组——即功率从螺母流向丝杠。数组值为 **Temperature** 数组中各温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Power threshold** — 低于此功率时应用数值平滑 `0.001` W（默认）| 正标量

高于此功率阈值时，完整效率因子生效。双曲正切函数在静止时的零效率和当前效率设定点之间平滑效率因子。

### 粘性损耗

### **Viscous friction coefficient** — 流体动摩擦系数 `0` N\*m/(rad/s)（默认）| 正标量

丝杠的粘性摩擦系数 *μ*S。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 正标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 正标量

仿真开始时的组件温度。初始温度根据您指定的效率向量改变组件效率，影响起始啮合或摩擦损耗。
## 所属库

Simscape / Driveline / Gears / Rotational- Translational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

螺纹旋转丝杠和平移螺母的丝杠齿轮组，具有可调的螺纹和摩擦损耗

Leadscrew 模块表示一个螺纹旋转-平移齿轮，它将两个连接的动力传动轴——丝杠 (S) 和螺母 (N)——约束为按您指定的固定比率分别一起旋转和平移。您可以选择当丝杠沿正右手方向旋转时，螺母轴沿正方向还是负方向平移。如果丝杠螺旋为右旋，*ω*S 和 *v*N 具有相同的符号。如果丝杠螺旋为左旋，*ω*S 和 *v*N 具有相反的符号。

### 理想螺母约束和传动比

该模块对两个连接的轴施加一个运动学约束：

|  |  |
| --- | --- |
| *ω*S*L* = 2*π**v*N。 | **(1)** |

传动比为 *R*NS = 2*π*/*L*。*L* 是丝杠导程，即丝杠旋转一圈时螺母的平移位移。用该比率表示，运动学约束为：

|  |  |
| --- | --- |
| *ω*S = *R*NS*v*N。 | **(2)** |

两个自由度被缩减为一个独立自由度。正向传递齿轮对约定为 (1,2) = (S,N)。

扭矩-力传递为：

|  |  |
| --- | --- |
| *R*NS*τ*S + *F*N – *F*loss = 0， | **(3)** |

在理想情况下 *F*loss = 0。

### 非理想螺母约束和损耗

在非理想情况下，*F*loss ≠ 0。关于非理想齿轮建模的一般考虑，请参见 Model Gears with Losses。

**几何表面接触摩擦**

在接触摩擦情况下，*η*SN 和 *η*NS 由以下因素确定：

- 丝杠-螺母螺纹几何形状，由螺旋角 *λ* 和梯形螺纹半角 *α* 指定。
- 表面接触摩擦系数 *k*。

|  |  |
| --- | --- |
| *η*SN = (cos*α* – *k*·tan*α*)/(cos*α* + *k*/tan*λ*)， | **(4)** |

|  |  |
| --- | --- |
| *η*NS = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*α*)。 | **(5)** |

**常数效率**

在常数效率情况下，您指定 *η*SN 和 *η*NS，与几何细节无关。

**自锁和负效率**

*η*NS 有两种不同的状态，取决于螺旋角 *λ*，由 *自锁点* 分隔，在该点 *η*NS = 0 且 cos*α* = *k*/tan*λ*。

- 在 *超越状态* 中，*η*NS > 0。作用在螺母上的力可以使丝杠旋转。
- 在 *自锁状态* 中，*η*NS < 0。必须对丝杠施加外部扭矩才能释放原本锁定的机构。*η*NS 越负，释放机构所需的扭矩越大。

*η*SN 通常为正值。

### 啮合效率

丝杠和螺母之间啮合的效率 *η* 仅在传递功率大于功率阈值时才完全生效。

如果功率小于阈值，实际效率在零速度时自动正则化为 1。

### 粘性摩擦力

粘性摩擦系数 *μ* 控制丝杠从润滑的非理想齿轮螺纹中受到的粘性摩擦力矩。丝杠动力传动轴上的粘性摩擦力矩为 –*μ*S*ω*S。*ω*S 是丝杠相对于其安装座的角速度。

### 热建模

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 硬件在环仿真

为了获得实时仿真的最佳性能，请在 **Meshing Losses** 选项卡上将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation`。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。
