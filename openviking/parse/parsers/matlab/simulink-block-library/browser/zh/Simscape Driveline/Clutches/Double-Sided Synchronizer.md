---
type: simulink-block
title: 'Double-Sided Synchronizer'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'doublesidedsynchronizer'
documentation_source_path: 'ref/doublesidedsynchronizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Sided Synchronizer

## 端口

### 输出

### **X1** — Dog clutch translation physical signal

物理信号输出端口，用于测量犬牙离合器位移的大小。

### **X2** — Cone clutch translation physical signal

物理信号输出端口，用于测量锥形离合器位移的大小。
### 守恒

### **HA** — Clutch hub *A* mechanical rotational

与离合器毂 *A* 轴关联的机械旋转守恒端口。

### **HB** — Clutch hub *B* mechanical rotational

与离合器毂 *B* 轴关联的机械旋转守恒端口。

### **R** — Clutch ring mechanical rotational

与离合器环关联的机械旋转守恒端口。

### **S** — Shift linkage mechanical rotational

与换挡连杆关联的机械旋转守恒端口。

### **T** — Heat flow thermal

与热流关联的热守恒端口。

#### 依赖关系

要启用此参数，请在 **摩擦** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 参数

该表显示了 **锥形离合器** 和 **犬牙离合器** 设置中参数的指定选项如何影响以下项的可见性：

- **锥形离合器**、**犬牙离合器** 和 **初始条件** 设置中的参数
- **热端口** 设置
- 热端口 **T**

### 锥形离合器

### **接触面最大直径** — 外径 `150` `mm`（默认）| 正标量

外锥直径 *do*。

### **接触面最小直径** — 内径 `100` `mm`（默认）| 正标量

内锥直径 *di*。

### **锥半角** — 锥半角 `12` `deg`（默认）| 正标量

锥几何形状的半开口角 *α*。

### **摩擦模型** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，指定为向量。向量中的值必须从左到右递增。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients`。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，指定为向量。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，指定为向量。向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient`。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，指定为向量。所有值都必须大于零。

如果 **摩擦模型** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 向量必须与温度向量具有相同数量的元素。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients`。

### **动摩擦系数矩阵** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，指定为矩阵。所有值都必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature and velocity-dependent friction coefficients`。

### **摩擦系数插值方法** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **摩擦系数外插方法** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外插方法：

- `Linear` — 选择此选项以在外插区域以及与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点且不低于数据中最低点的外插。
- `Error` — 当您希望数据位于表范围内时，选择此选项以避免进入外插模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

低于该相对速度时，两个表面可以锁止。如果扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则这些表面锁止。

### **阈值力** — 法向接触力阈值 `1` `N`（默认）| 标量

力阈值。仅当法向力超过 **阈值力** 参数的值时，模块才会模拟该法向力。否则，不会传递摩擦力矩。

### 犬牙离合器

### **扭矩传递模型** — 扭矩传递模型 `Friction clutch approximation — Suitable for HIL and linearization`（默认）| `Dynamic with backlash` | `Dynamic modal`

用于对犬牙离合器行为进行建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置对于实时仿真足够快，并且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒连接来控制换挡连杆。
- `Dynamic with backlash` — 高保真离合器接合模型，该模型考虑了齿隙、扭转柔度以及环和毂齿之间的接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，可捕获由于速度差而导致的接合阻塞效应。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

锥形离合器的温度。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **最大传递扭矩** — 最大传递扭矩 `1000` `N*m`（默认）| 正标量

