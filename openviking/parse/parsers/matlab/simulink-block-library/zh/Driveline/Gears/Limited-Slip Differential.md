---
type: simulink-block
title: 'Limited-Slip Differential'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'limitedslipdifferential'
documentation_source_path: 'ref/limitedslipdifferential.html'
language: zh-CN
chinese_source: worker-translation
---

# Limited-Slip Differential

## 端口
```yaml
ports:
- name: D
  summary: 驱动轴旋转机械
  direction: unspecified
- name: S1
  summary: 太阳轮 1 旋转机械
  direction: unspecified
- name: S2
  summary: 太阳轮 2 旋转机械
  direction: unspecified
- name: H
  summary: 热流热
  direction: unspecified
```

### 守恒

### **D** — 驱动轴旋转机械

与驱动轴关联的旋转机械守恒端口。

### **S1** — 太阳轮 1 旋转机械

与太阳轮 1 轴关联的旋转机械守恒端口。

### **S2** — 太阳轮 2 旋转机械

与太阳轮 2 轴关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖

要启用此端口，请在 **Differential** 选项卡中，将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 参数
```yaml
parameters:
- name: Crown gear located
  summary: 冠齿轮位置 To the right of centerline（默认）| To the left of centerline
  group: Differential
- name: Carrier (C) to driveshaft (D) teeth ratio (NC/ND)
  summary: 冠齿轮与驱动轴小齿轮的齿数比 4（默认）| 正标量
  group: Differential
- name: Friction model
  summary: 摩擦模型 No meshing losses - Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: Differential
- name: Sun-sun and carrier-driveshaft ordinary efficiencies
  summary: 差速器扭矩恒定传递效率 [.85, .92]（默认）| 向量
  group: Differential
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 向量
  group: Differential
- name: Sun-sun efficiency
  summary: 从驱动太阳轮到从动太阳轮的扭矩传递效率 [.95, .9, .85]（默认）| 向量
  group: Differential
- name: Carrier-driveshaft efficiency
  summary: 从冠齿轮到驱动轴小齿轮的扭矩传递效率 [.95, .9, .85]（默认）| 向量
  group: Differential
- name: Sun-carrier and driveshaft-casing power thresholds
  summary: 太阳轮-行星架和驱动轴-壳体齿轮联轴器的最小效率功率阈值 [.001, .001] W（默认）| 向量
  group: Differential
- name: Sun-carrier and driveshaft-casing viscous friction coefficients
  summary: 粘性摩擦系数 [0, 0] N*m/(rad/s)（默认）| 向量
  group: Differential
- name: Inertia
  summary: 惯性选项 off（默认）| on
  group: Differential
- name: Sun gear inertia
  summary: 太阳轮惯性 0.001 kg*m^2（默认）| 正标量
  group: Differential
- name: Sun gear radius
  summary: 太阳轮半径 0.01 m（默认）| 正标量
  group: Differential
- name: Carrier inertia
  summary: 行星架惯性 0.001 kg*m^2（默认）| 正标量
  group: Differential
- name: Planet gear spin inertia
  summary: 行星齿轮自转惯性 0.001 kg*m^2（默认）| 正标量
  group: Differential
- name: Planet gear mass
  summary: 行星齿轮质量 0.001 kg*m^2（默认）| 正标量
  group: Differential
- name: Number of friction surfaces
  summary: 接触面数量 4（默认）| 正标量
  group: Clutch
- name: Effective torque radius
  summary: 摩擦力作用半径 130 mm（默认）| 正标量
  group: Clutch
- name: Preload force
  summary: 离合器片接合压力 300 N（默认）| 非负标量
  group: Clutch
- name: Static friction coefficient
  summary: 静摩擦系数 0.35（默认）| 正标量
  group: Clutch
- name: Static friction coefficient vector
  summary: 静摩擦系数 [.4, .38, .36]（默认）| 向量
  group: Clutch
- name: Kinetic friction coefficient relative velocity vector
  summary: 绝对表面速度 [0, 100, 1000] rad/s（默认）| 向量
  group: Clutch
- name: Kinetic friction coefficient vector
  summary: 库仑摩擦系数 *k*K [.3, .22, .19]（默认）| 向量
  group: Clutch
- name: Kinetic friction coefficient matrix
  summary: 库仑摩擦系数 *k*K [.34, .32, .3; .3, .28, .25; .25, .2, .15]（默认）| 矩阵
  group: Clutch
- name: Friction coefficient interpolation method
  summary: 输出值填充方法 Linear（默认）| Smooth
  group: Clutch
- name: Friction coefficient extrapolation method
  summary: 输出值外推方法 Linear（默认）| Nearest
  group: Clutch
- name: Velocity tolerance
  summary: 滑移速度锁定边界 0.001 rad/s（默认）
  group: Clutch
- name: Initial state
  summary: 初始离合器状态 Unlocked（默认）| Locked
  group: Clutch
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 标量
  group: Thermal Port
- name: Initial temperature
  summary: 初始温度 300 K（默认）| 标量
  group: Thermal Port
```

