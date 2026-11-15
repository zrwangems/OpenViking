---
type: simulink-block
title: 'Dog Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
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

### **S** — 逻辑换挡机构，无量纲物理信号

与换挡机构关联的物理信号输入端口，无量纲。逻辑 `true` 允许离合器在轮毂和齿环的相对速度处于容差范围内时接合。逻辑 `false` 使离合器分离。

#### 依赖关系

要启用此端口，将 **扭矩传递模型** 设置为：

- `Two-mode`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **换挡机构控制** 设置为 `Physical signal`
- `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Physical signal`

### 输出

### **X** — 离合器位置，m 或无量纲物理信号

与离合器位置关联的物理信号输出端口，以 *m* 为单位或无量纲。当将 **扭矩传递模型** 设置为 `Two-mode` 时，该端口输出逻辑值 `true` 表示接合，或 `false` 表示分离。否则，该端口输出离合器的位置。

### 守恒

### **H** — 离合器轮毂机械旋转

与离合器轮毂关联的机械旋转守恒端口

### **R** — 离合器齿环机械旋转

与离合器齿环关联的机械旋转守恒端口。

### **S** — 换挡机构机械平动

与换挡机构关联的机械平动守恒端口。

#### 依赖关系

要启用此端口，将 **扭矩传递模型** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic modal`
- `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Conserving port`

### **T** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

## 参数

### 离合器

### **扭矩传递模型** — 扭矩传递模型 `Two-mode`（默认） | `Friction clutch approximation - Suitable for HIL and linearization` | `Dynamic with backlash` | `Dynamic modal`

为爪式离合器行为建模的方法：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置足够快，可用于实时仿真，并且不需要了解离合器尺寸。只能使用物理信号或逻辑控制信号来控制换挡机构。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中等至高保真度复合实现。此设置支持热建模。可以使用物理信号或机械平动守恒连接来控制换挡机构。
- `Dynamic with backlash` — 高保真度离合器接合模型，考虑了齿隙、扭转柔度和齿环与轮毂齿之间的接触力等现象。
- `Dynamic modal` — 系统级离合器接合模型，可捕获因速度差导致的接合阻塞效应。

### **接合速度阈值** — 接合速度阈值 `5` `rpm`（默认） | 正标量

离合器传递动力的最小转速。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Two-mode` 或 `Dynamic modal`。

### **热端口** — 启用热端口的选项 `Omit`（默认） | `Model`

是否启用热守恒端口 **T**。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`。

### **离合器齿平均半径** — 离合器齿平均半径 `50` `mm`（默认） | 正标量

从齿环或轮毂中心到对应齿中心的距离。在给定两个组件之间的传递扭矩时，平均齿半径决定齿环与轮毂齿之间的法向接触力。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **最大传递扭矩** — 最大传递扭矩 `1000` `N*m`（默认） | 正标量

离合器能够传递的最大扭矩。此值对应于无滑动接合配置。如果齿环与轮毂之间传递的扭矩超过此值，两个组件开始相对滑动。此扭矩决定摩擦离合器近似中的静摩擦极限。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Omit`。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认） | 向量

温度值。最小值的数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

### **最大传递扭矩向量** — 最大传递扭矩 `[1000, 1050, 1000]` `N*m`（默认） | 向量

在 **温度向量** 参数中给定温度下的最大传递扭矩。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

### **插值方法** — 插值方法 `Linear`（默认） | `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

### **外插方法** — 外插方法 `Linear`（默认） | `Nearest` | `Error`

当输入值位于参数列表指定的范围之外时，用于确定输出值的外插方法：

- `Linear` — 选择此选项以在外插区域以及与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外插。
- `Error` — 选择此选项以避免进入外插模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

### **齿数** — 齿环或轮毂的齿数 `6`（默认） | 正非零标量整数

齿环或轮毂中的总齿数。两个组件的齿数相等。该值必须大于或等于一。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **旋转间隙** — 旋转间隙 `10` `deg`（默认） | 正标量

离合器接合时，齿环与轮毂齿之间允许的角运动或游隙。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **扭转刚度** — 扭转刚度 `10e6` `N*m/rad`（默认） | 正标量

齿环与轮毂齿之间接触界面处的线性扭转刚度系数。此系数表征两组齿之间接触力的恢复分量。刚度值越大，接触力越大。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### **扭转阻尼** — 扭转阻尼 `100` `N*m*s/rad`（默认） | 正标量