离合器能够传递的最大扭矩，对应于非滑动接合配置。如果环和毂之间传递的扭矩超过此值，则两个组件开始相对滑动。该扭矩确定摩擦离合器近似中的静摩擦极限

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙离合器** 部分中，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`。

### **最大传递扭矩向量** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认）| 向量

离合器能够传递的最大扭矩，对应于非滑动接合配置，指定为向量。如果环和毂之间传递的扭矩超过此值，则两个组件开始相对滑动。该扭矩确定摩擦离合器近似中的静摩擦极限。该向量与温度向量具有相同数量的元素。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **插值方法** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **外插方法** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外插方法：

- `Linear` — 选择此选项以在外插区域以及与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点且不低于数据中最低点的外插。
- `Error` — 当您希望数据位于表范围内时，选择此选项以避免进入外插模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **离合器齿平均半径** — 离合器齿平均半径 `50` `mm`（默认）| 正标量

从环或毂中心到对应齿中心的距离。在给定两个组件之间的传递扭矩的情况下，平均齿半径决定环齿和毂齿之间的法向接触力。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **齿数** — 环齿或毂齿的数量 `6`（默认）| 正非零标量整数

环或毂中的齿总数。两个组件具有相等的齿数。此参数的值必须大于或等于一。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **旋转齿隙** — 旋转齿隙 `10` `deg`（默认）| 正标量

在离合器接合配置中，环齿和毂齿之间允许的角运动或游隙。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **扭转刚度** — 扭转刚度 `10e6` `N*m/rad`（默认）| 正标量

环与毂齿之间接触界面处的线性扭转刚度系数。该系数表征两组齿之间接触力的恢复分量。刚度值越大，接触力越大。此参数的值必须大于零。默认值为 `10e6` `N*m/rad`。

#### 依赖关系

要启用此参数，在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并且在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **扭转阻尼** — 扭转阻尼 `100` `N*m/(rad/s)`（默认）| 正标量

环与毂齿之间接触界面处的线性扭转阻尼系数。该系数表征两组齿之间接触力的耗散分量。阻尼值越大，接触过程中的能量耗散越大。此参数的值必须大于零。

#### 依赖关系

要启用此参数，在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并且在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 棘爪

### **峰值力** — 峰值剪切力 `500` `N`（默认）| 非负标量

棘爪的峰值剪切力。

### **凹口宽度** — 凹口宽度 `3` `mm`（默认）| 非负标量

棘爪表现出剪切力的区域宽度。

### **粘性摩擦系数** — 粘性摩擦系数 `0.1` `N/(m/s)`（默认）| 非负标量

棘爪接触表面处的粘性摩擦系数。此参数的值必须大于或等于零。

### **摩擦力与峰值力之比** — 摩擦力与峰值力之比 `0.01`（默认）| 非负标量

棘爪的动摩擦力与峰值剪切力之比。该参数用于设置动摩擦力的值。该参数必须大于或等于零。

### **摩擦速度阈值** — 动摩擦速度阈值 `0.05` `m/s`（默认）

棘爪接触表面处达到峰值动摩擦力所需的速度。该参数确保当运动方向改变时力是连续的，从而提高仿真的数值稳定性。该参数必须大于零。默认值为 `0.05` `m/s`。

### 换挡机构

### **最大接合速度** — 接合速度上限速度阈值 `inf`（默认）| 正标量

环与毂之间的相对角速度，高于此值时离合器无法接合。该值特定于具体的变速箱或变速器。最小化该值有助于避免接合期间的高动态冲击。此参数的值必须大于零。

### **接合所需齿重叠** — 齿重叠接合阈值 `3` `mm`（默认）| 正标量

环与毂齿沿公共纵向轴线的重叠长度。当齿重叠大于此值时，离合器接合。在啮合齿轮齿重叠至少达到此长度之前，离合器保持分离。该值必须大于零。

### **齿高** — 齿高 `10` `mm`（默认）| 正标量

齿的基部和顶部之间的距离。环和毂齿具有相同的高度。齿高以及完全分离时的环-毂间隙决定了换挡机构的最大行程范围。此参数的值必须大于零。

### **分离时环-毂间隙** — 分离时环-毂间隙 `3` `mm`（默认）| 正标量

沿换挡机构平移轴线，环与毂齿顶之间的最大开口间隙。此间隙对应于离合器完全分离状态。齿高以及完全分离时的环-毂间隙决定了换挡机构的最大行程范围。此参数的值必须大于零。

### **换挡机构后部硬限位** — 硬限位模型 `On`（默认）| `Off`

防止换挡机构行程超过完全分离位置的硬限位：

- `On` — 完全分离时硬限位。
- `Off` — 完全分离时无硬限位。

### **牙嵌式离合器环限位刚度** — 牙嵌式离合器环限位刚度 `10e5` `N/m`（默认）| 正标量

牙嵌式离合器环两侧硬限位的刚度。模型假设环和限位表现为弹性。接触变形与施加的力成正比，与接触刚度的倒数成正比。刚度的值必须参考参数 **接合所需齿重叠** 进行分配。刚度过低可能导致变形超过所需重叠并引发错误接合。该参数必须大于零。

### **锥形离合器环限位刚度** — 锥形离合器环限位刚度 `10e5` `N/m`（默认）| 正标量

锥形离合器环两侧硬限位的刚度。模型假设环和限位表现为弹性。接触变形与施加的力成正比，与接触刚度的倒数成正比。

### **牙嵌式离合器环限位阻尼** — 牙嵌式离合器环限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

牙嵌式离合器环与毂之间的平移接触阻尼。阻尼值与撞击后发生的振荡次数成反比。该参数必须大于零。

### **锥形离合器环限位阻尼** — 锥形离合器环限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

锥形离合器环与毂之间的平移接触阻尼。阻尼值与撞击后发生的振荡次数成反比。该参数必须大于零。

### **换挡机构粘性摩擦系数** — 换挡机构粘性摩擦系数 `100` `N/(m/s)`（默认）| 正标量

毂与环之间相对平移运动的粘性摩擦系数。该参数的值取决于润滑状态和接触表面的质量。该系数必须大于或等于零。

### **接合阻塞刚度** — 接合阻塞刚度系数 `10e6` `N/m`（默认）| 正标量

接合阻塞期间的刚度系数。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **接合阻塞阻尼** — 接合阻塞阻尼系数 `300` `N*s/m`（默认）| 正标量

接合阻塞期间的阻尼系数。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **换挡机构接合摩擦系数** — 接合摩擦系数 `100` `N*s/m`（默认）| 正标量

环与毂接合时换挡机构处的摩擦系数。该值是换挡机构与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **换挡机构分离摩擦系数** — 分离摩擦系数 `50` `N*s/m`（默认）| 正标量

环与毂分离时换挡机构处的摩擦系数。该值是换挡机构与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触速度阈值** — 静态接触速度阈值 `0.1` `m/s`（默认）| 正标量

速度阈值，低于该值时环和毂要么完全接合并锁定，要么完全分离并锁定。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触释放力阈值** — 释放力阈值 `0.001` `N`（默认）| 正标量

力阈值，高于该值时环和毂可以解锁并分离。

#### 依赖关系

要启用此参数，在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **齿-齿摩擦系数** — 齿-齿接触动摩擦系数 `0.05`（默认）| 正标量

环与毂齿之间接触界面处的动摩擦系数。该系数表征由于离合器接合/分离期间齿-齿接触而阻碍换挡机构运动的耗散力。

系数值越大，换挡机构运动过程中的能量耗散越大。此参数的值必须大于零。

#### 依赖关系

要启用此参数，在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并且在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 初始条件

### **初始状态** — 初始离合器状态 `All clutches unlocked`（默认）| `Cone clutch A and dog clutch A locked` | `Cone clutch A locked` | `Cone clutch B locked` | `Cone clutch B and dog clutch B locked`

锥形离合器和牙嵌式离合器的初始配置：

- `Cone clutch A and dog clutch A locked` — 锥形离合器 *A* 和牙嵌式离合器 *A* 在环与毂轴之间传递扭矩。
- `Cone clutch A locked` — 锥形离合器 *A* 在环与毂轴之间传递扭矩。
- `All clutches unlocked` — 锥形离合器和牙嵌式离合器在环与毂轴之间传递零扭矩。
- `Cone clutch B locked` — 锥形离合器 *B* 在环与毂轴之间传递扭矩。
- `Cone clutch B and dog clutch B locked` — 锥形离合器 *B* 和牙嵌式离合器 *B* 在环与毂轴之间传递扭矩。

### **牙嵌式离合器初始换挡机构位置** — 牙嵌式离合器初始换挡机构位置 `0` `mm`（默认）| 标量

连接到牙嵌式离合器的换挡机构部分的初始位置。该参数的值具有以下限制：

| 牙嵌式离合器状态 | 参数限制 |
| --- | --- |
| 牙嵌式离合器 A 初始接合 | 参数值的负数必须大于参数 **牙嵌式离合器分离时环-毂间隙** 与 **接合所需齿重叠** 之和 |
| 牙嵌式离合器 A 初始分离 | 参数值的负数必须小于参数 **牙嵌式离合器分离时环-毂间隙** 与 **接合所需齿重叠** 之和 |
| 牙嵌式离合器 B 初始接合 | 参数值必须大于参数 **牙嵌式离合器分离时环-毂间隙** 与 **接合所需齿重叠** 之和 |
| 牙嵌式离合器 B 初始分离 | 参数值必须小于参数 **牙嵌式离合器分离时环-毂间隙** 与 **接合所需齿重叠** 之和 |

### **锥形离合器初始换挡机构位置** — 锥形离合器初始换挡机构位置 `0` `mm`（默认）| 标量

连接到锥形离合器的换挡机构部分的初始位置。该参数的值具有以下限制：

| 锥形离合器状态 | 参数限制 |
| --- | --- |
| 锥形离合器 A 初始接合 | 参数的负数必须大于 **锥形离合器分离时环-毂间隙** 的值 |
| 锥形离合器 A 初始分离 | 参数的负数必须小于 **锥形离合器分离时环-毂间隙** 的值 |
| 锥形离合器 B 初始接合 | 参数必须大于 **锥形离合器分离时环-毂间隙** 的值 |
| 锥形离合器 B 初始分离 | 参数必须小于 **锥形离合器分离时环-毂间隙** 的值 |

### **初始牙嵌式离合器 A 环-毂偏移角** — 初始牙嵌式离合器 *B* 环-毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时牙嵌式离合器 *B* 的环与毂之间的旋转角度。此角度决定环和毂齿是否可以互锁，从而决定离合器是否可以接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N,

  其中 *N* 是环或毂中存在的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2,

  其中 *δ* 是环和毂齿之间的间隙角。

#### 依赖关系

要启用此参数，

- 在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **初始牙嵌式离合器 B 环-毂偏移角** — 初始牙嵌式离合器 *A* 环-毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时环与毂之间的旋转角度。此角度决定环和毂齿是否可以互锁，从而决定离合器是否可以接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N,

  其中 *N* 是环或毂中存在的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2,

  其中 *δ* 是环和毂齿之间的间隙角。

#### 依赖关系

要启用此参数，

- 在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **牙嵌式离合器** 部分，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 热端口

要启用热建模，在 **锥形离合器** 部分，将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **热质量** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，在 **锥形离合器** 设置中，**摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`

