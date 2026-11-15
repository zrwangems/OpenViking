---
type: simulink-block
title: 'Phase Shift Beamformer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Beamforming and Direction of Arrival Estimation / Beamforming'
documentation_page: 'phaseshiftbeamformer'
documentation_source_path: 'ref/phaseshiftbeamformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Shift Beamformer

## 端口

### 输入

### **X** — 输入信号 *M*×*N* 复值矩阵

输入信号，指定为 *M*×*N* 矩阵，其中 *M* 是数据中的样本数，*N* 是阵列单元数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **Ang** — 波束形成方向 `2`×`1` 实值向量 | `2`×*L* 实值矩阵

波束形成方向，指定为 `2`×*L* 实值矩阵，其中 *L* 是波束形成方向的数量。每列采用 `[AzimuthAngle;ElevationAngle]` 的形式。角度单位是度。方位角必须介于 –180° 和 180° 之间（含这两个值），俯仰角必须介于 –90° 和 90° 之间（含这两个值）。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，请将 **波束形成方向来源** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 波束形成输出 *M*×*L* 复值矩阵

波束形成输出，返回为 *M*×*L* 复值矩阵。量 *M* 是信号样本数，*L* 是由 `Beamforming direction` 参数指定或来自 `Ang` 端口的目标波束形成方向数。

**数据类型：** `double`
**复数支持：** Yes

### **W** — 波束形成权重 *N*×*L* 复值矩阵

波束形成权重，返回为 *N*×*L* 复值矩阵。量 *N* 是阵列单元数。当 **指定传感器阵列为** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，*N* 表示子阵列数。*L* 是 `Ang` 端口或 `Beamforming direction (deg)` 属性中指定的目标波束形成方向数。每个波束形成方向有一组权重。

#### 依赖关系

要启用此端口，请选中 **启用权重输出** 复选框。

**数据类型：** `double`
**复数支持：** Yes

## 参数

#### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')` (默认) | 实值正标量

信号传播速度，指定为实值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。单位是米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **工作频率 (Hz)** — 系统工作频率 `3e8` (默认) | 正实标量

系统工作频率，指定为正标量。单位是 Hz。

### **波束形成方向来源** — 波束形成方向来源 `Property` (默认) | `Input port`

波束形成方向来源，指定为 `Property` 或 `Input port`。当您将 **波束形成方向来源** 设置为 `Property` 时，然后使用 **波束形成方向 (deg)** 参数设置方向。当您选择 `Input port` 时，方向由 `Ang` 端口的输入决定。

### **波束形成方向 (deg)** — 波束形成方向 *2*×*L* 实值矩阵

波束形成方向，指定为 *2*×*L* 实值矩阵，其中 *L* 是波束形成方向的数量。每列采用 `[AzimuthAngle;ElevationAngle]` 的形式。角度单位是度。方位角必须介于 –180° 和 180° 之间。俯仰角必须介于 –90° 和 90° 之间。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此参数，请将 **波束形成方向来源** 参数设置为 `Property`。

### **移相器位数** — 移相量化位数 `0` (默认) | 非负整数

用于量化波束形成器或导向矢量权重的移相分量的位数。将位数指定为非负整数。值为零表示不执行量化。

### **权重归一化方法** — 指定权重归一化方法 `Distortionless` (默认) | `Preserve power`

指定此参数以设置权重归一化方法。选择 `Distortionless` 以将波束形成方向上的增益设置为零 dB。选择 `Preserve power` 以将权重的范数设置为 1。

### **启用权重输出** — 输出波束形成器权重的选项 off (默认) | on

选中此复选框以从输出端口 `W` 获取波束形成器权重。

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。该模块在 MATLAB 中运行底层的 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行该模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以在不重新编译的情况下重复执行，但如果您更改任何模块参数，则该模块会在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **指定传感器阵列为** — 指定阵列的方法 `Array (no subarrays)` (默认) | `Partitioned array` | `Replicated subarray` | `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `Partitioned array` — 使用模块参数指定阵列。
- `Replicated subarray` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **表达式** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **指定传感器阵列为** 设置为 `MATLAB expression`。

#### 单元参数

### **单元类型** — 阵列单元类型 `Isotropic Antenna` (默认) | `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风单元的工作频率范围 `[0,1e20]` (默认) | 实值 1×2 行向量

将天线或麦克风单元的工作频率范围指定为 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该单元在此频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风单元的工作频率范围 `[0,1e20]` (默认) | 实值行向量

