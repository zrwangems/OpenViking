---
type: simulink-block
title: 'Combined Slip Wheel 2DOF'
family: 'vdynblks'
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

### **BrkPrs** — 制动压力标量 | *N*×`1` 向量

制动压力，单位为 Pa。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

#### 依赖

要启用此端口，将 **Brake Type** 参数设置为以下类型之一：

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — 车轴扭矩标量 | *N*×`1` 向量

车轴扭矩 *Ta*，绕车轮旋转轴，单位为 N·m。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Vx** — 纵向速度标量 | *N*×`1` 向量

车轴纵向速度 *Vx*，沿轮胎固定 *x* 轴，单位为 m/s。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Vy** — 侧向速度标量 | *N*×`1` 向量

车轴侧向速度 *Vy*，沿轮胎固定 *y* 轴，单位为 m/s。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Camber** — 倾角标量 | *N*×`1` 向量

外倾角 *ɣ*，或倾角 *ε*，单位为 rad。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **YawRate** — 轮胎角速度标量 | *N*×`1` 向量

轮胎角速度 *r*，绕轮胎固定 *z* 轴（横摆角速度），单位为 rad/s。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Prs** — 轮胎充气压力标量 | *N*×`1` 向量

轮胎充气压力 *pi*，单位为 Pa。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Gnd** — 地面位移标量 | *N*×`1` 向量

地面位移，沿轮胎固定 *z* 轴，单位为 m。正输入产生车轮抬升。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

### **Fext** — 施加到轮胎的车轴力标量 | *N*×`1` 向量

施加到轮胎的车轴力 *Fext*，沿车辆固定 *z* 轴（正输入压缩轮胎），单位为 N。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

#### 依赖

要启用此参数，将 **Vertical Motion** 设置为 `None` 或 `Magic Formula`。

### **RadialDeflct** — 轮胎径向变形标量 | *N*×`1` 向量

轮胎径向变形 *RadialDeflct*，单位为 m。此值将用于所有依赖变形的内部魔术公式方程。

向量为车轮数 *N*×`1`。如果提供标量值，模块假定车轮数为一。

#### 依赖

要启用此端口，将 **Vertical Motion** 设置为 `External Deflection`。

### **ScaleFctrs** — 比例因子 `27`×`N` 数组

Magic Formula 6.2 比例因子数组。数组维度为 `27` 乘以车轮数 *N*。

Magic Formula 6.2 方程使用比例因子来考虑静态或仿真运行时的变化。名义上，大多数设置为 `1`。

| 数组元素 | 变量 | 比例因子 |
| --- | --- | --- |
| `ScaleFctrs(1,1)` | `lam_Fzo` | 名义载荷 |
| `ScaleFctrs(2,1)` | `lam_mux` | 纵向峰值摩擦系数 |
| `ScaleFctrs(3,1)` | `lam_muy` | 侧向峰值摩擦系数 |
| `ScaleFctrs(4,1)` | `lam_muV` | 滑移速度 *Vs* 衰减摩擦 |
| `ScaleFctrs(5,1)` | `lam_Kxkappa` | 制动滑移刚度 |
| `ScaleFctrs(6,1)` | `lam_Kyalpha` | 侧偏刚度 |
| `ScaleFctrs(7,1)` | `lam_Cx` | 纵向形状因子 |
| `ScaleFctrs(8,1)` | `lam_Cy` | 侧向形状因子 |
| `ScaleFctrs(9,1)` | `lam_Ex` | 纵向曲率因子 |
| `ScaleFctrs(10,1)` | `lam_Ey` | 侧向曲率因子 |
| `ScaleFctrs(11,1)` | `lam_Hx` | 纵向水平偏移 |
| `ScaleFctrs(12,1)` | `lam_Hy` | 侧向水平偏移 |
| `ScaleFctrs(13,1)` | `lam_Vx` | 纵向垂直偏移 |
| `ScaleFctrs(14,1)` | `lam_Vy` | 侧向垂直偏移 |
| `ScaleFctrs(15,1)` | `lam_Kygamma` | 外倾力刚度 |
| `ScaleFctrs(16,1)` | `lam_Kzgamma` | 外倾力矩刚度 |
| `ScaleFctrs(17,1)` | `lam_t` | 气胎拖距（影响回正力矩刚度） |
| `ScaleFctrs(18,1)` | `lam_Mr` | 残余力矩 |
| `ScaleFctrs(19,1)` | `lam_xalpha` | Alpha 对 *Fx*（kappa）的影响 |
| `ScaleFctrs(20,1)` | `lam_ykappa` | Kappa 对 *Fy*（alpha）的影响 |
| `ScaleFctrs(21,1)` | `lam_Vykappa` | 诱导帘布层转向 *Fy* |
| `ScaleFctrs(22,1)` | `lam_s` | *Fx* 的力臂 |
| `ScaleFctrs(23,1)` | `lam_Cz` | 径向轮胎刚度 |
| `ScaleFctrs(24,1)` | `lam_Mx` | 侧翻力矩刚度 |
| `ScaleFctrs(25,1)` | `lam_VMx` | 侧翻力矩垂直偏移 |
| `ScaleFctrs(26,1)` | `lam_My` | 滚动阻力矩 |
| `ScaleFctrs(27,1)` | `lam_Mphi` | 驻车力矩 *Mz* |
### 输出

### **Info** — 模块数据总线

模块数据，以包含以下模块值的总线信号形式返回。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `AxlTrq` | 绕车轮固定 *y* 轴的轴扭矩 | N·m |
| `Omega` | 绕车轮固定 *y* 轴的车轮角速度 | rad/s |
| `Fx` | 沿轮胎固定 *x* 轴的纵向车辆力 | N |
| `Fy` | 沿轮胎固定 *y* 轴的侧向车辆力 | N |
| `Fz` | 沿轮胎固定 *z* 轴的垂直车辆力 | N |
| `Mx` | 绕轮胎固定 *x* 轴的侧翻力矩 | N·m |
| `My` | 绕轮胎固定 *y* 轴的滚动阻力矩 | N·m |
| `Mz` | 绕轮胎固定 *z* 轴的回正力矩 | N·m |
| `Vx` | 沿轮胎固定 *x* 轴的车辆纵向速度 | m/s |
| `Vy` | 沿轮胎固定 *y* 轴的车辆侧向速度 | m/s |
| `Re` | 承载有效半径 | m |
| `Kappa` | 纵向滑移率 | NA |
| `Alpha` | 侧偏角 | rad |
| `a` | 接地区域半长 | m |
| `b` | 接地区域半宽 | m |
| `RL` | 承载半径 | m |
| `RadialDeflct` | 轮胎径向变形 | m |
| `WhlTrq` | 车轮扭矩 | N·m |
| `Gamma` | 外倾角 | rad |
| `psidot` | 绕轮胎固定 *z* 轴的轮胎角速度（横摆角速度） | rad/s |
| `BrkTrq` | 绕车辆固定 *y* 轴的制动扭矩 | N·m |
| `BrkPrs` | 制动压力 | Pa |
| `z` | 沿轮胎固定 *z* 轴的轴局部垂直位移 | m |
| `zdot` | 沿轮胎固定 *z* 轴的轴垂直速度 | m/s |
| `Gnd` | 沿轮胎固定 *z* 轴的地面位移（正输入产生车轮抬升） | m |
| `GndFz` | 沿轮胎固定 *z* 轴作用在地面上的垂直胎侧力 | N |
| `Prs` | 轮胎充气压力 | Pa |

### **Omega** — 车轮角速度 标量 | *N*×`1` 向量

车轮角速度 *ω*，绕车轮固定 *y* 轴，单位为 rad/s。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **Fx** — 纵向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *x* 轴作用于车轴的纵向力 *Fx*，单位为 N。正力用于使车辆向前运动。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **Fy** — 侧向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *y* 轴作用于车轴的侧向力 *Fy*，单位为 N。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **Fz** — 垂向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *z* 轴作用于车轴的垂向力 *Fz*，单位为 N。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **Mx** — 侧倾力矩 标量 | *N*×`1` 向量

