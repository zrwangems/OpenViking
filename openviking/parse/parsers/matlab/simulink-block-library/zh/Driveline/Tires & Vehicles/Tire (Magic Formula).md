---
type: simulink-block
title: 'Tire (Magic Formula)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'tiremagicformula'
documentation_source_path: 'ref/tiremagicformula.html'
language: zh-CN
chinese_source: worker-translation
---

# Tire (Magic Formula)

## 端口

### 输入

### **N** — 法向力，N 物理信号

与作用在轮胎上的法向力关联的物理信号输入端口，单位为 N。如果法向力向下作用在轮胎上，将其压向路面，则为正。

### **M** — Magic Formula 系数，无单位物理信号 | 向量

与 Magic Formula 系数关联的物理信号输入端口。以四元素向量形式提供 Magic Formula 系数，顺序为 [*B*, *C*, *D*, *E*]。

#### 依赖关系

要启用此端口，请将 **Parameterize by** 设置为 `Physical signal Magic Formula coefficients`。

### 输出

### **S** — 滑移物理信号

与轮胎和道路之间的相对滑移 *k* 关联的物理信号输出端口。

### 守恒

### **A** — 车轴机械旋转

与轮胎所在车轴关联的机械旋转端口。

### **H** — 轮毂机械旋转

与轮毂关联的机械旋转端口。

## 参数

### 主要

### **Parameterize by** — 参数化方法 `Peak longitudinal force and corresponding slip` (default) | `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula 轮胎仿真选项。选择模块如何使用 Magic Formula 对轮胎进行参数化：

- `Peak longitudinal force and corresponding slip` — 使用轮胎的物理特性对 Magic Formula 进行参数化。
- `Constant Magic Formula coefficients` — 将定义常数 *B*、*C*、*D* 和 *E* 系数的参数指定为标量。
- `Load-dependent Magic Formula coefficients` — 将定义载荷相关 *C*、*D*、*E*、*K*、*H* 和 *V* 系数的参数指定为向量，每个系数一个向量。
- `Physical signal Magic Formula coefficients` — 使用端口 **M** 将 Magic Formula 系数指定为四元素向量，顺序为 [*B*, *C*, *D*, *E*]。

### **Rated vertical load** — 额定载荷力 `3000` `N` (default) | 正标量

额定垂直载荷力 *Fz0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Peak longitudinal force at rated load** — 额定载荷下的最大纵向力 `3500` `N` (default) | 正标量

当垂直载荷等于其额定值 *Fz0* 时，轮胎施加在车轮上的最大纵向力 *Fx0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Slip at peak force at rated load (percent)** — 额定载荷下峰值力处的滑移（百分比） `10` (default) | 正标量

当纵向力等于其最大值 *Fx0* 且垂直载荷等于其额定值 *Fz0* 时，以百分比 (%) 表示的接触滑移 *k0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Magic Formula B coefficient** — 常数 Magic Formula *B* 系数 `10` (default) | 正标量

与载荷无关的 Magic Formula *B* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula C coefficient** — 常数 Magic Formula *C* 系数 `1.9` (default) | 正标量

与载荷无关的 Magic Formula *C* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula D coefficient** — 常数 Magic Formula *D* 系数 `1` (default) | 正标量

与载荷无关的 Magic Formula *D* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula E coefficient** — 常数 Magic Formula *E* 系数 `0.97` (default) | 正标量

与载荷无关的 Magic Formula *E* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Tire nominal vertical load, FNOMIN** — 法向力 `4000` `N` (default) | 正标量

轮胎上的额定法向力 *Fz0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula C-coefficient parameter, p\_Cx1** — 可变 Magic Formula *C* 系数 `1.685` (default) | 标量

载荷相关的 Magic Formula *C* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula D-coefficient parameters, [p\_Dx1 p\_Dx2]** — 可变 Magic Formula *D* 系数 `[1.21, -.037]` (default) | 向量

载荷相关的 Magic Formula *D* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula E-coefficient parameters, [p\_Ex1 p\_Ex2 p\_Ex3 p\_Ex4]** — 可变 Magic Formula *E* 系数 `[.344, .095, -.02, 0]` (default) | 向量

