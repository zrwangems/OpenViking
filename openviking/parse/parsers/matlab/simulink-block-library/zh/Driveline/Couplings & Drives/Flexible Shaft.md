---
type: simulink-block
title: 'Flexible Shaft'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'flexibleshaft'
documentation_source_path: 'ref/flexibleshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Flexible Shaft

## 端口

### 输出

### **Fr** — 轴承支撑上的力物理信号

与轴施加在轴承支撑上的力关联的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **Model bending** 设置为 `On`。

### **M** — 轴承支撑上的力矩物理信号

与轴施加在轴承支撑上的力矩关联的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **Model bending** 设置为 `On`。

### **V** — 轴平移速度物理信号

与轴在轴承支撑处的平移速度关联的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **Model bending** 设置为 `On`。

### **W** — 轴角速度物理信号

与轴在轴承支撑处的角速度关联的物理信号输出端口。

#### 依赖关系

要启用此端口，请将 **Model bending** 设置为 `On`。

### 守恒

### **B** — 基座旋转机械

与轴基座关联的旋转守恒端口。

### **F** — 从动端旋转机械

与轴从动端关联的旋转守恒端口。

## 参数

### 轴

### **Model torsional flexibility** — 扭转柔度选项 `on`（默认） | `off`

是否对扭转柔度建模。

### **Model bending flexibility** — 弯曲柔度选项 `off`（默认） | `on`

是否对弯曲柔度建模。

### **Minimum number of flexible elements** — 柔性单元最小数量 `1`（默认） | 正整数

用于近似的柔性单元最小数量，*Nmin*。

柔性单元可能具有不同的长度，或者仿真的柔性单元数量 *N* 可能大于 *Nmin*。有关详细信息，请参阅节点放置算法。

更大的柔性单元数量 *N* 会提高模型保真度，但会降低仿真性能。单柔性单元模型（*N*=1）的扭转固有频率接近连续分布参数模型的第一阶固有频率。

如果模型保真度比性能更重要，请选择 2、4、8 或更多柔性单元。例如，具有 16 个柔性单元的模型分别以 0.1%、1.9%、1.6% 和 5.3% 的精度表示最低的四个扭转固有频率。通常，准确建模弯曲动力学所需的柔性单元比准确建模扭转动力学所需的更多。

有关详细信息，请参阅提高仿真速度或精度。

#### 依赖关系

要启用此参数，请选择 **Model torsional flexibility** 或 **Model bending flexibility**。

### **Parameterization** — 参数化方法 `By stiffness and inertia`（默认） | `By material and geometry` | `By segment stiffness and inertia` | `By material and segment geometry`

参数化方法。您可以对均匀轴或轴向非均匀轴针对以下任一属性建模：

- 扭转刚度
- 扭转惯量
- 弯曲刚度
- 密度
- 剪切模量
- 杨氏模量
- 外径
- 内径

从以下均匀轴参数化中选择：

- `By stiffness and inertia` — 指定轴的扭转刚度和惯量，以及每单位长度的密度。对于弯曲模型，还要指定轴的弯曲刚度和长度。
- `By material and geometry` — 指定轴的长度和轴向横截面几何形状（以内径和外径表示）。对于轴材料，指定密度和剪切模量。对于弯曲模型，还要指定轴材料的杨氏模量。

轴向非均匀轴模型的参数化选项包括：

- `By segment stiffness and inertia` — 对于轴的每个段，指定扭转刚度、扭转惯量和每单位长度的密度。对于弯曲模型，还要指定每个段的弯曲刚度和长度。
- `By material and segment geometry` — 对于轴的每个段，指定长度和轴向横截面几何形状（以内径和外径表示）。对于轴的材料，指定密度和剪切模量。对于弯曲模型，还要指定轴材料的杨氏模量。

### **Shaft length** — 轴长度 `1` `m`（默认） | 正标量

轴的长度。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Parameterization** 设置为 `By material and geometry`。
- 选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia` 或 `By material and geometry`。

### **Segment lengths [B,...,F]** — 每个轴段的长度 `[1, .5, .25]`（默认） | 向量

为对轴向非均匀轴建模而沿长度方向将轴划分成的每个轴段的长度。向量中的元素数量等于用于对非均匀轴建模的段数。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Parameterization** 设置为 `By material and segment geometry`。
- 选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By segment stiffness and inertia`。

### **Torsional stiffness** — 材料刚度 `2e5` `N*m/rad`（默认） | 正标量

轴的每弧度扭转扭矩。

#### 依赖关系

要启用此参数，请选择 **Model torsional flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia`。

### **Torsional Inertia** — 极惯性矩 `0.02` `kg*m^2`（默认） | 正标量

轴抵抗扭转加速度的能力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By stiffness and inertia`。

### **Segment torsional stiffness [B,...,F]** — 每个轴段的材料刚度 `[400000, 200000, 100000]` `N*m/rad`（默认） | 正向量

轴的每个段的每弧度扭转扭矩。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By segment stiffness and inertia`。

### **Segment torsional inertia [B,...,F]** — 每个轴段的极惯性矩 `[.025, .02, .015]` `kg*m^2`（默认） | 正向量

每个轴段抵抗扭转加速度的能力。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By segment stiffness and inertia`。

### **Bending rigidity** — 弯曲刚度 `5e5` `m^4*Pa`（默认） | 正标量

轴材料的弯曲刚度。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia`。

### **Linear density** — 单位长度密度 `19` `kg/m`（默认） | 正标量

轴材料在轴每单位长度上的密度。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia`。

### **Segment bending rigidity [B,...,F]** — 每个段的弯曲刚度 `[600000, 500000, 400000]` `m^4*Pa`（默认） | 正元素向量

轴每个连续段的材料的弯曲刚度。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia`。

### **Segment linear density [B,...,F]** — 每个段的单位长度密度 `[20, 19, 18]` `kg/m`（默认） | 正向量

轴每个段的轴材料在每单位长度上的密度。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By segment stiffness and inertia`。

### **Material density** — 材料密度 `7.8e3` `kg/m^3`（默认） | 正标量

轴材料的密度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。

### **Shear modulus** — 剪切模量 `7.93e9` `Pa`（默认） | 正标量

轴材料的剪切模量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。

### **Shaft geometry** — 横截面几何形状 `Solid`（默认） | `Annular`

沿轴长度的横截面几何形状。如果轴或轴段为中空，请选择 `Annular`。否则，选择 `Solid`。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。

### **Young's modulus** — 杨氏模量 `200e9` `Pa`（默认） | 正标量

材料的杨氏模量。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。

### **Shaft outer diameter** — 轴的外径 `0.075` `m`（默认） | 正标量

轴的外径。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and geometry`。

### **Shaft inner diameter** — 轴的内径 `0.05` `m`（默认） | 正标量

环形轴的内径。该值必须小于 **Shaft outer diameter** 参数指定的值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and geometry`，并将 **Shaft geometry** 设置为 `Annular`。

### **Segment outer diameters [B,...,F]** — 每个轴段的外径 `[.085, .075, .065]` `m`（默认） | 正向量

每个轴段的外径。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and segment geometry`。

### **Segment inner diameters [B,...,F]** — 每个轴段的内径 `[.055, .05, .045]` `m`（默认） | 向量

轴段的内径。向量中的元素数量必须与 **Segment lengths [B,...,F]** 参数指定的元素数量相同。向量中元素的顺序对应于相对于 **B**（轴的基座端）的段顺序。每个值必须小于 **Segment outer diameter [B,...,F]** 参数指定的对应值。如果某个轴段为实心，请为对应向量元素指定 `0`。向量中至少有一个元素必须为正。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By material and segment geometry`，并将 **Shaft geometry** 设置为 `Annular`。

### 扭转

### **Damping ratio from internal losses** — 材料阻尼比 `0.01`（默认） | 正标量

材料阻尼比。

#### 依赖关系

要启用此参数，请选择 **Model torsional flexibility**。

### **Viscous friction coefficients at base (B) and follower (F)** — 粘性摩擦系数 `[0, 0]` `N*m/(rad/s)`（默认） | 非负向量

轴基座端 **B** 和从动端 **F** 处的粘性摩擦系数。该向量必须包含两个元素。

#### 依赖关系

要启用此参数，请取消选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By stiffness and inertia` 或 `By segment stiffness and inertia`。

### **Viscous friction coefficients at each support [B1,...,F1]** — 粘性摩擦系数 `[0, 0]` `N*m/(rad/s)`（默认） | 非负向量

每个支撑处的粘性摩擦系数。向量中的元素数量必须与 **Number of supports** 参数中指定的数量相同。元素顺序必须对应于每个支撑相对于轴基座端 **B** 的顺序位置。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 选择 **Model bending flexibility**。
- 取消选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。

### **Initial shaft torsional deflection** — 初始轴扭转偏转 `0` `rad`（默认） | 非负标量

仿真开始时轴的角偏转。正的初始偏转会导致轴的基座端 **B** 相对于轴的从动端 **F** 正向旋转。

#### 依赖关系

要启用此参数，请选择 **Model torsional flexibility**。

### **Initial shaft rotational velocity** — 初始角速度 `0` `rpm`（默认） | 非负标量

仿真开始时轴的角速度。

#### 依赖关系

要启用此参数，请选择 **Model torsional flexibility**。

### 支撑

要启用这些参数，请选择以下选项之一：

- 取消选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`。
- 选择 **Model bending flexibility**。

