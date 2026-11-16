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

### 守恒

### **S** — 鼓轴机械旋转

与鼓轴关联的机械旋转守恒端口。

### **A** — 绳索端 A 机械平移

与绳索端 A 关联的机械平移守恒端口。

### **B** — 绳索端 B 机械平移

与绳索端 B 关联的机械平移守恒端口。

## 参数

### 绳索卷绕

### **鼓半径** — 鼓的尺寸 `0.10` `m`（默认） | positive scalar

鼓中心与其外圆周之间的距离。鼓外圆周与鼓和绳索之间的接触面重合。

### **绳索卷绕类型** — B 绳索端相对于 A 绳索端的方向 `Ends move in same direction`（默认） | `Ends move in opposite direction`

两个绳索端 A 和 B 的平移运动的相对方向，其中 B 是从动端。

### **张力警告** — 可选的失张力警告 `Do not check tension`（默认） | `Warn if either end loses tension`

用于在绳索端变松时生成警告的选项。当用于保持其张紧的净拉力降到零以下时，绳索端会变松。由于松弛的缆索不传递力，当绳索失去张力时，仿真结果可能不准确。

### 鼓动力学

### **轴承黏性摩擦系数** — 鼓旋转的黏性摩擦 `0.001` `N*m/(rad/s)`（默认） | nonnegative scalar

鼓轴承处生效的线性阻尼系数。该系数确定在给定鼓角速度下由黏性摩擦引起的功率损耗。

### **惯量** — 对角加速度的阻力 `No inertia`（默认） | `Specify inertia and initial velocity`

用于考虑鼓惯量的选项。

- `No inertia` — 如果鼓惯量对传动系统动力学的影响可忽略，请选择此设置。此设置将鼓惯量设为零。
- `Specify inertia and initial velocity` — 如果鼓惯量对传动系统动力学有显著影响，请选择此设置。

### **鼓惯量** — 鼓保持运动的趋势 `0.01` `kg*m^2`（默认） | positive scalar

鼓绕其旋转轴的转动惯量。在实心圆柱鼓的简单情况下，转动惯量为

I=12MR2,

其中 *M* 是鼓质量，*R* 是鼓半径。

#### 依赖关系

要启用此参数，请将 **惯量** 设置为 `Specify inertia and initial velocity`。

### **鼓初始速度** — 鼓的初始状态 `0` `rad/s`（默认） | scalar

仿真开始时鼓的角速度。

#### 依赖关系

要启用此参数，请将 **惯量** 设置为 `Specify inertia and initial velocity`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

绳索紧密缠绕在圆柱鼓上的动力传输系统

Rope Drum 模块表示一种动力传输系统，其中绳索以足够的张力紧密缠绕在圆柱鼓上以防止打滑。您可以配置绳索，使两端指向相同或相反方向。您可以使用 **绳索卷绕类型** 参数设置两端移动的方向：

- 如果绳索端指向相同方向，则它们沿相反方向平移。
- 如果绳索端指向相反方向，则它们沿相同方向平移。

这些方程涉及绳索端 A 和 B，如图所示。

当绳索端 A 和 B 指向相同方向时，它们沿相反方向平移。当绳索端 A 和 B 指向相反方向时，它们沿相同方向平移。

在正常运行期间，驱动力矩使圆柱鼓绕其对称轴旋转。旋转的鼓将拉力传递给绳索端，绳索端相对于鼓中心线平移。两个绳索端之间的相对平移方向取决于 **绳索卷绕类型** 参数的设置。但是，正的鼓旋转始终对应于端口 **A** 处的正平移。

该模块假设每个绳索端在仿真期间保持张紧，因为松弛的绳索端不传递力。您可以将该模块设置为在绳索失去张力时向您发出警告。

您可以选择性地设置以下参数：

- 鼓惯量
- 鼓轴承处的黏性摩擦

该模块平衡转矩和力，使得

T=FB·R·δ−FA·R+μ·ω,

其中：

- *T* 是作用在鼓上的外部转矩。由于转矩平衡，作用在鼓上的外部转矩是作用在绳索端上的力所施加的净转矩的负值。
- *F*A 和 *F*B 是拉在绳索端 A 和 B 上的外部力。
- *R* 是鼓半径。
- *μ* 是鼓轴承处的黏性摩擦系数。
- *ω* 是鼓角速度。
- *δ* 是根据参数设置确定的绳索卷绕类型：

  - 当您将 **绳索卷绕类型** 设置为 `Ends move in the same direction` 时，*δ = -1*。
  - 当您将 **绳索卷绕类型** 设置为 `Ends move in the opposite directions` 时，*δ = +1*。

该图显示了交叉绳索配置和开放式绳索配置，它们分别对应于 `Ends move in the same direction` 和 `Ends move in the opposite directions` 设置。

在交叉绳索配置和开放式绳索配置中展示的与 Rope Drum 关联的变量。

两个绳索端的平移速度是鼓半径和角速度的函数。每个平移速度都等于鼓外圆周上某一点的切向速度，根据表达式

VA=ωRVB=δωR

其中：

- *V*A 是绳索端 A 的平移速度。
- *V*B 是绳索端 B 的平移速度。

### 假设和限制

- 该模块忽略绳索-鼓接触面处的滑动。
- 该模块忽略绳索柔度。