载荷相关的 Magic Formula *E* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula BCD-coefficient parameters, [p\_Kx1 p\_Kx2 p\_Kx3]** — 可变 Magic Formula *K* 系数 `[21.51, -.163, .245]` (default) | 向量

载荷相关的 Magic Formula *K* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula H-coefficient parameters, [p\_Hx1 p\_Hx2]** — 可变 Magic Formula *H* 系数 `[-.002, .002]` (default) | 向量

载荷相关的 Magic Formula *H* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula V-coefficient parameters, [p\_Vx1 p\_Vx2]** — 可变 Magic Formula *V* 系数 `[0, 0]` (default) | 向量

载荷相关的 Magic Formula *V* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### 几何

### **Effective rolling radius model** — 滚动半径模型选项 `Constant radius` (default) | `Load and velocity dependent (Magic Formula)`

是将滚动半径视为常数还是取决于载荷和速度。

#### 依赖关系

要启用此参数，请将 **Parameterize** 设置为 `Load-dependent Magic Formula coefficients`。

### **Rolling radius** — 承载轮胎半径 `0.3` `m` (default) | 正标量

承载的轮胎-车轮半径 *rw*。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Constant radius`，
  或
- 将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`、`Constant Magic Formula coefficients` 或 `Physical signal Magic Formula coefficients`。

### **Non-rolling free tire radius, R0** — 非滚动自由轮胎半径 `0.3` `m` (default) | 正标量

与 Magic Formula 关联的非滚动自由轮胎半径值。`R0` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Low load stiffness effective rolling radius, BREFF** — *Breff* 变量 `8.39` (default) | 正标量

低载荷刚度下的有效滚动半径。`BREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Peak value of effective rolling radius, DREFF** — *Dreff* 变量 `0.26` (default) | 正标量

有效滚动半径的峰值。`DREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **High load stiffness effective rolling radius, FREFF** — *Freff* 变量 `0.074` (default) | 正标量

高载荷刚度下的有效滚动半径。`FREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Ratio of nominal tire radius with non-rolling free tire radius, Q\_RE0** — *qre0* 变量 `0.99` (default) | 正标量

额定轮胎半径与非滚动自由轮胎半径之比。`Q_RE0` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Tire radius increase with speed, Q\_V1** — *qv1* 变量 `0.008` (default) | 正标量

轮胎半径随速度的增加量。`Q_V1` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Nominal hub longitudinal speed, LONGVL** — 额定轮毂纵向速度 `17` `m/s` (default) | 正标量

额定轮毂纵向速度。`LONGVL` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Vertical stiffness** — 垂直刚度 `5e5` `N/m` (default) | 正标量

轮胎的垂直刚度。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### 滚动阻力

### **Model rolling resistance** — 滚动阻力选项 `off` (default) | `on`

是否在轮胎仿真中包含滚动阻力。

### **Resistance model** — 滚动阻力选项 `Constant coefficient` (default) | `Pressure and velocity dependent SAE J2452` | `Pressure and velocity dependent (Magic Formula)`

是否使用常数系数或压力和速度相关的阻力来包含阻力：

- `Constant coefficient` — 忽略滚动阻力。
- `Pressure and velocity dependent SAE J2452` — 根据 SAE J2452 对滚动阻力进行参数化。
- `Pressure and velocity dependent (Magic Formula)` — 根据 Magic Formula 对滚动阻力进行参数化。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**。

### **Constant coefficient** — 比例常数 `0.015` (default) | 正标量

设置法向力与滚动阻力之间比例关系的系数。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Constant coefficient`。

### **Tire pressure** — 轮胎压力 `250e3` `Pa` (default) | 正标量

