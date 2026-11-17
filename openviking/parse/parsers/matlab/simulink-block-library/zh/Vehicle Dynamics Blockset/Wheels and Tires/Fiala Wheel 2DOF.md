---
type: simulink-block
title: 'Fiala Wheel 2DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'fialawheel2dof'
documentation_source_path: 'ref/fialawheel2dof.html'
language: zh-CN
chinese_source: worker-translation
---

# Fiala Wheel 2DOF

## 端口

### 输入

### **BrkPrs** — 制动压力标量 | *N*×`1` 向量

制动压力，单位为 Pa。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要启用此端口，将 **Brake Type** 参数设置为以下类型之一：

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — 车轴扭矩标量 | *N*×`1` 向量

车轴扭矩 *Ta*，绕车轮旋转轴，单位为 N·m。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Vx** — 纵向速度标量 | *N*×`1` 向量

车轴纵向速度 *Vx*，沿轮胎固定 *x* 轴，单位为 m/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Vy** — 侧向速度标量 | *N*×`1` 向量

车轴侧向速度 *Vy*，沿轮胎固定 *y* 轴，单位为 m/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Camber** — 倾角标量 | *N*×`1` 向量

外倾角 *ɣ*，或倾角 *ε*，单位为 rad。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **YawRate** — 轮胎角速度标量 | *N*×`1` 向量

轮胎角速度 *r*，绕轮胎固定 *z* 轴（横摆角速度），单位为 rad/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Prs** — 轮胎充气压力标量 | *N*×`1` 向量

轮胎充气压力 *pi*，单位为 Pa。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Gnd** — 地面位移标量 | *N*×`1` 向量

沿轮胎固定 *z* 轴的地面位移，单位为 m。正输入产生车轮抬升。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fext** — 施加到轮胎的车轴力标量 | *N*×`1` 向量

施加到轮胎的车轴力 *Fext*，沿车辆固定 *z* 轴（正输入压缩轮胎），单位为 N。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要启用此参数，将 **Vertical Motion** 设置为 `None` 或 `Magic Formula`。

### **RadialDeflct** — 轮胎径向变形标量 | *N*×`1` 向量

轮胎径向变形 *RadialDeflct*。此值直接用于有效半径计算。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要启用此端口，将 **Vertical Motion** 设置为 `External Deflection`。

### **ScaleFctrs** — 比例因子标量 | *N*×`1` 向量

用于考虑摩擦系数变化的比例因子。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。
### 输出

### **Info** — 模块数据总线

模块数据，以包含这些模块值的总线信号形式返回。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `AxlTrq` | 绕车轮固定 *y* 轴的车轴扭矩 | N·m |
| `Omega` | 绕车轮固定 *y* 轴的车轮角速度 | rad/s |
| `Fx` | 沿轮胎固定 *x* 轴的车辆纵向力 | N |
| `Fy` | 沿轮胎固定 *y* 轴的车辆侧向力 | N |
| `Fz` | 沿轮胎固定 *z* 轴的车辆垂向力 | N |
| `Mx` | 绕轮胎固定 *x* 轴的侧倾力矩 | N·m |
| `My` | 绕轮胎固定 *y* 轴的滚动阻力扭矩 | N·m |
| `Mz` | 绕轮胎固定 *z* 轴的回正力矩 | N·m |
| `Vx` | 沿轮胎固定 *x* 轴的车辆纵向速度 | m/s |
| `Vy` | 沿轮胎固定 *y* 轴的车辆侧向速度 | m/s |
| `Re` | 加载有效半径 | m |
| `Kappa` | 纵向滑移率 | NA |
| `Alpha` | 侧偏角 | rad |
| `a` | 接地面半长 | m |
| `b` | 接地面半宽 | m |
| `Gamma` | 外倾角 | rad |
| `psidot` | 绕轮胎固定 *z* 轴的轮胎角速度（横摆角速度） | rad/s |
| `BrkTrq` | 绕车辆固定 *y* 轴的制动扭矩 | N·m |
| `BrkPrs` | 制动压力 | Pa |
| `z` | 沿轮胎固定 *z* 轴的车轴垂向位移 | m |
| `zdot` | 沿轮胎固定 *z* 轴的车轴垂向速度 | m/s |
| `Gnd` | 沿轮胎固定 *z* 轴的地面位移（正输入产生车轮抬升） | m |
| `GndFz` | 沿轮胎固定 *z* 轴作用在地面上的垂向胎侧力 | N |
| `Prs` | 轮胎充气压力 | Pa |
| `WhlTrq` | 车轮扭矩 | N·m |
| `RL` | 加载半径 | m |
| `RadialDeflct` | 轮胎径向变形 | m |

### **Omega** — 车轮角速度 标量 | *N*×`1` 向量

绕车轮固定 *y* 轴的车轮角速度，*ω*，单位为 rad/s。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fx** — 纵向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *x* 轴作用在车轴上的纵向力，*Fx*，单位为 N。正力作用使车辆向前运动。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fy** — 侧向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *y* 轴作用在车轴上的侧向力，*Fy*，单位为 N。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fz** — 垂向车轴力 标量 | *N*×`1` 向量

沿轮胎固定 *z* 轴作用在车轴上的垂向力，*Fz*，单位为 N。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **Mx** — 侧倾力矩 标量 | *N*×`1` 向量

绕轮胎固定 *x* 轴作用在车轴上的纵向力矩，*Mx*，单位为 N·m。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **My** — 滚动阻力矩 标量 | *N*×`1` 向量

绕轮胎固定 *y* 轴作用在车轴上的侧向力矩，*My*，单位为 N·m。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

### **Mz** — 回正力矩 标量 | *N*×`1` 向量

绕轮胎固定 *z* 轴作用在车轴上的垂向力矩，*Mz*，单位为 N·m。

向量为车轮数量，*N*，×`1`。如果提供标量值，模块假定车轮数量为一。

## 参数

### 模块选项

### **Tire type** — 选择类型 `User defined`（默认）| `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

使用 **Tire type** 参数可以输入轮胎参数值或选择拟合的轮胎参数集。

