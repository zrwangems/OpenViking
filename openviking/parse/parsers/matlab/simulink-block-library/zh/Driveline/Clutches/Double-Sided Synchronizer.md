---
type: simulink-block
title: 'Double-Sided Synchronizer'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
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

### **X1** — 犬牙式离合器位移物理信号

物理信号输出端口，用于测量犬牙式离合器位移的大小。

### **X2** — 锥形离合器位移物理信号

物理信号输出端口，用于测量锥形离合器位移的大小。
### 守恒

### **HA** — 离合器轮毂 *A* 机械旋转

与离合器轮毂 *A* 轴关联的机械旋转守恒端口。

### **HB** — 离合器轮毂 *B* 机械旋转

与离合器轮毂 *B* 轴关联的机械旋转守恒端口。

### **R** — 离合器齿圈机械旋转

与离合器齿圈关联的机械旋转守恒端口。

### **S** — 换挡连杆机械旋转

与换挡连杆关联的机械旋转守恒端口。

### **T** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

要启用此参数，请在**摩擦**部分中，将**摩擦模型**设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 参数

下表显示了在**锥形离合器**和**犬牙式离合器**设置中指定的参数选项如何影响以下内容的可见性：

- **锥形离合器**、**犬牙式离合器**和**初始条件**设置中的参数
- **热端口**设置
- 热端口 **T**

### 锥形离合器

### **接触面最大直径** — 外径 `150` `mm`（默认）| 正标量

外锥直径 *do*。

### **接触面最小直径** — 内径 `100` `mm`（默认）| 正标量

内锥直径 *di*。

### **锥半角** — 锥半角 `12` `deg`（默认）| 正标量

锥形几何结构的半开角 *α*。

### **摩擦模型** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度通过查表定义动摩擦系数。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，以向量形式指定。向量中的值必须从左到右递增。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients`。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式指定。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，以向量形式指定。该向量的元素数量必须与温度向量相同。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Fixed kinetic friction coefficient`。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式指定。所有值必须大于零。

如果**摩擦模型**参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量的元素数量必须与相对速度向量相同。
- `Temperature-dependent friction coefficients` — 该向量的元素数量必须与温度向量相同。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients`。

### **动摩擦系数矩阵** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式指定。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Temperature and velocity-dependent friction coefficients`。

### **摩擦系数插值方法** — 插值方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **摩擦系数外推方法** — 外推方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及在与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当您希望数据在表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将**摩擦模型**设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则表面锁定。

### **阈值力** — 法向接触力阈值 `1` `N`（默认）| 标量

力阈值。仅当法向力超过**阈值力**参数的值时，模块才模拟法向力。否则，不会传递摩擦力矩。

### 犬牙式离合器

### **扭矩传递模型** — 扭矩传递模型 `Friction clutch approximation — Suitable for HIL and linearization`（默认）| `Dynamic with backlash` | `Dynamic modal`

用于对犬牙式离合器行为建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置足够快，可用于实时仿真，且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒连接来控制换挡连杆。
- `Dynamic with backlash` — 高保真离合器接合模型，考虑了齿圈与轮毂齿之间的齿隙、扭转柔度和接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，可捕捉由于速度差导致的接合阻塞效应。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

锥形离合器的温度。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **最大传递扭矩** — 最大传递扭矩 `1000` `N*m`（默认）| 正标量

离合器在非滑动接合配置下能够传递的最大扭矩。如果齿圈与轮毂之间传递的扭矩超过此值，两个组件将开始相对滑动。此扭矩决定了摩擦离合器近似中的静摩擦极限。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在**犬牙式离合器**部分中，将**扭矩传递模型**设置为 `Friction clutch approximation - Suitable for HIL and linearization`。

### **最大传递扭矩向量** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认）| 向量

