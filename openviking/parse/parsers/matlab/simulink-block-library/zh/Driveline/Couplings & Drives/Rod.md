---
type: simulink-block
title: 'Rod'
family: 'sdl'
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
```yaml
ports:
- name: B
  summary: 基座平移机械
  direction: unspecified
- name: F
  summary: 从动平移机械
  direction: unspecified
```

### 守恒

### **B** — 基座平移机械

与杆基座或输入关联的平移守恒端口。

### **F** — 从动平移机械

与杆从动件或输出关联的平移守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 参数化方法 By stiffness and inertia（默认）| By material and geometry
  group: Rod
- name: Stiffness
  summary: 材料刚度 5e8 N/m（默认）| 非负标量
  group: Rod
- name: Mass
  summary: 杆质量 20 kg（默认）| 正标量
  group: Rod
- name: Geometry
  summary: 杆横截面 Solid（默认）| Annular
  group: Rod
- name: Length
  summary: 杆长度 1 m（默认）| 正标量
  group: Rod
- name: Outer diameter
  summary: 杆外径 0.075 m（默认）| 正标量
  group: Rod
- name: Inner diameter
  summary: 杆内径 0.050 m（默认）| 正标量
  group: Rod
- name: Density
  summary: 材料密度 7.8e3 kg/m^3（默认）| 正标量
  group: Rod
- name: Young's modulus
  summary: 杨氏模量 200e9 Pa（默认）| 正标量
  group: Rod
- name: Damping ratio
  summary: 材料阻尼比 0.01（默认）| 非负标量
  group: Rod
- name: Number of flexible elements
  summary: '*N* 1（默认）| 正整数标量'
  group: Rod
- name: Viscous friction coefficients at base (B) and follower (F)
  summary: 粘性摩擦系数 [0, 0] N/(m/s)（默认）| 非负向量
  group: 粘性损耗
- name: Initial deflection
  summary: 初始挠度 0 m（默认）| 非负标量
  group: 初始条件
- name: Initial velocity
  summary: 初始速度 0 m/s（默认）| 非负标量
  group: 初始条件
```

### Rod

下表显示了某些 **Rod** 参数的可见性如何取决于您为其他 **Rod** 参数所做的选择。

**Rod 参数依赖关系表**

| **Rod** | | |
| --- | --- | --- |
| **参数化** | | |
| `By stiffness and inertia` | `By material and geometry` | |
| **刚度** | **几何** | |
| **质量** | `Solid` | `Annular` |
| **长度** | |
| **外径** | |
| - | **内径** |
| **密度** | |
| **杨氏模量** | |
| **阻尼比** | | |
| **柔性单元数** | | |

### **Parameterization** — 参数化方法 `By stiffness and inertia`（默认）| `By material and geometry`

参数化方法。

每个 **Parameterization** 选项会公开其他参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Stiffness** — 材料刚度 `5e8` `N/m`（默认）| 非负标量

材料刚度。

将 **Parameterization** 参数设置为 `By stiffness and inertia` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Mass** — 杆质量 `20` `kg`（默认）| 正标量

杆质量。

#### 依赖关系

将 **Parameterization** 参数设置为 `By stiffness and inertia` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Geometry** — 杆横截面 `Solid`（默认）| `Annular`

杆横截面几何。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会公开此参数。每个 **Geometry** 选项会公开其他参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Length** — 杆长度 `1` `m`（默认）| 正标量

杆长度。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Outer diameter** — 杆外径 `0.075` `m`（默认）| 正标量

杆外径。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Inner diameter** — 杆内径 `0.050` `m`（默认）| 正标量

杆内径。如果杆为实心，请指定 `0`。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 并将 **Geometry** 参数设置为 `Annular` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Density** — 材料密度 `7.8e3` `kg/m^3`（默认）| 正标量

材料密度。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Young's modulus** — 杨氏模量 `200e9` `Pa`（默认）| 正标量

杆材料的杨氏模量。

#### 依赖关系

将 **Parameterization** 参数设置为 `By material and geometry` 会公开此参数。有关详细信息，请参阅 Rod 参数依赖关系表。

### **Damping ratio** — 材料阻尼比 `0.01`（默认）| 非负标量

材料阻尼比。

### **Number of flexible elements** — *N* `1`（默认）| 正整数标量

用于近似的柔性单元数 *N*。

柔性单元数 *N* 越大，模型的精度越高，但会降低仿真性能，即仿真速度。单单元模型（*N*=1）的特征频率接近连续分布参数模型的第一特征频率。

如果精度比性能更重要，请选择 2、4、8 或更多柔性单元。例如，16 单元模型对最低四个特征频率的表示精度分别为 0.1、1.9、1.6 和 5.3 个百分点。

### 粘性损耗

### **Viscous friction coefficients at base (B) and follower (F)** — 粘性摩擦系数 `[0, 0]` `N/(m/s)`（默认）| 非负向量

基座端口 **B** 和从动端口 **F** 处的粘性摩擦系数。

### 初始条件

### **Initial deflection** — 初始挠度 `0` `m`（默认）| 非负标量

仿真开始时杆的挠度。

正初始挠度导致杆的基座 **B** 端相对于杆的从动件 **F** 端产生正平移。

### **Initial velocity** — 初始速度 `0` `m/s`（默认）| 非负标量

仿真开始时杆的基座 **B** 端相对于杆的从动件 **F** 端的纵向速度。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

轴向柔性杆或缆索

Rod 模块表示处于拉伸或压缩状态的轴向柔性杆或缆索。

### 模型

为了表示杆或缆索，该模块使用集总参数模型。该模型由 *N*+1 个集总质量组成，这些质量通过 *N* 组并联的弹簧和阻尼器电路串联连接。弹簧表示弹性。阻尼器表示材料阻尼。

单柔性单元模型的特征频率接近分布参数模型的第一特征频率。为了进行更准确的分析，请选择 2、4、8 或更多柔性单元。

等效物理网络包含 *N* 个弹簧和阻尼器电路以及 *N*+1 个质量块。杆的总质量均匀分布在质量块上。每个弹簧和阻尼器电路中弹簧的刚度等于杆材料刚度的 *N* 倍。

### 方程

该模型的定义方程为：

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

  - 对于实心杆，*d* = 0。
  - 对于环形（即空心）杆，*d* > 0。
- *E* 是杆材料的杨氏模量，即弹性模量。
- *L* 是杆的长度。
- *m* 是杆的质量。
- *ρ* 是杆材料的密度。

### 假设和限制

- 对于杆，在拉伸时不会屈曲；对于缆索，在拉伸时不会松弛。
- 杆沿其长度具有恒定横截面。
- 分布参数模型近似为有限数量的柔性单元 *N*。
