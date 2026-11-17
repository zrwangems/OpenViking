---
type: simulink-block
title: 'Synchronizer'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'synchronizer'
documentation_source_path: 'ref/synchronizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronizer

## 端口

### 输出

### **X1** — 犬牙离合器位移物理信号

物理信号输出端口，用于测量犬牙离合器位移的大小。

### **X2** — 锥形离合器位移物理信号

物理信号输出端口，用于测量锥形离合器位移的大小。
### 守恒

### **H** — 离合器轮毂机械旋转

与离合器轮毂关联的机械旋转守恒端口。

### **R** — 离合器齿圈机械旋转

与离合器齿圈关联的机械旋转守恒端口。

### **S** — 换挡连杆机械旋转

与换挡连杆关联的机械旋转守恒端口。

### **T** — 热流热

与热流关联的热守恒端口。

#### 依赖

要启用此端口，请在 **Friction** 部分中，将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 参数

### Cone Clutch

### **Contact surface maximum diameter** — 外径 `150` `mm`（默认）| 正标量

外锥直径 *do*。

### **Contact surface minimum diameter** — 内径 `100` `mm`（默认）| 正标量

内锥直径 *di*。

### **Cone half angle** — 锥半角 `12` `deg`（默认）| 正标量

锥形几何结构的半开角 *α*。

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度以及圆盘之间的相对角速度，通过查表定义动摩擦系数。

### **Relative velocity vector** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，以向量形式表示。向量中的值必须从左到右递增。最小值数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients`。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式表示。最小值数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静值或峰值，以向量形式表示。该向量的元素数量必须与温度向量相同。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Fixed kinetic friction coefficient`。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式表示。所有值必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量的元素数量必须与相对速度向量相同。
- `Temperature-dependent friction coefficients` — 该向量的元素数量必须与温度向量相同。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients`。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature and velocity-dependent friction coefficients`。

### **Friction coefficient interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Friction coefficient extrapolation method** — 外推方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表中指定范围之外时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及在与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点也不低于数据中最低点的外推。
- `Error` — 当您希望数据位于表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Velocity tolerance** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果扭矩小于有效半径、静摩擦系数和施加的法向力的乘积，则表面锁定。

### **Threshold force** — 法向接触力阈值 `1` `N`（默认）| 标量

力阈值。仅当法向力超过 **Threshold force** 参数的值时，模块才模拟法向力。否则，不会传递摩擦力矩。

### Dog Clutch

### **Torque transmission model** — 扭矩传递模型 `Friction clutch approximation — Suitable for HIL and linearization`（默认）| `Dynamic with backlash` | `Dynamic modal`

用于对 dog clutch 行为进行建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置对于实时仿真来说足够快，并且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒连接来控制换挡连杆。
- `Dynamic with backlash` — 高保真离合器接合模型，考虑了齿隙、扭转柔度和齿圈与轮毂齿之间的接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，可捕捉由于速度差导致的接合阻塞效应。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent friction coefficients`。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 递增值的向量

作为向量输入的温度值。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Maximum transmitted torque** — 最大传递扭矩 `1000` `N*m`（默认）| 正标量

离合器可以传递的最大扭矩，对应于非滑动接合配置。如果齿圈与轮毂之间传递的扭矩超过此值，则两个组件开始相对滑动。此扭矩决定了摩擦离合器近似中的静摩擦极限。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`。

### **Maximum transmitted torque vector** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认）| 向量

离合器可以传递的最大扭矩，对应于非滑动接合配置，指定为向量。如果齿圈与轮毂之间传递的扭矩超过此值，则两个组件开始相对滑动。此扭矩决定了摩擦离合器近似中的静摩擦极限。该向量的元素数量与温度向量相同。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **Extrapolation method** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外插方法：

- `Linear` — 选择此选项以生成在外插区域以及在与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点或低于数据中最低点的外插。
- `Error` — 当您希望数据位于表格范围内时，选择此选项以避免进入外插模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **Clutch teeth mean radius** — 离合器齿平均半径 `50` `mm`（默认）| 正标量

从齿圈或轮毂中心到相应齿中心的距离。给定两个组件之间的传递扭矩，平均齿半径决定了齿圈与轮毂齿之间的法向接触力。此参数的值必须大于零。

### **Number of teeth** — 齿圈或轮毂齿数 `6`（默认）| 正非零标量整数

齿圈或轮毂中的齿总数。两个组件的齿数相等。此参数的值必须大于或等于一。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Rotational backlash** — 旋转齿隙 `10` `deg`（默认）| 正标量