离合器在非滑动接合配置下能够传递的最大扭矩，以向量形式指定。如果齿圈与轮毂之间传递的扭矩超过此值，两个组件将开始相对滑动。此扭矩决定了摩擦离合器近似中的静摩擦极限。该向量的元素数量与温度向量相同。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **插值方法** — 插值方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **外推方法** — 外推方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及在与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当您希望数据在表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **离合器齿平均半径** — 离合器齿平均半径 `50` `mm`（默认）| 正标量

从齿圈或轮毂中心到相应齿中心的距离。给定两个组件之间的传递扭矩，平均齿半径决定了齿圈与轮毂齿之间的法向接触力。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent kinetic friction coefficient`。

### **齿数** — 齿圈或轮毂齿数 `6`（默认）| 正非零标量整数

齿圈或轮毂中的齿总数。两个组件的齿数相等。此参数的值必须大于或等于一。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在**犬牙式离合器**部分中，将**扭矩传递模型**设置为 `Dynamic with backlash`。

### **旋转齿隙** — 旋转齿隙 `10` `deg`（默认）| 正标量

在接合离合器配置中，齿圈与轮毂齿之间允许的角运动或游隙。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在**犬牙式离合器**部分中，将**扭矩传递模型**设置为 `Dynamic with backlash`。

### **Torsional stiffness** — 扭转刚度 `10e6` `N*m/rad`（默认）| 正标量

齿圈与轮毂齿之间接触界面处的线性扭转刚度系数。该系数表征两组齿之间接触力的恢复分量。刚度值越大，接触力越大。该参数的值必须大于零。默认值为 `10e6` `N*m/rad`。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Torsional damping** — 扭转阻尼 `100` `N*m/(rad/s)`（默认）| 正标量

齿圈与轮毂齿之间接触界面处的线性扭转阻尼系数。该系数表征两组齿之间接触力的耗散分量。阻尼值越大，接触过程中的能量耗散越大。该参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### Detent

### **Peak force** — 峰值剪切力 `500` `N`（默认）| 非负标量

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

### **Maximum engagement speed** — 接合速度上限阈值 `inf`（默认）| 正标量

齿圈与轮毂之间的相对角速度，超过该值时离合器无法接合。该值特定于具体的变速箱或变速器。最小化该值有助于避免接合过程中的高动态冲击。该参数的值必须大于零。

### **Tooth overlap to engage** — 齿重叠接合阈值 `3` `mm`（默认）| 正标量

齿圈与轮毂齿沿公共纵向轴线的重叠长度。当齿重叠大于此值时，离合器接合。在啮合齿重叠至少达到此长度之前，离合器保持分离状态。该值必须大于零。

### **Tooth height** — 齿高 `10` `mm`（默认）| 正标量

齿的根部与顶部之间的距离。齿圈和轮毂齿具有相同的高度。齿高和完全分离时的齿圈-轮毂间隙决定了换挡连杆的最大行程范围。该参数的值必须大于零。

### **Ring-hub clearance when disengaged** — 分离时齿圈-轮毂间隙 `3` `mm`（默认）| 正标量

沿换挡连杆平移轴线方向，齿圈与轮毂齿顶之间的最大开放间隙。该间隙对应于离合器完全分离状态。齿高和完全分离时的齿圈-轮毂间隙决定了换挡连杆的最大行程范围。该参数的值必须大于零。

### **Hard stop at back of shift linkage** — 硬限位模型 `On`（默认）| `Off`

防止换挡连杆越过完全分离位置的硬限位：

- `On` — 完全分离时硬限位。
- `Off` — 完全分离时无硬限位。

### **Dog clutch ring stop stiffness** — 犬牙离合器齿圈限位刚度 `10e5` `N/m`（默认）| 正标量

犬牙离合器齿圈两侧硬限位的刚度。模型假设齿圈和限位表现为弹性行为。接触变形与施加的力成正比，与接触刚度的倒数成正比。刚度的值必须参考参数 **Tooth overlap to engage** 来分配。刚度过低可能导致变形超过所需的重叠量并引发误接合。该参数必须大于零。

### **Cone clutch ring stop stiffness** — 锥形离合器齿圈限位刚度 `10e5` `N/m`（默认）| 正标量

锥形离合器齿圈两侧硬限位的刚度。模型假设齿圈和限位表现为弹性行为。接触变形与施加的力成正比，与接触刚度的倒数成正比。

### **Dog clutch ring stop damping** — 犬牙离合器齿圈限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

犬牙离合器齿圈与轮毂之间的平移接触阻尼。阻尼的值与碰撞后发生的振荡次数成反比。该参数必须大于零。

### **Cone clutch ring stop damping** — 锥形离合器齿圈限位阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

锥形离合器齿圈与轮毂之间的平移接触阻尼。阻尼的值与碰撞后发生的振荡次数成反比。该参数必须大于零。

### **Shift linkage viscous friction coefficient** — 换挡连杆粘性摩擦系数 `100` `N/(m/s)`（默认）| 正标量

轮毂与齿圈之间相对平移运动的粘性摩擦系数。该参数的值取决于润滑状态和接触表面的质量。该系数必须大于或等于零。

### **Engagement block stiffness** — 接合阻塞刚度系数 `10e6` `N/m`（默认）| 正标量

接合阻塞期间的刚度系数。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Engagement block damping** — 接合阻塞阻尼系数 `300` `N*s/m`（默认）| 正标量

接合阻塞期间的阻尼系数。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Shift linkage engaged friction coefficient** — 接合摩擦系数 `100` `N*s/m`（默认）| 正标量

齿圈与轮毂接合时换挡连杆处的摩擦系数。该值为换挡连杆与其支撑之间的摩擦力。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Shift linkage disengaged friction coefficient** — 分离摩擦系数 `50` `N*s/m`（默认）| 正标量

齿圈与轮毂分离时换挡连杆处的摩擦系数。该值为换挡连杆与其支撑之间的摩擦力。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact speed threshold** — 静态接触速度阈值 `0.1` `m/s`（默认）| 正标量

速度阈值，低于该值时齿圈和轮毂要么完全接合并锁定，要么完全分离并锁定。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact release force threshold** — 释放力阈值 `0.001` `N`（默认）| 正标量

力阈值，超过该值时齿圈和轮毂可以解锁并分离。

#### 依赖关系

要启用此参数，请在 **Dog clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Tooth-tooth friction coefficient** — 齿间接触动摩擦系数 `0.05`（默认）| 正标量

齿圈与轮毂齿之间接触界面处的动摩擦系数。该系数表征在离合器接合/分离过程中由于齿间接触而阻碍换挡连杆运动的耗散力。

系数值越大，换挡连杆运动过程中的能量耗散越大。该参数的值必须大于零。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### 初始条件

### **Initial state** — 初始离合器状态 `All clutches unlocked`（默认）| `Cone clutch A and dog clutch A locked` | `Cone clutch A locked` | `Cone clutch B locked` | `Cone clutch B and dog clutch B locked`

锥形离合器和犬牙离合器的初始配置：

- `Cone clutch A and dog clutch A locked` — 锥形离合器 *A* 和犬牙离合器 *A* 在齿圈与轮毂轴之间传递扭矩。
- `Cone clutch A locked` — 锥形离合器 *A* 在齿圈与轮毂轴之间传递扭矩。
- `All clutches unlocked` — 锥形离合器和犬牙离合器在齿圈与轮毂轴之间传递零扭矩。
- `Cone clutch B locked` — 锥形离合器 *B* 在齿圈与轮毂轴之间传递扭矩。
- `Cone clutch B and dog clutch B locked` — 锥形离合器 *B* 和犬牙离合器 *B* 在齿圈与轮毂轴之间传递扭矩。

### **Dog clutch initial shift linkage position** — 犬牙离合器初始换挡连杆位置 `0` `mm`（默认）| 标量

连接到犬牙离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| 犬牙离合器状态 | 参数限制 |
| --- | --- |
| 犬牙离合器 A 初始接合 | 参数值的负值必须大于参数 **Ring-hub clearance when dog clutch disengaged** 和 **Tooth overlap to engage** 之和 |
| 犬牙离合器 A 初始分离 | 参数值的负值必须小于参数 **Ring-hub clearance when dog clutch disengaged** 和 **Tooth overlap to engage** 之和 |
| 犬牙离合器 B 初始接合 | 参数值必须大于参数 **Ring-hub clearance when dog clutch disengaged** 和 **Tooth overlap to engage** 之和 |
| 犬牙离合器 B 初始分离 | 参数值必须小于参数 **Ring-hub clearance when dog clutch disengaged** 和 **Tooth overlap to engage** 之和 |

### **Cone clutch initial shift linkage position** — 锥形离合器初始换挡连杆位置 `0` `mm`（默认）| 标量

连接到锥形离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| 锥形离合器状态 | 参数限制 |
| --- | --- |
| 锥形离合器 A 初始接合 | 参数的负值必须大于 **Ring-hub clearance when cone clutch disengaged** 的值 |
| 锥形离合器 A 初始分离 | 参数的负值必须小于 **Ring-hub clearance when cone clutch disengaged** 的值 |
| 锥形离合器 B 初始接合 | 参数必须大于 **Ring-hub clearance when cone clutch disengaged** 的值 |
| 锥形离合器 B 初始分离 | 参数必须小于 **Ring-hub clearance when cone clutch disengaged** 的值 |

### **Initial dog clutch A ring-hub offset angle** — 初始犬牙离合器 *B* 齿圈-轮毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时犬牙离合器 *B* 的齿圈与轮毂之间的旋转角度。该角度决定了齿圈和轮毂齿是否可以互锁，从而决定离合器是否可以接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，则初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N，

  其中 *N* 是齿圈或轮毂中存在的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，则初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2，

  其中 *δ* 是齿圈与轮毂齿之间的齿隙角。

#### 依赖关系

要启用此参数，

- 在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Initial dog clutch B ring-hub offset angle** — 初始犬牙离合器 *A* 齿圈-轮毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时齿圈与轮毂之间的旋转角度。该角度决定了齿圈和轮毂齿是否可以互锁，从而决定离合器是否可以接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，则初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N，

  其中 *N* 是齿圈或轮毂中存在的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，则初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2，

  其中 *δ* 是齿圈与轮毂齿之间的齿隙角。

#### 依赖关系

要启用此参数，

- 在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **Dog Clutch** 部分中，将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### Thermal Port

要启用热建模，请在 **Cone Clutch** 部分中，将 **Friction model** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请在 **Cone Clutch** 设置中，将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的组件温度。初始温度根据您指定的效率向量改变组件效率，影响起始啮合或摩擦损失。

#### 依赖关系

此参数仅在 **Cone Clutch** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2024a: 捕获由于速度差导致的接合阻塞效应

当 **Torque transmission model** 为 `Dynamic modal` 时，您现在可以在系统级别捕获由于速度差导致的接合阻塞效应。

## 描述

机械双面同步器

Double-Sided Synchronizer 模块表示一个双面同步器，包含两个背靠背的狗离合器、两个背靠背的锥形离合器和一平移棘爪。与常规同步器不同，双面同步器在变速器的输入侧和输出侧同步并啮合齿轮。双面同步器可以同时接合和分离两个轴上的齿轮，从而实现更复杂的齿轮接合模式。重型商用车、非公路设备以及一些高性能汽车变速器通常使用这些同步器。

换挡连杆沿负方向平移使离合器将齿环与轮毂 *A* 接合。换挡连杆沿正方向平移使离合器将齿环与轮毂 *B* 接合。当换挡连杆平移的幅值小于锥形离合器齿环-轮毂间隙时，同步器处于空挡模式，不传递扭矩。

双面同步器的横截面图，轮毂轴位于齿环轴的两侧。平移棘爪将换挡连杆固定到位。

该示意图展示了处于分离状态的双面同步器。在此状态下，齿环 **R** 以及轮毂 **HA** 和 **HB** 的轴可以以不同速度独立旋转。当换挡连杆 **S** 沿负方向平移时，锥形离合器 *A*（**CCA**）的端面开始接触。锥形离合器中的摩擦减小了轴之间的转速差。当换挡连杆上的力超过棘爪 **D** 的峰值力时，狗离合器齿 **T** 可以接合。棘爪峰值力应使得锥形离合器有足够的时间和法向力将轴带到足够接近的速度以允许狗离合器接合。类似地，沿正方向平移换挡连杆使锥形离合器 *B*（**CCB**）的端面开始接触，并可以使齿环的轴与轮毂 *B*（**HB**）的轴接合。

Simscape 模型展示了使用两个 Dog Clutch 模块与两个 Cone Clutch 模块并联的等效复合模块布置。一个 Translational Detent 模块连接在锥形离合器模块和狗离合器模块之间的换挡连杆处。

该模型实现了两个 Dog Clutch 模块、两个 Cone Clutch 模块和一个 Translational Detent 模块。有关相应模块功能的更多信息，请参阅每个模块的参考页。

连接 **R**、**HA** 和 **HB** 是机械旋转守恒端口，分别表示齿环 **R**、轮毂 *A*（**HA**）和轮毂 *B*（**HB**）。连接 **S** 是机械平移守恒端口，表示齿环换挡手柄。

连接 **X1** 和 **X2** 是物理信号端口，分别输出狗离合器和锥形离合器的换挡连杆位置。下表提供了常见离合器接合情况下的 *X1* 和 *X2* 值。

| 狗离合器状态 | X1 |
| --- | --- |
| 分离 | 0 |
| 与轮毂 *A* 完全接合 | 齿环-轮毂间隙与齿高之和的负值 |
| 与轮毂 *B* 完全接合 | 齿环-轮毂间隙与齿高之和的正值 |

| 锥形离合器状态 | X2 |
| --- | --- |
| 分离 | 0 |
| 与轮毂 *A* 完全接合 | 齿环-轮毂间隙的负值 |
| 与轮毂 *B* 完全接合 | 齿环-轮毂间隙的正值 |

当同步器完全分离时，*X1* 和 *X2* 的值为零。当狗离合器与轮毂 *A* 完全接合时，*X1* 等于其齿环-轮毂间隙与齿高之和的负值。当狗离合器与轮毂 *B* 完全接合时，*X1* 等于其齿环-轮毂间隙与齿高之和的正值。当锥形离合器与轮毂 *A* 完全接合时，*X2* 等于其齿环-轮毂间隙的负值。当锥形离合器与轮毂 *B* 完全接合时，*X2* 等于其齿环-轮毂间隙。

### 狗离合器扭矩传递模型

您可以从以下扭矩传递模型中选择。

**摩擦离合器近似模型**

当您将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and` 时，模块将离合器接合视为齿环与轮毂之间的摩擦现象。此设置更适合线性化、固定步长仿真和硬件在环（HIL）仿真。模块使用 Fundamental Friction Clutch 模块的复合实现。