轮胎的充气压力。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452` 或 `Pressure and velocity dependent (Magic Formula)`。

### **Alpha** — 轮胎压力方程指数 `-0.003` (default) | 标量

模型方程中轮胎压力的指数。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Beta** — 法向力方程指数 `0.97` (default) | 标量

法向力模型方程的指数。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient A** — 速度无关的力分量 *A* `84e-4` (default)

模型方程中与速度无关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient B** — 速度相关的力分量 *B* `6.2e-4` `s/m` (default) | 正标量

模型方程中与速度相关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient C** — 速度相关的力分量 *C* `1.6e-4` `s^2/m^2` (default) | 正标量

模型方程中取决于速度项平方的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Tire nominal pressure, NOMPRES** — 额定轮胎压力 `240e3` `Pa` (default) | 正标量

额定轮胎压力。`NOMPRES` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Tire nominal vertical load, FNOMIN** — 法向力 `4000` `N` (default) | 正标量

轮胎上的额定法向力 *Fz0*。`FNOMIN` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Nominal hub longitudinal speed, LONGVL** — 额定轮毂纵向速度 `16` `m/s` (default) | 正标量

额定轮毂纵向速度。`LONGVL` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** — Magic Formula Q 系数 `[.0082, 0, .0014, .001, 0, 0, 1.08, -.5]` `1` (default) | 长度为 8 的向量

Magic Formula Q 系数。`qsy1`，…，`qsy8` 对应于 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Velocity threshold for rolling resistance** — 滚动阻力阈值 `0.001` `m/s` (default) | 正标量

完整滚动阻力传递到滚动轮毂时的速度。该参数确保在速度方向变化期间力保持连续，从而提高仿真的数值稳定性。该参数必须大于零。

#### 依赖关系

要启用此参数，请选择 **Model rolling resistance**。

### 缩放

### **Enable scaling coefficients** — 缩放选项 `off` (default) | `on`

是否在 Magic Formula 参数化中包含缩放系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，或将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Scale factor of Fx nominal vertical load, LFZO** — *Fx* 额定垂直载荷 `1` (default) | 正标量

*Fx* 额定垂直载荷的缩放因子 *λFZO*。`LFZO` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 形状因子的比例因子，LCX** — *Fx* 形状因子 `1`（默认） | 正标量

*Fx* 形状因子的比例因子，*λLCX*。
`LCX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 峰值摩擦系数的比例因子，LMUX** — *Fx* 峰值摩擦系数 `1`（默认） | 正标量

*Fx* 峰值摩擦系数的比例因子，*λμX*。
`LMUX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 曲率因子的比例因子，LEX** — *Fx* 曲率因子 `1`（默认） | 正标量

*Fx* 曲率因子的比例因子，*λEX*。
`LEX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 滑移刚度的比例因子，LKX** — *Fx* 滑移刚度 `1`（默认） | 正标量

*Fx* 滑移刚度的比例因子，*λKX*。
`LKX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 水平偏移的比例因子，LHX** — *Fx* 水平偏移 `1`（默认） | 正标量

*Fx* 水平偏移的比例因子，*λhX*。
`LHX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **Fx 垂直偏移的比例因子，LVX** — *Fx* 垂直偏移 `1`（默认） | 正标量

