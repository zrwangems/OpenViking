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

### **N** — 法向力, N physical signal

与作用在轮胎上的法向力（N）关联的 physical signal 输入端口。如果法向力向下作用在轮胎上，将其压向路面，则为正。

### **M** — Magic Formula 系数, unitless physical signal | vector

与 Magic Formula 系数关联的 physical signal 输入端口。以四元素 vector 形式提供 Magic Formula 系数，顺序为 [*B*, *C*, *D*, *E*]。

#### 依赖项

要启用此端口，请将 **参数化方式** 设置为 `Physical signal Magic Formula coefficients`。

### 输出

### **S** — 滑移 physical signal

与轮胎和道路之间的相对滑移 *k* 关联的 physical signal 输出端口。

### 守恒

### **T** — 轮胎胎面机械旋转

与轮胎胎面关联的机械旋转端口。

### **H** — 轮毂机械旋转

与轮毂关联的机械旋转端口。

## 参数

### 主要

### **参数化方式** — 参数化方法 `Peak longitudinal force and corresponding slip` (default) | `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula 轮胎仿真选项。选择模块使用 Magic Formula 对轮胎进行参数化的方式：

- `Peak longitudinal force and corresponding slip` — 使用轮胎的物理特性对 Magic Formula 进行参数化。
- `Constant Magic Formula coefficients` — 将定义常量 *B*、*C*、*D* 和 *E* 系数的参数指定为 scalars。
- `Load-dependent Magic Formula coefficients` — 将定义载荷相关 *C*、*D*、*E*、*K*、*H* 和 *V* 系数的参数指定为 vectors，每个系数一个。
- `Physical signal Magic Formula coefficients` — 使用端口 **M** 按 [*B*, *C*, *D*,*E*] 的顺序以四元素 vector 指定 Magic Formula 系数。

### **额定垂直载荷** — 额定载荷力 `3000` `N` (default) | positive scalar

额定垂直载荷力 *Fz0*。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Peak longitudinal force and corresponding slip`。

### **额定载荷下的峰值纵向力** — 额定载荷下的最大纵向力 `3500` `N` (default) | positive scalar

当垂直载荷等于其额定值 *Fz0* 时，轮胎施加在车轮上的最大纵向力 *Fx0*。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Peak longitudinal force and corresponding slip`。

### **额定载荷下峰值力处的滑移（百分比）** — 最大纵向力和额定载荷下的百分比滑移 `10` (default) | positive scalar

当纵向力等于其最大值 *Fx0* 且垂直载荷等于其额定值 *Fz0* 时，接触滑移 *κ'0*，以百分比 (%) 表示。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Peak longitudinal force and corresponding slip`。

### **Magic Formula B 系数** — 常量 Magic Formula *B* 系数 `10` (default) | positive scalar

与载荷无关的 Magic Formula *B* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula C 系数** — 常量 Magic Formula *C* 系数 `1.9` (default) | positive scalar

与载荷无关的 Magic Formula *C* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula D 系数** — 常量 Magic Formula *D* 系数 `1` (default) | positive scalar

与载荷无关的 Magic Formula *D* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Constant Magic Formula coefficients`。

### **Magic Formula E 系数** — 常量 Magic Formula *E* 系数 `0.97` (default) | positive scalar

与载荷无关的 Magic Formula *E* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Constant Magic Formula coefficients`。

### **轮胎标称垂直载荷, FNOMIN** — 法向力 `4000` `N` (default) | positive scalar

轮胎上的标称法向力 *Fz0*。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula C 系数参数, p\_Cx1** — 可变 Magic Formula *C* 系数 `1.685` (default) | scalar

载荷相关 Magic Formula *C* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula D 系数参数, [p\_Dx1 p\_Dx2]** — 可变 Magic Formula *D* 系数 `[1.21, -.037]` (default) | vector

载荷相关 Magic Formula *D* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula E 系数参数, [p\_Ex1 p\_Ex2 p\_Ex3 p\_Ex4]** — 可变 Magic Formula *E* 系数 `[.344, .095, -.02, 0]` (default) | vector

载荷相关 Magic Formula *E* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula BCD 系数参数, [p\_Kx1 p\_Kx2 p\_Kx3]** — 可变 Magic Formula *K* 系数 `[21.51, -.163, .245]` (default) | vector

载荷相关 Magic Formula *K* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula H 系数参数, [p\_Hx1 p\_Hx2]** — 可变 Magic Formula *H* 系数 `[-.002, .002]` (default) | vector

载荷相关 Magic Formula *H* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Magic Formula V 系数参数, [p\_Vx1 p\_Vx2]** — 可变 Magic Formula *V* 系数 `[0, 0]` (default) | vector

载荷相关 Magic Formula *V* 系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### 缩放

