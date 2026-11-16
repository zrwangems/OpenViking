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

### **X1** — 爪式离合器平移物理信号

物理信号输出端口，用于测量爪式离合器平移的幅值。

### **X2** — 锥形离合器平移物理信号

物理信号输出端口，用于测量锥形离合器平移的幅值。
### 守恒

### **H** — 离合器轮毂机械旋转

与离合器轮毂关联的机械旋转守恒端口。

### **R** — 离合器齿圈机械旋转

与离合器齿圈关联的机械旋转守恒端口。

### **S** — 换挡连杆机械旋转

与换挡连杆关联的机械旋转守恒端口。

### **T** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

要启用此端口，在**摩擦**部分中，将**摩擦模型**设置为 `Temperature-dependent friction
coefficients` 或 `Temperature and
velocity-dependent friction coefficients`。

## 参数

### 锥形离合器

### **接触面最大直径** — 外径 `150` `mm`（默认值）| 正标量

外锥直径 *do*。

### **接触面最小直径** — 内径 `100` `mm`（默认值）| 正标量

内锥直径 *di*。

### **锥半角** — 锥半角 `12` `deg`（默认值）| 正标量

锥几何形状的半开角 *α*。

### **摩擦模型** — 摩擦模型 `Fixed kinetic friction coefficient`（默认值）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction
  coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction
  coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction
  coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction
  coefficients` — 基于温度以及圆盘之间的相对角速度，通过查表定义动摩擦系数。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认值）| 向量

相对速度的输入值，指定为向量。向量中的值必须从左到右递增。最少值数量取决于所选插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Velocity-dependent kinetic friction
coefficient` 或 `Temperature and
velocity-dependent friction coefficients`。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认值）| 递增向量

温度的输入值，指定为向量。最少值数量取决于所选插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Temperature-dependent friction
coefficients` 或 `Temperature and
velocity-dependent friction coefficients`。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认值）| 标量

摩擦系数的静值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction
coefficient`。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认值）| 向量

摩擦系数的静值或峰值，指定为向量。该向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Temperature-dependent friction
coefficients` 或 `Temperature and
velocity-dependent friction coefficients`。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认值）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Fixed kinetic friction
coefficient`。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认值）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，指定为向量。所有值必须大于零。

如果**摩擦模型**参数设置为

- `Velocity-dependent kinetic friction
  coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction
  coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Velocity-dependent kinetic friction
coefficient` 或 `Temperature-dependent
friction coefficients`。

### **动摩擦系数矩阵** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认值）| 矩阵

动摩擦系数的输出值，指定为矩阵。所有值必须大于零。矩阵的大小必须等于由温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Temperature and velocity-dependent friction
coefficients`。

### **摩擦系数插值方法** — 插值方法 `Linear`（默认值）| `Smooth`

用于在输入值位于两个连续网格点之间时逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参见 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Velocity-dependent kinetic friction
coefficient`、`Temperature-dependent
friction coefficients` 或 `Temperature
and velocity-dependent friction
coefficients`。

### **摩擦系数外推方法** — 外推方法 `Linear`（默认值）| `Nearest` | `Error`

用于在输入值位于参数列表中指定范围之外时确定输出值的外推方法：

- `Linear` — 选择此选项以生成一条在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当希望数据位于表范围内时，选择此选项以避免进入外推模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参见 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，将**摩擦模型**设置为 `Velocity-dependent kinetic friction
coefficient`、`Temperature-dependent
friction coefficients` 或 `Temperature
and velocity-dependent friction
coefficients`。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认值）| 标量

低于该相对速度时，两个表面可以锁止。如果扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则这些表面锁止。

### **阈值力** — 法向接触力阈值 `1` `N`（默认值）| 标量

力阈值。仅当法向力超过**阈值力**参数的值时，模块才模拟该法向力。否则，不传递摩擦扭矩。

### 爪式离合器

### **扭矩传递模型** — 扭矩传递模型 `Friction clutch approximation — Suitable for HIL and linearization`（默认值）| `Dynamic with backlash` | `Dynamic modal`

