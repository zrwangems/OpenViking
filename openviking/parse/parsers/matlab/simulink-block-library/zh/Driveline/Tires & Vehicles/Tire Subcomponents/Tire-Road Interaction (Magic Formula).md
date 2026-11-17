---
type: simulink-block
title: 'Tire-Road Interaction (Magic Formula)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles / Tire Subcomponents'
documentation_page: 'tireroadinteractionmagicformula'
documentation_source_path: 'ref/tireroadinteractionmagicformula.html'
language: zh-CN
chinese_source: worker-translation
---

# Tire-Road Interaction (Magic Formula)

## 端口

### 输入

### **N** — 法向力，N 物理信号

与作用在轮胎上的法向力关联的物理信号输入端口，单位为 N。如果法向力向下作用在轮胎上，将轮胎压向路面，则为正值。

### **M** — Magic Formula 系数，无量纲物理信号 | 向量

与 Magic Formula 系数关联的物理信号输入端口。以四元素向量形式提供 Magic Formula 系数，按 [*B*、*C*、*D*、*E*] 的顺序指定。

#### 依赖关系

要启用此端口，请将 **Parameterize by** 设置为 `Physical signal Magic Formula coefficients`。
### 输出

### **S** — 滑移物理信号

与轮胎和道路之间的相对滑移 *k* 关联的物理信号输出端口。
### 守恒

### **T** — 轮胎胎面机械旋转

与轮胎胎面关联的机械旋转端口。

### **H** — 轮毂机械旋转

与轮毂关联的机械旋转端口。

## 参数

### 主要

### **Parameterize by** — 参数化方法 `Peak longitudinal force and corresponding slip`（默认）| `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula 轮胎仿真选项。选择模块使用 Magic Formula 对轮胎进行参数化的方式：

- `Peak longitudinal force and corresponding slip` — 使用轮胎的物理特性对 Magic Formula 进行参数化。
- `Constant Magic Formula coefficients` — 将定义常数 *B*、*C*、*D* 和 *E* 系数的参数指定为标量。
- `Load-dependent Magic Formula coefficients` — 将定义载荷相关 *C*、*D*、*E*、*K*、*H* 和 *V* 系数的参数指定为向量，每个系数对应一个向量。
- `Physical signal Magic Formula coefficients` — 使用端口 **M** 以四元素向量形式按 [*B*、*C*、*D*、*E*] 的顺序指定 Magic Formula 系数。

### **Rated vertical load** — 额定载荷力 `3000` `N`（默认）| 正标量

额定垂直载荷力 *Fz0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Peak longitudinal force at rated load** — 额定载荷下的最大纵向力 `3500` `N`（默认）| 正标量

当垂直载荷等于其额定值 *Fz0* 时，轮胎施加在车轮上的最大纵向力 *Fx0*。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip`。

### **Slip at peak force at rated load (percent)** — 最大纵向力和额定载荷下的滑移百分比 `10`（默认）| 正标量

当纵向力等于其最大值 *Fx0* 且垂直载荷等于其额定值 *Fz0* 时的接触滑移 *κ'0*，以百分比（%）表示。

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

### 缩放

### **Enable scaling coefficients** — 缩放选项 `off`（默认）| `on`

是否在 Magic Formula 参数化中包含缩放系数。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients`。

### **Scale factor of Fx nominal vertical load, LFZO** — *Fx* 标称垂直载荷 `1`（默认）| 正标量

*Fx* 标称垂直载荷的缩放系数 *λFZO*。`LFZO` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx shape factor, LCX** — *Fx* 形状因子 `1`（默认）| 正标量

*Fx* 形状因子的缩放系数 *λLCX*。`LCX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx peak friction coefficient, LMUX** — *Fx* 峰值摩擦系数 `1`（默认）| 正标量

*Fx* 峰值摩擦系数的缩放系数 *λμX*。`LMUX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx curvature factor, LEX** — *Fx* 曲率因子 `1`（默认）| 正标量

*Fx* 曲率因子的缩放系数 *λEX*。`LEX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx slip stiffness, LKX** — *Fx* 滑移刚度 `1`（默认）| 正标量

*Fx* 滑移刚度的缩放系数 *λKX*。`LKX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx horizontal shift, LHX** — *Fx* 水平偏移 `1`（默认）| 正标量