### **启用缩放系数** — 缩放选项 `off` (default) | `on`

是否在 Magic Formula 参数化中包含缩放系数。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`。

### **Fx 标称垂直载荷的缩放因子, LFZO** — *Fx* 标称垂直载荷 `1` (default) | positive scalar

*Fx* 标称垂直载荷的缩放因子，*λFZO*。`LFZO` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 形状因子的缩放因子, LCX** — *Fx* 形状因子 `1` (default) | positive scalar

*Fx* 形状因子的缩放因子，*λLCX*。`LCX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 峰值摩擦系数的缩放因子, LMUX** — *Fx* 峰值摩擦系数 `1` (default) | positive scalar

*Fx* 峰值摩擦系数的缩放因子，*λμX*。`LMUX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 曲率因子的缩放因子, LEX** — *Fx* 曲率因子 `1` (default) | positive scalar

*Fx* 曲率因子的缩放因子，*λEX*。`LEX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 滑移刚度的缩放因子, LKX** — *Fx* 滑移刚度 `1` (default) | positive scalar

*Fx* 滑移刚度的缩放因子，*λKX*。`LKX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 水平偏移的缩放因子, LHX** — *Fx* 水平偏移 `1` (default) | positive scalar

*Fx* 水平偏移的缩放因子，*λhX*。`LHX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **Fx 垂直偏移的缩放因子, LVX** — *Fx* 垂直偏移 `1` (default) | positive scalar

*Fx* 垂直偏移的缩放因子，*λVX*。`LVX` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### **滚动阻力的缩放因子, LMY** — 滚动阻力 `1` (default) | positive scalar

滚动阻力的缩放因子，*λMY*。`LMY` 是 TIR 文件标识符。

#### 依赖项