### **初始温度** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的组件温度。初始温度根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

#### 依赖关系

仅当在 **锥形离合器** 设置中，**摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2024a：捕获由于速度差导致的接合阻塞效应

现在，当 **Torque transmission model** 为 `Dynamic modal` 时，您可以在系统级捕获由于速度差导致的接合阻塞效应。

## 描述

机械双面同步器

Double-Sided Synchronizer 模块表示一个双面同步器，该同步器包含两个背靠背的爪形离合器、两个背靠背的锥形离合器以及一个平移定位器。与常规同步器相比，双面同步器在变速器的输入侧和输出侧均同步并啮合齿轮。双面同步器可以同时接合和分离两根轴上的齿轮，从而支持更复杂的齿轮接合模式。重型商用车、非公路设备以及部分高性能汽车变速器通常使用这些同步器。

换挡连杆沿负方向平移会使离合器将环与毂 *A* 接合。换挡连杆沿正方向平移会使离合器将环与毂 *B* 接合。当换挡连杆平移的幅值小于锥形离合器环-毂间隙时，同步器处于空挡模式，不传递扭矩。

双面同步器的横截面，其中毂轴位于环轴的两侧。平移定位器将换挡连杆固定到位。

该示意图展示了一个处于分离状态的双面同步器。在此状态下，环 **R** 以及毂轴 **HA** 和 **HB** 可以以不同转速独立旋转。当换挡连杆 **S** 沿负方向平移时，锥形离合器 *A*（**CCA**）的端面开始接触。锥形离合器中的摩擦力减小轴之间的转速差。当换挡连杆上的力超过定位器 **D** 的峰值力时，爪形离合器齿 **T** 可以接合。定位器峰值力应使得锥形离合器有足够的时间和法向力使轴达到足够接近的转速，以允许爪形离合器接合。类似地，使换挡连杆沿正方向平移可使锥形离合器 *B*（**CCB**）的端面开始接触，并可允许环的轴与毂 *B*（**HB**）的轴接合。

