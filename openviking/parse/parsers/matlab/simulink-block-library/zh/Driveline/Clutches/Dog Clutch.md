---
type: simulink-block
title: 'Dog Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'dogclutch'
documentation_source_path: 'ref/dogclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Dog Clutch

## 端口

### 输入

### **S** — 逻辑换挡连杆，无量纲物理信号

与换挡连杆关联的物理信号输入端口，无量纲。如果轮毂和齿圈的相对速度在容差范围内，逻辑 `true` 允许离合器接合。逻辑 `false` 使离合器分离。

#### 依赖关系

要启用此端口，请将 **Torque transmission model** 设置为：

- `Two-mode`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Shift linkage control** 设置为 `Physical signal`
- `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Physical signal`
### 输出

### **X** — 离合器位置，m 或无量纲物理信号

与离合器位置关联的物理信号输出端口，单位为 *m* 或无量纲。当您将 **Torque transmission model** 设置为 `Two-mode` 时，该端口输出逻辑值 `true` 表示接合或 `false` 表示分离。否则，该端口输出离合器的位置。
### 守恒

### **H** — 离合器轮毂机械旋转

与离合器轮毂关联的机械旋转守恒端口

### **R** — 离合器齿圈机械旋转

与离合器齿圈关联的机械旋转守恒端口。

### **S** — 换挡连杆机械平移

与换挡连杆关联的机械平移守恒端口。

#### 依赖关系

要启用此端口，请将 **Torque transmission model** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic modal`
- `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`

### **T** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

## 参数

### 离合器

### **Torque transmission model** — 扭矩传递模型 `Two-mode`（默认）| `Friction clutch approximation - Suitable for HIL and linearization` | `Dynamic with backlash` | `Dynamic modal`

为狗离合器行为建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置对于实时仿真足够快，并且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中等至高保真度复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒连接来控制换挡连杆。
- `Dynamic with backlash` — 高保真度离合器接合模型，考虑了齿圈和轮毂齿之间的齿隙、扭转柔度和接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，捕捉由于速度差导致的接合阻塞效应。

### **Engagement speed threshold** — 接合速度阈值 `5` `rpm`（默认）| 正标量

离合器传递动力的最小转速。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Two-mode` 或 `Dynamic modal`。

### **Thermal port** — 启用热端口的选项 `Omit`（默认）| `Model`

是否启用热守恒端口 **T**。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - 适用于 HIL 和线性化`。

### **Clutch teeth mean radius** — 离合器齿平均半径 `50` `mm`（默认）| 正标量

从齿圈或轮毂中心到相应齿中心的距离。平均齿半径决定了给定两个组件之间传递扭矩时齿圈和轮毂齿之间的法向接触力。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **Maximum transmitted torque** — 最大传递扭矩 `1000` `N*m`（默认）| 正标量

离合器可以传递的最大扭矩。此值对应于非滑动接合配置。如果齿圈和轮毂之间传递的扭矩超过此值，两个组件开始相对滑动。此扭矩决定了摩擦离合器近似中的静摩擦极限。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Omit`。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 向量

温度值。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

### **Maximum transmitted torque vector** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认）| 向量

**Temperature vector** 参数中给定温度下的最大传递扭矩。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的更多信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

### **Extrapolation method** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外插方法：

- `Linear` — 选择此选项以生成在外插区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点或低于数据中最低点的外插。
- `Error` — 选择此选项以避免进入外插模式。如果输入信号超出表的范围，仿真停止并生成错误。

有关外插算法的更多信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

### **Number of teeth** — 齿圈或轮毂齿数 `6`（默认）| 正非零标量整数

齿圈或轮毂中的齿总数。两个组件具有相等的齿数。该值必须大于或等于一。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Rotational backlash** — 旋转齿隙 `10` `deg`（默认）| 正标量

离合器接合时齿圈和轮毂齿之间允许的角运动或游隙。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Torsional stiffness** — 扭转刚度 `10e6` `N*m/rad`（默认）| 正标量

