---
type: simulink-block
title: 'Combined Slip Wheel CPI'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'combinedslipwheelcpi'
documentation_source_path: 'ref/combinedslipwheelcpi.html'
language: zh-CN
chinese_source: worker-translation
---

# Combined Slip Wheel CPI

## 端口
```yaml
ports:
- name: Omega
  summary: 旋转速度 标量 | N×1 向量
  direction: input
- name: Vx
  summary: 纵向速度 标量 | *N*×1 向量
  direction: input
- name: Vy
  summary: 侧向速度 标量 | *N*×1 向量
  direction: input
- name: Camber
  summary: 倾角 标量 | *N*×1 向量
  direction: input
- name: YawRate
  summary: 轮胎角速度 标量 | *N*×1 向量
  direction: input
- name: Fext
  summary: 施加到轮胎上的车轴力 标量 | *N*×1 向量
  direction: input
- name: RadialDeflct
  summary: 轮胎径向变形 标量 | *N*×1 向量
  direction: input
- name: ScaleFctrs
  summary: 比例因子 27×N 数组
  direction: input
- name: Prs
  summary: 轮胎充气压力 标量 | N×1 向量
  direction: input
- name: Info
  summary: 模块数据总线
  direction: output
- name: Fx
  summary: 纵向轴力 标量 | *N*×1 向量
  direction: output
- name: Fy
  summary: 横向轴力 标量 | *N*×1 向量
  direction: output
- name: Fz
  summary: 垂向轴力 标量 | *N*×1 向量
  direction: output
- name: Mx
  summary: 侧倾力矩 标量 | *N*×1 向量
  direction: output
- name: My
  summary: 滚动阻力矩 标量 | *N*×1 向量
  direction: output
- name: Mz
  summary: 回正力矩 标量 | *N*×1 向量
  direction: output
```

### 输入

### **Omega** — 旋转速度 标量 | `N`×`1` 向量

轮胎绕车轮旋转轴的旋转速度，*ω*，单位为 rad/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Vx** — 纵向速度 标量 | *N*×`1` 向量

车轴纵向速度，*Vx*，沿轮胎固定 *x* 轴方向，单位为 m/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Vy** — 侧向速度 标量 | *N*×`1` 向量

车轴侧向速度，*Vy*，沿轮胎固定 *y* 轴方向，单位为 m/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Camber** — 倾角 标量 | *N*×`1` 向量

外倾角，*ɣ*，或倾角，*ε*，单位为 rad。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **YawRate** — 轮胎角速度 标量 | *N*×`1` 向量

轮胎绕轮胎固定 *z* 轴的角速度，*r*（横摆角速度），单位为 rad/s。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fext** — 施加到轮胎上的车轴力 标量 | *N*×`1` 向量

施加到轮胎上的车轴力，*Fext*，沿车辆固定 *z* 轴方向（正输入压缩轮胎），单位为 N。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要启用此参数，请将 **Vertical Motion** 设置为 `None`。

### **RadialDeflct** — 轮胎径向变形 标量 | *N*×`1` 向量

轮胎径向变形，*RadialDeflct*，单位为 m。此值将用于所有依赖变形的内部 Magic Formula 6.2 方程中。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要启用此端口，请将 **Vertical Motion** 设置为 `External Deflection`。

### **ScaleFctrs** — 比例因子 `27`×`N` 数组

Magic Formula 6.2 比例因子数组。数组维度为 `27` 乘以车轮数量 *N*。

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
| `ScaleFctrs(23,1)` | `lam_Cz` | 轮胎径向刚度 |
| `ScaleFctrs(24,1)` | `lam_Mx` | 侧翻力矩刚度 |
| `ScaleFctrs(25,1)` | `lam_VMx` | 侧翻力矩垂直偏移 |
| `ScaleFctrs(26,1)` | `lam_My` | 滚动阻力矩 |
| `ScaleFctrs(27,1)` | `lam_Mphi` | 驻车力矩 *Mz* |

### **Prs** — 轮胎充气压力 标量 | `N`×`1` 向量

轮胎充气压力 *pi*，单位为 Pa。

向量为车轮数量 *N* 乘以 `1`。如果提供标量值，模块假定车轮数量为一。

#### 依赖关系

要创建此端口，请选择 **Input tire pressure**。
### 输出

### **Info** — 模块数据总线

模块数据，以总线信号形式返回，包含以下模块值。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `Omega` | 车轮绕车轮固定 *y* 轴的角速度 | rad/s |
| `Fx` | 沿轮胎固定 *x* 轴的纵向车辆力 | N |
| `Fy` | 沿轮胎固定 *y* 轴的侧向车辆力 | N |
| `Fz` | 沿轮胎固定 *z* 轴的垂直车辆力 | N |
| `Mx` | 绕轮胎固定 *x* 轴的侧翻力矩 | N·m |
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
| `FNormal` | 沿轮胎固定 *z* 轴作用在地面上的垂直胎侧力 | N |
| `Prs` | 轮胎充气压力 | Pa |
| `RL` | 加载半径 | m |
| `WhlTrq` | 车轮扭矩 | N·m |

### **Fx** — 纵向轴力 标量 | *N*×`1` 向量

沿轮胎固定 *x* 轴作用于车轴的纵向力 *Fx*，单位为 N。正力使车辆向前运动。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fy** — 横向轴力 标量 | *N*×`1` 向量

沿轮胎固定 *y* 轴作用于车轴的横向力 *Fy*，单位为 N。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Fz** — 垂向轴力 标量 | *N*×`1` 向量

沿轮胎固定 *z* 轴作用于车轴的垂向力 *Fz*，单位为 N。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Mx** — 侧倾力矩 标量 | *N*×`1` 向量

绕轮胎固定 *x* 轴作用于车轴的纵向力矩 *Mx*，单位为 N·m。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **My** — 滚动阻力矩 标量 | *N*×`1` 向量

绕轮胎固定 *y* 轴作用于车轴的横向力矩 *My*，单位为 N·m。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。

### **Mz** — 回正力矩 标量 | *N*×`1` 向量

绕轮胎固定 *z* 轴作用于车轴的垂向力矩 *Mz*，单位为 N·m。

