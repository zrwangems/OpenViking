---
type: simulink-block
title: 'Combined Slip Wheel STI'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'combinedslipwheelsti'
documentation_source_path: 'ref/combinedslipwheelsti.html'
language: zh-CN
chinese_source: worker-translation
---

# Combined Slip Wheel STI

## 端口

### 输入

### **Xe** — 惯性参考系中的车轮位置，`N`×`3` 向量

车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的位置，单位为 m。

向量大小为车轮数量 *N* × `3`。

### **DCM** — 方向余弦矩阵，`3`×`3` 向量

从车轮坐标系到地球固定惯性坐标系的变换矩阵。

### **Ang** — 轮辋旋转角度，`3`×`3` 向量

轮辋相对于车轮中心的旋转角度，单位为 rad。

### **Ve** — 惯性参考系中的车轮速度，`N`×`3` 向量

车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的速度，单位为 m/s。

向量大小为车轮数量 *N* × `3`。

### **Omega** — 旋转速度，`N`×`3` 向量

车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的旋转速度，单位为 rad/s。

向量大小为车轮数量 *N* × `3`。

### **OmegaWc** — 轮辋旋转速度，`scalar`

轮辋绕车轮旋转轴的旋转速度 *ω*，单位为 rad/s。

### **Road** — 车轮位置、旋转矩阵、速度，`1`×`18` 向量

包含车轮相对于地球固定惯性坐标系的位置、旋转和速度的向量。

| 向量元素 | 描述 |
| --- | --- |
| `Road(1,1)`  `Road(1,2)`  `Road(1,3)` | 车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的位置，单位为 m。 |
| `Road(1,4)`  `Road(1,5)`  `Road(1,6)`  `Road(1,7)`  `Road(1,8)`  `Road(1,9)`  `Road(1,10)`  `Road(1,11)`  `Road(1,12)` | 从车轮坐标系到地球固定惯性坐标系的变换矩阵。 |
| `Road(1,13)`  `Road(1,14)`  `Road(1,15)` | 车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的速度，单位为 m/s。 |
| `Road(1,16)`  `Road(1,17)`  `Road(1,18)` | 车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的角速度，单位为 rad/s。 |

### **ScaleFctrs** — 比例因子 `27`×`N` 数组

Magic Formula 6.2 比例因子数组。数组维度为 `27` 乘以车轮数量 *N*。

Magic Formula 6.2 方程使用比例因子来考虑静态或仿真运行时变化。名义上，大多数设置为 `1`。

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

### **Prs** — 轮胎充气压力 `scalar` | `N`×`1` 向量

轮胎充气压力 *pi*，单位为 Pa。