当您使用此设置时，离合器有三种可能的配置：分离、接合和锁定。分离时，齿环与轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿环-轮毂齿重叠 *h* 超过接合的最小值时，两个组件之间的接触力开始随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到其最大值，离合器状态切换为锁定。在此状态下，齿环和轮毂作为整体旋转而无滑动。要解锁离合器，传递的扭矩必须超过 **Maximum transmitted torque** 参数的值。

**带间隙的动态模型**

当您将 **Torque transmission model** 设置为 `Dynamic with backlash` 时，模块模拟离合器现象，如间隙、扭转柔度和齿环与轮毂齿之间的接触力。此模型比摩擦离合器近似提供更高的精度。

当您使用此设置时，离合器有两种可能的配置：分离和接合。分离时，齿环与轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿环-轮毂齿重叠 *h* 超过接合阈值时，离合器传递扭矩。该扭矩是扭转弹簧和阻尼器分量之和，包括齿环与轮毂齿之间的间隙，使得TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2，其中：

- *kRH* 是齿环-轮毂耦合的扭转刚度。
- *ϕ* 是齿环与轮毂之间绕公共旋转轴的相对角度。
- *δ* 是齿环与轮毂齿之间的间隙。
- *ω* 是齿环与轮毂之间的相对角速度。此变量描述两个组件相互滑动的速度。