### Differential

### **Crown gear located** — 冠齿轮位置 `To the right of centerline`（默认）| `To the left of centerline`

锥冠齿轮相对于齿轮组件中心线的位置。

### **Carrier (C) to driveshaft (D) teeth ratio (NC/ND)** — 冠齿轮与驱动轴小齿轮的齿数比 `4`（默认）| 正标量

冠齿轮齿数 *NC* 与驱动轴小齿轮齿数 *ND* 之比的固定比值 *gD*。此齿轮比必须严格大于 `0`。冠齿轮刚性安装在行星架上。

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`— 齿轮啮合为理想状态。
- `Constant efficiency`— 齿轮副之间的扭矩传递按恒定效率 *η* 降低，其中 0<η≤1。
- `Temperature-dependent efficiency`— 齿轮副之间的扭矩传递由温度查找表定义

### **Sun-sun and carrier-driveshaft ordinary efficiencies** — 差速器扭矩恒定传递效率 `[.85, .92]`（默认）| 向量

扭矩传递效率向量 [*ηSS*, *ηCD*]。其中，

- *ηSS* 是描述从驱动太阳轮到从动太阳轮功率流的输出输入功率比。
- *ηCD* 是描述从冠齿轮到驱动轴小齿轮功率流的输出输入功率比。

行星架刚性安装在冠齿轮上。向量元素必须在 (0,1] 范围内。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-sun efficiency** — 从驱动太阳轮到从动太阳轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从驱动太阳轮到从动太阳轮功率流的输出输入功率比向量 *ηSS*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Carrier-driveshaft efficiency** — 从冠齿轮到驱动轴小齿轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从冠齿轮到驱动轴小齿轮功率流的输出输入功率比向量 *ηCD*。模块使用这些值构建一维温度-效率查找表。行星架齿轮刚性安装在冠齿轮上。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-carrier and driveshaft-casing power thresholds** — 太阳轮-行星架和驱动轴-壳体齿轮联轴器的最小效率功率阈值 `[.001, .001]` `W`（默认）| 向量

太阳轮-行星架和纵向驱动轴-壳体 [*pS*, *pD*] 的功率阈值向量 *pth*。高于这些值时应用完整效率损失。低于这些值时，双曲正切函数对效率因子进行平滑处理。

当将 **Friction model** 设置为 `Constant efficiency` 时，模块在无功率传输时将效率损失降为零。当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块在静止时为零与功率阈值处温度-效率查找表提供的值之间对效率因子进行平滑处理。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### **Sun-carrier and driveshaft-casing viscous friction coefficients** — 粘性摩擦系数 `[0, 0]` `N*m/(rad/s)`（默认）| 向量

太阳轮-行星架和纵向驱动轴-壳体齿轮运动的粘性摩擦系数向量 [*μS*, *μD*]。

### **Inertia** — 惯性选项 `off`（默认）| `on`

是否在模块中包含惯性效应。

### **Sun gear inertia** — 太阳轮惯性 `0.001` `kg*m^2`（默认）| 正标量

太阳轮惯性。

#### 依赖

要启用此参数，请选中 **Inertia**。

### **Sun gear radius** — 太阳轮半径 `0.01` `m`（默认）| 正标量

太阳轮半径。

#### 依赖

要启用此参数，请选中 **Inertia**。

### **Carrier inertia** — 行星架惯性 `0.001` `kg*m^2`（默认）| 正标量

行星齿轮行星架的转动惯量。

#### 依赖

要启用此参数，请选中 **Inertia**。

### **Planet gear spin inertia** — 行星齿轮自转惯性 `0.001` `kg*m^2`（默认）| 正标量

行星齿轮绕自身轴线的惯性。

#### 依赖

要启用此参数，请选中 **Inertia**。

### **Planet gear mass** — 行星齿轮质量 `0.001` `kg*m^2`（默认）| 正标量

行星齿轮质量。

#### 依赖

要启用此参数，请选中 **Inertia**。

### Clutch

### **Number of friction surfaces** — 接触面数量 `4`（默认）| 正标量

离合器内部产生摩擦的接触面数量 *N*。

### **Effective torque radius** — 摩擦力作用半径 `130` `mm`（默认）| 正标量

确定离合器内部动摩擦扭矩的有效力臂半径 *reff*。

### **Preload force** — 离合器片接合压力 `300` `N`（默认）| 非负标量

弹簧预紧力施加在离合器片组件上的力。必须大于或等于零。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认）| 正标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation` 或 `Fixed kinetic friction coefficient`。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

