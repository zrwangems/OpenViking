---
type: simulink-block
title: 'FEM-Parameterized PMSM'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Permanent Magnet'
documentation_page: 'femparameterizedpmsm'
documentation_source_path: 'ref/femparameterizedpmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# FEM-Parameterized PMSM

## 端口

### 守恒

### **a** — A 相连接（电气）

与 A 相连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — B 相连接（电气）

与 B 相连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — C 相连接（电气）

与 C 相连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a1** — *a* 正端连接（电气）

*自 R2024a 起*

与 *a* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **b1** — *b* 正端连接（电气）

*自 R2024a 起*

与 *b* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **c1** — *c* 正端连接（电气）

*自 R2024a 起*

与 *c* 正端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **a2** — *a* 负端连接（电气）

*自 R2024a 起*

与 *a* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **b2** — *b* 负端连接（电气）

*自 R2024a 起*

与 *b* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **c2** — *c* 负端连接（电气）

*自 R2024a 起*

与 *c* 负端连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding type** 设置为 `Open-end`。

### **n** — 中性相（电气）

与中性相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 参数设置为以下之一

- `2-D partial derivative data | No thermal
  port`, `2-D partial
  derivative data | Show thermal port`,
  `3-D partial derivative data | No
  thermal port`, `3-D partial
  derivative data | Show thermal port`,
  `4-D partial derivative data | No
  thermal port`, or `4-D
  partial derivative data | Show thermal
  port` 并将 **Winding
  type** 参数设置为
  `Wye-wound`。
- `3-D flux linkage data | No thermal
  port` 或 `3-D flux linkage
  data | Show thermal port`，并将
  **Winding type** 参数设置为
  `Wye-wound`，将
  **Expose neutral port** 参数
  设置为 `Yes`。

### **C** — 电机外壳机械

与电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与电机转子关联的机械旋转守恒端口。

### **HA** — 绕组 A 热端口（热）

与绕组 A 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口（热）

与绕组 B 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口（热）

与绕组 C 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口（热）

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 磁链和转矩参数化方法 `2-D partial derivative data | No thermal port`（默认）| `2-D partial derivative data | Show thermal port` | `3-D partial derivative data | No thermal port` | `3-D partial derivative data | Show thermal port` | `4-D partial derivative data | No thermal port` | `4-D partial derivative data | Show thermal port` | `3-D flux linkage data | No thermal port` | `3-D flux linkage data | Show thermal port`

磁链和转矩的参数化方法。要对将电功率转换为热量的铜电阻和铁耗效应进行建模，请选择带热端口的选项。

### 电气（2-D 偏导数数据参数化）

**Electrical** 参数的此配置对应于 2-D Partial Derivative Data 模块参数化，带或不带热端口。如果您使用的是该模块的 3-D Partial Derivative Data、4-D Partial Derivative Data 或 3-D Flux Linkage Data 参数化，请分别参阅 Electrical (3-D Partial Derivative Data Parameterization)、Electrical (4-D Partial Derivative Data Parameterization) 或 Electrical (3-D Flux Linkage Data Parameterization)。

### **Parameterization** — 参数化方法 `Assume constant mutual inductance - tabulate with phase current and rotor angle`（默认）| `Assume sinusoidal back emf - tabulate with d- and q-axis currents`

选择参数化方法：

- `Assume constant mutual inductance - tabulate
  with phase current and rotor angle`
  — 此方法假定链接每个绕组的磁链仅非线性地取决于该同一绕组中的电流，再加上转子角度。
- `Assume sinusoidal back emf - tabulate with d-
  and q-axis currents` — 此方法
  假定链接每个绕组的磁链非线性地取决于所有定子绕组电流。它还假定永磁磁链为正弦。此选项通常非常适合内置磁体 PMSM（或 IPMSM）。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相连接在端口 **a** 和
  **b** 之间，*b* 相
  在端口 **b** 和
  **c** 之间，*c*
  相在端口 **c** 和
  **a** 之间。
- `Open-end` — 绕组采用
  开放式配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Current vector, i** — 电流向量 `[-2, 0, 2]` `A`（默认）

