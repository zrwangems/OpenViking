---
type: simulink-block
title: 'Beamscan Spectrum'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'beamscanspectrum'
documentation_source_path: 'ref/beamscanspectrum.html'
language: zh-CN
chinese_source: worker-translation
---

# Beamscan Spectrum

## 端口
```yaml
ports:
- name: X
  summary: 接收信号 *M*×*N* 复值矩阵
  direction: input
  data_types: double
- name: Y
  summary: Beamscan 二维空间谱 非负实值 *P*×*Q* 矩阵
  direction: output
  data_types: double
- name: Ang
  summary: 到达方向 非负实值 2×*L* 矩阵
  direction: output
  data_types: double
```

### 输入

### **X** — 接收信号 *M*×*N* 复值矩阵

接收信号，指定为 *M*×*N* 复值矩阵。量 *M* 是信号的长度，即信号中包含的采样值数量。量 *N* 是阵列中传感器元件的数量。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
### 输出

### **Y** — Beamscan 二维空间谱 非负实值 *P*×*Q* 矩阵

估计的二维空间谱的幅度，返回为非负实值 *P*×*Q* 矩阵。每个条目表示估计的 MUSIC 空间谱的幅度。每个条目对应于由 **Azimuth scan angles (deg)** 和 **Elevation scan angles (deg)** 参数指定的角度。*P* 等于 **Azimuth scan angles (deg)** 中指定的向量长度，*Q* 等于 **Elevation scan angles (deg)** 中指定的向量长度。

**数据类型：** `double`

### **Ang** — 到达方向 非负实值 2×*L* 矩阵

信号的到达方向，返回为实值 2×*L* 矩阵。*L* 是由 **Number of signals** 参数指定的信号数量。到达方向角由源相对于阵列局部坐标系的方位角和仰角定义。矩阵的第一行包含方位角，第二行包含仰角。如果对象无法识别频谱中的峰值，将返回 `NaN`。角度单位为度。

#### 依赖关系

要启用此输出端口，请选中 **Enable DOA output** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Signal propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 实值正标量
  group: ''
- name: Operating frequency (Hz)
  summary: 系统工作频率 3e8（默认）| 正实标量
  group: ''
- name: Number of bits in phase shifters
  summary: 移相器相位量化位数 0（默认）| 非负整数
  group: ''
- name: Forward-backward averaging
  summary: 启用前向-后向平均 off（默认）| on
  group: ''
- name: Azimuth scan angles (deg)
  summary: 方位方向的扫描角度 -180:180（默认）| 实值向量
  group: ''
- name: Elevation scan angles (deg)
  summary: 仰角方向的扫描角度 -90:90（默认）| 实值向量
  group: ''
- name: Enable DOA output
  summary: 通过输出端口输出到达方向 off（默认）| on
  group: ''
- name: Number of signals
  summary: 预期到达信号数 1（默认）| 正整数
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
- name: Specify sensor array as
  summary: 指定阵列的方法 Array (no subarrays)（默认）| MATLAB expression
  group: ''
- name: Expression
  summary: 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object
  group: ''
- name: Geometry
  summary: 阵列几何结构 ULA（默认）| URA | UCA | Conformal Array
  group: ''
- name: Number of elements
  summary: 阵列阵元数 ULA 阵列为 2，UCA 阵列为 5（默认）| 大于或等于 2 的整数
  group: ''
- name: Element spacing (m)
  summary: 阵列元素间距，ULA 阵列为 0.5，URA 阵列为 [0.5,0.5]（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量
  group: ''
- name: Array axis
  summary: ULA 的线性轴方向 y（默认）| x | z
  group: ''
- name: Array size
  summary: URA 阵列的维度 [2,2]（默认）| 正整数 | 1×2 正整数向量
  group: ''
- name: Element lattice
  summary: URA 元素位置的晶格 Rectangular（默认）| Triangular
  group: ''
- name: Array normal
  summary: 阵列法线方向，URA 阵列为 x，UCA 阵列为 z（默认）| y
  group: ''
- name: Radius of UCA (m)
  summary: UCA 阵列半径 0.5（默认）| 正标量
  group: ''
- name: Element positions (m)
  summary: 共形阵列元素的位置 [0;0;0]（默认）| 3×*N* 实数值矩阵
  group: ''
- name: Element normals (deg)
  summary: 共形阵列单元法向量方向 [0;0] | 2×1 列向量 | 2×*N* 矩阵
  group: ''
- name: Taper
  summary: 阵列单元锥削 1（默认）| 复标量 | 复值行向量
  group: ''
