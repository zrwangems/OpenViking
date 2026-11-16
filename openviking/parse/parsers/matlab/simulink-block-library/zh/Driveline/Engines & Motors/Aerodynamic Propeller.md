---
type: simulink-block
title: 'Aerodynamic Propeller'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'aerodynamicpropeller'
documentation_source_path: 'ref/aerodynamicpropeller.html'
language: zh-CN
chinese_source: worker-translation
---

# Aerodynamic Propeller

## 端口

### 输入

### **Va** — 前进速度，m/s physical signal

与通过螺旋桨的流速相关联的 Physical signal 输入端口，单位为 m/s。

#### 依赖关系

要启用此端口，请将 **Translational connections** 设置为 `Physical signals`。

### **θ** — 桨叶桨距，deg physical signal

与桨叶桨距相关联的 Physical signal 输入端口，单位为 deg。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Polynomial fit`、`Tabulated data for advance ratio`、`Tabulated data for advance angle` 或 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable collective pitch control**。

### **θ\_1c** — 横向周期变距，deg physical signal

与横向周期变距相关联的 Physical signal 输入端口，单位为 deg。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **θ\_1s** — 纵向周期变距，deg physical signal

与纵向周期变距相关联的 Physical signal 输入端口，单位为 deg。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **ξ** — 空气入流角，deg physical signal

与空气入流角相关联的 Physical signal 输入端口，单位为 deg。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **Rho** — 可变密度，kg/m^3 physical signal

与流体密度相关联的 Physical signal 输入端口，单位为 kg/m3。

#### 依赖关系

要启用此端口，请将 **Fluid density specification** 设置为 `Variable`。

### **w** — 螺旋桨旋转速度，rad/s physical signal

与螺旋桨旋转速度相关联的 Physical signal 端口，单位为 rad/s。

#### 依赖关系

要启用此端口，请将 **Rotational connections** 设置为 `Physical signals`。

### 输出

### **Th** — 螺旋桨推力，N physical signal

与螺旋桨生成的推力相关联的 Physical signal 输出端口，单位为 N。

#### 依赖关系

要启用此端口，请将 **Translational connections** 设置为 `Physical signals`。

### **E** — 效率，unitless physical signal

与螺旋桨效率相关联的 Physical signal 输出端口。效率信号是前进比绝对值的函数。

#### 依赖关系

要启用此端口，请选中 **Efficiency sensor**。

### **Q** — 螺旋桨阻力矩，N\*m physical signal

与螺旋桨阻力矩相关联的 Physical signal 端口，单位为 N\*m。

#### 依赖关系

要启用此端口，请将 **Rotational connections** 设置为 `Physical signals`。

### **Fx** — *x* 方向力，N physical signal

与 *x* 方向力相关联的 Physical signal 输出端口，单位为 N。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **Fy** — *y* 方向力，N physical signal

与 *y* 方向力相关联的 Physical signal 输出端口，单位为 N。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **Mx** — *x* 方向力矩，N\*m physical signal

与 *x* 方向力矩相关联的 Physical signal 输出端口，单位为 N\*m。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### **My** — *y* 方向力矩，N\*m physical signal

与 *y* 方向力矩相关联的 Physical signal 输出端口，单位为 N\*m。

#### 依赖关系

要启用此端口，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`，并选中 **Enable transverse flow and cyclic pitch controls**。

### 守恒

### **R1** — 杆接口机械旋转

与杆接口关联的机械旋转守恒端口。

#### 依赖关系

要启用此端口，请将 **Rotational connections** 设置为 `Conserving`。

### **R2** — 飞行器速度和推力机械平移

与飞行器速度和推力关联的机械平移守恒端口。

#### 依赖关系

要启用此端口，请将 **Translational connections** 设置为 `Conserving`。

### **C2** — 参考流机械平移

与螺旋桨所推挤的空气或风的运动关联的机械平移守恒端口。

#### 依赖关系

要启用此端口，请将 **Translational connections** 设置为 `Conserving`。

## 参数

### 螺旋桨

### **Parameterization** — 螺旋桨参数化 `Constant coefficients`（默认） | `Polynomial fit` | `Tabulated data for advance ratio` | `Tabulated data for advance angle` | `Tabulated data for airfoil lift and drag coefficients`

用于通过常数、多项式、制表推力和功率系数，或制表升力和阻力系数对螺旋桨进行参数化的选项。从以下设置中选择：

- `Constant coefficients` — 使用相对于前进比的恒定推力和功率系数。
- `Polynomial fit` — 使用多项式系数对前进比进行参数化。
- `Tabulated data for advance ratio` — 使用制表前进比数据对前进比进行参数化。
- `Tabulated data for advance angle` — 使用相对于桨叶半径 70% 处相对前进速度的推力和功率系数。
- `Tabulated data for airfoil lift and drag coefficients` — 使用相对于沿桨叶位置的升力和阻力系数。

### **Propeller direction** — 螺旋桨方向 `Negative rotational velocity generates positive thrust for positive thrust coefficients`（默认） | `Positive rotational velocity generates positive thrust for positive thrust coefficients`

典型螺旋桨旋转方向。当您选择：

- `Positive rotational velocity generates positive thrust for positive thrust coefficients` — *ε =*+1。
- `Negative rotational velocity generates positive thrust for positive thrust coefficients` — *ε =*-1。

### **Propeller diameter** — 螺旋桨直径 `0.254` `m`（默认） | positive scalar

螺旋桨的直径。

### **Enable collective pitch control** — 总距桨叶控制选项 `off`（默认） | `on`