齿圈和轮毂齿之间接触界面处的线性扭转刚度系数。此系数表征两组齿之间接触力的恢复分量。较大的刚度值对应于较大的接触力。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### **Torsional damping** — 扭转阻尼 `100` `N*m*s/rad`（默认）| 正标量

齿圈和轮毂齿之间接触界面处的线性扭转阻尼系数。此系数表征两组齿之间接触力的耗散分量。较大的阻尼值对应于接触期间较大的能量耗散。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic with backlash`。

### 换挡连杆

### **Abstract shift linkage control** — 双模式连杆控制选项 `Logic-controlled`（默认）| `Physical signal`

用于双模式扭矩传递的抽象换挡连杆控制。

- `Logic-controlled` — 使用物理信号端口 **S** 将换挡连杆输入为布尔运算符。
- `Physical signal` — 通过物理信号端口 **S** 直接输入换挡连杆位置。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Two-mode`。

### **Shift linkage control** — 换挡连杆控制端口 `Physical signal`（默认）| `Conserving port`

换挡连杆控制的端口类型：

- `Physical signal` — 通过物理信号端口 **S** 直接输入换挡连杆位置。
- `Conserving port` — 通过平移守恒端口 **S** 动态输入换挡连杆位置。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **Tooth height** — 齿高 `10` `mm`（默认）| 正标量

齿的基部和顶部之间的距离。齿圈和轮毂齿具有相同的高度。齿高和完全分离时的齿圈-轮毂间隙决定了换挡连杆的最大行程跨度。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`
- `Two-mode`，并将 **Abstract shift linkage control** 设置为 `Physical signal`

### **Ring-hub clearance when disengaged** — 分离时齿圈-轮毂间隙 `3` `mm`（默认）| 正标量

沿换挡连杆平移轴，齿圈和轮毂齿顶之间的最大开放间隙。此间隙对应于完全分离的离合器状态。齿高和完全分离时的齿圈-轮毂间隙决定了换挡连杆的最大行程跨度。此参数的值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`
- `Two-mode`，并将 **Abstract shift linkage control** 设置为 `Physical signal`

### **Hard stop at back of shift linkage** — 硬限位支撑选项 `on`（默认）| `off`

当换挡连杆行程超过完全分离位置时是否启用硬限位。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为：

- `Dynamic modal`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Shift linkage control** 设置为 `Conserving port`
- `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`

### **Ring stop stiffness** — 齿圈限位刚度 `10e5` `N/m`（默认）| 正标量

齿圈端部限位的线性刚度系数。此系数表征抵抗超过端部限位的平移运动的接触力的恢复分量。较大的刚度值对应于较大的接触力和较小的端部限位柔度。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`。

### **Ring stop damping** — 齿圈限位阻尼 `1e3` `N*s/m`（默认）| 非负标量

齿圈端部限位的线性阻尼系数。此系数表征抵抗超过端部限位的平移运动的接触力的耗散分量。较大的阻尼值对应于接触期间较大的能量耗散。该值必须大于或等于零

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`。

### **Shift linkage viscous friction coefficient** — 换挡连杆粘性摩擦系数 `100` `N*s/m`（默认）| 正标量

作用在换挡连杆上的线性阻尼系数。此系数表征由于粘性阻尼而抵抗换挡连杆运动的耗散力。较大的系数值对应于换挡连杆运动期间较大的能量耗散。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`。

### **Tooth-tooth friction coefficient** — 齿对齿接触动摩擦系数 `0.05`（默认）| 正标量

齿圈和轮毂齿之间接触界面处的动摩擦系数。此系数表征在离合器接合和分离期间由于齿对齿接触而抵抗换挡连杆运动的耗散力。

较大的系数值对应于换挡连杆运动期间较大的能量耗散。该值必须大于零。

#### 依赖关系

要启用此参数，请将：

- **Torque transmission model** 设置为 `Dynamic with backlash`
- **Shift linkage control** 设置为 `Conserving port`

### **Shift linkage engaged friction coefficient** — 接合摩擦系数 `100` `N*s/m`（默认）| 正标量

齿圈和轮毂接合时换挡连杆处的摩擦系数。此值是换挡连杆与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Shift linkage disengaged friction coefficient** — 分离摩擦系数 `50` `N*s/m`（默认）| 正标量

齿圈和轮毂分离时换挡连杆处的摩擦系数。此值是换挡连杆与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact speed threshold** — 静态接触速度阈值 `0.1` `m/s`（默认）| 正标量

t

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Static contact release force threshold** — 释放力阈值 `0.001` `N`（默认）| 正标量

齿圈和轮毂可以解锁并分离的力阈值。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### 接合条件

### **Linkage travel direction** — 接合条件行程方向 `Positive shift linkage displacement engages clutch`（默认）| `Negative shift linkage displacement engages clutch`

换挡连杆必须沿其移动才能使离合器接合的方向。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`