向量为车轮数量 *N*×`1`。如果提供标量值，模块假定车轮数量为一。
## 参数
```yaml
parameters:
- name: Tire type
  summary: 类型 External file | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger car 235/45R18
    | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
  group: 轮胎选项
  block_parameter: tireType
  values: External file（默认） | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger car 235/45R18
    | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
- name: 轮胎文件或对象，tireParamSet
  summary: 轮胎文件 .mat | .tir | .txt
  group: 轮胎选项
  block_parameter: tireParamSet
  values: vdynPassCar.mat（默认） | .tir | .txt
- name: 垂直运动
  summary: 垂直运动模型 None（默认） | External deflection
  group: 轮胎选项
  block_parameter: vertType
  values: None（默认） | External deflection
- name: 轮胎侧
  summary: 选择轮胎侧 Right（默认） | Left | Symmetric
  group: 轮胎选项
  block_parameter: TireSide
  values: Right（默认） | Left | Symmetric
- name: 轮胎压力
  summary: 压力标量
  group: 轮胎选项
  block_parameter: TirePrs
  values: scalar
- name: 帘布层转向
  summary: 包含帘布层转向 on（默认） | off
  group: 轮胎选项
  block_parameter: plySteer
  values: on（默认） | off
- name: Turn slip
  summary: 包含 turn slip on（默认） | off
  group: 轮胎选项
  block_parameter: turnslip
  values: on（默认） | off
- name: Install Extended Tire Features
  summary: 用于安装 Extended Tire Features for Vehicle Dynamics Blockset™ 支持包的选项 按钮
  group: 绘图
- name: Plot steady state force, moment response
  summary: 用于绘制稳态力和力矩轮胎响应的选项 按钮
  group: 绘图
- name: Nominal pressure, NOMPRES
  summary: 压力标量
  group: 仿真
  block_parameter: NOMPRES
  values: 标量
- name: Maximum pressure, PRESMAX
  summary: 最大压力标量
  group: 仿真
  block_parameter: PRESMAX
  values: 标量
- name: Minimum pressure, PRESMIN
  summary: 最小压力标量
  group: 仿真
  block_parameter: PRESMIN
  values: 标量
- name: Nominal normal force, FNOMIN
  summary: 力标量
  group: 仿真
  block_parameter: FNOMIN
  values: 标量
- name: Maximum normal force, FZMAX
  summary: 力标量
  group: 仿真
  block_parameter: FZMAX
  values: 标量
- name: Minimum normal force, FZMIN
  summary: 力标量
  group: 仿真
  block_parameter: FZMIN
  values: 标量
- name: Velocity tolerance used to handle low velocity situations, VXLOW
  summary: 容差标量
  group: 仿真
  block_parameter: VXLOW
  values: 标量
- name: Max allowable slip ratio (absolute), KPUMAX
  summary: 最大允许滑移率标量
  group: 仿真
  block_parameter: KPUMAX
  values: 标量
- name: Minimum allowable slip ratio (absolute), KPUMIN
  summary: 最小允许滑移率标量
  group: 仿真
  block_parameter: KPUMIN
  values: 标量
- name: Max allowable slip angle (absolute), ALPMAX
  summary: 最大允许侧偏角标量
  group: 仿真
  block_parameter: ALPMAX
  values: 标量
- name: Minimum allowable slip angle (absolute), ALPMIN
  summary: 最小允许侧偏角标量
  group: 仿真
  block_parameter: ALPMIN
  values: 标量
- name: Maximum allowable camber angle, CAMMAX
  summary: 最大允许外倾角标量
  group: 仿真
  block_parameter: CAMMAX
  values: 标量
- name: Minimum allowable camber angle, CAMMIN
  summary: 最小允许外倾角标量
  group: 仿真
  block_parameter: CAMMIN
  values: 标量
- name: Nominal longitudinal speed, LONGVL
  summary: 速度标量
  group: 仿真
  block_parameter: LONGVL
  values: 标量
- name: Default tyre side, tyreside
  summary: 侧边 'Right'（默认）| 字符
  group: 仿真
  block_parameter: tyreside
  values: '''Right''（默认）| 字符'
- name: Initial wheel rotational velocity, omegao
  summary: 速度标量
  group: 仿真
  block_parameter: omegao
  values: 标量
- name: Tire unloaded radius, UNLOADED_RADIUS
  summary: 半径标量
  group: 尺寸
  block_parameter: UNLOADED_RADIUS
  values: 标量
- name: Tire nominal section width, WIDTH
  summary: 宽度标量
  group: 尺寸
  block_parameter: WIDTH
  values: 标量
- name: Rim radius, RIM_RADIUS
  summary: 半径标量
  group: 尺寸
  block_parameter: RIM_RADIUS
  values: 标量
- name: Nominal aspect ratio, ASPECT_RATIO
  summary: 比率标量
  group: 尺寸
  block_parameter: ASPECT_RATIO
  values: 标量
- name: Initial tire displacement, zo
  summary: 位移标量
  group: 垂直
  block_parameter: zo
  values: 标量
- name: Initial wheel vertical velocity (wheel fixed frame), zdoto
  summary: 速度标量
  group: 垂直
  block_parameter: zdoto
  values: 标量
- name: Effective rolling radius at low load stiffness, BREFF
  summary: 刚度标量
  group: 垂直
  block_parameter: BREFF
  values: 标量
- name: 有效滚动半径峰值，DREFF
  summary: 半径标量
  group: 垂直
  block_parameter: DREFF
  values: 标量
- name: 高载荷刚度下的有效滚动半径，FREFF
  summary: 半径标量
  group: 垂直
  block_parameter: FREFF
  values: 标量
- name: 空载与额定滚动半径比，Q_RE0
  summary: 比值标量
  group: 垂直
  block_parameter: Q_RE0
  values: 标量
- name: 半径转速依赖性，Q_V1
  summary: 速度标量
  group: 垂直
  block_parameter: Q_V1
  values: 标量
- name: 刚度转速依赖性，Q_V2
  summary: 速度标量
  group: 垂直
  block_parameter: Q_V2
  values: 标量
- name: 随变形的线性载荷变化，Q_FZ1
  summary: 载荷变化标量
  group: 垂直
  block_parameter: Q_FZ1
  values: 标量
- name: 随变形的二次载荷变化，Q_FZ2
  summary: 载荷变化标量
  group: 垂直
  block_parameter: Q_FZ2
  values: 标量
- name: 随变形和二次外倾的线性载荷变化，Q_FZ3
  summary: 载荷变化标量
  group: 垂直
  block_parameter: Q_FZ3
  values: 标量
- name: 载荷对纵向力的响应，Q_FCX
  summary: 力标量
  group: 垂直
  block_parameter: Q_FCX
  values: 标量
- name: 侧向力载荷响应，Q_FCY
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_FCY
  values: 标量
- name: 侧向载荷对侧向刚度依赖引起的垂直刚度变化，Q_FCY2
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_FCY2
  values: 标量
- name: 刚度对压力的响应，PFZ1
  summary: 刚度标量
  group: 垂直
  block_parameter: PFZ1
  values: 标量
- name: 垂直轮胎刚度，VERTICAL_STIFFNESS
  summary: 刚度标量
  group: 垂直
  block_parameter: VERTICAL_STIFFNESS
  values: 标量
- name: 垂直轮胎阻尼，VERTICAL_DAMPING
  summary: 阻尼标量
  group: 垂直
  block_parameter: VERTICAL_DAMPING
  values: 标量
- name: 轮辋触底偏移量，BOTTOM_OFFST
  summary: 偏移量标量
  group: 垂直
  block_parameter: BOTTOM_OFFST
  values: 标量
- name: 触底刚度，BOTTOM_STIFF
  summary: 刚度标量
  group: 垂直
  block_parameter: BOTTOM_STIFF
  values: 标量
- name: 线性载荷相关外倾角对垂直刚度的影响，Q_CAM1
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_CAM1
  values: 标量
- name: Quadratic load dependent camber angle effect on vertical stiffness, Q_CAM2
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_CAM2
  values: 标量
- name: Linear reduction of stiffness with load and camber angle, Q_CAM3
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_CAM3
  values: 标量
- name: Constant camber and slip angle effect on vertical stiffness, Q_FYS1
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_FYS1
  values: 标量
- name: Linear camber and slip angle effect on vertical stiffness, Q_FYS2
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_FYS2
  values: 标量
- name: Quadratic camber and slip angle effect on vertical stiffness, Q_FYS3
  summary: 刚度标量
  group: 垂直
  block_parameter: Q_FYS3
  values: 标量
- name: Longitudinal stiffness, LONGITUDINAL_STIFFNESS
  summary: 刚度标量
  group: 结构
  block_parameter: LONGITUDINAL_STIFFNESS
  values: 标量
- name: Lateral stiffness, LATERAL_STIFFNESS
  summary: 刚度标量
  group: 结构
  block_parameter: LATERAL_STIFFNESS
  values: 标量
- name: Linear vertical deflection influence on longitudinal stiffness, PCFX1
  summary: 变形影响标量
  group: 结构
  block_parameter: PCFX1
  values: 标量
- name: Quadratic vertical deflection influence on longitudinal stiffness, PCFX2
  summary: 变形影响标量
  group: 结构
  block_parameter: PCFX2
  values: 标量
- name: 纵向刚度对压力的依赖性，PCFX3
  summary: 压力依赖性标量
  group: 结构
  block_parameter: PCFX3
  values: 标量
- name: 垂向挠度对侧向刚度的线性影响，PCFY1
  summary: 挠度影响标量
  group: 结构
  block_parameter: PCFY1
  values: 标量
- name: 垂向挠度对侧向刚度的二次影响，PCFY2
  summary: 挠度影响标量
  group: 结构
  block_parameter: PCFY2
  values: 标量
- name: 纵向刚度对压力的依赖性，PCFY3
  summary: 压力依赖性标量
  group: 结构
  block_parameter: PCFY3
  values: 标量
- name: 接触长度平方根项，Q_RA1
  summary: 长度项标量
  group: 接触印迹
  block_parameter: Q_RA1
  values: 标量
- name: 接触长度线性项，Q_RA2
  summary: 长度项标量
  group: 接触印迹
  block_parameter: Q_RA2
  values: 标量
- name: 接触宽度根项，Q_RB1
  summary: 宽度项标量
  group: 接触印迹
  block_parameter: Q_RB1
  values: 标量
- name: 接触宽度线性项，Q_RB2
  summary: 宽度项标量
  group: 接触印迹
  block_parameter: Q_RB2
  values: 标量
- name: Cfx 形状因子，PCX1
  summary: 形状因子标量
  group: 纵向
  block_parameter: PCX1
  values: 标量
- name: 名义法向载荷下的纵向摩擦，PDX1
  summary: 摩擦标量
  group: 纵向
  block_parameter: PDX1
  values: 标量
- name: 摩擦随载荷的变化，PDX2
  summary: 摩擦变化标量
  group: 纵向
  block_parameter: PDX2
  values: 标量
- name: 摩擦随外倾角的变化，PDX3
  summary: 摩擦变化标量
  group: 纵向
  block_parameter: PDX3
  values: 标量
- name: 名义法向载荷下的纵向曲率，PEX1
  summary: 曲率标量
  group: 纵向
  block_parameter: PEX1
  values: 标量
- name: 曲率因子随载荷的变化，PEX2
  summary: 曲率变化标量
  group: 纵向
  block_parameter: PEX2
  values: 标量
- name: 曲率因子随载荷平方的变化，PEX3
  summary: 曲率变化标量
  group: 纵向
  block_parameter: PEX3
  values: 标量
- name: 带滑移的纵向曲率因子，PEX4
  summary: 曲率标量
  group: 纵向
  block_parameter: PEX4
  values: 标量
- name: 名义法向载荷下的纵向滑移刚度，PKX1
  summary: 刚度标量
  group: 纵向
  block_parameter: PKX1
  values: 标量
- name: 滑移刚度随载荷的变化，PKX2
  summary: 刚度变化标量
  group: 纵向
  block_parameter: PKX2
  values: 标量
- name: Slip stiffness exponent factor, PKX3
  summary: 滑移刚度标量
  group: 纵向
  block_parameter: PKX3
  values: 标量
- name: Horizontal shift in slip ratio at nominal normal load, PHX1
  summary: 滑移率偏移标量
  group: 纵向
  block_parameter: PHX1
  values: 标量
- name: Variation of horizontal slip ratio with load, PHX2
  summary: 滑移变化标量
  group: 纵向
  block_parameter: PHX2
  values: 标量
- name: Vertical shift in load at nominal normal load, PVX1
  summary: 载荷偏移标量
  group: 纵向
  block_parameter: PVX1
  values: 标量
- name: Variation of vertical shift with load, PVX2
  summary: 载荷变化标量
  group: 纵向
  block_parameter: PVX2
  values: 标量
- name: Linear variation of longitudinal slip stiffness with tire pressure, PPX1
  summary: 刚度变化标量
  group: 纵向
  block_parameter: PPX1
  values: 标量
- name: Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2
  summary: 刚度变化标量
  group: 纵向
  block_parameter: PPX2
  values: 标量
- name: Linear variation of peak longitudinal friction with tire pressure, PPX3
  summary: 摩擦变化标量
  group: 纵向
  block_parameter: PPX3
  values: 标量
- name: Quadratic variation of peak longitudinal friction with tire pressure, PPX4
  summary: 摩擦变化标量
  group: 纵向
  block_parameter: PPX4
  values: 标量
- name: Combined slip Fx slope factor reduction, RBX1
  summary: 联合滑移纵向力斜率因子缩减标量
  group: 纵向
  block_parameter: RBX1
  values: 标量
- name: Slip ratio Fx slope reduction variation, RBX2
  summary: 滑移率纵向力斜率缩减变化标量
  group: 纵向
  block_parameter: RBX2
  values: 标量
- name: Camber influence on combined slip Fx stiffness, RBX3
  summary: 外倾角对联合滑移纵向力刚度影响的标量
  group: 纵向
  block_parameter: RBX3
  values: 标量
- name: Shape factor for combined slip Fx reduction, RCX1
  summary: 联合滑移纵向力缩减的形状因子标量
  group: 纵向
  block_parameter: RCX1
  values: 标量
- name: Combined Fx curvature factor, REX1
  summary: 联合纵向力曲率因子标量
  group: 纵向
  block_parameter: REX1
  values: 标量
- name: Combined Fx curvature factor with load, REX2
  summary: 联合纵向力曲率因子标量
  group: 纵向
  block_parameter: REX2
  values: 标量
- name: Combined slip Fx shift factor reduction, RHX1
  summary: 联合滑移纵向力滑移因子标量
  group: 纵向
  block_parameter: RHX1
  values: 标量
- name: Vertical shift of overturning moment, QSX1
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX1
  values: 标量
- name: Overturning moment due to camber, QSX2
  summary: 外倾引起的侧翻力矩标量
  group: Overturning
  block_parameter: QSX2
  values: 标量
- name: Overturning moment due to Fy, QSX3
  summary: 侧向力引起的侧翻力矩标量
  group: Overturning
  block_parameter: QSX3
  values: 标量
- name: Mx combined lateral force load and camber, QSX4
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX4
  values: 标量
- name: Mx load effect due to lateral force and camber, QSX5
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX5
  values: 标量
- name: Mx load effect due to B-factor, QSX6
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX6
  values: 标量
- name: Mx due to camber and load, QSX7
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX7
  values: 标量
- name: Mx due to lateral force and load, QSX8
  summary: 侧翻力矩标量
  group: Overturning
  block_parameter: QSX8
  values: 标量
- name: 由侧向力和载荷的 B 因子引起的 Mx，QSX9
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX9
  values: 标量
- name: 由垂直力和外倾引起的 Mx，QSX10
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX10
  values: 标量
- name: 由垂直力和外倾的 B 因子引起的 Mx，QSX11
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX11
  values: 标量
- name: 由外倾平方引起的 Mx，QSX12
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX12
  values: 标量
- name: 由侧向力引起的 Mx，QSX13
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX13
  values: 标量
- name: 由带外倾的侧向力引起的 Mx，QSX14
  summary: 倾覆力矩标量
  group: Overturning
  block_parameter: QSX14
  values: 标量
- name: 由充气压力引起的 Mx，PPMX1
  summary: 由压力引起的倾覆力矩标量
  group: Overturning
  block_parameter: PPMX1
  values: 标量
- name: 侧向力的 Cfy 形状因子，PCY1
  summary: 侧向力形状因子标量
  group: 侧向
  block_parameter: PCY1
  values: 标量
- name: Lateral friction muy, PDY1
  summary: 侧向摩擦标量
  group: 侧向
  block_parameter: PDY1
  values: 标量
- name: Lateral friction variation of muy with load, PDY2
  summary: 侧向摩擦变化标量
  group: 侧向
  block_parameter: PDY2
  values: 标量
- name: Lateral friction variation of muy with squared camber, PDY3
  summary: 侧向摩擦变化标量
  group: 侧向
  block_parameter: PDY3
  values: 标量
- name: Efy lateral curvature at nominal force FZNOM, PEY1
  summary: 额定力下侧向曲率标量
  group: 侧向
  block_parameter: PEY1
  values: 标量
- name: Efy curvature variation with load, PEY2
  summary: 侧向曲率变化标量
  group: 侧向
  block_parameter: PEY2
  values: 标量
- name: Efy curvature constant camber dependency, PEY3
  summary: 侧向曲率常数标量
  group: 侧向
  block_parameter: PEY3
  values: 标量
- name: Efy curvature variation with camber, PEY4
  summary: 侧向曲率变化标量
  group: 侧向
  block_parameter: PEY4
  values: 标量
- name: Efy curvature variation with camber squared, PEY5
  summary: 侧向曲率变化标量
  group: 侧向
  block_parameter: PEY5
  values: 标量
- name: Maximum KFy/FZNOM stiffness, PKY1
  summary: 最大刚度标量
  group: 侧向
  block_parameter: PKY1
  values: 标量
- name: 最大 KFy/FZNOM 刚度处的载荷，PKY2
  summary: 载荷标量
  group: 侧向
  block_parameter: PKY2
  values: 标量
- name: KFy/FZNOM 刚度随外倾角的变化，PKY3
  summary: 刚度变化标量
  group: 侧向
  block_parameter: PKY3
  values: 标量
- name: KFy 曲率，PKY4
  summary: 侧向力刚度曲率标量
  group: 侧向
  block_parameter: PKY4
  values: 标量
- name: 峰值刚度随外倾角平方的变化，PKY5
  summary: 刚度变化标量
  group: 侧向
  block_parameter: PKY5
  values: 标量
- name: Fy 外倾刚度因子，PKY6
  summary: 侧向力外倾刚度因子标量
  group: 侧向
  block_parameter: PKY6
  values: 标量
- name: 外倾刚度垂直载荷依赖性，PKY7
  summary: 刚度标量
  group: 侧向
  block_parameter: PKY7
  values: 标量
- name: FZNOM 处的 SHY 水平偏移，PHY1
  summary: 名义力处的水平偏移标量
  group: 侧向
  block_parameter: PHY1
  values: 标量
- name: SHY 随载荷的变化，PHY2
  summary: 水平偏移变化标量
  group: 侧向
  block_parameter: PHY2
  values: 标量
- name: Svy/Fz vertical shift at FZNOM, PVY1
  summary: 额定载荷下的垂直偏移标量
  group: 侧向
  block_parameter: PVY1
  values: 标量
- name: Svy/Fz variation with load, PVY2
  summary: 垂直偏移随载荷变化标量
  group: 侧向
  block_parameter: PVY2
  values: 标量
- name: Svy/Fz variation with camber, PVY3
  summary: 垂直偏移随外倾变化标量
  group: 侧向
  block_parameter: PVY3
  values: 标量
- name: Svy/Fz variation with load and camber, PVY4
  summary: 垂直偏移随载荷和外倾变化标量
  group: 侧向
  block_parameter: PVY4
  values: 标量
- name: Cornering stiffness variation with inflation pressure, PPY1
  summary: 刚度随压力变化标量
  group: 侧向
  block_parameter: PPY1
  values: 标量
- name: Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2
  summary: 刚度随压力变化标量
  group: 侧向
  block_parameter: PPY2
  values: 标量
- name: Linear inflation pressure on peak lateral friction, PPY3
  summary: 压力标量
  group: 侧向
  block_parameter: PPY3
  values: 标量
- name: Quadratic inflation pressure on peak lateral friction, PPY4
  summary: Pressure scalar
  group: 侧向
  block_parameter: PPY4
  values: scalar
- name: Inflation pressure effect on camber stiffness, PPY5
  summary: Pressure scalar
  group: 侧向
  block_parameter: PPY5
  values: scalar
- name: Combined Fy reduction slope factor, RBY1
  summary: Combined lateral force reduction slope factor scalar
  group: 侧向
  block_parameter: RBY1
  values: scalar
- name: Fy slope reduction with slip angle, RBY2
  summary: Lateral force slope reduction with slip angle scalar
  group: 侧向
  block_parameter: RBY2
  values: scalar
- name: Fy shift reduction with slip angle, RBY3
  summary: Lateral force shift reduction with slip angle scalar
  group: 侧向
  block_parameter: RBY3
  values: scalar
- name: Fy combined stiffness variation from camber, RBY4
  summary: Lateral force combined stiffness variation from camber scalar
  group: 侧向
  block_parameter: RBY4
  values: scalar
- name: Fy combined reduction shape factor, RCY1
  summary: Lateral force combined reduction shape factor scalar
  group: 侧向
  block_parameter: RCY1
  values: scalar
- name: Fy combined curvature factor, REY1
  summary: Lateral force combined curvature factor scalar
  group: 侧向
  block_parameter: REY1
  values: scalar
- name: Fy combined curvature factor with load, REY2
  summary: 侧向力联合曲率因子随载荷标量
  group: 侧向
  block_parameter: REY2
  values: scalar
- name: Fy combined reduction shift factor, RHY1
  summary: 侧向力联合折减偏移因子标量
  group: 侧向
  block_parameter: RHY1
  values: scalar
- name: Fy combined reduction shift factor with load, RHY2
  summary: 侧向力联合折减偏移因子随载荷标量
  group: 侧向
  block_parameter: RHY2
  values: scalar
- name: Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1
  summary: 滑移率侧向力在额定力下标量
  group: 侧向
  block_parameter: RVY1
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with load, RVY2
  summary: 侧向力随载荷变化标量
  group: 侧向
  block_parameter: RVY2
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with camber, RVY3
  summary: 侧向力随外倾变化标量
  group: 侧向
  block_parameter: RVY3
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with slip angle, RVY4
  summary: 侧向力随侧偏角变化标量
  group: 侧向
  block_parameter: RVY4
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with slip ratio, RVY5
  summary: 侧向力随滑移率变化标量
  group: 侧向
  block_parameter: RVY5
  values: 标量
- name: 侧向力 Svyk/Muy\*Fz 随滑移率反正切变化，RVY6
  summary: 侧向力随滑移率反正切变化标量
  group: 侧向
  block_parameter: RVY6
  values: 标量
- name: 阻力矩系数，QSY1
  summary: 阻力矩标量
  group: 滚动
  block_parameter: QSY1
  values: 标量
- name: 由 Fx 引起的阻力矩，QSY2
  summary: 由纵向力引起的阻力矩标量
  group: 滚动
  block_parameter: QSY2
  values: 标量
- name: 由速度引起的阻力矩，QSY3
  summary: 由速度引起的阻力矩标量
  group: 滚动
  block_parameter: QSY3
  values: 标量
- name: 由速度^4 引起的阻力矩，QSY4
  summary: 由速度引起的阻力矩标量
  group: 滚动
  block_parameter: QSY4
  values: 标量
- name: 由外倾角平方引起的阻力矩，QSY5
  summary: 由外倾角引起的阻力矩标量
  group: 滚动
  block_parameter: QSY5
  values: 标量
- name: 由外倾角平方和载荷引起的阻力矩，QSY6
  summary: 由外倾角和载荷引起的阻力矩标量
  group: 滚动
  block_parameter: QSY6
  values: 标量
- name: 由载荷引起的阻力矩，QSY7
  summary: 由载荷引起的阻力矩标量
  group: 滚动
  block_parameter: QSY7
  values: 标量
- name: Torque resistance due to pressure, QSY8
  summary: 压力引起的阻力矩标量
  group: 滚动
  block_parameter: QSY8
  values: scalar
- name: Trail slope factor for trail Bpt at FZNOM, QBZ1
  summary: 额定力下的拖距斜率因子标量
  group: Aligning
  block_parameter: QBZ1
  values: scalar
- name: Bpt slope variation with load, QBZ2
  summary: 斜率随载荷变化标量
  group: Aligning
  block_parameter: QBZ2
  values: scalar
- name: Bpt slope variation with square of load, QBZ3
  summary: 斜率随载荷变化 0 (default) | scalar
  group: Aligning
  block_parameter: QBZ3
  values: scalar
- name: Bpt slope variation with camber, QBZ4
  summary: 斜率随外倾变化标量
  group: Aligning
  block_parameter: QBZ4
  values: scalar
- name: Bpt slope variation with absolute value of camber, QBZ5
  summary: 斜率随外倾变化标量
  group: Aligning
  block_parameter: QBZ5
  values: scalar
- name: Bpt slope variation with square of camber, QBZ6
  summary: 斜率随外倾变化标量
  group: Aligning
  block_parameter: QBZ6
  values: scalar
- name: Br of Mzr slope scaling factor, QBZ9
  summary: 斜率缩放因子标量
  group: Aligning
  block_parameter: QBZ9
  values: scalar
- name: Br of Mzr cornering stiffness factor, QBZ10
  summary: 侧偏刚度因子标量
  group: Aligning
  block_parameter: QBZ10
  values: 标量
- name: Cpt pneumatic trail shape factor, QCZ1
  summary: 气胎拖距形状因子标量
  group: Aligning
  block_parameter: QCZ1
  values: 标量
- name: Dpt peak trail, QDZ1
  summary: 峰值拖距标量
  group: Aligning
  block_parameter: QDZ1
  values: 标量
- name: Dpt peak trail variation with load, QDZ2
  summary: 峰值拖距随载荷变化标量
  group: Aligning
  block_parameter: QDZ2
  values: 标量
- name: Dpt peak trail variation with camber, QDZ3
  summary: 峰值拖距随外倾变化标量
  group: Aligning
  block_parameter: QDZ3
  values: 标量
- name: Dpt peak trail variation with square of camber, QDZ4
  summary: 峰值拖距随外倾变化标量
  group: Aligning
  block_parameter: QDZ4
  values: 标量
- name: Dmr peak residual torque, QDZ6
  summary: 峰值残余力矩标量
  group: Aligning
  block_parameter: QDZ6
  values: 标量
- name: Dmr peak residual torque variation with load, QDZ7
  summary: 峰值残余力矩随载荷变化标量
  group: Aligning
  block_parameter: QDZ7
  values: 标量
- name: Dmr peak residual torque variation with camber, QDZ8
  summary: 峰值残余力矩随外倾变化标量
  group: Aligning
  block_parameter: QDZ8
  values: 标量
- name: Dmr peak residual torque variation with camber and load, QDZ9
  summary: 峰值残余力矩随外倾角和载荷变化的标量
  group: Aligning
  block_parameter: QDZ9
  values: 标量
- name: Dmr peak residual torque variation with square of camber, QDZ10
  summary: 峰值残余力矩随外倾角变化的标量
  group: Aligning
  block_parameter: QDZ10
  values: 标量
- name: Dmr peak residual torque variation with square of load, QDZ11
  summary: 峰值残余力矩随载荷变化的标量
  group: Aligning
  block_parameter: QDZ11
  values: 标量
- name: Ept trail curvature at FZNOM, QEZ1
  summary: 额定力下的拖距曲率标量
  group: Aligning
  block_parameter: QEZ1
  values: 标量
- name: Ept variation with load, QEZ2
  summary: 拖距曲率随载荷变化的标量
  group: Aligning
  block_parameter: QEZ2
  values: 标量
- name: Ept variation with square of load, QEZ3
  summary: 拖距曲率随载荷变化的标量
  group: Aligning
  block_parameter: QEZ3
  values: 标量
- name: Ept variation with sign of alpha-t, QEZ4
  summary: 拖距曲率变化标量
  group: Aligning
  block_parameter: QEZ4
  values: 标量
- name: Ept variation with sign of alpha-t and camber, QEZ5
  summary: 变化标量
  group: Aligning
  block_parameter: QEZ5
  values: 标量
- name: Sht horizontal trail shift at FZNOM, QHZ1
  summary: 额定载荷下的水平拖距偏移标量
  group: Aligning
  block_parameter: QHZ1
  values: 标量
- name: Sht variation with load, QHZ2
  summary: 水平拖距偏移随载荷变化标量
  group: Aligning
  block_parameter: QHZ2
  values: 标量
- name: Sht variation with camber, QHZ3
  summary: 水平拖距偏移随外倾变化标量
  group: Aligning
  block_parameter: QHZ3
  values: 标量
- name: Sht variation with load and camber, QHZ4
  summary: 水平拖距偏移随载荷和外倾变化标量
  group: Aligning
  block_parameter: QHZ4
  values: 标量
- name: Inflation pressure influence on trail length, PPZ1
  summary: 气压对拖距长度的影响标量
  group: Aligning
  block_parameter: PPZ1
  values: 标量
- name: Inflation pressure influence on residual aligning torque, PPZ2
  summary: 气压对回正力矩的影响标量
  group: Aligning
  block_parameter: PPZ2
  values: 标量
- name: 'Nominal value of s/R0: effect of Fx on Mz, SSZ1'
  summary: 纵向力对回正力矩的影响标量
  group: Aligning
  block_parameter: SSZ1
  values: 标量
- name: s/R0 variation with lateral to nominal force ratio, SSZ2
  summary: 随侧向力与额定力之比的变动标量
  group: Aligning
  block_parameter: SSZ2
  values: 标量
- name: s/R0 variation with camber, SSZ3
  summary: 随外倾角的变动标量
  group: Aligning
  block_parameter: SSZ3
  values: 标量
- name: s/R0 variation with camber and load, SSZ4
  summary: 随外倾角和载荷的变动标量
  group: Aligning
  block_parameter: SSZ4
  values: 标量
- name: Fx peak reduction due to spin, PDXP1
  summary: 因旋转导致的纵向力峰值衰减标量
  group: Turnslip
  block_parameter: PDXP1
  values: 标量
- name: Fx peak reduction due to spin with varying load, PDXP2
  summary: 因旋转导致的纵向力峰值衰减标量
  group: Turnslip
  block_parameter: PDXP2
  values: 标量
- name: Fx peak reduction due to spin with slip ratio, PDXP3
  summary: 因旋转导致的纵向力峰值衰减标量
  group: Turnslip
  block_parameter: PDXP3
  values: 标量
- name: Cornering stiffness reduction due to spin, PKYP1
  summary: 因旋转导致的刚度衰减标量
  group: Turnslip
  block_parameter: PKYP1
  values: 标量
- name: Fy peak reduction due to spin, PDYP1
  summary: 因旋转导致的侧向力峰值衰减标量
  group: Turnslip
  block_parameter: PDYP1
  values: 标量
- name: Fy peak reduction due to spin with varying load, PDYP2
  summary: 侧向力峰值因旋转随载荷变化的降低量 标量
  group: Turnslip
  block_parameter: PDYP2
  values: 标量
- name: Fy peak reduction due to spin with slip angle, PDYP3
  summary: 侧向力峰值因旋转随侧偏角的降低量 标量
  group: Turnslip
  block_parameter: PDYP3
  values: 标量
- name: Fy peak reduction due to square root of spin, PDYP4
  summary: 侧向力峰值因旋转平方根的降低量 标量
  group: Turnslip
  block_parameter: PDYP4
  values: 标量
- name: Fy vs. slip angle response lateral shift limit, PHYP1
  summary: 侧向力与侧偏角响应 标量
  group: Turnslip
  block_parameter: PHYP1
  values: 标量
- name: Fy vs. slip angle response max lateral shift limit, PHYP2
  summary: 侧向力与侧偏角响应 标量
  group: Turnslip
  block_parameter: PHYP2
  values: 标量
- name: Fy vs. slip angle response max lateral shift limit with load, PHYP3
  summary: 侧向力与侧偏角响应 标量
  group: Turnslip
  block_parameter: PHYP3
  values: 标量
- name: Fy vs. slip angle response lateral shift curvature factor, PHYP4
  summary: 侧向力与侧偏角响应 标量
  group: Turnslip
  block_parameter: PHYP4
  values: 标量
- name: Camber stiffness reduction due to spin, PECP1
  summary: 外倾刚度衰减标量
  group: Turnslip
  block_parameter: PECP1
  values: 标量
- name: Camber stiffness reduction due to spin with load, PECP2
  summary: 外倾刚度衰减标量
  group: Turnslip
  block_parameter: PECP2
  values: 标量
- name: Turn slip pneumatic trail reduction factor, QDTP1
  summary: 转弯滑移气胎拖距衰减因子标量
  group: Turnslip
  block_parameter: QDTP1
  values: 标量
- name: Turn moment for constant turning and zero longitudinal speed, QCRP1
  summary: 恒定转弯力矩标量
  group: Turnslip
  block_parameter: QCRP1
  values: 标量
- name: Turn slip moment increase with spin at 90deg slip angle, QCRP2
  summary: 转弯滑移力矩标量
  group: Turnslip
  block_parameter: QCRP2
  values: 标量
- name: Residual spin torque reduction from side slip, QBRP1
  summary: 残余旋转力矩衰减标量
  group: Turnslip
  block_parameter: QBRP1
  values: 标量
- name: Turn slip moment peak magnitude, QDRP1
  summary: 转弯滑移力矩峰值幅值标量
  group: Turnslip
  block_parameter: QDRP1
  values: 标量
- name: Turn slip moment curvature, QDRP2
  summary: 转弯滑移力矩曲率标量
  group: Turnslip
  block_parameter: QDRP2
  values: 标量
```