Simscape 模型，展示了使用两个 Dog Clutch 模块与两个 Cone Clutch 模块并联的等效复合模块布置。一个 Translational Detent 模块连接在换挡连杆处，位于 Cone Clutch 模块和 Dog Clutch 模块之间。

该模型实现两个 Dog Clutch 模块、两个 Cone Clutch 模块和一个 Translational Detent 模块。有关相应模块功能的更多信息，请参阅每个模块的参考页。

连接 **R**、**HA** 和 **HB** 是机械旋转守恒端口，分别表示环 **R**、毂 *A*（**HA**）和毂 *B*（**HB**）。连接 **S** 是机械平移守恒端口，表示环换挡手柄。

连接 **X1** 和 **X2** 是物理信号端口，分别输出 Dog Clutch 和 Cone Clutch 的换挡连杆位置。下表提供了常见离合器接合情况下的 *X1* 和 *X2* 值。

| Dog Clutch 状态 | X1 |
| --- | --- |
| 分离 | 0 |
| 与毂 *A* 完全接合 | 环-毂间隙与齿高之和的负值 |
| 与毂 *B* 完全接合 | 环-毂间隙与齿高之和的正值 |

| Cone Clutch 状态 | X2 |
| --- | --- |
| 分离 | 0 |
| 与毂 *A* 完全接合 | 环-毂间隙的负值 |
| 与毂 *B* 完全接合 | 环-毂间隙的正值 |