绕轮胎固定 *x* 轴作用于车轴的纵向力矩 *Mx*，单位为 N·m。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **My** — 滚动阻力矩 标量 | *N*×`1` 向量

绕轮胎固定 *y* 轴作用于车轴的侧向力矩 *My*，单位为 N·m。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

### **Mz** — 回正力矩 标量 | *N*×`1` 向量

绕轮胎固定 *z* 轴作用于车轴的垂向力矩 *Mz*，单位为 N·m。

向量为车轮数量 *N* × `1`。如果提供标量值，模块假定车轮数量为一。

## 参数

### 轮胎选项

### **Tire type** — 选择类型 `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 导入包含 Magic Formula 系数的自有外部文件，并使用这些系数驱动对轮胎1和2进行建模的经验方程。导入的文件可以是 .mat、.tir 或 .txt 类型，并且必须包含与轮胎模块中参数名称对应的参数名。 | 使用文件中的拟合系数更新模块参数：  1. 将 **Tire type** 设置为 `External    file`。 2. 在 **Wheel and Tire Parameters** > **External    tire source** 窗格中，选择 **Select file**。 3. 选择轮胎系数文件。 4. 选择 **Update mask values from file**。在提示确认的对话框中，点击 **OK**。模块将更新参数。 5. 选择 **Apply**。 |
| 选择内置的 Magic Formula 轮胎模型之一，以驱动对轮胎1和2进行建模的经验方程。 | 使用内置轮胎模型中的值更新适用的模块参数：  1. 将 **Tire type** 设置为要实现的轮胎。选项包括：  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 选择 **Update block with applicable tire    values**。在 **Tire    Parameters** 选项卡上，模块将更新适用参数，包括 **Tire nominal    section width**、**Rim    radius** 和 **Tire mass**。 3. 选择 **Apply**。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireType` |
| **值：** | `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **数据类型：** | `character vector` |

### **轮胎文件或对象，tireParamSet** — 轮胎文件 `vdynPassCar.mat`（默认）| `.tir` | `.txt`

轮胎文件 `.tir` 或包含经验数据的对象，用于通过 Magic Formula 对轮胎的纵向和横向行为进行建模。如果提供 `.txt` 文件，请确保该文件包含与模块参数对应的名称。

使用文件中的拟合系数更新模块参数：

1. 将 **轮胎类型** 设置为 `External file`。
2. 在 **车轮和轮胎参数** > **外部轮胎源** 窗格中，选择 **选择文件**。
3. 选择轮胎系数文件。
4. 选择 **从文件更新掩码值**。在提示确认的对话框中，点击 **确定**。模块将更新参数。
5. 选择 **应用**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireParamSet` |
| **值：** | `vdynPassCar.mat`（默认）| `.tir` | `.txt` |
| **数据类型：** | `character vector` |

### **垂直运动** — 垂直运动模型 `Magic Formula`（默认）| `None` | `External deflection`

垂直运动的类型。默认情况下，模块使用 Magic Formula 计算轮胎的垂直运动。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `vertType` |
| **值：** | `Magic Formula`（默认）| `None` | `External deflection` |
| **数据类型：** | `character vector` |

### **帘布层转向** — 包含帘布层转向 `on`（默认）| `off`

选择以在 Magic Formula 6.2 方程中包含帘布层转向。

默认情况下，模块在 Magic Formula 6.2 方程中包含帘布层转向和转弯滑移。这些方程拟合于平带测试数据，并预测多种轮胎效应，包括帘布层转向和转弯滑移。如果满足以下条件，请考虑移除此类效应：

- 测试数据不包含帘布层转向或转弯滑移数据。
- 分析不需要帘布层转向或转弯滑移效应。

如果清除 **帘布层转向**，模块将在内部将以下参数设置为 0：

- **翻转力矩的垂直偏移，QSX1**
- **组合滑移 Fx 偏移因子缩减，RHX1**
- **Efy 曲率常数外倾角依赖性，PEY3**
- **FZNOM 处的 SHY 水平偏移，PHY1**
- **SHY 随载荷的变化，PHY2**
- **FZNOM 处的 Svy/Fz 垂直偏移，PVY1**
- **Svy/Fz 随载荷的变化，PVY2**
- **Fy 偏移随侧偏角的缩减，RBY3**
- **FZNOM 处的滑移率侧向力 Svyk/Muy\*Fz，RVY1**
- **侧向力 Svyk/Muy\*Fz 随载荷的变化，RVY2**
- **Bpt 斜率随外倾角的变化，QBZ4**
- **Dpt 峰值拖距随外倾角的变化，QDZ3**
- **Dmr 峰值残余力矩，QDZ6**
- **Dmr 峰值残余力矩随载荷的变化，QDZ7**
- **Ept 随 alpha-t 符号的变化，QEZ4**
- **FZNOM 处的 Sht 水平拖距偏移，QHZ1**
- **Sht 随载荷的变化，QHZ2**
- **s/R0 的标称值：Fx 对 Mz 的影响，SSZ1**

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `plySteer` |
| **值：** | `on`（默认）| `off` |
| **数据类型：** | `character vector` |

### **Turn slip** — 包含侧偏转向 `on`（默认）| `off`

选择以在 Magic Formula 6.2 方程中包含帘布层转向和侧偏转向。

默认情况下，模块在 Magic Formula 6.2 方程中包含帘布层转向和侧偏转向。这些方程拟合于平带测试数据，并预测多种轮胎效应，包括帘布层转向和侧偏转向。如果满足以下条件，请考虑移除此效应：

- 测试数据不包含帘布层转向或侧偏转向数据。
- 分析不需要帘布层转向或侧偏转向效应。

如果清除 **Turn slip**，模块将在内部：

- 将 Magic Formula 侧偏转向方程设置为 1。具体为方程 4.E77、4.E79、4.E81、4.E83、4.E84、4.E92、4.E102、4.E101 和 4.E1052。
- 使用影响水平偏移的 Magic Formula 项。
- 在 4.E272 中使用 Magic Formula 小侧偏转向值。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `turnslip` |
| **值**：| `on`（默认）| `off` |
| **Data Types:** | `character vector` |

### **Brake type** — 制动器类型 `None` | `Disc` | `Drum` | `Mapped`

使用 **Brake Type** 参数选择制动器。

| 操作 | Brake Type 设置 |
| --- | --- |
| 无制动 | `None` |
| 实现将制动缸压力转换为制动力的制动器 | `Disc` |
| 实现将施加力和制动器几何形状转换为净制动扭矩的单工鼓式制动器 | `Drum` |
| 实现作为车轮速度和施加制动压力函数的查找表 | `Mapped` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **值**：| `None` | `Disc` | `Drum` | `Mapped` |
| **Data Types:** | `character vector` |

### Plotting

### **Install Extended Tire Features** — 安装 Extended Tire Features for Vehicle Dynamics Blockset™ 支持包的选项按钮

点击 **Install Extended Tire Features** 以安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包。使用该支持包，您可以从 Combined Slip Wheel 2DOF 模块参数对话框中绘制稳态力和力矩轮胎响应。

### **Plot steady state force, moment response** — 绘制稳态力和力矩轮胎响应的选项按钮

点击 **Plot steady state force, moment response** 以生成以下绘图：

- **Lateral force [N] vs Slip angle [rad]**
- **Self-aligning moment [Nm] vs Slip angle [rad]**
- **Longitudinal force [N] vs Longitudinal slip []**
- **Longitudinal force [N] vs Lateral force [N]**

#### 依赖关系

要启用此参数，请点击 **Install Extended Tire Features**。

### Brake

### **Static friction coefficient, mu\_static** — 静摩擦系数 `0.3`（默认）| 标量 | *N*×`1` 向量

静摩擦系数，指定为标量或 *N*×`1` 向量，无量纲。如果指定标量，模块将对所有车轮使用该值。如果指定向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`、`Drum` 或 `Mapped`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **值**：| `0.3`（默认）| 标量 | *N*×`1` 向量 |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, mu\_kinetic** — 动摩擦系数 `0.2`（默认）| 标量 | *N*×`1` 向量