| 目标 | 操作 |
| --- | --- |
| 输入用户定义的轮胎参数值。 | 使用用户定义的参数值更新模块参数： 1. 将 **Tire type** 设置为 `User    defined`。 2. 在 **Wheel and Tire Parameters**    部分中，输入用户定义的值。 3. 点击 **Apply**。 |
| 选择内置的 Fiala 轮胎模型之一来驱动横向和纵向计算。[link]。 | 使用内置轮胎模型中的值更新适用的模块参数： 1. 将 **Tire type** 设置为您    要实现的轮胎。选项包括：  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 点击 **Update block with applicable tire    values**。在 **Wheel and Tire    Parameters** 部分中，模块会更新    适用的 **Longitudinal and Lateral**    参数。 3. 点击 **Apply**。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tireType` |
| **值**：| `External file`（默认）| `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **Data Types:** | `character vector` |

### **Brake type** — 制动类型 `None` | `Disc` | `Drum` | `Mapped`

使用 **Brake Type** 参数选择制动器。

| 操作 | Brake Type 设置 |
| --- | --- |
| 无制动 | `None` |
| 实现将制动缸压力转换为制动力的制动器 | `Disc` |
| 实现将施加力和制动器几何参数转换为净制动扭矩的单工鼓式制动器 | `Drum` |
| 实现作为车轮转速和施加制动压力函数的查找表 | `Mapped` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **值**：| `None` | `Disc` | `Drum` | `Mapped` |
| **Data Types:** | `character vector` |

### **Rolling Resistance** — 滚动阻力扭矩 `None`（默认）| `Pressure and velocity` | `ISO 28580` | `Magic Formula` | `Mapped torque`

要计算滚动阻力扭矩，请指定以下 **Rolling Resistance** 参数之一。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 无 |
| `Pressure and velocity` | *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance* 中的方法。滚动阻力是轮胎压力、法向力和速度的函数。 |
| `ISO 28580` | ISO 28580:2018，*Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results* 中指定的方法。 |
| `Magic Formula` | *Tire and Vehicle Dynamics* 中 4.E70 的魔术公式方程。魔术公式是基于拟合系数的经验方程。 |
| `Mapped torque` | 作为法向力和自旋轴纵向速度函数的查找表。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rollingType` |
| **值：** | `None`（默认） | `Pressure and velocity` | `ISO 28580` | `Magic Formula` | `Mapped torque` |
| **数据类型：** | `character vector` |

#### 依赖关系

每个 **Rolling Resistance** 设置都会启用额外的参数。

| 设置 | 启用的参数 |
| --- | --- |
| `Pressure and velocity` | - **Velocity independent force coefficient, aMy** - **Linear velocity force component, bMy** - **Quadratic velocity force component, cMy** - **Tire pressure exponent, alphaMy** - **Normal force exponent, betaMy** |
| `ISO 28580` | - **Parasitic losses force, Fpl** - **Rolling resistance constant, Cr** - **Thermal correction factor, Kt** - **Measured temperature, Tmeas** - **Parasitic losses force, Fpl** - **Ambient temperature, Tamb** |
| `Magic Formula` | **Rolling resistance torque coefficient, QSY**  **Longitudinal force rolling resistance coefficient, QSY2**  **Linear rotational speed rolling resistance coefficient, QSY3**  **Quartic rotational speed rolling resistance coefficient, QSY4**  **Camber squared rolling resistance torque, QSY5**  **Load based camber squared rolling resistance torque, QSY6**  **Normal load rolling resistance coefficient, QSY7**  **Pressure load rolling resistance coefficient, QSY8**  **Rolling resistance scaling factor, lam\_My** |
| `Mapped torque` | **Spin axis velocity breakpoints, VxMy**  **Normal force breakpoints, FzMy**  **Rolling resistance torque map, MyMap** |

### **Vertical Motion** — 垂直运动 `None`（默认） | `Mapped stiffness and damping` | `External deflection`

要计算垂直运动，请指定以下 **Vertical Motion** 参数之一。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 模块将施加的底盘力直接传递到滚动阻力和纵向力计算。 |
| `Mapped stiffness and damping` | 垂直运动取决于车轮刚度和阻尼。刚度是轮胎侧壁位移和压力的函数。阻尼是轮胎侧壁速度和压力的函数。 |
| `External deflection` | 模块在有效半径计算中直接使用定义的侧壁变形量。 |

#### 依赖关系

将 **Vertical Motion** 设置为 `Mapped stiffness and damping` 会启用以下参数：

| 设置 | 启用的参数 |
| --- | --- |
| `Mapped stiffness and damping` | - **Wheel mass, MASS** - **Initial tire displacement, zo** - **Initial velocity, zdoto** - **Initial wheel vertical velocity (wheel fixed frame), zdoto** - **Vertical deflection breakpoints, zFz** - **Pressure breakpoints, pFz** - **Force due to deflection, Fzz** - **Vertical velocity breakpoints, zdotFz** - **Force due to velocity, Fzzdot** |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `vertType` |
| **值：** | `None`（默认） | `Mapped stiffness and damping` | `External deflection` |
| **数据类型：** | `character vector` |

### 纵向和横向

### **Longitudinal stiffness, Ckappa** — 纵向刚度 `1e7`（默认） | 标量 | *N*×`1` 向量

纵向刚度，*Cκ*，指定为标量或 *N*×`1` 向量，单位为 N。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ckappa` |
| **值：** | `1e7`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **侧偏刚度，Calpha** — 侧偏刚度 `4.5e4`（默认）| 标量 | *N*×`1` 向量

侧偏刚度，
*Cα*，指定为
标量或 *N*×`1` 向量，单位为 N/rad。
如果指定标量，模块将对所有车轮使用该值。如果
指定向量，则必须为其他
纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `Calpha` |
| **值：** | `4.5e4`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **外倾刚度，Cgamma** — 外倾刚度 `1e3`（默认）| 标量 | *N*×`1` 向量

外倾刚度，
*Cɣ*，指定为
标量或 *N*×`1` 向量，单位为 N/rad。
如果指定标量，模块将对所有车轮使用该值。如果
指定向量，则必须为其他
纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `Cgamma` |
| **值：** | `1e3`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **动摩擦，muMin** — 动摩擦 `0.8`（默认）| 标量 | *N*×`1` 向量