将设置天线和麦克风频率响应的频率指定为递增实值的 1×*L* 行向量。天线或麦克风单元在该向量的最小和最大元素指定的频率范围之外没有响应。频率单位是 Hz。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 在这些频率处设置响应。

### **遮挡单元背面** — 将 `Isotropic Antenna` 单元或 `Omni Microphone` 单元的背面响应设置为零 off (默认) | on

选中此复选框以遮挡单元的背面响应。当背面被遮挡时，从正侧向偏离 ±90° 以外的所有方位角处的响应都设置为零。正侧向方向定义为 0° 方位角和 0° 俯仰角。

#### 依赖关系

要启用此复选框，请将 **单元类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **余弦方向图指数** — 方位角和俯仰角余弦方向图的指数 `[1.5 1.5]` (默认) | 非负标量 | 非负值的实值 1×2 矩阵

将余弦方向图的指数指定为非负标量或非负值的实值 1×2 矩阵。当 **余弦方向图指数** 是 1×2 向量时，第一个元素是方位角方向上的指数，第二个元素是俯仰角方向上的指数。当您将此参数设置为标量时，方位角方向和俯仰角方向余弦方向图都升到相同的幂。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Cosine Antenna`。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]` (默认) | 实值行向量

自定义天线或自定义麦克风在由 **工作频率向量 (Hz)** 参数定义的频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量的维度匹配。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el` (默认) | `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **俯仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]` (默认) | 实值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须介于 –180° 和 180° 之间（含这两个值），并且严格递增。

#### 依赖关系

要启用此参数，请将 **单元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **俯仰角 (deg)** — 天线辐射方向图的俯仰角 `[-90:90]` (默认) | 实值行向量

将计算辐射方向图的俯仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位是度。俯仰角必须介于 –90° 和 90° 之间（含这两个值），并且严格递增。

#### 依赖关系

要启用此参数，请将 **单元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实值 1×*P* 行向量

指定天线辐射方向图的点的 Phi 角，指定为实值 1×*P* 行向量。*P* 必须大于 2。角度单位是度。Phi 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **单元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实值 1×*Q* 行向量

指定天线辐射方向图的点的 Theta 角，指定为实值 1×*Q* 行向量。*Q* 必须大于 2。角度单位是度。Theta 角必须介于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **单元类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)` (默认) | 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **俯仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*×*P*×*L* 数组，则该数组的每个 *Q*×*P* 页为 **工作频率向量 (Hz)** 参数中指定的 *对应* 频率指定一个方向图。

#### 依赖关系

要启用此参数，请将 **单元类型** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认） | 实值 *Q*-by-*P* 矩阵 | 实值 *Q*-by-*P*-by-*L* 数组

组合天线辐射方向图的相位，指定为 *Q*-by-*P* 矩阵或 *Q*-by-*P*-by-*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*-by-*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的 *所有* 频率。
- 如果该值是 *Q*-by-*P*-by-*L* 数组，则数组的每个 *Q*-by-*P* 页为 **Operating frequency vector (Hz)** 参数中指定的 *对应* 频率指定一个方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法向 `on`（默认） | `off`

选中此复选框可将天线阵元方向图旋转至与阵列法向对齐。未选中时，阵元方向图不进行旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴指向阵列法向。未选中时使用未经旋转的阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴指向阵列法向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认） | 实值标量 | 实值 1-by-*L* 行向量

极坐标方向图麦克风响应频率，指定为实值标量或实值 1-by-*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认） | 实值 -by-*P* 行向量

将极坐标方向图响应角度指定为 1-by-*P* 向量。角度从麦克风中心拾取轴测量，必须介于 –180° 和 180° 之间（含端点）。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认） | 实值 *L*-by-*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*-by-*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数量。*P* 是 **Polar pattern angles (deg)** 中指定的角度数量。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度上测得的极坐标方向图幅度。方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。您可以根据极坐标方向图构建 3-D 空间中的麦克风响应方向图。

#### 依赖项

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何 `ULA`（默认） | `URA` | `UCA` | `Conformal Array`

阵列几何，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆阵
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数 ULA 阵列为 `2`、UCA 阵列为 `5`（默认） | 大于或等于 2 的整数

