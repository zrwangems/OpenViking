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
```yaml
ports:
- name: N
  summary: 法向力，N 物理信号
  direction: input
- name: M
  summary: Magic Formula 系数，无量纲物理信号 | 向量
  direction: input
- name: S
  summary: 滑移物理信号
  direction: output
- name: A
  summary: 车轴机械旋转
  direction: output
- name: H
  summary: 轮毂机械旋转
  direction: output
```

### 输入

### **N** — 法向力，N 物理信号

与作用在轮胎上的法向力相关联的物理信号输入端口，单位为 N。当法向力向下作用在轮胎上并将其压向路面时，法向力为正。

### **M** — Magic Formula 系数，无量纲物理信号 | 向量

与 Magic Formula 系数相关联的物理信号输入端口。将 Magic Formula 系数提供为四元素向量，按 [*B*、*C*、*D*、*E*] 的顺序指定。

#### 依赖关系

要启用此端口，请将 **Parameterize by** 设置为 `Physical signal Magic Formula coefficients`。
### 输出

### **S** — 滑移物理信号

与轮胎和道路之间的相对滑移 *k* 相关联的物理信号输出端口。
### 守恒

### **A** — 车轴机械旋转

与轮胎所在车轴相关联的机械旋转端口。

### **H** — 轮毂机械旋转