齿环与轮毂齿之间接触界面处的线性扭转阻尼系数。此系数表征两组齿之间接触力的耗散分量。阻尼值越大，接触期间的能量耗散越大。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic with backlash`。

### 换挡机构

### **抽象换挡机构控制** — 双模式换挡机构控制选项 `Logic-controlled`（默认） | `Physical signal`

用于双模式扭矩传递的抽象换挡机构控制。

- `Logic-controlled` — 使用物理信号端口 **S** 将换挡机构作为布尔运算符输入。
- `Physical signal` — 直接通过物理信号端口 **S** 输入换挡机构位置。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Two-mode`。

### **换挡机构控制** — 换挡机构控制端口 `Physical signal`（默认） | `Conserving port`

换挡机构控制的端口类型：

- `Physical signal` — 直接通过物理信号端口 **S** 输入换挡机构位置。
- `Conserving port` — 通过平动守恒端口 **S** 动态输入换挡机构位置。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **齿高** — 齿高 `10` `mm`（默认） | 正标量

齿根与齿顶之间的距离。齿环和轮毂齿具有相同的高度。齿高和完全分离时的齿环-轮毂间隙决定换挡机构的最大行程范围。此参数的值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`
- `Two-mode`，并将 **抽象换挡机构控制** 设置为 `Physical signal`

### **分离时齿环-轮毂间隙** — 分离时齿环-轮毂间隙 `3` `mm`（默认） | 正标量

沿换挡机构平动轴方向，齿环与轮毂齿顶之间的最大开口间隙。此间隙对应于离合器完全分离状态。齿高和完全分离时的齿环-轮毂间隙决定换挡机构的最大行程范围。此参数的值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`
- `Two-mode`，并将 **抽象换挡机构控制** 设置为 `Physical signal`

### **换挡机构后部硬限位** — 硬限位选项 `on`（默认） | `off`

当换挡机构运动超过完全分离位置时，是否启用硬限位。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为：

- `Dynamic modal`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **换挡机构控制** 设置为 `Conserving port`
- `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Conserving port`

### **齿环限位刚度** — 齿环限位刚度 `10e5` `N/m`（默认） | 正标量

齿环端部限位的线性刚度系数。此系数表征抵抗超过端部限位的平动运动的接触力恢复分量。刚度值越大，接触力越大，端部限位柔量越小。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Conserving port`。

### **齿环限位阻尼** — 齿环限位阻尼 `1e3` `N*s/m`（默认） | 非负标量

齿环端部限位的线性阻尼系数。此系数表征抵抗超过端部限位的平动运动的接触力耗散分量。阻尼值越大，接触期间的能量耗散越大。该值必须大于或等于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Conserving port`。

### **换挡机构粘性摩擦系数** — 换挡机构粘性摩擦系数 `100` `N*s/m`（默认） | 正标量

作用在换挡机构上的线性阻尼系数。此系数表征因粘性阻尼而抵抗换挡机构运动的耗散力。系数值越大，换挡机构运动期间的能量耗散越大。该值必须大于零。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`，并将 **换挡机构控制** 设置为 `Conserving port`。

### **齿间摩擦系数** — 齿间接触动摩擦系数 `0.05`（默认） | 正标量

齿环与轮毂齿之间接触界面处的动摩擦系数。此系数表征在离合器接合和分离期间因齿间接触而抵抗换挡机构运动的耗散力。

系数值越大，换挡机构运动期间的能量耗散越大。该值必须大于零。

#### 依赖关系

要启用此参数，设置：

- **扭矩传递模型** 为 `Dynamic with backlash`
- **换挡机构控制** 为 `Conserving port`

### **换挡机构接合摩擦系数** — 接合摩擦系数 `100` `N*s/m`（默认） | 正标量

齿环和轮毂接合时换挡机构处的摩擦系数。此值是换挡机构与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **换挡机构分离摩擦系数** — 分离摩擦系数 `50` `N*s/m`（默认） | 正标量

齿环和轮毂分离时换挡机构处的摩擦系数。此值是换挡机构与其支撑之间的摩擦。

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触速度阈值** — 静态接触速度阈值 `0.1` `m/s`（默认） | 正标量

t

#### 依赖关系

要启用此参数，将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **静态接触释放力阈值** — 释放力阈值 `0.001` `N`（默认） | 正标量

力阈值，超过该阈值时齿环和轮毂可以解锁并分离。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Dynamic modal`。