*Fx* 水平偏移的缩放系数 *λhX*。`LHX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of Fx vertical shift, LVX** — *Fx* 垂直偏移 `1`（默认）| 正标量

*Fx* 垂直偏移的缩放系数 *λVX*。`LVX` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### **Scale factor of rolling resistance, LMY** — 滚动阻力 `1`（默认）| 正标量

滚动阻力的缩放系数 *λMY*。`LMY` 是 TIR 文件标识符。

#### 依赖关系

要启用此参数，请将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 并选中 **Enable scaling coefficients**。

### 高级

### **Lower boundary of slip denominator, VXLOW** — 滑移分母下边界 `1` `m/s`（默认）| 正标量

滑移分母的下边界 *VXLOW*。`VXLOW` 是 TIR 文件标识符。

### **Velocity threshold** — 数学滑移模型的轮毂速度阈值 `0.1` `m/s`（默认）| 正标量

轮毂速度 *Vth*，低于该值时模块平滑过渡到零。

### **Minimum valid wheel slip, KPUMIN** — 最小车轮滑移阈值 `-1.5`（默认）| 标量

最小有效车轮滑移。负值表示车轮沿反向旋转方向滑移。

### **Maximum valid wheel slip, KPUMAX** — 最大车轮滑移阈值 `1.5`（默认）| 标量

最大有效车轮滑移。

## 所属库

Simscape / Driveline / Tires & Vehicles / Tire Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：可视化摩擦力与胎面滑移的关系

您现在可以使用模块对话框中的 **Plot friction force versus slip** 超链接，轻松可视化纵向摩擦力与车轮滑移的关系。

### R2024b：跟踪胎面滑移导致的功率耗散

该模块现在在 `simlog` 工作区变量中记录 `power_dissipated`，表示胎面滑移导致的功率耗散。

### R2023a：Magic Formula 兼容性增强

您可以将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 以启用载荷相关 Magic Formula 系数。

以下参数对所有参数化方法都是新增的：

- **Lower boundary of slip denominator, VXLOW**
- **Minimum valid wheel slip, KPUMIN**
- **Maximum valid wheel slip, KPUMAX**

## 描述

由 Magic Formula 系数给出的轮胎-道路动力学

Tire-Road Interaction (Magic Formula) 模块表示轮胎胎面与道路路面之间的相互作用。Magic Formula 使用基于拟合系数的经验公式来预测由此相互作用产生的纵向力。该模块忽略轮胎特性，如柔量和惯量。您可以轻松可视化纵向摩擦力与车轮滑移的关系。要查看图形，请点击模块对话框 **Description** 部分中的 **Plot friction force versus slip** 超链接。

纵向力与车轮滑移关系图窗口

### 轮胎-道路相互作用模型

该模块使用 Pacejka 的 Magic Formula [2] 表示轮胎-道路接触印迹处的纵向力。

图中显示了轮胎上的力。表中定义了轮胎模型变量。

展示 F\_z、F\_x、V\_x 和旋转速度 Omega 的轮胎示意图

| 符号 | 描述 |
| --- | --- |
| *Ω* | 车轮角速度。 |
| *rw* | 车轮半径。 |
| *Vx* | 轮毂纵向速度。 |
| rwΩ | 轮胎胎面纵向速度。 |
| *u* | 轮胎纵向变形。 |
| VT=rwΩ′=rwΩ+u˙ | 轮胎胎面纵向速度。通常，轮胎胎面纵向速度包含由轮胎旋转引起的分量 *rwΩ*，以及由轮胎变形引起的可选分量 u˙。由于端口 **T** 计算 *VT*，轮胎旋转和变形的计算在模块外部进行。 |
| Vsx=Vx−VT | 接触印迹滑移速度。如果没有轮胎纵向柔量，则 u=0。 |
| k=−Vsx|Vx|smooth | 无柔量轮胎的车轮滑移。 |
| *Fz* | 轮胎上的垂直载荷。 |
| *Fz0* | 轮胎上的标称垂直载荷。 |
| Fx=f(k,Fz) | 在接触点处施加在轮胎上的纵向力。*f* 是轮胎的特性函数。 |

### 轮胎响应

您可以对轮胎滚动和滑移进行建模。

**力和特性函数**

该模块使用稳态轮胎特性函数 Fx=f(k,Fz)，其中：

- *Fx* 是轮胎上的纵向力。
- *Fz* 是垂直载荷。
- *k* 是车轮滑移

**滚动和滑移**

非滑移、无柔量轮胎的平移运动方程为 Vx=rwΩ。当轮胎发生滑移时，会产生纵向力 *Fx*。

接触印迹滑移速度为 Vsx=Vx−rwΩ−u˙。对于无柔量轮胎，*u* = 0。未平滑的接触印迹滑移为

k=−Vsx|Vx|，

模块将滑移分母饱和为

|Vx|={VXLOWif  |Vx|<VXLOW|Vx|otherwise

其中 *VXLOW* 是 **Lower boundary of slip denominator, VXLOW** 参数。模块在过渡区域 -*VXLOW* - *Vth*/2 < *Vx* < -*VXLOW* + *Vth*/2 和 *VXLOW* - *Vth*/2 < *Vx* < *VXLOW* + *Vth*/2 内将 *|Vx|* 平滑过渡到 *VXLOW*。模块根据以下公式饱和滑移

k={kpuminif −Vsx|Vx|<kpuminkpumaxif −Vsx|Vx|>kpumax−Vsx|Vx|otherwise

其中 *kpumin* 是 **Minimum valid wheel slip, KPUMIN** 参数，*kpumax* 是 **Maximum valid wheel slip, KPUMAX** 参数。模块在区域 *kpumin* - *kth*/2 < *k* < *kpumin* + *kth*/2 和 *kpumax* - *kth*/2 < *k* < *kpumax* + *kth*/2 内过渡 *k*。模块将滑移平滑阈值定义为

kth=Vth1m/s.

对于此方程，抱死滑动的车轮 *k* = -1。完美滚动时，*k* = 0。

**典型道路条件下的 Magic Formula 系数**

该模块使用基于经验轮胎数据的数值。这些值是常见道路条件下典型的常数 Magic Formula 系数集。

| 表面 | B | C | D | E |
| --- | --- | --- | --- | --- |
| 干燥沥青路面 | 10 | 1.9 | 1 | 0.97 |
| 潮湿沥青路面 | 12 | 2.3 | 0.82 | 1 |
| 雪地 | 5 | 2 | 0.3 | 1 |
| 冰面 | 4 | 2 | 0.1 | 1 |

### 参数化

**峰值纵向力和相应滑移**

当您将 **Parameterize by** 设置为 `Peak
longitudinal force and corresponding slip` 时，该模块使用一组具有代表性的魔术公式系数。该模块对这些系数进行缩放，以在额定垂直载荷 *Fz0* 下，产生您指定的相应滑移 *κ0* 处的峰值纵向力 *Fx0*。

**恒定系数魔术公式**

当您将 **Parameterize by** 设置为 `Constant Magic Formula
coefficients` 时，该模块使用无量纲系数 *B*、*C*、*D* 和 *E*，或刚度、形状、峰值和曲率，使得

Fx=f(κ,Fz)=Fz⋅D⋅sin(C⋅arctan{Bκ−E[Bκ−arctan(Bκ)]}).

*f* 在 k=0 处的斜率为 BCD⋅Fz。

**载荷相关系数魔术公式**

当您将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 时，该模块使用作为轮胎载荷函数的无量纲系数。在属性检查器中输入的更复杂参数集 `p_i` 指定了这些函数：

Fx0=Dxsin(Cxarctan{Bxκx−Ex[Bxκx−arctan(Bxκx)]})+SVx,

其中：

dfz= (Fz–Fz0)Fz0

κx=κ+SHx

Cx= p\_Cx1

Dx=μx·Fz

μx= p\_Dx1 + p\_Dx2·dfz

Ex= (p\_Ex1 + p\_Ex2·dfz+ p\_Ex3·dfz2)[1 – p\_Ex4·sgn(κx)]

Kxκ=Fz⋅(p\_Kx1 + p\_Kx2·dfz)⋅e(p\_Kx3·dfz)

Bx=KxκCxDx+εx

SHx= p\_Hx1 + p\_Hx2·dfz

SVx=Fz·(p\_Vx1 + p\_Vx2·dfz)

*SHx* 和 *SVx* 表示力-滑移函数中滑移和纵向力的偏移量，或者如果将该函数绘制为曲线，则表示水平和垂直偏移量。*μx* 是纵向载荷相关摩擦系数。*εx* 是一个小数，用于防止当 *Fz* 趋近于零时发生除零错误。

### 假设和限制

Tire-Road Interaction (Magic Formula) 模块假设仅存在纵向运动，并且不包括外倾、转向或横向运动。