### **Maximum engagement speed** — 接合速度上限速度阈值 `inf`（默认）| 正标量

齿圈与轮毂之间的相对角速度，超过该值时离合器无法接合。该值特定于具体的变速箱或变速器。最小化该值有助于避免接合过程中的高动态冲击。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **Tooth overlap to engage** — 齿重叠接合阈值 `3` `mm`（默认）| 正标量

齿圈与轮毂齿沿公共纵向轴线的重叠长度。当齿重叠大于此值时，离合器接合。在啮合齿轮齿重叠至少达到此长度之前，离合器保持分离状态。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为

- `Dynamic modal`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Shift linkage control** 设置为 `Conserving port`
- `Dynamic with backlash`，并将 **Shift linkage control** 设置为 `Conserving port`

### **Engagement block stiffness** — 接合阻挡刚度系数 `10e6` `N/m`（默认）| 正标量

接合阻挡期间的刚度系数。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### **Engagement block damping** — 接合阻挡阻尼系数 `300` `N*s/m`（默认）| 正标量

接合阻挡期间的阻尼系数。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic modal`。

### 初始条件

### **Clutch locked** — 初始离合器状态 `off`（默认）| `on`

仿真开始时的离合器状态：

- `off` — 离合器在齿圈与轮毂之间传递零扭矩。
- `on` — 离合器在齿圈与轮毂之间传递扭矩。

### **Initial shift linkage position** — 初始换挡连杆位置 `0` `mm`（默认）| 标量

仿真时间零时的换挡连杆位置。当该值在零与齿圈-轮毂间隙之和之间时，离合器处于分离状态。

#### 依赖关系

要启用此参数，请设置：

- **Torque transmission model** 为 `Dynamic with backlash`
- **Thermal model** 为 `Omit`
- **Shift linkage control** 为 `Conserving port`

### **Initial ring-hub offset angle** — 初始齿圈-轮毂偏移角 `0` `deg`（默认）| 标量

仿真时间零时齿圈与轮毂之间的旋转角度。该角度决定齿圈与轮毂齿是否能接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N，

  其中 *N* 是齿圈或轮毂上的齿数。两个组件包含相同数量的齿。
- 如果离合器初始状态为接合，初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2，

  其中 *δ* 是齿圈与轮毂齿之间的齿隙角。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Dynamic with backlash`，并将 **Thermal port** 设置为 `Omit`。

### 热端口

### **Thermal mass** — 温度变化阻力 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时组件的温度。初始温度通过调整起始啮合或摩擦损耗来改变组件效率。

#### 依赖关系

要启用此参数，请将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2024a：捕获由于速度差导致的接合阻挡效应

当 **Torque transmission model** 为 `Dynamic modal` 时，您现在可以在系统级别捕获由于速度差导致的接合阻挡效应。

### R2023b：双模式支持

Dog Clutch 模块现在可以在 **Torque transmission model** 为 `Two-mode` 时对抽象行为进行建模。将此选项用于系统级设计或速度优先于精度的场合。

## 描述

带有齿板的离合器，当板齿啮合时接合

Dog Clutch 模块表示一种非滑动离合器，它利用互锁齿的正啮合在驱动轴之间传递扭矩。犬牙离合器常见于需要高速和频繁换挡的应用中。犬牙离合器通常用于摩托车手动变速器和一些工业机械。