是否启用总距控制。您使用 **θ** 端口指定桨叶总距的值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为

- `Polynomial fit`
- `Tabulated data for advance ratio`
- `Tabulated data for advance angle`
- `Tabulated data for airfoil lift and drag coefficients`

### **Enable transverse flow and cyclic pitch controls** — 受控周期变距选项 `off`（默认） | `on`

是否启用横向流和周期变距，您使用 **θ\_1c** 和 **θ\_1s** 端口指定。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`。

### **Thrust coefficient, kT** — 推力系数 `0.25`（默认） | positive scalar

无量纲恒定推力系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Constant coefficients`。

### **Power coefficient, kP** — 功率系数 `0.13`（默认） | positive scalar

无量纲恒定功率系数。

### **kT polynomial coefficients (pN...p0)** — 推力系数多项式系数 `[.002, .0006, -.0509, .0617]`（默认） | vector

无量纲多项式推力系数的 vector。按降序指定元素。该模块使用这些系数生成查找表。有关详细信息，请参阅 Using Lookup Tables in Equations。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Polynomial fit`
- 清除 **Enable collective pitch control**

### **kP polynomial coefficients (pN...p0)** — 功率系数多项式系数 `[-.0752, .0577, -.0622, .16]`（默认） | vector

无量纲多项式功率系数的 vector。按降序指定元素。该模块使用这些系数生成查找表。有关详细信息，请参阅 Using Lookup Tables in Equations。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Polynomial fit`
- 清除 **Enable collective pitch control**

### **Pitch angle vector, θ** — 桨距角 `[-15, 15, 25, 35, 45]` `deg`（默认） | vector of elements in the range [-360,360]

使用总距控制时的参考桨距角。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Polynomial fit`、`Tabulated data for advance ratio` 或 `Tabulated data for advance angle`
- 选中 **Enable collective pitch control**

### **Table of kT polynomial coefficients (θ, pN...p0)** — 可控桨距螺旋桨的多项式推力系数 `[.0002, -.00041, -.036, .03; .00026, -.00056, -.048, .04; .002, .00063, -.051, .062; .0014, -.0016, -.048, .087; .00087, -.0036, -.041, .12]`（默认） | matrix

针对 **Pitch angle vector, θ** 参数中给定 *θ* 的多项式推力系数 vector 的表。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Polynomial fit`
- 选中 **Enable collective pitch control**

### **Table of kP polynomial coefficients (θ, pN...p0)** — 可控桨距螺旋桨的多项式功率系数 `[-.1, .031, .0055, .088; -.081, -.025, .0044, .07; -.075, .058, -.062, .16; -.052, .065, -.08, .3; -.031, .057, -.069, .4]`（默认） | matrix

针对 **Pitch angle vector, θ** 参数中给定 *θ* 的多项式扭矩系数 vector 的表。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Polynomial fit`
- 选中 **Enable collective pitch control**

### **Advance ratio vector, J** — 制表推力和功率系数对应的前进比范围 `[.01, .3, .625, 1.55, 2, 2.6]`（默认） | vector

制表前进比。每个元素在 **Thrust coefficient vector, kT(J)** 和 **Power coefficient vector, kP(J)** 参数中都有一个对应元素，或在 **Thrust coefficient table, kT(θ, J)** 和 **Power coefficient table, kT(θ, J)** 参数中对应一列。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance ratio`。

### **Thrust coefficient vector, kT(J)** — 给定前进比的制表推力系数值 `[.0614, .0473, .0318, -.0127, -.0343, -.063]`（默认） | vector

作为前进比函数的制表推力系数值。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance ratio`
- 清除 **Enable collective pitch control**

### **Power coefficient vector, kP(J)** — 给定前进比的制表功率系数值 `[.1496, .1314, .116, -.0521, -.1503, -.2813]`（默认） | vector

作为前进比函数的制表功率系数值。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance ratio`
- 清除 **Enable collective pitch control**

### **Thrust coefficient table, kT(θ, J)** — 给定桨距角和前进比的制表推力系数值 `[.00019, .013, .0048, -.017, -.03, -.045;`（默认） | matrix | ...

作为桨距角和前进比函数的制表推力系数值。各列对应于 **Advance ratio vector, J** 参数中的元素，各行对应于 **Pitch angle vector, θ** 参数中的元素。