用于对爪式离合器行为进行建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置对于实时仿真足够快，并且不需要了解离合器尺寸。只能使用物理信号或逻辑控制信号控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真度复合实现。此设置支持热建模。可以使用物理信号或机械平移守恒连接来控制换挡连杆。
- `Dynamic with backlash` — 高保真度离合器接合模型，考虑齿隙、扭转柔度和齿圈与轮毂齿之间的接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，可捕获由于速度差导致的接合阻塞效应。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent friction coefficients`。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认值）| 递增数值向量

温度的输入值，指定为向量。最少值数量取决于所选插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent friction
coefficients` 或 `Temperature and
velocity-dependent friction coefficients`。

### **最大传递扭矩** — 最大传递扭矩 `1000` `N*m`（默认值）| 正标量

离合器在不打滑接合配置下能够传递的最大扭矩。如果齿圈和轮毂之间传递的扭矩超过此值，则两个组件开始相对打滑。此扭矩确定摩擦离合器近似中的静摩擦极限。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction
coefficient`，并在**爪式离合器**部分中，将**扭矩传递模型**设置为 `Friction clutch approximation -
Suitable for HIL and linearization`。

### **最大传递扭矩向量** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认值）| 向量

离合器在不打滑接合配置下能够传递的最大扭矩，指定为向量。如果齿圈和轮毂之间传递的扭矩超过此值，则两个组件开始相对打滑。此扭矩确定摩擦离合器近似中的静摩擦极限。该向量与温度向量具有相同数量的元素。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction
coefficient` 或 `Temperature and
velocity-dependent kinetic friction
coefficient`。

### **插值方法** — 插值方法 `Linear`（默认值）| `Smooth`

用于在输入值位于两个连续网格点之间时逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参见 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction
coefficient` 或 `Temperature and
velocity-dependent kinetic friction
coefficient`。

### **外推方法** — 外推方法 `Linear`（默认值）| `Nearest` | `Error`

用于在输入值位于参数列表中指定范围之外时确定输出值的外推方法：

- `Linear` — 选择此选项以生成一条在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当希望数据位于表范围内时，选择此选项以避免进入外推模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参见 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Temperature-dependent kinetic friction
coefficient` 或 `Temperature and
velocity-dependent kinetic friction
coefficient`。

### **离合器齿平均半径** — 离合器齿平均半径 `50` `mm`（默认值）| 正标量

从齿圈或轮毂中心到对应齿中心的距离。在给定两个组件之间的传递扭矩的情况下，平均齿半径决定齿圈与轮毂齿之间的法向接触力。此参数的值必须大于零。

### **齿数** — 齿圈或轮毂齿数 `6`（默认值）| 正非零标量整数

齿圈或轮毂中的齿总数。两个组件具有相同的齿数。此参数的值必须大于或等于一。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction
coefficient`，并在**爪式离合器**部分中，将**扭矩传递模型**设置为 `Dynamic with
backlash`。

### **旋转齿隙** — 旋转齿隙 `10` `deg`（默认值）| 正标量

在接合离合器配置中，齿圈与轮毂齿之间允许的角运动或间隙。此参数的值必须大于零。

#### 依赖关系

要启用此参数，在**锥形离合器**部分中，将**摩擦模型**设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction
coefficient`，并在**爪式离合器**部分中，将**扭矩传递模型**设置为 `Dynamic with
backlash`。

### **扭转刚度** — 扭转刚度 `10e6` `N*m/rad`（默认值）| 正标量

齿圈与轮毂齿之间接触界面处的线性扭转刚度系数。此系数表征两组齿之间接触力的恢复分量。刚度值越大，接触力越大。此参数的值必须大于零。默认值为 `10e6`
`N*m/rad`。

#### 依赖项

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **扭转阻尼** — 扭转阻尼 `100` `N*m/(rad/s)` (default) | positive scalar

环与毂齿之间接触界面处的线性扭转阻尼系数。该系数表征两组齿之间接触力的耗散分量。阻尼值越大，接触期间的能量耗散越大。此参数的值必须大于零。

#### 依赖项

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **接合速度阈值** — 接合速度阈值 `5` `rpm` (default) | positive scalar