### **Number of supports** — 支撑数量 `2`（默认） | `3` | `4`

轴支撑的数量。

#### 依赖关系

要启用这些参数，请选择以下选项之一：

- 取消选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`
- 选择 **Model bending flexibility**。

### **Support locations relative to base (B)** — 支撑位置 `[0, 1]` `m`（默认） | 非负递增向量

支撑相对于轴基座端 **B** 的位置。元素数量必须与 **Number of supports** 参数指定的数量相同。元素顺序对应于每个支撑相对于轴基座端的顺序位置。最大值不得大于轴的长度。对于分段轴模型，轴的长度等于各段长度之和。

#### 依赖关系

- 取消选择 **Model bending flexibility**，并将 **Parameterization** 设置为 `By material and geometry` 或 `By material and segment geometry`
- 选择 **Model bending flexibility**。

### **Base (B1) mounting type** — 支撑 *B1* 安装类型 `Clamped`（默认） | `Pinned` | `Free` | `Bearing matrix` | `Speed-dependent bearing matrix`

轴基座端的安装类型。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Base (B1) rotational damping [xx,yy]** — *B1* 支撑的旋转阻尼 `[1e3, 1e3]` `N*m/(rad/s)`（默认）| vector

*B1* 支撑的旋转阻尼。
*B1* 是最靠近 **B**（轴的基端）的支撑。二元素向量的元素为：

- *xx* — 绕 *x* 轴的阻尼
- *yy* — 绕 *y* 轴的阻尼

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Pinned`、`Free`、`Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Base (B1) translational damping [xx,xy,yx,yy]** — *B1* 支撑的平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5]` `N/(m/s)`（默认）| vector

*B1* 支撑的平移阻尼。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的阻尼
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yy* — 沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Bearing matrix`。

### **Base (B1) speed-dependent translational damping [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — *B1* 支撑的速度相关平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5; 1e4, -2.5e4, -2.5e4, 1.4e5; 5e3, -1.0e4, -1.0e4, 2.0e4]` `N/(m/s)`（默认）| matrix

*B1* 支撑的速度相关平移阻尼。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的阻尼
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Bearing matrix`。

### **Base (B1) rotational stiffness [xx,yy]** — *B1* 支撑的旋转刚度 `[1e4, 1e4]` `N*m/rad`（默认）| nonnegative vector

*B1* 支撑的旋转刚度。二元素向量的元素为：

- *xx* — 绕 *x* 轴的刚度
- *yy* — 绕 *y* 轴的刚度

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Base (B1) translational stiffness [xx,xy,yx,yy]** — *B1* 支撑的平移刚度 `[1e6, -2e5, -3e5, 5e]` `N/m`（默认）| vector

*B1* 支撑的平移刚度。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的刚度
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yy* — 沿 *y* 轴方向的刚度

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Bearing matrix`。

### **Base (B1) speed-dependent translational stiffness [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — *B1* 支撑的速度相关平移刚度 `[1e6, -6e5, -3.5e6, 8e6; 1e6, -2e5, -3.0e6, 5e6; 1e6, -5e4, -2.5e6, 3e6]` `N/m`（默认）| matrix

*B1* 支撑的速度相关平移刚度。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的刚度
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的刚度

所有 *xx* 和 *yy* 刚度值必须为正。所有 *xy* 和 *yx* 值在所有速度下必须为零或非零。

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Base (B1) mounting type** 设置为 `Speed-dependent bearing matrix`。

### **Intermediate (I1) mounting type** — *I1* 支撑的安装类型 `Clamped`（默认）| `Pinned` | `Free` | `Bearing matrix` | `Speed-dependent bearing matrix`

*I1* 支撑处的安装类型。*I1* 支撑是最靠近 *B1* 支撑的中间支撑。

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Number of supports** 设置为 `3` 或 `4`。

### **Intermediate (I1) rotational damping [xx,yy]** — *I1* 支撑的旋转阻尼 `[1e3, 1e3]` `N*m/(rad/s)`（默认）| vector

*I1* 支撑的旋转阻尼。二元素向量的元素为：

- *xx* — 绕 *x* 轴的阻尼
- *yy* — 绕 *y* 轴的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Pinned`、`Free`、`Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Intermediate (I1) translational damping [xx,xy,yx,yy]** — *I1* 支撑的平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5]` `N/(m/s)`（默认）| vector

*I1* 支撑的平移阻尼。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的阻尼
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yy* — 沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Bearing matrix`。

### **Intermediate (I1) speed-dependent translational damping [xx1,xy1,yx1,yy1;...xxsS,xyS,yxS,yyS]** — *I1* 支撑的速度相关平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5; 1e4, -2.5e4, -2.5e4, 1.4e5; 5e3, -1.0e4, -1.0e4, 2.0e4]` `N/(m/s)`（默认）| matrix

*I1* 支撑的速度相关平移阻尼。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的阻尼
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Bearing matrix`。

### **Intermediate (I1) rotational stiffness [xx,yy]** — *I1* 支撑的旋转刚度 `[1e4, 1e4]` `N*m/rad`（默认）| nonnegative vector

*I1* 支撑的旋转刚度。二元素向量的元素为：

- *xx* — 绕 *x* 轴的刚度
- *yy* — 绕 *y* 轴的刚度

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Intermediate (I1) translational stiffness [xx,xy,yx,yy]** — *I1* 支撑的平移刚度 `[1e6, -2e5, -3e5, 5e]` `N/m`（默认）| vector

*I1* 支撑的平移刚度。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的刚度
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yy* — 沿 *y* 轴方向的刚度

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Bearing matrix`。

### **Intermediate (I1) speed-dependent translational stiffness [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — *I1* 支撑的速度相关平移刚度 `[1e6, -6e5, -3.5e6, 8e6; 1e6, -2e5, -3.0e6, 5e6; 1e6, -5e4, -2.5e6, 3e6]` `N/m`（默认）| matrix

*I1* 支撑的速度相关平移刚度。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的刚度
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的刚度

所有 *xx* 和 *yy* 刚度值必须为正。所有 *xy* 和 *yx* 值在所有速度下必须为零或非零。

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `3` 或 `4`。
- 将 **Intermediate (I1) mounting type** 设置为 `Speed-dependent bearing matrix`。

### **Intermediate (I2) mounting type** — *I2* 支撑的安装类型 `Clamped`（默认）| `Pinned` | `Free` | `Bearing matrix` | `Speed-dependent bearing matrix`

*I2* 支撑处的安装类型。*I2* 支撑位于 *I1* 和 *F1* 支撑之间。

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Number of supports** 设置为 `4`。

### **Intermediate (I2) rotational damping [xx,yy]** — *I2* 支撑的旋转阻尼 `[1e3, 1e3]` `N*m/(rad/s)`（默认）| vector

*I2* 支撑的旋转阻尼。二元素向量的元素为：

- *xx* — 绕 *x* 轴的阻尼
- *yy* — 绕 *y* 轴的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Pinned`、`Free`、`Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Intermediate (I2) translational damping [xx,xy,yx,yy]** — *I2* 支撑的平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5]` `N/(m/s)`（默认）| vector

*I2* 支撑的平移阻尼。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的阻尼
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yy* — 沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Bearing matrix`。

### **Intermediate (I2) speed-dependent translational damping [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — *I2* 支撑的速度相关平移阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5; 1e4, -2.5e4, -2.5e4, 1.4e5; 5e3, -1.0e4, -1.0e4, 2.0e4]` `N/(m/s)`（默认）| matrix

*I2* 支撑的速度相关平移阻尼。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的阻尼
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的阻尼
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的阻尼
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的阻尼

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Speed-dependent bearing matrix`。

### **Intermediate (I2) rotational stiffness [xx,yy]** — *I2* 支撑的旋转刚度 `[1e4, 1e4]` `N*m/rad`（默认）| nonnegative vector

*I2* 支撑的旋转刚度。二元素向量的元素为：

- *xx* — 绕 *x* 轴的刚度
- *yy* — 绕 *y* 轴的刚度

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Intermediate (I2) translational stiffness [xx,xy,yx,yy]** — *I2* 支撑的平移刚度 `[1e6, -2e5, -3e5, 5e]` `N/m`（默认）| vector

*I2* 支撑的平移刚度。四元素向量的元素为：

- *xx* — 沿 *x* 轴方向的刚度
- *xy* — 沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yx* — 沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yy* — 沿 *y* 轴方向的刚度

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Bearing matrix`。

### **Intermediate (I2) speed-dependent translational stiffness [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — *I2* 支撑的速度相关平移刚度 `[1e6, -6e5, -3.5e6, 8e6; 1e6, -2e5, -3.0e6, 5e6; 1e6, -5e4, -2.5e6, 3e6]` `N/m`（默认）| vector