当同步器完全分离时，*X1* 和 *X2* 的值均为零。当 Dog Clutch 与毂 *A* 完全接合时，*X1* 等于其环-毂间隙与齿高之和的负值。当 Dog Clutch 与毂 *B* 完全接合时，*X1* 等于其环-毂间隙与齿高之和的正值。当 Cone Clutch 与毂 *A* 完全接合时，*X2* 等于其环-毂间隙的负值。当 Cone Clutch 与毂 *B* 完全接合时，*X2* 等于其环-毂间隙。

### Dog Clutch 扭矩传递模型

您可以选择以下扭矩传递模型。

**摩擦离合器近似模型**

当您将 **Torque transmission model** 设置为
`Friction clutch approximation - Suitable for HIL
and` 时，模块将离合器接合视为环与毂之间的摩擦现象。此设置更适合线性化、固定步长仿真和硬件在环（HIL）仿真。模块使用 Fundamental Friction Clutch 模块的复合实现。

当您使用此设置时，离合器有三种可能的配置：分离、接合和锁定。当分离时，环与毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当环-毂齿重叠 *h* 超过接合的最小值时，两部件之间的接触力开始随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到其最大值，离合器状态切换为锁定。在此状态下，环与毂作为一个整体旋转而不打滑。要解锁离合器，传递的扭矩必须超过 **Maximum transmitted torque** 参数的值。

**带齿隙的动态模型**

当您将 **Torque transmission model** 设置为
`Dynamic with backlash` 时，模块会仿真离合器现象，例如齿隙、扭转柔度以及环与毂齿之间的接触力。此模型比摩擦离合器近似模型提供更高的精度。