离合器传递动力的最低转速。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Dynamic modal`。

### 棘轮

### **峰值力** — 峰值剪切力 `500` `N` (default) | nonnegative scalar

棘轮的峰值剪切力。

### **凹口宽度** — 凹口宽度 `3` `mm` (default) | nonnegative scalar

棘轮表现出剪切力的区域宽度。

### **粘性摩擦系数** — 粘性摩擦系数 `0.1` `N/(m/s)` (default) | nonnegative scalar

棘轮接触表面处的粘性摩擦系数。此参数的值必须大于或等于零。

### **摩擦力与峰值力之比** — 摩擦力与峰值力之比 `0.01` (default) | nonnegative scalar

棘轮的动摩擦力与峰值剪切力之比。该参数用于设置动摩擦力的值。该参数必须大于或等于零。

### **摩擦速度阈值** — 动摩擦速度阈值 `0.05` `m/s` (default)

棘轮接触表面处达到峰值动摩擦力所需的速度。该参数确保行程方向改变时力连续，从而提高仿真的数值稳定性。该参数必须大于零。默认值为 `0.05` `m/s`。

### 换挡连杆

### **连杆运动方向** — 接合条件运动方向 `Positive shift linkage displacement engages clutch` (default) | `Negative shift linkage displacement engages clutch`

换挡连杆必须运动以接合离合器的方向。选项包括正位移和负位移。

### **最大接合速度** — 接合速度上限速度阈值 `inf` (default) | positive scalar

环与毂之间的相对角速度，高于该速度时离合器无法接合。该值特定于具体变速箱或传动系统。最小化该值有助于避免接合期间的高动态冲击。此参数的值必须大于零。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **接合所需齿重叠** — 齿重叠接合阈值 `3` `mm` (default) | positive scalar

环齿与毂齿沿公共纵向轴线的重叠长度。当齿重叠大于此值时，离合器接合。在啮合齿轮齿至少重叠此长度之前，离合器保持分离。该值必须大于零。

### **齿高** — 齿高 `10` `mm` (default) | positive scalar

齿根与齿顶之间的距离。环齿和毂齿具有相同的高度。齿高和完全分离时的环-毂间隙决定换挡连杆的最大行程跨度。此参数的值必须大于零。

### **分离时环-毂间隙** — 分离时环-毂间隙 `3` `mm` (default) | positive scalar

沿换挡连杆平移轴线的环齿顶与毂齿顶之间的最大开口间隙。该间隙对应于离合器完全分离状态。齿高和完全分离时的环-毂间隙决定换挡连杆的最大行程跨度。此参数的值必须大于零。

### **换挡连杆后部硬限位** — 硬限位模型 `on` (default) | `off`

防止换挡连杆运动超过完全分离位置的硬限位：

- 选中 — 完全分离时硬限位。
- 清除 — 完全分离时无硬限位。

### **犬牙式离合器环限位刚度** — 犬牙式离合器环限位刚度 `10e5` `N/m` (default) | positive scalar

犬牙式离合器环两侧硬限位的刚度。模型假设环和限位表现为弹性。接触变形与施加的力成正比，与接触刚度的倒数成正比。刚度的值必须参考参数 **接合所需齿重叠** 进行赋值。刚度过低可能导致变形超过所需重叠并引发错误接合。该参数必须大于零。

### **锥形离合器环限位刚度** — 锥形离合器环限位刚度 `10e5` `N/m` (default) | positive scalar

锥形离合器环两侧硬限位的刚度。模型假设环和限位表现为弹性。接触变形与施加的力成正比，与接触刚度的倒数成正比。

### **犬牙式离合器环限位阻尼** — 犬牙式离合器环限位阻尼 `1e3` `N/(m/s)` (default) | nonegative scalar

犬牙式离合器环与毂之间的平移接触阻尼。阻尼值与冲击后发生的振荡次数成反比。

### **锥形离合器环限位阻尼** — 锥形离合器环限位阻尼 `1e3` `N/(m/s)` (default) | nonegative scalar

锥形离合器环与毂之间的平移接触阻尼。阻尼值与冲击后发生的振荡次数成反比。

### **换挡连杆粘性摩擦系数** — 换挡连杆粘性摩擦系数 `100` `N/(m/s)` (default) | positive scalar

毂与环之间相对平移运动的粘性摩擦系数。该参数的值取决于润滑状态和接触表面质量。

### **接合阻挡刚度** — 接合阻挡刚度系数 `10e6` `N/m` (default) | positive scalar

阻挡接合时的刚度系数。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **接合阻挡阻尼** — 接合阻挡阻尼系数 `300` `N*s/m` (default) | positive scalar

阻挡接合时的阻尼系数。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **换挡连杆接合摩擦系数** — 接合摩擦系数 `100` `N*s/m` (default) | positive scalar

环与毂接合时换挡连杆处的摩擦系数。该值是换挡连杆与其支撑件之间的摩擦力。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **换挡连杆分离摩擦系数** — 分离摩擦系数 `50` `N*s/m` (default) | positive scalar

环与毂分离时换挡连杆处的摩擦系数。该值是换挡连杆与其支撑件之间的摩擦力。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触速度阈值** — 静态接触速度阈值 `0.1` `m/s` (default) | positive scalar

速度阈值，低于该阈值时环和毂要么完全接合并锁定，要么完全分离并锁定。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触释放力阈值** — 释放力阈值 `0.001` `N` (default) | positive scalar

力阈值，高于该阈值时环和毂可以解锁并分离。

#### 依赖项

要启用此参数，请在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **齿间摩擦系数** — 齿间接触动摩擦系数 `0.05` (default) | positive scalar

环齿与毂齿之间接触界面处的动摩擦系数。该系数表征在离合器接合/分离期间由于齿间接触而阻碍换挡连杆运动的耗散力。

系数值越大，换挡连杆运动期间的能量耗散越大。此参数的值必须大于零。

#### 依赖项

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`，并在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 初始条件