动摩擦系数，指定为标量或 *N*×`1` 向量，无量纲。
如果指定标量，模块将对所有车轮使用该值。如果
指定向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Disc`、`Drum` 或
`Mapped`。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param`
函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_kinetic` |
| **值：** | `0.2`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

#### Disc

### **Disc brake actuator bore, disc\_abore** — 孔径距离 `0.05`（默认）| 标量 | *N*×`1` 向量

盘式制动器执行器孔径，指定为标量
或 *N*×`1` 向量，单位为 m。如果
指定标量，模块将对所有车轮使用该值。如果指定
向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Disc`。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param`
函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `disc_abore` |
| **值：** | `0.05`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **Brake pad mean radius, Rm** — 半径 `0.177`（默认）| 标量 | *N*×`1` 向量

制动衬块平均半径，指定为标量
或 *N*×`1` 向量，单位为 m。如果指定
标量，模块将对所有车轮使用该值。如果指定向量，
则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Disc`。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param`
函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rm` |
| **值：** | `0.177`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **Number of brake pads, num\_pads** — 制动衬块数量 `2`（默认）| 标量 | *N*×`1` 向量

制动衬块数量，指定为标量
或 *N*×`1` 向量，无量纲。如果
指定标量，模块将对所有车轮使用该值。如果指定
向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Disc`。

#### 编程使用

要以编程方式设置模块参数
值，请使用 `set_param`
函数。

要以编程方式获取模块参数
值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `num_pads` |
| **值：** | `2`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

#### Drum

### **Drum brake actuator bore, drum\_abore** — 孔径距离 `0.0508`（默认）| 标量 | *N*×`1` 向量

鼓式制动器执行器孔径，指定为标量
或 *N*×`1` 向量，单位为 m。如果
指定标量，模块将对所有车轮使用该值。如果指定
向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_abore` |
| **值：** | `0.0508`（默认） | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **制动蹄销到制动鼓中心距离，drum\_a** — 制动蹄销到制动鼓中心距离 `0.123`（默认） | 标量

制动蹄销到制动鼓中心距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_a` |
| **值：** | `0.123`（默认） | 标量 |
| **数据类型：** | `double` |

### **制动蹄销中心到力作用点距离，drum\_c** — 制动蹄销中心到力作用点距离 `0.212`（默认） | 标量

制动蹄销中心到力作用点距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_c` |
| **值：** | `0.212`（默认） | 标量 |
| **数据类型：** | `double` |

### **制动鼓内半径，drum\_r** — 制动鼓内半径 `0.15`（默认） | 标量

制动鼓内半径，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_r` |
| **值：** | `0.15`（默认） | 标量 |
| **数据类型：** | `double` |

### **制动蹄销到衬片起始角度，drum\_theta1** — 制动蹄销到衬片起始角度 `0`（默认） | 标量

制动蹄销到衬片起始角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta1` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **制动蹄销到衬片终止角度，drum\_theta2** — 制动蹄销到衬片终止角度 `126`（默认） | 标量

制动蹄销到衬片终止角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta2` |
| **值：** | `126`（默认） | 标量 |
| **数据类型：** | `double` |

#### 映射

### **制动执行器压力断点，brake\_p\_bpt** — 制动执行器压力断点向量

制动执行器压力断点，单位为 bar。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_p_bpt` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### **车轮速度断点，brake\_n\_bpt** — 车轮速度断点向量

车轮速度断点，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_n_bpt` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### **Brake torque map, f\_brake\_t** — 制动扭矩数组的查找表

制动扭矩的查找表 fbrake(P,N) 是施加的制动压力和车轮速度的函数，其中：

- *T* 是制动扭矩，单位为 N·m。
- *P* 是施加的制动压力，单位为 bar。
- *N* 是车轮速度，单位为 rpm。

显示制动扭矩作为车轮速度和施加制动压力函数的图

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_brake_t` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### 仿真

### **Nominal pressure, NOMPRES** — 压力标量

标称压力 *NOMPRES*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NOMPRES` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum pressure, PRESMAX** — 最大压力标量

最大压力 *PRESMAX*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum pressure, PRESMIN** — 最小压力标量

最小压力 *PRESMIN*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal normal force, FNOMIN** — 力标量

标称法向力 *FNOMIN*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FNOMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum normal force, FZMAX** — 力标量

最大法向力 *FZMAX*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum normal force, FZMIN** — 力标量

最小法向力 *FZMIN*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — 容差标量

用于处理低速情况的速度容差 *VXLOW*，单位为 m/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VXLOW` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — 最大允许滑移率标量

最大允许滑移率（绝对值），*KPUMAX*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — 最小允许滑移率标量

最小允许滑移率（绝对值），*KPUMIN*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — 最大允许侧偏角标量

最大允许侧偏角（绝对值），*ALPMAX*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — 最小允许侧偏角标量

最小允许侧偏角（绝对值），*ALPMIN*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum allowable camber angle, CAMMAX** — 最大允许外倾角标量

最大允许外倾角 *CAMMAX*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable camber angle, CAMMIN** — 最小允许外倾角标量

最小允许外倾角，*CAMMIN*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal longitudinal speed, LONGVL** — 速度标量

标称纵向速度，*LONGVL*，单位为 m/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LONGVL` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Initial wheel rotational velocity, omegao** — 初始车轮转速标量 | *N*×`1` 向量

初始车轮转速，指定为标量或 *N*×`1` 向量，单位为 rad/s。如果指定标量，模块将对所有车轮使用该值。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegao` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### Dimension

### **Tire unloaded radius, UNLOADED\_RADIUS** — 半径标量

轮胎无载半径，*UNLOADED\_RADIUS*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `UNLOADED_RADIUS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **轮胎名义断面宽度，WIDTH** — 轮胎名义断面宽度标量

轮胎名义断面宽度，*WIDTH*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WIDTH` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **轮辋半径，RIM\_RADIUS** — 半径标量

轮辋半径，*RIM\_RADIUS*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RIM_RADIUS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义扁平比，ASPECT\_RATIO** — 比值标量

名义扁平比，*ASPECT\_RATIO*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ASPECT_RATIO` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 惯性与阻尼

### **轮胎质量，MASS** — 质量标量 | *N*×`1` 向量

轮胎质量，指定为标量或 *N*×`1` 向量，单位为 kg。如果指定为标量，模块将该值用于所有车轮。如果指定为向量，则必须为其他惯性参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Magic Formula`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MASS` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **轮胎转动惯量（滚动轴），IYY** — 轮胎转动惯量标量 | *N*×`1` 向量

轮胎转动惯量（滚动轴），指定为标量或 *N*×`1` 向量，单位为 kg·m2。如果指定为标量，模块将该值用于所有车轮。如果指定为向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IYY` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **旋转阻尼，br** — 旋转阻尼标量 | *N*×`1` 向量

旋转阻尼，指定为标量或 *N*×`1` 向量，单位为 N·m·s/rad。如果指定为标量，模块将该值用于所有车轮。如果指定为向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `br` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **重力，GRAVITY** — 重力标量

重力，*GRAVITY*，单位为 m/s^2。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Magic Formula`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GRAVITY` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Vertical

### **Initial tire displacement, zo** — 位移 标量 | *N*×`1` 向量

初始轮胎位移，指定为标量或 *N*×`1` 向量，单位为 m。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他垂向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zo` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — 速度 标量 | *N*×`1` 向量

初始车轮垂向速度，指定为标量或 *N*×`1` 向量，单位为 m/s。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他垂向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zdoto` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **Effective rolling radius at low load stiffness, BREFF** — 刚度 标量