与轮毂相关联的机械旋转端口。
## 参数
```yaml
parameters:
- name: Parameterize by
  summary: 参数化方法 Peak longitudinal force and corresponding slip（默认）| Constant Magic Formula coefficients | Load-dependent
    Magic Formula coefficients | Physical signal Magic Formula coefficients
  group: 主要
- name: Rated vertical load
  summary: 额定载荷力 3000 N（默认）| 正标量
  group: 主要
- name: Peak longitudinal force at rated load
  summary: 额定载荷下的最大纵向力 3500 N（默认）| 正标量
  group: 主要
- name: Slip at peak force at rated load (percent)
  summary: 最大纵向力和额定载荷下的滑移百分比 10（默认）| 正标量
  group: 主要
- name: Magic Formula B coefficient
  summary: 常数 Magic Formula *B* 系数 10（默认）| 正标量
  group: 主要
- name: Magic Formula C coefficient
  summary: 常数 Magic Formula *C* 系数 1.9（默认）| 正标量
  group: 主要
- name: Magic Formula D coefficient
  summary: 常数 Magic Formula *D* 系数 1（默认）| 正标量
  group: 主要
- name: Magic Formula E coefficient
  summary: 常数 Magic Formula *E* 系数 0.97（默认）| 正标量
  group: 主要
- name: Tire nominal vertical load, FNOMIN
  summary: 法向力 4000 N（默认）| 正标量
  group: 主要
- name: Magic Formula C-coefficient parameter, p_Cx1
  summary: 可变 Magic Formula *C* 系数 1.685（默认）| 标量
  group: 主要
- name: Magic Formula D-coefficient parameters, [p_Dx1 p_Dx2]
  summary: 可变 Magic Formula *D* 系数 [1.21, -.037]（默认）| 向量
  group: 主要
- name: Magic Formula E-coefficient parameters, [p_Ex1 p_Ex2 p_Ex3 p_Ex4]
  summary: 可变 Magic Formula *E* 系数 [.344, .095, -.02, 0]（默认）| 向量
  group: 主要
- name: Magic Formula BCD-coefficient parameters, [p_Kx1 p_Kx2 p_Kx3]
  summary: 可变 Magic Formula *K* 系数 [21.51, -.163, .245]（默认）| 向量
  group: 主要
- name: Magic Formula H-coefficient parameters, [p_Hx1 p_Hx2]
  summary: 可变 Magic Formula *H* 系数 [-.002, .002]（默认）| 向量
  group: 主要
- name: Magic Formula V-coefficient parameters, [p_Vx1 p_Vx2]
  summary: 可变 Magic Formula *V* 系数 [0, 0]（默认）| 向量
  group: 主要
- name: Effective rolling radius model
  summary: 滚动半径模型选项 Constant radius（默认）| Load and velocity dependent (Magic Formula)
  group: 几何
- name: Rolling radius
  summary: 承载轮胎半径 0.3 m（默认）| 正标量
  group: 几何
- name: Non-rolling free tire radius, R0
  summary: 非滚动自由轮胎半径 0.3 m（默认）| 正标量
  group: 几何
- name: Low load stiffness effective rolling radius, BREFF
  summary: '*Breff* 变量 8.39（默认）| 正标量'
  group: 几何
- name: Peak value of effective rolling radius, DREFF
  summary: '*Dreff* 变量 0.26（默认）| 正标量'
  group: 几何
- name: High load stiffness effective rolling radius, FREFF
  summary: '*Freff* 变量 0.074（默认）| 正标量'
  group: 几何
- name: Ratio of nominal tire radius with non-rolling free tire radius, Q_RE0
  summary: '*qre0* 变量 0.99（默认）| 正标量'
  group: 几何
- name: Tire radius increase with speed, Q_V1
  summary: '*qv1* 变量 0.008（默认）| 正标量'
  group: 几何
- name: Nominal hub longitudinal speed, LONGVL
  summary: 标称轮毂纵向速度 17 m/s（默认）| 正标量
  group: 几何
- name: Vertical stiffness
  summary: 垂直刚度 5e5 N/m（默认）| 正标量
  group: 几何
- name: Model rolling resistance
  summary: 滚动阻力选项 off（默认）| on
  group: 滚动阻力
- name: Resistance model
  summary: 滚动阻力选项 Constant coefficient（默认）| Pressure and velocity dependent SAE J2452 | Pressure and velocity dependent (Magic
    Formula)
  group: 滚动阻力
- name: Constant coefficient
  summary: 比例常数 0.015（默认）| 正标量
  group: 滚动阻力
- name: Tire pressure
  summary: 轮胎压力 250e3 Pa（默认）| 正标量
  group: 滚动阻力
- name: Alpha
  summary: 轮胎压力方程指数 -0.003（默认）| 标量
  group: 滚动阻力
- name: Beta
  summary: 法向力方程指数 0.97（默认）| 标量
  group: 滚动阻力
- name: Coefficient A
  summary: 速度无关力分量 *A* 84e-4（默认）
  group: 滚动阻力
- name: Coefficient B
  summary: 速度相关力分量 *B* 6.2e-4 s/m（默认）| 正标量
  group: 滚动阻力
- name: Coefficient C
  summary: 速度相关力分量 *C* 1.6e-4 s^2/m^2（默认）| 正标量
  group: 滚动阻力
- name: Tire nominal pressure, NOMPRES
  summary: 标称轮胎压力 240e3 Pa（默认）| 正标量
  group: 滚动阻力
- name: Tire nominal vertical load, FNOMIN
  summary: 法向力 4000 N（默认）| 正标量
  group: 滚动阻力
- name: Nominal hub longitudinal speed, LONGVL
  summary: 标称轮毂纵向速度 16 m/s（默认）| 正标量
  group: 滚动阻力
- name: Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]
  summary: Magic Formula Q 系数 [.0082, 0, .0014, .001, 0, 0, 1.08, -.5] 1（默认）| 长度为 8 的向量
  group: 滚动阻力
- name: Velocity threshold for rolling resistance
  summary: 滚动阻力阈值 0.001 m/s（默认）| 正标量
  group: 滚动阻力
- name: Enable scaling coefficients
  summary: 缩放选项 off（默认）| on
  group: 缩放
- name: Scale factor of Fx nominal vertical load, LFZO
  summary: '*Fx* 标称垂直载荷 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx shape factor, LCX
  summary: '*Fx* 形状因子比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx peak friction coefficient, LMUX
  summary: '*Fx* 峰值摩擦系数比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx curvature factor, LEX
  summary: '*Fx* 曲率因子比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx slip stiffness, LKX
  summary: '*Fx* 滑移刚度比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx horizontal shift, LHX
  summary: '*Fx* 水平偏移比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of Fx vertical shift, LVX
  summary: '*Fx* 垂直偏移比例因子 1（默认）| 正标量'
  group: 缩放
- name: Scale factor of rolling resistance, LMY
  summary: 滚动阻力比例因子 1（默认）| 正标量
  group: 缩放
- name: Compliance
  summary: 动态柔顺性选项 No compliance - Suitable for HIL simulation（默认）| Specify stiffness and damping
  group: 动力学
- name: Longitudinal stiffness
  summary: 纵向刚度 1e6 N/m（默认）| 正标量
  group: 动力学
- name: Longitudinal damping
  summary: 纵向阻尼 1000 N/(m/s)（默认）| 正标量
  group: 动力学
- name: Inertia
  summary: 惯性模型 No inertia（默认）| Specify inertia and initial velocity
  group: 动力学
- name: Tire inertia
  summary: 转动惯量 1 kg*m^2（默认）| 正标量
  group: 动力学
- name: Initial velocity
  summary: 初始转动速度 0 rad/s（默认）| 标量
  group: 动力学
- name: Lower boundary of slip denominator, VXLOW
  summary: 滑移分母下边界 1 m/s（默认）| 正标量
  group: 高级
- name: Velocity threshold
  summary: 轮胎滑移状态阈值 0.1 m/s（默认）| 正标量
  group: 高级
- name: Minimum valid wheel slip, KPUMIN
  summary: 最小有效车轮滑移阈值 -1.5（默认）| 标量
  group: 高级
- name: Maximum valid wheel slip, KPUMAX
  summary: 最大有效车轮滑移阈值 1.5（默认）| 标量
  group: 高级
```