动摩擦，
*μk*，指定为
标量或 *N*×`1` 向量，
无量纲。如果指定标量，模块将对
所有车轮使用该值。如果指定向量，则必须为
其他纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `muMin` |
| **值：** | `0.8`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **静摩擦，muMax** — 静摩擦 `1`（默认）| 标量 | *N*×`1` 向量

静摩擦，
*μs*，指定为
标量或 *N*×`1` 向量，
无量纲。如果指定标量，模块将对
所有车轮使用该值。如果指定向量，则必须为
其他纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `muMax` |
| **值：** | `1`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **纵向松弛长度，Lrelx** — 纵向松弛长度 `0.05`（默认）| 标量 | *N*×`1` 向量

纵向松弛长度，
*Lrelx*，指定为
标量或 *N*×`1` 向量，单位为 m。如果
指定标量，模块将对所有车轮使用该值。如果
指定向量，则必须为其他纵向
和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lrelx` |
| **值：** | `0.05`（默认） | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **横向松弛长度，Lrely** — 横向松弛长度 `0.15`（默认） | 标量 | *N*×`1` 向量

横向松弛长度，*Lrely*，单位为 m/rad。

横向松弛长度，*Lrely*，指定为标量或 *N*×`1` 向量，单位为 m/rad。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他纵向和横向参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lrely` |
| **值：** | `0.15`（默认） | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### 滚动阻力

#### 压力和速度

### **速度无关力系数，aMy** — 速度无关力系数 `84e-4`（默认） | 标量

速度无关力系数，*a*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `aMy` |
| **值：** | `84e-4`（默认） | 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `压力和速度`。

### **线性速度力分量，bMy** — 线性速度力分量 `6.2e-4`（默认） | 标量

线性速度力分量，*b*，单位为 s/m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bMy` |
| **值：** | `6.2e-4`（默认） | 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `压力和速度`。

### **二次速度力分量，cMy** — 二次速度力分量 `1.6e-4`（默认） | 标量

二次速度力分量，*c*，单位为 s^2/m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cMy` |
| **值：** | `1.6e-4`（默认） | 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `压力和速度`。

### **轮胎压力指数，alphaMy** — 轮胎压力指数 `-0.003`（默认） | 标量

轮胎压力指数，*ɑ*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `alphaMy` |
| **值：** | `-0.003`（默认） | 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `压力和速度`。

### **法向力指数，betaMy** — 法向力指数 `0.97`（默认） | 标量

法向力指数，*β*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `betaMy` |
| **值：** | `0.97`（默认） | 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Pressure
and velocity`。

#### ISO 28580

### **寄生损耗力，Fpl** — 寄生力损耗 `10`（默认）| 标量

寄生力损耗，*Fpl*，单位为 N。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fpl` |
| **值：** | `10`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

### **滚动阻力常数，Cr** — 滚动阻力常数 `1e-3`（默认）| 标量

滚动阻力常数，*Cr*，单位为 N/kN。ISO
28580 规定滚动阻力单位为每千牛顿法向载荷对应一牛顿牵引阻力。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cr` |
| **值：** | `1e-3`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

### **热修正因子，Kt** — 热修正因子 `0.008`（默认）| 标量

热修正因子，*Kt*，单位为 1/degC。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kt` |
| **值：** | `0.008`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

### **测量温度，Tmeas** — 测试期间的温度 `298.15`（默认）| 标量

轮胎测试期间轮胎附近的测量环境温度，*Tmeas*，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmeas` |
| **值：** | `298.15`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

### **环境温度，Tamb** — 应用环境中的温度 `298.15`（默认）| 标量

应用环境中轮胎附近的测量环境温度，*Tamb*，单位为 K。例如，测量环境温度是车辆在道路上行驶时轮胎附近的环境温度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `298.15`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

### **输入环境温度** — 输入环境温度的选项 `off`（默认）| on

选择以创建输入端口 **Tamb**，用于输入测量环境温度。

测量环境温度，*Tamb*，是应用环境中轮胎附近的温度，单位为 K。例如，测量环境温度是车辆在道路上行驶时轮胎附近的环境温度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tamb` |
| **值：** | `off`（默认）| on |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `ISO
28580`。

#### Magic Formula

### **滚动阻力扭矩系数，QSY1** — 扭矩系数 `0.007`（默认）| 标量

滚动阻力扭矩系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY1` |
| **值：** | `0.007`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **纵向力滚动阻力系数，QSY2** — 力阻力系数 `0`（默认）| 标量

纵向力滚动阻力系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY2` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **线性转速滚动阻力系数，QSY3** — 线性速度系数 `0.0015`（默认）| 标量

线性转速滚动阻力系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY3` |
| **值：** | `0.0015`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **四次转速滚动阻力系数，QSY4** — 四次速度系数 `8.5e-05`（默认）| 标量

四次转速滚动阻力系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY4` |
| **值：** | `8.5e-05`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **外倾角平方滚动阻力扭矩，QSY5** — 外倾角阻力扭矩 `0`（默认）| 标量

外倾角平方滚动阻力扭矩，单位为 1/rad^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY5` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **基于载荷的外倾角平方滚动阻力扭矩，QSY6** — 载荷阻力扭矩 `0`（默认）| 标量

基于载荷的外倾角平方滚动阻力扭矩，单位为 1/rad^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY6` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `Magic Formula`。

### **法向载荷滚动阻力系数，QSY8** — 法向阻力系数 `0.9`（默认）| 标量

法向载荷滚动阻力系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY8` |
| **值：** | `0.9`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Magic Formula`。

### **Pressure load rolling resistance coefficient, QSY8** — 压力阻力系数 `-0.4`（默认）| 标量

压力载荷滚动阻力系数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY8` |
| **值：** | `-0.4`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Magic Formula`。

### **Rolling resistance scaling factor, lam\_My** — 缩放因子 `1`（默认）| 标量