### 轮胎选项

### **Tire type** — 类型 `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

使用 **Tire type** 参数选择轮胎数据的来源。

| 目标 | 操作 |
| --- | --- |
| 使用经验方程1, 2实现 Magic Formula 6.2。这些方程使用与模块参数对应的拟合系数。 | 使用文件中的拟合系数更新模块参数：  1. 将 **Tire type** 设置为 `External file`。 2. 在 **External tire    source** 窗格上，点击 **Select    file**。 3. 选择轮胎系数文件。 4. 点击 **Update mask values from    file**。在提示确认的对话框中，点击    **OK**。模块更新参数。 5. 点击 **Apply**。 |
| 选择 Magic Formula 6.2 内置轮胎模型之一来驱动轮胎 1 和 2 的经验方程建模。 | 使用内置轮胎模型的值更新适用的模块参数：  1. 将 **Tire type** 设置为您要实现的轮胎。选项包括：  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. 点击 **Update block with    applicable tire values**。在    **Tire Parameters** 选项卡上，模块更新适用的参数，包括    **Tire nominal section width**、    **Rim radius** 和    **Tire mass**。 3. 点击 **Apply**。 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireType` |
| **值：** | `External file`（默认） | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **数据类型：** | `character vector` |

### **轮胎文件或对象，tireParamSet** — 轮胎文件 `.mat` | `.tir` | `.txt`

包含经验数据的轮胎文件 `.tir` 或对象，用于通过 Magic Formula 6.2 对轮胎纵向和横向行为进行建模。如果提供 `.txt` 文件，请确保该文件包含与模块参数对应的名称。

从文件更新模块参数中的拟合系数：

- 将 **Tire type** 设置为 `External file`。
- 在 **External tire source** 窗格上，选择 **Select file**。
- 选择轮胎系数文件。
- 选择 **Update mask values from file**。在提示您确认的对话框中，点击 **OK**。模块将更新参数。
- 选择 **Apply**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tireParamSet` |
| **值：** | `vdynPassCar.mat`（默认） | `.tir` | `.txt` |
| **数据类型：** | `character vector` |