ULA 或 UCA 阵列的阵列阵元数，指定为大于或等于 2 的整数。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元间距 ULA 阵列为 `0.5`、URA 阵列为 `[0.5,0.5]`（默认） | ULA 或 URA 阵列的正标量 | URA 阵列的 2 元素正值向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或 1-by-2 正值向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认） | `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖项

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认） | 正整数 | 1-by-2 正整数向量

URA 阵列的维度，指定为正整数或 1-by-2 正整数向量。

- 如果 **Array size** 是 1-by-2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列具有相同的行数和列数。
- 当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

对于 URA，阵列阵元沿最左列从上到下索引，然后从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 创建具有三行两列的阵列。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 阵元位置的格点 `Rectangular`（默认） | `Triangular`

URA 阵元位置的格点，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 将所有阵元沿行和列方向对齐。
- `Triangular` — 将矩形格点的偶数行阵元向正行轴方向偏移。位移为沿行维度的阵元间距的一半。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法向方向 URA 阵列为 `x`、UCA 阵列为 `z`（默认） | `y`

阵列法向方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法向方向正交的平面内。阵元视轴方向沿阵列法向方向指向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面。所有阵元视轴向量沿 *x* 轴指向。 |
| `y` | 阵列阵元位于 *zx* 平面。所有阵元视轴向量沿 *y* 轴指向。 |
| `z` | 阵列阵元位于 *xy* 平面。所有阵元视轴向量沿 *z* 轴指向。 |

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认） | 正标量

UCA 阵列半径，指定为正标量。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元位置 `[0;0;0]`（默认） | 3-by-*N* 实值矩阵

共形阵列中阵元的位置，指定为 3-by-*N* 实值矩阵，其中 *N* 是共形阵列中的阵元数。此矩阵的每一列表示阵列局部坐标系中一个阵列阵元的位置 `[x;y;z]`。局部坐标系的原点是 *(0,0,0)*。单位是米。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Element normals (deg)** — 共形阵列阵元法向量的方向 `[0;0]` | 2-by-1 列向量 | 2-by-*N* 矩阵

共形阵列中阵元法向量的方向，指定为 2-by-1 列向量或 2-by-*N* 矩阵。*N* 表示阵列中的阵元数。对于矩阵，每一列以 `[azimuth;elevation]` 形式指定对应阵元相对于局部坐标系的法向方向。局部坐标系使正 *x* 轴与共形阵列的法向方向对齐。如果参数值是 2-by-1 列向量，则所有阵列阵元使用相同的指向方向。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

您可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数表示任意成对阵元通过某些变换不同的排列。这些变换可以组合平移、方位旋转和仰角旋转。但是，不能使用需要绕法向方向旋转的变换。

#### 依赖项

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

### **Taper** — 阵列阵元加权 1（默认） | 复值标量 | 复值行向量

阵元加权，指定为复值标量或复值 1-by-*N* 行向量。在此向量中，*N* 表示阵列中的阵元数。

也称为 *element weights*，加权会乘以阵列阵元响应。加权修改响应的幅度和相位，以减少旁瓣或控制主响应轴。

如果 **Taper** 是标量，则对每个阵元应用相同权重。如果 **Taper** 是向量，则将向量中的权重应用于对应传感器阵元。权重数量必须与阵列的阵元数量匹配。

当您将 **Specify sensor array as** 设置为 `Replicated subarray` 时，此参数适用于每个子阵。

### **Subarray definition matrix** — 定义属于子阵的阵元 logical 矩阵

将子阵选择指定为 *M*-by-*N* 矩阵。*M* 是子阵数量，*N* 是阵列中的阵元总数。矩阵的每一行表示一个子阵，行中的每个条目指示阵元何时属于该子阵。当条目为零时，该阵元不属于该子阵。非零条目表示应用于对应阵元的复值权重。每一行必须至少包含一个非零条目。

每个子阵的相位中心位于子阵几何中心。子阵几何中心取决于 **Subarray definition matrix** 和 **Geometry** 参数。

#### 依赖项

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array`。

### **Subarray steering method** — 指定子阵导引方法 `None`（默认） | `Phase` | `Time`

子阵导引方法，指定为以下之一

- `None`
- `Phase`
- `Time`
- `Custom`

选择 `Phase` 或 `Time` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `Steer` 输入端口。

选择 `Custom` 会在 Narrowband Receive Array、Narrowband Transmit Array、Wideband Receive Array、Wideband Transmit Array 模块、Constant Gamma Clutter 和 GPU Constant Gamma Clutter 模块上打开 `WS` 输入端口。

#### 依赖项