滚动阻力缩放因子，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `lam_My` |
| **值：** | `1`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Magic Formula`。

#### 映射

### **Spin axis velocity breakpoints, VxMy** — 自旋轴速度断点 `-20:1:20`（默认）| 向量

自旋轴速度断点，单位为 m/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VxMy` |
| **值：** | `-20:1:20`（默认）| 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Mapped torque`。

### **Normal force breakpoints, FzMy** — 法向力断点 `0:200:1e4`（默认）| 向量

法向力断点，单位为 N。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FzMy` |
| **值：** | `0:200:1e4`（默认）| 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Mapped torque`。

### **Rolling resistance torque map, MyMap** — 滚动阻力矩映射数组

滚动阻力矩与车轴速度和法向力的关系，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MyMap` |
| **值：** | 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Rolling Resistance** 设置为 `Mapped torque`。

### 对齐

### **Tire nominal section width, WIDTH** — 轮胎名义断面宽度 标量

轮胎名义断面宽度，*WIDTH*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WIDTH` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear yaw rate resistance, bMz** — 线性横摆角速度阻力 `0` | 标量

线性横摆角速度阻力，*bMz*，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bMz` |
| **值：** | `0` | 标量 |
| **数据类型：** | `double` |

### Brake

### **静摩擦系数，mu\_static** — 静摩擦系数 `0.3`（默认）| 标量 | *N*×`1` 向量

静摩擦系数，指定为标量或 *N*×`1` 向量，无量纲。如果指定为标量，则该模块对所有车轮使用该值。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`、`Drum` 或 `Mapped`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_static` |
| **值：** | `0.3`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **动摩擦系数，mu\_kinetic** — 动摩擦 `0.2`（默认）| 标量 | *N*×`1` 向量

动摩擦系数，指定为标量或 *N*×`1` 向量，无量纲。如果指定为标量，则该模块对所有车轮使用该值。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`、`Drum` 或 `Mapped`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_kinetic` |
| **值：** | `0.2`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

#### Disc

### **盘式制动器执行器孔径，disc\_abore** — 孔径距离 `0.05`（默认）| 标量 | *N*×`1` 向量

盘式制动器执行器孔径，指定为标量或 *N*×`1` 向量，单位为 m。如果指定为标量，则该模块对所有车轮使用该值。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `disc_abore` |
| **值：** | `0.05`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **制动片平均半径，Rm** — 半径 `0.177`（默认）| 标量 | *N*×`1` 向量

制动片平均半径，指定为标量或 *N*×`1` 向量，单位为 m。如果指定为标量，则该模块对所有车轮使用该值。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rm` |
| **值：** | `0.177`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **制动片数量，num\_pads** — 制动片数量 `2`（默认）| 标量 | *N*×`1` 向量

制动片数量，指定为标量或 *N*×`1` 向量，无量纲。如果指定为标量，模块将该值用于所有车轮。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Disc`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `num_pads` |
| **值：** | `2`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

#### 鼓式

### **鼓式制动器执行器孔径，drum\_abore** — 孔径距离 `0.0508`（默认）| 标量 | *N*×`1` 向量

鼓式制动器执行器孔径，指定为标量或 *N*×`1` 向量，单位为 m。如果指定为标量，模块将该值用于所有车轮。如果指定为向量，则必须为其他制动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_abore` |
| **值：** | `0.0508`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **制动蹄销到制动鼓中心距离，drum\_a** — 制动蹄销到制动鼓中心距离 `0.123`（默认）| 标量

制动蹄销到制动鼓中心距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_a` |
| **值：** | `0.123`（默认）| 标量 |
| **数据类型：** | `double` |

### **制动蹄销中心到力作用点距离，drum\_c** — 制动蹄销中心到力作用点距离 `0.212`（默认）| 标量

制动蹄销中心到力作用点距离，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_c` |
| **值：** | `0.212`（默认）| 标量 |
| **数据类型：** | `double` |

### **制动鼓内半径，drum\_r** — 制动鼓内半径 `0.15`（默认）| 标量

制动鼓内半径，单位为 m。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_r` |
| **值：** | `0.15`（默认）| 标量 |
| **数据类型：** | `double` |

### **制动蹄销到制动片起始角度，drum\_theta1** — 制动蹄销到制动片起始角度 `0`（默认）| 标量

制动蹄销到制动片起始角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为 `Drum`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta1` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

### **制动蹄销到制动片终止角度，drum\_theta2** — 制动蹄销到制动片终止角度 `126`（默认）| 标量

制动蹄销到制动片终止角度，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Drum`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `drum_theta2` |
| **值：** | `126`（默认） | 标量 |
| **数据类型：** | `double` |

#### Mapped

### **Brake actuator pressure breakpoints, brake\_p\_bpt** — 制动执行器压力断点向量

制动执行器压力断点，单位为 bar。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_p_bpt` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### **Wheel speed breakpoints, brake\_n\_bpt** — 车轮速度断点向量

车轮速度断点，单位为 rpm。

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brake_n_bpt` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### **Brake torque map, f\_brake\_t** — 制动扭矩查找表数组

制动扭矩的查找表 fbrake(P,N) 是所施加制动压力和车轮速度的函数，其中：

- *T* 是制动扭矩，单位为 N·m。
- *P* 是所施加的制动压力，单位为 bar。
- *N* 是车轮速度，单位为 rpm。

显示制动扭矩作为车轮速度和所施加制动压力函数的图

#### 依赖关系

要启用此参数，请将 **Brake Type** 设置为
`Mapped`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_brake_t` |
| **值：** | 向量 |
| **数据类型：** | `double` |

### Wheel

### **Rotational damping, br** — 旋转阻尼标量 | *N*×`1` 向量

旋转阻尼，指定为标量或 *N*×`1` 向量，单位为 N·m·s/rad。如果指定标量，模块将对所有车轮使用该值。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `br` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — 轮胎旋转惯量标量 | *N*×`1` 向量

轮胎旋转惯量（滚动轴），指定为标量或 *N*×`1` 向量，单位为 kg·m2。如果指定标量，模块将对所有车轮使用该值。如果指定向量，则必须为其他旋转参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IYY` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **初始车轮转速，omegao** — 初始车轮转速标量 | *N*×`1` 向量