向量为车轮数量 *N* 乘 `1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要创建此端口，请选择 **Input tire pressure**。
### 输出

### **Info** — 模块数据总线

模块数据，以包含以下模块值的总线信号形式返回。

| 信号 | | 描述 | 单位 |
| --- | --- | --- | --- |
| `CPI_info` | `Omega` | 车轮绕车轮固定 *y* 轴的角速度 | rad/s |
| `Fx` | 沿轮胎固定 *x* 轴的车辆纵向力 | N |
| `Fy` | 沿轮胎固定 *y* 轴的车辆侧向力 | N |
| `Fz` | 沿轮胎固定 *z* 轴的车辆垂向力 | N |
| `Mx` | 绕轮胎固定 *x* 轴的侧倾力矩 | N·m |
| `My` | 绕轮胎固定 *y* 轴的滚动阻力矩 | N·m |
| `Mz` | 绕轮胎固定 *z* 轴的回正力矩 | N·m |
| `Vx` | 沿轮胎固定 *x* 轴的车辆纵向速度 | m/s |
| `Vy` | 沿轮胎固定 *y* 轴的车辆侧向速度 | m/s |
| `Re` | 加载有效半径 | m |
| `Kappa` | 纵向滑移率 | NA |
| `Alpha` | 侧偏角 | rad |
| `a` | 接地面半长 | m |
| `b` | 接地面半宽 | m |
| `Gamma` | 外倾角 | rad |
| `psidot` | 轮胎绕轮胎固定 *z* 轴的角速度（横摆角速度） | rad/s |
| `RadialDeflct` | 轮胎径向变形 | m |
| `FNormal` | 沿轮胎固定 *z* 轴作用在地面上的垂向胎侧力 | N |
| `Prs` | 轮胎充气压力 | Pa |
| `DCM` | | 从车轮坐标系到地固惯性坐标系的变换矩阵 | NA |
| `Xe` | | 车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的位置 | m |
| `Ang` | | 轮辋相对于车轮中心的旋转角度 | rad |
| `Omega` | | 轮胎绕车轮旋转轴的旋转速度，*ω* | rad/s |
| `Ve` | | 车轮分别沿惯性固定 *X*、*Y*、*Z* 轴的速度 | m/s |
| `OmegaWc` | | 轮辋绕车轮旋转轴的旋转速度，*ω* | rad/s |
| `Road` | | 包含车轮相对于地固惯性坐标系的位置、旋转和速度的向量 | NA |

### **Fwc** — 车轮中心处的力 `1`-by-`3` 向量

轮胎在车轮中心处分别沿车轮固定 *x*、*y*、*z* 轴施加的力，单位为 N。

### **Mwc** — 车轮中心处的力矩 `1`-by-`3` 向量

轮胎在车轮中心处分别绕车轮固定 *x*、*y*、*z* 轴施加的力矩，单位为 N·m。

## 参数

### 轮胎选项

### **Tire type** — 选择类型 `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 使用经验方程1, 2实现 Magic Formula 6.2。这些方程使用与模块参数对应的拟合系数。 | 使用文件中的拟合系数更新模块参数：  1. 将 **Tire type** 设置为 `External file`。 2. 在 **External tire    source** 窗格上，点击 **Select    file**。 3. 选择轮胎系数文件。 4. 点击 **Update mask values from    file**。在提示您确认的对话框中，点击    **OK**。模块将更新   参数。 5. 点击 **Apply**。 |
| 选择其中一个 Magic Formula 6.2 内置轮胎模型来驱动对轮胎建模的经验方程 1 和 2。 | 使用内置轮胎模型中的值更新适用的模块参数：  1. 将 **Tire type** 设置为您要实现的   轮胎。选项包括：  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 点击 **Update block with    applicable tire values**。在    **Tire Parameters** 选项卡上，    模块将更新适用的参数，包括    **Tire nominal section width**、    **Rim radius** 和    **Tire mass**。 3. 点击 **Apply**。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireType` |
| **值：** | `External file`（默认） | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **数据类型：** | `character vector` |

### **轮胎文件或对象，tireParamSet** — 轮胎文件 `.mat` | `.tir` | `.txt`

轮胎文件 `.tir` 或包含经验数据的对象，用于通过 Magic Formula 6.2 对轮胎的纵向和横向行为进行建模。如果提供 `.txt` 文件，请确保该文件包含与模块参数对应的名称。

使用文件中的拟合系数更新模块参数：

1. 将 **Tire type** 设置为 `External file`。
2. 在 **External tire source** 窗格上，点击 **Select file**。
3. 选择轮胎系数文件。
4. 点击 **Update mask values from file**。在提示确认的对话框中，点击 **OK**。模块将更新参数。
5. 点击 **Apply**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireParamSet` |
| **值：** | `vdynPassCar.mat`（默认） | `.tir` | `.txt` |
| **数据类型：** | `character vector` |

### **轮胎侧** — 选择轮胎侧 `Right`（默认） | `Left` | `Symmetric`

指定轮胎侧。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TireSide` |
| **值：** | `Right`（默认） | `Left` | `Symmetric` |
| **数据类型：** | `character vector` |

### **轮胎压力** — 选择轮胎侧 标量

轮胎充气压力，*p*，单位为 Pa。

#### 依赖关系

要启用此参数，请清除 **Input tire pressure**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TirePrs` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **帘布层转向** — 包含帘布层转向 `on`（默认） | `off`

选择是否在 Magic Formula 6.2 方程中包含帘布层转向。

默认情况下，模块在 Magic Formula 6.2 方程中包含帘布层转向和转弯滑移。这些方程是根据平带测试数据拟合的，可预测多种轮胎效应，包括帘布层转向和转弯滑移。如果满足以下条件，请考虑移除这些效应：

- 测试数据不包含帘布层转向或转弯滑移数据。
- 分析不需要帘布层转向或转弯滑移效应。

如果清除 **Ply steer**，模块会在内部将以下参数设置为 0：

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

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `plySteer` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

### **Turn slip** — 包含 turn slip `on`（默认） | `off`

选择以在 Magic Formula 6.2 方程中包含 ply steer。

默认情况下，模块在 Magic Formula 6.2 方程中包含 ply steer 和 turn slip。这些方程拟合于 flat-belt 测试数据，并预测多种轮胎效应，包括 ply steer 和 turn slip。如果满足以下条件，请考虑移除此类效应：

- 测试数据不包含 ply steer 或 turn slip 数据。
- 分析不需要 ply steer 或 turn slip 效应。

如果清除 **Turn slip**，模块将在内部：

- 将 Magic Formula turn slip 方程设置为 1。具体为方程 4.E77、4.E79、4.E81、4.E83、4.E84、4.E92、4.E102、4.E101 和 4.E1052。
- 使用影响水平偏移的 Magic Formula 项。
- 在 4.E272 中使用 Magic Formula 小 turn slip 值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `turnslip` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