```

### **Signal propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。单位为米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **Operating frequency (Hz)** — 系统工作频率 `3e8`（默认）| 正实标量

系统工作频率，指定为正标量。单位为 Hz。

### **Number of bits in phase shifters** — 移相器相位量化位数 `0`（默认）| 非负整数

用于量化波束形成器或导向矢量权重的相移分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **Forward-backward averaging** — 启用前向-后向平均 off（默认）| on

选择此参数以使用前向-后向平均来估计具有共轭对称阵列流形结构的传感器阵列的协方差矩阵。

### **Azimuth scan angles (deg)** — 方位方向的扫描角度 `-180:180`（默认）| 实值向量

方位方向的扫描角度，指定为实值向量。角度必须介于 –180° 和 180° 之间（含端点）。必须以升序指定角度。单位为度。

**数据类型：** `double`

### **Elevation scan angles (deg)** — 仰角方向的扫描角度 `-90:90`（默认）| 实值向量

仰角方向的扫描角度，指定为实值向量。角度必须介于 –90° 和 90° 之间（含端点）。必须以升序指定角度。单位为度。

**数据类型：** `double`

### **Enable DOA output** — 通过输出端口输出到达方向 off（默认）| on

选择此参数以通过 **Ang** 输出端口输出信号的到达方向（DOA）。

### **Number of signals** — 预期到达信号数 `1`（默认）| 正整数

将 DOA 估计的预期信号数指定为正标量整数。

#### 依赖

要启用此参数，请选中 **Enable DOA output** 复选框。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **Specify sensor array as** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **Expression** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖

要启用此参数，请将 **Specify sensor array as** 设置为 `MATLAB expression`。

#### 阵列参数

### **Geometry** — 阵列几何结构 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何结构，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数 ULA 阵列为 `2`，UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数，指定为大于或等于 2 的整数。

#### 依赖

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列元素间距，ULA 阵列为 `0.5`，URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的 2 元正数值向量

相邻阵列元素之间的间距：

- ULA — 将阵列中两个相邻元素之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1×2 正数值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量的形式为
  `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、
`x` 或 `z`。所有 ULA 阵列元素在局部阵列坐标系中沿此轴均匀间隔排列。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为
  `ULA`。
- 当模块仅支持 ULA 阵列时，此参数也会启用。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 1×2 正整数向量

URA 阵列的维度，指定为正整数或 1×2 正整数向量。

- 如果 **Array size** 是 1×2 向量，则该向量的形式为
  `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列每一行和每一列中的元素数量相同。

对于 URA，阵列元素沿最左侧阵列列从上到下索引，并从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 创建一个具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Element lattice** — URA 元素位置的晶格 `Rectangular`（默认）| `Triangular`

URA 元素位置的晶格，指定为 `Rectangular`
或 `Triangular`。

- `Rectangular` — 将所有元素沿行和列方向对齐。
- `Triangular` — 将矩形晶格的偶数行元素向正行轴方向偏移。
  位移为沿行维度元素间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`URA`。

### **Array normal** — 阵列法线方向，URA 阵列为 `x`，UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为
`x`、
`y` 或
`z`。

平面阵列的元素位于与所选阵列法线方向正交的平面内。元素视轴方向沿阵列法线方向指向。

| 阵列法线参数值 | 元素位置和视轴方向 |
| --- | --- |
| `x` | 阵列元素位于 *yz* 平面内。所有元素视轴向量沿 *x* 轴指向。 |
| `y` | 阵列元素位于 *zx* 平面内。所有元素视轴向量沿 *y* 轴指向。 |
| `z` | 阵列元素位于 *xy* 平面内。所有元素视轴向量沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将
**Geometry** 设置为
`URA` 或
`UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为
`UCA`。

### **Element positions (m)** — 共形阵列元素的位置 `[0;0;0]`（默认）| 3×*N* 实数值矩阵

共形阵列中元素的位置，指定为 3×*N* 实数值矩阵，其中 *N* 是共形阵列中的元素数量。此矩阵的每一列表示阵列局部坐标系中一个阵列元素的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal
Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列单元法向量方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中单元法向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的单元数量。如果参数值为矩阵，则每一列以 `[azimuth;elevation]` 的形式指定对应单元相对于局部坐标系的法向方向。局部坐标系将正 *x* 轴与共形阵列的法向方向对齐。如果参数值为 2×1 列向量，则所有阵列单元使用相同的指向方向。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数来表示任意一种单元对之间通过特定变换产生差异的排列。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，您不能使用需要绕法向方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列单元锥削 1（默认）| 复标量 | 复值行向量

将单元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的单元数量。

锥削也称为*单元权重*，它与阵列单元响应相乘。锥削修改响应的幅度和相位，以降低旁瓣或对主响应轴进行波束扫描。

如果 **Taper** 为标量，则对每个单元施加相同的权重。如果 **Taper** 为向量，则将向量中的一个权重施加到对应的传感器单元。权重的数量必须与阵列的单元数量匹配。

**数据类型：** `double`
## 所属库

Phased Array System Toolbox / Direction of Arrival

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

Beamscan 空间谱估计器

Beamscan Spectrum 模块通过使用窄带常规波束形成器扫描一定范围的方位角和俯仰角，来估计入射窄带信号的二维空间谱。该模块可选地通过定位频谱峰值来计算指定数量信号的到达方向。