### 接合条件

### **连杆行程方向** — 接合条件行程方向 `Positive shift linkage displacement engages clutch`（默认） | `Negative shift linkage displacement engages clutch`

换挡连杆为接合离合器必须行进的方向。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为：

- `Friction clutch approximation - Suitable for HIL and linearization`
- `Dynamic with backlash`
- `Dynamic modal`

### **最大接合速度** — 接合速度上限速度阈值 `inf`（默认） | 正标量

环与毂之间的相对角速度，高于该值时离合器无法接合。该值特定于具体的变速箱或变速器。最小化该值有助于避免接合期间的高动态冲击。该值必须大于零。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 或 `Dynamic with backlash`。

### **接合所需齿重叠** — 齿重叠接合阈值 `3` `mm`（默认） | 正标量

环齿与毂齿沿共同纵向轴线的重叠长度。当齿重叠大于此值时，离合器接合。在啮合齿轮齿重叠至少达到此长度之前，离合器保持分离。该值必须大于零。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为

- `Dynamic modal`
- `Friction clutch approximation - Suitable for HIL and linearization`，并将 **换挡连杆控制** 设置为 `Conserving port`
- `Dynamic with backlash`，并将 **换挡连杆控制** 设置为 `Conserving port`

### **接合阻挡刚度** — 接合阻挡刚度系数 `10e6` `N/m`（默认） | 正标量

接合阻挡期间的刚度系数。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Dynamic modal`。

### **接合阻挡阻尼** — 接合阻挡阻尼系数 `300` `N*s/m`（默认） | 正标量

接合阻挡期间的阻尼系数。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Dynamic modal`。

### 初始条件

### **离合器锁止** — 初始离合器状态 `off`（默认） | `on`

仿真开始时的离合器状态：

- `off` — 离合器在环与毂之间传递零扭矩。
- `on` — 离合器在环与毂之间传递扭矩。

### **初始换挡连杆位置** — 初始换挡连杆位置 `0` `mm`（默认） | 标量

仿真时间零时的换挡连杆位置。当该值介于零与环-毂间隙之和之间时，离合器分离。

#### 依赖项

要启用此参数，请设置：

- **扭矩传递模型** 设置为 `Dynamic with backlash`
- **热模型** 设置为 `Omit`
- **换挡连杆控制** 设置为 `Conserving port`

### **初始环-毂偏移角** — 初始环-毂偏移角 `0` `deg`（默认） | 标量

仿真时间零时环与毂之间的旋转角度。此角度决定环齿与毂齿能否接合。初始偏移角必须满足以下条件：

- 如果离合器初始状态为分离，则初始偏移角必须落在以下范围内

  −180°N≤ϕ0≤+180°N,

  其中 *N* 是环或毂中的齿数。两个部件包含相同数量的齿。
- 如果离合器初始状态为接合，则初始偏移角必须落在以下范围内

  −δ2≤ϕ0≤+δ2,

  其中 *δ* 是环齿与毂齿之间的间隙角。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Dynamic with backlash`，并将 **热端口** 设置为 `Omit`。

### 热端口

### **热质量** — 对温度变化的阻力 `50` `kJ/K`（默认） | 标量

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

### **初始温度** — 初始温度 `300` `K`（默认） | 标量

仿真开始时的组件温度。初始温度通过调整起始啮合损失或摩擦损失来改变组件效率。

#### 依赖项

要启用此参数，请将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization`，并将 **热端口** 设置为 `Model`。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2024a: 捕获由于速度差导致的接合阻挡效应

现在，当 **扭矩传递模型** 为 `Dynamic modal` 时，您可以在系统级捕获由于速度差导致的接合阻挡效应。

### R2023b: 双模式支持

当 **扭矩传递模型** 为 `Two-mode` 时，Dog Clutch 模块现在可以对抽象行为进行建模。将此选项用于系统级设计，或在速度优先于精度的场合。

## 描述

当板齿啮合时接合的带齿板离合器

Dog Clutch 模块表示一种非滑动离合器，它利用互锁齿的强制啮合在驱动轴之间传递扭矩。Dog 离合器常见于需要高速和频繁换挡的应用中。Dog 离合器通常用于摩托车手动变速器和一些工业机械。