在接合离合器配置中，齿圈与轮毂齿之间允许的角运动或间隙。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Torsional stiffness** — 扭转刚度 `10e6` `N*m/rad`（默认）| 正标量

齿圈与轮毂齿之间接触界面处的线性扭转刚度系数。该系数表征两组齿之间接触力的恢复分量。刚度值越大，接触力越大。该参数的值必须大于零。默认值为 `10e6` `N*m/rad`。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Torsional damping** — 扭转阻尼 `100` `N*m/(rad/s)`（默认）| 正标量

齿圈与轮毂齿之间接触界面处的线性扭转阻尼系数。该系数表征两组齿之间接触力的耗散分量。阻尼值越大，接触过程中的能量耗散越大。该参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Engagement speed threshold** — 接合速度阈值 `5` `rpm`（默认）| 正标量

离合器传递动力的最低转速。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### Detent

### **Peak force** — 峰值力 `500` `N`（默认）| 非负标量

定位器的峰值剪切力。

### **Notch width** — 凹口宽度 `3` `mm`（默认）| 非负标量

定位器表现出剪切力的区域宽度。

### **Viscous friction coefficient** — 粘性摩擦系数 `0.1` `N/(m/s)`（默认）| 非负标量

定位器接触表面处的粘性摩擦系数。该参数的值必须大于或等于零。

### **Friction to peak force ratio** — 摩擦力与峰值力之比 `0.01`（默认）| 非负标量

定位器的动摩擦力与峰值剪切力之比。该参数用于设置动摩擦力的值。该参数必须大于或等于零。

### **Friction velocity threshold** — 动摩擦速度阈值 `0.05` `m/s`（默认）

定位器接触表面处达到峰值动摩擦力所需的速度。该参数确保当运动方向改变时力是连续的，从而提高仿真的数值稳定性。该参数必须大于零。默认值为 `0.05` `m/s`。

### Shift Linkage

### **Linkage travel direction** — 接合条件行程方向 `Positive shift linkage displacement engages clutch`（默认）| `Negative shift linkage displacement engages clutch`

换挡机构必须沿其运动以使离合器接合的方向。选项包括正位移和负位移。

### **Maximum engagement speed** — 接合速度上限阈值 `inf`（默认）| 正标量

齿圈与轮毂之间高于该相对角速度时离合器无法接合。该值特定于具体的变速箱或变速器。将该值最小化有助于避免接合过程中的高动态冲击。该参数的值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **Tooth overlap to engage** — 接合所需齿重叠量 `3` `mm`（默认）| 正标量

齿圈与轮毂齿沿公共纵向轴线的重叠长度。当齿重叠量大于此值时，离合器接合。在啮合齿轮齿重叠至少达到此长度之前，离合器保持分离状态。该值必须大于零。

### **Tooth height** — 齿高 `10` `mm`（默认）| 正标量

齿的根部与顶部之间的距离。齿圈和轮毂齿具有相同的高度。齿高和完全分离时的齿圈-轮毂间隙决定了换挡机构的最大行程范围。该参数的值必须大于零。

### **Ring-hub clearance when disengaged** — 分离时齿圈-轮毂间隙 `3` `mm`（默认）| 正标量

沿换挡机构平移轴线方向，齿圈与轮毂齿顶之间的最大开放间隙。该间隙对应于离合器完全分离状态。齿高和完全分离时的齿圈-轮毂间隙决定了换挡机构的最大行程范围。该参数的值必须大于零。

### **Hard stop at back of shift linkage** — 换挡机构后部硬限位 `on`（默认）| `off`

防止换挡机构运动超过完全分离位置的硬限位：

- 选中 — 完全分离时具有硬限位。
- 清除 — 完全分离时无硬限位。

### **Dog clutch ring stop stiffness** — 爪式离合器齿圈限位刚度 `10e5` `N/m`（默认）| 正标量

爪式离合器齿圈两侧硬限位的刚度。模型假设齿圈和限位表现为弹性行为。接触变形与施加的力成正比，与接触刚度的倒数成正比。刚度的取值必须参考参数 **Tooth overlap to engage** 进行设定。刚度过低可能导致变形超过所需重叠量并引发误接合。该参数必须大于零。

### **Cone clutch ring stop stiffness** — 锥式离合器齿圈限位刚度 `10e5` `N/m`（默认）| 正标量

锥式离合器齿圈两侧硬限位的刚度。模型假设齿圈和限位表现为弹性行为。接触变形与施加的力成正比，与接触刚度的倒数成正比。

### **Dog clutch ring stop damping** — 爪式离合器齿圈限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