### **垂直运动** — 垂直运动模型 `None`（默认） | `External deflection`

垂直运动的类型。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `vertType` |
| **值：** | `None`（默认） | `External deflection` |
| **数据类型：** | `character vector` |

### **轮胎侧** — 选择轮胎侧 `Right`（默认） | `Left` | `Symmetric`

指定轮胎侧。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TireSide` |
| **值：** | `Right`（默认） | `Left` | `Symmetric` |
| **数据类型：** | `character vector` |

### **轮胎压力** — 压力标量

轮胎充气压力，*p*，单位为 Pa。

#### 依赖关系

要启用此参数，请清除 **Input tire pressure**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TirePrs` |
| **值：** | scalar |
| **数据类型：** | `double` |

### **帘布层转向** — 包含帘布层转向 `on`（默认） | `off`

选择以在 Magic Formula 6.2 方程中包含帘布层转向。

默认情况下，模块在 Magic Formula 6.2 方程中包含帘布层转向和转弯滑移。这些方程拟合于平带测试数据，并预测多种轮胎效应，包括帘布层转向和转弯滑移。如果您的以下情况，请考虑移除这些效应：

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

#### 编程用法

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

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `turnslip` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

### 绘图

### **Install Extended Tire Features** — 用于安装 Extended Tire Features for Vehicle Dynamics Blockset™ 支持包的选项 按钮