环和毂是 Dog 离合器的主要组件。输入轴转动环，环上具有槽或齿。毂连接到输出轴，输出轴具有突出的“dogs”，可嵌入环的槽中。当您换挡时，dogs 和槽接合，锁止两个组件并传递动力。再次换挡以分离离合器，这会使 dogs 与槽脱开，并允许变速器自由旋转。环和毂作为一个整体一起旋转。

为控制接合，Dog 离合器包含一个换挡连杆，用于控制环相对于毂的位置。您可以使用 **扭矩传递模型** 参数选择通过物理信号或机械平移守恒端口来控制换挡连杆。根据性能、保真度和离合器行为选择参数设置：

- `Two-mode` — 基于模式图的完全抽象扭矩传递模型。此设置对于实时仿真足够快，并且不需要了解离合器尺寸。您只能使用物理信号或逻辑控制信号来控制换挡连杆。
- `Friction clutch approximation - Suitable for HIL and linearization` — Fundamental Friction Clutch 模块的中高保真复合实现。此设置支持热建模。您可以使用物理信号或机械平移守恒端口来控制换挡连杆。
- `Dynamic with backlash` — 高保真离合器接合模型，考虑间隙、扭转柔度和环齿与毂齿之间的接触力等现象。
- `Dynamic modal` — 中高保真模式图实现，可仿真接合阻挡，并从机械平移守恒端口确定换挡连杆位置。

将环朝向毂移动，使齿互锁，会将离合器状态变为接合。齿重叠必须超过最小值才能接合。反向移动环，使两组齿不再互锁，会将离合器状态变回分离。端口 **S** 指定换挡连杆位置。当离合器完全分离时，换挡连杆位置为零。当离合器完全接合时，换挡连杆位置等于齿高与完全分离状态下的环-毂间隙之和，

z=h+zGap,

其中：

- *z* 是换挡连杆位置。
- *h* 是齿高。
- *zGap* 是分离时的环-毂间隙。

该图显示了 Dog 离合器的侧视图和前视图及其一些相关变量。

### 扭矩传递模型

您可以从以下扭矩传递模型中选择。

**双模式**

要仿真抽象 Dog 离合器，请将 **扭矩传递模型** 设置为 `Two-mode`。双模式扭矩传递模型使用模式图来控制离合器是接合还是分离。您可以使用基于逻辑的命令或连杆位置物理信号来控制换挡连杆位置。使用基于逻辑的命令时，端口 **X** 处的 `false` 表示离合器分离，`true` 表示离合器接合。

**摩擦离合器近似模型**