### 主要

### **Parameterize by** — 参数化方法 `Peak longitudinal force and corresponding slip`（默认）| `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula 轮胎仿真选项。选择模块使用 Magic Formula 对轮胎进行参数化的方式：

- `Peak longitudinal force and corresponding slip` — 使用轮胎的物理特性对 Magic Formula 进行参数化。
- `Constant Magic Formula coefficients` — 将定义常数 *B*、*C*、*D* 和 *E* 系数的参数指定为标量。
- `Load-dependent Magic Formula coefficients` — 将定义载荷相关 *C*、*D*、*E*、*K*、*H* 和 *V* 系数的参数指定为向量，每个系数一个向量。
- `Physical signal Magic Formula coefficients` — 使用端口 **M** 将 Magic Formula 系数指定为四元素向量，按 [*B*、*C*、*D*、*E*] 的顺序。

### **Rated vertical load** — 额定载荷力 `3000` `N`（默认）| 正标量

额定垂直载荷力 *Fz0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Peak longitudinal force at rated load** — 额定载荷下的最大纵向力 `3500` `N`（默认）| 正标量

当垂直载荷等于其额定值 *Fz0* 时，轮胎施加在车轮上的最大纵向力 *Fx0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Slip at peak force at rated load (percent)** — 最大纵向力和额定载荷下的滑移百分比 `10`（默认）| 正标量

当纵向力等于其最大值 *Fx0* 且垂直载荷等于其额定值 *Fz0* 时的接触滑移 *k0*，以百分比（%）表示。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Magic Formula B coefficient** — 常数 Magic Formula *B* 系数 `10`（默认）| 正标量

与载荷无关的 Magic Formula *B* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula C coefficient** — 常数 Magic Formula *C* 系数 `1.9`（默认）| 正标量

与载荷无关的 Magic Formula *C* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula D coefficient** — 常数 Magic Formula *D* 系数 `1`（默认）| 正标量

与载荷无关的 Magic Formula *D* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula E coefficient** — 常数 Magic Formula *E* 系数 `0.97`（默认）| 正标量