低载荷刚度下的有效滚动半径，*BREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Effective rolling radius peak value, DREFF** — 半径 标量

有效滚动半径峰值，*DREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Effective rolling radius at high load stiffness, FREFF** — 半径 标量

高载荷刚度下的有效滚动半径，*FREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Unloaded to nominal rolling radius ratio, Q\_RE0** — 比值 标量

空载与名义滚动半径之比，*Q\_RE0*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RE0` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Radius rotational speed dependence, Q\_V1** — 速度 标量

半径的转速依赖性，*Q\_V1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Stiffness rotational speed dependence, Q\_V2** — 速度标量

刚度随转速变化，*Q\_V2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear load change with deflection, Q\_FZ1** — 载荷变化 `标量`

载荷随挠度线性变化，*Q\_FZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic load change with deflection, Q\_FZ2** — 载荷变化 标量

载荷随挠度二次变化，*Q\_FZ2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear load change with deflection and quadratic camber, Q\_FZ3** — 载荷变化 标量

载荷随挠度线性变化及外倾角二次变化，*Q\_FZ3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Load response to longitudinal force, Q\_FCX** — 力 标量

载荷对纵向力的响应，*Q\_FCX*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Load response to lateral force, Q\_FCY** — 力 标量

载荷对侧向力的响应，*Q\_FCY*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCY` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Vertical stiffness change due to lateral load dependency on lateral stiffness, Q\_FCY2** — 刚度 标量

由于侧向载荷对侧向刚度的依赖性引起的垂直刚度变化，*Q\_FCY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Stiffness response to pressure, PFZ1** — 刚度 `0.7098`（默认） | `标量`

刚度对压力的响应，*PFZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PFZ1` |
| **值：** | `0.7098`（默认） | `标量` |
| **数据类型：** | `double` |

### **Vertical tire stiffness, VERTICAL\_STIFFNESS** — 刚度 标量

垂直轮胎刚度，*VERTICAL\_STIFFNESS*，单位为 N/m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VERTICAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂向轮胎阻尼，VERTICAL\_DAMPING** — 阻尼标量

垂向轮胎阻尼，*VERTICAL\_DAMPING*，单位为 N·s/m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VERTICAL_DAMPING` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **轮辋触底偏移量，BOTTOM\_OFFST** — 偏移量标量

轮辋触底偏移量，*BOTTOM\_OFFST*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BOTTOM_OFFST` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **触底刚度，BOTTOM\_STIFF** — 刚度标量

触底刚度，*BOTTOM\_STIFF*，单位为 N/m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BOTTOM_STIFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **线性载荷相关外倾角对垂向刚度的影响，Q\_CAM1** — 刚度标量

线性载荷相关外倾角对垂向刚度的影响，*Q\_CAM1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **二次载荷相关外倾角对垂向刚度的影响，Q\_CAM2** — 刚度标量

二次载荷相关外倾角对垂向刚度的影响，*Q\_CAM2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **刚度和外倾角随载荷的线性折减，Q\_CAM3** — 刚度标量

刚度和外倾角随载荷的线性折减，*Q\_CAM3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **恒定外倾角和侧偏角对垂向刚度的影响，Q\_FYS1** — 刚度标量

恒定外倾角和侧偏角对垂向刚度的影响，*Q\_FYS1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **线性外倾角和侧偏角对垂向刚度的影响，Q\_FYS2** — 刚度标量

线性外倾角和侧偏角对垂向刚度的影响，*Q\_FYS2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic camber and slip angle effect on vertical stiffness, Q\_FYS3** — 刚度标量

外倾角和侧偏角对垂直刚度的二次影响，
*Q\_FYS3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 结构

### **Longitudinal stiffness, LONGITUDINAL\_STIFFNESS** — 刚度标量

纵向刚度，*LONGITUDINAL\_STIFFNESS*，单位为
N/m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LONGITUDINAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Lateral stiffness, LATERAL\_STIFFNESS** — 刚度标量

纵向刚度，*LATERAL\_STIFFNESS*，单位为 N/m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LATERAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear vertical deflection influence on longitudinal stiffness, PCFX1** — 变形影响标量

垂直变形对纵向刚度的线性影响，
*PCFX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic vertical deflection influence on longitudinal stiffness, PCFX2** — 变形影响标量

垂直变形对纵向刚度的二次影响，
*PCFX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Pressure dependency on longitudinal stiffness, PCFX3** — 压力依赖标量

纵向刚度对压力的依赖性，*PCFX3*，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear vertical deflection influence on lateral stiffness, PCFY1** — 变形影响标量

垂直变形对侧向刚度的线性影响，
*PCFY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic vertical deflection influence on lateral stiffness, PCFY2** — 变形影响标量

垂直变形对侧向刚度的二次影响，
*PCFY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Pressure dependency on longitudinal stiffness, PCFY3** — 压力依赖标量

纵向刚度对压力的依赖性，*PCFY3*，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Contact Patch

### **Contact length square root term, Q\_RA1** — 长度项标量

接触长度平方根项，*Q\_RA1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact length linear term, Q\_RA2** — 长度项标量

接触长度线性项，*Q\_RA2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact width root term, Q\_RB1** — 宽度项标量

接触宽度根项，*Q\_RB1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact width linear term, Q\_RB2** — 宽度项标量

接触宽度线性项，*Q\_RB2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Longitudinal

### **Cfx shape factor, PCX1** — 形状因子标量

形状因子，*Cfx*，*PCX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Longitudinal friction at nominal normal load, PDX1** — 摩擦标量

额定法向载荷下的纵向摩擦，*PDX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Frictional variation with load, PDX2** — 摩擦变化标量

摩擦随载荷的变化，*PDX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Frictional variation with camber, PDX3** — 摩擦变化标量

摩擦随外倾角的变化，*PDX3*，单位为 1/rad^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Longitudinal curvature at nominal normal load, PEX1** — 曲率标量

额定法向载荷下的纵向曲率，*PEX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷的变化，PEX2** — 曲率变化标量

曲率因子随载荷的变化，*PEX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷平方的变化，PEX3** — 曲率变化标量

曲率因子随载荷平方的变化，*PEX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向曲率因子随滑移的变化，PEX4** — 曲率标量

纵向曲率因子随滑移的变化，*PEX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **额定法向载荷下的纵向滑移刚度，PKX1** — 刚度标量

额定法向载荷下的纵向滑移刚度，*PKX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度随载荷的变化，PKX2** — 刚度变化标量

滑移刚度随载荷的变化，*PKX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度指数因子，PKX3** — 滑移刚度标量

滑移刚度指数因子，*PKX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **额定法向载荷下滑移率的水平偏移，PHX1** — 滑移率偏移标量

额定法向载荷下滑移率的水平偏移，*PHX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **水平滑移率随载荷的变化，PHX2** — 滑移变化标量

水平滑移率随载荷的变化，*PHX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Vertical shift in load at nominal normal load, PVX1** — 载荷偏移标量

额定法向载荷下的载荷垂直偏移，*PVX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Variation of vertical shift with load, PVX2** — 载荷变化标量

垂直偏移随载荷的变化，*PVX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear variation of longitudinal slip stiffness with tire pressure, PPX1** — 刚度变化标量

纵向滑移刚度随轮胎压力的线性变化，*PPX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2** — 刚度变化标量

纵向滑移刚度随轮胎压力的二次变化，*PPX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear variation of peak longitudinal friction with tire pressure, PPX3** — 摩擦变化标量

峰值纵向摩擦力随轮胎压力的线性变化，*PPX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic variation of peak longitudinal friction with tire pressure, PPX4** — 摩擦变化标量

峰值纵向摩擦力随轮胎压力的二次变化，*PPX4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined slip Fx slope factor reduction, RBX1** — 联合滑移纵向力斜率因子缩减标量

联合滑移纵向力，*Fx*，斜率因子缩减，*RBX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Slip ratio Fx slope reduction variation, RBX2** — 滑移率纵向力斜率缩减变化标量

滑移率纵向力，*Fx*，斜率缩减变化，*RBX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber influence on combined slip Fx stiffness, RBX3** — 侧倾对联合滑移纵向力刚度的影响标量

侧倾对联合滑移纵向力 *Fx* 刚度 *RBX3* 的影响，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Shape factor for combined slip Fx reduction, RCX1** — 联合滑移纵向力折减的形状因子标量

联合滑移纵向力 *Fx* 折减的形状因子 *RCX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined Fx curvature factor, REX1** — 联合纵向力曲率因子标量

联合纵向力 *Fx* 曲率因子 *REX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined Fx curvature factor with load, REX2** — 联合纵向力曲率因子标量

联合纵向力 *Fx* 随载荷变化的曲率因子 *REX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined slip Fx shift factor reduction, RHX1** — 联合滑移纵向力滑移因子标量

联合滑移纵向力 *Fx* 滑移因子折减 *RHX1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Overturning

### **Vertical shift of overturning moment, QSX1** — 侧翻力矩标量

侧翻力矩的垂直偏移 *QSX1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Overturning moment due to camber, QSX2** — 由侧倾引起的侧翻力矩标量

由侧倾引起的侧翻力矩 *QSX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Overturning moment due to Fy, QSX3** — 由侧向力引起的侧翻力矩标量

由侧向力引起的侧翻力矩 *QSX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx combined lateral force load and camber, QSX4** — 倾覆力矩标量

倾覆力矩，*Mx*，侧向力载荷与外倾角组合，*QSX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to lateral force and camber, QSX5** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和外倾角引起的载荷效应，*QSX5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to B-factor, QSX6** — 倾覆力矩标量

倾覆力矩，*Mx*，由 B 因子引起的载荷效应，*QSX6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to camber and load, QSX7** — 倾覆力矩标量

倾覆力矩，*Mx*，由外倾角和载荷引起，*QSX7*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to lateral force and load, QSX8** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和载荷引起，*QSX8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to B-factor of lateral force and load, QSX9** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和载荷的 B 因子引起，*QSX9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to vertical force and camber, QSX10** — 倾覆力矩标量

倾覆力矩，*Mx*，由垂直力和外倾角引起，*QSX10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to B-factor of vertical force and camber, QSX11** — 倾覆力矩标量

倾覆力矩，*Mx*，由垂直力和外倾角的 B 因子引起，*QSX11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to squared camber, QSX12** — 翻转力矩标量

由外倾角平方引起的翻转力矩，*Mx*，*QSX12*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX12` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force, QSX13** — 翻转力矩标量