要启用此参数，请将 **Specify sensor array as** 设置为 `Partitioned array` 或 `Replicated subarray`。

### **Phase shifter frequency (Hz)** — 子阵相移频率 `3.0e8`（默认） | 正实值标量

子阵导引移相器的工作频率，指定为正实值标量。单位是 Hz。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Number of bits in phase shifters** — 子阵导引相移量化位数 `0`（默认） | 非负整数

子阵导引相移量化位数，指定为非负整数。值为零表示不执行量化。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Partitioned array` 或 `Replicated subarray`，并将 **Subarray steering method** 设置为 `Phase`。

### **Subarrays layout** — 子阵位置指定 `Rectangular`（默认） | `Custom`

将复制子阵的布局指定为 `Rectangular` 或 `Custom`。

- 当您将此参数设置为 `Rectangular` 时，使用 **Grid size** 和 **Grid spacing** 参数放置子阵。
- 当您将此参数设置为 `Custom` 时，使用 **Subarray positions (m)** 和 **Subarray normals** 参数放置子阵。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`

### **Grid size** — 矩形子阵网格的维度 `[1,2]`（默认）

矩形子阵网格大小，指定为单个正整数或 1-by-2 正整数行向量。

如果 **Grid size** 是整数标量，则阵列在每一行和每一列具有相等的子阵数量。如果 **Grid size** 是形式为 `[NumberOfRows, NumberOfColumns]` 的 1-by-2 向量，则第一个条目是沿每一列的子阵数量。第二个条目是每一行中的子阵数量。行沿局部 *y* 轴，列沿局部 *z* 轴。此图展示了如何使用 **Grid size** 值 `[1,2]` 复制 3-by-2 URA 子阵。

#### 依赖项

要启用此参数，请将 **Sensor array** 设置为 `Replicated subarray`，并将 **Subarrays layout** 设置为 `Rectangular`。

### **Grid spacing (m)** — 矩形网格上子阵之间的间距 `Auto`（默认） | 正实值标量 | 1-by-2 正值向量

子阵的矩形网格间距，指定为正实值标量、1-by-2 正值行向量或 `Auto`。单位是米。

- 如果 **Grid spacing** 是标量，则沿行的间距和沿列的间距相同。
- 如果 **Grid spacing** 是 1-by-2 行向量，则该向量具有形式 `[SpacingBetweenRows,SpacingBetweenColumn]`。第一个条目指定沿列的行间间距。第二个条目指定沿行的列间间距。
- 如果 **Grid spacing** 设置为 `Auto`，复制会在构建完整阵列时保留子阵在行和列两个方向上的阵元间距。仅当您将 **Geometry** 指定为 `ULA` 或 `URA` 时，此选项可用。

#### 依赖项

要启用此参数，请将 **传感器阵列** 设置为 `Replicated subarray`，并将 **子阵布局** 设置为 `Rectangular`。

### **子阵位置 (m)** — 子阵的位置 `[0,0;0.5,0.5;0,0]` (默认) | 3-by-*N* 实值矩阵

子阵在自定义网格中的位置，指定为 3-by-*N* 实值矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列表示阵列局部坐标系中单个子阵的位置。坐标采用 `[x; y; z]` 形式表示。单位是 meters。

#### 依赖项

要启用此参数，请将 **传感器阵列** 设置为 `Replicated subarray`，并将 **子阵布局** 设置为 `Custom`。

### **子阵法线** — 子阵法线向量的方向 `[0,0;0,0]` (默认) | 2-by-*N* 实矩阵

指定阵列中子阵的法线方向。此参数值是 2-by-*N* 矩阵，其中 *N* 是阵列中的子阵数量。矩阵的每一列指定对应子阵的法线方向，形式为 `[azimuth;elevation]`。角度单位是 degrees。角度是相对于局部坐标系定义的。

您可以使用 **子阵位置** 和 **子阵法线** 参数表示任意排列，其中成对的子阵通过某些变换而不同。这些变换可以组合平移、方位角旋转和俯仰角旋转。但是，不能使用需要绕法线旋转的变换。

#### 依赖项

要启用此参数，请将 **传感器阵列** 参数设置为 `Replicated subarray`，并将 **子阵布局** 设置为 `Custom`。

## 所属库

Phased Array System Toolbox / Beamforming

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

窄带相移波束形成器

Phase Shift Beamformer 模块执行延迟求和波束形成。该延迟使用时域中的相移近似进行近似。