爪式离合器齿圈与轮毂之间的平移接触阻尼。阻尼值与碰撞后发生的振荡次数成反比。

### **Cone clutch ring stop damping** — 锥式离合器齿圈限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

锥式离合器齿圈与轮毂之间的平移接触阻尼。阻尼值与碰撞后发生的振荡次数成反比。

### **Shift linkage viscous friction coefficient** — 换挡机构粘性摩擦系数 `100` `N/(m/s)`（默认）| 正标量

轮毂与齿圈之间相对平移运动的粘性摩擦系数。该参数的值取决于润滑状态和接触表面的质量。

### **Engagement block stiffness** — 接合阻挡刚度系数 `10e6` `N/m`（默认）| 正标量

阻挡接合时的刚度系数。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Engagement block damping** — 接合阻挡阻尼系数 `300` `N*s/m`（默认）| 正标量

阻挡接合时的阻尼系数。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Shift linkage engaged friction coefficient** — 接合摩擦系数 `100` `N*s/m`（默认）| 正标量

当齿环与轮毂接合时，换挡连杆处的摩擦系数。该值为换挡连杆与其支撑之间的摩擦力。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Shift linkage disengaged friction coefficient** — 分离摩擦系数 `50` `N*s/m`（默认）| 正标量

当齿环与轮毂分离时，换挡连杆处的摩擦系数。该值为换挡连杆与其支撑之间的摩擦力。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact speed threshold** — 静态接触速度阈值 `0.1` `m/s`（默认）| 正标量

速度阈值，低于该值时，齿环与轮毂要么完全接合并锁定，要么完全分离并锁定。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact release force threshold** — 释放力阈值 `0.001` `N`（默认）| 正标量

力阈值，高于该值时，齿环与轮毂可以解锁并分离。

#### 依赖关系

要启用此参数，请在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Tooth-tooth friction coefficient** — 齿对齿接触动摩擦系数 `0.05`（默认）| 正标量

齿环与轮毂齿之间接触界面处的动摩擦系数。该系数表征在离合器接合/分离过程中，由于齿对齿接触而阻碍换挡连杆运动的耗散力。

系数值越大，换挡连杆运动过程中的能量耗散越大。该参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### 初始条件

### **Initial state** — 初始离合器状态 `All clutches unlocked`（默认）| `Cone clutch locked` | `All clutches locked`

锥形离合器和爪形离合器的初始配置：

- `All clutches unlocked` — 锥形离合器和爪形离合器在齿环与轮毂轴之间传递零扭矩。
- `Cone clutch locked` — 锥形离合器在齿环与轮毂轴之间传递扭矩。
- `All clutches locked` — 锥形离合器和爪形离合器在齿环与轮毂轴之间传递扭矩。

### **Dog clutch initial shift linkage position** — 爪形离合器初始换挡连杆位置 `0` `mm`（默认）| 标量

连接到爪形离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| Linkage Travel Direction | Dog Clutch State | Parameter Restriction |
| --- | --- | --- |
| `Positive shift linkage displacement engages clutch` | 初始接合 | 参数必须大于参数 **Ring-hub clearance when dog clutch disengaged** 与 **Tooth overlap to engage** 之和 |
| 初始分离 | 参数必须小于参数 **Ring-hub clearance when dog clutch disengaged** 与 **Tooth overlap to engage** 之和 |
| `Negative shift linkage displacement engages clutch` | 初始接合 | 参数的负值必须大于参数 **Ring-hub clearance when dog clutch disengaged** 与 **Tooth overlap to engage** 之和 |
| 初始分离 | 参数的负值必须小于参数 **Ring-hub clearance when dog clutch disengaged** 与 **Tooth overlap to engage** 之和 |

### **Cone clutch initial shift linkage position** — 锥形离合器初始换挡连杆位置 `0` `mm`（默认）| 标量

连接到锥形离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| Linkage Travel Direction | Dog Clutch State | Parameter Restriction |
| --- | --- | --- |
| `Positive shift linkage displacement engages clutch` | 初始接合 | 参数必须大于 **Ring-hub clearance when cone clutch disengaged** 的值 |
| 初始分离 | 参数必须小于 **Ring-hub clearance when cone clutch disengaged** 的值 |
| `Negative shift linkage displacement engages clutch` | 初始接合 | 参数的负值必须大于 **Ring-hub clearance when dog cone disengaged** 的值 |
| 初始分离 | 参数的负值必须小于 **Ring-hub clearance when dog cone disengaged** 的值 |