点击 **Install Extended Tire Features** 以安装 Extended Tire Features for Vehicle Dynamics Blockset 支持包。使用该支持包，您可以从 Combined Slip Wheel CPI 模块参数对话框中绘制稳态力和力矩轮胎响应。

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

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NOMPRES` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum pressure, PRESMAX** — 最大压力标量

最大压力，*PRESMAX*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum pressure, PRESMIN** — 最小压力标量

最小压力，*PRESMIN*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PRESMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal normal force, FNOMIN** — 力标量

标称法向力，*FNOMIN*，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FNOMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum normal force, FZMAX** — 力标量

最大法向力，*FZMAX*，单位为 N。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum normal force, FZMIN** — 力标量

最小法向力，*FZMIN*，单位为 N。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FZMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — 容差标量

用于处理低速情况的速度容差，*VXLOW*，单位为 m/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VXLOW` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — 最大允许滑移率标量

最大允许滑移率（绝对值），*KPUMAX*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — 最小允许滑移率标量

最小允许滑移率（绝对值），*KPUMIN*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `KPUMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — 最大允许侧偏角标量

最大允许侧偏角（绝对值），*ALPMAX*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — 最小允许侧偏角标量

最小允许侧偏角（绝对值），*ALPMIN*，单位为
rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ALPMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum allowable camber angle, CAMMAX** — 最大允许外倾角标量

最大允许外倾角 *CAMMAX*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMAX` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Minimum allowable camber angle, CAMMIN** — 最小允许外倾角标量

最小允许外倾角，*CAMMIN*，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CAMMIN` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal longitudinal speed, LONGVL** — 速度标量

名义纵向速度，*LONGVL*，单位为 m/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `LONGVL` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Default tyre side, tyreside** — 侧边 `'Right'`（默认）| 字符

默认轮胎侧边，*tyreside*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tyreside` |
| **值：** | `'Right'`（默认）| 字符 |
| **数据类型：** | `character vector` |

### **Initial wheel rotational velocity, omegao** — 速度标量