*I2* 支撑的速度相关平移刚度。矩阵的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的向量中的元素数。每行包含四个元素：

- *xxs* — 在第 *s* 个速度下沿 *x* 轴方向的刚度
- *xys* — 在第 *s* 个速度下沿 *x* 轴方向并与 *y* 轴方向运动耦合的刚度
- *yxs* — 在第 *s* 个速度下沿 *y* 轴方向并与 *x* 轴方向运动耦合的刚度
- *yys* — 在第 *s* 个速度下沿 *y* 轴方向的刚度

所有 *xx* 和 *yy* 刚度值必须为正。所有 *xy* 和 *yx* 值在所有速度下必须为零或非零。

#### 依赖项

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Number of supports** 设置为 `4`。
- 将 **Intermediate (I2) mounting type** 设置为 `Speed-dependent bearing matrix`。

### **Follower (F1) mounting type** — *F1* 支撑的安装类型 `Clamped`（默认）| `Pinned` | `Free` | `Bearing matrix` | `Speed-dependent bearing matrix`

轴从动端处的安装类型。

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**。

### **Follower (F1) rotational damping [xx,yy]** — *F1* 支撑的旋转阻尼 `[1e3, 1e3]` `N*m/(rad/s)`（默认）| vector

*F1* 支撑的旋转阻尼，*F1* 是位于最靠近 **F**（轴的从动端）的支撑。二元素向量的元素为：

- *xx* — 绕 *x* 轴的阻尼
- *yy* — 绕 *y* 轴的阻尼

#### 依赖项

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Pinned`、`Free`、`Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Follower (F1) translational damping [xx,xy,yx,yy]** — 支撑 *F1* 平动阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5]` `N/(m/s)` (default) | vector

*F1* 支撑的平动阻尼，该支撑是最靠近 **F**（轴的从动端）的支撑。四元素 vector 的元素为：

- *xx* — 沿 *x* 轴方向的阻尼
- *xy* — 沿 *x* 轴方向的阻尼与沿 *y* 轴方向的运动耦合
- *yx* — 沿 *y* 轴方向的阻尼与沿 *x* 轴方向的运动耦合
- *yy* — 沿 *y* 轴方向的阻尼

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Bearing matrix`。

### **Follower (F1) speed-dependent translational damping [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — 支撑 *F1* 随速度变化的平动阻尼 `[2e4, -4.4e4, -4.4e4, 3.5e5; 1e4, -2.5e4, -2.5e4, 1.4e5; 5e3, -1.0e4, -1.0e4, 2.0e4]` `N/(m/s)` (default) | matrix

*F1* 支撑的随速度变化的平动阻尼，该支撑是最靠近 **F**（轴的从动端）的支撑。

matrix 的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的 vector 中的元素数。每行包含四个元素：

- *xxs* — 第 *s* 个速度下沿 *x* 轴方向的阻尼
- *xys* — 第 *s* 个速度下沿 *x* 轴方向的阻尼与沿 *y* 轴方向的运动耦合
- *yxs* — 第 *s* 个速度下沿 *y* 轴方向的阻尼与沿 *x* 轴方向的运动耦合
- *yys* — 第 *s* 个速度下沿 *y* 轴方向的阻尼

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Bearing matrix`。

### **Follower (F1) rotational stiffness [xx,yy]** — 支撑 *F1* 旋转刚度 `[1e4, 1e4]` `N*m/rad` (default) | nonnegative vector

*F1* 支撑的旋转刚度，该支撑是最靠近 **F**（轴的从动端）的支撑。二元素 vector 的元素为：

- *xx* — 绕 *x* 轴的刚度
- *yy* — 绕 *y* 轴的刚度

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Bearing matrix` 或 `Speed-dependent bearing matrix`。

### **Follower (F1) translational stiffness [xx,xy,yx,yy]** — 支撑 *F1* 平动刚度 `[1e6, -2e5, -3e5, 5e]` `N/m` (default) | vector

*F1* 支撑的平动刚度，该支撑是最靠近 **F**（轴的从动端）的支撑。四元素 vector 的元素为：