与载荷无关的 Magic Formula *E* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Constant Magic Formula coefficients`。

### **Tire nominal vertical load, FNOMIN** — 法向力 `4000` `N`（默认）| 正标量

轮胎上的标称法向力 *Fz0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula C-coefficient parameter, p\_Cx1** — 可变 Magic Formula *C* 系数 `1.685`（默认）| 标量

载荷相关 Magic Formula *C* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula D-coefficient parameters, [p\_Dx1 p\_Dx2]** — 可变 Magic Formula *D* 系数 `[1.21, -.037]`（默认）| 向量

载荷相关 Magic Formula *D* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula E-coefficient parameters, [p\_Ex1 p\_Ex2 p\_Ex3 p\_Ex4]** — 可变 Magic Formula *E* 系数 `[.344, .095, -.02, 0]`（默认）| 向量

载荷相关 Magic Formula *E* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula BCD-coefficient parameters, [p\_Kx1 p\_Kx2 p\_Kx3]** — 可变 Magic Formula *K* 系数 `[21.51, -.163, .245]`（默认）| 向量

载荷相关 Magic Formula *K* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula H-coefficient parameters, [p\_Hx1 p\_Hx2]** — 可变 Magic Formula *H* 系数 `[-.002, .002]`（默认）| 向量

载荷相关 Magic Formula *H* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula V-coefficient parameters, [p\_Vx1 p\_Vx2]** — 可变 Magic Formula *V* 系数 `[0, 0]`（默认）| 向量

载荷相关 Magic Formula *V* 系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### 几何

### **Effective rolling radius model** — 滚动半径模型选项 `Constant radius`（默认）| `Load and velocity dependent (Magic Formula)`

是将滚动半径视为常数还是取决于载荷和速度。

#### 依赖关系

要启用此参数，请将 **Parameterize** 设置为 `Load-dependent Magic Formula coefficients`。

### **Rolling radius** — 承载轮胎半径 `0.3` `m`（默认）| 正标量

承载轮胎-车轮半径 *rw*。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 且 **Effective rolling radius model** 设置为 `Constant radius`，或
- **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`、`Constant Magic Formula coefficients` 或 `Physical signal Magic Formula coefficients`。

### **Non-rolling free tire radius, R0** — 非滚动自由轮胎半径 `0.3` `m`（默认）| 正标量

与 Magic Formula 相关联的非滚动自由轮胎半径值。`R0` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Low load stiffness effective rolling radius, BREFF** — *Breff* 变量 `8.39`（默认）| 正标量

低载荷刚度下的有效滚动半径。`BREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Peak value of effective rolling radius, DREFF** — *Dreff* 变量 `0.26`（默认）| 正标量

有效滚动半径的峰值。`DREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **High load stiffness effective rolling radius, FREFF** — *Freff* 变量 `0.074`（默认）| 正标量

高载荷刚度下的有效滚动半径。`FREFF` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Ratio of nominal tire radius with non-rolling free tire radius, Q\_RE0** — *qre0* 变量 `0.99`（默认）| 正标量

标称轮胎半径与非滚动自由轮胎半径之比。`Q_RE0` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Tire radius increase with speed, Q\_V1** — *qv1* 变量 `0.008`（默认）| 正标量

轮胎半径随速度的增加量。`Q_V1` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Nominal hub longitudinal speed, LONGVL** — 标称轮毂纵向速度 `17` `m/s`（默认）| 正标量

标称轮毂纵向速度。`LONGVL` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### **Vertical stiffness** — 垂直刚度 `5e5` `N/m`（默认）| 正标量

轮胎的垂直刚度。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，并将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`。

### 滚动阻力

### **Model rolling resistance** — 滚动阻力选项 `off`（默认）| `on`

是否在轮胎仿真中包含滚动阻力。

### **Resistance model** — 滚动阻力选项 `Constant coefficient`（默认）| `Pressure and velocity dependent SAE J2452` | `Pressure and velocity dependent (Magic Formula)`

是使用常数系数还是压力和速度相关阻力来包含阻力：

- `Constant coefficient` — 忽略滚动阻力。
- `Pressure and velocity dependent SAE J2452` — 根据 SAE J2452 对滚动阻力进行参数化。
- `Pressure and velocity dependent (Magic Formula)` — 根据 Magic Formula 对滚动阻力进行参数化。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**。

### **Constant coefficient** — 比例常数 `0.015`（默认）| 正标量

设置法向力与滚动阻力之间比例关系的系数。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Constant coefficient`。

### **Tire pressure** — 轮胎压力 `250e3` `Pa`（默认）| 正标量