*Fx* 垂直偏移的比例因子，*λVX*。
`LVX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，并选择 **启用缩放系数**。

### **滚动阻力的比例因子，LMY** — 滚动阻力 `1`（默认） | 正标量

滚动阻力的比例因子，*λMY*。
`LMY` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **参数化方式** 设置为 `Load and velocity dependent (Magic Formula)`，或
- 将 **阻力模型** 设置为 `Pressure and velocity dependent (Magic Formula)`

并选择 **启用缩放系数**。

### 动力学

### **柔顺性** — 动态柔顺性选项 `No compliance - Suitable for HIL simulation`（默认） | `Specify stiffness and damping`

是否包含轮胎的动态柔顺性：

- `No compliance - Suitable for HIL simulation` — 该模块忽略动态柔顺性。
- `Specify stiffness and damping` — 该模块将轮胎视为载荷下的弹簧-阻尼器系统。

### **纵向刚度** — 纵向刚度 `1e6` `N/m`（默认） | 正标量

轮胎纵向刚度 *CFx*。

#### 依赖关系

要启用此参数，请将 **柔顺性** 设置为 `Specify stiffness and damping`。

### **纵向阻尼** — 纵向阻尼 `1000` `N/(m/s)`（默认） | 正标量

轮胎纵向阻尼 *bFx*。

#### 依赖关系

要启用此参数，请将 **柔顺性** 设置为 `Specify stiffness and damping`。

### **惯性** — 惯性模型 `No inertia`（默认） | `Specify inertia and initial velocity`

轮胎转动惯性的模型。

- `No inertia` — 该模块忽略动态柔顺性。
- `Specify inertia and initial velocity` — 该模块将轮胎视为刚性阻尼弹簧，并在载荷下变形。

### **轮胎惯性** — 转动惯性 `1` `kg*m^2`（默认） | 正标量

车轮-轮胎总成的转动惯性 *Iw*。

#### 依赖关系

要启用此参数，请将 **惯性** 设置为 `Specify inertia and initial velocity`。

### **初始速度** — 初始转速 `0` `rad/s`（默认） | 标量

轮胎的初始角速度 *Ω*(0)。

#### 依赖关系

要启用此参数，请将 **惯性** 设置为 `Specify inertia and initial velocity`。

### 高级

### **滑移分母下边界，VXLOW** — 滑移分母下边界 `1` `m/s`（默认） | 正标量

滑移分母下边界 *VXLOW*。
`VXLOW` 是 TIR 文件标识符。

### **速度阈值** — 轮胎滑移区域阈值 `0.1` `m/s`（默认） | 正标量

该模块用于在滑移区域之间过渡的阈值速度 *Vth*。要了解详细信息，请参阅滚动与滑移。

### **最小有效车轮滑移，KPUMIN** — 最小车轮滑移阈值 `-1.5`（默认） | 标量

最小有效车轮滑移。
负值表示反向旋转方向的车轮滑移。

### **最大有效车轮滑移，KPUMAX** — 最大车轮滑移阈值 `1.5`（默认） | 标量

最大有效车轮滑移。

## 所属库

Simscape / Driveline / Tires & Vehicles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：可视化摩擦力与胎面滑移的关系

现在，可以使用模块对话框中的 **绘制摩擦力与滑移的关系** 超链接，轻松可视化纵向摩擦力相对于车轮滑移的关系。

### R2024b：跟踪因胎面滑移耗散的功率

该模块现在会在 `simlog` 工作区变量中记录 `power_dissipated`，其表示因胎面滑移耗散的功率。

### R2023a：Magic Formula 兼容性增强

该模块包含更广泛的 Magic Formula 参数集。现在，可以通过以下参数设置，使用载荷相关 Magic Formula 系数来参数化模块或有效滚动半径：

- 将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`
- 将 **有效滚动半径模型** 设置为 `Load and velocity dependent (Magic Formula)`

选择 **启用缩放系数** 时，还可以对缩放系数建模。

以下参数对于所有参数化方式都是新增参数：

- **滑移分母下边界，VXLOW**
- **最小有效车轮滑移，KPUMIN**
- **最大有效车轮滑移，KPUMAX**

## 描述

由 Magic Formula 系数定义的轮胎

Tire (Magic Formula) 模块表示一个轮胎，其纵向行为由 Magic Formula [1] 给出，这是一个基于四个拟合系数的经验公式。可以对恒定或变化路面条件下的轮胎动力学建模。可以轻松可视化纵向摩擦力相对于车轮滑移的关系。要查看图形，请点击模块对话框的 **描述** 部分中的 **绘制摩擦力与滑移的关系** 超链接。

纵向力与车轮滑移关系图窗口

轮胎的纵向与其在路面上滚动时的运动方向相同。此模块是一个基于 Tire-Road Interaction (Magic Formula) 模块的结构组件。

要提高轮胎模型的保真度，可以指定柔顺性、惯性、滚动阻力和变化的有效滚动半径等属性。但是，这些属性会增加轮胎模型的复杂度，并可能减慢仿真速度。如果要对模型进行实时仿真，或准备将该模型用于硬件在环 (HIL) 仿真，请考虑忽略轮胎柔顺性和惯性。

### 轮胎模型

