---
type: simulink-block
title: 'Combined Slip Wheel 2DOF'
family: 'wheels-and-tires'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'combinedslipwheel2dof'
documentation_source_path: 'ref/combinedslipwheel2dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Combined Slip Wheel 2DOF

## 端口

### 输入

### **BrkPrs** — 制动压力 scalar | *N*-by-`1` vector

制动压力，单位为 Pa。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

#### 依赖关系

要启用此端口，请将 **Brake Type** 参数设置为以下类型之一：

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — 车轴转矩 scalar | *N*-by-`1` vector

车轴转矩，*Ta*，绕车轮旋转轴，单位为 N·m。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Vx** — 车轴纵向速度 scalar | *N*-by-`1` vector

车轴纵向速度，*Vx*，沿轮胎固定的 *x* 轴，单位为 m/s。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Vy** — 车轴横向速度 scalar | *N*-by-`1` vector

车轴横向速度，*Vy*，沿轮胎固定的 *y* 轴，单位为 m/s。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Camber** — 外倾角 scalar | *N*-by-`1` vector

外倾角，*ɣ*，或倾角，*ε*，单位为 rad。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **YawRate** — 轮胎角速度 scalar | *N*-by-`1` vector

轮胎角速度，*r*，绕轮胎固定的 *z* 轴（横摆角速度），单位为 rad/s。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Prs** — 轮胎充气压力 scalar | *N*-by-`1` vector

轮胎充气压力，*pi*，单位为 Pa。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Gnd** — 地面位移 scalar | *N*-by-`1` vector

沿轮胎固定的 *z* 轴的地面位移，单位为 m。正输入产生车轮抬升。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Fext** — 施加到轮胎的车轴力 scalar | *N*-by-`1` vector

施加到轮胎的车轴力，*Fext*，沿车辆固定的 *z* 轴（正输入压缩轮胎），单位为 N。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `None` 或 `Magic Formula`。

### **RadialDeflct** — 轮胎径向变形 scalar | *N*-by-`1` vector

轮胎径向变形，*RadialDeflct*，单位为 m。此值将用于所有依赖变形的内部相关 magic formula 方程。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

#### 依赖关系

要启用此端口，请将 **Vertical Motion** 设置为 `External Deflection`。

### **ScaleFctrs** — 比例因子 `27`-by-`N` array

Magic Formula 6.2 比例因子数组。数组维度为 `27` × 车轮数 *N*。

Magic Formula 6.2 方程使用比例因子来考虑静态或仿真运行时变化。名义上，大多数设置为 `1`。

| 数组元素 | 变量 | 比例因子 |
| --- | --- | --- |
| `ScaleFctrs(1,1)` | `lam_Fzo` | 名义载荷 |
| `ScaleFctrs(2,1)` | `lam_mux` | 纵向峰值摩擦系数 |
| `ScaleFctrs(3,1)` | `lam_muy` | 横向峰值摩擦系数 |
| `ScaleFctrs(4,1)` | `lam_muV` | 滑移速度 *Vs* 衰减摩擦 |
| `ScaleFctrs(5,1)` | `lam_Kxkappa` | 制动滑移刚度 |
| `ScaleFctrs(6,1)` | `lam_Kyalpha` | 侧偏刚度 |
| `ScaleFctrs(7,1)` | `lam_Cx` | 纵向形状因子 |
| `ScaleFctrs(8,1)` | `lam_Cy` | 横向形状因子 |
| `ScaleFctrs(9,1)` | `lam_Ex` | 纵向曲率因子 |
| `ScaleFctrs(10,1)` | `lam_Ey` | 横向曲率因子 |
| `ScaleFctrs(11,1)` | `lam_Hx` | 纵向水平偏移 |
| `ScaleFctrs(12,1)` | `lam_Hy` | 横向水平偏移 |
| `ScaleFctrs(13,1)` | `lam_Vx` | 纵向垂直偏移 |
| `ScaleFctrs(14,1)` | `lam_Vy` | 横向垂直偏移 |
| `ScaleFctrs(15,1)` | `lam_Kygamma` | 外倾力刚度 |
| `ScaleFctrs(16,1)` | `lam_Kzgamma` | 外倾扭矩刚度 |
| `ScaleFctrs(17,1)` | `lam_t` | 气胎拖距（影响回正力矩刚度） |
| `ScaleFctrs(18,1)` | `lam_Mr` | 残余扭矩 |
| `ScaleFctrs(19,1)` | `lam_xalpha` | Alpha 对 *Fx* 的影响（kappa） |
| `ScaleFctrs(20,1)` | `lam_ykappa` | Kappa 对 *Fy* 的影响（alpha） |
| `ScaleFctrs(21,1)` | `lam_Vykappa` | 诱导帘布层转向 *Fy* |
| `ScaleFctrs(22,1)` | `lam_s` | *Fx* 的力臂 |
| `ScaleFctrs(23,1)` | `lam_Cz` | 径向轮胎刚度 |
| `ScaleFctrs(24,1)` | `lam_Mx` | 倾覆力偶刚度 |
| `ScaleFctrs(25,1)` | `lam_VMx` | 倾覆力偶垂直偏移 |
| `ScaleFctrs(26,1)` | `lam_My` | 滚动阻力矩 |
| `ScaleFctrs(27,1)` | `lam_Mphi` | 驻车扭矩 *Mz* |

### 输出

### **Info** — 模块数据总线

模块数据，作为包含这些模块值的总线信号返回。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `AxlTrq` | 绕车轮固定的 *y* 轴的车轴转矩 | N·m |
| `Omega` | 绕车轮固定的 *y* 轴的车轮角速度 | rad/s |
| `Fx` | 沿轮胎固定的 *x* 轴的车辆纵向力 | N |
| `Fy` | 沿轮胎固定的 *y* 轴的车辆横向力 | N |
| `Fz` | 沿轮胎固定的 *z* 轴的车辆垂向力 | N |
| `Mx` | 绕轮胎固定的 *x* 轴的倾覆力矩 | N·m |
| `My` | 绕轮胎固定的 *y* 轴的滚动阻力矩 | N·m |
| `Mz` | 绕轮胎固定的 *z* 轴的回正力矩 | N·m |
| `Vx` | 沿轮胎固定的 *x* 轴的车辆纵向速度 | m/s |
| `Vy` | 沿轮胎固定的 *y* 轴的车辆横向速度 | m/s |
| `Re` | 承载有效半径 | m |
| `Kappa` | 纵向滑移率 | NA |
| `Alpha` | 侧偏角 | rad |
| `a` | 接地面半长 | m |
| `b` | 接地面半宽 | m |
| `RL` | 承载半径 | m |
| `RadialDeflct` | 轮胎径向变形 | m |
| `WhlTrq` | 车轮扭矩 | N·m |
| `Gamma` | 外倾角 | rad |
| `psidot` | 绕轮胎固定的 *z* 轴的轮胎角速度（横摆角速度） | rad/s |
| `BrkTrq` | 绕车辆固定的 *y* 轴的制动力矩 | N·m |
| `BrkPrs` | 制动压力 | Pa |
| `z` | 沿轮胎固定的 *z* 轴的车轴局部垂向位移 | m |
| `zdot` | 沿轮胎固定的 *z* 轴的车轴垂向速度 | m/s |
| `Gnd` | 沿轮胎固定的 *z* 轴的地面位移（正输入产生车轮抬升） | m |
| `GndFz` | 沿轮胎固定的 *z* 轴作用在地面上的垂向胎侧力 | N |
| `Prs` | 轮胎充气压力 | Pa |

### **Omega** — 车轮角速度 scalar | *N*-by-`1` vector

车轮角速度，*ω*，绕车轮固定的 *y* 轴，单位为 rad/s。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Fx** — 车轴纵向力 scalar | *N*-by-`1` vector

作用在车轴上的纵向力，*Fx*，沿轮胎固定的 *x* 轴，单位为 N。正力用于使车辆向前运动。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Fy** — 车轴横向力 scalar | *N*-by-`1` vector

作用在车轴上的横向力，*Fy*，沿轮胎固定的 *y* 轴，单位为 N。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Fz** — 车轴垂向力 scalar | *N*-by-`1` vector

作用在车轴上的垂向力，*Fz*，沿轮胎固定的 *z* 轴，单位为 N。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Mx** — 倾覆力矩 scalar | *N*-by-`1` vector