轮胎的充气压力。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452` 或 `Pressure and velocity dependent (Magic Formula)`。

### **Alpha** — 轮胎压力方程指数 `-0.003`（默认）| 标量

模型方程中轮胎压力的指数。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Beta** — 法向力方程指数 `0.97`（默认）| 标量

法向力模型方程的指数。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient A** — 速度无关力分量 *A* `84e-4`（默认）

模型方程中与速度无关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient B** — 速度相关力分量 *B* `6.2e-4` `s/m`（默认）| 正标量

模型方程中与速度相关的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Coefficient C** — 速度相关力分量 *C* `1.6e-4` `s^2/m^2`（默认）| 正标量

模型方程中取决于速度项平方的力分量。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**，并将 **Rolling resistance** 设置为 `Pressure and velocity dependent SAE J2452`。

### **Tire nominal pressure, NOMPRES** — 标称轮胎压力 `240e3` `Pa`（默认）| 正标量

标称轮胎压力。`NOMPRES` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Tire nominal vertical load, FNOMIN** — 法向力 `4000` `N`（默认）| 正标量

轮胎上的标称法向力 *Fz0*。`FNOMIN` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Nominal hub longitudinal speed, LONGVL** — 标称轮毂纵向速度 `16` `m/s`（默认）| 正标量

标称轮毂纵向速度。`LONGVL` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** — Magic Formula Q 系数 `[.0082, 0, .0014, .001, 0, 0, 1.08, -.5]` `1`（默认）| 长度为 8 的向量

Magic Formula Q 系数。`qsy1`、…、`qsy8` 对应于 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Velocity threshold for rolling resistance** — 滚动阻力阈值 `0.001` `m/s`（默认）| 正标量

将全部滚动阻力传递到滚动轮毂的速度。该参数确保在速度方向变化期间力保持连续，从而提高仿真的数值稳定性。该参数必须大于零。

#### 依赖关系

要启用此参数，请选中 **Model rolling resistance**。

### 缩放

### **Enable scaling coefficients** — 缩放选项 `off`（默认）| `on`

是否在 Magic Formula 参数化中包含缩放系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`，或将 **Resistance model** 设置为 `Pressure and velocity dependent (Magic Formula)`。

### **Scale factor of Fx nominal vertical load, LFZO** — *Fx* 标称垂直载荷 `1`（默认）| 正标量

*Fx* 标称垂直载荷的缩放系数 *λFZO*。`LFZO` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx shape factor, LCX** — *Fx* 形状因子比例因子 `1`（默认）| 正标量

*Fx* 形状因子的比例因子，*λLCX*。
`LCX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx peak friction coefficient, LMUX** — *Fx* 峰值摩擦系数比例因子 `1`（默认）| 正标量

*Fx* 峰值摩擦系数的比例因子，*λμX*。
`LMUX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx curvature factor, LEX** — *Fx* 曲率因子比例因子 `1`（默认）| 正标量

*Fx* 曲率因子的比例因子，*λEX*。
`LEX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx slip stiffness, LKX** — *Fx* 滑移刚度比例因子 `1`（默认）| 正标量

*Fx* 滑移刚度的比例因子，*λKX*。
`LKX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx horizontal shift, LHX** — *Fx* 水平偏移比例因子 `1`（默认）| 正标量

*Fx* 水平偏移的比例因子，*λhX*。
`LHX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of Fx vertical shift, LVX** — *Fx* 垂直偏移比例因子 `1`（默认）| 正标量

*Fx* 垂直偏移的比例因子，*λVX*。
`LVX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为
`Load-dependent Magic Formula
coefficients`，并选中 **Enable scaling
coefficients**。

### **Scale factor of rolling resistance, LMY** — 滚动阻力比例因子 `1`（默认）| 正标量

滚动阻力的比例因子，*λMY*。
`LMY` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将

- **Parameterize by** 设置为
  `Load and velocity dependent (Magic
  Formula)`，或
- **Resistance model** 设置为
  `Pressure and velocity dependent (Magic
  Formula)`

并选中 **Enable scaling
coefficients**。

### 动力学

### **Compliance** — 动态柔顺性选项 `No compliance - Suitable for HIL simulation`（默认）| `Specify stiffness and damping`