### **初始状态** — 初始离合器状态 `All clutches unlocked` (default) | `Cone clutch locked` | `All clutches locked`

锥形和犬牙式离合器的初始配置：

- `All clutches unlocked` — 锥形和犬牙式离合器在环轴与毂轴之间传递零扭矩。
- `Cone clutch locked` — 锥形离合器在环轴与毂轴之间传递扭矩。
- `All clutches locked` — 锥形和犬牙式离合器在环轴与毂轴之间传递扭矩。

### **犬牙式离合器初始换挡连杆位置** — 犬牙式离合器初始换挡连杆位置 `0` `mm` (default) | scalar

连接到犬牙式离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| 连杆运动方向 | 犬牙式离合器状态 | 参数限制 |
| --- | --- | --- |
| `Positive shift linkage displacement engages clutch` | 初始接合 | 参数必须大于参数 **分离时犬牙式离合器环-毂间隙** 与 **接合所需齿重叠** 之和 |
| 初始分离 | 参数必须小于参数 **分离时犬牙式离合器环-毂间隙** 与 **接合所需齿重叠** 之和 |
| `Negative shift linkage displacement engages clutch` | 初始接合 | 参数的负值必须大于参数 **分离时犬牙式离合器环-毂间隙** 与 **接合所需齿重叠** 之和 |
| 初始分离 | 参数的负值必须小于参数 **分离时犬牙式离合器环-毂间隙** 与 **接合所需齿重叠** 之和 |

### **锥形离合器初始换挡连杆位置** — 锥形离合器初始换挡连杆位置 `0` `mm` (default) | scalar

连接到锥形离合器的换挡连杆部分的初始位置。该参数的值具有以下限制：

| 连杆运动方向 | 犬牙式离合器状态 | 参数限制 |
| --- | --- | --- |
| `Positive shift linkage displacement engages clutch` | 初始接合 | 参数必须大于 **分离时锥形离合器环-毂间隙** 的值 |
| 初始分离 | 参数必须小于 **分离时锥形离合器环-毂间隙** 的值 |
| `Negative shift linkage displacement engages clutch` | 初始接合 | 参数的负值必须大于 **分离时犬牙式锥形环-毂间隙** 的值 |
| 初始分离 | 参数的负值必须小于 **分离时犬牙式锥形环-毂间隙** 的值 |

### **初始犬牙式离合器环-毂偏移角** — 初始犬牙式离合器环-毂偏移角 `0` `deg` (default) | scalar

仿真时间零时环与毂之间的旋转角度。该角度决定环齿和毂齿能否互锁，从而决定离合器能否接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，则初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N，

  其中 *N* 是环或毂上存在的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，则初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2，

  其中 *δ* 是环齿与毂齿之间的齿隙角。

#### 依赖项

要启用此参数，