### 绘图

### **Install Extended Tire Features** — 用于安装 Extended Tire Features for Vehicle Dynamics Blockset™ 支持包的选项 按钮

点击 **Install Extended Tire Features** 以安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包。使用该支持包，您可以从 Combined Slip Wheel STI 模块参数对话框中绘制稳态力和力矩轮胎响应。

### **Plot steady state force, moment response** — 用于绘制稳态力和力矩轮胎响应的选项 按钮

点击 **Plot steady state force, moment response** 以生成以下绘图：

- **Lateral force [N] vs Slip angle [rad]**
- **Self-aligning moment [Nm] vs Slip angle [rad]**
- **Longitudinal force [N] vs Longitudinal slip []**
- **Longitudinal force [N] vs Lateral force [N]**

#### 依赖关系

要启用此参数，请点击 **Install Extended Tire Features**。

### 仿真

### **Nominal pressure, NOMPRES** — 压力标量

标称压力，*NOMPRES*，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NOMPRES` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Maximum pressure, PRESMAX** — 最大压力标量

最大压力，*PRESMAX*，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMAX` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Minimum pressure, PRESMIN** — 最小压力标量

最小压力，*PRESMIN*，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Nominal normal force, FNOMIN** — 力标量

标称法向力，*FNOMIN*，单位为 N。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FNOMIN` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Maximum normal force, FZMAX** — 力标量

最大法向力，*FZMAX*，单位为 N。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum normal force, FZMIN** — 力标量

最小法向力，*FZMIN*，单位为 N。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — 容差标量

用于处理低速情况的速度容差，*VXLOW*，单位为 m/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VXLOW` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — 最大允许滑移率标量

最大允许滑移率（绝对值），*KPUMAX*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — 最小允许滑移率标量

最小允许滑移率（绝对值），*KPUMIN*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — 最大允许侧偏角标量

最大允许侧偏角（绝对值），*ALPMAX*，单位为 rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — 最小允许侧偏角标量

最小允许侧偏角（绝对值），*ALPMIN*，单位为
rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum allowable camber angle, CAMMAX** — 最大允许外倾角标量

最大允许外倾角 *CAMMAX*，单位为 rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable camber angle, CAMMIN** — 最小允许外倾角标量

最小允许外倾角，*CAMMIN*，单位为 rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal longitudinal speed, LONGVL** — Speed scalar

标称纵向速度，*LONGVL*，单位为 m/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LONGVL` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Default tyre side, tyreside** — Side `'Right'` (default) | char

默认轮胎侧，*tyreside*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tyreside` |
| **值**：| `'Right'` (default) | char |
| **Data Types:** | `character vector` |

### **Initial wheel rotational velocity, omegao** — Velocity scalar

初始旋转速度，指定为标量，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **值**：| scalar |
| **Data Types:** | `double` |

### Dimension

### **Tire unloaded radius, UNLOADED\_RADIUS** — Radius scalar

轮胎无载半径，*UNLOADED\_RADIUS*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `UNLOADED_RADIUS` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Tire nominal section width, WIDTH** — Width scalar

轮胎标称断面宽度，*WIDTH*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `WIDTH` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Rim radius, RIM\_RADIUS** — Radius scalar

轮辋半径，*RIM\_RADIUS*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `RIM_RADIUS` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Nominal aspect ratio, ASPECT\_RATIO** — Ratio scalar

标称扁平比，*ASPECT\_RATIO*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `ASPECT_RATIO` |
| **值**：| scalar |
| **Data Types:** | `double` |

### Inertial and Damping

### **Tire mass, MASS** — Mass scalar

轮胎质量，指定为标量，单位为 kg。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `MASS` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — Inertia scalar

轮胎转动惯量（滚动轴），指定为标量，单位为
kg·m2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `IYY` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Rotational damping, br** — Damping scalar

旋转阻尼，指定为标量，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `br` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Gravity, GRAVITY** — 重力标量

重力，*GRAVITY*，单位为 m/s^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GRAVITY` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Vertical

### **Initial tire displacement, zo** — 位移标量

初始轮胎位移，*zo*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zo` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — 速度标量

初始车轮垂向速度（车轮固定坐标系），*zdoto*，单位为 m/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zdoto` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Effective rolling radius at low load stiffness, BREFF** — 刚度标量

低载荷刚度下的有效滚动半径，*BREFF*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Effective rolling radius peak value, DREFF** — 半径标量

有效滚动半径峰值，*DREFF*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Effective rolling radius at high load stiffness, FREFF** — 半径标量

高载荷刚度下的有效滚动半径，*FREFF*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Unloaded to nominal rolling radius ratio, Q\_RE0** — 比值标量

空载与额定滚动半径之比，*Q\_RE0*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RE0` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Radius rotational speed dependence, Q\_V1** — 速度标量