- *xx* — 沿 *x* 轴方向的刚度
- *xy* — 沿 *x* 轴方向的刚度与沿 *y* 轴方向的运动耦合
- *yx* — 沿 *y* 轴方向的刚度与沿 *x* 轴方向的运动耦合
- *yy* — 沿 *y* 轴方向的刚度

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Bearing matrix`。

### **Follower (F1) speed-dependent translational stiffness [xx1,xy1,yx1,yy1;...xxS,xyS,yxS,yyS]** — 支撑 *F1* 随速度变化的平动刚度 `[1e6, -6e5, -3.5e6, 8e6; 1e6, -2e5, -3.0e6, 5e6; 1e6, -5e4, -2.5e6, 3e6]` `N/m` (default) | matrix

*F1* 支撑的随速度变化的平动刚度，该支撑是最靠近 **F**（轴的从动端）的支撑。

matrix 的行数必须等于为 **Bearing speed [s1, … sS]** 参数指定的 vector 中的元素数。每行包含四个元素：

- *xxs* — 第 *s* 个速度下沿 *x* 轴方向的刚度
- *xys* — 第 *s* 个速度下沿 *x* 轴方向的刚度与沿 *y* 轴方向的运动耦合
- *yxs* — 第 *s* 个速度下沿 *y* 轴方向的刚度与沿 *x* 轴方向的运动耦合
- *yys* — 第 *s* 个速度下沿 *y* 轴方向的刚度

所有 *xx* 和 *yy* 刚度值必须为正。所有 *xy* 和 *yx* 值在所有速度下必须为零或非零。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Follower (F1) mounting type** 设置为 `Speed-dependent bearing matrix`。

### **Bearing speed [s1,...,sS]** — 支撑轴承转速 `[200, 500, 1500]` `rpm` (default) | nonnegative vector

支撑轴承转速。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将以下参数之一设置为 `Speed-dependent bearing matrix`：

- **Base (B1) mounting type**
- **Intermediate (I1) mounting type**
- **Intermediate (I2) mounting type**
- **Follower (F1) mounting type**

### 弯曲

要启用这些参数，请选择 **Model bending flexibility**。

### **Damping constant proportional to mass** — 与质量成正比的阻尼常数 *α* `10` `1/s` (default) | positive scalar

阻尼常数 *α*，与质量成正比。

当启用特征模态弯曲模型时，每个模态质量-弹簧-阻尼器系统中的平动阻尼器具有阻尼系数 *aMMode*，其中 *MMode* 是模态质量。

当启用集中质量弯曲模型时，阻尼 matrix *α**M*** 被添加到系统中。***M*** 是运动方程的质量 matrix。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Damping constant proportional to stiffness** — 与刚度成正比的阻尼常数 *β* `1e-8` `s` (default) | positive scalar

阻尼常数 *β*，与刚度成正比。

当启用集中质量弯曲模型时，阻尼 matrix *β**K*** 被添加到系统中。***K*** 是运动方程的刚度 matrix。当启用特征模态弯曲模型时，阻尼 *β**KModal*** 被添加到系统中。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Rigid masses concentrically attached to shaft** — 连接到轴的刚性质量类型 `None` (default) | `Point mass` | `Disk`

连接到轴的刚性质量类型（如果有）。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Rigid mass distances from base (B)** — 沿轴距基座节点的刚性质量位置 `0.5` `m` (default) | nonnegative scalar or vector

刚性质量沿轴的位置，距 **B**（轴的基端）的距离。对于多个质量，请指定递增的 row vector。vector 中的元素数必须等于连接到轴的刚性质量数。该 scalar 的值，或者对于多个质量，vector 中的最大值，不得超过轴的长度。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Rigid masses concentrically attached to shaft** 设置为 `Point mass`。

### **Rigid masses** — 同心连接到轴的刚性质量的质量 `2` `kg` (default) | positive scalar or vector

同心连接到轴的刚性质量的质量。对于多个质量，请指定 row vector。vector 中元素的数量和顺序必须对应于为 **Rigid mass distances from base (B)** 参数指定的 vector 中的元素。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Rigid masses concentrically attached to shaft** 设置为 `Point mass`。

### **Rigid mass diametric moments of inertia about axis perpendicular to shaft** — 绕垂直于轴的轴线的直径转动惯量 `0.025` `kg*m^2` (default) | positive scalar or vector

刚性质量绕垂直于轴的轴线的转动惯量。对于多个质量，请指定 row vector。vector 中元素的数量和顺序必须对应于为 **Rigid mass distances from base (B)** 参数指定的 vector 中的元素。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Rigid masses concentrically attached to shaft** 设置为 `Disk`。

### **Rigid mass polar moments of inertia about shaft axis** — 绕轴轴线的极转动惯量 `0.050` `kg*m^2` (default) | positive scalar or vector

刚性质量绕主轴轴线的极转动惯量。对于多个质量，请指定 row vector。vector 中元素的数量和顺序必须对应于为 **Rigid mass distances from base (B)** 参数指定的 vector 中的元素。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Rigid masses concentrically attached to shaft** 设置为 `Disk`。

### **Enable static unbalances that excite bending** — 静态不平衡激励选项 `on` (default) | `off`

是否启用会激励弯曲的静态不平衡。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Static unbalances** — 激励性静态不平衡 `[.01, .01]` `m*kg` (default) | nonnegative vector

激励弯曲的静态不平衡。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable static unbalances that excite bending**。

### **Static unbalance distances from base (B)** — 距基座 (B) 的静态不平衡距离 `[.33, .67]` `m` (default) | nonnegative vector

激励性静态不平衡距 **B**（轴的基端）的距离。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable static unbalances that excite bending**。

### **Static unbalance offset angles** — 静态不平衡偏移角 `[0, pi]` `rad` (default) | nonnegative vector

激励性静态不平衡的初始角，该角度绕轴的中心线并相对于 *x* 轴。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable static unbalances that excite bending**。

### **Enable external forces that excite bending** — 外部力激励选项 `off` (default) | `on`

是否对外部力激励弯曲进行建模。有关详细信息，请参阅弯曲模型集中质量法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **External force magnitudes** — 外部力大小 `[1, 2]` `N` (default) | vector

外部力的大小。有关详细信息，请参阅弯曲模型集中质量法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable external forces that excite bending**。

### **External force distances from base (B)** — 外部力位置 `[.25, .75]` `m` (default)

外部力相对于端口 **B** 的位置。有关详细信息，请参阅弯曲模型集中质量法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable external forces that excite bending**。

### **External force frequency harmonic of rotor speed** — 外部力频率谐波 `[.5, 2]` (default) | vector

外部力频率相对于转子速度的谐波。有关详细信息，请参阅弯曲模型集中质量法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable external forces that excite bending**。

### **External force offset angles** — 外部力偏移角 `[pi / 2, 3 * pi / 4]` `rad` (default)

外部力的偏移角。有关详细信息，请参阅弯曲模型集中质量法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility** 和 **Enable external forces that excite bending**。

### 高级弯曲

要启用这些参数，请选择 **Model bending flexibility**。

### **Bending vibration analysis method** — 弯曲振动分析方法 `Lumped mass` (default) | `Eigenmodes`

分析弯曲振动的方法。有关详细信息，请参阅弯曲模型集中质量法和弯曲模型特征模态法。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**。

### **Bending mode determination** — 弯曲模态确定方法 `Simscape determined` (default) | `User defined`

确定特征模态频率和振型的方法：

- `Simscape determined` — Simscape 根据您指定的边界条件确定模态。
- `User defined` — 直接指定特征模态频率和振型。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Bending vibration analysis method** 设置为 `Eigenmodes`。

### **Limit number of modes** — 最大模态数 `6` (default) | positive integer scalar

Simscape 求解器确定的最大模态数。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `Simscape determined`。

### **Simulated eigenmode dependency on rotation speed** — 特征模态依赖性 `Static` (default) | `Dynamic`

特征模态属性对轴转速的模拟依赖性：

- Static — 弯曲分析在轴的转速变化期间保持特征模态属性恒定。
- Dynamic — 弯曲分析会随着轴转速的变化调整特征模态属性。该模块使用为 **Bearing speed [s1,…, sS]** 参数指定的 vector 中的元素作为查找表参考点。对于此模型，随速度变化的平动刚度元素的相对大小在每个轴承速度下可能不会变化。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。

### **Nominal shaft speed for bending modes** — 标称轴转速 `5000` `rpm` (default) | scalar

用于弯曲模态分析的额定轴转速。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Simulated eigenmode dependency on rotation speed** 设置为 `Static`。

### **Eigenfrequency upper limit** — 特征频率上限 `1e8` `rpm` (default) | positive integer scalar

特征频率上限。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `Simscape determined`。

### **Shaft length increments for mode shape computations** — 轴长度增量 `0.01` `m` (default) | positive scalar

用于模态质量和振型计算的轴长度增量。有关详细信息，请参阅弯曲模型特征模态法。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `Simscape determined`。

### **Modal frequencies [m]** — 与轴承速度无关的模态频率 `[280, 644, 615, 1285]` `rad/s` (default) | nonnegative vector

用于与轴承速度无关的模型的模态频率。有关详细信息，请参阅弯曲模型特征模态法。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 不要将任何安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **Modal frequencies [s,m]** — 轴承转速相关模态频率 `[257, 780, 580, 1560; 280, 644, 615, 1285; 294, 513, 636, 1020]` `rad/s`（默认）| 非负矩阵

轴承转速相关模型的模态频率。有关详细信息，请参阅 Bending Model Eigenmodes Method。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **Shaft position [z]** — 轴位置 `[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]`（默认）| 递增非负向量

模态振型的轴位置。向量中的元素数量对应于 *X* 方向和 *Y* 方向模态振型的行数。有关详细信息，请参阅 Bending Model Eigenmodes Method。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **X-direction mode shapes [z,m]** — 轴承转速无关的 *X* 方向模态振型 `[.1648, .0086, -.2759, .0162; .1671, .0093, -.2231, .0133; .1691, .01, -.1689, .0102; .1707, .0105, -.1135, .007; .1717, .0108, -.057, .0035; .1721, .0109, 0, 0; .1717, .0108, .057, -.0035; .1707, .0105, .1135, -.007; .1691, .01, .1689, -.0102; .1671, .0093, .2231, -.0133; .1648, .0086, .2759, -.0162]`（默认）| 矩阵

轴承转速无关模型的 *X* 方向模态振型矩阵。有关详细信息，请参阅 Bending Model Eigenmodes Method。

该矩阵的维度必须为 *z*-by-*m*，其中：

- *z* 是 **Shaft position [z]** 参数指定向量中的元素数量。
- *m* 是 **Modal frequencies** 参数指定向量中的列数。

模态振型矩阵的形式为 [*U1x*, *U2x*, …, *Umx*]，其中每一列是第 *m* 阶模态在 *X* 方向上的模态振型挠度。该算法基于 **Shaft** 和 **Bending** 设置中的参数计算模态属性。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **X-direction mode shapes [z,m,s]** — 轴承转速相关的 *X* 方向模态振型 *z*-by-*m*-by-*s* 矩阵（默认）| ...

轴承转速相关模型的 *X* 方向模态振型矩阵。默认值为 `cat(3, [.1842, .0134, -.3072, .0272; .1863, .0152, -.2482, .0226; .1882, .0169, -.1878, .0176; .1897, .0182, -.1261, .0121; .1906, .019, -.0634, .0062; .191, .0193, 0, 0; .1906, .019, .0634, -.0062; .1897, .0182, .1261, -.0121; .1882, .0169, .1878, -.0176; .1863, .0152, .2482, -.0226; .1842, .0134, .3072, -.0272], [.1648, .0086, -.2759, .0162; .1671, .0093, -.2231, .0133; .1691, .01, -.1689, .0102; .1707, .0105, -.1135, .007; .1717, .0108, -.057, .0035; .1721, .0109, 0, 0; .1717, .0108, .057, -.0035; .1707, .0105, .1135, -.007; .1691, .01, .1689, -.0102; .1671, .0093, .2231, -.0133; .1648, .0086, .2759, -.0162], [.1291, .0046, -.2166, .0082; .131, .0048, -.1751, .0067; .1327, .005, -.1327, .0051; .1341, .0052, -.0891, .0035; .135, .0053, -.0448, .0017; .1353, .0053, 0, 0; .135, .0053, .0448, -.0017; .1341, .0052, .0891, -.0035; .1327, .005, .1327, -.0051; .131, .0048, .1751, -.0067; .1291, .0046, .2166, -.0082])`有关详细信息，请参阅 Bending Model Eigenmodes Method。

该矩阵的维度必须为 *z*-by-*m*-by-*s*，其中：

- *z* 是 **Shaft position [z]** 参数指定向量中的元素数量。
- *m* 是 **Modal frequencies [z,m]** 参数指定向量中的列数。
- *s* 是 **Bearing speed [s1,…, sS]** 参数指定向量中的元素数量。

模态振型矩阵的形式为 cat(3,[*U1x1*, *U2x1*, …, *Umx1*], …, [*U1xs*, *U2xs*, …, *Umxs*])，其中每一列是第 *m* 阶模态在 *x* 方向上的模态振型挠度。每一页对应于为 **Bearing speed [s1,…, sS]** 参数指定的向量中的一个元素。该算法基于 **Shaft** 和 **Bending** 设置中的参数计算模态属性。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **Y-direction mode shapes [z,m]** — 轴承转速无关的 *Y* 方向模态振型 `[.1193, -.1784, -.1997, -.3348; .1209, -.1933, -.1615, -.2751; .1224, -.2068, -.1223, -.2119; .1235, -.2176, -.0821, -.1445; .1243, -.2245, -.0413, -.0734; .1246, -.2269, 0, 0; .1243, -.2245, .0413, .0734; .1235, -.2176, .0821, .1445; .1224, -.2068, .1223, .2119; .1209, -.1933, .1615, .2751; .1193, -.1784, .1997, .3348]`（默认）| 矩阵

轴承转速无关模型的 *Y* 方向模态振型矩阵。有关详细信息，请参阅 Bending Model Eigenmodes Method。

该矩阵的维度必须为 *z*-by-*m*，其中：

- *z* 是 **Shaft position [z]** 参数指定向量中的元素数量。
- *m* 是 **Modal frequencies** 参数指定向量中的列数。

模态振型矩阵的形式为 [*U1y*, *U2y*, …, *Umy*]，其中每一列是第 *m* 阶模态在 *Y* 方向上的模态振型挠度。该算法基于 **Shaft** 和 **Bending** 设置中的参数计算模态属性。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### **Y-direction mode shapes [z,m,s]** — 轴承转速相关的 *y* 方向模态振型 *z*-by-*m*-by-*s* 矩阵

轴承转速相关模型的 *Y* 方向模态振型矩阵。有关详细信息，请参阅 Bending Model Eigenmodes Method。

该矩阵的维度必须为 *z*-by-*m*-by-*s*，其中：

- *z* 是 **Shaft position [z]** 参数指定向量中的元素数量。
- *m* 是 **Modal frequencies [z,m]** 参数指定向量中的列数。
- *s* 是 **Bearing speed [s1,…, sS]** 参数指定向量中的元素数量。

模态振型矩阵的形式为 cat(3,[*U1y1*, *U2y1*, …, *Umy1*], …, [*U1ys*, *U2ys*, …, *Umys*])，其中每一列是第 *m* 阶模态在 *y* 方向上的模态振型挠度。每一页对应于为 **Bearing speed [s1,…, sS]** 参数指定的向量中的一个元素。默认值为 `cat(3, [.0885, -.1625, -.1475, -.3301; .0895, -.1847, -.1192, -.2745; .0904, -.2048, -.0902, -.2141; .0911, -.2209, -.0606, -.1475; .0916, -.2313, -.0304, -.0754; .0917, -.2349, 0, 0; .0916, -.2313, .0304, .0754; .0911, -.2209, .0606, .1475; .0904, -.2048, .0902, .2141; .0895, -.1847, .1192, .2745; .0885, -.1625, .1475, .3301], [.1193, -.1784, -.1997, -.3348; .1209, -.1933, -.1615, -.2751; .1224, -.2068, -.1223, -.2119; .1235, -.2176, -.0821, -.1445; .1243, -.2245, -.0413, -.0734; .1246, -.2269, 0, 0; .1243, -.2245, .0413, .0734; .1235, -.2176, .0821, .1445; .1224, -.2068, .1223, .2119; .1209, -.1933, .1615, .2751; .1193, -.1784, .1997, .3348], [.1566, -.1901, -.2628, -.3377; .1589, -.1994, -.2125, -.2753; .161, -.2079, -.1609, -.2103; .1627, -.2146, -.1081, -.1424; .1638, -.219, -.0544, -.0719; .1642, -.2205, 0, 0; .1638, -.219, .0544, .0719; .1627, -.2146, .1081, .1424; .161, -.2079, .1609, .2103; .1589, -.1994, .2125, .2753; .1566, -.1901, .2628, .3377])`。

#### 依赖关系

要启用此参数：

- 选择 **Model bending flexibility**。
- 将至少一个安装类型参数设置为 `Speed-dependent bearing matrix`。
- 将 **Bending vibration analysis method** 设置为 `Eigenmodes`。
- 将 **Bending mode determination** 设置为 `User defined`。

### 标称值

### **Bending node displacements (units of m and rad)** — 标称弯曲节点位移 `1`（默认）| 正标量

弯曲节点的位移。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Bending vibration analysis method** 设置为 `Lumped mass`。

### **Bending node velocities (units of m/s and rad/s)** — 标称弯曲节点速度 `1`（默认）| 正标量

弯曲节点的速度。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Bending vibration analysis method** 设置为 `Lumped mass`。

### **Bending mode displacements (units of 1)** — 标称弯曲模态位移 `1`（默认）| 正标量

弯曲模态的位移。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Bending vibration analysis method** 设置为 `Eigenmodes`。

### **Bending mode velocities nominal value (units of 1/s)** — 标称弯曲模态速度 `1`（默认）| 正标量

弯曲模态的速度。

#### 依赖关系

要启用此参数，请选择 **Model bending flexibility**，并将 **Bending vibration analysis method** 设置为 `Eigenmodes`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2011b 中引入**

### R2023a：Model Bending 更新

**Model torsional flexibility** 参数是新增的，并启用新的扭转参数。**Model bending flexibility** 参数取代了之前版本中的 **Model bending** 参数。

可选地，使用 **Enable static unbalances that excite bending** 和 **Enable external forces that excite bending** 参数来包括具有轴转速处谐波频率的静态不平衡和外部力。

当将 **Bending vibration analysis method** 设置为 `Lumped mass` 时，**Nominal Values** 选项卡显示 **Bending node displacements (units of m and rad)** 和 **Bending node velocities (units of m/s and rad/s)** 参数。当将 **Bending vibration analysis method** 设置为 `Eigenmodes` 时，该选项卡显示 **Bending mode displacements (units of 1)** 和 **Bending mode velocities (units of 1/s)** 参数。指定这些标称值可以提高仿真的数值稳健性。

以前，该模块以零弯曲初始化。在 R2023a 中，该模块使用静态不平衡和外部力以静态平衡方式初始化弯曲。

## 描述

具有扭转和弯曲柔性的轴

Flexible Shaft 模块表示具有扭转和弯曲柔性的传动系统轴。该轴由柔性材料组成，它会响应所施加的扭矩而扭转，并响应静态质量不平衡而弯曲。扭转作用会延迟轴端之间的动力传输，从而改变传动系统动态响应。

一端具有连接 B 且另一端具有连接 F 的轴的示意图。

为了表示扭转柔性轴，该模块使用集总质量法。该模型将轴划分为不同的单元，这些单元通过并联弹簧阻尼器系统互连。这些单元提供轴惯量，而弹簧阻尼器系统提供轴柔度。

该模块提供四种参数化方法，允许您对均质轴或轴向非均质轴的柔度进行建模。轴向非均质轴是指以下任一属性沿轴长度变化的轴：

- 扭转刚度
- 扭转惯量
- 弯曲刚度
- 密度
- 剪切模量
- 杨氏模量
- 外径
- 内径

附加参数使您能够对轴端处由于粘性摩擦而在轴承中产生的功率损耗进行建模。有关详细信息，请参阅 Torsion Model。

**注意**

轴端处的粘性摩擦不同于内部材料阻尼，后者对应于轴材料本身产生的损耗。

为了表示弯曲柔性轴，该模块使用集总质量法或特征模态法。虽然集总质量法配置更简单，但特征模态法通常仿真更快。

**提示**

为了优先考虑仿真速度，首先使用集总质量法进行仿真，根据需要调整参数，直到结果与您的数学模型或实验数据匹配。然后，使用特征模态法进行仿真。再次根据需要调整参数，直到结果与数学模型或实验数据匹配。有关使用这两种方法的示例，请参阅 Shaft with Torsional and Transverse Flexibility。

对于集总质量法，弯曲轴单元的数量与扭转轴单元的数量相同。该模型将轴划分为一系列这样的单元。这些单元提供轴惯量，而刚度矩阵提供轴柔度。特征模态法计算表示轴弯曲模态的有效质量-弹簧-阻尼器系统。您可以指定要包含的模态数量以及模态振型的精度。集总质量法和特征模态法都允许您对以下内容建模：

- 激励静态不平衡
- 同心附着的刚性质量
- 沿轴最多四个支撑位置
- 与轴惯量成比例的线性阻尼
- 与轴刚度成比例的线性阻尼

**注意**

特征模态法假设支撑阻尼相对于支撑刚度较小。

静态不平衡会激励弯曲，当轴或附着的刚性质量的质心未与轴主轴线对齐时，就会发生静态不平衡。您可以改变轴上静态不平衡的位置、大小和角度偏移。

您可以将同心附着的刚性质量表示为圆盘或理想化质点。同心圆盘会为轴增加直径转动惯量和极转动惯量，并为轴节点的平移自由度增加质量。该模型假设圆盘很薄，因此轴在带有圆盘的轴向位置两侧仍可弯曲。极转动惯量耦合两个弯曲平面。同心质点是同心圆盘的理想化版本。同心质点会为轴节点的平移自由度增加质量，但没有转动惯量。您可以改变附着在轴上的同心圆盘或质点的位置和惯量。

您可以将支撑建模为理想支撑，或使用刚度和阻尼矩阵建模。对于每个支撑，您可以改变：

- 位置 — 沿轴长度的任意点。
- 类型 — 理想夹紧、理想销、自由、恒定轴承刚度和阻尼，或转速相关刚度和阻尼。
- 数量 — 二、三或四。

对于这两种弯曲方法，您可以通过使用弯曲刚度和线性质量密度，或杨氏模量和轴直径来指定轴弯曲柔度。

您可以通过使用刚度 *k* 和惯量 *J*，或轴的尺寸和材料属性来参数化扭转模型。

### 扭转模型

对于扭转模型，Flexible Shaft block 通过使用集中质量法近似轴的分布连续特性。模型包含有限数量 *N* 个串联的集中惯性阻尼弹簧元件，再加一个末端惯性。结果是 N+1 个惯性组成的一系列，通过 *N* 个旋转弹簧和 *N* 个旋转阻尼器连接。

图示展示柔性轴如何分解为集中参数，并进一步分解为柔性元件的扭转模型等效系统。

该模块将轴视为由 *N* 个柔性元件组成的等效物理网络。每个柔性元件 *FEi* 表示传动轴的一小段，并包含：

- 一个弹簧 *kFE\_i*，用于扭转柔度。网络总共有 *N* 个弹簧。
- 一个阻尼器 *bFE\_i*，用于材料阻尼。网络总共有 *N* 个阻尼器。
- 两个惯性 *IFE\_iC* 和 *IFE\_iR*，用于旋转阻力。相邻柔性元件的惯性合并在一起，因此网络总共有 N+1 个惯性。

对于轴向均匀轴，物理网络中的柔性元件长度、柔度、阻尼和分布惯性相等，因此：

lFE\_1=lFE\_2=⋯=lFE\_N=LN

kFE\_1=kFE\_2=⋯=kFE\_N=k

bFE\_1=bFE\_2=⋯=bFE\_N=b

IFE\_1C=IFE\_1R=IFE\_2C=IFE\_2R=⋯=IFE\_NC=IFE\_NR=I2N

对于轴向非均匀轴，物理网络模型中各个柔性元件的柔度、阻尼以及 **R** 节点和 **C** 节点惯性可以不同。

**节点放置算法**

模型保真度与仿真速度之间的平衡取决于 *N*，即该模块用于表示轴的柔性元件数量。有关平衡仿真速度和模型保真度的信息，请参阅提高仿真速度或精度。

该模块允许您指定最小柔性元件数量 *Nmin*，作为最小柔性元件数参数的值。但是，该模块实际使用的柔性元件数量取决于其所建模轴的复杂度。如果该模块求解包含轴向非均匀性、中间支撑、同心圆盘或质量、静不平衡或外力的模型时需要比您指定的更多的柔性元件，则 N≥Nmin。

例如，假设对于图中的复杂轴，您指定了支撑、静不平衡或外力、较大直径段以及同心圆盘的轴向位置。您将 *Nmin* 的参数设置为 `7`。

带有基座、基座支撑、静不平衡、同心圆盘、从动支撑和从动件标记的柔性轴示意图。这些标记分别对应于位置 Z\_1 到 Z\_7。

如果模型弯曲已打开，则扭转模型柔性元件位置会考虑静不平衡或外力以及同心刚性质量的位置，以使扭转柔性元件与弯曲柔性元件对齐。在仿真期间，扭转模型独立于任何静不平衡、外力或同心刚性质量。

该模块的算法确定求解仿真所需的柔性元件数量以及各个元件的长度：

1. 该模块在轴的基座端和从动端各放置一个节点。这些节点在轴向位置上被视为*固定*，因为它们表示沿轴轴线的物理实体。在图中，固定节点用红色显示。该模块将其他五个 (*Nmin*-2) 内部节点沿轴长度均匀分布。然后在每对相邻节点之间放置一个柔性元件。

   上图进一步分解为各个柔性元件。固定节点为红色。

   对于端部支撑、轴向均匀、无静不平衡、无外力且未附接同心圆盘的轴，根据您指定的其他参数选项和值，该模块可能仅使用 *Nmin* 个等长柔性元件即可求解仿真：

   l=LNmin

   但是，在大多数情况下，该模块只有在添加更多柔性元件后才能求解仿真。
2. 为了添加更多柔性元件，该模块在以下位置放置固定内部节点：

   - 每个轴支撑位置。该模块允许您指定轴支撑的数量和位置。对于图中的轴，支撑位于 *z1* 和 *z6*。
   - 每个静不平衡或外力。对于图中的轴，静不平衡位于 *z2*。
   - 每个刚性质量。刚性质量是同心附接的圆盘或点质量。对于图中的轴，在 *z5* 处有一个表示为圆盘的刚性质量。
   - 每个参数化分段边界。*参数化边界* 是轴向非均匀轴上相邻两段轴的刚度、惯性或几何形状发生变化的位置。该模块允许您定义参数化分段边界位置。对于图中的轴，分段边界位于 *z3* 和 *z4*。

     上述图示的变体，用于说明节点放置。

     请注意，该模块没有在 *z4* 处添加节点，因为在前一步算法中已经添加了一个节点。但是，该节点现在是固定的，因为它表示沿轴长度的一个物理实体。
3. 该模块调整固定节点之间的非固定节点位置，使其均匀分布。

   上述图示的变体，用于说明节点放置。

   最后，该模块在每个节点之间放置柔性元件。每个柔性元件的长度对应于相邻节点之间的中心到中心距离。该模块根据各个元件的长度和相应的轴几何形状在柔性元件之间分配惯性。最终，该复杂轴由 12 个柔性元件表示，其中 l1=z1, l2=l3=(z2−z1)2, l4=l5=(z3−z2)2, l6=l7=(z4−z3)2, l8=l9=(z5−z4)2, l10=l11=(z6−z5)2, 以及 l12=z7−z6。

   上述图示的变体，用于说明节点放置。

   如果 *Nmin* 足够大，使得非固定节点数量大于固定节点数量，则该模块会在每组相邻固定节点之间分布多个非固定节点。

**尺寸和材料属性**

您可以使用刚度 *k* 和极惯性矩 *J*，或使用轴的尺寸和材料属性来参数化扭转模型。

每个元件的刚度和惯性根据轴尺寸和材料属性计算如下：

Jp=π32(D4−d4)

m=π4(D2−d2)ρl

J=m8(D2+d2)=ρl⋅Jp

k=Jp⋅Gl

其中：

- *JP* 是柔性元件位置处轴的极惯性矩。
- *D* 是柔性元件位置处轴的外径。
- *d* 是柔性元件位置处轴的内径。对于实心轴，d=0。对于环形轴，d>0。
- l 是柔性元件长度。
- *m* 是柔性元件位置处轴的质量。
- *J* 是柔性元件位置处轴的惯性矩。
- *ρ* 是轴材料的密度。
- *G* 是轴材料的剪切弹性模量。
- *k* 是柔性元件的旋转刚度。

**内部材料阻尼**

对于任一扭转参数化，内部材料阻尼由阻尼比 *c* 定义，该阻尼比针对具有等效扭转刚度和惯性的单柔性元件模型。阻尼系数则为 2ckωN，其中无阻尼固有频率为 ωN=2kJ。施加在集中质量模型单个柔性元件上的阻尼力矩等于阻尼系数与该柔性元件相对旋转速度的乘积。

### 弯曲模型

**轴几何、支撑载荷和运动**图展示如何测量：

- 静态不平衡偏移角，即静态不平衡绕轴轴线相对于 *x* 轴的角度
- 支撑、刚性质量和静态不平衡相对于轴基端 **B** 的距离
- 段长度的参数化

在图中，轴有三个固定支撑：

1. *B1* — 基端支撑
2. *I1* — 中间支撑
3. *F1* — 从动端支撑

轴具有平移速度 *V*、旋转速度 *W*，并对支撑施加力 *F* 和力矩 *M*。弯曲箭头和符号约定遵循右手定则。模块输出的物理信号符号对应于表示轴作用在支撑上的力、力矩和速度的箭头。

矢量信号为：

- Force, Fr=[FxB1,FyB1,FxI1,FyI1,FxF1,FyF1]
- Moment, M=[MxB1,MyB1,MxI1,MyI1,MxF1,MyF1]
- Translational velocity, V=[VxB1,VyB1,VxI1,VyI1,VxF1,VyF1]
- Rotational velocity, M=[MxB1,MyB1,MxI1,MyI1,MxF1,MyF1]

如果轴有两个支撑，则每个矢量信号长度为四。例如，Force 为 Fr=[FxB1,FyB1,FxF1,FyF1]。

如果轴有四个支撑，则每个矢量信号长度为八。例如，Force 为 Fr=[FxB1,FyB1,FxI1,FyI1,FxI2,FyI2,FxF1,FyF1]。

**轴几何、支撑载荷和运动**

三维空间中的轴坐标示意图。

**弯曲模型集总质量法**

与扭转模型一样，弯曲模型的集总质量法将轴的分布连续特性离散为有限数量 *N* 个柔性单元。这 *N* 个柔性单元对应于 N+1 个集总惯量，通过阻尼和弹簧单元串联连接。然而，对于弯曲模型，每个质量有四个自由度：沿垂直于轴轴线的 *x* 和 *y* 方向的平移和旋转。

弯曲模型集总质量离散化示意图。

集总质量运动方程 [1] 为

Mx→¨+(B+GDiskΩ)x→˙+(K+GDiskΩ˙)x→=f→.

其中：

- ***M*** 是表示轴质量的 4(N+1)×4(N+1) 矩阵。
- ***B*** 是内部阻尼和支撑阻尼的 4(N+1)×4(N+1) 矩阵。
- ***G**Disk* 是考虑圆盘陀螺效应的 4(N+1)×4(N+1) 矩阵。
- Ω 是仿真期间的轴扭转速度。
- ***K*** 是弹簧刚度的 4(N+1)×4(N+1) 矩阵。
- x→ 是表示所有节点自由度的 4(N+1)×1 矢量。
- f→ 是表示由于施加静态质量不平衡而产生的外部力的 4(N+1)×1 矢量。

质量矩阵的方程 [5] 为

M=M1/2+M2/3+…Mi/i+1+…MN/N+1 + ∑​Mdisk, i,

其中：

- Mi/(i+1) 是单个柔性单元的质量矩阵。对于每个柔性单元，一半的质量和转动惯量被传递到柔性单元两端的节点。Mi/(i+1) 矩阵在 (4i−3):(4i+4) 行和 (4i−3):(4i+4) 列中具有非零元素：

  Mi/(i+1)= [0⋱12m0000000012m00000000Id00000000Id0000000012m0000000012m00000000Id00000000Id⋱0],

  其中：

  - l 是内部节点之间沿轴的柔性单元长度。为确定每个柔性单元的长度，模块使用 Node Placement Algorithm 中描述的算法。每个柔性单元包含两个惯量。每个惯量有两个平移自由度、两个旋转自由度和一个刚度矩阵。

    在 *XZ* 平面中弯曲的等效物理模型（梁沿 *X* 方向平移并绕 *Y* 轴旋转）以及在 *YZ* 平面中弯曲的物理模型（梁沿 Y 方向平移并绕 X 轴旋转）中，每个柔性单元随后包含两个质量、两个惯量和一个刚度矩阵。

    刚度矩阵将一侧的质量和惯量与另一侧分开。

    为确定内部节点位置，并因此确定柔性单元的数量和长度，模块使用与扭转模型相同的节点布置算法。有关详细信息，请参阅 Node Placement Algorithm。
  - *m* 是柔性单元质量。*m* 取决于外径 *D*、内径 *d*、轴的密度 *ρ* 以及柔性单元长度，使得 m= (π4)(D2−d2)ρl。
  - *Id*，即绕垂直于轴轴线的轴线的半单元质量转动惯量，取决于质量 *m*、长度 l 和柔性单元的扭转转动惯量 *J*，使得 Id=J4+m6(l2)2。
- ∑​Mdisk, i 是同心附接到轴的刚性质量的求和质量矩阵。
- 同心附接到轴的每个刚性质量的质量属性被添加到最近的节点 i，使得

  Mdisk, i([(4i-3):4i],[(4i-3):4i])=[Mdisk, i0000Mdisk, i0000ID,disk, i0000ID,disk, i],

  其中 *ID,disk,i* 是附接到第 *i* 个节点的刚性圆盘绕垂直于轴的轴线的质量直径转动惯量。模型假设圆盘很薄，因此轴仍可在圆盘轴向位置的两侧弯曲。同心点质量有 ID,disk, i= 0。

阻尼矩阵的方程为

B= αM +βK+Bsupport,

其中：

- *α* 是与质量成比例的阻尼常数。
- *β* 是与刚度成比例的阻尼常数。
- ***B**support* 是每个支撑处的阻尼系数。对于第 *i* 个节点处的支撑，用全局坐标表示的阻尼矩阵为

  Bsupport([(4i − 3) : 4i], [(4i − 3) : 4i])= [bxxbxy00byxbyy0000bθθ0000bφφ],

  其中：

  - [bxx bxy byx byy] 是支撑平移阻尼。
  - [bθθ bφφ] 是支撑旋转阻尼。
- Gdisk, i 考虑任何同心附接圆盘的陀螺效应，定义为

  Gdisk, i([(4i−3):4i],[(4i−3):4i])=[00000000000ΩIP,disk, i00−ΩIP,disk, i0],

  其中 *IP,disk,i* 是附接到第 *i* 个节点的圆盘绕轴轴线的质量极转动惯量。同心点质量的质量极转动惯量为 IP,disk, i= 0。

轴承刚度矩阵的方程为

K =K1/2 + K2/3 + ...+KN/N+1 + ∑​Ksupport,

其中：

- Ki/i+1 是单个轴柔性单元的刚度矩阵。第 i 个轴柔性单元（在第 *i* 个和第 (i+1) 个节点之间）的刚度矩阵在 (4i−3):(4i+4) 行和 (4i−3):(4i+4) 列中具有非零元素，使得

  Ki/i+1=2EIl3 [0⋱6003l−6003l06−3l00−6−3l00−3l2l2003ll203l002l2−3l00l2−600−3l600−3l0−63l0063l00−3ll2003l2l203l00l2−3l002l2⋱0],

  其中：

  - l 是柔性单元长度。
  - *EI* 是轴刚度。
- ***K**support* 是每个支撑处的刚度。对于第 *i* 个节点处的支撑，用全局坐标表示的刚度矩阵为

  Ksupport([(4i − 3) : 4i], [(4i − 3) : 4i])= [kxxkxy00kyxkyy0000kθθ0000kφφ],

  其中：

  - [kxx kxy kyx kyy] 是支撑平移刚度。
  - [kθθ kφφ] 是支撑旋转刚度。

仅当为支撑选择 `Bearing matrix` 或 `Speed-dependent bearing matrix` 时，支撑刚度矩阵 *Ksupport* 才非零。如果选择 `Clamped` 安装类型，则将零旋转和零平移的运动学条件应用于对应于支撑节点（*B1*、*I1*、*I2* 或 *F1*）的自由度。如果选择 `Pinned` 安装类型，则将零平移的运动学条件应用于对应于支撑节点（*B1*、*I1*、*I2* 或 *F1*）的平移自由度。

该表包含应用于带支撑的集总质量节点的边界条件。

| 支撑类型 | 集总质量方程的边界条件 |
| --- | --- |
| `Clamped` | xi= 0,   yi= 0,   θi= 0,    φi= 0 |
| `Pinned` | xi= 0,   yi= 0 |
| `Bearing Matrix` | *Ksupport* 是非平凡的。 |
| `Speed-dependent bearing matrix` | *Ksupport* 是非平凡的，并且取决于轴旋转速度。在每个时间步，*KSupport* 计算为：<br>KSupport(Ω)=lookup( |ΩRef|,  KSupport, Ref,  Ω,  interpolation=linear,  extrapolation=nearest),<br>其中：<br>- ΩRef 是轴承速度，如 **Supports** 设置中所指定，用于 **Bearing speed [s1,...,sS]** 参数。<br>- 对于每个支撑，*KSupport,Ref* 是取决于轴承速度的平移刚度，您在 **Supports** 设置中指定。<br>- 查找表对轴旋转速度使用线性插值和最近邻外插。 |

表示所有节点自由度的矩阵 x→ 计算如下：第 *i* 个和第 (i+1) 个节点的自由度为

x→=[⋮xiyiθiφixi+1yi+1θi+1φi+1⋮].

由于每个静态质量不平衡产生的外部力被施加到最近的节点。第 ith 个节点处的激励为

f→4(i−1:i−2)= [mεj,offset(Ω2icos(φshaft,i+φoffset, j) +∂Ωi∂t sin(φshaft, i+φoffset, j) )mεj,offset(Ω2isin(φshaft,i+φoffset, j) −∂Ωi∂t  cos(φshaft, i+φoffset, j) )],

其中：

- *mεj* 是第 *j* 个静态不平衡，位于第 *i* 个节点。
- Ωi 是仿真期间第 *i* 个节点的轴旋转速度。
- *φshaft, i* 是第 *i* 个节点的扭转集总质量旋转角。

当模块对以旋转速度的倍数或分数激励轴的外部力进行建模时：

f→4(i−1:i−2)= [Fmag,jcos(pϕshaft,j+ϕfoffset,j)Fmag,jcos(pϕshaft,j+ϕfoffset,j)],

其中：

- *Fmag,j* 是 **External force magnitudes vector** 参数的第 *j* 个元素。
- *p* 是 **External force frequency harmonic of rotor speed vector** 参数的第 *j* 个元素。
- *ϕfoffset* 是 **External force offset angles vector** 参数的第 *j* 个元素。

  节点索引 *i* 是力的 *z* 轴向位置处的节点。

**弯曲模型特征模态法**

对于特征模态法，模块将弯曲动力学从弯曲模型集总质量法提供的 4(N+1) 个自由度降为 *M* 个自由度，其中 *M* 是模态数。

模块在模型编译期间计算轴弯曲模态属性，然后在模型仿真期间求解模态质量-弹簧-阻尼器系统。

减少模型动力学中的自由度并将计算分为编译时和运行时任务可提高仿真性能。特征模态法假设模态形状不受阻尼影响。因此，该方法最适合包含有限圆盘陀螺和支撑阻尼的模型。

在编译期间，模块使用以下步骤计算近似阻尼特征模态：

1. 模块使用与弯曲模型集总质量法相同的集总质量运动方程计算矩阵：

   Mx→¨+(B+GDiskΩ)x→˙+(K+GDiskΩ˙)x→=f→.

   有关详细信息，请参阅弯曲模型集总质量法。

   在确定 x→ 的节点轴向位置时，模块使用用于扭转模型和弯曲模型集总质量法的 Node Placement Algorithm 的两种变体之一。模块使用的变体取决于在 **Advanced Bending** 设置中，**Bending mode determination** 参数设置为 `Simscape determined` 还是 `User defined`。

   如果 **Bending mode determination** 参数设置为 `Simscape determined`，则特征模态法不是像集总质量法那样使用 **Minimum number of flexible elements** 参数作为 *Nmin*，而是计算 *Nmin* 为

   NMin, Eig= round(Ldz),

   其中：

   - *L* 是 **Shaft length** 参数的指定值。
   - *dz* 是 **Shaft length increments for mode shape computations** 参数的指定值。

   为计算 *m* 个无阻尼特征模态和特征频率，模块使用 `eigs` 函数。方程形式为：

   [HRight, λ] = eigs( sparse(K), sparse(M), mMax, 'smallestabs’ )
   [HLeft, λ] = eigs( sparse(K), sparse(M), mMax, 'smallestabs’ )

   其中：

   - `HRight` 是 4(N+1)×M 右特征矢量矩阵。每一列是 x→ 坐标中的右特征模态。
   - `HLeft` 是 4(N+1)×M 左特征矢量矩阵。每一列是 x→ 坐标中的左特征模态。
   - `λ` 表示特征值，即特征频率的平方。
   - *mMax* 是 **Limit number of modes** 参数。

   计算的特征模态数 *m* 在以下情况下小于 *mMax*：

   - 存在特征频率超过 **Eigenfrequency upper limit** 参数指定值的模态。模块会丢弃这些模态。
   - 特征值不收敛。有关详细信息，请参阅 `eigs`。

   如果将 **Bending mode determination** 设置为 `User defined`，则模块为以下参数计算特征矢量矩阵 ***H***：

   - **X-direction mode shapes**
   - **Y-direction mode shapes**
   - **Shaft position**

   为确定 x→ 的节点轴向位置，模块使用为 **Shaft position** 参数指定的元素作为主节点。

   为计算每个节点的模态旋转 θ 和 φ，模块使用 `gradient` 函数。方程形式为：

   θ = -gradient(Y direction mode shapes)
   φ = gradient(X direction mode shapes)

   模块将 **X-direction mode shapes** 参数、**Y-direction mode shapes** 参数以及模态旋转 θ 和 φ 的值组装到 *HLeft* 和 *HRight* 每一列的 x→ 坐标中。
2. 模块计算模态矩阵 ***M**Modal*、***K**Modal*、***B**Modal*、***G**Modal* 和 *fModal* 为：

   MModal= HLeftTMHRight

   KModal = HLeftTKHRight

   BModal = HLeftTBHRight

   GModal = HLeftTGDiskHRight

   f→Modal = HLeftTf→

   尽管模块在步骤 1 中计算无阻尼特征模态 ***H***，但模态阻尼矩阵 ***B**Modal* 和模态陀螺矩阵 ***G**Modal* 可以对轻阻尼建模。模块对矩阵进行归一化，使 ***M**Modal* 为单位矩阵。

在仿真期间，模块仿真特征模态运动方程：

MModalη→¨+(BModal+GModalΩ)η→˙+(KModal+GModalΩ˙)η→ = f→Modal,

其中模态自由度 η→ 与节点自由度的关系为：

x→=HRightη→

**速度相关特征模态法**

如果在 **Supports** 设置中，任何支撑的安装类型参数设置为 `Speed-dependent bearing matrix`，则支撑刚度和支撑阻尼会变化。速度相关特征模态模型通过随轴速度变化改变模态属性 *HRight* 和 *HLeft*、***B**Modal*、***G**Modal*、***K**Modal* 和 *fModal* 来考虑这些效应。***M**Modal* 对所有轴速度都归一化为单位矩阵，因此它不取决于轴速度。

如果轴具有速度相关轴承支撑，则模块对轴速度矢量中的每个元素重复弯曲模型特征模态法步骤。轴矢量元素是 **Supports** 设置中为 **Bearing speed [s1,...,sS]** 参数指定的值。在仿真期间，模态刚度、阻尼和激励幅值根据属性与轴速度的查找表进行调整。

也就是说，模块将特征模态运动方程仿真为：

MModalη→¨+ (BModal(Ω)+GModal(Ω)Ω)η→˙+ (KModal(Ω)+GModal(Ω)Ω˙)η→ = f→Modal(Ω),

其中 ***K**Modal*、***B**Modal* 和 *fModal* 的形式为：

KModal(Ω)=lookup( |ΩRef|,  KModal, Ref,  Ω,  interpolation=linear,  extrapolation=nearest) ,

BModal(Ω)=lookup( |ΩRef|,  BModal, Ref,  Ω,  interpolation=linear,  extrapolation=nearest) ,

GModal(Ω)=lookup( |ΩRef|,  GModal, Ref,  Ω,  interpolation=linear,  extrapolation=nearest) ,

f→Modal(Ω)=lookup( |ΩRef|,  f→Modal, Ref,  Ω,  interpolation=linear,  extrapolation=nearest) ,

其中：

- ΩRef 是在
  **Supports** 设置中，为
  **Bearing speed [s1,...,sS]** 参数指定的值。
- ***K**Modal,Ref* 是每个
  ΩRef 处的模态刚度表。
- *BModal,Ref* 是每个 ΩRef 处的支承阻尼表。
- *GModal,Ref* 是每个 ΩRef 处的圆盘陀螺阻尼表。
- ***f**Modal,Ref* 是每个 ΩRef 处的模态激励表。

该模块关联不同 ΩRef 值下的模态振型相似性，并在必要时重新排序模态，使每个模态自由度 η→ 的属性随轴转速逐渐变化。

### 提高仿真速度或精度

仿真精度与性能之间的平衡取决于 *N*，即模块用于表示轴的柔性单元数量。仿真精度衡量仿真结果与数学及经验模型的一致程度。通常，随着 *N* 增加，模型保真度和仿真精度也提高。但是，仿真的计算成本也与 *N* 相关，并且随着计算成本增加，性能下降。相反，随着 *N* 减小，仿真速度提高，但仿真精度下降。

对于扭转或弯曲模型的集中质量法，要提高仿真精度，请增加最小柔性单元数 *Nmin*。单柔性单元扭转模型表现出的扭转特征频率接近连续分布参数模型的第一特征频率。为了获得更高精度，可以选择 2、4、8 个或更多柔性单元。例如，16 柔性单元模型分别以 0.1、1.9、1.6 和 5.3 percent 的精度表示最低的四个扭转特征频率。

对于弯曲模型的特征模态法，要提高仿真精度：

- 如果使用特征模态对旋转速度的静态依赖性进行仿真，请验证 **Nominal shaft speed for bending modes** 参数接近仿真轴转速。如果将连接到轴的刚性圆盘参数化为绕轴轴线具有较大质量惯性矩，或指定任何速度相关的轴承矩阵支承，则此参数可能影响模型结果。
- 如果使用特征模态对旋转速度的动态依赖性进行仿真，请验证在 **Supports** 设置中为 **Bearing speed [s1,...,sS]** 指定的值覆盖仿真的轴转速范围，或者在超出该范围的轴转速下支承刚度和阻尼的饱和是可接受的近似。
- 在 **Advanced Bending** 设置中，减小 **Shaft length increments for mode shape computations** 参数的值。减小该值可以提高模态频率和振型的精度。
- 减小支承阻尼和绕轴轴线的圆盘极惯性矩。Simscape™ 在仿真前对模态振型和频率的计算未考虑该阻尼。
- 通过在 Shaft with Torsional and Transverse Flexibility 示例中的柔性轴模型中使用您的参数，检查对 **Advanced Bending** 设置的敏感度。调整这些参数，并使用示例中提供的链接来检查这些值如何影响特征模态频率和振型。相应地调整模型中的参数值。
- 增加 **Eigenfrequency upper limit** 和 **Limit number of modes** 参数的值。仿真中的最高模态频率必须显著大于轴旋转频率。

### 假设和限制

- 连续扭转轴的分布参数模型通过有限数量 *N* 的集中质量近似。
- 轴旋转和扭转柔性会激发轴弯曲，但弯曲不影响轴旋转和扭转柔性。
- 连接到轴的刚性点质量或圆盘在平行于轴轴线方向上的长度很小。
- 对于特征模态弯曲模型，阻尼不影响特征频率。
- 轴弯曲不会在 Flexible Shaft 模块之间传递。
- 相对于轴长度，轴外径较小。
- 相对于轴长度，弯曲挠度较小。
- 静态质量不平衡是唯一的外部轴弯曲激励载荷。
- 轴支承是固定的。
- 考虑刚性圆盘的陀螺效应；忽略轴本身的陀螺效应。
- 特征模态法中的静态质量不平衡激励使用轴中点处的旋转速度。
- 如果轴仅对扭转建模并使用参数化选项 **By stiffness and inertia** 或 **By segment stiffness and inertia**，则该模块仅使用两个支承，分别在 **B** 和 **F** 端各一个。