当您使用此设置时，离合器有两种可能的配置：分离和接合。当分离时，环与毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当环-毂齿重叠 *h* 超过接合阈值时，离合器传递扭矩。此扭矩是扭转弹簧和阻尼器分量之和，包括环与毂齿之间的齿隙，因此TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2，其中：

- *kRH* 是环-毂耦合的扭转刚度。
- *ϕ* 是环与毂之间绕共同旋转轴的相对角度。
- *δ* 是环与毂齿之间的齿隙。
- *ω* 是环与毂之间的相对角速度。此变量描述两个部件彼此滑过的速度。

柔性端部止挡限制离合器换挡连杆和环的平移运动。柔度模型将端部止挡视为线性弹簧-阻尼器组。端部止挡的位置取决于环与毂齿之间的相对角度和角速度：

- 如果齿对齐且相对角速度小于离合器接合的最大值，则端部止挡位置为完全分离时的环毂间隙与齿高之和。离合器可在此端部止挡位置接合。
- 如果齿未对齐或相对角速度超过离合器接合的最大值，则设置端部止挡位置以阻止环与毂接合。离合器不会在此端部止挡位置接合。

平移摩擦阻碍换挡连杆和环的运动。此摩擦是库仑和粘性分量之和，因此FZ=−kK·FN·tanh(4vvth)−μTv，其中：

- *FZ* 是作用在换挡连杆和环上的净平移摩擦力。
- *kK* 是环与毂齿之间的动摩擦系数。
- *FN* 是环与毂齿之间的法向力，其中 *FN* = *TC*/*Rm*。
- *v* 是换挡连杆和环的平移速度。
- *vth* 是平移速度阈值。低于此阈值时，当换挡连杆和环的速度趋于零时，双曲正切函数将库仑摩擦力平滑至零。
- *μT* 是作用在换挡连杆和环上的粘性阻尼系数。

**动态模态**

当您将 **Torque transmission model** 设置为
`Dynamic modal` 时，模块通过从机械平移守恒端口 **S** 获取换挡连杆位置来确定离散离合器模态行为。此设置比 `Two-mode` 参数化捕获更复杂的离合器动力学，并且比 `Friction clutch approximation` 和 `Dynamic with backlash` 设置更快。

您可以使用 `Dynamic modal` 设置来仿真当速度差过大以致离合器片无法接合时的接合阻塞。模块将接合阻塞表示为弹簧-阻尼系统，您可以在其中参数化弹簧和阻尼系数。接合模式重叠，这会阻止模式发生变化，直到换挡连杆位置超出接合重叠区域。您使用 **Tooth overlap to engage** 参数定义接合重叠区域。

图示描绘了接合与分离之间的模式转换。变量 z 表示换挡连杆位置。接合和分离模态区域重叠，这会减弱模式转换速率。

连杆位置约束包括：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **Tooth height** 参数。
- *zGap* 是 **Ring hub clearance when disengaged** 参数。
- *zOverlap* 是 **Tooth overlap to engage** 参数。
- *ωthr* 是 **Engagement speed threshold** 参数。

接合模式位置为：

- *z* = 0 — 离合器完全分离。
- 0 < *z* < *zGap* — 当换挡连杆位置处于 *zGap* 定义的区域时，离合器分离。离合器可在 *x* = *zGap* + *zOverlap* 处从分离转换为接合。
- *zGap* < *z* < *h* — 当 *z* 处于 *h* 定义的区域时，离合器接合。离合器可在 *z* = *zGap* 处从接合转换为分离。
- *z* = *zGap* + *h* — 离合器完全接合。
- *z* = *zGap* + *zOverlap* — 当 *z* 处于接合重叠区域时，仅当速度差小于 *ωthr* 参数的值时，离合器才接合。

### 热建模

您可以通过可选的热守恒端口对热流和温度变化的影响进行建模。默认情况下，热端口处于隐藏状态。要显示热端口，请在 **Clutch** 设置中，为 **Friction model** 参数选择温度相关设置。指定该组件的相关热参数。