给定温度下摩擦系数的静态值或峰值向量。向量长度必须与 **Temperature** 相同。每个元素必须大于 **Kinetic friction coefficient matrix** 中对应行的最大值。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Kinetic friction coefficient relative velocity vector** — 绝对表面速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值向量。向量中的值必须从左到右递增。最小值的数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

### **Kinetic friction coefficient vector** — 库仑摩擦系数 *k*K `[.3, .22, .19]`（默认）| 向量

动摩擦系数的输出值向量。所有值必须大于零。

#### 依赖

要启用此参数，请在 **Differential** 选项卡中，将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation` 或 `Constant efficiency`。

### **Kinetic friction coefficient matrix** — 库仑摩擦系数 *k*K `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值矩阵。所有值必须大于零。

#### 依赖

要启用此参数，请在 **Differential** 选项卡中，将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Friction coefficient interpolation method** — 输出值填充方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时用于近似输出值的插值方法。为优化性能，请选择 `Linear`。要生成具有连续一阶导数的连续曲线，请选择 `Smooth`。

有关插值算法的更多信息，请参阅 PS Lookup Table (1D)。

### **Friction coefficient extrapolation method** — 输出值外推方法 `Linear`（默认）| `Nearest`

当输入值超出参数列表中指定的范围时用于近似输出值的外推方法。要在外推区域以及在与插值区域的边界处生成具有连续一阶导数的曲线，请选择 `Linear`。要生成不高于数据中最高点或低于数据中最低点的外推，请选择 `Nearest`。

有关插值算法的更多信息，请参阅 PS Lookup Table (1D)。

### **Velocity tolerance** — 滑移速度锁定边界 `0.001` `rad/s`（默认）

离合器可以锁定的最大滑移速度。滑移速度是基轴与从动轴角速度之间的有符号差值，w=wF−wB。当动摩擦扭矩非零且传递扭矩在静摩擦扭矩限值内时，如果实际滑移速度低于速度容差，则离合器锁定。

### **Initial state** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：锁定和解锁。锁定的离合器约束基轴和从动轴以相同速度旋转，即作为单个单元。解锁的离合器允许两个轴以不同速度旋转，从而在离合器片之间产生滑移。

### Thermal Port

