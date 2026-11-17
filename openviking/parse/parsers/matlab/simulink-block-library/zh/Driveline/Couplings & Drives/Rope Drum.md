---
type: simulink-block
title: 'Rope Drum'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'ropedrum'
documentation_source_path: 'ref/ropedrum.html'
language: zh-CN
chinese_source: worker-translation
---

# Rope Drum

## 端口
```yaml
ports:
- name: S
  summary: 卷筒轴机械旋转
  direction: conserving
- name: A
  summary: 绳索端 A 机械平移
  direction: conserving
- name: B
  summary: 绳索端 B 机械平移
  direction: conserving
```

### 守恒端口

### **S** — 卷筒轴机械旋转

与卷筒轴关联的机械旋转守恒端口。

### **A** — 绳索端 A 机械平移

与绳索端 A 关联的机械平移守恒端口。

### **B** — 绳索端 B 机械平移

与绳索端 B 关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Drum radius
  summary: 卷筒尺寸 0.10 m（默认）| 正标量
  group: 绳索缠绕
- name: Rope windup type
  summary: B 绳索端相对于 A 绳索端的方向 Ends move in same direction（默认）| Ends move in opposite direction
  group: 绳索缠绕
- name: Tension warning
  summary: 可选的张力丢失警告 Do not check tension（默认）| Warn if either end loses tension
  group: 绳索缠绕
- name: Bearing viscous friction coefficient
  summary: 卷筒旋转的粘性摩擦 0.001 N*m/(rad/s)（默认）| 非负标量
  group: 卷筒动力学
- name: Inertia
  summary: 对角加速度的阻力 No inertia（默认）| Specify inertia and initial velocity
  group: 卷筒动力学
- name: Drum inertia
  summary: 卷筒保持运动的趋势 0.01 kg*m^2（默认）| 正标量
  group: 卷筒动力学
- name: Drum initial velocity
  summary: 卷筒初始状态 0 rad/s（默认）| 标量
  group: 卷筒动力学
```

### 绳索缠绕

### **Drum radius** — 卷筒尺寸 `0.10` `m`（默认）| 正标量

卷筒中心与其外围之间的距离。卷筒外围与卷筒和绳索之间的接触面重合。

### **Rope windup type** — B 绳索端相对于 A 绳索端的方向 `Ends move in same direction`（默认）| `Ends move in opposite direction`

两个绳索端 A 和 B 的平移运动的相对方向，其中 B 是跟随端。

### **Tension warning** — 可选的张力丢失警告 `Do not check tension`（默认）| `Warn if either end loses tension`

当绳索端变松弛时生成警告的选项。当用于保持绳索张紧的净拉伸力降至零以下时，绳索端变松弛。由于松弛的缆绳不传递力，当绳索失去张力时仿真结果可能不准确。

### 卷筒动力学

### **Bearing viscous friction coefficient** — 卷筒旋转的粘性摩擦 `0.001` `N*m/(rad/s)`（默认）| 非负标量

作用于卷筒轴承的线性阻尼系数。该系数决定了在给定卷筒角速度下由于粘性摩擦导致的功率损耗。

### **Inertia** — 对角加速度的阻力 `No inertia`（默认）| `Specify inertia and initial velocity`

考虑卷筒惯性的选项。

- `No inertia` — 如果卷筒惯性对传动系统动力学的影响可忽略不计，请选择此设置。此设置将卷筒惯性设为零。
- `Specify inertia and initial velocity` — 如果卷筒惯性对传动系统动力学有显著影响，请选择此设置。

### **Drum inertia** — 卷筒保持运动的趋势 `0.01` `kg*m^2`（默认）| 正标量

卷筒绕其旋转轴的转动惯量。在实心圆柱形卷筒的简单情况下，转动惯量为

I=12MR2，

其中 *M* 是卷筒质量，*R* 是卷筒半径。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Drum initial velocity** — 卷筒初始状态 `0` `rad/s`（默认）| 标量

仿真开始时卷筒的角速度。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

绳索紧密缠绕在圆柱形卷筒上的动力传输系统

Rope Drum 模块表示一种动力传输系统，其中绳索以足够的张力水平紧密缠绕在圆柱形卷筒上以防止打滑。您可以配置绳索使其两端指向相同或相反的方向。您可以通过 **Rope windup type** 参数设置两端移动的方向：

- 如果绳索端指向相同方向，则它们沿相反方向平移。
- 如果绳索端指向相反方向，则它们沿相同方向平移。

方程中涉及绳索端 A 和 B，如图所示。

当绳索端 A 和 B 指向相同方向时，它们沿相反方向平移。当绳索端 A 和 B 指向相反方向时，它们沿相同方向平移。

在正常运行期间，驱动力矩使圆柱形卷筒绕其对称轴旋转。旋转的卷筒将拉伸力传递给绳索端，绳索端相对于卷筒中心线平移。两个绳索端之间的相对平移方向取决于 **Rope windup type** 参数的设置。然而，正的卷筒旋转始终对应于端口 **A** 处的正平移。

该模块假设每个绳索端在仿真期间保持张紧，因为松弛的绳索端不传递力。您可以设置模块在绳索失去张力时向您发出警告。

您可以选择性地设置以下参数：

- 卷筒惯性
- 卷筒轴承处的粘性摩擦

该模块平衡力矩和力，使得

T=FB·R·δ−FA·R+μ·ω，

其中：

- *T* 是作用于卷筒的外部力矩。由于力矩平衡，作用于卷筒的外部力矩等于作用于绳索端的力所施加的净力矩的负值。
- *F*A 和 *F*B 是拉动绳索端 A 和 B 的外部力。
- *R* 是卷筒半径。
- *μ* 是卷筒轴承处的粘性摩擦系数。
- *ω* 是卷筒角速度。
- *δ* 是根据参数设置的绳索缠绕类型：

  - 当您将 **Rope windup type** 设置为 `Ends move in the same direction` 时，*δ = -1*。
  - 当您将 **Rope windup type** 设置为 `Ends move in the opposite directions` 时，*δ = +1*。

该图展示了交叉绳索配置和开放式绳索配置，分别对应于 `Ends move in the same direction` 和 `Ends move in the opposite directions` 设置。

在交叉绳索配置和开放式绳索配置中演示的与 Rope Drum 相关的变量。

两个绳索端的平移速度是卷筒半径和角速度的函数。每个平移速度等于卷筒外围某点的切向速度，根据以下表达式

VA=ωRVB=δωR

其中：

- *V*A 是绳索端 A 的平移速度。
- *V*B 是绳索端 B 的平移速度。

### 假设和限制

- 该模块忽略绳索-卷筒接触面的打滑。
- 该模块忽略绳索的柔顺性。