初始旋转速度，指定为标量，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegao` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 尺寸

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

### **Tire nominal section width, WIDTH** — 宽度标量

轮胎名义断面宽度，*WIDTH*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WIDTH` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Rim radius, RIM\_RADIUS** — 半径标量

轮辋半径，*RIM\_RADIUS*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RIM_RADIUS` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal aspect ratio, ASPECT\_RATIO** — 比率标量

名义扁平比，*ASPECT\_RATIO*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ASPECT_RATIO` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 垂直

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

初始车轮垂直速度（车轮固定坐标系），*zdoto*，单位为 m/s。

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

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **有效滚动半径峰值，DREFF** — 半径标量

有效滚动半径峰值，*DREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `DREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **高载荷刚度下的有效滚动半径，FREFF** — 半径标量

高载荷刚度下的有效滚动半径，*FREFF*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FREFF` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **空载与额定滚动半径比，Q\_RE0** — 比值标量

空载与额定滚动半径比，*Q\_RE0*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RE0` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **半径转速依赖性，Q\_V1** — 速度标量

半径转速依赖性，*Q\_V1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **刚度转速依赖性，Q\_V2** — 速度标量

刚度转速依赖性，*Q\_V2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_V2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **随变形的线性载荷变化，Q\_FZ1** — 载荷变化标量

随变形的线性载荷变化，*Q\_FZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **随变形的二次载荷变化，Q\_FZ2** — 载荷变化标量

随变形的二次载荷变化，*Q\_FZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **随变形和二次外倾的线性载荷变化，Q\_FZ3** — 载荷变化标量

随变形和二次外倾的线性载荷变化，*Q\_FZ3*，无量纲。

#### 编程用法

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

### **侧向力载荷响应，Q\_FCY** — 刚度标量

侧向力载荷响应，*Q\_FCY*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FCY` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **侧向载荷对侧向刚度依赖引起的垂直刚度变化，Q\_FCY2** — 刚度标量

侧向载荷对侧向刚度依赖引起的垂直刚度变化，*Q\_FCY2*，无量纲。

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

### **Quadratic load dependent camber angle effect on vertical stiffness, Q\_CAM2** — 刚度标量

二次载荷相关外倾角对垂直刚度的影响，
*Q\_CAM2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear reduction of stiffness with load and camber angle, Q\_CAM3** — 刚度标量

刚度和载荷与外倾角之间的线性缩减关系，
*Q\_CAM3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_CAM3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Constant camber and slip angle effect on vertical stiffness, Q\_FYS1** — 刚度标量

恒定外倾角和侧偏角对垂直刚度的影响，
*Q\_FYS1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear camber and slip angle effect on vertical stiffness, Q\_FYS2** — 刚度标量

线性外倾角和侧偏角对垂直刚度的影响，
*Q\_FYS2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_FYS2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic camber and slip angle effect on vertical stiffness, Q\_FYS3** — 刚度标量

二次外倾角和侧偏角对垂直刚度的影响，
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

线性垂直变形对纵向刚度的影响，
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

二次垂直变形对纵向刚度的影响，
*PCFX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **纵向刚度对压力的依赖性，PCFX3** — 压力依赖性标量

纵向刚度对压力的依赖性，*PCFX3*，无量纲。

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

### **纵向刚度对压力的依赖性，PCFY3** — 压力依赖性标量

纵向刚度对压力的依赖性，*PCFY3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCFY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 接触印迹

### **接触长度平方根项，Q\_RA1** — 长度项标量

接触长度平方根项，*Q\_RA1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触长度线性项，Q\_RA2** — 长度项标量

接触长度线性项，*Q\_RA2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RA2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触宽度根项，Q\_RB1** — 宽度项标量

接触宽度根项，*Q\_RB1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **接触宽度线性项，Q\_RB2** — 宽度项标量

接触宽度线性项，*Q\_RB2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Q_RB2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### 纵向

### **Cfx 形状因子，PCX1** — 形状因子标量

形状因子，*Cfx*，*PCX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向摩擦，PDX1** — 摩擦标量

名义法向载荷下的纵向摩擦，*PDX1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **摩擦随载荷的变化，PDX2** — 摩擦变化标量

摩擦随载荷的变化，*PDX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **摩擦随外倾角的变化，PDX3** — 摩擦变化标量

摩擦随外倾角的变化，*PDX3*，单位为 1/rad^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向曲率，PEX1** — 曲率标量

名义法向载荷下的纵向曲率，*PEX1*，无量纲。

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

### **带滑移的纵向曲率因子，PEX4** — 曲率标量

带滑移的纵向曲率因子，*PEX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **名义法向载荷下的纵向滑移刚度，PKX1** — 刚度标量

名义法向载荷下的纵向滑移刚度，*PKX1*，无量纲。

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

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Slip stiffness exponent factor, PKX3** — 滑移刚度标量

滑移刚度指数因子，*PKX3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Horizontal shift in slip ratio at nominal normal load, PHX1** — 滑移率偏移标量

额定法向载荷下滑移率的水平偏移，*PHX1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Variation of horizontal slip ratio with load, PHX2** — 滑移变化标量

水平滑移率随载荷的变化，*PHX2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Vertical shift in load at nominal normal load, PVX1** — 载荷偏移标量

额定法向载荷下载荷的垂直偏移，*PVX1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Variation of vertical shift with load, PVX2** — 载荷变化标量

垂直偏移随载荷的变化，*PVX2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear variation of longitudinal slip stiffness with tire pressure, PPX1** — 刚度变化标量

纵向滑移刚度随轮胎压力的线性变化，*PPX1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2** — 刚度变化标量

纵向滑移刚度随轮胎压力的二次变化，*PPX2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

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

峰值纵向摩擦随轮胎压力的二次变化，*PPX4*，无量纲。

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

### **Camber influence on combined slip Fx stiffness, RBX3** — 外倾角对联合滑移纵向力刚度影响的标量

外倾角对联合滑移纵向力，*Fx*，刚度的影响，*RBX3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RBX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Shape factor for combined slip Fx reduction, RCX1** — 联合滑移纵向力缩减的形状因子标量

联合滑移纵向力，*Fx*，缩减的形状因子，*RCX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RCX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined Fx curvature factor, REX1** — 联合纵向力曲率因子标量

联合纵向力，*Fx*，曲率因子，*REX1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined Fx curvature factor with load, REX2** — 联合纵向力曲率因子标量

联合纵向力，*Fx*，随载荷变化的曲率因子，*REX2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `REX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Combined slip Fx shift factor reduction, RHX1** — 联合滑移纵向力滑移因子标量

联合滑移纵向力，*Fx*，偏移因子缩减，*RHX1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RHX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Overturning

### **Vertical shift of overturning moment, QSX1** — 侧翻力矩标量

侧翻力矩的垂直偏移，*QSX1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Overturning moment due to camber, QSX2** — 外倾引起的侧翻力矩标量

外倾引起的侧翻力矩，*QSX2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Overturning moment due to Fy, QSX3** — 侧向力引起的侧翻力矩标量

侧向力引起的侧翻力矩，*QSX3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx combined lateral force load and camber, QSX4** — 侧翻力矩标量

侧翻力矩，*Mx*，侧向力载荷与外倾组合，*QSX4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to lateral force and camber, QSX5** — 侧翻力矩标量

侧翻力矩，*Mx*，侧向力与外倾引起的载荷效应，*QSX5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx load effect due to B-factor, QSX6** — 侧翻力矩标量

侧翻力矩，*Mx*，B 因子引起的载荷效应，*QSX6*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to camber and load, QSX7** — 侧翻力矩标量

侧翻力矩，*Mx*，由外倾和载荷引起，*QSX7*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Mx due to lateral force and load, QSX8** — 侧翻力矩标量

侧翻力矩，*Mx*，由侧向力和载荷引起，*QSX8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由侧向力和载荷的 B 因子引起的 Mx，QSX9** — 倾覆力矩标量

由侧向力和载荷的 B 因子引起的倾覆力矩，*Mx*，*QSX9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由垂直力和外倾引起的 Mx，QSX10** — 倾覆力矩标量

由垂直力和外倾引起的倾覆力矩，*Mx*，*QSX10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由垂直力和外倾的 B 因子引起的 Mx，QSX11** — 倾覆力矩标量

由垂直力和外倾的 B 因子引起的倾覆力矩，*Mx*，*QSX11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾平方引起的 Mx，QSX12** — 倾覆力矩标量

由外倾平方引起的倾覆力矩，*Mx*，*QSX12*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX12` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由侧向力引起的 Mx，QSX13** — 倾覆力矩标量

由侧向力引起的倾覆力矩，*Mx*，*QSX13*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX13` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由带外倾的侧向力引起的 Mx，QSX14** — 倾覆力矩标量

由带外倾的侧向力引起的倾覆力矩，*Mx*，*QSX14*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSX14` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由充气压力引起的 Mx，PPMX1** — 由压力引起的倾覆力矩标量

由充气压力引起的倾覆力矩，*Mx*，*PPMX1*，无量纲。

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

### **Lateral friction muy, PDY1** — 侧向摩擦标量

侧向摩擦，*μy*，
*PDY1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Lateral friction variation of muy with load, PDY2** — 侧向摩擦变化标量