半径的转速依赖性，*Q\_V1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Stiffness rotational speed dependence, Q\_V2** — 速度标量

刚度的转速依赖性，*Q\_V2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **带挠度的线性载荷变化，Q\_FZ1** — 载荷变化标量

带挠度的线性载荷变化，*Q\_FZ1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **带挠度的二次载荷变化，Q\_FZ2** — 载荷变化标量

带挠度的二次载荷变化，*Q\_FZ2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **带挠度和二次外倾的线性载荷变化，Q\_FZ3** — 载荷变化标量

带挠度和二次外倾的线性载荷变化，*Q\_FZ3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **载荷对纵向力的响应，Q\_FCX** — 力标量

载荷对纵向力的响应，*Q\_FCX*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **载荷对侧向力的响应，Q\_FCY** — 力标量

载荷对侧向力的响应，*Q\_FCY*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCY` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由于侧向载荷对侧向刚度的依赖性引起的垂直刚度变化，Q\_FCY2** — 刚度标量

由于侧向载荷对侧向刚度的依赖性引起的垂直刚度变化，*Q\_FCY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **刚度对压力的响应，PFZ1** — 刚度标量

刚度对压力的响应，*PFZ1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PFZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直轮胎刚度，VERTICAL\_STIFFNESS** — 刚度标量

垂直轮胎刚度，*VERTICAL\_STIFFNESS*，单位为 N/m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VERTICAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂直轮胎阻尼，VERTICAL\_DAMPING** — 阻尼标量

垂直轮胎阻尼，*VERTICAL\_DAMPING*，单位为 N·s/m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VERTICAL_DAMPING` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **轮辋触底偏移，BOTTOM\_OFFST** — 偏移标量

轮辋触底偏移，*BOTTOM\_OFFST*，单位为 m。

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

### **线性载荷相关外倾角对垂直刚度的影响，Q\_CAM1** — 刚度标量

线性载荷相关外倾角对垂直刚度的影响，*Q\_CAM1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **二次载荷相关外倾角对垂直刚度的影响，Q\_CAM2** — 刚度标量

二次载荷相关外倾角对垂直刚度的影响，*Q\_CAM2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **刚度和载荷及外倾角的线性缩减，Q\_CAM3** — 刚度标量

刚度和载荷及外倾角的线性缩减，*Q\_CAM3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **恒定外倾角和侧偏角对垂直刚度的影响，Q\_FYS1** — 刚度标量

恒定外倾角和侧偏角对垂直刚度的影响，*Q\_FYS1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **线性外倾角和侧偏角对垂直刚度的影响，Q\_FYS2** — 刚度标量

线性外倾角和侧偏角对垂直刚度的影响，*Q\_FYS2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **二次外倾角和侧偏角对垂直刚度的影响，Q\_FYS3** — 刚度标量

二次外倾角和侧偏角对垂直刚度的影响，*Q\_FYS3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 结构

### **纵向刚度，LONGITUDINAL\_STIFFNESS** — 刚度标量

纵向刚度，*LONGITUDINAL\_STIFFNESS*，单位为 N/m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LONGITUDINAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向刚度，LATERAL\_STIFFNESS** — 刚度标量

纵向刚度，*LATERAL\_STIFFNESS*，单位为 N/m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LATERAL_STIFFNESS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂向挠度对纵向刚度的线性影响，PCFX1** — 挠度影响标量

垂向挠度对纵向刚度的线性影响，*PCFX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂向挠度对纵向刚度的二次影响，PCFX2** — 挠度影响标量

垂向挠度对纵向刚度的二次影响，*PCFX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向刚度的压力依赖性，PCFX3** — 压力依赖性标量

纵向刚度的压力依赖性，*PCFX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂向挠度对侧向刚度的线性影响，PCFY1** — 挠度影响标量

垂向挠度对侧向刚度的线性影响，*PCFY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **垂向挠度对侧向刚度的二次影响，PCFY2** — 挠度影响标量

垂向挠度对侧向刚度的二次影响，*PCFY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向刚度的压力依赖性，PCFY3** — 压力依赖性标量

纵向刚度的压力依赖性，*PCFY3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Contact Patch

### **Contact length square root term, Q\_RA1** — 长度项标量

接触长度平方根项，*Q\_RA1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact length linear term, Q\_RA2** — 长度项标量

接触长度线性项，*Q\_RA2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact width root term, Q\_RB1** — 宽度项标量

接触宽度根项，*Q\_RB1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Contact width linear term, Q\_RB2** — 宽度项标量

接触宽度线性项，*Q\_RB2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Longitudinal