作用在车轴上的纵向力矩，*Mx*，绕轮胎固定的 *x* 轴，单位为 N·m。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **My** — 滚动阻力矩 scalar | *N*-by-`1` vector

作用在车轴上的横向力矩，*My*，绕轮胎固定的 *y* 轴，单位为 N·m。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

### **Mz** — 回正力矩 scalar | *N*-by-`1` vector

作用在车轴上的垂向力矩，*Mz*，绕轮胎固定的 *z* 轴，单位为 N·m。

向量为车轮数 *N* × `1`。如果提供标量值，模块假定车轮数为 1。

## 参数

### 轮胎选项

### **Tire type** — 选择类型 `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 导入自己的包含 Magic Formula 系数的外部文件，并使用它们驱动对轮胎 1 和 2 建模的经验方程。导入的文件可以是 .mat、.tir 或 .txt 类型，并且必须包含与轮胎模块中参数对应的参数名。 | 使用文件中的拟合系数更新模块参数：  1. 将 **Tire type** 设置为 `External    file`。 2. 在 **Wheel and Tire Parameters** > **External    tire source** 窗格中，选择 **Select file**。 3. 选择轮胎系数文件。 4. 选择 **Update mask values from file**。在提示确认的对话框中，点击 **OK**。模块将更新参数。 5. 选择 **Apply**。 |
| 选择其中一个 Magic Formula 内置轮胎模型来驱动对轮胎 1 和 2 建模的经验方程。 | 使用内置轮胎模型中的值更新适用的模块参数：  1. 将 **Tire type** 设置为要实现的轮胎。选项包括：  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 选择 **Update block with applicable tire    values**。在 **Tire    Parameters** 选项卡上，模块将更新适用参数，包括 **Tire nominal    section width**、**Rim    radius** 和 **Tire mass**。 3. 选择 **Apply**。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireType` |
| **值：** | `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **数据类型：** | `character vector` |

### **Tire file or object, tireParamSet** — 轮胎文件 `vdynPassCar.mat` (default) | `.tir` | `.txt`

轮胎文件 `.tir` 或对象，包含用于通过 Magic Formula 对轮胎纵向和横向行为建模的经验数据。如果提供 `.txt` 文件，请确保该文件包含与模块参数对应的名称。

使用文件中的拟合系数更新模块参数：

1. 将 **Tire type** 设置为 `External file`。
2. 在 **Wheel and Tire Parameters** > **External tire source** 窗格中，选择 **Select file**。
3. 选择轮胎系数文件。
4. 选择 **Update mask values from file**。在提示确认的对话框中，点击 **OK**。模块将更新参数。
5. 选择 **Apply**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireParamSet` |
| **值：** | `vdynPassCar.mat` (default) | `.tir` | `.txt` |
| **数据类型：** | `character vector` |

### **Vertical Motion** — 垂向运动模型 `Magic Formula` (default) | `None` | `External deflection`

垂向运动类型。默认情况下，模块使用 Magic Formula 计算轮胎的垂向运动。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `vertType` |
| **值：** | `Magic Formula` (default) | `None` | `External deflection` |
| **数据类型：** | `character vector` |

### **Ply steer** — 包括帘布层转向 `on` (default) | `off`

选择以在 Magic Formula 6.2 方程中包括帘布层转向。

默认情况下，模块在 Magic Formula 6.2 方程中包括帘布层转向和转弯滑移。这些方程拟合到平带测试数据，并预测多种轮胎效应，包括帘布层转向和转弯滑移。如果满足以下情况，请考虑移除此类效应：

- 测试数据不包括帘布层转向或转弯滑移数据。
- 分析不需要帘布层转向或转弯滑移效应。

如果清除 **Ply steer**，模块会在内部将这些参数设置为 0：

- **Vertical shift of overturning moment, QSX1**
- **Combined slip Fx shift factor reduction, RHX1**
- **Efy curvature constant camber dependency, PEY3**
- **SHY horizontal shift at FZNOM, PHY1**
- **SHY variation with load, PHY2**
- **Svy/Fz vertical shift at FZNOM, PVY1**
- **Svy/Fz variation with load, PVY2**
- **Fy shift reduction with slip angle, RBY3**
- **Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1**
- **Side force Svyk/Muy\*Fz variation with load, RVY2**
- **Bpt slope variation with camber, QBZ4**
- **Dpt peak trail variation with camber, QDZ3**
- **Dmr peak residual torque, QDZ6**
- **Dmr peak residual torque variation with load, QDZ7**
- **Ept variation with sign of alpha-t, QEZ4**
- **Sht horizontal trail shift at FZNOM, QHZ1**
- **Sht variation with load, QHZ2**
- **Nominal value of s/R0: effect of Fx on Mz, SSZ1**

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `plySteer` |
| **值：** | `on` (default) | `off` |
| **数据类型：** | `character vector` |

### **Turn slip** — 包括转弯滑移 `on` (default) | `off`

选择以在 Magic Formula 6.2 方程中包括帘布层转向。

默认情况下，模块在 Magic Formula 6.2 方程中包括帘布层转向和转弯滑移。这些方程拟合到平带测试数据，并预测多种轮胎效应，包括帘布层转向和转弯滑移。如果满足以下情况，请考虑移除此类效应：

- 测试数据不包括帘布层转向或转弯滑移数据。
- 分析不需要帘布层转向或转弯滑移效应。

如果清除 **Turn slip**，模块会在内部：

- 将 Magic Formula 转弯滑移方程设置为 1。具体来说，方程 4.E77、4.E79、4.E81、4.E83、4.E84、4.E92、4.E102、4.E101 和 4.E1052。
- 使用影响水平偏移的 Magic Formula 项。
- 在 4.E272 中使用 Magic Formula 小转弯滑移值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `turnslip` |
| **值：** | `on` (default) | `off` |
| **数据类型：** | `character vector` |

### **Brake type** — 制动类型 `None` | `Disc` | `Drum` | `Mapped`

使用 **Brake Type** 参数选择制动器。

| 操作 | Brake Type 设置 |
| --- | --- |
| 不制动 | `None` |
| 实现将制动缸压力转换为制动力的制动器 | `Disc` |
| 实现将施加力和制动器几何形状转换为净制动转矩的简单鼓式制动器 | `Drum` |
| 实现作为车轮转速和施加制动压力的函数的查找表 | `Mapped` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BrakeType` |
| **值：** | `None` | `Disc` | `Drum` | `Mapped` |
| **数据类型：** | `character vector` |

### 绘图

### **Install Extended Tire Features** — 用于安装 Extended Tire Features for Vehicle Dynamics Blockset™ 支持包的选项按钮

点击 **Install Extended Tire Features** 以安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包。使用该支持包，您可以从 Combined Slip Wheel 2DOF Block Parameters 对话框中绘制稳态力和力矩轮胎响应。

### **Plot steady state force, moment response** — 用于绘制稳态力和力矩轮胎响应的选项按钮

点击 **Plot steady state force, moment response** 生成以下绘图：

- **侧向力 [N] vs 侧偏角 [rad]**
- **回正力矩 [Nm] vs 侧偏角 [rad]**
- **纵向力 [N] vs 纵向滑移 []**
- **纵向力 [N] vs 侧向力 [N]**

#### 依赖关系

要启用此参数，请点击 **Install Extended Tire Features**。

### Brake

### **Static friction coefficient, mu\_static** — 静态摩擦系数 `0.3`（默认） | scalar | *N*-by-`1` vector

静态摩擦系数，指定为 scalar 或 *N*-by-`1` vector，无量纲。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`、`Drum` 或 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_static` |
| **值：** | `0.3`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

### **Kinetic friction coefficient, mu\_kinetic** — 动摩擦系数 `0.2`（默认） | scalar | *N*-by-`1` vector

运动学摩擦系数，指定为 scalar 或 *N*-by-`1` vector，无量纲。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`、`Drum` 或 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_kinetic` |
| **值：** | `0.2`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

#### Disc

### **Disc brake actuator bore, disc\_abore** — 孔径距离 `0.05`（默认） | scalar | *N*-by-`1` vector

盘式制动器执行器孔径，指定为 scalar 或 *N*-by-`1` vector，单位为 m。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `disc_abore` |
| **值：** | `0.05`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