与所提供的磁链偏导数对应的电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。该值对应于 A 相磁链与转子永磁峰值磁通方向（直轴，或 *`d`* 轴）对齐时的角度。最后一个值 *Θ*max 必须是磁链模式再次达到峰值的转子角度。因此，如果 *Θ*max 以度为单位，则极对数为 360/*Θ*max。默认值对应于 6 极对电机。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。

### **Flux linkage partial derivative wrt current, dPhi(i,theta)/di** — 磁链相对于电流的偏导数 `0.0002*ones(3,4)` `Wb/A`（默认）

磁链相对于电流的偏导数矩阵，定义为电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。默认值对应于定子电感不依赖于定子电流或转子角度的特殊情况。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。

### **Flux linkage partial derivative wrt angle, dPhi(i,theta)/dtheta** — 磁链相对于角度的偏导数 `[0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0]` `Wb/rad`（默认）

磁链相对于转子角度的偏导数矩阵，定义为电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。默认值为 `[0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0; 0, -0.16, 0.16, 0]` Wb/rad，对应于定子电感不依赖于定子电流的特殊情况。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。

### **Direct axis current vector, id** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的电感对应的 *`d`* 轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Quadrature axis current vector, iq** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的电感对应的 *`q`* 轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.0002*ones(3,3)` `H`（默认）

*`d`* 轴电感相对于电流的矩阵，定义为 *`d`* 轴和 *`q`* 轴电流向量的函数。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.0002*ones(3,3)` `H`（默认）

*`q`* 轴电感相对于电流的矩阵，定义为 *`d`* 轴和 *`q`* 轴电流向量的函数。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Permanent magnet flux linkage, PM(id,iq)** — 永磁磁链 `0.1*ones(3,3)` `Wb`（默认）

永磁磁链相对于电流的矩阵，定义为 *`d`* 轴和 *`q`* 轴电流向量的函数。磁链是磁通乘以绕组匝数。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Number of pole pairs** — 极对数 `6`（默认）

永磁电机的极对数。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents` 时，此参数才可见。

### **Calculate torque matrix?** — 电磁转矩数据指定 `Yes`（默认）| `No — specify directly`

指定提供电磁转矩数据的方式：

- Yes — 该模块根据磁链信息计算转矩，作为电流和转子角度的函数。
- `No — specify directly`
  — 通过 **Torque matrix, T(i,theta)**
  参数直接输入电磁转矩数据。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。如果您将 **Parameterization** 参数设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents`，则转矩方程明确地以所提供的矩阵表示。

### **Torque matrix, T(i,theta)** — 转矩矩阵 `zeros(3, 3, 3, 4)` `N*m`（默认）

指定施加到转子的电磁转矩矩阵，作为电流和转子角度的函数。仅当 **Calculate torque matrix?** 设置为 `No — specify directly` 时，此参数才可见。

#### 依赖关系

仅当您将 **Calculate torque matrix?** 参数设置为 `No — specify directly` 时，此参数才可见。

### **Interpolation method** — 插值方法 `Linear` `Smooth`（默认）

选择以下插值方法之一，用于当输入值位于两个连续网格点之间时近似输出值：

- `Linear` — 使用多维插值的线性扩展算法。选择此选项以获得最佳性能。
- `Smooth` — 使用修改后的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (2D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H`（默认）

定子-定子互感，假定其与电流和转子角度均无关。

#### 依赖关系

仅当您将 **Parameterization** 参数设置为 `Assume constant mutual inductance - tabulate with phase current and rotor angle` 时，此参数才可见。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）

零序电感。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Assume sinusoidal back emf - tabulate with d- and q-axis currents`。

### 电气（3-D 偏导数数据参数化）

**Electrical** 参数的此配置对应于 3-D Partial Derivative Data 模块变体，带或不带热端口。如果您使用的是该模块的 2-D Partial Derivative Data、4-D Partial Derivative Data 或 3-D Flux Linkage Data 参数化，请分别参阅 Electrical (2-D Partial Derivative Data Parameterization)、Electrical (4-D Partial Derivative Data Parameterization) 或 Electrical (3-D Flux Linkage Data Parameterization)。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相连接在端口 **a** 和
  **b** 之间，*b* 相
  在端口 **b** 和
  **c** 之间，*c*
  相在端口 **c** 和
  **a** 之间。
- `Open-end` — 绕组采用
  开放式配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的直轴电流向量。电流向量必须是双侧的（具有正值和负值）。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的交轴电流向量。电流向量必须是双侧的（具有正值和负值）。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。该值对应于 A 相磁链与转子永磁峰值磁通方向（直轴，或 *`d`* 轴）对齐时的角度。最后一个值 *Θ*max 必须是磁链模式再次达到峰值的转子角度。因此，如果 *Θ*max 以度为单位，则极对数为 360/*Θ*max。默认值对应于 6 极对电机。

### **A-phase flux linkage partial derivative wrt iA, dPhiA(id,iq,theta)/diA** — A 相磁链相对于 iA 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 A 中电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iB, dPhiA(id,iq,theta)/diB** — A 相磁链相对于 iB 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 B 中电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iC, dPhiA(id,iq,theta)/diC** — A 相磁链相对于 iC 的偏导数 `zeros(3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 C 中电流的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt angle, dPhiA(id,iq,theta)/dtheta** — A 相磁链相对于角度的偏导数 `zeros(3, 3, 4)` `Wb/rad`（默认）

A 相磁链相对于转子角度的偏导数矩阵，定义为两个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **Torque matrix, T(id,iq,theta)** — 转矩矩阵 `zeros(3, 3, 4)` `N*m`（默认）

指定施加到转子的电磁转矩矩阵，作为两个电流和转子角度的函数。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

选择以下插值方法之一，用于当输入值位于两个连续网格点之间时近似输出值：

- `Linear` — 使用多维插值的线性扩展算法。选择此选项以获得最佳性能。
- `Smooth` — 使用修改后的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (3D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### 电气（4-D 偏导数数据参数化）

**Electrical** 参数的此配置对应于 4-D Partial Derivative Data 模块变体，带或不带热端口。如果您使用的是该模块的 2-D Partial Derivative Data、3-D Partial Derivative Data 或 3-D Flux Linkage Data 参数化，请分别参阅 Electrical (2-D Partial Derivative Data Parameterization)、Electrical (3-D Partial Derivative Data Parameterization) 或 Electrical (3-D Flux Linkage Data Parameterization)。

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相连接在端口 **a** 和
  **b** 之间，*b* 相
  在端口 **b** 和
  **c** 之间，*c*
  相在端口 **c** 和
  **a** 之间。
- `Open-end` — 绕组采用
  开放式配置。该模块将绕组的每一端作为电气连接暴露出来。

### **A-phase current vector, iA** — A 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 A 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **B-phase current vector, iB** — B 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 B 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **C-phase current vector, iC** — C 相电流向量 `[-200, 0, 200]` `A`（默认）

与所提供的磁链偏导数对应的 C 相电流向量。电流向量必须是双侧的（具有正值和负值）。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 20, 40, 60]` `deg`（默认）

与所提供的磁链偏导数对应的转子角度向量。该向量必须从零开始。该值对应于 A 相磁链与转子永磁峰值磁通方向（直轴，或 *`d`* 轴）对齐时的角度。最后一个值 *Θ*max 必须是磁链模式再次达到峰值的转子角度。因此，如果 *Θ*max 以度为单位，则极对数为 360/*Θ*max。默认值对应于 6 极对电机。

### **A-phase flux linkage partial derivative wrt iA, dPhiA(iA,iB,iC,theta)/diA** — A 相磁链相对于 iA 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 A 中电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iB, dPhiA(iA,iB,iC,theta)/diB** — A 相磁链相对于 iB 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 B 中电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt iC, dPhiA(iA,iB,iC,theta)/diC** — A 相磁链相对于 iC 的偏导数 `zeros(3, 3, 3, 4)` `Wb/A`（默认）

A 相磁链相对于绕组 C 中电流的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **A-phase flux linkage partial derivative wrt angle, dPhiAiA,iB,iC,theta)/dtheta** — A 相磁链相对于角度的偏导数 `zeros(3, 3, 3, 4)` `Wb/rad`（默认）

A 相磁链相对于转子角度的偏导数矩阵，定义为三个电流向量和转子角度向量的函数。磁链是磁通乘以绕组匝数。

### **Torque matrix, T(iA,iB,iC,theta)** — 转矩矩阵 `zeros(3, 3, 3, 4)` `N*m`（默认）

指定施加到转子的电磁转矩矩阵，作为三个电流和转子角度的函数。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

选择以下插值方法之一，用于当输入值位于两个连续网格点之间时近似输出值：

- `Linear` — 使用多维插值的线性扩展算法。选择此选项以获得最佳性能。
- `Smooth` — 使用修改后的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (3D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### 电气（3-D 磁链数据参数化）

**Electrical** 参数的此配置对应于 3-D Flux Linkage Data 模块变体，带或不带热端口。如果您使用的是该模块的 2-D Partial Derivative Data、3-D Partial Derivative Data 或 4-D Partial Derivative Data 参数化，请分别参阅 Electrical (2-D Partial Derivative Data Parameterization)、Electrical (3-D Partial Derivative Data Parameterization) 或 Electrical (4-D Partial Derivative Data Parameterization)。

### **Flux linkage data format** — 磁链数据格式 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`（默认）| `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` | `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` | `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`

选择您的 FE 工具使用的磁链数据格式：

- `D and Q axes flux linkages as a function of
  D-axis current (iD), Q-axis current (iQ), and rotor
  angle (theta)`
- `D and Q axes flux linkages as a function of
  peak current magnitude (I), current advance angle (B),
  and rotor angle (theta)`
- `A-phase flux linkage as a function of D-axis
  current (iD), Q-axis current (iQ), and rotor angle
  (theta)`
- `A-phase flux linkage as a function of peak
  current magnitude (I), current advance angle (B), and
  rotor angle (theta)`

### **Winding type** — 定子绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

选择定子绕组配置：

- `Wye-wound` — 定子绕组
  为星形连接。
- `Delta-wound` — 定子
  绕组为三角形连接。*a* 相连接在端口 **a** 和
  **b** 之间，*b* 相
  在端口 **b** 和
  **c** 之间，*c*
  相在端口 **c** 和
  **a** 之间。
- `Open-end` — 绕组采用
  开放式配置。该模块将绕组的每一端作为电气连接暴露出来。

### **Expose neutral port** — 中性端口可见性 `No`（默认）| `Yes`

是否暴露模块的中性端口。

如果您暴露中性端口，该模块还会对零序电流建模。零序由 **Stator zero-sequence inductance, L0** 参数参数化。当您按 *iD* 和 *iQ* 进行表格化，或按电流幅值和相角超前进行表格化时，没有关于对零序电流的非线性依赖的信息，模块会引入一定程度的近似。对于更准确的结果，尤其是对于大零序电流，请使用 **4-D partial derivative data** 参数化选项。

#### 依赖关系

要启用此参数，请将 **Winding type** 参数设置为 `Wye-wound`。

### **Number of pole pairs** — 极对数 `4`（默认）

永磁电机的极对数。默认值为 `4`。

### **Park's convention for tabulated data** — 表格数据的 Park 约定 `Q leads D, rotor angle measured from A-phase to D-axis`（默认）| `Q leads D, rotor angle measured from A-phase to Q-axis` | `D leads Q, rotor angle measured from A-phase to D-axis` | `D leads Q, rotor angle measured from A-phase to Q-axis`

选择将给定 *dq* 数据映射到三个绕组的 Park 变换的顺序和参考角。

- `Q leads D, rotor angle measured from A-phase
  to D-axis` — 交-直变换，角度相对于
  *d* 轴测量。
- `Q leads D, rotor angle measured from A-phase
  to Q-axis` — 交-直变换，角度相对于
  *q* 轴测量。
- `D leads Q, rotor angle measured from A-phase
  to D-axis` — 直-交变换，角度相对于
  *d* 轴测量。
- `D leads Q, rotor angle measured from A-phase
  to Q-axis` — 直-交变换，角度相对于
  *q* 轴测量。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）

磁链表格化所依据的直轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）

磁链表格化所依据的交轴电流向量。电流向量必须是双侧的（具有正值和负值）。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Peak current magnitude vector, I** — 峰值电流幅值向量 `[0, 100, 200]` `A`（默认）

磁链表格化所依据的电流幅值的行向量。第一个元素必须为零。相邻电流值应相对于磁饱和开始发生的电流值较小。这是因为推导出的磁通偏导数在零电流处定义不良，因此改为在该第一个非零电流处计算。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Current advance angle, B** — 电流超前角 `[-180, -90, 0, 90, 180]` `deg`（默认）

磁链表格化所依据的电流超前角值的行向量。电流超前角定义为电流超前交轴 (Q) 的角度。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Rotor angle vector, theta** — 转子角度向量 `[0, 5, 10, 15, 20, 25, 30]` `deg`（默认）

磁链表格化所依据的转子角度向量。该向量必须从零开始。默认值对应于 4 极对电机。

如果 **Flux linkage data format** 为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`（即，如果您表格化 D 和 Q 磁链数据），则转子角度向量必须具有四个或更多点，并且范围从 0 到 120/*N* 度，其中 *N* 是极对数。如果 **Flux linkage data format** 为 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`（即，如果您表格化 A 相磁链数据），则转子角度向量必须具有 3*n*+1 个点，其中 *n*>=2，并且范围必须从 0 到 360/*N* 度。

### **D-axis flux linkage, Fd(iD,iQ,theta)** — D 轴磁链 `zeros(3, 3, 7)` `Wb`（默认）

*`d`* 轴磁链矩阵，定义为 *dq* 电流和转子角度向量的函数。磁链是磁通乘以绕组匝数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Q-axis flux linkage, Fq(iD,iQ,theta)** — Q 轴磁链 `zeros(3, 3, 7)` `Wb`（默认）

*`q`* 轴磁链矩阵，定义为 *dq* 电流和转子角度向量的函数。磁链是磁通乘以绕组匝数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **D-axis flux linkage, Fd(I,B,theta)** — D 轴磁链 `zeros(3, 5, 7)` `Wb`（默认）

*`d`* 轴磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor angle vector, theta** 的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Q-axis flux linkage, Fq(I,B,theta)** — Q 轴磁链 `zeros(3, 5, 7)` `Wb`（默认）

*`q`* 轴磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor angle vector, theta** 的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **A-phase flux linkage, F(iD,iQ,theta)** — A 相磁链 `zeros(3, 3, 7)` `Wb`（默认）

A 相磁链值的 3-D 矩阵，作为 *dq* 电流和转子角度的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **A-phase flux linkage, F(I,B,theta)** — A 相磁链 `zeros(3, 5, 7)` `Wb`（默认）

A 相磁链值的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor angle vector, theta** 的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Torque matrix, T(iD,iQ,theta)** — 转矩矩阵 `zeros(3, 3, 7)` `N*m`（默认）

施加到转子的电磁转矩的 3-D 矩阵，作为 *dq* 电流和转子角度的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 时，此参数才可见。

### **Torque matrix, T(I,B,theta)** — 转矩矩阵 `zeros(3, 5, 7)` `N*m`（默认）

施加到转子的电磁转矩的 3-D 矩阵，作为 **Peak current magnitude vector, I**、**Current advance angle, B** 和 **Rotor angle vector, theta** 的函数。

如果您的磁通数据以不同顺序给出，可以使用 `permute` 函数对其重新排序。有关此重新排序的示例，请参阅 Import IPMSM Flux Linkage Data from ANSYS Maxwell 中关联的 MATLAB 脚本。

#### 依赖关系

仅当您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 时，此参数才可见。

### **Interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

选择以下插值方法之一，用于当输入值位于两个连续网格点之间时近似输出值：

- `Linear` — 使用多维插值的线性扩展算法。选择此选项以获得最佳性能。
- `Smooth` — 使用修改后的 Akima 插值算法。选择此选项以生成具有连续一阶导数的连续曲面。

有关插值方法的详细信息，请参阅 PS Lookup Table (4D) 模块参考页。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）

每个定子绕组的电阻。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）

零序电感。

#### 依赖关系

要启用此参数，请将 **Winding type** 设置为 `Delta-Wound` 或将 **Expose neutral port** 设置为 `Yes`。

### 铁耗

有关计算铁耗的详细信息，请参阅 Calculating Iron Losses。

### **Model** — 铁耗建模选项 `None`（默认）| `Specify open and short circuit loss data (permanent magnet motors only)` | `Specify tabulated Steinmetz coefficients` | `Tabulate with current and speed`

是否启用铁耗建模。`Specify tabulated Steinmetz coefficients` 和 `Tabulate with current and speed` 选项仅在您选择 **3-D flux linkage data | No thermal port** 或 **3-D flux linkage data | Show thermal port** 变体时可用。

### **Open-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 开路铁耗 `[0.0, 0.0, 0.0]` `W`（默认）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下，由磁滞、涡流和过剩损耗引起的开路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent magnet motors only)`

### **Short-circuit iron losses, [P\_hysteresis P\_eddy P\_excess]** — 短路铁耗 `[0.0, 0.0, 0.0]` `W`（默认）

长度为 3 的行向量，分别表示在 **Electrical frequency at which losses determined** 指定的频率下，由磁滞、涡流和过剩损耗引起的短路铁耗。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent magnet motors only)`

### **Electrical frequency at which losses determined** — 确定损耗时的电气频率 `60` `Hz`（默认）

测量开路和短路铁耗时的电气频率。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent magnet motors only)`。

### **Short-circuit RMS current for short-circuit iron losses** — 用于短路铁耗的短路 RMS 电流 `95` `A`（默认）

测量短路损耗时得到的短路 RMS 相电流。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify open and short circuit loss data (permanent magnet motors only)`

### **Rotor hysteresis loss coefficient, k\_hr(id,iq)** — 转子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

转子的磁滞损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Rotor eddy current loss coefficient, k\_Jr(id,iq)** — 转子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

转子的涡流损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Rotor excess current loss coefficient, k\_er(id,iq)** — 转子过剩电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

转子的过剩电流损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Stator hysteresis loss coefficient, k\_hs(id,iq)** — 定子磁滞损耗系数 `zeros(3, 3)` `W/Hz`（默认）

定子的磁滞损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Stator eddy current loss coefficient, k\_Js(id,iq)** — 定子涡流损耗系数 `zeros(3, 3)` `W/Hz^2`（默认）

定子的涡流损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Stator excess current loss coefficient, k\_es(id,iq)** — 定子过剩电流损耗系数 `zeros(3, 3)` `W/Hz^1.50000`（默认）

定子的过剩电流损耗系数，取决于 *`d`* 轴和 *`q`* 轴电流。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Rotor hysteresis loss coefficient, k\_hr(I,B)** — 转子磁滞损耗系数 `zeros(3, 5)` `W/Hz`（默认）

转子的磁滞损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Rotor eddy current loss coefficient, k\_Jr(I,B)** — 转子涡流损耗系数 `zeros(3, 5)` `W/Hz^2`（默认）

转子的涡流损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Rotor excess current loss coefficient, k\_er(I,B)** — 转子过剩电流损耗系数 `zeros(3, 5)` `W/Hz^1.50000`（默认）

转子的过剩电流损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Stator hysteresis loss coefficient, k\_hs(I,B)** — 定子磁滞损耗系数 `zeros(3, 5)` `W/Hz`（默认）

定子的磁滞损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Stator eddy current loss coefficient, k\_Js(I,B)** — 定子涡流损耗系数 `zeros(3, 5)` `W/Hz^2`（默认）

定子的涡流损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Stator excess current loss coefficient, k\_es(I,B)** — 定子过剩电流损耗系数 `zeros(3, 5)` `W/Hz^1.50000`（默认）

定子的过剩电流损耗系数，取决于电流幅值和电流相位超前。它由 Steinmetz 方程使用。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Specify tabulated Steinmetz coefficients`，并在 **Electrical** 选项卡中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Rotor speed vector, w** — 转子速度 `[1000, 2000]` `rpm`（默认）

铁耗表格化所依据的转子速度向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`，并在 **Electrical** 设置中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Rotor iron loss table, Pr(id,iq,w)** — 转子铁耗表 `zeros(3, 3, 2)` `W`（默认）

转子的铁耗，按 *`d`* 轴和 *`q`* 轴电流以及转子速度表格化。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`，并在 **Electrical** 设置中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Stator iron loss table, Ps(id,iq,w)** — 定子铁耗表 `zeros(3, 3, 2)` `W`（默认）

定子的铁耗，按 *`d`* 轴和 *`q`* 轴电流以及转子速度表格化。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`，并在 **Electrical** 设置中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`。

### **Rotor iron loss table, Pr(I,B,w)** — 转子铁耗表 `zeros(3, 5, 2)` `W`（默认）

转子的铁耗，按电流幅值、电流相位超前和转子速度表格化。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`，并在 **Electrical** 设置中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### **Stator iron loss table, Ps(I,B,w)** — 定子铁耗表 `zeros(3, 5, 2)` `W`（默认）

定子的铁耗，按电流幅值、电流相位超前和转子速度表格化。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Tabulate with current and speed`，并在 **Electrical** 设置中，将 **Flux linkage data format** 设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认）

连接到机械平移端口 **R** 的转子的惯量。该值可以为零。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认）

旋转阻尼。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认）

电机参数所引用的温度。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

关联电阻与温度的方程中的系数 α，如 Thermal Model for Actuator Blocks 所述。默认值适用于铜。

### **Permanent magnet flux temperature coefficient** — 永磁磁通温度系数 `-0.001`（默认）

永磁磁通密度随温度变化的分数变化率。它用于在温度升高时线性降低转矩和感应反电动势。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal mass for each stator winding** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Initial stator winding temperatures** — 定子绕组初始温度 `[298.15, 298.15, 298.15]` `K`（默认）

一个 1×3 行向量，定义仿真开始时 A、B 和 C 热端口的温度。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即将转子温度升高一度所需的能量。

### **Rotor initial temperature** — 转子初始温度 `298.15` `K`（默认）

仿真开始时转子的温度。

### **Percentage of main flux path iron losses associated with the rotor** — 与转子关联的主磁通路径铁耗百分比 `90`（默认）

与通过转子的磁路关联的主磁通路径铁耗百分比。它确定有多少铁耗热量归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。

### **Percentage of cross-tooth flux path iron losses associated with the rotor** — 与转子关联的跨齿磁通路径铁耗百分比 `30`（默认）

与通过转子的磁路关联的跨齿磁通路径铁耗百分比。它确定有多少铁耗热量归属于转子热端口 **HR**，以及有多少归属于三个绕组热端口 **HA**、**HB** 和 **HC**。

## 库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

### R2024a：定子绕组的开放式配置

要对机器的定子绕组采用开放式配置进行建模，请将 **Winding type** 参数设置为 `Open-end`。然后，FEM-Parameterized PMSM 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

## 描述

根据磁链定义的永磁同步电机

FEM-Parameterized PMSM 模块对根据磁链定义的永磁同步电机 (PMSM) 进行建模。使用此模块对具有永磁转子的任何三相电机进行建模，例如：

- 轴向磁通（盘式）电机
- 无刷伺服电机
- 具有内置磁体转子的电机，例如内置永磁 (IPM) 电机或内置永磁同步电机 (IPMSM)
- 具有表面安装磁体转子的电机：

  - 表面永磁 (SPM) 电机或表面永磁同步电机 (SPMSM)
  - 无刷直流 (BLDC) 电机

您通过使用电机磁通作为电流和转子角度的函数的表格化数据来参数化该模块。这是有限元方法 (FEM) 软件包通常导出磁通信息的方式。由于该模块使用表格化数据，磁通可以随转子角度和电流二者非线性变化。对转子角度的非线性依赖使该模块能够支持 BLDC 电机表现出的梯形磁通分布，并且还能捕获仅近似正弦磁通分布的电机的高次谐波。

此图显示了星形连接 PMSM 的等效电路。

此图显示了转子具有单极对的电机结构。当永磁磁通与 *A* 相磁轴对齐时，转子角度为零。

在实践中，链接三个绕组中每个绕组的磁通取决于所有三个电流和转子角度。将磁通表格化为四个自变量的函数可能导致仿真效率低下和显著的内存需求。因此，该模块允许您使用 **Modeling option** 参数指定如何对磁链和转矩建模：

- 2-D partial derivative data — 2-D 查表，可选择按电流和转子角度表格化，或按 *`d`* 轴和 *`q`* 轴电流表格化。第一个选项假定恒定互感并支持非正弦反电动势 (EMF) 分布。第二个选项假定正弦反电动势并捕获 IPMSM 的饱和效应。
- 3-D partial derivative data — 基于直轴电流、交轴电流和转子角度的 3-D 查表。您为 *a* 相提供磁通查找数据。该模块使用 Park 变换将三个定子绕组电流映射为直轴和交轴电流。与 4-D 查表相比，此方法降低了数据复杂性，并改善了仿真性能。
- 4-D partial derivative data — 基于三个定子绕组电流和转子角度的 4-D 查表。您为 *a* 相提供磁通查找数据。此模型比 2-D 和 3-D 偏导数数据模型具有更高的保真度，但其仿真性能最低，内存需求最高。
- 3-D flux linkage data — 基于磁链数据的 3-D 查表。您可以以多种格式提供磁链数据。该模块使用 Park 变换将三个定子绕组电流映射为直轴和交轴电流。与 4-D 查表相比，此方法降低了数据复杂性，并改善了仿真性能。

某些 **Modeling option** 参数设置还会启用热端口。有关详细信息，请参阅 Model Thermal Effects。

默认情况下，对于所有这些参数化方法，该模块为定子绕组实现星形连接配置。但是，您可以使用 **Winding type** 参数切换到三角形连接或开放式配置。在三角形连接配置中，*a* 相连接端口 **a** 和 **b**，*b* 相在端口 **b** 和 **c** 之间，*c* 相连接端口 **c** 和 **a**。

**注意**

Simscape™ Electrical™ 包含多个可以对同一类型电机或执行器建模的模块。请选择一个具有足够建模细节的模块，以回答您需要解决的工程设计问题。不要使用建模细节超出您需要的模块，因为更高保真度的模型会减慢仿真速度并且参数化更复杂。

像 FEM-Parameterized PMSM 模块这样的模块根据磁链定义电机行为。这些模型具有高保真度。仅在需要高建模细节时使用此模块，例如，预测牵引应用的效率或捕获转矩和电流谐波。有关选择合适模块以适当保真度对电机建模的详细信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 具有恒定互感的 2-D 数据模型

在此 2-D 磁通数据模型中，假定链接每个绕组的磁通仅非线性地取决于该同一绕组中的电流，再加上转子角度。在实践中，对于许多永磁同步电机来说，这是一个合理的假设；然而，对于开关磁阻电机来说，其准确性较低。给定此假设，三个绕组中的磁通为：

[ϕaϕbϕc]=[0−Ms−Ms−Ms0−Ms−Ms−Ms0][iaibic]+[ϕ(ia,θr)ϕ(ib,θr−2π/(3N))ϕ(ic,θr−4π/(3N))]

其中 ϕ(θr,ia) 是 A 相绕组的磁链，作为转子角度和 A 相电流的函数。*Θ*r = 0 对应于转子 *`d`* 轴与 A 相正磁通方向对齐。*M*s 是定子-定子互感。

为了提高数值性能，该模块中实现的方程实际上使用磁链相对于电流的偏导数 ∂ϕ(i,θr)/∂i 和相对于转子角度的偏导数 ∂ϕ(i,θr)/∂θr，而不是直接使用磁链。如果您的 FEM 软件包不导出这些偏导数，您可以使用 MATLAB® 脚本确定它们。有关如何执行此操作的示例，请参阅 Solenoid Parameterized with FEM Data 示例模型及其支持的 MATLAB 脚本。

该模块的电气方程，以磁通偏导数形式定义，为：

va=∂ϕ∂iadiadt+∂ϕ∂θrdθrdt−Ms(dibdt+dicdt)+Rsiavb=∂ϕ∂ibdibdt+∂ϕ∂θrdθrdt−Ms(diadt+dicdt)+Rsibvc=∂ϕ∂icdicdt+∂ϕ∂θrdθrdt−Ms(diadt+dibdt)+Rsic

其中

- *v*a、*v*b、*v*c 是施加到 A、B 和 C 定子绕组的电压。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *R*s 是每个定子绕组的电阻。
- *M*s 是定子-定子互感。
- ∂ϕ/∂ia、∂ϕ/∂ib、∂ϕ/∂ic 是磁链相对于三个绕组中每个绕组定子电流的偏导数。
- ∂ϕ/∂θr 是磁链相对于转子角度的偏导数。

该模块可以根据您提供的磁通信息自动计算转矩矩阵。或者，您可以将 **Calculate torque matrix?** 参数设置为 `No`，并直接指定转矩作为电流和转子角度的函数。有关详细信息，请参阅 FEM-Parameterized Rotary Actuator 模块参考页。

### 具有正弦反电动势的 2-D 数据模型

在此 2-D 磁通数据模型中，假定链接每个绕组的磁通非线性地取决于所有定子绕组电流，此外还假定永磁磁链为正弦。内置磁体 PMSM（或 IPMSM）通常很好地符合此假设。方程为：

[ϕdϕq]=[Ld(id,iq)Lq(id,iq)][idiq]+[ϕm(id,iq)]

T=32N(iq(idLd(id,iq)+ϕm(id,iq))−idiqLq(id,iq))

其中

- *i*d 和 *i*q 分别是 *`d`* 轴和 *`q`* 轴电流。
- *ϕ*d 和 *ϕ*q 分别是 *`d`* 轴和 *`q`* 轴磁链。
- *ϕ*m 是永磁磁链。
- *L*d 和 *L*q 分别是 *`d`* 轴和 *`q`* 轴电感。假定它们取决于 *`d`* 轴和 *`q`* 轴电流。
- *N* 是极对数。
- *T* 是电磁转矩。

### 使用 Park 变换的 3-D 偏导数数据模型

处理四维数据既有仿真性能成本，也有内存成本。为了将表维度降低到三维，3-D 数据模型使用 Park 变换将三个电流映射为直轴和交轴电流：

[idiq]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)][iaibic]

在一般情况下，Park 变换映射为直轴、交轴和零序电流。然而，在正常工作条件下，零序电流通常很小。因此，该模型忽略磁链项对零序电流的依赖，并仅根据直轴和交轴电流加上转子角度来确定磁链。3-D 数据模型的磁通方程为：

[ϕaϕbϕc]=[ϕ(id,iq,θr)ϕ(id,iq,θr−2π/(3N))ϕ(id,iq,θr−4π/(3N))]

该模块的电气方程也以磁通偏导数形式定义，类似于 4-D 数据模型。您可以使用 `ee_calculateFluxPartialDerivatives` 从 4-D 磁链数据计算 3-D 磁链偏导数数据。

### 4-D 偏导数数据模型

链接每个绕组的磁通是该绕组中的电流、其他两个绕组中的电流以及转子角度的函数。为了完全准确，4-D 磁通数据模型假定磁链是三个电流和转子角度的函数，因此执行四维查表。磁通方程为：

[ϕaϕbϕc]=[ϕ(ia,ib,ic,θr)ϕ(ib,ic,ia,θr−2π/(3N))ϕ(ic,ia,ib,θr−4π/(3N))]

其中

- *ϕ*a、*ϕ*b、*ϕ*c 是 A、B 和 C 定子绕组的磁链。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *Θ*r 是转子角度。*Θ*r = 0 对应于永磁磁通与 A 相定子绕组磁通对齐的情况。
- *N* 是极对数。

假定磁链数据随 *Θ*r 周期性变化。例如，如果电机有六个极对，则数据范围为 0 ≤ *Θ*r ≤ 60°。您必须在 0 度和 60 度处都提供数据，并且由于数据是周期性的，磁链偏导数在这两个端点处必须相同。

转矩方程为：

τ=T(ia,ib,ic,θr)

4-D 数据模型没有让模块根据磁链确定转矩的选项。由于 4-D 情况下的数值开销增加，最好只预先计算一次转矩，而不是每次运行仿真时都计算它。

为了提高数值性能，该模块中实现的方程实际上使用磁链相对于三个电流和转子角度的偏导数，而不是直接使用磁链。如果您的 FEM 软件包不导出这些偏导数，您可以使用 `ee_calculateFluxPartialDerivatives` 确定它们。

该模块的电气方程，以磁通偏导数形式定义，为：

va=∂ϕa∂iadiadt+∂ϕa∂ibdibdt+∂ϕa∂icdicdt+∂ϕa∂θrdθrdt+Rsiavb=∂ϕb∂iadiadt+∂ϕb∂ibdibdt+∂ϕb∂icdicdt+∂ϕb∂θrdθrdt+Rsibvc=∂ϕc∂iadiadt+∂ϕc∂ibdibdt+∂ϕc∂icdicdt+∂ϕc∂θrdθrdt+Rsic

其中

- *v*a、*v*b、*v*c 是施加到 A、B 和 C 定子绕组的电压。
- *i*a、*i*b、*i*c 是三个绕组中每个绕组的定子电流。
- *R*s 是每个定子绕组的电阻。

### 3-D 磁链数据模型

3-D 磁链数据选项允许您使用从有限元 (FE) 电机设计工具导出的原始磁链数据。这与 3-D 偏导数数据选项形成对比，后者需要您确定偏导数。您可以以多种格式提供磁链数据，以支持不同的 FE 工具约定：

- 表格化 DQ 轴磁链数据或 A 相磁链数据 — 一些工具支持使用分解为直轴 (D) 和交轴 (Q) 的磁链。这种方法的一个优点是只需要 0 到 360/*N*/3 度范围内的转子角度数据（其中 *N* 是极对数）。其他工具直接使用 A、B 和 C 相磁链，对于这种情况，您可以仅导入 A 相磁链，其转子角度范围必须在 0 到 360/*N* 度范围内。仅导入 A 相数据的隐含假设是 B 和 C 相数据相同，只是相位偏移。
- 使用笛卡尔或极坐标电流进行表格化 — 笛卡尔表格化意味着磁链按 D 轴电流和 Q 轴电流（加上转子角度）表格化。或者，极坐标表格化涉及按电流幅值、相对于 Q 轴的电流超前角和转子角度表格化磁链。极坐标的优点是它更自然地反映允许的工作电流，从而避免未使用的表格数据点。

这些约定产生了四个 **Flux linkage data format** 参数化选项：

- `D and Q axes flux linkages as a function of D-axis current
  (iD), Q-axis current (iQ), and rotor angle (theta)`
- `D and Q axes flux linkages as a function of peak current
  magnitude (I), current advance angle (B), and rotor angle
  (theta)`
- `A-phase flux linkage as a function of D-axis current (iD),
  Q-axis current (iQ), and rotor angle (theta)`
- `A-phase flux linkage as a function of peak current magnitude
  (I), current advance angle (B), and rotor angle
  (theta)`

FEM-Parameterized PMSM 模块需要 3-D 磁链数据。要将 2-D 磁链数据 `F(id,iq)` 转换为 3-D 表 `F(id,iq,x)`，请使用 `repmat` 函数。

除了选择您的 FE 工具使用的磁链数据格式外，您还必须选择该工具使用的 Park 变换版本。下面描述了四种约定，它们对应于 **Park’s convention for tabulated data** 下拉菜单的四个选项。

**注意**

查看记录的 D 轴和 Q 轴电流值时，请记住，对于这些选项中的每一个，格式都会根据需要转换，以便在内部，FEM-Parameterized PMSM 模块一致地使用 Option 1。

**注意**

为了保留由永磁反电动势引起的高次谐波，请提供 A 相磁通数据而不是 D 轴和 Q 轴磁通数据。相反，如果您提供 D 轴和 Q 轴磁通，Park 变换会移除高次谐波。使用 D 和 Q 磁通对于许多应用来说已经足够，特别是如果您将 **Winding type** 参数设置为 `Wye-wound` 并且没有连接到该模块的中性端口。对于这种特定情况，中性端口处电流和为零的约束会移除所有三次谐波。

**Option 1. Q leads D, rotor angle measured from A-phase to D-axis**

这是 Simscape Electrical 电机和电机模块内部使用的 Park 约定。所有其他选项都会转换为这种格式。

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

对应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**Option 2. Q leads D, rotor angle measured from A-phase to Q-axis**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

对应的 Park 变换为

[idiqi0]=23[sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**Option 3. D leads Q, rotor angle measured from A-phase to D-axis**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

对应的 Park 变换为

[idiqi0]=23[cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)sin(Nθr)sin(Nθr−2π3)sin(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

**Option 4. D leads Q, rotor angle measured from A-phase to Q-axis**

- *N*：极对数
- *θ*r：转子角度
- *i*d、*i*q：D 轴和 Q 轴电流
- *i*p：电流幅值 = id2+iq2
- *β*：电流超前角 = tan−1(−id/iq)

对应的 Park 变换为

[idiqi0]=23[−sin(Nθr)−sin(Nθr−2π3)−sin(Nθr+2π3)cos(Nθr)cos(Nθr−2π3)cos(Nθr+2π3)121212][iaibic]

其中 *i*a、*i*b 和 *i*c 分别是 A 相、B 相和 C 相电流。

### 计算铁耗

FEM-Parameterized PMSM 模块根据您为磁链和转矩选择的参数化方法对铁耗建模。

这些铁耗会产生热量。该模块将转子铁耗产生的热量注入表示转子热质量的 **HR** 热端口。该模块将定子铁耗分成三个相等部分，并将每一部分注入定子绕组热端口 **HA**、**HB** 和 **HC**。

**指定开路和短路损耗数据（仅永磁电机）**

对于 **2-D partial derivative data**、**3-D partial derivative data** 和 **4-D partial derivative data** 选项，带或不带热端口，铁耗模型基于 Mellor [1] 的工作。铁耗分为两项，一项表示主磁化路径，另一项表示在弱磁操作期间变为活动的跨齿尖路径。

表示主磁化路径的项取决于感应 RMS 定子电压 Vmrms：

POC(Vmrms)=ahkVmrms+ajk2Vmrms2+aexk1.5Vmrms1.5.

这是空载操作期间的主导项。*k* 是关联 RMS 伏特每赫兹的反电动势常数。它定义为 k=Vmrms/f，其中 *f* 是电气频率。右侧第一项是磁滞损耗，第二项是涡流损耗，第三项是过剩损耗。分子中出现的三个系数由您为开路磁滞、涡流和过剩损耗提供的值推导而来。

表示跨齿尖路径的项在建立去磁场时变得重要，可以通过有限元分析短路测试确定。它取决于与跨齿尖磁通关联的 RMS EMF Vdrms\*：

PSC(Vdrms\*)=bhkVdrms\*+bjk2Vdrms\*2+bexk1.5Vdrms\*1.5.

三个分子项由您为短路磁滞、涡流和过剩损耗提供的值推导而来。

**Steinmetz 参数化方法**

对于带或不带热端口的 **3-D flux linkage data**，您还可以基于 Steinmetz 方程对铁耗建模。Steinmetz 方法会随不同电机速度或电气频率进行缩放，因此铁耗数据仅需要作为电机电流的函数。

如果在 **Iron Losses** 设置中，您将 **Model** 参数设置为 `Specify open and short circuit loss data (permanent magnet motors only)`，则该模块使用 Steinmetz 方法，但假定系数恒定，并且不依赖于峰值电流和电流相位超前。如果您有测功机测量数据，或者您执行 FE 分析以仅从开路和短路仿真获得铁耗，请选择此选项。

相反，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`，则该模块使用 **Peak current magnitude vector, I** 和 **Current advance angle vector, B** 参数表格化系数，因此铁耗由下式给出：

Protor(f)=khr(Ip,β)f+kJr(Ip,β)f2+ker(Ip,β)f1.5Pstator(f)=khs(Ip,β)f+kJs(Ip,β)f2+kes(Ip,β)f1.5

其中：

- *f* 是电气瞬时频率，单位为 `Hz`，等于转子机械速度乘以极对数。此频率是随时间变化的变量。
- *khr(Ip,β)* 是 **Rotor hysteresis loss coefficient, k\_hr(I,B)**。
- *kJr(Ip,β)* 是 **Rotor eddy current loss coefficient, k\_Jr(I,B)**。
- *ker(Ip,β)* 是 **Rotor excess current loss coefficient, k\_er(I,B)**。
- *khs(Ip,β)* 是 **Stator hysteresis loss coefficient, k\_hs(I,B)**。
- *kJs(Ip,β)* 是 **Stator eddy current loss coefficient, k\_Js(I,B)**。
- *kes(Ip,β)* 是 **Stator excess current loss coefficient, k\_es(I,B)**。

类似地，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`，则铁耗由下式给出：

Ploss,rotor(f)=khr(id,iq)f+kJr(id,iq)f2+ker(id,iq)f1.5Ploss,stator(f)=khs(id,iq)f+kJs(id,iq)f2+kes(id,iq)f1.5

其中：

- *khr(id,iq)* 是 **Rotor hysteresis loss coefficient, k\_hr(id,iq)**。
- *kJr(id,iq)* 是 **Rotor eddy current loss coefficient, k\_Jr(id,iq)**。
- *ker(id,idq)* 是 **Rotor excess current loss coefficient, k\_er(id,iq)**。
- *khs(id,iq)* 是 **Stator hysteresis loss coefficient, k\_hs(id,iq)**。
- *kJs(id,iq)* 是 **Stator eddy current loss coefficient, k\_Js(id,iq)**。
- *kes(id,iq)* 是 **Stator excess current loss coefficient, k\_es(id,iq)**。

仅结合能够计算系数的电机设计工具选择此选项。您可以使用 Motor-CAD 或 ANSYS® Maxwell® 等 FEM 工具，以笛卡尔坐标 (*id*,*iq*) 或径向坐标 (*Ip*,*β*) 导出 Steinmetz 系数查找表。这些系数在一定电流和频率范围内有效。为了根据机器的当前状态获得正确的值，该模块在运行时插值 Steinmetz 系数值。

有关从 FEM 工具导入 Steinmetz 系数的详细信息，请参阅 Import IPMSM Flux Linkage Data from Motor-CAD 示例。

**按电流和速度表格化**

对于带或不带热端口的 **3-D flux linkage data**，您还可以通过分别对转子和定子表格化来对铁耗建模。

如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)` 或 `A-phase flux linkage as a function of peak current magnitude (I), current advance angle (B), and rotor angle (theta)`，则该模块使用 **Peak current magnitude vector, I** 和 **Current advance angle vector, B** 参数表格化铁耗，因此铁耗由下式给出：

Ploss(Ip,β,w)=tablelookup(Ptable,Ip,β,w)

其中 *w* 是 **Rotor speed vector, w** 参数。

类似地，如果您将 **Flux linkage data format** 参数设置为 `D and Q axes flux linkages as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)` 或 `A-phase flux linkage as a function of D-axis current (iD), Q-axis current (iQ), and rotor angle (theta)`，则铁耗由下式给出：

Ploss(id,iq,w)=tablelookup(Ptable,id,iq,w).

### 热效应建模

您可以暴露热端口，以对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `2-D partial derivative data | No thermal port` — 2-D 查表参数化，可选择按电流和转子角度表格化，但不带热端口。
- `2-D partial derivative data | Show thermal port` — 2-D 查表参数化，可选择按电流和转子角度表格化，并带热端口。
- `3-D partial derivative data | No thermal port` — 基于直轴电流、交轴电流和转子角度的 3-D 查表参数化，但不带热端口。
- `3-D partial derivative data | Show thermal port` — 基于直轴电流、交轴电流和转子角度的 3-D 查表参数化，并带热端口。
- `4-D partial derivative data | No thermal port` — 基于三个定子绕组电流和转子角度的 4-D 查表参数化，但不带热端口。
- `4-D partial derivative data | Show thermal port` — 基于三个定子绕组电流和转子角度的 4-D 查表参数化，并带热端口。
- `3-D flux linkage data | No thermal port` — 基于磁链数据的 3-D 查表参数化，不带热端口。
- `3-D flux linkage data | Show thermal port` — 基于磁链数据的 3-D 查表参数化，带热端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

**永磁磁通的温度依赖性**

为了计算永磁体的温度依赖性，该模块使用 **Permanent magnet flux temperature coefficient** 参数 *αflux*。此参数确定温度每升高一度时电机磁通减少多少。该模块使用以下方程计算磁通减少因子：

FluxReductionForTemp=1+αflux⋅(TR−Tmeas),

其中 *TR* 是 **HR** 端口处的温度，*Tmeas* 是 **Measurement temperature** 参数的值。在此模块中，磁通随温度线性降低。这种降低导致反电动势和转矩也随温度线性降低相同的量，

EMF=FluxReductionForTemp⋅EMF0τ=FluxReductionForTemp⋅τ0

其中：

- *τ0* 是当转子温度等于 **Measurement temperature** 参数值时的转矩。
- *EMF0* 是当转子温度等于 **Measurement temperature** 参数值时的 EMF。

根据温度调整转矩后，该模块会根据铁耗进一步降低转矩 *τ*。

**定子电阻的温度依赖性**

永磁体温度的升高会改变定子电阻。**Resistance temperature coefficient** 参数 *α* 驱动这种电阻变化：

Ra=Rs⋅[1+α(TA−Tmeas)]Rb=Rs⋅[1+α(TB−Tmeas)]Rc=Rs⋅[1+α(TC−Tmeas)]

其中 *Ra*、*Rb* 和 *Rc* 是每相经温度调整后的电阻，*TA*、*TB* 和 *TC* 是 **HA**、**HB** 和 **HC** 端口处的温度。