侧向摩擦，*μy*，
随载荷的变化，*PDY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Lateral friction variation of muy with squared camber, PDY3** — 侧向摩擦变化标量

侧向摩擦，*μy*，
随外倾角平方的变化，*PDY3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy lateral curvature at nominal force FZNOM, PEY1** — 额定力下侧向曲率标量

侧向曲率，*Efy*，在额定
力 *FZNOM* 下，*PEY1*，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with load, PEY2** — 侧向曲率变化标量

侧向曲率，*Efy*，随
载荷的变化，*PEY2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature constant camber dependency, PEY3** — 侧向曲率常数标量

侧向曲率，*Efy*，常数
外倾角依赖性，*PEY3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此
参数内部设置为 0。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with camber, PEY4** — 侧向曲率变化标量

侧向曲率，*Efy*，随
外倾角的变化，*PEY4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Efy curvature variation with camber squared, PEY5** — 侧向曲率变化标量

侧向曲率，*Efy*，随
外倾角平方的变化，*PEY5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param`
函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PEY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Maximum KFy/FZNOM stiffness, PKY1** — 最大刚度标量

最大侧向力刚度，
*KFy*，与额定力
*FZNOM* 之比，
*PKY1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **最大 KFy/FZNOM 刚度处的载荷，PKY2** — 载荷标量

最大侧向力刚度 *KFy* 与名义力 *FZNOM* 之比处的载荷，*PKY2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **KFy/FZNOM 刚度随外倾角的变化，PKY3** — 刚度变化标量

侧向力刚度 *KFy* 与名义力 *FZNOM* 之比随外倾角的变化，*PKY3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **KFy 曲率，PKY4** — 侧向力刚度曲率标量

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

### **FZNOM 处的 SHY 水平偏移，PHY1** — 名义力处的水平偏移标量

名义力 *FZNOM* 处的水平偏移 *SHY*，*PHY1*，无量纲。

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

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz vertical shift at FZNOM, PVY1** — 额定载荷下的垂直偏移标量

额定载荷 *FZNOM* 下的垂直偏移 *Svy*，*PVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz variation with load, PVY2** — 垂直偏移随载荷变化标量

垂直偏移 *Svy* 随载荷的变化，*PVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz variation with camber, PVY3** — 垂直偏移随外倾变化标量

垂直偏移 *Svy* 随外倾的变化，*PVY3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Svy/Fz variation with load and camber, PVY4** — 垂直偏移随载荷和外倾变化标量

垂直偏移 *Svy* 随载荷和外倾的变化，*PVY4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PVY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cornering stiffness variation with inflation pressure, PPY1** — 刚度随压力变化标量

侧偏刚度随充气压力的变化，*PPY1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2** — 刚度随压力变化标量

侧偏刚度随充气压力引起的额定载荷依赖性的变化，*PPY2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Linear inflation pressure on peak lateral friction, PPY3** — 压力标量

充气压力对峰值侧向摩擦力的线性影响，*PPY3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Quadratic inflation pressure on peak lateral friction, PPY4** — Pressure scalar

Quadratic inflation pressure on peak lateral friction，
*PPY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Inflation pressure effect on camber stiffness, PPY5** — Pressure scalar

Inflation pressure effect on camber stiffness，*PPY5*，
无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PPY5` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Combined Fy reduction slope factor, RBY1** — Combined lateral force reduction slope factor scalar

Combined lateral force，*Fy*，
reduction slope factor，*RBY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RBY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy slope reduction with slip angle, RBY2** — Lateral force slope reduction with slip angle scalar

Lateral force，*Fy*，slope reduction
with slip angle，*RBY2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RBY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy shift reduction with slip angle, RBY3** — Lateral force shift reduction with slip angle scalar

Lateral force，*Fy*，shift reduction
with slip angle，*RBY3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中在内部将此参数设置为 0。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RBY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined stiffness variation from camber, RBY4** — Lateral force combined stiffness variation from camber scalar

Lateral force，*Fy*，combined
stiffness variation from camber，*RBY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RBY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shape factor, RCY1** — Lateral force combined reduction shape factor scalar

Lateral force，*Fy*，combined
reduction shape factor，*RCY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RCY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined curvature factor, REY1** — Lateral force combined curvature factor scalar

Lateral force，*Fy*，combined
curvature factor，*REY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param`
函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `REY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined curvature factor with load, REY2** — 侧向力联合曲率因子随载荷标量

侧向力 *Fy* 联合曲率因子随载荷 *REY2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `REY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shift factor, RHY1** — 侧向力联合折减偏移因子标量

侧向力 *Fy* 联合折减偏移因子 *RHY1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RHY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shift factor with load, RHY2** — 侧向力联合折减偏移因子随载荷标量

侧向力 *Fy* 联合折减偏移因子随载荷 *RHY2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RHY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1** — 滑移率侧向力在额定力下标量

滑移率侧向力在额定力 *FZNOM* 下，*RVY1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RVY1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with load, RVY2** — 侧向力随载荷变化标量

侧向力随载荷变化 *RVY2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RVY2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with camber, RVY3** — 侧向力随外倾变化标量

侧向力随外倾变化 *RVY3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RVY3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with slip angle, RVY4** — 侧向力随侧偏角变化标量

侧向力随侧偏角变化 *RVY4*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RVY4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with slip ratio, RVY5** — 侧向力随滑移率变化标量

侧向力随滑移率变化 *RVY5*，无量纲。

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

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由速度^4 引起的阻力矩，QSY4** — 由速度引起的阻力矩标量

由速度^4 引起的阻力矩，*QSY4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾角平方引起的阻力矩，QSY5** — 由外倾角引起的阻力矩标量

由外倾角平方引起的阻力矩，*QSY5*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由外倾角平方和载荷引起的阻力矩，QSY6** — 由外倾角和载荷引起的阻力矩标量

由外倾角平方和载荷引起的阻力矩，*QSY6*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **由载荷引起的阻力矩，QSY7** — 由载荷引起的阻力矩标量

由载荷引起的阻力矩，*QSY7*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QSY7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Torque resistance due to pressure, QSY8** — 压力引起的阻力矩标量

压力引起的阻力矩，*QSY8*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QSY8` |
| **值**：| scalar |
| **Data Types:** | `double` |

### Aligning

### **Trail slope factor for trail Bpt at FZNOM, QBZ1** — 额定力下的拖距斜率因子标量

额定力 *FZNOM* 下拖距 *Bpt* 的拖距斜率因子，*QBZ1*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ1` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with load, QBZ2** — 斜率随载荷变化标量

斜率随载荷变化，*QBZ2*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ2` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with square of load, QBZ3** — 斜率随载荷变化 `0` (default) | scalar

斜率随载荷平方变化，*QBZ3*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ3` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with camber, QBZ4** — 斜率随外倾变化标量

斜率随外倾变化，*QBZ4*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ4` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with absolute value of camber, QBZ5** — 斜率随外倾变化标量

斜率随外倾绝对值变化，*QBZ5*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ5` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with square of camber, QBZ6** — 斜率随外倾变化标量

斜率随外倾平方变化，*QBZ6*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ6` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Br of Mzr slope scaling factor, QBZ9** — 斜率缩放因子标量

斜率缩放因子，*QBZ9*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `QBZ9` |
| **值**：| scalar |
| **Data Types:** | `double` |

### **Br of Mzr cornering stiffness factor, QBZ10** — 侧偏刚度因子标量

*Mzr* 的 *Br* 侧偏刚度因子，*QBZ10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cpt pneumatic trail shape factor, QCZ1** — 气胎拖距形状因子标量

气胎拖距形状因子，*Cpt*，*QCZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail, QDZ1** — 峰值拖距标量

峰值拖距，*Dpt*，*QDZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with load, QDZ2** — 峰值拖距随载荷变化标量

峰值拖距，*Dpt*，随载荷的变化，*QDZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with camber, QDZ3** — 峰值拖距随外倾变化标量

峰值拖距，*Dpt*，随外倾的变化，*QDZ3*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dpt peak trail variation with square of camber, QDZ4** — 峰值拖距随外倾变化标量

峰值拖距，*Dpt*，随外倾平方的变化，*QDZ4*，无量纲。

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

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ6` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with load, QDZ7** — 峰值残余力矩随载荷变化标量

峰值残余力矩，*Dmr*，随载荷的变化，*QDZ7*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ7` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber, QDZ8** — 峰值残余力矩随外倾变化标量

峰值残余力矩，*Dmr*，随外倾的变化，*QDZ8*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ8` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with camber and load, QDZ9** — 峰值残余力矩随外倾角和载荷变化的标量

峰值残余力矩，*Dmr*，随外倾角和载荷的变化，*QDZ9*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ9` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of camber, QDZ10** — 峰值残余力矩随外倾角变化的标量

峰值残余力矩，*Dmr*，随外倾角平方的变化，*QDZ10*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ10` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Dmr peak residual torque variation with square of load, QDZ11** — 峰值残余力矩随载荷变化的标量

峰值残余力矩，*Dmr*，随载荷平方的变化，*QDZ11*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDZ11` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept trail curvature at FZNOM, QEZ1** — 额定力下的拖距曲率标量

拖距曲率，*Ept*，在额定力 *FZNOM* 下，*QEZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with load, QEZ2** — 拖距曲率随载荷变化的标量