是否包含轮胎的动态柔顺性：

- `No compliance - Suitable for HIL
  simulation` — 模块忽略动态柔顺性。
- `Specify stiffness and damping` — 模块将轮胎视为负载下的弹簧-阻尼系统。

### **Longitudinal stiffness** — 纵向刚度 `1e6` `N/m`（默认）| 正标量

轮胎纵向刚度
*CFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify
stiffness and damping`。

### **Longitudinal damping** — 纵向阻尼 `1000` `N/(m/s)`（默认）| 正标量

轮胎纵向阻尼
*bFx*。

#### 依赖关系

要启用此参数，请将 **Compliance** 设置为 `Specify
stiffness and damping`。

### **Inertia** — 惯性模型 `No inertia`（默认）| `Specify inertia and initial velocity`

轮胎转动惯量的模型。

- `No inertia` — 模块忽略动态柔顺性。
- `Specify inertia and initial
  velocity` — 模块将轮胎视为刚性、阻尼弹簧，并在负载下变形。

### **Tire inertia** — 转动惯量 `1` `kg*m^2`（默认）| 正标量

车轮-轮胎组件的转动惯量 *Iw*。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify
inertia and initial velocity`。

### **Initial velocity** — 初始转动速度 `0` `rad/s`（默认）| 标量