### **Initial dog clutch ring-hub offset angle** — 初始爪形离合器齿环-轮毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时齿环与轮毂之间的旋转角度。该角度决定齿环与轮毂齿是否可以互锁，从而决定离合器是否可以接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，则初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N，

  其中 *N* 为齿环或轮毂中存在的齿数。两个部件包含相同数量的齿。
- 如果离合器初始状态为接合，则初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2，

  其中 *δ* 为齿环与轮毂齿之间的齿隙角。

#### 依赖关系

要启用此参数，

- 在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### Thermal Port

**Thermal Port** 设置仅在 **Cone Clutch** 设置中的 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时组件的温度。初始温度会根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2025a: Enumeration Updates

**Hard stop at back of shift linkage** 参数现在使用复选框。在之前的版本中，该参数使用下拉菜单。

### R2024a: Capture effects of engagement blocking due to speed differentials

当 **Torque transmission model** 为 `Dynamic modal` 时，您现在可以在系统级别捕获由于速度差导致的接合阻止效应。

## 描述

机械同步器

Synchronizer 模块表示一个同步器，包含牙嵌式离合器、锥形离合器和平移式定位器。同步器通过在接合前使齿轮速度相等，促进手动变速器的平顺换挡，减少齿轮冲击并确保不同传动比之间的无缝过渡。

换挡连杆首先平移以接合锥形离合器。摩擦力矩使换挡连杆和锥形离合器轴以相等速度旋转。当作用在换挡连杆上的力超过定位力时，牙嵌式离合器可以接合。

典型同步器的横截面。轮毂侧的锥形离合器与齿圈侧脱离接合。

该示意图展示了处于脱离接合状态的同步器。在此状态下，齿圈（R）和轮毂（H）轴可以以不同速度独立旋转。为了使齿圈和轮毂轴速度同步，换挡连杆（S）向轮毂轴方向平移以接合锥形离合器。锥形离合器的摩擦表面产生摩擦力矩，使齿圈和轮毂轴的转速相等。当作用在换挡连杆上的平移力超过峰值定位力时，牙嵌式离合器齿（T）可以接合。峰值定位力应允许有足够的时间和法向力来使齿圈和轮毂轴速度相等，以便牙嵌式离合器能够接合。

Dog Clutch 模块与 Cone Clutch 模块并联连接。Translational Detent 模块连接在它们的换挡连杆端口之间。

该模型实现了 Dog Clutch、Cone Clutch 和 Translational Detent 模块。有关相应模块功能的更多信息，请参阅各模块参考页。您可以使用类似的方法来建模同步器的定制版本。一个示例是 Vehicle with Manual Transmission 示例模型中的 Transmission (Detailed) 子系统。

连接 **R** 和 **H** 是机械旋转守恒端口，分别表示齿圈（R）和轮毂（H）。连接 **S** 是机械平移守恒端口，表示齿圈换挡手柄。

连接 **X1** 和 **X2** 是物理信号输出，分别报告牙嵌式离合器和锥形离合器的换挡连杆位置。当离合器完全脱离接合时，换挡连杆位置为零。当牙嵌式离合器完全接合时，牙嵌式离合器换挡连杆位置的幅值等于牙嵌式离合器齿圈-轮毂间隙与齿高之和。当锥形离合器完全接合时，锥形离合器换挡连杆位置的幅值等于锥形离合器齿圈-轮毂间隙。

### Dog Clutch Torque Transmission Models

你可以从这些扭矩传递模型中进行选择。

**Friction Clutch Approximate Model**

当您将 **Torque transmission model** 设置为
`Friction clutch approximation - Suitable for HIL
and` 时，该模块将离合器接合视为环与轮毂之间的摩擦
现象。此设置更适合
线性化、固定步长仿真和硬件在环（HIL）仿真。该
模块使用 Fundamental Friction Clutch
模块的复合实现。

当您使用此设置时，离合器有三种可能的配置：
分离、接合和锁定。分离时，环与轮毂之间的接触力为零。该力保持为零，直到换挡连杆
达到接合的最小位置。

当环-轮毂齿重叠量 *h* 超过接合的
最小值时，两个部件之间的接触力开始
随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到其最大值，离合器
状态切换为锁定。在此状态下，环和轮毂作为一个整体旋转
而不打滑。要解锁离合器，传递的扭矩必须超过
**Maximum transmitted torque** 参数的值。

**Dynamic with Backlash**

当您将 **Torque transmission model** 设置为
`Dynamic with backlash` 时，该模块仿真离合器
现象，例如齿隙、扭转柔度和环与轮毂齿之间的
接触力。此模型比摩擦
离合器近似提供更高的精度。