当您将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and` 时，模块将离合器接合视为环与毂之间的摩擦现象。此设置更适合线性化、固定步长仿真和硬件在环（HIL）仿真。该模块使用 Fundamental Friction Clutch 模块的复合实现。

使用此设置时，离合器有三种可能的配置：分离、接合和锁止。分离时，环与毂之间的接触力为零。在换挡连杆达到接合最小位置之前，该力保持为零。

当环-毂齿重叠 *h* 超过接合最小值时，两个组件之间的接触力开始随换挡连杆位置 *z* 线性增加。

在完全接合时，接触力达到最大值，离合器状态切换为锁止。在此状态下，环和毂作为一个整体无滑动地旋转。要解锁离合器，传递的扭矩必须超过 **最大传递扭矩** 参数的值。

**带间隙的动态模型**

当您将 **扭矩传递模型** 设置为 `Dynamic with backlash` 时，模块会仿真离合器现象，例如间隙、扭转柔度和环齿与毂齿之间的接触力。此模型比摩擦离合器近似提供更高的精度。

使用此设置时，离合器有两种可能的配置：分离和接合。分离时，环与毂之间的接触力为零。在换挡连杆达到接合最小位置之前，该力保持为零。

当环-毂齿重叠 *h* 超过接合阈值时，离合器传递扭矩。此扭矩是扭转弹簧和阻尼器分量之和，包括环齿与毂齿之间的间隙，使得TC={−kRH(ϕ−δ2)−μR· ωϕ>δ20−δ2<ϕ<δ2−kRH(ϕ+δ2)−μRωϕ<−δ2,其中：

- *kRH* 是环-毂耦合的扭转刚度。
- *ϕ* 是环与毂之间绕共同旋转轴的相对角度。
- *δ* 是环齿与毂齿之间的间隙。
- *ω* 是环与毂之间的相对角速度。此变量描述两个组件相互滑过的速度。

柔性端挡限制离合器换挡连杆和环的平移运动。柔度模型将端挡视为线性弹簧-阻尼器组。端挡的位置取决于环齿与毂齿之间的相对角度和角速度：

- 如果齿对齐且相对角速度小于离合器接合的最大值，则端挡位置为完全分离时的环-毂间隙与齿高之和。离合器可在此端挡位置接合。
- 如果齿未对齐或相对角速度超过离合器接合的最大值，则设置端挡位置以防止环与毂接合。离合器不在此端挡位置接合。

平移摩擦阻碍换挡连杆和环的运动。此摩擦是库仑分量和黏性分量之和，使得FZ=−kK·FN·tanh(4vvth)−μTv,其中：

- *FZ* 是作用在换挡连杆和环上的净平移摩擦力。
- *kK* 是环齿与毂齿之间的动摩擦系数。
- *FN* 是环齿与毂齿之间的法向力，其中 *FN* = *TC*/*Rm*。
- *v* 是换挡连杆和环的平移速度。
- *vth* 是平移速度阈值。低于此阈值时，当换挡连杆和环的速度趋于零时，双曲正切函数将库仑摩擦力平滑至零。
- *μT* 是作用在换挡连杆和环上的黏性阻尼系数。

**动态模态**

当您将 **扭矩传递模型** 设置为 `Dynamic modal` 时，模块通过从机械平移守恒端口 **S** 获取换挡连杆位置来确定离散离合器模态行为。此设置捕获比 `Two-mode` 参数化更复杂的离合器动力学，并且比 `Friction clutch approximation` 和 `Dynamic with backlash` 设置更快。

当速度差太大以至于离合器片无法接合时，您可以使用 `Dynamic modal` 设置来仿真接合阻挡。该模块将接合阻挡表示为弹簧-阻尼器系统，您可以在其中参数化弹簧和阻尼系数。接合模式重叠，这会防止模式发生变化，直到换挡连杆位置超出接合重叠区域。您使用 **接合所需齿重叠** 参数定义接合重叠区域。

描绘接合与分离之间模式转换的图。z 变量表示换挡连杆位置。接合和分离模态区域重叠，这会衰减模式转换速率。

连杆位置约束为：

- *z* 是端口 **S** 处的换挡连杆位置。
- *h* 是 **齿高** 参数。
- *zGap* 是 **分离时的环-毂间隙** 参数。
- *zOverlap* 是 **接合所需齿重叠** 参数。
- *ωthr* 是 **接合速度阈值** 参数。

接合模式位置为：

- *z* = 0 — 离合器完全分离。
- 0 < *z* < *zGap* — 当换挡连杆位置位于由 *zGap* 定义的区域时，离合器分离。离合器可在 *x* = *zGap* + *zOverlap* 处从分离转换为接合。
- *zGap* < *z* < *h* — 当 *z* 位于由 *h* 定义的区域时，离合器接合。离合器可在 *z* = *zGap* 处从接合转换为分离。
- *z* = *zGap* + *h* — 离合器完全接合。
- *z* = *zGap* + *zOverlap* — 当 *z* 位于接合重叠区域时，仅当速度差小于 *ωthr* 参数的值时，离合器才接合。

### 旋转功率耗散

当离合器在施加扭矩下打滑时，它会耗散功率。功率损耗等于打滑角速度与环和毂之间接触扭矩的乘积，因此

Ploss=ω · TC,

其中：

- *Ploss* 是由于打滑而耗散的功率。
- *TC* 是动接触扭矩。

### 热建模

当您将 **扭矩传递模型** 设置为 `Friction clutch approximation - Suitable for HIL and linearization` 时，您可以使用可选热守恒端口 **T** 对热流和温度变化的影响进行建模。

### 线性化

要为线性化优化您的模型，请使用 **Clutch** > **Torque transmission model** 参数的默认设置，`Friction clutch approximation -
Suitable for HIL and linearization`。

### 硬件在环仿真

为获得最佳仿真性能，请使用 **Clutch** > **Torque transmission model** 参数的默认设置，`Friction clutch approximation -
Suitable for HIL and linearization`。