该模块将轮胎视为与道路接触并受到滑移作用的刚性车轮-轮胎组合。当扭矩驱动轮轴时，轮胎将纵向力 *Fx* 传递到道路。轮胎将产生的反作用力作为力传回车轮。此动作使车轮旋转，从而产生纵向运动。如果对轮胎柔顺性建模，则轮胎还会在载荷下发生柔性变形。如果将 **有效滚动半径模型** 设置为 `Load and velocity dependent (Magic Formula)`，轮胎半径还会随载荷和转速变化。

该图显示了作用在轮胎上的力。下表定义了轮胎模型变量。

展示 F\_z、F\_x、V\_x 和转速 Omega 的轮胎示意图

**轮胎模型变量**

| 符号 | 描述 |
| --- | --- |
| *rw* | 轮胎滚动半径。 |
| *Vx* | 轮毂纵向速度。 |
| *u* | 轮胎纵向变形。 |
| *Ω* | 车轮角速度。 |
| Ω′=Ω+u˙rW | 接触点角速度。如果没有轮胎纵向变形，则 u=0。 |
| VT=rwΩ′=rwΩ+u˙ | 轮胎胎面纵向速度。通常，轮胎胎面纵向速度包含由轮胎旋转产生的分量 *rwΩ*，以及可选的由轮胎变形产生的分量 u˙。 |
| Vsx=Vx−VT | 接触印迹滑移速度。如果没有轮胎纵向柔顺性，则 u=0。 |
| k=−Vsx|Vx|smooth | 无柔顺性轮胎的车轮滑移。 |
| *Vth* | 轮毂阈值速度。 |
| *VXLOW* | 滑移分母下边界。 |
| *Fz* | 轮胎上的垂直载荷。 |
| *Fx* | 在接触点施加到轮胎上的纵向力。 |
| CFx=(∂Fx∂u)0 | 变形下的轮胎纵向刚度。 |
| bFx=(∂Fx∂u˙)0 | 变形下的轮胎纵向阻尼。 |
| *Iw* | 车轮-轮胎惯性，使得有效质量等于 Iwrw2 |
| *τdrive* | 车轴施加到车轮的扭矩。 |

### 轮胎运动学与响应

可以对滚动、滑移和变形建模。

**滚动与滑移**

无滑移、无柔顺性轮胎的平移运动方程为 Vx=rwΩ。当轮胎发生滑移时，会产生纵向力 *Fx*。

接触印迹滑移速度为 Vsx=Vx−rwΩ−u˙。对于无柔顺性的轮胎，*u* = 0。未平滑的接触印迹滑移为

k=−Vsx|Vx|,

该模块按下式对滑移分母进行饱和处理