### **Brake pad mean radius, Rm** — 半径 `0.177`（默认） | scalar | *N*-by-`1` vector

制动衬块平均半径，指定为 scalar 或 *N*-by-`1` vector，单位为 m。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rm` |
| **值：** | `0.177`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

### **Number of brake pads, num\_pads** — 制动衬块数量 `2`（默认） | scalar | *N*-by-`1` vector

制动衬块数量，指定为 scalar 或 *N*-by-`1` vector，无量纲。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `num_pads` |
| **值：** | `2`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

#### Drum

### **Drum brake actuator bore, drum\_abore** — 孔径距离 `0.0508`（默认） | scalar | *N*-by-`1` vector

鼓式制动器执行器孔径，指定为 scalar 或 *N*-by-`1` vector，单位为 m。如果指定 scalar，则模块将该值用于所有车轮。如果指定 vector，则必须为其他制动参数指定 vectors。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_abore` |
| **值：** | `0.0508`（默认） | scalar | *N*-by-`1` vector |
| **数据类型：** | `double` |

### **Shoe pin to drum center distance, drum\_a** — 制动蹄销到制动鼓中心距离 `0.123`（默认） | scalar

制动蹄销到制动鼓中心距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_a` |
| **值：** | `0.123`（默认） | scalar |
| **数据类型：** | `double` |

### **Shoe pin center to force application point distance, drum\_c** — 制动蹄销中心到力作用点距离 `0.212`（默认） | scalar

制动蹄销中心到力作用点距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_c` |
| **值：** | `0.212`（默认） | scalar |
| **数据类型：** | `double` |

### **Drum internal radius, drum\_r** — 制动鼓内半径 `0.15`（默认） | scalar

制动鼓内半径，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_r` |
| **值：** | `0.15`（默认） | scalar |
| **数据类型：** | `double` |

### **Shoe pin to pad start angle, drum\_theta1** — 制动蹄销到衬块起始角度 `0`（默认） | scalar

制动蹄销到衬块起始角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta1` |
| **值：** | `0`（默认） | scalar |
| **数据类型：** | `double` |

### **Shoe pin to pad end angle, drum\_theta2** — 制动蹄销到衬块终止角度 `126`（默认） | scalar

制动蹄销到衬块终止角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta2` |
| **值：** | `126`（默认） | scalar |
| **数据类型：** | `double` |

#### Mapped

### **Brake actuator pressure breakpoints, brake\_p\_bpt** — 制动执行器压力断点 vector

制动执行器压力断点，单位为 bar。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_p_bpt` |
| **值：** | vector |
| **数据类型：** | `double` |

### **Wheel speed breakpoints, brake\_n\_bpt** — 车轮转速断点 vector

车轮转速断点，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_n_bpt` |
| **值：** | vector |
| **数据类型：** | `double` |

### **Brake torque map, f\_brake\_t** — 用于制动转矩数组的查找表

制动转矩的查找表 fbrake(P,N) 是施加制动压力和车轮转速的函数，其中：

- *T* 是制动转矩，单位为 N·m。
- *P* 是施加制动压力，单位为 bar。
- *N* 是车轮转速，单位为 rpm。

显示制动转矩随车轮转速和施加制动压力变化的图

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_brake_t` |
| **值：** | vector |
| **数据类型：** | `double` |

### 仿真

### **Nominal pressure, NOMPRES** — 压力 scalar

标称压力，*NOMPRES*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NOMPRES` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Maximum pressure, PRESMAX** — 最大压力 scalar

最大压力，*PRESMAX*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMAX` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Minimum pressure, PRESMIN** — 最小压力 scalar

最小压力，*PRESMIN*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Nominal normal force, FNOMIN** — 力 scalar

标称法向力，*FNOMIN*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FNOMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Maximum normal force, FZMAX** — 力 scalar

最大法向力，*FZMAX*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMAX` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Minimum normal force, FZMIN** — 力 scalar

最小法向力，*FZMIN*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — 容差 scalar

用于处理低速情况的速度容差，*VXLOW*，单位为 m/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VXLOW` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — 最大允许滑移率 scalar

最大允许滑移率（绝对值），*KPUMAX*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMAX` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — 最小允许滑移率 scalar

最小允许滑移率（绝对值），*KPUMIN*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — 最大允许侧偏角 scalar

最大允许侧偏角（绝对值），*ALPMAX*，单位为 rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMAX` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — 最小允许侧偏角 scalar

最小允许侧偏角（绝对值），*ALPMIN*，单位为 rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Maximum allowable camber angle, CAMMAX** — 最大允许外倾角标量

最大允许外倾角 *CAMMAX*，单位为 rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CAMMAX` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Minimum allowable camber angle, CAMMIN** — 最小允许外倾角标量

最小允许外倾角，*CAMMIN*，单位为 rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CAMMIN` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Nominal longitudinal speed, LONGVL** — 速度标量

名义纵向速度，*LONGVL*，单位为 m/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LONGVL` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Initial wheel rotational velocity, omegao** — 初始车轮旋转速度标量 | *N*-by-`1` 向量

初始车轮旋转速度，指定为标量或 *N*-by-`1` 向量，单位为 rad/s。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omegao` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### 尺寸

### **Tire unloaded radius, UNLOADED\_RADIUS** — 半径标量

轮胎未加载半径，*UNLOADED\_RADIUS*，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `UNLOADED_RADIUS` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Tire nominal section width, WIDTH** — 轮胎名义断面宽度标量

轮胎名义断面宽度，*WIDTH*，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `WIDTH` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Rim radius, RIM\_RADIUS** — 半径标量

轮辋半径，*RIM\_RADIUS*，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RIM_RADIUS` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Nominal aspect ratio, ASPECT\_RATIO** — 比值标量

名义高宽比，*ASPECT\_RATIO*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ASPECT_RATIO` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### 惯性与阻尼

### **Tire mass, MASS** — 质量标量 | *N*-by-`1` 向量

轮胎质量，指定为标量或 *N*-by-`1` 向量，单位为 kg。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他惯性参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Magic Formula`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `MASS` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — 轮胎转动惯量标量 | *N*-by-`1` 向量

轮胎转动惯量（滚动轴），指定为标量或 *N*-by-`1` 向量，单位为 kg·m2。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `IYY` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### **Rotational damping, br** — 旋转阻尼标量 | *N*-by-`1` 向量

旋转阻尼，指定为标量或 *N*-by-`1` 向量，单位为 N·m·s/rad。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `br` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### **Gravity, GRAVITY** — 重力标量

重力，*GRAVITY*，单位为 m/s^2。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Magic Formula`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `GRAVITY` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### 垂直

### **Initial tire displacement, zo** — 位移标量 | *N*-by-`1` 向量

初始轮胎位移，指定为标量或 *N*-by-`1` 向量，单位为 m。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他垂直参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `zo` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — 速度标量 | *N*-by-`1` 向量

初始车轮垂直速度，指定为标量或 *N*-by-`1` 向量，单位为 m/s。如果指定标量，模块会将该值用于所有车轮。如果指定向量，则必须为其他垂直参数指定向量。

*N* 是车轮数量，并且必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `zdoto` |
| **值:** | 标量 | *N*-by-`1` 向量 |
| **数据类型:** | `double` |

### **Effective rolling radius at low load stiffness, BREFF** — 刚度标量

低载荷刚度下的有效滚动半径，*BREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BREFF` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Effective rolling radius peak value, DREFF** — 半径标量

有效滚动半径峰值，*DREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `DREFF` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Effective rolling radius at high load stiffness, FREFF** — 半径标量

高载荷刚度下的有效滚动半径，*FREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FREFF` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Unloaded to nominal rolling radius ratio, Q\_RE0** — 比值标量

未加载与名义滚动半径之比，*Q\_RE0*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_RE0` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Radius rotational speed dependence, Q\_V1** — 速度标量

滚动半径的转速依赖性，*Q\_V1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_V1` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Stiffness rotational speed dependence, Q\_V2** — 速度标量

刚度的转速依赖性，*Q\_V2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_V2` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Linear load change with deflection, Q\_FZ1** — 载荷变化 `scalar`

线性载荷随变形量变化，*Q\_FZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FZ1` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Quadratic load change with deflection, Q\_FZ2** — 载荷变化标量