齿圈和轮毂是犬牙离合器的两个主要组件。输入轴转动齿圈，齿圈上带有槽或齿。轮毂连接到输出轴，输出轴上带有突出的“犬牙”，可嵌入齿圈的槽中。当您换挡时，犬牙和槽啮合并锁定两个组件，从而传递动力。再次换挡使离合器分离，这使犬牙从槽中脱出，允许变速器自由旋转。齿圈和轮毂作为一个整体一起旋转。

为控制接合，犬牙离合器包含一个换挡连杆，用于控制齿圈相对于轮毂的位置。您可以通过 **Torque transmission model** 参数选择使用物理信号或机械平移守恒端口来控制换挡连杆。根据您的性能、保真度和离合器行为选择参数设置：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置足够快，可用于实时仿真，且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒端口来控制换挡连杆。
- `Dynamic with backlash` — 高保真离合器接合模型，考虑了齿隙、扭转柔度和齿圈与轮毂齿之间的接触力等现象。
- `Dynamic modal` — 中高保真模式图实现，模拟接合阻挡并从机械平移守恒端口确定换挡连杆位置。

将齿圈向轮毂移动使齿互锁，将离合器状态变为接合。齿重叠必须超过最小值才能接合。反向移动齿圈使两组齿不再互锁，将离合器状态变回分离。端口 **S** 指定换挡连杆位置。当离合器完全分离时，换挡连杆位置为零。当离合器完全接合时，换挡连杆位置等于齿高与完全分离状态下齿圈-轮毂间隙之和，

z=h+zGap，

其中：

- *z* 是换挡连杆位置。
- *h* 是齿高。
- *zGap* 是分离时的齿圈轮毂间隙。

该图显示了犬牙离合器的侧视图和前视图以及一些相关变量。

### 扭矩传递模型

您可以从以下扭矩传递模型中选择。

**双模式**

要模拟抽象的犬牙离合器，请将 **Torque transmission model** 设置为 `Two-mode`。双模式扭矩传递模型使用模式图来控制离合器是接合还是分离。您可以使用基于逻辑的命令或连杆位置物理信号来控制换挡连杆位置。当您使用基于逻辑的命令时，端口 **X** 处的 `false` 表示离合器分离，`true` 表示离合器接合。

**摩擦离合器近似模型**