当您使用此设置时，离合器有两种可能的配置：
分离和接合。分离时，环与轮毂之间的接触力为零。该力保持为零，直到换挡连杆
达到接合的最小位置。

当环-轮毂齿重叠量 *h* 超过接合
阈值时，离合器传递扭矩。该扭矩是
扭转弹簧和阻尼器分量之和，包括环与
轮毂齿之间的齿隙，因此TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2，其中：

- *kRH* 是环-轮毂耦合的扭转
  刚度。
- *ϕ* 是环与轮毂之间绕共同
  旋转轴的相对角度。
- *δ* 是环与轮毂
  齿之间的齿隙。
- *ω* 是环与轮毂之间的相对角速度。此变量描述
  两个部件彼此滑过的速度。

柔顺端止点限制离合器换挡连杆和环的平移运动。
柔度模型将端止点视为线性弹簧-阻尼器
组。端止点的位置取决于环与轮毂齿之间的相对角度和角
速度：

- 如果齿对齐且相对角速度小于
  离合器接合的最大值，则端止点位置
  为完全分离时的环-轮毂间隙与
  齿高之和。离合器可在此端止点
  位置接合。
- 如果齿未对齐或相对角速度超过
  离合器接合的最大值，则设置端止点位置
  以防止环与轮毂接合。离合器不会
  在此端止点位置接合。

平移摩擦阻碍换挡连杆和环的运动。此摩擦是
库仑分量和黏性分量之和，因此FZ=−kK·FN·tanh(4vvth)−μTv，其中：

- *FZ* 是作用在换挡连杆和
  环上的净平移摩擦力。
- *kK* 是环与轮毂齿之间的动
  摩擦系数。
- *FN* 是环与轮毂齿之间的法向力，
  其中 *FN* =
  *TC*/*Rm*。
- *v* 是换挡连杆和环的平移
  速度。
- *vth* 是平移
  速度阈值。低于此阈值时，双曲正切
  函数将库仑摩擦力平滑至零，因为换挡
  连杆和环的速度趋于零。
- *μT* 是作用在换挡连杆和环上的黏性
  阻尼系数。

**Dynamic Modal**

当您将 **Torque transmission model** 设置为
`Dynamic modal` 时，该模块通过从机械
平移守恒端口 **S** 获取换挡连杆位置来确定离散
离合器模态行为。此设置比 `Two-mode` 参数化
捕获更复杂的离合器动力学，
并且比 `Friction clutch approximation`
和 `Dynamic with backlash` 设置更快。

您可以使用 `Dynamic modal` 设置来仿真
当速度差过大以致离合器片无法接合时的
接合阻塞。该模块将接合阻塞表示为弹簧-阻尼器系统，
您可以参数化弹簧和阻尼系数。接合
模式重叠，这防止模式改变，直到换挡连杆
位置超出接合重叠区域。您使用 **Tooth overlap to engage** 参数
定义接合重叠区域。

图示描绘了接合与分离之间的模式转换。z 变量表示换挡连杆位置。Engaged 和 Disengaged 模态区域重叠，这减弱了模式转换速率。

连杆位置约束为：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **Tooth height**
  参数。
- *zGap* 是
  **Ring hub clearance when disengaged**
  参数。
- *zOverlap* 是
  **Tooth overlap to engage** 参数。
- *ωthr* 是
  **Engagement speed threshold**
  参数。

接合模式位置为：

- *z* = 0 — 离合器完全分离。
- 0 < *z* <
  *zGap* — 当换挡连杆位置处于由
  *zGap* 定义的区域时，离合器分离。离合器
  可以在 *x* =
  *zGap* +
  *zOverlap* 处从分离转换为接合。
- *zGap* <
  *z* <
  *h* — 当 *z*
  处于由 *h* 定义的区域时，离合器接合。离合器可以在 *z* =
  *zGap* 时从接合转换为分离。
- *z* =
  *zGap* +
  *h* — 离合器完全接合。
- *z* =
  *zGap* +
  *zOverlap* — 当 *z* 处于接合
  重叠区域时，离合器仅在速度差
  小于
  *ωthr* 参数的值时接合。

### Thermal Modeling

您可以通过可选的热守恒端口来建模热流和温度变化的影响。默认情况下，热端口是隐藏的。要显示
热端口，请在 **Clutch** 设置中，为 **Friction model** 参数选择
与温度相关的设置。
指定组件的相关热参数。

### 假设和限制

- 该模型不考虑惯性效应。您可以在每个端口处添加一个 Simscape™
  Inertia 模块
  来为同步器模型添加惯性。