二次载荷随变形量变化，*Q\_FZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FZ2` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Linear load change with deflection and quadratic camber, Q\_FZ3** — 载荷变化标量

随变形量和二次外倾角的线性载荷变化，*Q\_FZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FZ3` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Load response to longitudinal force, Q\_FCX** — 力标量

载荷对纵向力的响应，*Q\_FCX*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FCX` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Load response to lateral force, Q\_FCY** — 力标量

载荷对侧向力的响应，*Q\_FCY*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FCY` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Vertical stiffness change due to lateral load dependency on lateral stiffness, Q\_FCY2** — 刚度标量

由于侧向载荷对侧向刚度的依赖性引起的垂直刚度变化，*Q\_FCY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_FCY2` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Stiffness response to pressure, PFZ1** — 刚度 `0.7098`（默认） | `scalar`

刚度对压力的响应，*PFZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PFZ1` |
| **值:** | `0.7098`（默认） | `scalar` |
| **数据类型:** | `double` |

### **Vertical tire stiffness, VERTICAL\_STIFFNESS** — 刚度标量

垂直轮胎刚度，*VERTICAL\_STIFFNESS*，单位为 N/m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VERTICAL_STIFFNESS` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Vertical tire damping, VERTICAL\_DAMPING** — 阻尼标量

垂直轮胎阻尼，*VERTICAL\_DAMPING*，单位为 N·s/m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `VERTICAL_DAMPING` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Rim bottoming out offset, BOTTOM\_OFFST** — 偏移标量

轮辋触底偏移量，*BOTTOM\_OFFST*，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BOTTOM_OFFST` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Bottoming out stiffness, BOTTOM\_STIFF** — 刚度标量

触底刚度，*BOTTOM\_STIFF*，单位为 N/m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BOTTOM_STIFF` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Linear load dependent camber angle effect on vertical stiffness, Q\_CAM1** — 刚度标量

线性载荷相关的外倾角对垂直刚度的影响，*Q\_CAM1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Q_CAM1` |
| **值:** | 标量 |
| **数据类型:** | `double` |

### **Quadratic load dependent camber angle effect on vertical stiffness, Q\_CAM2** — 刚度标量

二次载荷相关的外倾角对垂直刚度的影响，*Q\_CAM2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **刚度随载荷和外倾角的线性降低，Q\_CAM3** — 刚度标量

刚度随载荷和外倾角的线性降低，*Q\_CAM3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾角和侧偏角对垂直刚度的恒定影响，Q\_FYS1** — 刚度标量

外倾角和侧偏角对垂直刚度的恒定影响，*Q\_FYS1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾角和侧偏角对垂直刚度的线性影响，Q\_FYS2** — 刚度标量

外倾角和侧偏角对垂直刚度的线性影响，*Q\_FYS2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾角和侧偏角对垂直刚度的二次影响，Q\_FYS3** — 刚度标量

外倾角和侧偏角对垂直刚度的二次影响，*Q\_FYS3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 结构

### **纵向刚度，LONGITUDINAL\_STIFFNESS** — 刚度标量

纵向刚度，*LONGITUDINAL\_STIFFNESS*，单位为 N/m。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LONGITUDINAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **横向刚度，LATERAL\_STIFFNESS** — 刚度标量

横向刚度，*LATERAL\_STIFFNESS*，单位为 N/m。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LATERAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直变形对纵向刚度的线性影响，PCFX1** — 变形影响标量

垂直变形对纵向刚度的线性影响，*PCFX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直变形对纵向刚度的二次影响，PCFX2** — 变形影响标量

垂直变形对纵向刚度的二次影响，*PCFX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向刚度的压力依赖性，PCFX3** — 压力依赖性标量

纵向刚度的压力依赖性，*PCFX3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直变形对横向刚度的线性影响，PCFY1** — 变形影响标量

垂直变形对横向刚度的线性影响，*PCFY1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直变形对横向刚度的二次影响，PCFY2** — 变形影响标量

垂直变形对横向刚度的二次影响，*PCFY2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **横向刚度的压力依赖性，PCFY3** — 压力依赖性标量

横向刚度的压力依赖性，*PCFY3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 接触印迹

### **接触长度平方根项，Q\_RA1** — 长度项标量

接触长度平方根项，*Q\_RA1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触长度线性项，Q\_RA2** — 长度项标量

接触长度线性项，*Q\_RA2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触宽度根项，Q\_RB1** — 宽度项标量

接触宽度根项，*Q\_RB1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触宽度线性项，Q\_RB2** — 宽度项标量

接触宽度线性项，*Q\_RB2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 纵向

### **Cfx 形状因子，PCX1** — 形状因子标量

形状因子，*Cfx*，*PCX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向摩擦，PDX1** — 摩擦标量

名义法向载荷下的纵向摩擦，*PDX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **摩擦随载荷的变化，PDX2** — 摩擦变化标量

摩擦随载荷的变化，*PDX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **摩擦随外倾角的变化，PDX3** — 摩擦变化标量

摩擦随外倾角的变化，*PDX3*，单位为 1/rad^2。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向曲率，PEX1** — 曲率标量

名义法向载荷下的纵向曲率，*PEX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷的变化，PEX2** — 曲率变化标量

曲率因子随载荷的变化，*PEX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷平方的变化，PEX3** — 曲率变化标量

曲率因子随载荷平方的变化，*PEX3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **随滑移的纵向曲率因子，PEX4** — 曲率标量

随滑移的纵向曲率因子，*PEX4*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向滑移刚度，PKX1** — 刚度标量

名义法向载荷下的纵向滑移刚度，*PKX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度随载荷的变化，PKX2** — 刚度变化标量

滑移刚度随载荷的变化，*PKX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度指数因子，PKX3** — 滑移刚度标量

滑移刚度指数因子，*PKX3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下滑移率的水平偏移，PHX1** — 滑移率偏移标量

名义法向载荷下滑移率的水平偏移，*PHX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **水平滑移率随载荷的变化，PHX2** — 滑移变化标量

水平滑移率随载荷的变化，*PHX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下载荷的垂直偏移，PVX1** — 载荷偏移标量

名义法向载荷下载荷的垂直偏移，*PVX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直偏移随载荷的变化，PVX2** — 载荷变化标量

垂直偏移随载荷的变化，*PVX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向滑移刚度随轮胎压力的线性变化，PPX1** — 刚度变化标量

纵向滑移刚度随轮胎压力的线性变化，*PPX1*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向滑移刚度随轮胎压力的二次变化，PPX2** — 刚度变化标量

纵向滑移刚度随轮胎压力的二次变化，*PPX2*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **峰值纵向摩擦随轮胎压力的线性变化，PPX3** — 摩擦变化标量

峰值纵向摩擦随轮胎压力的线性变化，*PPX3*，无量纲。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **峰值纵向摩擦随轮胎压力的二次变化，PPX4** — 摩擦变化标量

峰值纵向摩擦随轮胎压力的二次变化，*PPX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **复合滑移 Fx 斜率因子降低，RBX1** — 复合滑移纵向力斜率因子降低标量

复合滑移纵向力，*Fx*，斜率因子降低，*RBX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移率 Fx 斜率降低变化，RBX2** — 滑移率纵向力斜率降低变化标量

滑移率纵向力，*Fx*，斜率降低变化，*RBX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾对复合滑移 Fx 刚度的影响，RBX3** — 外倾对复合滑移纵向力刚度的影响标量

外倾对复合滑移纵向力，*Fx*，刚度的影响，*RBX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **复合滑移 Fx 降低的形状因子，RCX1** — 复合滑移纵向力降低的形状因子标量

复合滑移纵向力，*Fx*，降低的形状因子，*RCX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **复合 Fx 曲率因子，REX1** — 复合纵向力曲率因子标量

复合纵向力，*Fx*，曲率因子，*REX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **带载荷的复合 Fx 曲率因子，REX2** — 复合纵向力曲率因子标量

复合纵向力，*Fx*，带载荷的曲率因子，*REX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **复合滑移 Fx 偏移因子降低，RHX1** — 复合滑移纵向力滑移因子标量

复合滑移纵向力，*Fx*，偏移因子降低，*RHX1*，无量纲。

#### 依赖关系