当您将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and` 时，模块将离合器接合视为齿圈与轮毂之间的摩擦现象。此设置更适合线性化、固定步长仿真和硬件在环（HIL）仿真。模块使用 Fundamental Friction Clutch 模块的复合实现。

当您使用此设置时，离合器有三种可能的配置：分离、接合和锁定。分离时，齿圈与轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿圈-轮毂齿重叠 *h* 超过接合最小值时，两个组件之间的接触力开始随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到最大值，离合器状态切换为锁定。在此状态下，齿圈和轮毂作为一个整体旋转而无滑动。要解锁离合器，传递的扭矩必须超过 **Maximum transmitted torque** 参数的值。

**带齿隙的动态模型**

当您将 **Torque transmission model** 设置为 `Dynamic with backlash` 时，模块模拟齿隙、扭转柔度和齿圈与轮毂齿之间的接触力等离合器现象。此模型比摩擦离合器近似提供更高的精度。

当您使用此设置时，离合器有两种可能的配置：分离和接合。分离时，齿圈与轮毂之间的接触力为零。该力保持为零，直到换挡连杆达到接合的最小位置。

当齿圈-轮毂齿重叠 *h* 超过接合阈值时，离合器传递扭矩。该扭矩是扭转弹簧和阻尼器分量之和，包括齿圈与轮毂齿之间的齿隙，使得TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2，其中：

- *kRH* 是齿圈-轮毂耦合的扭转刚度。
- *ϕ* 是齿圈与轮毂之间绕公共旋转轴的相对角度。
- *δ* 是齿圈与轮毂齿之间的齿隙。
- *ω* 是齿圈与轮毂之间的相对角速度。该变量描述两个组件相互滑动的速度。

柔性端部止挡限制离合器换挡连杆和齿圈的平移运动。柔度模型将端部止挡视为线性弹簧-阻尼器组。端部止挡的位置取决于齿圈与轮毂齿之间的相对角度和角速度：

- 如果齿对齐且相对角速度小于离合器接合的最大值，端部止挡位置为完全分离时齿圈-轮毂间隙与齿高之和。离合器可在此端部止挡位置接合。
- 如果齿未对齐或相对角速度超过离合器接合的最大值，端部止挡位置设置为防止齿圈与轮毂接合。离合器不会在此端部止挡位置接合。

平移摩擦阻碍换挡连杆和齿圈的运动。该摩擦是库仑分量和粘性分量之和，使得FZ=−kK·FN·tanh(4vvth)−μTv，其中：

- *FZ* 是作用在换挡连杆和齿圈上的净平移摩擦力。
- *kK* 是齿圈与轮毂齿之间的动摩擦系数。
- *FN* 是齿圈与轮毂齿之间的法向力，其中 *FN* = *TC*/*Rm*。
- *v* 是换挡连杆和齿圈的平移速度。
- *vth* 是平移速度阈值。低于此阈值时，双曲正切函数在换挡连杆和齿圈速度趋于零时将库仑摩擦力平滑至零。
- *μT* 是作用在换挡连杆和齿圈上的粘性阻尼系数。

**动态模态**

当您将 **Torque transmission model** 设置为 `Dynamic modal` 时，模块通过从机械平移守恒端口 **S** 获取换挡连杆位置来确定离散离合器模态行为。此设置比 `Two-mode` 参数化捕获更复杂的离合器动力学，并且比 `Friction clutch approximation` 和 `Dynamic with backlash` 设置更快。

您可以使用 `Dynamic modal` 设置来模拟当速度差过大以致离合器片无法接合时的接合阻挡。模块将接合阻挡表示为弹簧-阻尼器系统，您可以参数化弹簧和阻尼系数。接合模式重叠，这防止模式改变，直到换挡连杆位置超出接合重叠区域。您使用 **Tooth overlap to engage** 参数定义接合重叠区域。

图示了接合与分离之间的模式转换。z 变量表示换挡连杆位置。接合和分离模态区域重叠，这衰减了模式转换速率。

连杆位置约束为：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **Tooth height** 参数。
- *zGap* 是 **Ring hub clearance when disengaged** 参数。
- *zOverlap* 是 **Tooth overlap to engage** 参数。
- *ωthr* 是 **Engagement speed threshold** 参数。

接合模式位置为：

- *z* = 0 — 离合器完全分离。
- 0 < *z* < *zGap* — 当换挡连杆位置在 *zGap* 定义的区域内时，离合器分离。离合器可在 *x* = *zGap* + *zOverlap* 处从分离转换到接合。
- *zGap* < *z* < *h* — 当 *z* 在 *h* 定义的区域内时，离合器接合。离合器可在 *z* = *zGap* 处从接合转换到分离。
- *z* = *zGap* + *h* — 离合器完全接合。
- *z* = *zGap* + *zOverlap* — 当 *z* 在接合重叠区域内时，离合器仅在速度差小于 *ωthr* 参数的值时接合。

### 旋转功率耗散

当离合器在施加扭矩下打滑时，它会耗散功率。功率损耗等于滑移角速度与齿圈和轮毂之间接触扭矩的乘积，使得

Ploss=ω · TC，

其中：

- *Ploss* 是由于打滑而耗散的功率。
- *TC* 是动接触扭矩。

### 热建模

当您将 **Torque transmission model** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 时，您可以使用可选的热守恒端口 **T** 来建模热流和温度变化的影响。

### 线性化

要针对线性化优化模型，请使用 **Clutch** > **Torque transmission model** 参数的默认设置，即 `Friction clutch approximation -
适用于 HIL 和线性化`。

### 硬件在环仿真

为获得最佳仿真性能，请使用 **Clutch** > **Torque transmission model** 参数的默认设置，即 `Friction clutch approximation -
适用于 HIL 和线性化`。