|Vx|={VXLOWif  |Vx|<VXLOW|Vx|otherwise

其中 *VXLOW* 是 **滑移分母下边界，VXLOW** 参数。该模块在过渡区域 -*VXLOW* - *Vth*/2 < *Vx* < -*VXLOW* + *Vth*/2 和 *VXLOW* - *Vth*/2 < *Vx* < *VXLOW* + *Vth*/2 内将 *|Vx|* 平滑过渡到 *VXLOW*。该模块按下式对滑移进行饱和处理

k={kpuminif −Vsx|Vx|<kpuminkpumaxif −Vsx|Vx|>kpumax−Vsx|Vx|otherwise

其中 *kpumin* 是 **最小有效车轮滑移，KPUMIN** 参数，*kpumax* 是 **最大有效车轮滑移，KPUMAX** 参数。该模块在区域 *kpumin* - *kth*/2 < *k* < *kpumin* + *kth*/2 和 *kpumax* - *kth*/2 < *k* < *kpumax* + *kth*/2 内对 *k* 进行过渡。该模块将滑移平滑阈值定义为

kth=Vth1m/s.

对于此方程，锁死滑动的车轮具有 *k* = -1。对于纯滚动，*k* = 0。

**变形**

当将 **柔顺性** 设置为 `Specify stiffness and damping` 时，该模块将轮胎视为柔性体。当轮胎变形时，轮胎-道路接触点以与车轮速度 *Ω* 略有不同的角速度 *Ω′* 转动，从而产生接触印迹滑移。该模块将变形轮胎定义为刚度为 *CFx*、阻尼为 *bFx* 的平动弹簧-阻尼器。

当将 **柔顺性** 设置为 `No compliance - Suitable for HIL simulation` 时，u=0，并且在仿真中的任何时刻都不存在轮胎纵向变形，因此 Ω′=Ω。

### 轮胎与车轮动力学

该模块等效于以下组件图。该模块对瞬态和稳态行为进行仿真，并表示起动和停止。Translational Spring 和 Translational Damper 模块分别等效于轮胎刚度 *CFx* 和阻尼 *bFx*。Tire-Road Interaction (Magic Formula) 模块使用 Magic Formula 将作用在轮胎上的纵向力 *Fx* 表示为 *Fz* 和 *k* 的函数，其中 *k* 是独立滑移变量，*Fz* 是端口 **N** 处的输入信号。

组件图直观显示了 Tire (Magic Formula) 模块的等效 Simscape 系统

标记为 `Rolling Radius` 的模块是轮胎滚动半径 *rw*。惯性值是有效惯性 Iwrw2。轮胎特性函数 *f*(*k′*, *Fz*) 确定纵向力 *Fx*。连同施加到车轮轴上的驱动轴扭矩，*Fx* 决定车轮角运动和纵向运动。

当不对轮胎柔顺性建模时，该模块会省略图中的 `Longitudinal Stiffness` 和 `Longitudinal Damper` 模块，接触变量退化为车轮变量。在这种情况下，轮胎实际上具有无限刚度，Rolling Radius 的端口 **P** 直接连接到 Ideal Force Sensor 模块的端口 **C**。

当将 **滚动阻力** 设置为 `Pressure and velocity dependent (Magic Formula)` 以外的设置时，该模块会省略 Ideal Force Sensor 模块以及 Rolling Resistance 模块的连接 **T**。当将 **柔顺性** 设置为 `No compliance - Suitable for HIL simulation` 时，**Rolling Radius** 的端口 **P** 直接连接到 Ideal Force Sensor 端口 **C**，或连接到 Tire-Road Interaction (Magic Formula) 模块的端口 **T**。

### 有效滚动半径

该模块确定有效滚动半径，以考虑离心增长和因加载导致的减小，使得

rw=RΩ−Fz0cz(Dreffarctan(BreffFzFz0)+FreffFzFz0)RΩ=R0(qre0+qv1(ΩR0V0)2)

其中：

- *rw* 是有效滚动半径。
- *RΩ* 是自由轮胎半径的离心增长。
- *Fz* 是轮胎上的垂直载荷。
- *Fz0* 是 **轮胎额定垂直载荷，FNOMIN** 参数。
- *cz* 是 **垂直刚度** 参数。
- *Ω* 是车轮转速。

量 *Fz* 和 *Ω* 随时间变化。

这些量对应 TIR 文件值和模块参数：

| 变量 | TIR 文件标识符 | 参数名 |
| --- | --- | --- |
| *Breff* | `BREFF` | **低载荷刚度有效滚动半径，BREFF** |
| *Dreff* | `DREFF` | **有效滚动半径峰值，DREFF** |
| *Freff* | `FREFF` | **高载荷刚度有效滚动半径，FREFF** |
| *qre0* | `Q_RE0` | **额定轮胎半径与非滚动自由轮胎半径之比，Q\_RE0** |
| *qv1* | `Q_V1` | **轮胎半径随速度的增加量，Q\_V1** |

**注意**

如果您的 TIR 文件未提供 `Q_RE0` 和 `Q_V1`，请将这些值分别设置为 1 和 0。`sdlUtility.tirread` 函数会自动处理此情况。

### 假设与限制

- 该模块假设仅存在纵向运动，不包括外倾、转向或侧向运动。
- 轮胎柔顺性意味着轮胎对作用力的响应存在时间滞后。时间滞后仿真会提高模型保真度，但会降低仿真性能。请参阅 Adjust Model Fidelity。