要启用此参数，请将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients` 并选择 **启用缩放系数**。

### 高级

### **滑移分母下边界, VXLOW** — 滑移分母下边界 `1` `m/s` (default) | positive scalar

滑移分母下边界，*VXLOW*。`VXLOW` 是 TIR 文件标识符。

### **速度阈值** — 数学滑移模型的轮毂速度阈值 `0.1` `m/s` (default) | positive scalar

轮毂速度，*Vth*，低于该值时模块将过渡平滑至零。

### **最小有效车轮滑移, KPUMIN** — 最小车轮滑移阈值 `-1.5` (default) | scalar

最小有效车轮滑移。负值表示反向旋转方向上的车轮滑移。

### **最大有效车轮滑移, KPUMAX** — 最大车轮滑移阈值 `1.5` (default) | scalar

最大有效车轮滑移。

## 所属库

Simscape / Driveline / Tires & Vehicles / Tire Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a: 可视化摩擦力与胎面滑移的关系

现在，您可以使用模块对话框中的 **绘制摩擦力与滑移的关系** 超链接，轻松可视化纵向摩擦力相对于车轮滑移的关系。

### R2024b: 跟踪因胎面滑移耗散的功率

该模块现在会在 `simlog` 工作区变量中记录 `power_dissipated`，其表示因胎面滑移而耗散的功率。

### R2023a: Magic Formula 兼容性增强

您可以将 **参数化方式** 设置为 `Load-dependent Magic Formula coefficients`，以启用载荷相关 Magic Formula 系数。

以下参数对于所有参数化都是新增的：

- **滑移分母下边界, VXLOW**
- **最小有效车轮滑移, KPUMIN**
- **最大有效车轮滑移, KPUMAX**

## 描述

由 Magic Formula 系数给出的轮胎-道路动力学

Tire-Road Interaction (Magic Formula) 模块表示轮胎胎面与道路路面之间的相互作用。Magic Formula 使用基于拟合系数的经验公式预测由这种相互作用产生的纵向力。该模块忽略轮胎特性，如柔顺性和惯性。您可以轻松可视化纵向摩擦力相对于车轮滑移的关系。要查看该图，请单击模块对话框 **描述** 部分中的 **绘制摩擦力与滑移的关系** 超链接。

纵向力与车轮滑移关系图窗口

### 轮胎-道路相互作用模型

该模块使用 Pacejka [2] 的 Magic Formula 表示轮胎-道路接地点处的纵向力。

该图显示作用在轮胎上的力。下表定义轮胎模型变量。

展示 F\_z、F\_x、V\_x 和旋转速度 Omega 的轮胎示意图

| 符号 | 描述 |
| --- | --- |
| *Ω* | 车轮角速度。 |
| *rw* | 车轮半径。 |
| *Vx* | 轮毂纵向速度。 |
| rwΩ | 轮胎胎面纵向速度。 |
| *u* | 轮胎纵向变形。 |
| VT=rwΩ′=rwΩ+u˙ | 轮胎胎面纵向速度。通常，轮胎胎面纵向速度包含由轮胎旋转引起的分量 *rwΩ*，以及可选的由轮胎变形引起的分量 u˙。由于端口 **T** 计算 *VT*，轮胎旋转和变形的计算发生在该模块之外。 |
| Vsx=Vx−VT | 接地点滑移速度。如果不存在轮胎纵向柔顺性，则 u=0。 |
| k=−Vsx|Vx|smooth | 无柔顺性轮胎的车轮滑移。 |
| *Fz* | 作用在轮胎上的垂直载荷。 |
| *Fz0* | 作用在轮胎上的标称垂直载荷。 |
| Fx=f(k,Fz) | 在接触点处施加到轮胎上的纵向力。*f* 是轮胎的特性函数。 |

### 轮胎响应

您可以对轮胎滚动和滑移进行建模。

**力和特性函数**

该模块使用稳态轮胎特性函数 Fx=f(k,Fz)，其中：

- *Fx* 是作用在轮胎上的纵向力。
- *Fz* 是垂直载荷。
- *k* 是车轮滑移

**滚动和滑移**

无滑移、无柔顺性轮胎的平移运动方程为 Vx=rwΩ。当轮胎发生滑移时，会产生纵向力 *Fx*。

接地点滑移速度为 Vsx=Vx−rwΩ−u˙。对于无柔顺性轮胎，*u* = 0。未平滑的接地点滑移为

k=−Vsx|Vx|,

并且该模块按如下方式饱和滑移分母

|Vx|={VXLOWif  |Vx|<VXLOW|Vx|otherwise

其中 *VXLOW* 是 **滑移分母下边界, VXLOW** 参数。该模块在过渡区域 -*VXLOW* - *Vth*/2 < *Vx* < -*VXLOW* + *Vth*/2  和 *VXLOW* - *Vth*/2 < *Vx* < *VXLOW* + *Vth*/2 上将 *|Vx|* 平滑过渡到 *VXLOW*。该模块根据以下方式饱和滑移

k={kpuminif −Vsx|Vx|<kpuminkpumaxif −Vsx|Vx|>kpumax−Vsx|Vx|otherwise

其中 *kpumin* 是 **最小有效车轮滑移, KPUMIN** 参数，*kpumax* 是 **最大有效车轮滑移, KPUMAX** 参数。该模块在区域 *kpumin* - *kth*/2 < *k* < *kpumin* + *kth*/2  和 *kpumax* - *kth*/2 < *k* < *kpumax* + *kth*/2 上过渡 *k*。该模块将滑移平滑阈值定义为

kth=Vth1m/s.

对于此方程，抱死滑动的车轮具有 *k* = -1。对于完美滚动，*k* = 0。

**典型道路条件下的 Magic Formula 系数**

该模块使用基于经验轮胎数据的数值。这些值是常见道路条件下常量 Magic Formula 系数的典型集合。

| 路面 | B | C | D | E |
| --- | --- | --- | --- | --- |
| 干燥沥青路面 | 10 | 1.9 | 1 | 0.97 |
| 潮湿沥青路面 | 12 | 2.3 | 0.82 | 1 |
| 雪 | 5 | 2 | 0.3 | 1 |
| 冰 | 4 | 2 | 0.1 | 1 |

### 参数化

**峰值纵向力与对应滑移**

当将 **Parameterize by** 设置为 `Peak longitudinal force and corresponding slip` 时，该模块使用一组具有代表性的 Magic Formula 系数。模块会缩放这些系数，以在额定垂直载荷 *Fz0* 下，得到你指定的对应滑移 *κ0* 处的峰值纵向力 *Fx0*。

**具有常量系数的 Magic Formula**

当将 **Parameterize by** 设置为 `Constant Magic Formula coefficients` 时，该模块使用无量纲系数 *B*、*C*、*D* 和 *E*，或刚度、形状、峰值和曲率，使得

Fx=f(κ,Fz)=Fz⋅D⋅sin(C⋅arctan{Bκ−E[Bκ−arctan(Bκ)]}).

*f* 在 k=0 处的斜率为 BCD⋅Fz。

**具有载荷相关系数的 Magic Formula**

当将 **Parameterize by** 设置为 `Load-dependent Magic Formula coefficients` 时，该模块使用无量纲系数，这些系数是轮胎载荷的函数。在属性检查器中输入的更复杂参数集 `p_i` 指定了这些函数：

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

*SHx* 和 *SVx* 表示力-滑移函数中滑移和纵向力的偏移量，或者如果将该函数绘制为曲线，则表示水平和垂直偏移量。
*μx* 是纵向载荷相关摩擦系数。
*εx* 是一个很小的数，用于在 *Fz* 趋近于零时防止除零。

### 假设与限制

Tire-Road Interaction (Magic Formula) 模块仅假设纵向运动，不包含外倾、转向或侧向运动。
