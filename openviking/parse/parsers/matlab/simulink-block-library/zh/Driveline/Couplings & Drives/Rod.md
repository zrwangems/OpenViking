---
type: simulink-block
title: 'Rod'
family: 'couplings-drives'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'rod'
documentation_source_path: 'ref/rod.html'
language: zh-CN
chinese_source: worker-translation
---

# Rod

## 端口

### 守恒

### **B** — 基座平动机械

与杆基座或输入关联的平动守恒端口。

### **F** — 从动件平动机械

与杆从动件或输出关联的平动守恒端口。

## 参数

### Rod

该表显示某些 **Rod** 参数的可见性如何取决于您为其他 **Rod** 参数所做的选择。

**Rod 参数依赖关系表**

| **Rod** | | |
| --- | --- | --- |
| **Parameterization** | | |
| `By stiffness and inertia` | `By material and geometry` | |
| **Stiffness** | **Geometry** | |
| **Mass** | `Solid` | `Annular` |
| **Length** | |
| **Outer diameter** | |
| - | **Inner diameter** |
| **Density** | |
| **Young's modulus** | |
| **Damping ratio** | | |
| **Number of flexible elements** | | |

### **Parameterization** — 参数化方法 `By stiffness and inertia` (default) | `By material and geometry`

参数化方法。

每个 **Parameterization** 选项会显示其他参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Stiffness** — 材料刚度 `5e8` `N/m` (default) | 非负标量

材料刚度。

将 **Parameterization** 参数设置为 `By stiffness and inertia` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Mass** — 杆质量 `20` `kg` (default) | 正标量

杆质量。

#### 依赖关系

将 **Parameterization** 参数设置为 `By stiffness and inertia` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Geometry** — 杆横截面 `Solid` (default) | `Annular`

杆横截面几何形状。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会显示此参数。每个 **Geometry** 选项会显示其他参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Length** — 杆长度 `1` `m` (default) | 正标量

杆长度。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Outer diameter** — 杆外径 `0.075` `m` (default) | 正标量

杆外径。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Inner diameter** — 杆内径 `0.050` `m` (default) | 正标量

杆内径。如果杆为实心，请指定 `0`。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry`，并将 **Geometry** 参数设置为 `Annular` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Density** — 材料密度 `7.8e3` `kg/m^3` (default) | 正标量

材料密度。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Young's modulus** — 杨氏模量 `200e9` `Pa` (default) | 正标量

杆材料的杨氏模量。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会显示此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Damping ratio** — 材料阻尼比 `0.01` (default) | 非负标量

材料阻尼比。

### **Number of flexible elements** — *N* `1` (default) | 正整数标量

用于近似的柔性单元数 *N*。

柔性单元数 *N* 越大，模型精度越高，但会降低仿真性能，即仿真速度。单个柔性单元模型的特征频率接近连续分布参数模型的第一特征频率。

如果精度比性能更重要，请选择 2、4、8 个或更多柔性单元。例如，16 单元模型分别以 0.1、1.9、1.6 和 5.3 percent 的精度表示四个最低特征频率。

### 粘性损耗

### **Viscous friction coefficients at base (B) and follower (F)** — 粘性摩擦系数 `[0, 0]` `N/(m/s)` (default) | 非负向量

基座端口 **B** 和从动端口 **F** 处的粘性摩擦系数。

### 初始条件

### **Initial deflection** — 初始挠度 `0` `m` (default) | 非负标量

仿真开始时杆的挠度。

正初始挠度会导致杆的基座端 **B** 相对于杆的从动端 **F** 产生正平移。

### **Initial velocity** — 初始速度 `0` `m/s` (default) | 非负标量

仿真开始时，杆的基座端 **B** 相对于杆的从动端 **F** 的纵向速度。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

轴向柔性杆或缆索

Rod 模块表示受拉伸或压缩的轴向柔性杆或缆索。

### 模型

为了表示杆或缆索，该模块使用集总参数模型。该模型由 *N*+1 个集总质量组成，这些质量通过 *N* 组并联的弹簧和阻尼器回路串联连接。弹簧表示弹性。阻尼器表示材料阻尼。

单个柔性单元模型的特征频率接近分布参数模型的第一特征频率。要进行更准确的分析，请选择 2、4、8 个或更多柔性单元。

等效物理网络包含 *N* 个弹簧和阻尼器回路以及 *N*+1 个质量块。杆的总质量均匀分布在这些质量块上。每个弹簧和阻尼器回路中弹簧的刚度等于杆材料刚度的 *N* 倍。

### 方程

模型的定义方程为：

η=2ζK⋅m2

A=π(D2−d2)4

K=E⋅AL

m=A⋅L⋅ρ

其中：

- *η* 是杆的阻尼。
- *ς* 是杆材料的阻尼比。
- *K* 是杆的刚度。
- *A* 是杆的横截面积。
- *D* 是杆的外径。
- *d* 是杆的内径，其中

  - *d* = 0 对于实心杆。
  - *d* > 0 对于环形（即空心）杆。
- *E* 是杆材料的 Young's modulus，即弹性模量。
- *L* 是杆的长度。
- *m* 是杆的质量。
- *ρ* 是杆材料的密度。

### 假设和限制

- 在受拉时，对于杆而言，杆不会屈曲；对于缆索而言，缆索不会松弛。
- 杆沿其长度具有恒定横截面。
- 分布参数模型近似为有限数量的柔性单元 *N*。