如果您清除 **Ply steer**，模块将在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 翻转力矩

### **翻转力矩的垂直偏移，QSX1** — 翻转力矩标量

翻转力矩的垂直偏移，*QSX1*，无量纲。

#### 依赖关系

如果您清除 **Ply steer**，模块将在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾引起的翻转力矩，QSX2** — 由外倾引起的翻转力矩标量

由外倾引起的翻转力矩，*QSX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由 Fy 引起的翻转力矩，QSX3** — 由侧向力引起的翻转力矩标量

由侧向力引起的翻转力矩，*QSX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 复合侧向力载荷和外倾，QSX4** — 翻转力矩标量

翻转力矩，*Mx*，复合侧向力载荷和外倾，*QSX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由侧向力和外倾引起的载荷效应，QSX5** — 翻转力矩标量

翻转力矩，*Mx*，由侧向力和外倾引起的载荷效应，*QSX5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由 B 因子引起的载荷效应，QSX6** — 翻转力矩标量

翻转力矩，*Mx*，由 B 因子引起的载荷效应，*QSX6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由外倾和载荷引起，QSX7** — 翻转力矩标量

翻转力矩，*Mx*，由外倾和载荷引起，*QSX7*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由侧向力和载荷引起，QSX8** — 翻转力矩标量

翻转力矩，*Mx*，由侧向力和载荷引起，*QSX8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由侧向力和载荷的 B 因子引起，QSX9** — 翻转力矩标量

翻转力矩，*Mx*，由侧向力和载荷的 B 因子引起，*QSX9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由垂直力和外倾引起，QSX10** — 翻转力矩标量

翻转力矩，*Mx*，由垂直力和外倾引起，*QSX10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由垂直力的 B 因子和外倾引起，QSX11** — 翻转力矩标量

翻转力矩，*Mx*，由垂直力的 B 因子和外倾引起，*QSX11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由外倾平方引起，QSX12** — 翻转力矩标量

翻转力矩，*Mx*，由外倾平方引起，*QSX12*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX12` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由侧向力引起，QSX13** — 翻转力矩标量

翻转力矩，*Mx*，由侧向力引起，*QSX13*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX13` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由带外倾的侧向力引起，QSX14** — 翻转力矩标量

翻转力矩，*Mx*，由带外倾的侧向力引起，*QSX14*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX14` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx 由充气压力引起，PPMX1** — 由压力引起的翻转力矩标量

翻转力矩，*Mx*，由充气压力引起，*PPMX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPMX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 侧向

### **侧向力的 Cfy 形状因子，PCY1** — 侧向力形状因子标量

侧向力的形状因子，*Cfy*，*PCY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向摩擦 muy，PDY1** — 侧向摩擦标量

侧向摩擦，*μy*，*PDY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **muy 随载荷变化的侧向摩擦变化，PDY2** — 侧向摩擦变化标量

侧向摩擦，*μy*，随载荷的变化，*PDY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **muy 随外倾平方变化的侧向摩擦变化，PDY3** — 侧向摩擦变化标量

侧向摩擦，*μy*，随外倾平方的变化，*PDY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **额定力 FZNOM 下的 Efy 侧向曲率，PEY1** — 额定力下的侧向曲率标量

侧向曲率，*Efy*，在额定力，*FZNOM* 下，*PEY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy 曲率随载荷变化，PEY2** — 侧向曲率变化标量

侧向曲率，*Efy*，随载荷的变化，*PEY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy 曲率常数外倾依赖，PEY3** — 侧向曲率常数标量

侧向曲率，*Efy*，常数外倾依赖，*PEY3*，无量纲。

#### 依赖关系

如果您清除 **Ply steer**，模块将在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy 曲率随外倾变化，PEY4** — 侧向曲率变化标量

侧向曲率，*Efy*，随外倾的变化，*PEY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy 曲率随外倾平方变化，PEY5** — 侧向曲率变化标量

侧向曲率，*Efy*，随外倾平方的变化，*PEY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **最大 KFy/FZNOM 刚度，PKY1** — 最大刚度标量

最大侧向力刚度，*KFy*，与额定力，*FZNOM*，之比，*PKY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **最大 KFy/FZNOM 刚度处的载荷，PKY2** — 载荷标量

最大侧向力刚度，*KFy*，与额定力，*FZNOM*，之比处的载荷，*PKY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **KFy/FZNOM 刚度随外倾角的变化，PKY3** — 刚度变化标量

侧向力刚度，*KFy*，相对于名义力，*FZNOM*，随外倾角的刚度变化，*PKY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY3` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **KFy 曲率，PKY4** — 侧向力刚度曲率标量

侧向力刚度，*KFy* 曲率，*PKY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY4` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **峰值刚度随外倾角平方的变化，PKY5** — 刚度变化标量

峰值刚度随外倾角平方的变化，*PKY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY5` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 外倾刚度因子，PKY6** — 侧向力外倾刚度因子标量

侧向力，*Fy*，外倾刚度因子，*PKY6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY6` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **外倾刚度垂向载荷依赖性，PKY7** — 刚度标量

外倾刚度垂向载荷依赖性，*PKY7*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY7` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **SHY 在 FZNOM 处的水平偏移，PHY1** — 名义力处水平偏移标量

水平偏移，*SHY*，在名义力 *FZNOM* 处，*PHY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **SHY 随载荷的变化，PHY2** — 水平偏移变化标量

水平偏移，*SHY*，随载荷的变化，*PHY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 在 FZNOM 处的垂向偏移，PVY1** — 名义力处垂向偏移标量

垂向偏移，*Svy*，在名义力 *FZNOM* 处，*PVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 随载荷的变化，PVY2** — 垂向偏移随载荷变化标量

垂向偏移，*Svy*，随载荷的变化，*PVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 随外倾角的变化，PVY3** — 垂向偏移随外倾角变化标量

垂向偏移，*Svy*，随外倾角的变化，*PVY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY3` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 随载荷和外倾角的变化，PVY4** — 垂向偏移随载荷和外倾角变化标量

垂向偏移，*Svy*，随载荷和外倾角的变化，*PVY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY4` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧偏刚度随充气压力的变化，PPY1** — 刚度随压力变化标量

侧偏刚度随充气压力的变化，*PPY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧偏刚度随充气压力引起的名义载荷依赖性的变化，PPY2** — 刚度随压力变化标量

侧偏刚度随充气压力引起的名义载荷依赖性的变化，*PPY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **峰值侧向摩擦的线性充气压力影响，PPY3** — 压力标量

峰值侧向摩擦的线性充气压力影响，*PPY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY3` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **峰值侧向摩擦的二次充气压力影响，PPY4** — 压力标量

峰值侧向摩擦的二次充气压力影响，*PPY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY4` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **充气压力对外倾刚度的影响，PPY5** — 压力标量

充气压力对外倾刚度的影响，*PPY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY5` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **组合 Fy 降低斜率因子，RBY1** — 组合侧向力降低斜率因子标量

组合侧向力，*Fy*，降低斜率因子，*RBY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 斜率随侧偏角的降低，RBY2** — 侧向力斜率随侧偏角降低标量

侧向力，*Fy*，斜率随侧偏角的降低，*RBY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 偏移随侧偏角的降低，RBY3** — 侧向力偏移随侧偏角降低标量

侧向力，*Fy*，偏移随侧偏角的降低，*RBY3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY3` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 来自外倾角的组合刚度变化，RBY4** — 侧向力组合刚度来自外倾角变化标量

侧向力，*Fy*，来自外倾角的组合刚度变化，*RBY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY4` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 组合降低形状因子，RCY1** — 侧向力组合降低形状因子标量

侧向力，*Fy*，组合降低形状因子，*RCY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 组合曲率因子，REY1** — 侧向力组合曲率因子标量

侧向力，*Fy*，组合曲率因子，*REY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 随载荷的组合曲率因子，REY2** — 侧向力随载荷组合曲率因子标量

侧向力，*Fy*，随载荷的组合曲率因子，*REY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 组合降低偏移因子，RHY1** — 侧向力组合降低偏移因子标量

侧向力，*Fy*，组合降低偏移因子，*RHY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 随载荷的组合降低偏移因子，RHY2** — 侧向力随载荷组合降低偏移因子标量

侧向力，*Fy*，随载荷的组合降低偏移因子，*RHY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **名义力 FZNOM 处的滑移率侧向力 Svyk/Muy\*Fz，RVY1** — 名义力处滑移率侧向力标量

名义力 *FZNOM* 处的滑移率侧向力，*RVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY1` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随载荷的变化，RVY2** — 侧向力随载荷变化标量