由侧向力引起的翻转力矩，*Mx*，*QSX13*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX13` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force with camber, QSX14** — 翻转力矩标量

由带外倾角的侧向力引起的翻转力矩，*Mx*，*QSX14*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX14` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to inflation pressure, PPMX1** — 由压力引起的翻转力矩标量

由充气压力引起的翻转力矩，*Mx*，*PPMX1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPMX1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### Lateral

### **Cfy shape factor for lateral force, PCY1** — 侧向力形状因子标量

侧向力形状因子，*Cfy*，*PCY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PCY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Lateral friction muy, PDY1** — 侧向摩擦标量

侧向摩擦，*μy*，*PDY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Lateral friction variation of muy with load, PDY2** — 侧向摩擦变化标量

侧向摩擦 *μy* 随载荷的变化，*PDY2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Lateral friction variation of muy with squared camber, PDY3** — 侧向摩擦变化标量

侧向摩擦 *μy* 随外倾角平方的变化，*PDY3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PDY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Efy lateral curvature at nominal force FZNOM, PEY1** — 额定力下的侧向曲率标量

额定力 *FZNOM* 下的侧向曲率，*Efy*，*PEY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with load, PEY2** — 侧向曲率变化标量

侧向曲率 *Efy* 随载荷的变化，*PEY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature constant camber dependency, PEY3** — 侧向曲率常数标量

侧向曲率 *Efy* 的常数外倾依赖，*PEY3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with camber, PEY4** — 侧向曲率变化标量

侧向曲率 *Efy* 随外倾的变化，*PEY4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with camber squared, PEY5** — 侧向曲率变化标量

侧向曲率 *Efy* 随外倾平方的变化，*PEY5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum KFy/FZNOM stiffness, PKY1** — 最大刚度标量

最大侧向力刚度 *KFy* 与标称力 *FZNOM* 之比，*PKY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Load at maximum KFy/FZNOM stiffness, PKY2** — 载荷标量

最大侧向力刚度 *KFy* 与标称力 *FZNOM* 之比处的载荷，*PKY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **KFy/FZNOM stiffness variation with camber, PKY3** — 刚度变化标量

侧向力刚度 *KFy* 与标称力 *FZNOM* 之比随外倾的刚度变化，*PKY3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **KFy curvature, PKY4** — 侧向力刚度曲率标量

侧向力刚度 *KFy* 曲率，*PKY4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **峰值刚度随外倾角平方的变化，PKY5** — 刚度变化标量

峰值刚度随外倾角平方的变化，*PKY5*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 外倾刚度因子，PKY6** — 侧向力外倾刚度因子标量

侧向力 *Fy* 外倾刚度因子，*PKY6*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾刚度垂直载荷依赖性，PKY7** — 刚度标量

外倾刚度垂直载荷依赖性，*PKY7*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **FZNOM 处的 SHY 水平偏移，PHY1** — 额定力处的水平偏移标量

额定力 *FZNOM* 处的水平偏移 *SHY*，*PHY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **SHY 随载荷的变化，PHY2** — 水平偏移变化标量

水平偏移 *SHY* 随载荷的变化，*PHY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 在 FZNOM 处的垂直偏移，PVY1** — 额定力处的垂直偏移标量

额定力 *FZNOM* 处的垂直偏移 *Svy*，*PVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz 随载荷的变化，PVY2** — 垂直偏移随载荷变化标量

垂直偏移 *Svy* 随载荷的变化，*PVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz variation with camber, PVY3** — 随外倾角的垂直偏移变化标量

垂直偏移，*Svy*，随外倾角的变化，*PVY3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PVY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Svy/Fz variation with load and camber, PVY4** — 随载荷和外倾角的垂直偏移变化标量

垂直偏移，*Svy*，随载荷和外倾角的变化，*PVY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PVY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure, PPY1** — 随压力的刚度变化标量

侧偏刚度随充气压力的变化，*PPY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2** — 随压力的刚度变化标量

侧偏刚度随充气压力引起的额定载荷依赖性的变化，*PPY2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Linear inflation pressure on peak lateral friction, PPY3** — 压力标量

充气压力对峰值侧向摩擦力的线性影响，*PPY3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Quadratic inflation pressure on peak lateral friction, PPY4** — 压力标量

充气压力对峰值侧向摩擦力的二次影响，*PPY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Inflation pressure effect on camber stiffness, PPY5** — 压力标量

充气压力对外倾刚度的影​​响，*PPY5*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY5` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Combined Fy reduction slope factor, RBY1** — 组合侧向力缩减斜率因子标量

组合侧向力，*Fy*，缩减斜率因子，*RBY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RBY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy slope reduction with slip angle, RBY2** — 侧向力斜率随侧偏角的缩减标量

侧向力，*Fy*，斜率随侧偏角的缩减，*RBY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY2` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy shift reduction with slip angle, RBY3** — 侧向力随侧偏角的偏移缩减标量

侧向力 *Fy* 随侧偏角的偏移缩减，*RBY3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY3` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined stiffness variation from camber, RBY4** — 侧向力组合刚度随外倾角变化标量

侧向力 *Fy* 组合刚度随外倾角变化，*RBY4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY4` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined reduction shape factor, RCY1** — 侧向力组合缩减形状因子标量