- 在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient`。
- 在 **犬牙式离合器** 部分中，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 热端口

**热端口** 设置仅在 **锥形离合器** 设置中的 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。

### **热质量** — 热质量 `50` `kJ/K` (default) | scalar

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗越强。

#### 依赖项

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

### **初始温度** — 初始温度 `300` `K` (default) | scalar

仿真开始时组件的温度。初始温度根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

#### 依赖项

要启用此参数，请在 **锥形离合器** 部分中，将 **摩擦模型** 设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients`。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2025a：枚举更新

**换挡连杆后部硬限位** 参数现在使用复选框。此参数在以前的版本中使用下拉列表。

### R2024a：捕获由于速度差导致的接合阻挡效应

现在，当 **扭矩传递模型** 为 `Dynamic modal` 时，您可以在系统级别捕获由于速度差导致的接合阻挡效应。

## 描述

机械同步器

Synchronizer 模块表示一个同步器，其包含牙嵌式离合器、锥形离合器和平移式定位器。同步器通过接合前使齿轮速度相等，促进手动变速器的平顺换挡，减少齿轮冲击，并确保不同挡位速比之间的无缝过渡。

换挡连杆首先平移以接合锥形离合器。摩擦力矩使换挡连杆和锥形离合器轴以相同速度旋转。当作用在换挡连杆上的力超过定位器力时，牙嵌式离合器可以接合。

典型同步器的横截面。轮毂侧的锥形离合器与齿环侧脱开。

该示意图展示了处于脱开状态的同步器。在此状态下，齿环（R）和轮毂（H）轴可以以不同速度独立旋转。为了使齿环和轮毂轴速度同步，换挡连杆（S）向轮毂轴平移以接合锥形离合器。锥形离合器的摩擦表面产生摩擦力矩，使齿环和轮毂轴的转速相等。当作用在换挡连杆上的平移力超过峰值定位器力时，牙嵌式离合器齿（T）可以接合。峰值定位器力应允许有足够的时间和法向力来使齿环和轮毂轴速度相等，以便牙嵌式离合器可以接合。

Dog Clutch 模块与 Cone Clutch 模块并联连接。一个 Translational Detent 模块连接在它们的换挡连杆端口之间。

该模型实现了 Dog Clutch、Cone Clutch 和 Translational Detent 模块。有关相应模块功能的更多信息，请参阅每个模块的参考页。您可以使用类似的方法来对同步器的自定义版本进行建模。一个示例是 Vehicle with Manual Transmission 示例模型中的 Transmission (Detailed) 子系统。

连接 **R** 和 **H** 是机械旋转守恒端口，分别表示齿环（R）和轮毂（H）。连接 **S** 是机械平移守恒端口，表示齿环换挡手柄。

连接 **X1** 和 **X2** 是物理信号输出，分别报告牙嵌式离合器和锥形离合器的换挡连杆位置。当离合器完全脱开时，换挡连杆位置为零。当牙嵌式离合器完全接合时，牙嵌式离合器换挡连杆位置的幅值等于牙嵌式离合器齿环-轮毂间隙与齿高之和。当锥形离合器完全接合时，锥形离合器换挡连杆位置的幅值等于锥形离合器齿环-轮毂间隙。

### Dog Clutch 扭矩传递模型

您可以从以下扭矩传递模型中选择。

**摩擦离合器近似模型**