拖距曲率，*Ept*，随载荷的变化，*QEZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with square of load, QEZ3** — 拖距曲率随载荷变化的标量

拖距曲率，*Ept*，随载荷平方的变化，*QEZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with sign of alpha-t, QEZ4** — 拖距曲率变化标量

拖距曲率，*Ept*，随 alpha-t 符号的变化，*QEZ4*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中将此参数内部设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Ept variation with sign of alpha-t and camber, QEZ5** — 变化标量

拖距曲率，*Ept*，随 alpha-t 符号和外倾角的变化，*QEZ5*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QEZ5` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht horizontal trail shift at FZNOM, QHZ1** — 额定载荷下的水平拖距偏移标量

额定载荷 *FZNOM* 下的水平拖距偏移 *Sht*，*QHZ1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中在内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht variation with load, QHZ2** — 水平拖距偏移随载荷变化标量

水平拖距偏移 *Sht* 随载荷的变化 *QHZ2*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中在内部将此参数设置为 0。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht variation with camber, QHZ3** — 水平拖距偏移随外倾变化标量

水平拖距偏移 *Sht* 随外倾的变化 *QHZ3*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Sht variation with load and camber, QHZ4** — 水平拖距偏移随载荷和外倾变化标量

水平拖距偏移 *Sht* 随载荷和外倾的变化 *QHZ4*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QHZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Inflation pressure influence on trail length, PPZ1** — 气压对拖距长度的影响标量

气压对拖距长度的影响 *PPZ1*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Inflation pressure influence on residual aligning torque, PPZ2** — 气压对回正力矩的影响标量

气压对残余回正力矩的影响 *PPZ2*，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PPZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Nominal value of s/R0: effect of Fx on Mz, SSZ1** — 纵向力对回正力矩的影响标量

s/R0 的额定值：纵向力 *Fx* 对回正力矩 *Mz* 的影响 *SSZ1*，无量纲。

#### 依赖关系

如果清除 **Ply steer**，模块会在 Magic Formula 方程中在内部将此参数设置为 0。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with lateral to nominal force ratio, SSZ2** — 随侧向力与额定力之比的变动标量

随侧向力与额定力之比的变动，*SSZ2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with camber, SSZ3** — 随外倾角的变动标量

随外倾角的变动，*SSZ3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **s/R0 variation with camber and load, SSZ4** — 随外倾角和载荷的变动标量

随外倾角和载荷的变动，*SSZ4*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SSZ4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### Turnslip

### **Fx peak reduction due to spin, PDXP1** — 因旋转导致的纵向力峰值衰减标量

因旋转导致的纵向力 *Fx* 峰值衰减，*PDXP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with varying load, PDXP2** — 因旋转导致的纵向力峰值衰减标量

因旋转导致的纵向力 *Fx* 峰值衰减，随载荷变化，*PDXP2*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fx peak reduction due to spin with slip ratio, PDXP3** — 因旋转导致的纵向力峰值衰减标量

因旋转导致的纵向力 *Fx* 峰值衰减，随滑移率变化，*PDXP3*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDXP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Cornering stiffness reduction due to spin, PKYP1** — 因旋转导致的刚度衰减标量

因旋转导致的侧偏刚度衰减，*PKYP1*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PKYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin, PDYP1** — 因旋转导致的侧向力峰值衰减标量

因旋转导致的侧向力 *Fy* 峰值衰减，*PDYP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin with varying load, PDYP2** — 侧向力峰值因旋转随载荷变化的降低量 标量

侧向力 *Fy* 峰值因旋转随载荷变化的降低量 *PDYP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to spin with slip angle, PDYP3** — 侧向力峰值因旋转随侧偏角的降低量 标量

侧向力 *Fy* 峰值因旋转随侧偏角的降低量 *PDYP3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy peak reduction due to square root of spin, PDYP4** — 侧向力峰值因旋转平方根的降低量 标量

侧向力 *Fy* 峰值因旋转平方根的降低量 *PDYP4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PDYP4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response lateral shift limit, PHYP1** — 侧向力与侧偏角响应 标量

侧向力 *Fy* 与侧偏角响应的侧向偏移限值 *PHYP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit, PHYP2** — 侧向力与侧偏角响应 标量

侧向力 *Fy* 与侧偏角响应的最大侧向偏移限值 *PHYP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response max lateral shift limit with load, PHYP3** — 侧向力与侧偏角响应 标量

侧向力 *Fy* 与侧偏角响应的随载荷变化的最大侧向偏移限值 *PHYP3*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP3` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Fy vs. slip angle response lateral shift curvature factor, PHYP4** — 侧向力与侧偏角响应 标量

侧向力 *Fy* 与侧偏角响应的侧向偏移曲率因子 *PHYP4*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PHYP4` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin, PECP1** — 外倾刚度衰减标量

由于旋转引起的外倾刚度衰减，*PECP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Camber stiffness reduction due to spin with load, PECP2** — 外倾刚度衰减标量

由于旋转并伴随载荷引起的外倾刚度衰减，*PECP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PECP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip pneumatic trail reduction factor, QDTP1** — 转弯滑移气胎拖距衰减因子标量

转弯滑移气胎拖距衰减因子，*QDTP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDTP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn moment for constant turning and zero longitudinal speed, QCRP1** — 恒定转弯力矩标量

恒定转弯且纵向速度为零时的转弯力矩，*QCRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip moment increase with spin at 90deg slip angle, QCRP2** — 转弯滑移力矩标量

在 90 度滑移角下，转弯滑移力矩随旋转的增加，*QCRP2*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QCRP2` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Residual spin torque reduction from side slip, QBRP1** — 残余旋转力矩衰减标量

由侧滑引起的残余旋转力矩衰减，*QBRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QBRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip moment peak magnitude, QDRP1** — 转弯滑移力矩峰值幅值标量

转弯滑移力矩峰值幅值，*QDRP1*，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `QDRP1` |
| **值：** | 标量 |
| **数据类型：** | `double` |

### **Turn slip moment curvature, QDRP2** — 转弯滑移力矩曲率标量

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

### R2024b：新增 **Vertical Motion** 选项

从 R2024b 开始，将 **Vertical Motion** 指定为 `External Deflection` 会启用 **RadialDeflct** 端口。当未提供力时，可使用此端口在与轮胎交互时定义胎侧变形。

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

### R2022b：新增 **Ply steer** 和 **Turn slip** 参数

从 R2022b 开始，Combined Slip Wheel CPI 模块包含 **Ply steer** 和
**Turn slip** 参数。要从这些模块的
Magic Formula 实现中移除 ply steer 和 turn slip，请清除 **Ply steer** 和
**Turn slip** 参数。

## 描述

符合 CPI Tydex 标准的组合滑移车轮

Combined Slip Wheel CPI 模块实现了由符合接触点接口（CPI）轮胎数据交换格式（TYDEX）[3] 标准的 Magic Formula[1][2] 6.2 所表征的车轮的纵向和横向行为。您可以导入自己的轮胎模型或使用内置轮胎模型。在需要低频轮胎-道路相互作用以确定车辆加速、制动和车轮滚动阻力的传动系和车辆仿真中使用该模块。该模块适用于需要组合横向滑移的应用，例如横向运动和横摆稳定性研究。

基于车轮旋转速度、纵向和横向速度、车轮外倾角以及充气压力，该模块确定所有六个自由度（DOF）的垂向运动、力和力矩。使用垂向自由度来研究来自道路轮廓或底盘运动的轮胎-悬架共振。

如果您安装了 Extended Tire Features for Vehicle Dynamics Blockset 支持包，则可以使用以下附加功能：

- 绘图生成 — 点击 **Plot steady state force, moment response** 按钮生成以下绘图：

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle [rad]**
  - **Longitudinal force [N] vs Longitudinal slip []**
  - **Longitudinal force [N] vs Lateral force [N]**
- 导入轮胎参数 — 使用 `tireModel.get` 方法将 Combined Slip Wheel CPI 模块中定义的轮胎参数值导入到 `tireModel` 对象。
- 导出轮胎参数 — 使用 `set` 方法将轮胎参数值从 `tireModel` 对象导出到 Combined Slip Wheel CPI 模块。
- 轮胎模型转换 — 使用 `convert` 方法将以下类型之一的轮胎模型转换为可导入 Combined Slip Wheel CPI 模块的 Magic Formula 6.2 轮胎模型：

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

### CPI Tire Coordinate System

该模块使用轮胎坐标系轴
(*XT*、
*YT*、
*ZT*)，这些轴固定在附着于轮胎的参考坐标系中。原点位于轮胎与地面的接触点。

CPI 轮胎坐标系以红色显示。

**注意**

CPI 轮胎坐标系（红色）等效于 TYDEX 车轮轴线
坐标系。

1

Z-Up 轮胎和车轮坐标系，显示车轮平面和道路平面

| 轴 | 描述 |
| --- | --- |
| *XT* | *XT* 和 *YT* 平行于道路平面。车轮平面与道路平面的交线定义了 *XT* 轴的方向。 |
| *YT* | *YT* 是车轮旋转轴在地面上的投影。 |
| *ZT* | *ZT* 指向上方。 |