侧向力随载荷的变化，*RVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在内部将 Magic Formula 方程中的此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY2` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随外倾角的变化，RVY3** — 侧向力随外倾角变化标量

侧向力随外倾角的变化，*RVY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY3` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随侧偏角的变化，RVY4** — 侧向力随侧偏角变化标量

侧向力随侧偏角的变化，*RVY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY4` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随滑移率的变化，RVY5** — 侧向力随滑移率变化标量

侧向力随滑移率的变化，*RVY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY5` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随滑移率反正切的变化，RVY6** — 侧向力随滑移率反正切变化标量

侧向力随滑移率反正切的变化，*RVY6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY6` |
| **取值：** | 标量 |
| **数据类型：** | `double` |

### 滚动

### **阻力矩系数，QSY1** — 阻力矩标量

阻力矩系数，*QSY1*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由 Fx 引起的阻力矩，QSY2** — 纵向力引起的阻力矩标量

纵向力引起的阻力矩，*Fx*，*QSY2*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由速度引起的阻力矩，QSY3** — 速度引起的阻力矩标量

速度引起的阻力矩，*QSY3*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由速度^4 引起的阻力矩，QSY4** — 速度引起的阻力矩标量

速度^4 引起的阻力矩，*QSY4*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾角平方引起的阻力矩，QSY5** — 外倾角引起的阻力矩标量

外倾角平方引起的阻力矩，*QSY5*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾角平方与载荷引起的阻力矩，QSY6** — 外倾角和载荷引起的阻力矩标量

外倾角平方与载荷引起的阻力矩，*QSY6*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由载荷引起的阻力矩，QSY7** — 载荷引起的阻力矩标量

载荷引起的阻力矩，*QSY7*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由压力引起的阻力矩，QSY8** — 压力引起的阻力矩标量

压力引起的阻力矩，*QSY8*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 回正

### **FZNOM 处拖距 Bpt 的拖距斜率因子，QBZ1** — 名义力处的拖距斜率因子标量

在名义力 *FZNOM* 下，拖距 *Bpt* 的拖距斜率因子，*QBZ1*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt 斜率随载荷的变化，QBZ2** — 随载荷变化的斜率标量

斜率随载荷的变化，*QBZ2*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt 斜率随载荷平方的变化，QBZ3** — 随载荷变化的斜率 `0`（默认）| 标量

斜率随载荷平方的变化，*QBZ3*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt 斜率随外倾角的变化，QBZ4** — 随外倾角变化的斜率标量

斜率随外倾角的变化，*QBZ4*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt 斜率随外倾角绝对值的变化，QBZ5** — 随外倾角变化的斜率标量

斜率随外倾角绝对值的变化，*QBZ5*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt 斜率随外倾角平方的变化，QBZ6** — 随外倾角变化的斜率标量

斜率随外倾角平方的变化，*QBZ6*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mzr 的 Br 斜率缩放因子，QBZ9** — 斜率缩放因子标量

斜率缩放因子，*QBZ9*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mzr 的 Br 侧偏刚度因子，QBZ10** — 侧偏刚度因子标量

*Mzr* 的 *Br* 侧偏刚度因子，*QBZ10*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cpt 气胎拖距形状因子，QCZ1** — 气胎拖距形状因子标量

气胎拖距形状因子，*Cpt*，*QCZ1*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt 峰值拖距，QDZ1** — 峰值拖距标量

峰值拖距，*Dpt*，*QDZ1*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt 峰值拖距随载荷的变化，QDZ2** — 峰值拖距随载荷的变化标量

峰值拖距 *Dpt* 随载荷的变化，*QDZ2*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt 峰值拖距随外倾角的变化，QDZ3** — 峰值拖距随外倾角的变化标量

峰值拖距 *Dpt* 随外倾角的变化，*QDZ3*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt 峰值拖距随外倾角平方的变化，QDZ4** — 峰值拖距随外倾角的变化标量

峰值拖距 *Dpt* 随外倾角平方的变化，*QDZ4*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩，QDZ6** — 峰值残余扭矩标量

峰值残余扭矩，*Dmr*，*QDZ6*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩随载荷的变化，QDZ7** — 峰值残余扭矩随载荷的变化标量

峰值残余扭矩 *Dmr* 随载荷的变化，*QDZ7*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩随外倾角的变化，QDZ8** — 峰值残余扭矩随外倾角的变化标量

峰值残余扭矩 *Dmr* 随外倾角的变化，*QDZ8*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩随外倾角和载荷的变化，QDZ9** — 峰值残余扭矩随外倾角和载荷的变化标量

峰值残余扭矩 *Dmr* 随外倾角和载荷的变化，*QDZ9*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩随外倾角平方的变化，QDZ10** — 峰值残余扭矩随外倾角的变化标量

峰值残余扭矩 *Dmr* 随外倾角平方的变化，*QDZ10*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr 峰值残余扭矩随载荷平方的变化，QDZ11** — 峰值残余扭矩随载荷的变化标量

峰值残余扭矩 *Dmr* 随载荷平方的变化，*QDZ11*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **FZNOM 处的 Ept 拖距曲率，QEZ1** — 名义力处的拖距曲率标量

在名义力 *FZNOM* 下，拖距曲率 *Ept*，*QEZ1*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随载荷的变化，QEZ2** — 拖距曲率随载荷的变化标量

拖距曲率 *Ept* 随载荷的变化，*QEZ2*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随载荷平方的变化，QEZ3** — 拖距曲率随载荷的变化标量

拖距曲率 *Ept* 随载荷平方的变化，*QEZ3*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随 alpha-t 符号的变化，QEZ4** — 拖距曲率变化标量

拖距曲率 *Ept* 随 alpha-t 符号的变化，*QEZ4*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随 alpha-t 符号和外倾角的变化，QEZ5** — 变化标量

拖距曲率 *Ept* 随 alpha-t 符号和外倾角的变化，*QEZ5*，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **FZNOM 处的 Sht 水平拖距偏移，QHZ1** — 名义载荷处的水平拖距偏移标量

在名义载荷 *FZNOM* 下，水平拖距偏移 *Sht*，*QHZ1*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht 随载荷的变化，QHZ2** — 水平拖距偏移随载荷的变化标量

水平拖距偏移 *Sht* 随载荷的变化，*QHZ2*，无量纲。

#### 依赖关系

如果清除 **帘布层转向**，模块会在魔术公式方程内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QHZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht variation with camber, QHZ3** — Horizontal trail shift variation with camber scalar

Horizontal trail shift, *Sht*,
variation with camber, *QHZ3*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QHZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht variation with load and camber, QHZ4** — Horizontal trail shift variation with load and camber scalar

Horizontal trail shift, *Sht*,
variation with load and camber, *QHZ4*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QHZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Inflation pressure influence on trail length, PPZ1** — Pressure influence on trail length scalar

Inflation pressure influence on trail length, *PPZ1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Inflation pressure influence on residual aligning torque, PPZ2** — Pressure influence on aligning torque scalar

Inflation pressure influence on residual aligning torque,
*PPZ2*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal value of s/R0: effect of Fx on Mz, SSZ1** — Effect of longitudinal force on aligning torque scalar

Nominal value of s/R0: effect of longitudinal force,
*Fx*, on aligning torque,
*Mz*, *SSZ1*,
dimensionless.

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将该参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SSZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with lateral to nominal force ratio, SSZ2** — Variation with lateral to nominal force ratio scalar

Variation with lateral to nominal force ratio, *SSZ2*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SSZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with camber, SSZ3** — Variation with camber scalar

Variation with camber, *SSZ3*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SSZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with camber and load, SSZ4** — Variation with camber and load scalar

Variation with camber and load, *SSZ4*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SSZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Turnslip

### **Fx peak reduction due to spin, PDXP1** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin, *PDXP1*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDXP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fx peak reduction due to spin with varying load, PDXP2** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin with varying load, *PDXP2*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDXP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fx peak reduction due to spin with slip ratio, PDXP3** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin with slip ratio, *PDXP3*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDXP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Cornering stiffness reduction due to spin, PKYP1** — Stiffness reduction due to spin scalar

Cornering stiffness reduction due to spin, *PKYP1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PKYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin, PDYP1** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin, *PDYP1*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin with varying load, PDYP2** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin with varying load, *PDYP2*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDYP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin with slip angle, PDYP3** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin with slip angle, *PDYP3*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDYP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to square root of spin, PDYP4** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to square root of spin, *PDYP4*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDYP4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response lateral shift limit, PHYP1** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response lateral shift limit, *PHYP1*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PHYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response max lateral shift limit, PHYP2** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response max lateral shift limit, *PHYP2*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PHYP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response max lateral shift limit with load, PHYP3** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response max lateral shift limit with load, *PHYP3*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PHYP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response lateral shift curvature factor, PHYP4** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response lateral shift curvature factor, *PHYP4*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PHYP4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber stiffness reduction due to spin, PECP1** — Camber stiffness reduction scalar

Camber stiffness reduction due to spin, *PECP1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PECP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber stiffness reduction due to spin with load, PECP2** — Camber stiffness reduction scalar

Camber stiffness reduction due to spin with load, *PECP2*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PECP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip pneumatic trail reduction factor, QDTP1** — Turn slip pneumatic trail reduction factor scalar

Turn slip pneumatic trail reduction factor, *QDTP1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QDTP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn moment for constant turning and zero longitudinal speed, QCRP1** — Turn moment for constant turning scalar

Turn moment for constant turning and zero longitudinal speed,
*QCRP1*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QCRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment increase with spin at 90deg slip angle, QCRP2** — Turn slip moment scalar

Turn slip moment increase with spin at 90-degree slip angle,
*QCRP2*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QCRP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Residual spin torque reduction from side slip, QBRP1** — Residual spin torque reduction scalar

Residual spin torque reduction from side slip, *QBRP1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment peak magnitude, QDRP1** — Turn slip moment peak magnitude scalar

Turn slip moment peak magnitude, *QDRP1*,
dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QDRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment curvature, QDRP2** — Turn slip moment curvature scalar

Turn slip moment curvature, *QDRP2*, dimensionless.

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QDRP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

## 所属库

Vehicle Dynamics Blockset / Wheels and Tires

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：新增 **Tire type** 选项

从 R2024b 开始，您可以指定 **Tire type** 以使用新的内置轮胎模型 `Light passenger car 245/60R16`。

### R2024b：重命名了模块参数

从 R2024b 开始，这些参数已被重命名。

| Old Name | New Name |
| --- | --- |
| **Wheel width** | **Tire nominal section width** |
| **Unloaded radius** | **Tire unloaded radius** |
| **Initial rotational velocity** | **Initial wheel rotational velocity** |
| **Wheel mass** | **Tire mass** |
| **Rotational inertia** | **Tire rotational inertia** |

### R2024b：新增 **Vertical Motion** 选项

从 R2024b 开始，将 **Vertical Motion** 指定为 `External Deflection` 会启用 **RadialDeflct** 端口。当与轮胎连接但在未提供力的情况下，使用此端口定义胎侧变形。

### R2024b：新增信号添加到 **Info** 端口总线

从 R2024b 开始，**Info** 端口总线包含这些新信号。

| Signal | Description |
| --- | --- |
| `RadialDeflct` | Tire radial deflection |
| `RL` | Loaded radius |
| `WhlTrq` | Wheel torque |

### R2024a：绘制稳态力和力矩响应

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，您可以使用新的 **Plot
steady state force, moment response** 按钮来生成绘图。

### R2023a：新增 **Vertical Motion** 参数

从 R2023a 开始，Combined Slip Wheel 2DOF 模块包含 **Vertical
Motion** 参数。默认情况下，Combined Slip Wheel 2DOF 模块使用 Magic
Formula 计算轮胎的垂直运动。

### R2022b：为每个车轮指定制动和轮胎参数

从 R2022b 开始，您可以使用 Combined Slip Wheel 2DOF 模块为车辆上的每个车轮指定制动和轮胎特性。具体来说，该模块允许这些参数使用 *N*×`1` 向量：

- **静摩擦系数，mu\_static**
- **动摩擦系数，mu\_kinetic**
- **盘式制动器执行器缸径，disc\_abore**
- **制动片平均半径，Rm**
- **制动片数量，num\_pads**
- **鼓式制动器执行器缸径，disc\_abore**
- **初始旋转速度，omegao**
- **旋转阻尼，br**
- **车轮质量，MASS**
- **转动惯量（滚动轴），IYY**
- **初始轮胎位移，zo**
- **初始车轮垂向速度（车轮固定坐标系），zdoto**

*N* 是车轮数量，并且必须与输入信号维度匹配。

### R2022b：新增 **Ply steer** 和 **Turn slip** 参数

从 R2022b 开始，Combined Slip Wheel 2DOF 模块包含 **Ply steer** 和 **Turn slip** 参数。要从这些模块的 Magic Formula 实现中移除 ply steer 和 turn slip，请清除 **Ply steer** 和 **Turn slip** 参数。

## 描述

带盘式、鼓式或 mapped 制动的联合滑移 2DOF 车轮

Combined Slip Wheel 2DOF 在纵向和横向联合滑移工况下，集成了车轮运动的两个自由度（DOF），以及轮胎力的 6 个 DOF。

- 车轮运动：绕旋转轴旋转，以及垂直位移。
- 轮胎力和力矩：Fx、Fy 和 Fz；Mx、My 和 Mz。

它使用 Magic Formula 6.2 对轮胎建模。[1] 和 [2] 通过导入您自己的轮胎模型文件，或选择内置轮胎模型之一，来设置 Magic Formula 6.2 系数。

在以下仿真中使用此模块。

- 车辆制动和加速，包括滚动阻力。
- 车辆行驶运动，包括悬架模态的影响。
- 具有联合横向和纵向滑移的操纵，例如车辆横向运动和横摆稳定性。

如果安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则以下附加功能可用：

- 绘图生成 — 点击 **Plot steady state force, moment response** 按钮生成以下图：

  - **横向力 [N] vs 滑移角 [rad]**
  - **回正力矩 [Nm] vs 滑移角 [rad]**
  - **纵向力 [N] vs 纵向滑移 []**
  - **纵向力 [N] vs 横向力 [N]**
- 导入轮胎参数 — 使用 `tireModel.get` 方法将 Combined Slip Wheel 2DOF 模块中定义的轮胎参数值导入到 `tireModel` 对象。
- 导出轮胎参数 — 使用 `set` 方法将轮胎参数值从 `tireModel` 对象导出到 Combined Slip Wheel 2DOF 模块。
- 轮胎模型转换 — 使用 `convert` 方法将以下类型之一的轮胎模型转换为可导入到 Combined Slip Wheel 2DOF 模块的 Magic Formula 6.2 轮胎模型：

  - Magic Formula 5.2
  - Fiala
  - Dugoff

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 导入包含 Magic Formula 系数的您自己的外部文件，并使用它们驱动对轮胎1和2建模的经验方程。您导入的文件可以是 .mat、.tir 或 .txt 类型，并且必须包含与轮胎模块中参数名对应的参数名。 | 使用来自文件的拟合系数更新模块参数：  1. 将 **Tire type** 设置为 `External    file`。  2. 在 **Wheel and Tire Parameters** > **External    tire source** 窗格上，选择 **Select file**。  3. 选择轮胎系数文件。  4. 选择 **Update mask values from file**。在提示您确认的对话框中，点击 **OK**。模块将更新参数。  5. 选择 **Apply**。 |
| 选择一个 Magic Formula 内置轮胎模型，以驱动对轮胎 1 和 2 建模的经验方程。 | 使用内置轮胎模型中的值更新适用的模块参数：  1. 将 **Tire type** 设置为要实现的轮胎。选项包括：  - `Light passenger car      205/60R15`  - `Light passenger car      245/60R16`  - `Mid-size passenger car      235/45R18`  - `Performance car      225/40R19`  - `SUV      265/50R20`  - `Light truck      275/65R18`  - `Commercial truck      295/75R22.5`  2. 选择 **Update block with applicable tire values**。在 **Tire Parameters** 选项卡上，模块更新适用参数，包括 **Tire nominal section width**、**Rim radius** 和 **Tire mass**。  3. 选择 **Apply**。 |

使用 **Brake Type** 参数选择制动器。

| 操作 | Brake Type 设置 |
| --- | --- |
| 无制动 | `None` |
| 实现将制动缸压力转换为制动力的制动器 | `Disc` |
| 实现将施加的力和制动几何尺寸转换为净制动扭矩的单工鼓式制动器 | `Drum` |
| 实现作为车轮速度和施加的制动压力函数的查找表 | `Mapped` |

### 车轮旋转动力学

模块计算车轮在以下条件下的惯性响应：

- 车桥损耗
- 制动和驱动扭矩
- 轮胎滚动阻力
- 通过轮胎-道路界面的地面接触

为实现 Magic Formula 6.2，模块使用引用文献中的以下方程：

| 计算 | 方程 |
| --- | --- |
| 纵向力 | *Tire and Vehicle Dynamics*2 方程 4.E9 至 4.E57 |
| 横向力 - 纯侧偏 | *Tire and Vehicle Dynamics*2 方程 4.E19 至 4.E30 |
| 横向力 - 联合滑移 | *Tire and Vehicle Dynamics*2 方程 4.E58 至 4.E67 |
| 垂向动力学 | *Tire and Vehicle Dynamics*2 方程 4.E68、4.E1、4.E2a 和 4.E2b |
| 倾覆力矩偶 | *Tire and Vehicle Dynamics*2 方程 4.E69 |
| 滚动阻力 | - *An improved Magic Formula/Swift tyre model that can handle inflation pressure changes*1 方程 6.1.2 - *Tire and Vehicle Dynamics*2 方程 4.E70 |
| 回正力矩 | *Tire and Vehicle Dynamics*2 方程 4.E31 至 4.E49 |
| 回正扭矩 - 联合滑移 | *Tire and Vehicle Dynamics*2 方程 4.E71 至 4.E78 如果清除 **Include turn slip**，模块将这些方程中的一些设置为 1。 |

输入扭矩是施加的车轴扭矩、制动扭矩以及由联合轮胎扭矩产生的力矩之和。

Ti=Ta−Tb+Td

对于由联合轮胎扭矩产生的力矩，模块使用一阶动力学实现牵引车轮力和滚动阻力。滚动阻力具有以松弛长度参数化的时间常数。

Td(s)=1Le|ω|Res+1(FxRe+My)

制动扭矩基于理想干式离合器摩擦模型（如果选择了制动器）。根据锁止条件，模块实现以下摩擦和动力学模型：

| 如果 | 锁止条件 | 摩擦模型 | 动力学模型 |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | 未锁止 | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | 锁止 | Tf=Ts | ω=0 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 车轮角速度 |
| *a* | 与速度无关的力分量 |
| *b* | 线性速度力分量 |
| *c* | 二次速度力分量 |
| *Le* | 轮胎松弛长度 |
| *J* | 惯性矩 |
| *My* | 滚动阻力扭矩 |
| *Ta* | 绕车轮旋转轴施加的车轴扭矩 |
| *Tb* | 制动扭矩 |
| *Td* | 联合轮胎扭矩 |
| *Tf* | 摩擦力矩 |
| *Ti* | 净输入扭矩 |
| *Tk* | 动摩擦力矩 |
| *To* | 净输出扭矩 |
| *Ts* | 静摩擦力矩 |
| *Fc* | 施加的离合器力 |
| *Fx* | 因滑移由轮胎-道路界面产生的纵向力 |
| *Reff* | 有效离合器半径 |
| *Ro* | 环形盘外半径 |
| *Ri* | 环形盘内半径 |
| *Re* | 在载荷下和给定压力下的有效轮胎半径 |
| *Vx* | 纵向车轴速度 |
| *Fz* | 车辆法向力 |
| *ɑ* | 轮胎压力指数 |
| *β* | 法向力指数 |
| *pi* | 轮胎压力 |
| *μs* | 静摩擦系数 |
| *μk* | 动摩擦系数 |

### 轮胎和车轮坐标系

为解析力和力矩，模块使用轮胎和车轮坐标系的 Z-Up 方向。

- 轮胎坐标系轴（*XT*、*YT*、*ZT*）固定在附连到轮胎的参考系中。原点位于轮胎与地面的接触点。
- 车轮坐标系轴（*XW*、*YW*、*ZW*）固定在附连到车轮的参考系中。原点位于车轮中心。

**Z-Up Orientation**1

显示车轮平面和道路平面的 Z-Up 轮胎和车轮坐标系

### 制动器

**Disc**

如果将 **Brake Type** 参数指定为 `Disc`，模块实现盘式制动器。此图显示盘式制动器的侧视图和前视图。

盘式制动器的前视图和侧视图，显示制动片、制动盘和制动钳

盘式制动器将制动缸的制动缸压力转换为力。盘式制动器在制动片平均半径处施加该力。

模块使用以下方程计算盘式制动器的制动扭矩。

T={μPπBa2RmNpads4                when N≠0μstaticPπBa2RmNpads4         when N=0

Rm=Ro+Ri2

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动扭矩 |
| *P* | 施加的制动压力 |
| *N* | 车轮速度 |
| *Npads* | 盘式制动器总成中的制动片数量 |
| *μstatic* | 盘式制动片-制动盘界面的静摩擦系数 |
| *μ* | 盘式制动片-制动盘界面的动摩擦系数 |
| *Ba* | 制动执行器缸径 |
| *Rm* | 制动片在制动盘上施加力的平均半径 |
| *Ro* | 制动片外半径 |
| *Ri* | 制动片内半径 |

**Drum**

如果将 **Brake Type** 参数指定为 `Drum`，模块实现静态（稳态）单工鼓式制动器。单工鼓式制动器由单个双面液压执行器和两个制动蹄组成。这些制动蹄不共用同一铰接销。

单工鼓式制动器模型使用施加的力和制动几何尺寸计算每个制动蹄的净扭矩。鼓式模型假设两侧的执行器和制动蹄几何形状对称，从而允许两个制动蹄使用同一组几何和摩擦参数。

模块实现的方程源自 *Fundamentals of Machine Elements* 中的这些方程。

Trshoe=(πμcr(cosθ2−cosθ1)Ba22μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))PTlshoe=(πμcr(cosθ2−cosθ1)Ba2−2μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))P

T={Trshoe+Tlshoe                 when N≠0(Trshoe+Tlshoe)μstaticμ   when N=0

鼓式制动器的侧视图

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动扭矩 |
| *P* | 施加的制动压力 |
| *N* | 车轮速度 |
| *μstatic* | 盘式制动片-制动盘界面的静摩擦系数 |
| *μ* | 盘式制动片-制动盘界面的动摩擦系数 |
| *Trshoe* | 右蹄制动扭矩 |
| *Tlshoe* | 左蹄制动扭矩 |
| *a* | 从鼓中心到制动蹄铰接销中心的距离 |
| *c* | 从制动蹄铰接销中心到制动蹄上制动执行器连接点的距离 |
| *r* | 鼓内半径 |
| *Ba* | 制动执行器缸径 |
| *Θ1* | 从制动蹄铰接销中心到制动蹄上制动片材料起点的角度 |
| *Θ2* | 从制动蹄铰接销中心到制动蹄上制动片材料终点的角度 |

**Mapped**

如果将 **Brake Type** 参数指定为 `Mapped`，模块使用查找表确定制动扭矩。

T={fbrake(P,N)                   when N≠0(μstaticμ)fbrake(P,N)    when N=0

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动扭矩 |
| fbrake(P,N) | 制动扭矩查找表 |
| *P* | 施加的制动压力 |
| *N* | 车轮速度 |
| *μstatic* | 静态条件下鼓式制动片-面界面的摩擦系数 |
| *μ* | 盘式制动片-制动盘界面的摩擦系数 |

制动扭矩的查找表 fbrake(P,N) 是施加的制动压力和车轮速度的函数，其中：

- *T* 是制动扭矩，单位为 N·m。
- *P* 是施加的制动压力，单位为 bar。
- *N* 是车轮速度，单位为 rpm。

制动扭矩随车轮速度和施加的制动压力变化的图