当您将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and` 时，该模块将离合器接合视为齿环和轮毂之间的摩擦现象。此设置更适合线性化、固定步长仿真和硬件在环（HIL）仿真。该模块使用 Fundamental Friction Clutch 模块的复合实现。

当您使用此设置时，离合器有三种可能的配置：脱开、接合和锁止。脱开时，齿环和轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿环-轮毂齿重叠量 *h* 超过接合的最小值时，两个组件之间的接触力开始随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到其最大值，离合器状态切换到锁止。在此状态下，齿环和轮毂作为一个整体无滑动地旋转。要解锁离合器，传递的扭矩必须超过 **最大传递扭矩** 参数的值。

**带齿隙的动态模型**

当您将 **扭矩传递模型** 设置为 `Dynamic with backlash` 时，该模块仿真诸如齿隙、扭转柔度以及齿环和轮毂齿之间的接触力等离合器现象。此模型比摩擦离合器近似模型提供更高的精度。

当您使用此设置时，离合器有两种可能的配置：脱开和接合。脱开时，齿环和轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿环-轮毂齿重叠量 *h* 超过接合阈值时，离合器传递扭矩。该扭矩是扭转弹簧和阻尼器分量之和，包括齿环和轮毂齿之间的齿隙，使得TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2，其中：

- *kRH* 是齿环-轮毂耦合的扭转刚度。
- *ϕ* 是齿环和轮毂之间绕公共旋转轴的相对角度。
- *δ* 是齿环和轮毂齿之间的齿隙。
- *ω* 是齿环和轮毂之间的相对角速度。此变量描述两个组件彼此滑过的速度。

柔顺限位挡块限制离合器换挡连杆和齿环的平移运动。柔度模型将限位挡块视为线性弹簧-阻尼器组。限位挡块的位置取决于齿环和轮毂齿之间的相对角度和角速度：

- 如果齿对齐且相对角速度小于离合器接合的最大值，则限位挡块位置为完全脱开时的齿环-轮毂间隙与齿高之和。离合器可以在此限位挡块位置接合。
- 如果齿未对齐或相对角速度超过离合器接合的最大值，则设置限位挡块位置以防止齿环接合轮毂。离合器不会在此限位挡块位置接合。

平移摩擦阻止换挡连杆和齿环运动。该摩擦是库仑分量和粘性分量之和，使得FZ=−kK·FN·tanh(4vvth)−μTv，其中：

- *FZ* 是作用在换挡连杆和齿环上的净平移摩擦力。
- *kK* 是齿环和轮毂齿之间的动摩擦系数。
- *FN* 是齿环和轮毂齿之间的法向力，其中 *FN* = *TC*/*Rm*。
- *v* 是换挡连杆和齿环的平移速度。
- *vth* 是平移速度阈值。低于此阈值时，双曲正切函数将库仑摩擦力平滑到零，因为换挡连杆和齿环速度趋于零。
- *μT* 是作用在换挡连杆和齿环上的粘性阻尼系数。

**动态模态**

当您将 **扭矩传递模型** 设置为 `Dynamic modal` 时，该模块通过从机械平移守恒端口 **S** 获取换挡连杆位置来确定离散离合器模态行为。此设置比 `Two-mode` 参数化捕获更复杂的离合器动力学，并且比 `Friction clutch approximation` 和 `Dynamic with backlash` 设置更快。

您可以使用 `Dynamic modal` 设置来仿真当速度差过大以致离合器片无法接合时的接合阻挡。该模块将接合阻挡表示为弹簧-阻尼器系统，您可以参数化弹簧和阻尼系数。接合模式重叠，这防止模式发生变化，直到换挡连杆位置超出接合重叠区域。您可以使用 **接合齿重叠量** 参数定义接合重叠区域。

图示描绘了接合和脱开之间的模式转换。变量 z 表示换挡连杆位置。接合和脱开模态区域重叠，这衰减了模式转换速率。

连杆位置约束为：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **齿高** 参数。
- *zGap* 是 **脱开时的齿环轮毂间隙** 参数。
- *zOverlap* 是 **接合齿重叠量** 参数。
- *ωthr* 是 **接合速度阈值** 参数。

接合模式位置为：

- *z* = 0 — 离合器完全脱开。
- 0 < *z* < *zGap* — 当换挡连杆位置处于 *zGap* 定义的区域时，离合器脱开。离合器可以在 *x* = *zGap* + *zOverlap* 处从脱开转换到接合。
- *zGap* < *z* < *h* — 当 *z* 处于 *h* 定义的区域时，离合器接合。当 *z* = *zGap* 时，离合器可以从接合转换到脱开。
- *z* = *zGap* + *h* — 离合器完全接合。
- *z* = *zGap* + *zOverlap* — 当 *z* 处于接合重叠区域时，仅当速度差小于 *ωthr* 参数的值时，离合器才接合。

### 热建模

您可以通过可选的热守恒端口对热流和温度变化的影响进行建模。默认情况下，热端口是隐藏的。要显示热端口，请在 **离合器** 设置中，为 **摩擦模型** 参数选择温度相关设置。指定组件的相关热参数。

### 假设与限制

- 该模型不考虑惯性效应。您可以在每个端口添加 Simscape™ Inertia 模块，以向 Synchronizer 模型添加惯性。