初始车轮转速，指定为标量或 *N*×`1` 向量，单位为 rad/s。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他转动参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegao` |
| **值：** | 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **轮胎无载半径，UNLOADED\_RADIUS** — 轮胎无载半径 `0.309384029954441`（默认）| 标量

轮胎无载半径，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `UNLOADED_RADIUS` |
| **值：** | `0.309384029954441`（默认）| 标量 |
| **数据类型：** | `double` |

### 垂直

### **轮胎质量，m** — 轮胎质量 `9.46491996974568`（默认）| 标量 | *N*×`1` 向量

轮胎质量，指定为标量或 *N*×`1` 向量，单位为 kg。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他垂直参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `MASS` |
| **值：** | `9.46491996974568`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **初始轮胎位移，zo** — 初始轮胎位移 `0`（默认）| 标量 | *N*×`1` 向量

初始轮胎位移，指定为标量或 *N*×`1` 向量，单位为 m。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他垂直参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zo` |
| **值：** | `0`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **初始车轮垂直速度（车轮固定坐标系），zdoto** — 初始车轮速度 `0`（默认）| 标量 | *N*×`1` 向量

初始车轮垂直速度，指定为标量或 *N*×`1` 向量，单位为 m/s。如果指定为标量，模块将对所有车轮使用该值。如果指定为向量，则必须为其他垂直参数指定向量。

*N* 是车轮数量，必须与输入信号维度匹配。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zdoto` |
| **值：** | `0`（默认）| 标量 | *N*×`1` 向量 |
| **数据类型：** | `double` |

### **重力加速度，GRAVITY** — 重力加速度 `-9.81`（默认）| 标量

重力加速度，单位为 m/s^2。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `GRAVITY` |
| **值：** | `-9.81`（默认） | 标量 |
| **数据类型：** | `double` |

#### 映射刚度和阻尼

### **垂直变形断点，zFz** — 垂直变形断点 `[0 .01 .1]`（默认） | 向量

对应于力表的侧壁变形断点向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `zFz` |
| **值：** | `[0 .01 .1]`（默认） | 向量 |
| **数据类型：** | `double` |

### **压力断点，pFz** — 压力断点 `[10000 1000000]`（默认） | 向量

对应于力表的压力数据点向量，单位为 Pa。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `pFz` |
| **值：** | `[10000 1000000]`（默认） | 向量 |
| **数据类型：** | `double` |

### **由变形引起的力，Fzz** — 由变形引起的力 `[0 1e3 1e4; 0 1e4 1e5]`（默认） | 向量

由侧壁变形和压力沿车轮固定 *z* 轴引起的力，单位为 N。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `Fzz` |
| **值：** | `[0 1e3 1e4; 0 1e4 1e5]`（默认） | 向量 |
| **数据类型：** | `double` |

### **垂直速度断点，zdotFz** — 垂直速度断点 `[-20 0 20]`（默认） | 向量

对应于由速度引起的力表的侧壁速度断点向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `zdotFz` |
| **值：** | `[-20 0 20]`（默认） | 向量 |
| **数据类型：** | `double` |

### **由速度引起的力，Fzzdot** — 由速度引起的力 `[500 0 -500;250 0 -250]`（默认） | 数组

由侧壁速度和压力沿车轮固定 *z* 轴引起的力，单位为 N。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `Mapped
stiffness and damping`。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `Fzzdot` |
| **值：** | `[500 0 -500;250 0 -250]`（默认） | 数组 |
| **数据类型：** | `double` |

### 仿真设置

### **最大法向力，FZMAX** — 最大法向力 `10000`（默认） | 标量

最大法向力，单位为 N。用于所有垂直力计算。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMAX` |
| **值：** | `10000`（默认） | 标量 |
| **数据类型：** | `double` |

### **最小法向力，FZMIN** — 最小法向力 `0`（默认） | 标量

最小法向力，单位为 N。用于所有垂直力计算。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMIN` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **最大压力，PRESMAX** — 最大压力 `1003118`（默认） | 标量

最大压力，*PRESMAX*，单位为 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMAX` |
| **值：** | `1003118`（默认） | 标量 |
| **数据类型：** | `double` |

### **最小压力，PRESMIN** — 最小压力 `9982`（默认） | 标量

最小压力，*PRESMIN*，单位为 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMIN` |
| **值：** | `9982`（默认） | 标量 |
| **数据类型：** | `double` |

### **最大允许滑移率（绝对值），KPUMAX** — 最大允许滑移率 `0.999`（默认） | 标量

最大允许滑移率（绝对值），*KPUMAX*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMAX` |
| **值：** | `0.999`（默认） | 标量 |
| **数据类型：** | `double` |

### **最小允许滑移率（绝对值），KPUMIN** — 最小允许滑移率 `-0.999`（默认） | 标量

最小允许滑移率（绝对值），*KPUMIN*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMIN` |
| **值：** | `-0.999`（默认） | 标量 |
| **数据类型：** | `double` |

### **最大允许侧偏角（绝对值），ALPMAX** — 最大允许侧偏角 `1.5708`（默认） | 标量

最大允许侧偏角（绝对值），*ALPMAX*，单位为 rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMAX` |
| **值：** | `1.5708`（默认） | 标量 |
| **数据类型：** | `double` |

### **最小允许侧偏角（绝对值），ALPMIN** — 最小允许侧偏角 `-1.5708`（默认） | 标量

最小允许侧偏角（绝对值），*ALPMIN*，单位为 rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMIN` |
| **值：** | `-1.5708`（默认） | 标量 |
| **数据类型：** | `double` |

### **最大允许外倾角，CAMMAX** — 最大允许外倾角 `0.173` | 标量

最大允许外倾角 *CAMMAX*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMAX` |
| **值：** | `0.173` | 标量 |
| **数据类型：** | `double` |

### **最小允许外倾角，CAMMIN** — 最小允许外倾角 `-0.173` | 标量

最小允许外倾角，*CAMMIN*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMIN` |
| **值：** | `-0.173` | 标量 |
| **数据类型：** | `double` |

### **最低环境温度，TMIN** — 最低环境温度 `0`（默认）| 标量

最低环境温度，*TMIN*，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TMIN` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `ISO 28580`。

### **最高环境温度，TMAX** — 最高环境温度 `400`（默认）| 标量