### **Cfx shape factor, PCX1** — 形状因子标量

形状因子，*Cfx*，*PCX1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Longitudinal friction at nominal normal load, PDX1** — 摩擦标量

额定法向载荷下的纵向摩擦，*PDX1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Frictional variation with load, PDX2** — 摩擦变化标量

摩擦随载荷的变化，*PDX2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Frictional variation with camber, PDX3** — 摩擦变化标量

摩擦随外倾角的变化，*PDX3*，单位为 1/rad^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Longitudinal curvature at nominal normal load, PEX1** — 曲率标量

额定法向载荷下的纵向曲率，*PEX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷的变化，PEX2** — 曲率变化标量

曲率因子随载荷的变化，*PEX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **曲率因子随载荷平方的变化，PEX3** — 曲率变化标量

曲率因子随载荷平方的变化，*PEX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向曲率因子随滑移的变化，PEX4** — 曲率标量

纵向曲率因子随滑移的变化，*PEX4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **额定法向载荷下的纵向滑移刚度，PKX1** — 刚度标量

额定法向载荷下的纵向滑移刚度，*PKX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度随载荷的变化，PKX2** — 刚度变化标量

滑移刚度随载荷的变化，*PKX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **滑移刚度指数因子，PKX3** — 滑移刚度标量

滑移刚度指数因子，*PKX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **额定法向载荷下滑移率的水平偏移，PHX1** — 滑移率偏移标量

额定法向载荷下滑移率的水平偏移，*PHX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **水平滑移率随载荷的变化，PHX2** — 滑移变化标量

水平滑移率随载荷的变化，*PHX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Vertical shift in load at nominal normal load, PVX1** — 载荷偏移标量

额定法向载荷下的载荷垂直偏移，*PVX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Variation of vertical shift with load, PVX2** — 载荷变化标量

垂直偏移随载荷的变化，*PVX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear variation of longitudinal slip stiffness with tire pressure, PPX1** — 刚度变化标量

纵向滑移刚度随轮胎压力的线性变化，*PPX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2** — 刚度变化标量

纵向滑移刚度随轮胎压力的二次变化，*PPX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear variation of peak longitudinal friction with tire pressure, PPX3** — 摩擦变化标量

峰值纵向摩擦力随轮胎压力的线性变化，*PPX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic variation of peak longitudinal friction with tire pressure, PPX4** — 摩擦变化标量

峰值纵向摩擦力随轮胎压力的二次变化，*PPX4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined slip Fx slope factor reduction, RBX1** — 联合滑移纵向力斜率因子缩减标量

联合滑移纵向力，*Fx*，斜率因子缩减，*RBX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Slip ratio Fx slope reduction variation, RBX2** — 滑移率纵向力斜率缩减变化标量

滑移率纵向力，*Fx*，斜率缩减变化，*RBX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber influence on combined slip Fx stiffness, RBX3** — 外倾对联合滑移纵向力刚度的影响标量

外倾对联合滑移纵向力 *Fx* 刚度 *RBX3* 的影响，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Shape factor for combined slip Fx reduction, RCX1** — 联合滑移纵向力缩减形状因子标量

联合滑移纵向力 *Fx* 缩减形状因子 *RCX1*，无量纲。

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

联合滑移纵向力 *Fx* 偏移因子缩减 *RHX1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Overturning moment due to camber, QSX2** — 由外倾引起的侧翻力矩标量

由外倾引起的侧翻力矩 *QSX2*，无量纲。

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

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx combined lateral force load and camber, QSX4** — 倾覆力矩标量

倾覆力矩，*Mx*，侧向力载荷与外倾组合，*QSX4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to lateral force and camber, QSX5** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和外倾引起的载荷效应，*QSX5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to B-factor, QSX6** — 倾覆力矩标量

倾覆力矩，*Mx*，由 B 因子引起的载荷效应，*QSX6*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to camber and load, QSX7** — 倾覆力矩标量

倾覆力矩，*Mx*，由外倾和载荷引起，*QSX7*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to lateral force and load, QSX8** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和载荷引起，*QSX8*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to B-factor of lateral force and load, QSX9** — 倾覆力矩标量

倾覆力矩，*Mx*，由侧向力和载荷的 B 因子引起，*QSX9*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to vertical force and camber, QSX10** — 倾覆力矩标量

倾覆力矩，*Mx*，由垂直力和外倾引起，*QSX10*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to B-factor of vertical force and camber, QSX11** — 倾覆力矩标量

倾覆力矩，*Mx*，由垂直力和外倾的 B 因子引起，*QSX11*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to squared camber, QSX12** — 侧倾力矩标量