柔性端部止挡限制离合器换挡连杆和齿环的平移运动。柔度模型将端部止挡视为线性弹簧-阻尼器组。端部止挡的位置取决于齿环与轮毂齿之间的相对角度和角速度：

- 如果齿对齐且相对角速度小于离合器接合的最大值，则端部止挡位置为完全分离时的齿环-轮毂间隙与齿高之和。离合器可以在此端部止挡位置接合。
- 如果齿未对齐或相对角速度超过离合器接合的最大值，则端部止挡位置设置为防止齿环与轮毂接合。离合器不会在此端部止挡位置接合。

平移摩擦阻碍换挡连杆和齿环运动。该摩擦是库仑分量和粘性分量之和，使得FZ=−kK·FN·tanh(4vvth)−μTv，其中：

- *FZ* 是作用在换挡连杆和齿环上的净平移摩擦力。
- *kK* 是齿环与轮毂齿之间的动摩擦系数。
- *FN* 是齿环与轮毂齿之间的法向力，其中 *FN* = *TC*/*Rm*。
- *v* 是换挡连杆和齿环的平移速度。
- *vth* 是平移速度阈值。低于此阈值时，双曲正切函数在换挡连杆和齿环速度趋于零时将库仑摩擦力平滑至零。
- *μT* 是作用在换挡连杆和齿环上的粘性阻尼系数。

**动态模态**

当您将 **Torque transmission model** 设置为 `Dynamic modal` 时，模块通过从机械平移守恒端口 **S** 获取换挡连杆位置来确定离散离合器模态行为。此设置比 `Two-mode` 参数化捕获更复杂的离合器动力学，并且比 `Friction clutch approximation` 和 `Dynamic with backlash` 设置更快。

您可以使用 `Dynamic modal` 设置来模拟当速度差太大以至于离合器片无法接合时的接合阻塞。模块将接合阻塞表示为弹簧-阻尼器系统，您可以参数化弹簧和阻尼系数。接合模式重叠，这防止模式改变，直到换挡连杆位置超出接合重叠区域。您使用 **Tooth overlap to engage** 参数定义接合重叠区域。

图示描述了接合和分离之间的模式转换。变量 z 表示换挡连杆位置。接合和分离模态区域重叠，这衰减了模式转换速率。

连杆位置约束为：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **Tooth height** 参数。
- *zGap* 是 **Ring hub clearance when disengaged** 参数。
- *zOverlap* 是 **Tooth overlap to engage** 参数。
- *ωthr* 是 **Engagement speed threshold** 参数。

接合模式位置为：

- *z* = 0 — 离合器完全分离。
- 0 < *z* < *zGap* — 当换挡连杆位置在 *zGap* 定义的区域内时，离合器分离。离合器可以在 *x* = *zGap* + *zOverlap* 处从分离转换到接合。
- *zGap* < *z* < *h* — 当 *z* 在 *h* 定义的区域内时，离合器接合。离合器可以在 *z* = *zGap* 处从接合转换到分离。
- *z* = *zGap* + *h* — 离合器完全接合。
- *z* = *zGap* + *zOverlap* — 当 *z* 在接合重叠区域内时，离合器仅在速度差小于 *ωthr* 参数的值时接合。

### 热建模

您可以通过可选的热守恒端口对热流和温度变化的影响进行建模。默认情况下，热端口是隐藏的。要显示热端口，在 **Clutch** 设置中，为 **Friction model** 参数选择温度相关设置。指定组件的相关热参数。