最高环境温度，*TMAX*，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TMAX` |
| **值：** | `400`（默认）| 标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **滚动阻力** 设置为 `ISO 28580`。

### 绘图

### **安装扩展轮胎功能** — 用于安装 Vehicle Dynamics Blockset 支持包的扩展轮胎功能的选项 按钮

点击 **安装扩展轮胎功能** 以安装 Vehicle Dynamics Blockset 支持包的扩展轮胎功能。借助该支持包，您可以从 Fiala Wheel 2DOF 模块参数对话框中绘制稳态力和力矩轮胎响应。

### **绘制稳态力、力矩响应** — 用于绘制稳态力和力矩轮胎响应的选项 按钮

点击 **绘制稳态力、力矩响应** 以生成以下绘图：

- **侧向力 [N] vs 侧偏角 [rad]**
- **回正力矩 [Nm] vs 侧偏角 [rad]**
- **纵向力 [N] vs 纵向滑移 []**
- **纵向力 [N] vs 侧向力 [N]**

#### 依赖关系

要启用此参数，请点击 **安装扩展轮胎功能**。

## 所属库

Vehicle Dynamics Blockset / Wheels and Tires

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2024b：新增 **轮胎类型** 选项

从 R2024b 开始，您可以指定 **轮胎类型** 以使用新的内置轮胎模型 `Light passenger car 245/60R16`。

### R2024b：新增 **垂直运动** 选项

从 R2024b 开始，将 **垂直运动** 指定为 `External Deflection` 会启用 **RadialDeflct** 端口。在与轮胎交互且未提供力的情况下，使用此端口定义胎侧变形。

### R2024b：新增信号添加到 **Info** 端口总线

从 R2024b 开始，**Info** 端口总线包含以下新信号。

| 信号 | 描述 |
| --- | --- |
| `RadialDeflct` | 轮胎径向变形 |
| `RL` | 负载半径 |
| `WhlTrq` | 车轮扭矩 |

### R2024b：重命名模块参数

从 R2024b 开始，以下参数已被重命名。

| 旧名称 | 新名称 |
| --- | --- |
| **Wheel width** | **Tire nominal section width** |
| **Unloaded radius** | **Tire unloaded radius** |
| **Initial rotational velocity** | **Initial wheel rotational velocity** |
| **Wheel mass** | **Tire mass** |
| **Rotational inertia** | **Tire rotational inertia** |

### R2024a：新增 **Tire type** 参数

从 R2024a 开始，Fiala Wheel 2DOF 模块包含 **Tire type** 参数，用于从六种不同的轮胎尺寸中选择拟合参数集。

### R2024a：绘制稳态力和力矩响应

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用新的 **Plot steady state force, moment response** 按钮生成绘图。

### R2022b：为每个车轮指定制动和轮胎参数

从 R2022b 开始，您可以使用 Fiala Wheel 2DOF 模块为车辆上的每个车轮指定制动和轮胎特性。具体而言，该模块允许以下参数使用 *N*×`1` 向量：

- **Static friction coefficient, mu\_static**
- **Kinetic friction coefficient, mu\_kinetic**
- **Disc brake actuator bore, disc\_abore**
- **Brake pad mean radius, Rm**
- **Number of brake pads, num\_pads**
- **Drum brake actuator bore, disc\_abore**
- **Initial rotational velocity, omegao**
- **Rotational damping, br**
- **Wheel mass, m**
- **Rotational inertia (rolling axis), IYY**
- **Initial tire displacement, zo**
- **Initial wheel vertical velocity (wheel fixed frame), zdoto**
- **Longitudinal stiffness, Ckappa**
- **Lateral stiffness per slip angle, Calpha**
- **Camber stiffness, Cgamma**
- **Kinematic friction, muMin**
- **Static friction, muMax**
- **Longitudinal relaxation length, Lrelx**
- **Lateral relaxation length, Lrely**

*N* 是车轮数量，并且必须与输入信号维度匹配。

## 描述

Fiala wheel 2DOF 带盘式、鼓式或映射制动的车轮

Fiala Wheel 2DOF 模块基于 E. Fiala 模型[1]实现了一个具有侧向和纵向滑移能力的简化轮胎。该模块使用平移摩擦模型来计算纵向和侧向联合滑移期间的力和力矩，所需参数比 Combined Slip Wheel 2DOF 模块更少。如果您没有 Magic Formula 所需的轮胎系数，可以考虑将此模块用于不涉及大量非线性联合侧向滑移或侧向动力学的分析。如果您的分析确实需要非线性联合滑移或侧向动力学，请考虑使用 Combined Slip Wheel 2DOF 模块。

该模块根据传动系统扭矩、制动压力、路面高度、车轮外倾角和充气压力，确定车轮转速、垂向运动以及全部六个自由度（DOF）的力和力矩。您可以将此模块用于以下类型的分析：

- 传动系统和车辆仿真，需要低频轮胎-路面力和制动力，以最少的轮胎参数进行车辆加速、制动和车轮滚动阻力计算。
- 车轮与理想化路面的相互作用。
- 经历轻微联合滑移的车辆的平顺性和操纵性试验。对于此分析，您可以将该模块连接到传动系统和底盘组件，如差速器、悬架和车身系统。
- 横摆稳定性。对于此分析，您可以将该模块连接到更详细的制动系统模型。
- 使用模块垂向自由度的轮胎刚度与簧下质量相互作用，涉及地面变化、载荷转移或底盘运动。

该模块集成了车轮旋转、垂向质量和制动动力学模型。对于滑移相关的轮胎力和力矩，该模块实现了 Fiala 轮胎模型。

您可以设置自己的用户定义模型参数值，或使用内置轮胎模型。

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用以下附加功能：

- 绘图生成 — 点击 **Plot steady state force, moment response** 按钮生成以下绘图：

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle [rad]**
  - **Longitudinal force [N] vs Longitudinal slip []**
  - **Longitudinal force [N] vs Lateral force [N]**
- 导入轮胎参数 — 使用 `tireModel.get` 方法将 Fiala Wheel 2DOF 模块中定义的轮胎参数值导入到 `tireModel` 对象。
- 导出轮胎参数 — 使用 `set` 方法将 `tireModel` 对象中的轮胎参数值导出到 Fiala Wheel 2DOF 模块。
- 轮胎模型转换 — 使用 `convert` 方法将以下类型之一的轮胎模型转换为可导入 Fiala Wheel 2DOF 模块的 Fiala 轮胎模型：

  - Magic Formula 5.2
  - Magic Formula 6.2
  - Dugoff

使用 **Tire type** 参数来输入轮胎参数值或选择拟合的轮胎参数集。

| 目标 | 操作 |
| --- | --- |
| 输入用户定义的轮胎参数值。 | 使用用户定义的参数值更新模块参数：1. 将 **Tire type** 设置为 `User    defined`。2. 在 **Wheel and Tire Parameters** 部分中，输入用户定义的值。3. 点击 **Apply**。 |
| 选择一个内置 Fiala 轮胎模型来驱动纵向和侧向计算。[link]。 | 使用内置轮胎模型中的值更新适用的模块参数：1. 将 **Tire type** 设置为您要实现的轮胎。选项包括：- `Light passenger car      205/60R15` - `Light passenger car      245/60R16` - `Mid-size passenger car      235/45R18` - `Performance car      225/40R19` - `SUV      265/50R20` - `Light truck      275/65R18` - `Commercial truck      295/75R22.5` 2. 点击 **Update block with applicable tire    values**。在 **Wheel and Tire    Parameters** 部分中，模块会更新适用的 **Longitudinal and Lateral** 参数。3. 点击 **Apply**。 |

使用 **Brake Type** 参数选择制动器。

| 操作 | Brake Type 设置 |
| --- | --- |
| 无制动 | `None` |
| 实现将制动缸压力转换为制动力的制动器 | `Disc` |
| 实现将施加力和制动器几何结构转换为净制动扭矩的单工鼓式制动器 | `Drum` |
| 实现作为车轮转速和施加制动压力函数的查找表 | `Mapped` |

要计算滚动阻力扭矩，请指定以下 **Rolling Resistance** 参数之一。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 无 |
| `Pressure and velocity` | *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance* 中的方法。滚动阻力是轮胎压力、法向力和速度的函数。 |
| `ISO 28580` | ISO 28580:2018，*Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results* 中规定的方法。 |
| `Magic Formula` | *Tire and Vehicle Dynamics* 中 4.E70 的魔术公式方程。魔术公式是基于拟合系数的经验方程。 |
| `Mapped torque` | 作为法向力和自旋轴纵向速度函数的查找表。 |

要计算垂向运动，请指定以下 **Vertical Motion** 参数之一。

| 设置 | 模块实现 |
| --- | --- |
| `None` | 模块将施加的底盘力直接传递到滚动阻力和纵向力计算。 |
| `Mapped stiffness and damping` | 垂向运动取决于车轮刚度和阻尼。刚度是轮胎侧壁位移和压力的函数。阻尼是轮胎侧壁速度和压力的函数。 |
| `External deflection` | 模块在有效半径计算中直接使用定义的侧壁变形。 |

### Rotational Wheel Dynamics

该模块计算车轮在以下因素作用下的惯性响应：

- 车轴损耗
- 制动和驱动力矩
- 轮胎滚动阻力
- 通过轮胎-道路界面的地面接触

输入力矩是施加的车轴力矩、制动力矩以及由组合轮胎力矩产生的力矩之和。

Ti=Ta−Tb+Td

对于由组合轮胎力矩产生的力矩，该模块使用一阶动力学实现牵引车轮力和滚动阻力。滚动阻力具有以松弛长度参数化的时间常数。

Td(s)=1Le|ω|Res+1(FxRe+My)

要计算滚动阻力矩，您可以指定以下 **Rolling Resistance** 参数之一。

| Setting | Block Implementation |
| --- | --- |
| `None` | 模块将滚动阻力 `My` 设置为零。 |
| `Pressure and velocity` | 模块使用 SAE *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance* 中的方法。滚动阻力是轮胎压力、法向力和速度的函数，具体为： My=Re{a+b|Vx|+cVx2}{Fzβpiα}tanh(4Vx) |
| `ISO 28580` | 模块使用 ISO 28580:2018 *Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results* 中指定的方法。该方法考虑了法向载荷、寄生损耗以及测试条件下的热修正，具体为： My=Re(FzCr1+Kt(Tamb−Tmeas)−Fpl)tanh(ω) |
| `Magic Formula` | 模块使用 *Tire and Vehicle Dynamics* 中 4.E70 的 Magic Formula 方程计算滚动阻力 `My`。Magic Formula 是基于拟合系数的经验方程。 |
| `Mapped torque` | 对于滚动阻力 `My`，模块使用以法向力和自旋轴纵向速度为函数的查找表。 |

如果启用了制动器，模块基于理想干式离合器摩擦模型确定制动锁定或未锁定状态。基于锁止状态，模块实现以下摩擦和动力学模型。

| If | Lock-Up Condition | Friction Model | Dynamic Model |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | Unlocked | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | Locked | Tf=Ts | ω=0 |

这些方程使用以下变量。

| Variable | Value |
| --- | --- |
| *ω* | 车轮角速度 |
| *a* | 与速度无关的力分量 |
| *b* | 线性速度力分量 |
| *c* | 二次速度力分量 |
| *Le* | 轮胎松弛长度 |
| *J* | 转动惯量 |
| *My* | 滚动阻力矩 |
| *Ta* | 施加的车轴力矩 |
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
| *Vx* | 车轴纵向速度 |
| *Fz* | 车辆法向力 |
| *Cr* | 滚动阻力常数 |
| *Tamb* | 环境温度 |
| *Tmeas* | 滚动阻力常数的测量温度 |
| *Fpl* | 寄生力损耗 |
| *Kt* | 热修正因子 |
| *ɑ* | 轮胎压力指数 |
| *β* | 法向力指数 |
| *pi* | 轮胎压力 |
| *μs* | 静摩擦系数 |
| *μk* | 动摩擦系数 |

### Longitudinal Force

该模块使用以下方程，将纵向力实现为车轮相对路面的滑移的函数。

| 计算 | 方程 |
| --- | --- |
| 临界滑移 | κ'Critical=|μFz2Cκ| |
| 纵向力 | Fx={Ck κ'                                          when |κ'|≤κ'Criticaltanh(4κ')(μ|Fz|−|(μFz)24κ'Cκ|)         when |κ'|>κ'Critical |
| 摩擦系数 | μ=(μs−(μs−μk) κkα)λμ |
| 滑移系数 | κkα=κ'2+tan2(α') |

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *κ'* | 滑移状态 |
| *Fx* | 沿轮胎固定 *x* 轴作用在车轴上的纵向力 |
| *Cκ* | 纵向刚度 |
| *Fz* | 沿轮胎固定 *z* 轴作用在接地点上的垂直法向力 |
| *μ* | 摩擦系数 |
| *μs* | 静摩擦系数 |
| *μk* | 动摩擦系数 |
| *κka* | 综合滑移系数 |
| *α'* | 侧偏角状态 |
| *λμ* | 摩擦缩放 |

### Lateral Force

该模块使用以下方程，将侧向力实现为车轮侧偏角状态的函数。

| 计算 | 方程 |
| --- | --- |
| 临界侧偏角 | α'Critical=atan(3μ|Fz|Ca) |
| 侧向力 | Fy={−tanh(4α')μ|Fz|                           when |α'|>α'Critical−tanh(4α')μ|Fz|(1−ξ3)+γCγ    when |α'|≤α'Criticalξ=1−Ca|tan(α')|3μ|Fz| |

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *α'* | 侧偏角状态 |
| *Fy* | 沿轮胎固定 *y* 轴作用在车轴上的侧向力 |
| *Fz* | 沿轮胎固定 *z* 轴作用在接地点上的垂直法向力 |
| *Cɣ* | 外倾刚度 |
| *Cα* | 每侧偏角的侧向刚度 |
| *μ* | 摩擦系数 |

### Vertical Dynamics

该模块使用以下方程实现垂直动力学。

| 计算 | 方程 |
| --- | --- |
| 垂直响应 | z¨m=Fztire+mg−Fz |
| 轮胎法向力 | Fztire=ρzk−bz˙ |
| 垂直侧壁变形 | ρz=zgnd−z,z≥0 |

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *z* | 沿轮胎固定 *z* 轴的轮胎变形 |
| *zgnd* | 沿轮胎固定 *z* 轴的地面位移 |
| *Fztire* | 沿轮胎固定 *z* 轴的轮胎法向力 |
| *Fz* | 沿轮胎固定 *z* 轴作用在车轴上的垂直力 |
| *ρz* | 沿轮胎固定 *z* 轴的垂直侧壁变形 |
| *k* | 垂直侧壁刚度 |
| *b* | 垂直侧壁阻尼 |

### Overturning, Aligning, and Scaling

此表总结了侧翻、回正和缩放实现。

| 计算 | 实现 |
| --- | --- |
| 侧翻力矩 | Fiala 模型未定义侧翻力矩。该模块实现此方程，所需参数最少。  Mx=FyRecos(γ) |
| 回正力矩 | 该模块将回正力矩实现为横摆率阻尼和侧偏角状态的组合。  Mz={ψ˙bMz                                               when |α'|>α'Criticaltanh(4α')wμ|Fz|(1−ξ)ξ3+ψ˙bMz    when |α'|≤α'Criticalξ=1−Ca|tan(α')|3μ|Fz| |
| 摩擦缩放 | 要改变摩擦系数，请使用 **ScaleFctr** 输入端口。 |

这些方程使用以下变量。

| 变量 | 值 |
| --- | --- |
| *Mx* | 绕轮胎固定 *x* 轴作用在车轴上的侧翻力矩 |
| *Mz* | 绕轮胎固定 *z* 轴作用在车轴上的回正力矩 |
| *Re* | 接地点到轮毂的径向有效距离 |
| *ɣ* | 外倾角 |
| *k* | 垂直侧壁刚度 |
| *b* | 垂直侧壁阻尼 |
| ψ˙ | 绕轮胎固定 *z* 轴的轮胎角速度（横摆率） |
| *w* | 轮胎宽度 |
| *α'* | 侧偏角状态 |
| *bMz* | 线性横摆率阻力 |
| *Fy* | 沿轮胎固定 *y* 轴作用在车轴上的侧向力 |
| *Cɣ* | 外倾刚度 |
| *Cα* | 每侧偏角的侧向刚度 |
| *μ* | 摩擦系数 |
| *Fz* | 沿轮胎固定 *z* 轴作用在接地点上的垂直法向力 |

### 轮胎与车轮坐标系

为求解力和力矩，该模块使用轮胎与车轮坐标系的 Z-Up 方向。

- 轮胎坐标系轴（*XT*、*YT*、*ZT*）固定在附着于轮胎的参考系中。原点位于轮胎与地面的接触点。
- 车轮坐标系轴（*XW*、*YW*、*ZW*）固定在附着于车轮的参考系中。原点位于车轮中心。

**Z-Up 方向**1

显示车轮平面和道路平面的 Z-Up 轮胎与车轮坐标系

### Brakes

**Disc**

如果将 **Brake Type** 参数指定为
`Disc`，则该模块实现盘式制动器。下图
展示了盘式制动器的侧视图和前视图。

盘式制动器的前视图和侧视图，显示制动片、制动盘和制动钳

盘式制动器将制动缸压力从制动缸转换为力。盘式制动器在制动片平均半径处施加力。

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
| *Rm* | 制动片在制动盘上施加力的平均半径 |
| *Ro* | 制动片外半径 |
| *Ri* | 制动片内半径 |

**Drum**

如果将 **Brake Type** 参数指定为
`Drum`，则该模块实现静态（稳态）
简单鼓式制动器。简单鼓式制动器由单个双面液压
执行器和两个制动蹄组成。制动蹄不共享
公共铰链销。

简单鼓式制动器模型使用施加的力和制动器几何结构，为每个制动蹄计算净力矩。鼓式模型假设执行器和制动蹄几何结构在两侧对称，从而允许两个制动蹄使用同一组几何结构和摩擦参数。

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