由于外倾角平方引起的侧倾力矩，*Mx*，*QSX12*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX12` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force, QSX13** — 侧倾力矩标量

由于侧向力引起的侧倾力矩，*Mx*，*QSX13*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX13` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force with camber, QSX14** — 侧倾力矩标量

由于带外倾角的侧向力引起的侧倾力矩，*Mx*，*QSX14*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSX14` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Mx due to inflation pressure, PPMX1** — 由于压力引起的侧倾力矩标量

由于充气压力引起的侧倾力矩，*Mx*，*PPMX1*，无量纲。

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

在额定力 *FZNOM* 下的侧向曲率，*Efy*，*PEY1*，无量纲。

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

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

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **峰值刚度随外倾角平方的变化，PKY5** — 刚度变化标量

峰值刚度随外倾角平方的变化，*PKY5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy 外倾刚度因子，PKY6** — 侧向力外倾刚度因子标量

侧向力 *Fy* 外倾刚度因子，*PKY6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **外倾刚度垂直载荷依赖性，PKY7** — 刚度标量

外倾刚度垂直载荷依赖性，*PKY7*，无量纲。

#### 编程用法

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

#### 编程用法

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

#### 编程用法

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

#### 编程用法

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

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz variation with camber, PVY3** — 随外倾角变化的垂直偏移标量

垂直偏移，*Svy*，随外倾角的变化，*PVY3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PVY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Svy/Fz variation with load and camber, PVY4** — 随载荷和外倾角变化的垂直偏移标量

垂直偏移，*Svy*，随载荷和外倾角的变化，*PVY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PVY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure, PPY1** — 随压力变化的刚度标量

侧偏刚度随充气压力的变化，*PPY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2** — 随压力变化的刚度标量

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

充气压力对外倾刚度的影响，*PPY5*，无量纲。

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

### **Fy slope reduction with slip angle, RBY2** — 侧向力斜率随侧偏角缩减标量

侧向力，*Fy*，斜率随侧偏角的缩减，*RBY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBY2` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy shift reduction with slip angle, RBY3** — 侧向力随侧偏角的平移缩减标量

侧向力 *Fy* 随侧偏角的平移缩减，*RBY3*，无量纲。

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

### **Fy combined curvature factor with load, REY2** — 侧向力组合曲率因子随载荷标量

侧向力 *Fy* 组合曲率因子随载荷，*REY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REY2` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined reduction shift factor, RHY1** — 侧向力组合缩减平移因子标量

侧向力 *Fy* 组合缩减平移因子，*RHY1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHY1` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **Fy combined reduction shift factor with load, RHY2** — 侧向力组合缩减平移因子随载荷标量

侧向力 *Fy* 组合缩减平移因子随载荷，*RHY2*，无量纲。

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

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to speed^4, QSY4** — 速度四次方引起的力矩阻力标量

速度四次方引起的力矩阻力，*QSY4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to square of camber, QSY5** — 外倾角平方引起的力矩阻力标量

外倾角平方引起的力矩阻力，*QSY5*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to square of camber and load, QSY6** — 外倾角平方与载荷引起的力矩阻力标量

外倾角平方与载荷引起的力矩阻力，*QSY6*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to load, QSY7** — 载荷引起的力矩阻力标量

载荷引起的力矩阻力，*QSY7*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to pressure, QSY8** — 压力引起的力矩阻力标量

压力引起的力矩阻力，*QSY8*，无量纲。

#### 程序化使用

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

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with load, QBZ2** — 斜率随载荷变化标量

斜率随载荷变化，*QBZ2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Bpt slope variation with square of load, QBZ3** — 斜率随载荷平方变化 `0`（默认）| 标量

斜率随载荷平方变化，*QBZ3*，无量纲。

#### 程序化使用

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with square of camber, QDZ4** — 峰值拖距随外倾角平方的变化标量

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with load, QDZ7** — 峰值残余力矩随载荷的变化标量

峰值残余力矩，*Dmr*，随载荷的变化，*QDZ7*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber, QDZ8** — 峰值残余力矩随外倾角的变化标量

峰值残余力矩，*Dmr*，随外倾角的变化，*QDZ8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber and load, QDZ9** — 峰值残余力矩随外倾角和载荷的变化标量

峰值残余力矩，*Dmr*，随外倾角和载荷的变化，*QDZ9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of camber, QDZ10** — 峰值残余力矩随外倾角的变化标量

峰值残余力矩，*Dmr*，随外倾角平方的变化，*QDZ10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of load, QDZ11** — 峰值残余力矩随载荷的变化标量

峰值残余力矩，*Dmr*，随载荷平方的变化，*QDZ11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept trail curvature at FZNOM, QEZ1** — 名义力下的拖距曲率标量