侧向力 *Fy* 组合缩减形状因子，*RCY1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCY1` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined curvature factor, REY1** — 侧向力组合曲率因子标量

侧向力 *Fy* 组合曲率因子，*REY1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REY1` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined curvature factor with load, REY2** — 侧向力组合曲率因子随载荷变化标量

侧向力 *Fy* 组合曲率因子随载荷变化，*REY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REY2` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined reduction shift factor, RHY1** — 侧向力组合缩减偏移因子标量

侧向力 *Fy* 组合缩减偏移因子，*RHY1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHY1` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined reduction shift factor with load, RHY2** — 侧向力组合缩减偏移因子随载荷变化标量

侧向力 *Fy* 组合缩减偏移因子随载荷变化，*RHY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHY2` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1** — 在额定力下的滑移率侧向力标量

在额定力 *FZNOM* 下的滑移率侧向力，*RVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随载荷变化，RVY2** — 侧向力随载荷变化标量

侧向力随载荷变化，*RVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随外倾角变化，RVY3** — 侧向力随外倾角变化标量

侧向力随外倾角变化，*RVY3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随侧偏角变化，RVY4** — 侧向力随侧偏角变化标量

侧向力随侧偏角变化，*RVY4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随滑移率变化，RVY5** — 侧向力随滑移率变化标量

侧向力随滑移率变化，*RVY5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向力 Svyk/Muy\*Fz 随滑移率反正切变化，RVY6** — 侧向力随滑移率反正切变化标量

侧向力随滑移率反正切变化，*RVY6*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RVY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 滚动

### **阻力矩系数，QSY1** — 阻力矩标量

阻力矩系数，*QSY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由 Fx 引起的阻力矩，QSY2** — 由纵向力引起的阻力矩标量

由纵向力 *Fx* 引起的阻力矩，*QSY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由速度引起的阻力矩，QSY3** — 由速度引起的阻力矩标量

由速度引起的阻力矩，*QSY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to speed^4, QSY4** — 随速度^4变化的阻力矩标量

随速度^4变化的阻力矩，*QSY4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to square of camber, QSY5** — 随外倾角平方变化的阻力矩标量

随外倾角平方变化的阻力矩，*QSY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to square of camber and load, QSY6** — 随外倾角平方和载荷变化的阻力矩标量

随外倾角平方和载荷变化的阻力矩，*QSY6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to load, QSY7** — 随载荷变化的阻力矩标量

随载荷变化的阻力矩，*QSY7*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to pressure, QSY8** — 随压力变化的阻力矩标量

随压力变化的阻力矩，*QSY8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 对齐

### **Trail slope factor for trail Bpt at FZNOM, QBZ1** — 额定力下的拖距斜率因子标量

额定力 *FZNOM* 下拖距 *Bpt* 的拖距斜率因子，*QBZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with load, QBZ2** — 随载荷变化的斜率标量

随载荷变化的斜率，*QBZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with square of load, QBZ3** — 随载荷变化的斜率 `0`（默认）| 标量

随载荷平方变化的斜率，*QBZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with camber, QBZ4** — 随外倾角的斜率变化标量

随外倾角的斜率变化，*QBZ4*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with absolute value of camber, QBZ5** — 随外倾角的斜率变化标量

随外倾角绝对值的斜率变化，*QBZ5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with square of camber, QBZ6** — 随外倾角的斜率变化标量

随外倾角平方的斜率变化，*QBZ6*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Br of Mzr slope scaling factor, QBZ9** — 斜率缩放因子标量

斜率缩放因子，*QBZ9*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Br of Mzr cornering stiffness factor, QBZ10** — 侧偏刚度因子标量

*Mzr* 的 *Br* 侧偏刚度因子，*QBZ10*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cpt pneumatic trail shape factor, QCZ1** — 气胎拖距形状因子标量

气胎拖距形状因子，*Cpt*，*QCZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail, QDZ1** — 峰值拖距标量

峰值拖距，*Dpt*，*QDZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with load, QDZ2** — 随载荷的峰值拖距变化标量

峰值拖距，*Dpt*，随载荷的变化，*QDZ2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with camber, QDZ3** — 随外倾角的峰值拖距变化标量

峰值拖距，*Dpt*，随外倾角的变化，*QDZ3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with square of camber, QDZ4** — 随外倾角平方变化的峰值拖距标量

峰值拖距，*Dpt*，随外倾角平方的变化，*QDZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque, QDZ6** — 峰值残余力矩标量

峰值残余力矩，*Dmr*，*QDZ6*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with load, QDZ7** — 随载荷变化的峰值残余力矩标量

峰值残余力矩，*Dmr*，随载荷的变化，*QDZ7*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber, QDZ8** — 随外倾角变化的峰值残余力矩标量

峰值残余力矩，*Dmr*，随外倾角的变化，*QDZ8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber and load, QDZ9** — 随外倾角和载荷变化的峰值残余力矩标量

峰值残余力矩，*Dmr*，随外倾角和载荷的变化，*QDZ9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of camber, QDZ10** — 随外倾角变化的峰值残余力矩标量

峰值残余力矩，*Dmr*，随外倾角平方的变化，*QDZ10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of load, QDZ11** — 随载荷变化的峰值残余力矩标量

峰值残余力矩，*Dmr*，随载荷平方的变化，*QDZ11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **FZNOM 处的 Ept 轨迹曲率，QEZ1** — 额定力下的轨迹曲率标量

额定力 *FZNOM* 下的轨迹曲率 *Ept*，*QEZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随载荷变化，QEZ2** — 轨迹曲率随载荷变化标量

轨迹曲率 *Ept* 随载荷变化，*QEZ2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随载荷平方变化，QEZ3** — 轨迹曲率随载荷变化标量

轨迹曲率 *Ept* 随载荷平方变化，*QEZ3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随 alpha-t 符号变化，QEZ4** — 轨迹曲率变化标量

轨迹曲率 *Ept* 随 alpha-t 符号变化，*QEZ4*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept 随 alpha-t 符号和外倾角变化，QEZ5** — 变化标量

轨迹曲率 *Ept* 随 alpha-t 符号和外倾角变化，*QEZ5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **FZNOM 处的 Sht 水平轨迹偏移，QHZ1** — 额定载荷下的水平轨迹偏移标量

额定载荷 *FZNOM* 下的水平轨迹偏移 *Sht*，*QHZ1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht 随载荷变化，QHZ2** — 水平轨迹偏移随载荷变化标量

水平轨迹偏移 *Sht* 随载荷变化，*QHZ2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht 随外倾角变化，QHZ3** — 水平轨迹偏移随外倾角变化标量

水平轨迹偏移 *Sht* 随外倾角变化，*QHZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht variation with load and camber, QHZ4** — 水平拖距偏移随载荷和外倾角变化的标量

水平拖距偏移，*Sht*，随载荷和外倾角的变化，*QHZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Inflation pressure influence on trail length, PPZ1** — 充气压力对拖距长度影响的标量

充气压力对拖距长度的影响，*PPZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Inflation pressure influence on residual aligning torque, PPZ2** — 充气压力对回正力矩影响的标量

充气压力对残余回正力矩的影响，*PPZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal value of s/R0: effect of Fx on Mz, SSZ1** — 纵向力对回正力矩影响的标量

s/R0 的标称值：纵向力 *Fx* 对回正力矩 *Mz* 的影响，*SSZ1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with lateral to nominal force ratio, SSZ2** — 随侧向力与标称力之比变化的标量

随侧向力与标称力之比的变化，*SSZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with camber, SSZ3** — 随外倾角变化的标量

随外倾角的变化，*SSZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with camber and load, SSZ4** — 随外倾角和载荷变化的标量

随外倾角和载荷的变化，*SSZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Turnslip

### **Fx peak reduction due to spin, PDXP1** — 由于旋转导致的纵向力峰值降低标量

纵向力 *Fx* 由于旋转导致的峰值降低，*PDXP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with varying load, PDXP2** — 由于旋转导致的纵向力峰值降低标量

纵向力 *Fx* 由于旋转随载荷变化导致的峰值降低，*PDXP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with slip ratio, PDXP3** — 由于旋转导致的纵向力峰值降低标量

纵向力 *Fx* 由于旋转随滑移率导致的峰值降低，*PDXP3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cornering stiffness reduction due to spin, PKYP1** — 由于旋转导致的刚度降低标量

由于旋转导致的侧偏刚度降低，*PKYP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin, PDYP1** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转导致的峰值降低，*PDYP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin with varying load, PDYP2** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转随载荷变化导致的峰值降低，*PDYP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin with slip angle, PDYP3** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转随侧偏角导致的峰值降低，*PDYP3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to square root of spin, PDYP4** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转的平方根导致的峰值降低，*PDYP4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response lateral shift limit, PHYP1** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的侧向偏移限值，*PHYP1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit, PHYP2** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的最大侧向偏移限值，*PHYP2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit with load, PHYP3** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的带载荷最大侧向偏移限值，*PHYP3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response lateral shift curvature factor, PHYP4** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的侧向偏移曲率因子，*PHYP4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin, PECP1** — 外倾刚度折减标量

由于旋转引起的外倾刚度折减，*PECP1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin with load, PECP2** — 外倾刚度折减标量

由于旋转引起的带载荷外倾刚度折减，*PECP2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip pneumatic trail reduction factor, QDTP1** — 转向滑移气胎拖距折减因子标量

转向滑移气胎拖距折减因子，*QDTP1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDTP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn moment for constant turning and zero longitudinal speed, QCRP1** — 恒定转向力矩标量

恒定转向和零纵向速度下的转向力矩，*QCRP1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip moment increase with spin at 90deg slip angle, QCRP2** — 转向滑移力矩标量

在90度侧偏角下由于旋转引起的转向滑移力矩增量，*QCRP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧滑引起的残余回正力矩减小量，QBRP1** — 残余回正力矩减小量标量

侧滑引起的残余回正力矩减小量，*QBRP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **转向滑移力矩峰值幅值，QDRP1** — 转向滑移力矩峰值幅值标量

转向滑移力矩峰值幅值，*QDRP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **转向滑移力矩曲率，QDRP2** — 转向滑移力矩曲率标量

转向滑移力矩曲率，*QDRP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDRP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Wheels and Tires

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：新增 **Tire type** 选项

从 R2024b 开始，您可以指定 **Tire type** 以使用新的内置轮胎模型 `Light passenger car 245/60R16`。

### R2024b：重命名的模块参数

从 R2024b 开始，以下参数已被重命名。

| 旧名称 | 新名称 |
| --- | --- |
| **Wheel width** | **Tire nominal section width** |
| **Unloaded radius** | **Tire unloaded radius** |
| **Initial rotational velocity** | **Initial wheel rotational velocity** |
| **Wheel mass** | **Tire mass** |
| **Rotational inertia** | **Tire rotational inertia** |

### R2024b：新增 **Vertical Motion** 选项

从 R2024b 开始，将 **Vertical Motion** 指定为 `External Deflection` 会启用 **RadialDeflct** 端口。在与轮胎交互且未提供力的情况下，使用此端口定义胎侧变形。

### R2024b：新增信号添加到 **Info** 端口总线

从 R2024b 开始，**Info** 端口总线包含以下新信号。

| 信号 | 描述 |
| --- | --- |
| `RadialDeflct` | 轮胎径向变形 |
| `RL` | 负载半径 |
| `WhlTrq` | 车轮扭矩 |

### R2024a：绘制稳态力和力矩响应

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用新的 **Plot
steady state force, moment response** 按钮生成绘图。

### R2023a：新增 **Vertical Motion** 参数

从 R2023a 开始，Combined Slip Wheel 2DOF 模块包含 **Vertical
Motion** 参数。默认情况下，Combined Slip Wheel 2DOF 模块使用 Magic
Formula 计算轮胎的垂直运动。

### R2022b：为每个车轮指定制动和轮胎参数

从 R2022b 开始，您可以使用 Combined Slip Wheel 2DOF 模块为车辆上的每个车轮指定制动和轮胎特性。具体而言，该模块允许以下参数使用 *N*×`1` 向量：

- **Static friction coefficient, mu\_static**
- **Kinetic friction coefficient, mu\_kinetic**
- **Disc brake actuator bore, disc\_abore**
- **Brake pad mean radius, Rm**
- **Number of brake pads, num\_pads**
- **Drum brake actuator bore, disc\_abore**
- **Initial rotational velocity, omegao**
- **Rotational damping, br**
- **Wheel mass, MASS**
- **Rotational inertia (rolling axis), IYY**
- **Initial tire displacement, zo**
- **Initial wheel vertical velocity (wheel fixed frame), zdoto**

*N* 是车轮数量，并且必须与输入信号维度匹配。

### R2022b：新增 **Ply steer** 和 **Turn slip** 参数

从 R2022b 开始，Combined Slip Wheel 2DOF 模块包含 **Ply steer** 和 **Turn slip** 参数。要从这些模块的 Magic Formula 实现中移除 ply steer 和 turn slip，请清除 **Ply steer** 和 **Turn slip** 参数。

## 描述

带盘式、鼓式或映射制动的组合滑移 2DOF 车轮

Combined Slip Wheel 2DOF 在纵向和横向组合滑移条件下，融合了车轮运动的两个自由度（DOF）和轮胎力的 6 个自由度。

- 车轮运动：绕旋转轴旋转，以及垂直位移。
- 轮胎力和力矩：Fx、Fy 和 Fz；Mx、My 和 Mz。

它使用 Magic Formula 6.2 对轮胎进行建模。[1] 和 [2] 通过导入您自己的轮胎模型文件，或选择内置轮胎模型之一，来设置 Magic Formula 6.2 系数。

在如下仿真中使用此模块。

- 车辆制动和加速，包括滚动阻力。
- 车辆行驶运动，包括悬架模式的影响。
- 具有横向和纵向组合滑移的机动操作，例如车辆横向运动和横摆稳定性。

如果安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用以下附加功能：

- 绘图生成 — 点击 **Plot steady state force, moment response** 按钮以生成以下绘图：

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle [rad]**
  - **Longitudinal force [N] vs Longitudinal slip []**
  - **Longitudinal force [N] vs Lateral force [N]**
- 导入轮胎参数 — 使用 `tireModel.get` 方法将 Combined Slip Wheel 2DOF 模块中定义的轮胎参数值导入到 `tireModel` 对象。
- 导出轮胎参数 — 使用 `set` 方法将轮胎参数值从 `tireModel` 对象导出到 Combined Slip Wheel 2DOF 模块。
- 轮胎模型转换 — 使用 `convert` 方法将以下类型之一的轮胎模型转换为可导入 Combined Slip Wheel 2DOF 模块的 Magic Formula 6.2 轮胎模型：

  - Magic Formula 5.2
  - Fiala
  - Dugoff

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 导入您自己的包含 Magic Formula 系数的外部文件，并使用它们驱动对轮胎1和2建模的经验方程。您导入的文件可以是 .mat、.tir 或 .txt 类型，并且必须包含与轮胎模块中参数名称对应的参数名称。 | 使用文件中的拟合系数更新模块参数： 1. 将 **Tire type** 设置为 `External    file`。 2. 在 **Wheel and Tire Parameters** > **External    tire source** 窗格中，选择 **Select file**。 3. 选择轮胎系数文件。 4. 选择 **Update mask values from file**。在提示您确认的对话框中，点击 **OK**。模块将更新参数。 5. 选择 **Apply**。 |
| 选择 Magic Formula 内置轮胎模型之一，以驱动对轮胎 1 和 2 建模的经验方程。 | 使用内置轮胎模型中的值更新适用的模块参数： 1. 将 **Tire type** 设置为您要实现的轮胎。选项包括： - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 选择 **Update block with applicable tire    values**。在 **Tire    Parameters** 选项卡上，模块会更新适用参数，包括 **Tire nominal    section width**、**Rim    radius** 和 **Tire mass**。 3. 选择 **Apply**。 |

使用 **Brake Type** 参数选择制动。

| 操作 | Brake Type 设置 |
| --- | --- |
| 无制动 | `None` |
| 实现将制动缸压力转换为制动力的制动 | `Disc` |
| 实现将施加的力和制动几何形状转换为净制动扭矩的单工鼓式制动 | `Drum` |
| 实现作为车轮速度和施加制动压力的函数的查找表 | `Mapped` |

### Rotational Wheel Dynamics

该模块计算车轮在以下因素作用下的惯性响应：

- 车轴损耗
- 制动和驱动力矩
- 轮胎滚动阻力
- 通过轮胎-道路界面的地面接触

为实现 Magic Formula 6.2，该模块使用引用文献中的以下方程：

| 计算 | 方程 |
| --- | --- |
| 纵向力 | *Tire and Vehicle Dynamics*2 方程 4.E9 至 4.E57 |
| 侧向力 - 纯侧偏 | *Tire and Vehicle Dynamics*2 方程 4.E19 至 4.E30 |
| 侧向力 - 联合滑移 | *Tire and Vehicle Dynamics*2 方程 4.E58 至 4.E67 |
| 垂向动力学 | *Tire and Vehicle Dynamics*2 方程 4.E68、4.E1、4.E2a 和 4.E2b |
| 侧倾力矩偶 | *Tire and Vehicle Dynamics*2 方程 4.E69 |
| 滚动阻力 | - *An improved Magic Formula/Swift tyre model that   can handle inflation pressure   changes*1 方程   6.1.2 - *Tire and Vehicle   Dynamics*2   方程 4.E70 |
| 回正力矩 | *Tire and Vehicle Dynamics*2 方程 4.E31 至 4.E49 |
| 回正力矩 - 联合滑移 | *Tire and Vehicle Dynamics*2 方程 4.E71 至 4.E78  如果清除 **Include turn slip**，该模块会将这些方程中的一些设置为 1。 |

输入力矩是施加的车轴力矩、制动力矩以及由组合轮胎力矩产生的力矩之和。

Ti=Ta−Tb+Td

对于由组合轮胎力矩产生的力矩，该模块使用一阶动力学实现牵引车轮力和滚动阻力。滚动阻力具有以松弛长度参数化的时间常数。

Td(s)=1Le|ω|Res+1(FxRe+My)

制动力矩基于理想化干式离合器摩擦模型（如果选择了制动器）。根据锁止条件，该模块实现以下摩擦和动力学模型：

| 如果 | 锁止条件 | 摩擦模型 | 动力学模型 |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | 未锁止 | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | 锁止 | Tf=Ts | ω=0 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 车轮角速度 |
| *a* | 速度无关力分量 |
| *b* | 线性速度力分量 |
| *c* | 二次速度力分量 |
| *Le* | 轮胎松弛长度 |
| *J* | 转动惯量 |
| *My* | 滚动阻力矩 |
| *Ta* | 绕车轮旋转轴施加的车轴力矩 |
| *Tb* | 制动力矩 |
| *Td* | 组合轮胎力矩 |
| *Tf* | 摩擦力矩 |
| *Ti* | 净输入力矩 |
| *Tk* | 动摩擦力矩 |
| *To* | 净输出力矩 |
| *Ts* | 静摩擦力矩 |
| *Fc* | 施加的离合器力 |
| *Fx* | 由于滑移由轮胎道路界面产生的纵向力 |
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

### Tire and Wheel Coordinate Systems

为求解力和力矩，该模块使用轮胎和车轮坐标系的 Z-Up 方向。

- 轮胎坐标系轴（*XT*、*YT*、*ZT*）固定在附着于轮胎的参考系中。原点位于轮胎与地面的接触点。
- 车轮坐标系轴（*XW*、*YW*、*ZW*）固定在附着于车轮的参考系中。原点位于车轮中心。

**Z-Up Orientation**1

显示车轮平面和道路平面的 Z-Up 轮胎和车轮坐标系

### Brakes

**Disc**

如果将 **Brake Type** 参数指定为
`Disc`，则该模块实现盘式制动器。下图
展示了盘式制动器的侧视图和前视图。

盘式制动器的前视图和侧视图，显示制动片、制动盘和制动钳

盘式制动器将制动缸压力从制动缸转换为力。盘式制动器在制动片平均半径处施加该力。

该模块使用以下方程计算盘式制动器的制动力矩。

T={μPπBa2RmNpads4                当 N≠0μstaticPπBa2RmNpads4          当 N=0

Rm=Ro+Ri2

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动力矩 |
| *P* | 施加的制动压力 |
| *N* | 车轮转速 |
| *Npads* | 盘式制动器总成中的制动片数量 |
| *μstatic* | 盘式制动片-制动盘静摩擦系数 |
| *μ* | 盘式制动片-制动盘动摩擦系数 |
| *Ba* | 制动执行器缸径 |
| *Rm* | 制动片上制动力施加到制动盘的平均半径 |
| *Ro* | 制动片外半径 |
| *Ri* | 制动片内半径 |

**Drum**

如果将 **Brake Type** 参数指定为
`Drum`，则该模块实现静态（稳态）
简单鼓式制动器。简单鼓式制动器由单个双面液压
执行器和两个制动蹄组成。制动蹄不共享
公共铰链销。

简单鼓式制动器模型使用施加的力和制动器几何参数来计算每个制动蹄的净力矩。鼓式模型假设执行器和制动蹄几何参数在两侧对称，从而允许两个制动蹄使用同一组几何参数和摩擦参数。

该模块实现的方程源自
*Fundamentals of Machine Elements* 中的以下方程。

Trshoe=(πμcr(cosθ2−cosθ1)Ba22μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))PTlshoe=(πμcr(cosθ2−cosθ1)Ba2−2μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))P

T={Trshoe+Tlshoe                 当 N≠0(Trshoe+Tlshoe)μstaticμ   当 N=0

鼓式制动器侧视图

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动力矩 |
| *P* | 施加的制动压力 |
| *N* | 车轮转速 |
| *μstatic* | 盘式制动片-制动盘静摩擦系数 |
| *μ* | 盘式制动片-制动盘动摩擦系数 |
| *Trshoe* | 右制动蹄制动力矩 |
| *Tlshoe* | 左制动蹄制动力矩 |
| *a* | 从制动鼓中心到制动蹄铰链销中心的距离 |
| *c* | 从制动蹄铰链销中心到制动蹄上制动执行器连接点的距离 |
| *r* | 制动鼓内半径 |
| *Ba* | 制动执行器缸径 |
| *Θ1* | 从制动蹄铰链销中心到制动蹄上制动片材料起点的角度 |
| *Θ2* | 从制动蹄铰链销中心到制动蹄上制动片材料终点的角度 |

**Mapped**

如果将 **Brake Type** 参数指定为
`Mapped`，则该模块使用查找表来确定
制动力矩。

T={fbrake(P,N)                   当 N≠0(μstaticμ)fbrake(P,N)    当 N=0

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *T* | 制动力矩 |
| fbrake(P,N) | 制动力矩查找表 |
| *P* | 施加的制动压力 |
| *N* | 车轮转速 |
| *μstatic* | 静态条件下鼓式制动片-端面界面的摩擦系数 |
| *μ* | 盘式制动片-制动盘界面的摩擦系数 |

制动力矩查找表 fbrake(P,N) 是施加的制动压力和车轮转速的函数，其中：

- *T* 是制动力矩，单位为 N·m。
- *P* 是施加的制动压力，单位为 bar。
- *N* 是车轮转速，单位为 rpm。

制动力矩随车轮转速和施加的制动压力变化的图