轮胎的初始角速度 *Ω*(0)。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify
inertia and initial velocity`。

### 高级

### **Lower boundary of slip denominator, VXLOW** — 滑移分母下边界 `1` `m/s`（默认）| 正标量

滑移分母的下边界，*VXLOW*。
`VXLOW` 是 TIR 文件标识符。

### **Velocity threshold** — 轮胎滑移状态阈值 `0.1` `m/s`（默认）| 正标量

模块用于在滑移状态之间过渡的阈值速度，*Vth*。要了解更多信息，请参阅 Roll and Slip。

### **Minimum valid wheel slip, KPUMIN** — 最小有效车轮滑移阈值 `-1.5`（默认）| 标量

最小有效车轮滑移。
负值表示反向旋转方向的车轮滑移。

### **Maximum valid wheel slip, KPUMAX** — 最大有效车轮滑移阈值 `1.5`（默认）| 标量

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

您现在可以使用模块对话框中的 **Plot friction force versus slip** 超链接，轻松可视化纵向摩擦力与车轮滑移的关系。

### R2024b：跟踪胎面滑移导致的功率耗散

模块现在在 `simlog` 工作区变量中记录 `power_dissipated`，表示胎面滑移导致的功率耗散。

### R2023a：Magic Formula 兼容性增强

模块包含更广泛的 Magic Formula 参数集。您现在可以通过以下参数设置，使用载荷相关的 Magic Formula 系数来参数化模块或有效滚动半径：

- **Parameterize by** 设置为 `Load-dependent
  Magic Formula coefficients`
- **Effective rolling radius model** 设置为
  `Load and velocity dependent (Magic
  Formula)`

您还可以在选中 **Enable scaling coefficients** 时对比例系数进行建模。

以下参数对所有参数化方式都是新增的：

- **Lower boundary of slip denominator, VXLOW**
- **Minimum valid wheel slip, KPUMIN**
- **Maximum valid wheel slip, KPUMAX**

## 描述

由 Magic Formula 系数定义的轮胎

Tire (Magic Formula) 模块表示一个纵向行为由 Magic Formula [1] 给出的轮胎，该公式是基于四个拟合系数的经验方程。您可以在恒定或可变路面条件下对轮胎动力学进行建模。您可以轻松可视化纵向摩擦力与车轮滑移的关系。要查看图形，请单击模块对话框 **Description** 部分中的 **Plot friction force versus slip** 超链接。

纵向力与车轮滑移关系图窗口

轮胎的纵向方向与其在路面上滚动时的运动方向相同。此模块是基于 Tire-Road Interaction (Magic Formula) 模块的结构组件。

为提高轮胎模型的保真度，您可以指定柔顺性、惯性、滚动阻力和可变有效滚动半径等属性。但是，这些属性会增加轮胎模型的复杂性，并可能减慢仿真速度。如果实时仿真模型或准备进行硬件在环（HIL）仿真，请考虑忽略轮胎柔顺性和惯性。

### 轮胎模型

模块将轮胎视为与路面接触并受滑移影响的刚性车轮-轮胎组合。当扭矩驱动轮轴时，轮胎将纵向力 *Fx* 传递给路面。轮胎将产生的反作用力作为力传回车轮。此作用使车轮旋转以产生纵向运动。如果您对轮胎柔顺性进行建模，轮胎还会在负载下柔性变形。如果您将 **Effective rolling radius model** 设置为 `Load and velocity dependent (Magic Formula)`，轮胎半径还会根据负载和转动速度而变化。

该图显示了作用在轮胎上的力。该表定义了轮胎模型变量。

展示 F\_z、F\_x、V\_x 和转动速度 Omega 的轮胎示意图

**轮胎模型变量**

| 符号 | 描述 |
| --- | --- |
| *rw* | 轮胎滚动半径。 |
| *Vx* | 轮毂纵向速度。 |
| *u* | 轮胎纵向变形。 |
| *Ω* | 车轮角速度。 |
| Ω′=Ω+u˙rW | 接触点角速度。如果没有轮胎纵向变形，则 u=0。 |
| VT=rwΩ′=rwΩ+u˙ | 轮胎胎面纵向速度。通常，轮胎胎面纵向速度包含由轮胎旋转引起的分量 *rwΩ*，以及由轮胎变形引起的可选分量 u˙。 |
| Vsx=Vx−VT | 接触印迹滑移速度。如果没有轮胎纵向柔顺性，则 u=0。 |
| k=−Vsx|Vx|smooth | 无柔顺性轮胎的车轮滑移。 |
| *Vth* | 轮毂阈值速度。 |
| *VXLOW* | 滑移分母下边界。 |
| *Fz* | 轮胎上的垂直载荷。 |
| *Fx* | 在接触点施加在轮胎上的纵向力。 |
| CFx=(∂Fx∂u)0 | 变形下的轮胎纵向刚度。 |
| bFx=(∂Fx∂u˙)0 | 变形下的轮胎纵向阻尼。 |
| *Iw* | 车轮-轮胎惯量，使得有效质量等于 Iwrw2 |
| *τdrive* | 车轴施加到车轮的扭矩。 |

### 轮胎运动学与响应

您可以对滚动、滑移和变形进行建模。

**滚动与滑移**

无滑移、无柔顺性轮胎的平移运动方程为 Vx=rwΩ。当轮胎经历滑移时，它们会产生纵向力 *Fx*。

接触印迹滑移速度为 Vsx=Vx−rwΩ−u˙。对于无柔顺性的轮胎，*u* = 0。未平滑的接触印迹滑移为

k=−Vsx|Vx|，

模块将滑移分母饱和为

|Vx|={VXLOWif  |Vx|<VXLOW|Vx|otherwise

其中 *VXLOW* 是 **Lower boundary of slip denominator, VXLOW** 参数。模块在过渡区域 -*VXLOW* - *Vth*/2 < *Vx* < -*VXLOW* + *Vth*/2 和 *VXLOW* - *Vth*/2 < *Vx* < *VXLOW* + *Vth*/2 上将 *|Vx|* 平滑过渡到 *VXLOW*。模块根据以下公式饱和滑移

k={kpuminif −Vsx|Vx|<kpuminkpumaxif −Vsx|Vx|>kpumax−Vsx|Vx|otherwise

其中 *kpumin* 是 **Minimum valid wheel slip, KPUMIN** 参数，*kpumax* 是 **Maximum valid wheel slip, KPUMAX** 参数。模块在区域 *kpumin* - *kth*/2 < *k* < *kpumin* + *kth*/2 和 *kpumax* - *kth*/2 < *k* < *kpumax* + *kth*/2 上过渡 *k*。模块将滑移平滑阈值定义为

kth=Vth1m/s。

对于此方程，抱死滑动的车轮 *k* = -1。对于完美滚动，*k* = 0。

**变形**

当您将 **Compliance** 设置为 `Specify stiffness and damping` 时，模块将轮胎视为柔性体。当轮胎变形时，轮胎-路面接触点以与车轮速度 *Ω* 略有不同的角速度 *Ω′* 转动，从而产生接触印迹滑移。模块将变形轮胎定义为刚度为 *CFx*、阻尼为 *bFx* 的平移弹簧-阻尼器。

当您将 **Compliance** 设置为 `No compliance - Suitable for HIL simulation` 时，u=0，并且在仿真中的任何时刻都没有轮胎纵向变形，因此 Ω′=Ω。

### 轮胎与车轮动力学

模块等效于此组件图。模块模拟瞬态和稳态行为，并表示启动和停止。Translational Spring 和 Translational Damper 模块分别等效于轮胎刚度 *CFx* 和阻尼 *bFx*。Tire-Road Interaction (Magic Formula) 模块使用 Magic Formula 表示轮胎上的纵向力 *Fx* 作为 *Fz* 和 *k* 的函数，其中 *k* 是独立滑移变量，*Fz* 是端口 **N** 处的输入信号。

组件图直观地显示了 Tire (Magic Formula) 模块的等效 Simscape 系统

标记为 `Rolling Radius` 的模块是轮胎滚动半径 *rw*。惯性值是有效惯量 Iwrw2。轮胎特性函数 *f*(*k′*, *Fz*) 确定纵向力 *Fx*。与施加到车轮轴上的驱动轴扭矩一起，*Fx* 确定车轮角运动和纵向运动。

当您不对轮胎柔顺性进行建模时，模块在图中省略 `Longitudinal Stiffness` 和 `Longitudinal Damper` 模块，接触变量恢复为车轮变量。在这种情况下，轮胎实际上具有无限刚度，Rolling Radius 的端口 **P** 直接连接到 Ideal Force Sensor 模块的端口 **C**。

当您将 **Rolling Resistance** 设置为 `Pressure and velocity dependent (Magic Formula)` 以外的设置时，模块省略 Ideal Force Sensor 模块和 Rolling Resistance 模块的连接 **T**。当您将 **Compliance** 设置为 `No compliance - Suitable for HIL simulation` 时，**Rolling Radius** 的端口 **P** 直接连接到 Ideal force sensor 端口 **C** 或 Tire-Road Interaction (Magic Formula) 模块的端口 **T**。

### 有效滚动半径

模块确定有效滚动半径，以考虑离心增长和由于加载导致的减小，使得

rw=RΩ−Fz0cz(Dreffarctan(BreffFzFz0)+FreffFzFz0)RΩ=R0(qre0+qv1(ΩR0V0)2)

其中：

- *rw* 是有效滚动半径。
- *RΩ* 是自由轮胎半径的离心增长。
- *Fz* 是轮胎上的垂直载荷。
- *Fz0* 是 **Tire nominal vertical load, FNOMIN** 参数。
- *cz* 是 **Vertical stiffness** 参数。
- *Ω* 是车轮转动速度。

量 *Fz* 和 *Ω* 随时间变化。

这些量对应于 TIR 文件值和模块参数：

| 变量 | TIR 文件标识符 | 参数名称 |
| --- | --- | --- |
| *Breff* | `BREFF` | **Low load stiffness effective rolling radius, BREFF** |
| *Dreff* | `DREFF` | **Peak value of effective rolling radius, DREFF** |
| *Freff* | `FREFF` | **High load stiffness effective rolling radius, FREFF** |
| *qre0* | `Q_RE0` | **Ratio of nominal tire radius with non-rolling free tire radius, Q\_RE0** |
| *qv1* | `Q_V1` | **Tire radius increase with speed, Q\_V1** |

**注意**

如果您的 TIR 文件未提供 `Q_RE0` 和 `Q_V1`，请将这些值分别设置为 1 和 0。`sdlUtility.tirread` 函数会自动处理此情况。

### 假设与限制

- 模块仅假设纵向运动，不包括外倾、转向或横向运动。
- 轮胎柔顺性意味着轮胎对作用力的响应存在时间滞后。时间滞后仿真提高了模型保真度，但降低了仿真性能。请参阅 Adjust Model Fidelity。