拖距曲率，*Ept*，在名义力 *FZNOM* 下，*QEZ1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with load, QEZ2** — 拖距曲率随载荷变化标量

拖距曲率，*Ept* 随载荷的变化，*QEZ2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with square of load, QEZ3** — 拖距曲率随载荷平方变化标量

拖距曲率，*Ept* 随载荷平方的变化，*QEZ3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with sign of alpha-t, QEZ4** — 拖距曲率变化标量

拖距曲率，*Ept* 随 alpha-t 符号的变化，*QEZ4*，无量纲。

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

### **Ept variation with sign of alpha-t and camber, QEZ5** — 变化标量

拖距曲率，*Ept* 随 alpha-t 符号和外倾角的变化，*QEZ5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht horizontal trail shift at FZNOM, QHZ1** — 名义载荷下的水平拖距偏移标量

水平拖距偏移，*Sht*，在名义载荷 *FZNOM* 下，*QHZ1*，无量纲。

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

### **Sht variation with load, QHZ2** — 水平拖距偏移随载荷变化标量

水平拖距偏移，*Sht*，随载荷的变化，*QHZ2*，无量纲。

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

### **Sht variation with camber, QHZ3** — 水平拖距偏移随外倾角变化标量

水平拖距偏移，*Sht*，随外倾角的变化，*QHZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **随载荷和外倾变化的 Sht 变化量，QHZ4** — 随载荷和外倾变化的水平拖距偏移变化量标量

水平拖距偏移，*Sht*，随载荷和外倾的变化量，*QHZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **充气压力对拖距长度的影响，PPZ1** — 压力对拖距长度影响标量

充气压力对拖距长度的影响，*PPZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **充气压力对残余回正力矩的影响，PPZ2** — 压力对回正力矩影响标量

充气压力对残余回正力矩的影响，*PPZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 的标称值：Fx 对 Mz 的影响，SSZ1** — 纵向力对回正力矩影响标量

s/R0 的标称值：纵向力，*Fx*，对回正力矩，*Mz* 的影响，*SSZ1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 随侧向力与标称力之比的变化，SSZ2** — 随侧向力与标称力之比变化标量

随侧向力与标称力之比的变化，*SSZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 随外倾的变化，SSZ3** — 随外倾变化标量

随外倾的变化，*SSZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 随外倾和载荷的变化，SSZ4** — 随外倾和载荷变化标量

随外倾和载荷的变化，*SSZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Turnslip

### **由于旋转导致的 Fx 峰值降低，PDXP1** — 由于旋转导致的纵向力峰值降低标量

纵向力，*Fx*，由于旋转导致的峰值降低，*PDXP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with varying load, PDXP2** — 由于旋转导致的纵向力峰值降低标量

纵向力 *Fx* 由于旋转并随载荷变化的峰值降低，*PDXP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with slip ratio, PDXP3** — 由于旋转导致的纵向力峰值降低标量

纵向力 *Fx* 由于旋转并随滑移率变化的峰值降低，*PDXP3*，无量纲。

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

侧向力 *Fy* 由于旋转并随载荷变化的峰值降低，*PDYP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin with slip angle, PDYP3** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转并随侧偏角变化的峰值降低，*PDYP3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to square root of spin, PDYP4** — 由于旋转导致的侧向力峰值降低标量

侧向力 *Fy* 由于旋转平方根导致的峰值降低，*PDYP4*，无量纲。

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

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit, PHYP2** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的最大侧向偏移限值，*PHYP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit with load, PHYP3** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应在载荷下的最大侧向偏移限值，*PHYP3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response lateral shift curvature factor, PHYP4** — 侧向力与侧偏角响应标量

侧向力 *Fy* 与侧偏角响应的侧向偏移曲率因子，*PHYP4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin, PECP1** — 外倾刚度折减标量

由于旋转引起的外倾刚度折减，*PECP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin with load, PECP2** — 外倾刚度折减标量

由于旋转在载荷下引起的外倾刚度折减，*PECP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip pneumatic trail reduction factor, QDTP1** — 转向滑移回正力臂折减因子标量

转向滑移回正力臂折减因子，*QDTP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDTP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn moment for constant turning and zero longitudinal speed, QCRP1** — 恒定转向力矩标量

恒定转向和零纵向速度下的转向力矩，*QCRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip moment increase with spin at 90deg slip angle, QCRP2** — 转向滑移力矩标量

在90度侧偏角下随旋转增加的转向滑移力矩，*QCRP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧滑引起的残余回正力矩减小量，QBRP1** — 侧滑引起的残余回正力矩减小量标量

侧滑引起的残余回正力矩减小量，*QBRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **转弯滑移力矩峰值大小，QDRP1** — 转弯滑移力矩峰值大小标量