要启用这些设置，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度变化一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的模块温度。初始温度根据各自的效率向量设置初始组件效率。

#### 依赖

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2025a：枚举更新

**Inertia** 参数现在使用复选框。此参数在之前的版本中使用下拉菜单。

### R2024b：惯性更新

您现在可以指定所有齿轮子组件（包括太阳轮、齿圈和行星架齿轮）的惯性。您现在还可以在行星齿轮惯性行为中包含行星进动的影响。

## 描述

减小两个连接轴之间的速度差

Limited-Slip Differential 模块表示限滑差速器（LSD），它是一种齿轮组件，用于限制两个连接轴之间的速度差。该模块将 LSD 机构建模为一个结构组件，结合了差速器和离合器。

LSD 模块中的差速器组件是一个开放式差速器。*开放式差速器*是一种齿轮机构，允许两个从动轴以不同速度旋转。在汽车中，差速器允许内侧车轮在车辆转弯时比外侧车轮旋转得更慢。车轮轴通过开放式差速器连接的车辆，当其中一个车轮因失去牵引力而打滑并自由旋转时，车辆可能会被困住。该车辆停止移动，因为传动轴向有牵引力的车轮提供的动力少于向打滑车轮提供的动力。

在相同场景下，配备 LSD 的车辆不太可能被困住，因为它包含一个离合器组件，可以将动力传递给保持牵引力的车轮。LSD 模块中的离合器组件是一个摩擦离合器，具有两组扁平摩擦片。当施加的压力超过接合阈值压力时，离合器接合。在 LSD 中，分离太阳轮的弹簧预载将两组摩擦片压在一起。当轴经历牵引力差异时，行星小齿轮向高牵引力轴的方向施加额外的力。如果额外压力超过接合阈值，离合器组件接合。接合允许传动轴向旋转较慢的高牵引力车轮传递更多动力。额外的动力减小了两个轴的速度差。由于高牵引力车轮继续旋转，车辆继续移动。

该图显示了 LSD 机构中主要组件的方向。传动轴小齿轮在此表示中不可见。

Limited-Slip Differential 模块基于 Simscape™ Driveline™ 的 Differential 和 Disc Friction Clutch 模块，将 LSD 机构建模为结构组件。Differential 模块建模的差速器机构是一个结构组件，基于另外两个 Simscape Driveline 模块：Simple Gear 和 Sun-Planet Bevel。框图显示了 LSD 的结构组件。

Limited-Slip Differential 模块的端口与传动轴（端口 **D**）和两个从动轴（端口 **S1** 和 **S2**）相关联，这些端口将太阳轮连接到车轮。

Limited-Slip Differential 模块允许您仅为齿轮架和内部行星齿轮指定惯量。默认情况下，外齿轮的惯量假定可忽略不计。要对 外齿轮的惯量建模，请将 Simscape Inertia 模块连接到 **D**、**S1** 和 **S2** 端口。

下表显示了不同模块参数化和输入条件下从动轴端口的旋转方向。

| 从动轴端口（S1 和 S2）的旋转方向 | 冠齿轮相对于中心线的位置 | 传动轴端口 D 的旋转方向 | 差速器两端的相对滑移 |
| --- | --- | --- | --- |
| 正 | 右 | 正 | 0 |
| - 非打滑端口为正 - 打滑端口为负 | 右 | 正 | > 0 |
| 负 | 右 | 负 | 0 |
| - 非打滑端口为负 - 打滑端口为正 | 右 | 负 | > 0 |
| 负 | 左 | 正 | 0 |
| - 非打滑端口为负 - 打滑端口为正 | 左 | 正 | > 0 |
| 正 | 左 | 负 | 0 |
| - 非打滑端口为正 - 打滑端口为负 | 左 | 负 | > 0 |

### 模型

要查看 Limited-Slip Differential 模块结构组件的数学模型，请参阅：

- Disc Friction Clutch
- Differential
- Simple Gear
- Sun-Planet Bevel

### 热模型

您可以通过启用可选的热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