默认值为 `[.00019, .013, .0048, -.017, -.03, -.045; .00039, .025, .0096, -.037, -.06, -.09; .00061, .047, .032, -.013, -.034, -.063; .00086, .072, .057, .014, -.0076, -.036; .12, .104, .09, .049, .029, .0019]`。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance ratio`
- 选中 **Enable collective pitch control**

### **Power coefficient table, kP(θ, J)** — 给定桨距角和前进比的制表功率系数值 `[.029, .029, .016, .06, .009, -.16;`（默认） | matrix | ...

作为桨距角和前进比函数的制表功率系数值。各列对应于 **Advance ratio vector, J** 参数中的元素，各行对应于 **Pitch angle vector, θ** 参数中的元素。

默认值为 `[.029, .029, .016, .06, .009, -.16; .059, .054, .031, -.12, -.19, -.29; .15, .13, .12, -.052, -.15, -.28; .26, .24, .22, .097, -.04, -.25; .39, .39, .38, .32, .24, .062]`。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance ratio`
- 选中 **Enable collective pitch control**

### **Advance angle vector, β** — 递增前进角 `linspace(0, 360, 10)` `deg`（默认） | vector of length *N*

制表前进角。使用单调递增的 vector，其元素范围为 [0, 360] deg。在仿真期间，螺旋桨前进角可以在 [0, 360) deg 范围内，此时该模块会将角度包裹在 0 到 360 deg 之间。

当您将 **Extrapolation method** 设置为 `Linear` 或 `Nearest` 时：

- 如果第一个元素不是 0，则当 *β* 小于第一个元素时，该模块基于第一个或前两个元素进行外插。
- 如果最后一个元素不等于 360 deg，则当 *β* 大于最后一个元素时，该模块基于最后一个或最后两个元素进行外插。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance angle`。

### **Thrust coefficient vector, Ct(β)** — 给定前进角的制表推力系数 `0.035 * sind(linspace(0, 360, 10) - 200)`（默认） | vector of length *N*

作为前进角函数的制表推力系数。该系数取决于桨叶半径 70% 处的桨叶相对前进速度。此 vector 中的元素必须与 **Advance angle vector, β** 参数一一对应。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance angle`
- 清除 **Enable collective pitch control**

### **Torque coefficient vector, Cq(β)** — 给定前进角的制表扭矩系数 `0.010 * sind(linspace(0, 360, 10) - 200)`（默认） | vector of length *N*

作为前进角函数的制表阻力扭矩系数。该系数基于桨叶半径 70% 处的桨叶相对前进速度。此 vector 中的元素必须与 **Advance angle vector, β** 参数一一对应。

#### 依赖关系

要启用此参数：

- 将 **Parameterization** 设置为 `Tabulated data for advance angle`
- 清除 **Enable collective pitch control**

### **Thrust coefficient table, Ct(θ, β)** — 给定桨距角和前进角的制表推力系数 `[0.01 * sind(linspace(0, 360, 10) - 200); 0.020 * sind(linspace(0, 360, 10) - 200);`（默认） | matrix | ...

作为桨距角和前进角函数的制表推力系数。默认值为 `[0.01 * sind(linspace(0, 360, 10) - 200); 0.020 * sind(linspace(0, 360, 10) - 200); 0.035 * sind(linspace(0, 360, 10) - 200); 0.04 * sind(linspace(0, 360, 10) - 200); 0.06 * sind(linspace(0, 360, 10) - 200)]`。

#### 依赖项

要启用此参数：

- 将 **Parameterization** 设置为
  `Tabulated data for advance
  angle`
- 选择 **Enable collective pitch
  control**

### **Torque coefficient table, Cq(θ, β)** — 给定桨距角和前进角的表格化扭矩系数 `[0.0005 * sind(linspace(0, 360, 10) - 200); 0.0015 * sind(linspace(0, 360, 10) - 200);` （默认） | matrix | ...

作为桨距角和前进角函数的表格化扭矩系数。默认值为 `[0.0005 * sind(linspace(0, 360, 10)
- 200); 0.0015 * sind(linspace(0, 360, 10) - 200); 0.0025 *
sind(linspace(0, 360, 10) - 200); 0.0035 * sind(linspace(0, 360, 10)
- 200); 0.0045 * sind(linspace(0, 360, 10) - 200)]`。

#### 依赖项

要启用此参数：

- 将 **Parameterization** 设置为
  `Tabulated data for advance
  angle`
- 选择 **Enable collective pitch
  control**

### **Interpolation method** — 断点值之间的插值方法 `Linear` （默认） | `Smooth`

用于查找表断点插值的方法。模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可获得最低计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for advance ratio` 或 `Tabulated
data for advance angle`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear` （默认） | `Nearest` | `Error`

用于查找表断点外推的方法。此方法确定当输入值在参数列表中指定的范围之外时的输出值。模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可在外推区域以及与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点或不低于数据中最低点的外推。
- `Error` — 当希望数据位于表范围内时，选择此选项可避免外推。如果输入信号超出表范围，仿真会停止并生成错误。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for advance ratio` 或 `Tabulated
data for advance angle`。

### **Root pitch angle** — 根部桨距角 `20` `deg` （默认） | scalar

螺旋桨叶片的恒定桨距偏移角。

#### 依赖项

要启用此参数：

- 将 **Parameterization** 设置为
  `Tabulated data for airfoil lift and
  drag coefficients`
- 清除 **Enable collective pitch
  control**

### **Number of blades** — 叶片数量 `2` （默认） | positive scalar

螺旋桨叶片数量。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Number of blade elements** — 叶素数量 `10` （默认） | positive scalar

单个叶片的叶素数量。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Number of azimuthal locations** — 方位角位置数量 `10` （默认） | positive scalar

模块沿方位角积分力和力矩的位置数量。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients` 并选择 **Enable transverse flow and cyclic pitch controls**。

### **Nondimensional radial location vector, r** — 径向位置 `[.1, .12, .2, .4, .6, .8, 1]` （默认） | vector

给定一组叶片尺寸的径向位置。`1` 等效于叶片半径。此向量的第一个元素定义 *e*，即根部切除。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Blade twist vector, θ\_tw(r)** — 叶素扭转 `[30, 35, 50, 30, 20, 15, 10]` `deg` （默认） | vector

给定径向位置处的叶片扭转角 *θ*。此向量的元素与 **Nondimensional radial location vector, r** 参数一一对应。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Normalized chord length vector, c(r)/D** — 叶素弦长 `[.0676, .0666, .0824, .1025, .0885, .0598, .0133]` （默认） | vector of length *N*

沿叶片给定径向位置处的按直径归一化的弦长。此向量的元素与 **Nondimensional radial location vector, r** 参数以及 **Airfoil lift coefficient table, Cl(α,r)** 和 **Airfoil drag coefficient table, Cd(α,r)** 参数的列一一对应。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Airfoil angle of attack vector, α** — 攻角 `-180 : 10 : 180` `deg` （默认） | vector of length *M*

攻角范围。此向量的元素与 **Airfoil lift coefficient table, Cl(α,r)** 和 **Airfoil drag coefficient table, Cd(α,r)** 参数的行一一对应。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Airfoil lift coefficient table, Cl(α,r)** — 翼型升力系数 *M* x *N* matrix | ...

给定攻角和沿叶片径向位置的翼型升力系数。此矩阵中的行与 **Airfoil angle of attack vector, α** 参数一一对应。此矩阵中的列与 **Nondimensional radial location vector, r** 参数一一对应。

默认值为 `[.1326, .1326, .1274, .1274, .1274,
.1274, .1274; .3626, .3626, .5002, .5002, .5002, .5002, .5002;
.5528, .5528, .8007, .8007, .8007, .8007, .8007; .7256, .7256,
1.0125, 1.0125, 1.0125, 1.0125, 1.0125; .8016, .8016, 1.1556,
1.1556, 1.1556, 1.1556, 1.1556; .7873, .7873, 1.1604, 1.1604,
1.1604, 1.1604, 1.1604; .7031, .7031, 1.0493, 1.0493, 1.0493,
1.0493, 1.0493; .5423, .5423, .7973, .7973, .7973, .7973, .7973;
.3537, .3537, .4332, .4332, .4332, .4332, .4332; .1155, .1155,
-.0376, -.0376, -.0376, -.0376, -.0376; -.1045, -.1045, -.4096,
-.4096, -.4096, -.4096, -.4096; -.2999, -.2999, -.672, -.672, -.672,
-.672, -.672; -.4401, -.4401, -.9343, -.9343, -.9343, -.9343,
-.9343; -.5186, -.5186, -1.0477, -1.0477, -1.0477, -1.0477, -1.0477;
-.5303, -.5303, -1.0387, -1.0387, -1.0387, -1.0387, -1.0387; -.5073,
-.5073, -.9565, -.9565, -.9565, -.9565, -.9565; -.442, -.442,
-.7713, -.7713, -.7713, -.7713, -.7713; -.2658, -.2658, -.4832,
-.4832, -.4832, -.4832, -.4832; .4109, .4109, .3629, .3629, .3629,
.3629, .3629; 1.1635, 1.1635, 1.3779, 1.3779, 1.3779, 1.3779,
1.3779; 1.2412, 1.2412, 1.4033, 1.4033, 1.4033, 1.4033, 1.4033;
.7434, .7434, 1.3453, 1.3453, 1.3453, 1.3453, 1.3453; .7908, .7908,
1.2862, 1.2862, 1.2862, 1.2862, 1.2862; .7525, .7525, 1.1562,
1.1562, 1.1562, 1.1562, 1.1562; .6722, .6722, .9487, .9487, .9487,
.9487, .9487; .5324, .5324, .7047, .7047, .7047, .7047, .7047;
.3365, .3365, .382, .382, .382, .382, .382; .0529, .0529, -.0229,
-.0229, -.0229, -.0229, -.0229; -.2728, -.2728, -.316, -.316, -.316,
-.316, -.316; -.4135, -.4135, -.6195, -.6195, -.6195, -.6195,
-.6195; -.5087, -.5087, -.7847, -.7847, -.7847, -.7847, -.7847;
-.5342, -.5342, -.8419, -.8419, -.8419, -.8419, -.8419; -.5166,
-.5166, -.7658, -.7658, -.7658, -.7658, -.7658; -.4321, -.4321,
-.5707, -.5707, -.5707, -.5707, -.5707; -.2864, -.2864, -.3098,
-.3098, -.3098, -.3098, -.3098; -.1073, -.1073, -.0893, -.0893,
-.0893, -.0893, -.0893; .1326, .1326, .1274, .1274, .1274, .1274,
.1274]`。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### **Airfoil drag coefficient table, Cd(α,r)** — 翼型阻力系数 *M* x *N* matrix | ...

给定攻角和沿叶片径向位置的翼型阻力系数。此矩阵中的行与 **Airfoil angle of attack vector, α** 参数一一对应。此矩阵中的列与 **Nondimensional radial location vector, r** 参数一一对应。

默认值为 `[.0055, .0055, .3904, .3904, .3904,
.3904, .3904; .0774, .0774, .449, .449, .449, .449, .449; .2412,
.2412, .5915, .5915, .5915, .5915, .5915; .4342, .4342, .8307,
.8307, .8307, .8307, .8307; .679, .679, 1.0909, 1.0909, 1.0909,
1.0909, 1.0909; .9003, .9003, 1.3868, 1.3868, 1.3868, 1.3868,
1.3868; 1.0825, 1.0825, 1.6565, 1.6565, 1.6565, 1.6565, 1.6565;
1.2281, 1.2281, 1.875, 1.875, 1.875, 1.875, 1.875; 1.3205, 1.3205,
2.017, 2.017, 2.017, 2.017, 2.017; 1.3234, 1.3234, 2.0407, 2.0407,
2.0407, 2.0407, 2.0407; 1.2391, 1.2391, 1.9513, 1.9513, 1.9513,
1.9513, 1.9513; 1.0963, 1.0963, 1.7643, 1.7643, 1.7643, 1.7643,
1.7643; .8978, .8978, 1.5048, 1.5048, 1.5048, 1.5048, 1.5048; .6525,
.6525, 1.2281, 1.2281, 1.2281, 1.2281, 1.2281; .4203, .4203, .838,
.838, .838, .838, .838; .2428, .2428, .5434, .5434, .5434, .5434,
.5434; .0951, .0951, .2517, .2517, .2517, .2517, .2517; .0292,
.0292, .0698, .0698, .0698, .0698, .0698; .0148, .0148, .0267,
.0267, .0267, .0267, .0267; .0808, .0808, .0509, .0509, .0509,
.0509, .0509; .2429, .2429, .1561, .1561, .1561, .1561, .1561;
.5019, .5019, .3927, .3927, .3927, .3927, .3927; .7217, .7217,
.7438, .7438, .7438, .7438, .7438; .9336, .9336, 1.1277, 1.1277,
1.1277, 1.1277, 1.1277; 1.0984, 1.0984, 1.4838, 1.4838, 1.4838,
1.4838, 1.4838; 1.2274, 1.2274, 1.7877, 1.7877, 1.7877, 1.7877,
1.7877; 1.3016, 1.3016, 1.9779, 1.9779, 1.9779, 1.9779, 1.9779;
1.3305, 1.3305, 2.0516, 2.0516, 2.0516, 2.0516, 2.0516; 1.2889,
1.2889, 1.9974, 1.9974, 1.9974, 1.9974, 1.9974; 1.1677, 1.1677,
1.8463, 1.8463, 1.8463, 1.8463, 1.8463; 1.0076, 1.0076, 1.5699,
1.5699, 1.5699, 1.5699, 1.5699; .8068, .8068, 1.2596, 1.2596,
1.2596, 1.2596, 1.2596; .5688, .5688, .9493, .9493, .9493, .9493,
.9493; .3604, .3604, .6154, .6154, .6154, .6154, .6154; .1802,
.1802, .5015, .5015, .5015, .5015, .5015; .0699, .0699, .4265,
.4265, .4265, .4265, .4265; .0055, .0055, .3904, .3904, .3904,
.3904, .3904]`。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for airfoil lift and drag
coefficients`。

### 环境和动力学

### **Fluid density specification** — 流体密度选择 `Constant` （默认） | `Variable`

用于指定恒定或可变流体密度的选项。

### **Fluid density** — 恒定流体密度值 `1.225` `kg/m^3` （默认）

恒定流体密度值。

#### 依赖项

要启用此参数，请将 **Fluid density specification** 设置为 `Constant`。

### **Rotational connections** — 旋转运动输入选项 `Physical signals` （默认） | `Conserving`

用于将螺旋桨旋转速度和阻力扭矩分别作为物理信号输入和输出，或作为旋转连接进行仿真的选项。此设置决定图标中轮毂的颜色，该颜色指示模块处于旋转守恒域还是物理信号域。

### **Translational connections** — 平动运动输入选项 `Conserving` （默认） | `Physical signals`

用于将前进速度和螺旋桨推力分别作为物理信号输入和输出，或作为平动连接进行仿真的选项。此设置决定图标中叶片的颜色，该颜色指示模块处于平动守恒域还是物理信号域。当你选择 时，恒定伴流分数会相对于车辆速度降低前进速度。

### **Model inertia** — 惯性选项 `off` （默认） | `on`

是否模拟由转子运动引起的惯性。模块在端口 **R1** 施加旋转惯性，在端口 **R2** 施加平动惯性。

#### 依赖项

要启用此参数，请将 **Rotational connections** 或 **Translational connections** 设置为 conserving。

### **Propeller inertia** — 螺旋桨惯性 `1` `kg*m^2` （默认） | positive scalar

螺旋桨组件的惯性。模块在端口 **R1** 施加该惯性。

#### 依赖项

要启用此参数，请将 `Conserving`**Rotational connections** 设置为 conserving 并选择 **Model inertia**。

### **Propeller mass** — 螺旋桨质量 `10` `kg` （默认） | positive scalar

螺旋桨组件的质量。模块在端口 **R2** 施加平动惯性。

#### 依赖项

要启用此参数，请将 **Translational connections** 设置为 conserving 并选择 **Model inertia**。

### 高级

### **Efficiency sensor** — 运行效率输出选项 `off` （默认） | `on`

是否启用效率端口 **E**，该端口输出正值效率信号。

### **Rotational speed threshold** — 转速平滑点 `0.001` `Hz` （默认） | positive scalar

饱和阈值 *nThr*，超过该值时模块会应用平滑，直到饱和点。

### **Saturation threshold for nondimensional coefficients** — 无量纲系数平滑点 `0.001` （默认） | positive scalar

饱和阈值 *kThr*，模块在此对无量纲系数应用平滑。

### **Check if operating beyond normal propeller operation** — 工作边界容差 `Warning` （默认） | `None` | `Error`

是否在螺旋桨超出运行参数时生成警告或错误。模块检查螺旋桨是否在第一象限运行。如果 *Va* 或 *n(t)* 不是正值，螺旋桨会生成具有相应符号的推力系数和扭矩系数，并根据参数设置生成警告或错误。提高 **Rotational speed threshold** 参数的值会使触发变得不那么敏感。

当你将 **Parameterization** 设置为 `Polynomial fit` 时，当螺旋桨超过 *kT* 参数的第一个正根时，模块会生成警告或错误。

模块使用关于第一象限的对称或非对称行为来近似水动力学。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Polynomial fit` 或 `Tabulated data for advance ratio`。

### **Power threshold for efficiency calculation** — 功率阈值 100 `W` （默认）

计算效率时的功率阈值。

#### 依赖项

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients` 并选择 **Efficiency sensor**。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：控制横向流动和周期变距

要控制横向流动和周期变距，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients` 并选择 **Enable transverse flow and cyclic controls**。在端口 **ξ** 处将气流角输入为物理信号。使用 **Number of azimuthal locations** 参数指定模块沿方位角积分力和力矩的位置数。分别在端口 **θ\_1c** 和 **θ\_1s** 处输入横向和纵向周期变距。模块将横向和纵向力及力矩输出到端口 **Fx**、**Fy**、**Mx** 和 **My**。

### R2025a: Blade pitch type 参数已重命名

**Blade pitch type** 参数现在为 **Enable collective pitch control** 参数。当您选择 **Enable collective pitch control** 时，模块的行为与在先前版本中将 **Blade pitch type** 设置为 `Controlled` 时相同。

### R2023b: 通过升力和阻力系数进行参数化

要沿螺旋桨按表格化升力和阻力系数对模块进行参数化，请将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients`。

### R2023a: 性能更新

端口 **C1** 不再需要，已被移除。

### R2023a: 新增惯性选项

要对惯性建模，请选择 **Model inertia**，并将 **Rotational connections** 或 **Translational connections** 设置为 `Conserving`，以分别启用 **Propeller inertia** 或 **Propeller mass** 参数。

## 描述

由旋转运动产生推力的螺旋桨

Aerodynamic Propeller 模块表示一个将旋转机械运动转换为空气动力学应用推力的螺旋桨。您可以使用常数、多项式或表格化数据对螺旋桨进行参数化，以表征推力与功率或系数。您可以提供表格化的前进速度数据、表格化的前进角数据，或表格化的翼型升力和阻力系数数据。当您对惯性建模时，默认模块参数表示一个 10 kg、两叶、直径 1.5 m 的螺旋桨。

您可以使用物理信号来控制总距叶片桨距、周期变距和横向流速。

以下术语有助于理解该模块：

- *前进速度* 是穿过螺旋桨的流速，*Va*。
- *前进比* 是穿过螺旋桨的流速相对于螺旋桨叶尖角速度的比值。当您将 **Parameterization** 设置为 `Polynomial fit` 或 `Tabulated data for advance ratio` 时，模块使用该值确定 *kT* 和 *kP*。
- *前进角* 是螺旋桨运行条件在四象限图上的角位置。当您将 **Parameterization** 设置为 `Tabulated data for advance ratio` 时，模块使用该值确定 *CT* 和 *CQ*。
- *象限* 是螺旋桨运行条件的相对二维位置，其中垂直轴为 *Va*，水平轴为 *ω*。
- *桨距角* 是叶片旋转平面与叶片弦线之间的角度。

模块方程引用以下量：

- *T* 是螺旋桨推力。
- *Q* 是螺旋桨扭矩。
- *ρ* 是流体密度。您可以使用 **Density** 参数或 **Rho** 端口指定流体密度。
- *θ* 是桨距角。
- *D* 是 **Propeller diameter** 参数。
- *ω* 是端口 **R** 处的螺旋桨角速度输入。有关在 Simscape™ 中使用角单位的详细信息，请参阅 Angular Units。
- *n* 是螺旋桨角速度，单位为每秒转数，它一致地对功率和推力进行无量纲化。模块定义 *ω = 2πn*。
- *nThr* 是 **Rotational speed threshold** 参数。
- *ε* 是 **Propeller direction** 参数。
- *kT* 是相对于螺旋桨转速的推力系数。
- *kP* 是相对于螺旋桨转速的功率系数。
- *pkT* 是多项式推力系数向量或二维矩阵。
- *pkP* 是多项式功率系数向量或二维矩阵。
- *CT* 是相对于相对前进速度的推力系数。
- *CQ* 是相对于相对前进速度的扭矩系数。
- *kThr* 是 **Saturation threshold for nondimensional coefficients** 参数。
- *J* 是前进比。
- *Va* 是前进速度。使用 **Va** 端口指定前进速度。
- *VR* 是叶片半径 70% 处叶片截面的相对前进速度。
- *η* 是效率。
- *C\*T* 是基于叶片半径 70% 处叶片相对前进速度的推力系数。
- *C\*T,TLU* 是参考推力系数向量或二维矩阵。
- *C\*Q* 是基于叶片半径 70% 处叶片相对前进速度的扭矩系数。
- *C\*Q,TLU* 是参考扭矩系数向量或二维矩阵。
- *β* 是前进角。
- *βTLU* 是参考前进角。

### 参数化

螺旋桨性能取决于推力和功率系数。**Parameterization** 参数为您提供不同的选项来控制这些系数。螺旋桨输出取决于螺旋桨运行所在的象限。模块按如下方式定义四个象限：

- 第一象限：*+Va*、*+n*
- 第二象限：*+Va*、*-n*
- 第三象限：*-Va*、*-n*
- 第四象限：*-Va*、*+n*

该图显示了象限的可视化表示。

四象限图，其中前进速度为正 y 轴，前进旋转为正 x 轴。

当您将 **Parameterization** 设置为 `Constant coefficients` 时，直接指定推力和功率系数。否则，模块根据 **Parameterization** 设置计算这些系数。

**前进比**

当您将 **Parameterization** 设置为 `Polynomial fit` 或 `Tabulated data for advance ratio` 时，模块使用前进比 *J*。模块使用基本推力和功率方程的数值平滑版本，使得

T=kTρD4εnn2+nthr2Q=kPρD52πnn2+nthr2

模块将前进比定义为

J=VaεnD(n2+nThr2),

其中角速度阈值 *nThr* 对螺旋桨转速 *n* 进行线性化以实现平滑。

当您将 **Parameterization** 设置为：

- `Polynomial fit` —
  *kT* 和 *kP* 根据您为多项式系数参数指定的值随时间变化。模块将 *J* 饱和在 0 与多项式的第一个正根之间，并限制 *kT* 和 *kP* 始终为正。模块按如下方式计算推力和功率系数：

  kT=∑j=1:NNpkT,jJjkP=∑j=1:NNpkP,jJj

  其中 *pkT* 和 *pkP* 表示多项式系数。
- `Tabulated data for advance ratio` — 您针对给定的 *J* 值，或 *J* 和 *θ* 值（取决于 **Blade pitch type** 参数），为 *kT* 和 *kP* 指定表格化值。

当 **Efficiency sensor** 为 on 时，模块按如下方式计算效率：

η=PoweroutPowerin=TVA2πnQ=J2+kThr2kTkP2+kThr2

**前进角**

当您将 **Parameterization** 设置为 `Tabulated data for advance angle` 时，模块使用相对于相对前进角的推力和功率系数。模块将前进角定义为

β=arctan(Va0.7πεnD),

其中 *β* 是周期变距。您必须确保系数外插和周期环绕按预期发生。模块将相对前进速度的推力和扭矩系数定义为

CT\*=T18ρVR2πD2CQ\*=Q18ρVR2πD3

其中 *VR* 是叶片半径 70% 处叶片截面的相对前进速度，使得

VR2=VA2+(0.7Dπεn)2.

重新排列系数方程可得到模块针对相对前进速度的推力和扭矩方程：

T=CT\*18ρVR2D2Q=CQ\*18ρVR2D3

当您清除 **Enable collective pitch control** 时，模块按如下方式计算推力和扭矩系数：

CT\*=tablelookup(βTLU,CT,TLU\*,β,interpolation = interp\_method,extrapolation = extrap\_method)CQ\*=tablelookup(βTLU,CQ,TLU\*,β,interpolation = interp\_method,extrapolation = extrap\_method)

螺旋桨效率的基础是基本关系式

η=PoweroutPowerin=TVA2πεnQ=VACT\*2πεnDCQ\*.

当 **Efficiency sensor** 为 on 时，模块按如下方式计算平滑后的效率：

η=12πDVA2C\*2+(DπnThrKThr)2n2CQ\*2+(0.1nThrKThr)2.

**叶片单元升力和阻力系数**

当您将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients` 时，可以针对给定叶片单元对升力和阻力系数以及翼型几何进行参数化。模块将螺旋桨视为连续圆盘。当模块计算诱导速度 *vi* 时，动量守恒适用于穿过圆盘的空气。模块使用诱导速度来求沿叶片径向位置向量处总流速的大小和方向，然后使用该信息基于升力和阻力系数查找表求升力和阻力。以下量特定于该参数化：

- *TMT* — 由动量理论计算的推力
- *vi* — 由螺旋桨运动诱导的流速
- *vinflow* — 螺旋桨所经历空气的自由流来流速度
- *vax* — 叶片位置处的轴向速度
- *vh* — 理论悬停诱导速度
- *λ* — 无量纲化后的 *vax*
- *g(λ)* — 模块用于入流的函数
- *TBET* — 由叶片单元理论计算的推力
- *QBET* — 由叶片单元理论计算的扭矩
- *Nblades* — 螺旋桨叶片数量
- *r* — 由 **Nondimensional radial location vector, r** 参数定义的离散叶片单元位置，模块对其进行插值以求得 *y*
- *c* — 沿叶片某一位置处的弦长，其中长度以 *c* = *Geometric chord length/D* 的方式无量纲化
- *e* — 由 **Nondimensional radial location vector, r** 参数第一个元素给出的根部切除无量纲位置
- *vr(y)* — 作为 *y* 函数的切向速度
- *Cl,Cd* — 分别为逐元素的升力系数和阻力系数
- *ϕ(y)* — 沿叶片给定点处的入流角

模块使用动量理论定义平滑后的推力方程，使得

TMT=2ρπD24vinflow⋅vi,

其中模块隐式求解 *TMT* 和 *vi*。该图显示了模块如何考虑平移运动。虚线包围的较大区域包含内部质量。较小区域不包含。

该图显示了模块如何考虑旋转运动。虚线包围的较大区域包含内部惯性。较小区域不包含。

模块对 *vax* 进行平滑以求得 *vinflow*，从而允许前进流和倒退流之间的过渡，使得

vinflow=vax2+vh2⋅g(λ)vh=2⋅|TMT|ρπD2λ=2vax/ωDg(λ)={(2+λ)−2−λ2+(1+λ)⋅(0.109+0.217(λ−0.15)2)for −1≤λ≤0.63780else.

模块通过 **Nondimensional radial location vector, r** 参数中的值进行插值以求得 *y*。然后，模块基于表格化的攻角以及升力和阻力系数对升力和阻力系数进行插值，以求得 *Cl(y)* 和 *Cd(y)*。模块使用叶片单元理论按如下方式计算推力和扭矩：

TBET=NbladesρD24∫e1(vr2+vax2)⋅(Clcosϕ(y)−Cdsinϕ(y))⋅cdyQBET=NbladesρD38∫e1(vr2+vax2)⋅(Clsinϕ(y)−Cdcosϕ(y))⋅cydy

模块对每个离散叶片单元执行此积分。模块根据 **Number of blade elements** 参数中的设定对 *y* 进行离散化。该图总结了相对于地面的力和扭矩方向。

### 控制

默认情况下，模块将叶片桨距和总距周期变距约束为零。您可以选择使用物理信号控制其中一个或两个特性。当您控制周期变距时，还要为横向流提供物理信号。

**总距**

总距通过同时且均匀地改变所有旋翼叶片的桨距角来控制飞机的总升力。

当您将 **Parameterization** 设置为 `Tabulated data for advance angle` 并选择 **Enable collective pitch control** 时，可以在一定范围的桨距角 *θ* 内对螺旋桨进行参数化。您必须在 **Pitch angle vector,θ** 参数中将 *θ* 指定为向量，其中每个元素对应于 *kT* 和 *kP* 数组中的一行。模块按如下方式计算推力和功率系数：

CT\*=tablelookup(P/DTLU,βTLU,CT,TLU\*,P/D,β,interpolation = interp\_method,extrapolation = extrap\_method)CQ\*=tablelookup(P/DTLU,βTLU,CQ,TLU\*,P/D,β,interpolation = interp\_method,extrapolation = extrap\_method)

**周期变距和横向流**

周期变距通过随着旋翼叶片旋转周期性地改变其桨距角来控制飞机的滚转和俯仰。当您将 **Parameterization** 设置为 `Tabulated data for airfoil lift and drag coefficients` 并选择 **Enable transverse flow and cyclic controls** 时，模块分别从端口 **θ\_1c** 和 **θ\_1s** 接收横向和纵向周期变距作为物理信号。您在端口 **ξ** 提供气流角作为物理信号。模块将横向和纵向力及力矩输出到端口 **Fx**、**Fy**、**Mx** 和 **My**。

模块在计算推力和扭矩时，沿方位位置 *ψ* 考虑入流角 *ξ*，使得

Vplanar=ωr+Vatanξsinψϕ=atan2 (vax,vplanar)α=θ−ϕ

在模块计算出 *Cl(y)* 和 *Cd(y)* 的值后，它使用叶片力按如下方式计算叶片单元理论量：

TBET=∑iblade=1nblades∫e1Fi,NormaldyQBET=∑iblade=1nblades∫e1Fi,PlanarydyMBET,x=∑iblade=1nblades∫e1Fi,Normalsin(ψ)ydyFBET,x=∑iblade=1nblades∫e1Fi,Planarsin(ψ) dyMBET,y=∑iblade=1nblades∫e1Fi,Normalcos(ψ)ydyFBET,y=−∑iblade=1nblades∫e1Fi,Planarcos(ψ)dy

其中 *Fi,Normal* 和 *Fi,Planar* 是给定叶片 *iblade* 上的法向力和平面内力。模块使用以下方程计算这些力：

FNormal= ρD2 8(vr2+vax2)(Clcos(ϕ)−Cdsin(ϕ)) cFPlanar= ρD3 16(vr2+vax2)(Clsin(ϕ)+Cdcos(ϕ))c

然后，模块沿 *y* 进行积分，并根据方位位置对螺旋桨进行离散化，再对其进行积分以计算一个旋转周期内的效应，使得

T¯BET =12π∫02πTBETdψQBET=12π∫02πQBETdψM¯BET,x=12π∫02πMBET,xdψF¯BET,x=12π∫02πFBET,xdψM¯BET,y=12π∫02πMBET,ydψF¯BET,y=12π∫02πFBET,ydψ

其中模块将输出在 2π 上归一化。

使用 **Number of azimuthal locations** 参数指定模块沿方位角对力和力矩进行积分的位置数量。

### 惯性

您可以选择包含螺旋桨的平移惯性和旋转惯性。要模拟惯性，请将 **Rotational connections** 或 **Translational connections** 设置为 `Conserving`，并选择 **Model inertia**。当您选择 **Model inertia** 并将 **Rotational connections** 设置为 `Conserving` 时，请在 **Initial Targets** 部分设置轴上的初始旋转速度或扭矩，或将代数链接变量设置为高优先级以初始化旋转惯性。当您选择 **Model inertia** 并将 **Translational connections** 设置为 `Conserving` 时，请在 **Initial Targets** 部分设置初始平移速度或推力，或将代数链接变量设置为高优先级以初始化平移质量。

**注意**

对于旋转守恒连接，模块记录 `Q`（气动扭矩）和 `Inertia.t`。

对于平移守恒连接，模块记录 `thrust`（气动推力）和 `mass.f`。

您可以使用 Ideal Torque Sensor 或 Ideal Force Sensor 模块来分别记录惯性与气动扭矩或力之和。

### 假设和限制

- 该模块将流体速度视为时间上的准稳态。流体均匀地流过螺旋桨。
- 该模块仅考虑穿过螺旋桨的轴向流。
- 当将 **Parameterization** 设置为
  `Polynomial fit` 时，该模块假设螺旋桨功率和推力系数与第一象限对称。
- 当将 **Parameterization** 设置为
  `Tabulated data for advance ratio` 时，该模块假设功率和推力系数在第一和第三象限以及第二和第四象限中相同。
  如果 *J* 的所有元素均为正，则该模块假设所有象限中的系数均与第一象限对称。
- 当将 **Parameterization** 设置为
  `Tabulated data for advance angle` 时，该模块移除 *Va* 的符号。要获得负推力和扭矩，必须在 *CT* 和 *CQ* 的值中包含符号。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，
请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。
基于标称值使用系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