转弯滑移力矩峰值大小，*QDRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **转弯滑移力矩曲率，QDRP2** — 转弯滑移力矩曲率标量

转弯滑移力矩曲率，*QDRP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

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

**在 R2021b 中引入**

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

### R2024b：新增信号添加到 **Info** 端口总线

从 R2024b 开始，**Info** 端口总线包含以下新信号。

| 信号 | 描述 |
| --- | --- |
| `RadialDeflct` | 轮胎径向变形 |

### R2024a：绘制稳态力和力矩响应

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，您可以使用新的 **Plot steady state force, moment response** 按钮生成绘图。

### R2022b：新增 **Ply steer** 和 **Turn slip** 参数

从 R2022b 开始，Combined Slip Wheel STI 模块包含 **Ply steer** 和 **Turn slip** 参数。要从这些模块的 Magic Formula 实现中移除 ply steer 和 turn slip，请清除 **Ply steer** 和 **Turn slip** 参数。

## 描述

符合 STI Tydex 标准的组合滑移车轮

Combined Slip Wheel STI 模块实现了符合标准轮胎接口（STI）轮胎数据交换格式（TYDEX）[3] 标准的 Magic Formula[1][2] 6.2 所描述的车轮纵向和横向行为。您可以导入自己的轮胎模型或使用内置轮胎模型。在需要低频轮胎-道路相互作用以确定车辆加速度和车轮滚动阻力的传动系统和车辆仿真中使用该模块。该模块适用于需要组合横向滑移的应用，例如横向运动和横摆稳定性研究。

基于车轮旋转速度、纵向和横向速度、车轮外倾角以及充气压力，该模块确定所有六个自由度（DOF）中的垂向运动、力和力矩。使用垂向自由度来研究来自道路轮廓或底盘运动的轮胎-悬架共振。

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用以下附加功能：

- 绘图生成 — 点击 **Plot steady state force, moment response** 按钮生成以下绘图：

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle [rad]**
  - **Longitudinal force [N] vs Longitudinal slip []**
  - **Longitudinal force [N] vs Lateral force [N]**
- 导入轮胎参数 — 使用 `tireModel.get` 方法将 Combined Slip Wheel STI 模块中定义的轮胎参数值导入到 `tireModel` 对象。
- 导出轮胎参数 — 使用 `set` 方法将轮胎参数值从 `tireModel` 对象导出到 Combined Slip Wheel STI 模块。
- 轮胎模型转换 — 使用 `convert` 方法将以下类型之一的轮胎模型转换为可导入 Combined Slip Wheel STI 模块的 Magic Formula 6.2 轮胎模型：

  - Magic Formula 5.2
  - Fiala
  - Dugoff

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 使用经验方程1, 2实现 Magic Formula 6.2。这些方程使用与模块参数对应的拟合系数。 | 使用文件中的拟合系数更新模块参数： 1. 将 **Tire type** 设置为 `External file`。 2. 在 **External tire source** 窗格上，点击 **Select file**。 3. 选择轮胎系数文件。 4. 点击 **Update mask values from file**。在提示您确认的对话框中，点击 **OK**。模块将更新参数。 5. 点击 **Apply**。 |
| 选择 Magic Formula 6.2 内置轮胎模型之一来驱动模拟轮胎 1 和 2 的经验方程。 | 使用内置轮胎模型中的值更新适用的模块参数： 1. 将 **Tire type** 设置为您要实现的轮胎。选项包括： - `Light passenger car 205/60R15` - `Light passenger car 245/60R16` - `Mid-size passenger car 235/45R18` - `Performance car 225/40R19` - `SUV 265/50R20` - `Light truck 275/65R18` - `Commercial truck 295/75R22.5` 2. 点击 **Update block with applicable tire values**。在 **Tire Parameters** 选项卡上，模块更新适用的参数，包括 **Tire nominal section width**、**Rim radius** 和 **Tire mass**。 3. 点击 **Apply**。 |

### Rotational Wheel Dynamics

该模块计算车轮在以下因素作用下的惯性响应：

- 车轴损耗
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

### STI Wheel Coordinate System

该模块使用固定在附着于车轮的参考系中的车轮坐标系轴
(*XW*、
*YW*、
*ZW*)。原点位于车轮中心。

STI 车轮坐标系以蓝色显示。

**注意**

STI 车轮坐标系（蓝色）等效于 TYDEX
中心轴坐标系。

1

Z-Up 轮胎和车轮坐标系，显示车轮平面和道路平面

| 轴 | 描述 |
| --- | --- |
| *XW* | *XW* 和 *YW* 平行于车轮平面：  - *XW*   平行于局部道路平面。 - *YW*   平行于车轮旋转轴。 |
| *YW* |
| *ZW* | *ZW* 指向上方。 |
