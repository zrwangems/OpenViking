---
type: simulink-block
title: 'Frost Beamformer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Beamforming and Direction of Arrival Estimation / Beamforming'
documentation_page: 'frostbeamformer'
documentation_source_path: 'ref/frostbeamformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Frost Beamformer

## 端口

### 输入

### **X** — 输入信号 *M*×*N* 复数值矩阵

输入信号，指定为 *M*×*N* 矩阵，其中 *M* 是数据中的样本数，*N* 是阵列元素数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形中可能发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **XT** — 训练信号 *M*×*N* 复数值矩阵

输入信号，指定为 *M*×*N* 矩阵，其中 *M* 是数据中的样本数，*N* 是阵列元素数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形中可能发生大小变化。

#### 依赖关系

要启用此端口，请选中 **启用训练数据输入** 复选框。

**数据类型：** `double`
**复数支持：** Yes

### **Ang** — 波束形成方向 `2`×`1` 实数值向量

波束形成方向，指定为采用 `[AzimuthAngle;ElevationAngle]` 形式的 `2`×`1` 实数值向量。角度单位为度。方位角必须位于 –180° 和 180° 之间（含端点），仰角必须位于 –90° 和 90° 之间（含端点）。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此端口，请将 **波束形成方向源** 参数设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 波束形成输出 *M*×1 复数值向量

波束形成输出，以 *M*×1 复数值向量形式返回。量 *M* 是信号样本数。

**数据类型：** `double`
**复数支持：** Yes

### **W** — 波束形成权重 *N*×1 复数值向量

波束形成权重，以 *N*×1 复数值向量形式返回。量 *N* 是阵列元素数。当 **指定传感器阵列方式** 参数设置为 `Partitioned array` 或 `Replicated subarray` 时，*N* 表示子阵列数量。

#### 依赖关系

要启用此端口，请选中 **启用权重输出** 复选框。

**数据类型：** `double`
**复数支持：** Yes

## 参数

#### 主选项卡

### **信号传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 实数值正标量

信号传播速度，指定为实数值正标量。光速的默认值是由 `physconst('LightSpeed')` 返回的值。单位是米每秒。

**示例：** `3e8`

**数据类型：** `double`

### **继承采样率** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **采样率 (Hz)** — 信号的采样率 `1e6`（默认）| 正实数值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **继承采样率** 复选框。

**数据类型：** `double`

### **FIR 滤波器长度** — FIR 滤波器长度 `1`（默认）| 正整数

用于处理每个传感器元素数据的 FIR 滤波器的长度，指定为正整数。

**数据类型：** `double`

### **对角加载因子** — 用于稳定性的对角加载因子 非负标量

将对角加载因子指定为非负标量。对角加载是一种用于实现稳健波束形成性能的技术，尤其是在样本支持较小时。

### **启用训练数据输入** — 启用训练数据的使用 off（默认）| on

选中此复选框以通过输入端口 `XT` 指定额外的训练数据。要使用输入信号作为训练数据，请清除此复选框，这会移除该端口。

### **波束形成方向源** — 波束形成方向源 `Property`（默认）| `Input port`

波束形成方向源，指定为 `Property` 或 `Input port`。当您将 **波束形成方向源** 设置为 `Property` 时，您可以使用 **波束形成方向 (deg)** 参数设置方向。当您选择 `Input port` 时，方向由 `Ang` 端口的输入确定。

### **波束形成方向 (deg)** — 波束形成方向 2×1 实数值向量

波束形成方向，指定为采用 `[AzimuthAngle;ElevationAngle]` 形式的 2×1 实数值向量。角度单位为度。方位角必须位于 –180° 和 180° 之间。仰角必须位于 –90° 和 90° 之间。角度是相对于阵列的局部坐标系定义的。

#### 依赖关系

要启用此参数，请将 **波束形成方向源** 参数设置为 `Property`。

### **启用权重输出** — 输出波束形成器权重的选项 off（默认）| on

选中此复选框以从输出端口 `W` 获取波束形成器权重。

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### 传感器阵列选项卡

### **指定传感器阵列方式** — 指定阵列的方法 `Array (no subarrays)`（默认）| `MATLAB expression`

指定阵列的方法，指定为 `Array (no subarrays)` 或 `MATLAB expression`。

- `Array (no subarrays)` — 使用模块参数指定阵列。
- `MATLAB expression` — 使用 MATLAB 表达式创建阵列。

### **表达式** — 用于创建阵列的 MATLAB 表达式 Phased Array System Toolbox™ 阵列 System object

用于创建阵列的 MATLAB 表达式，指定为有效的 Phased Array System Toolbox™ 阵列 System object。

**示例：** `phased.URA('Size',[5,3])`

#### 依赖关系

要启用此参数，请将 **指定传感器阵列方式** 设置为 `MATLAB expression`。

### **元素类型** — 阵列元素类型 `Isotropic Antenna`（默认）| `Cosine Antenna` | `Custom Antenna` | `Omni Microphone` | `Custom Microphone`

天线或麦克风类型，指定为以下之一：

- `Isotropic Antenna`
- `Cosine Antenna`
- `Custom Antenna`
- `Omni Microphone`
- `Custom Microphone`

### **工作频率范围 (Hz)** — 天线或麦克风元素的工作频率范围 `[0,1e20]`（默认）| 实数值 1×2 行向量

将天线或麦克风元素的工作频率范围指定为采用 `[LowerBound,UpperBound]` 形式的 1×2 行向量。该元素在此频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Isotropic Antenna`、`Cosine Antenna` 或 `Omni Microphone`。

### **工作频率向量 (Hz)** — 自定义天线或麦克风元素的工作频率范围 `[0,1e20]`（默认）| 实数值行向量

将设置天线和麦克风频率响应的频率指定为 1×*L* 递增实数值行向量。天线或麦克风元素在此向量的最小和最大元素指定的频率范围之外没有响应。频率单位为 Hz。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。使用 **频率响应 (dB)** 在这些频率处设置响应。

### **遮挡元素背面** — 将 `Isotropic Antenna` 元素或 `Omni Microphone` 元素的背面响应设置为零 off（默认）| on

选中此复选框可遮挡元素的背面响应。当背面加障板时，偏离视轴 ±90° 以外的所有方位角处的响应都设置为零。视轴方向定义为 0° 方位角和 0° 仰角。

#### 依赖关系

要启用此复选框，请将 **元素类型** 设置为 `Isotropic Antenna` 或 `Omni Microphone`。

### **余弦方向图指数** — 方位和仰角余弦方向图的指数 `[1.5 1.5]`（默认）| 非负标量 | 由非负值组成的实数值 1×2 矩阵

将余弦方向图的指数指定为非负标量或由非负值组成的实数值 1×2 矩阵。当 **余弦方向图指数** 为 1×2 向量时，第一个元素是方位方向上的指数，第二个元素是仰角方向上的指数。当您将此参数设置为标量时，方位方向和仰角方向的余弦方向图都提升到相同的幂。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Cosine Antenna`。

### **频率响应 (dB)** — 天线和麦克风频率响应 `[0,0]`（默认）| 实数值行向量

自定义天线或自定义麦克风在 **工作频率向量 (Hz)** 参数所定义频率处的频率响应。**频率响应 (dB)** 的维度必须与 **工作频率向量 (Hz)** 参数指定的向量的维度匹配。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna` 或 `Custom Microphone`。

### **输入方向图坐标系** — 自定义天线方向图的坐标系 `az-el`（默认）| `phi-theta`

自定义天线方向图的坐标系，指定为 `az-el` 或 `phi-theta`。当您指定 `az-el` 时，使用 **方位角 (deg)** 和 **仰角 (deg)** 参数指定方向图点的坐标。当您指定 `phi-theta` 时，使用 **Phi 角 (deg)** 和 **Theta 角 (deg)** 参数指定方向图点的坐标。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **方位角 (deg)** — 天线辐射方向图的方位角 `[-180:180]`（默认）| 实数值行向量

将计算天线辐射方向图的方位角指定为 1×*P* 行向量。*P* 必须大于 2。方位角必须位于 –180° 和 180° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **仰角 (deg)** — 天线辐射方向图的仰角 `[-90:90]`（默认）| 实数值行向量

将计算辐射方向图的仰角指定为 1×*Q* 向量。*Q* 必须大于 2。角度单位为度。仰角必须位于 –90° 和 90° 之间（含端点），并且严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `az-el`。

### **Phi 角 (deg)** — 自定义天线辐射方向图的 Phi 角坐标 `0:360` | 实数值 1×*P* 行向量

指定天线辐射方向图所在点的 Phi 角，指定为实数值 1×*P* 行向量。*P* 必须大于 2。角度单位为度。Phi 角必须位于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **Theta 角 (deg)** — 自定义天线辐射方向图的 Theta 角坐标 `0:180` | 实数值 1×*Q* 行向量

指定天线辐射方向图所在点的 Theta 角，指定为实数值 1×*Q* 行向量。*Q* 必须大于 2。角度单位为度。Theta 角必须位于 0° 和 360° 之间，并且严格递增。

#### 依赖关系

要启用此参数，请将 **元素类型** 参数设置为 `Custom Antenna`，并将 **输入方向图坐标系** 参数设置为 `phi-theta`。

### **幅度方向图 (dB)** — 组合天线辐射方向图的幅度 `zeros(181,361)`（默认）| 实数值 *Q*×*P* 矩阵 | 实数值 *Q*×*P*×*L* 数组

组合天线辐射方向图的幅度，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **输入方向图坐标系** 参数设置为 `az-el` 时，*Q* 等于 **仰角 (deg)** 参数指定的向量长度，*P* 等于 **方位角 (deg)** 参数指定的向量长度。
- 当 **输入方向图坐标系** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta 角 (deg)** 参数指定的向量长度，*P* 等于 **Phi 角 (deg)** 参数指定的向量长度。

量 *L* 等于 **工作频率向量 (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **工作频率向量 (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页指定 **工作频率向量 (Hz)** 参数中指定的*对应*频率的方向图。

#### 依赖关系

要启用此参数，请将 **元素类型** 设置为 `Custom Antenna`。

### **Phase pattern (deg)** — 自定义天线辐射相位方向图 `zeros(181,361)`（默认）| 实值 *Q*×*P* 矩阵 | 实值 *Q*×*P*×*L* 数组

组合天线辐射方向图的相位，指定为 *Q*×*P* 矩阵或 *Q*×*P*×*L* 数组。

- 当 **Input Pattern Coordinate System** 参数设置为 `az-el` 时，*Q* 等于 **Elevation angles (deg)** 参数指定的向量长度，*P* 等于 **Azimuth angles (deg)** 参数指定的向量长度。
- 当 **Input Pattern Coordinate System** 参数设置为 `phi-theta` 时，*Q* 等于 **Theta Angles (deg)** 参数指定的向量长度，*P* 等于 **Phi Angles (deg)** 参数指定的向量长度。

量 *L* 等于 **Operating frequency vector (Hz)** 的长度。

- 如果此参数是 *Q*×*P* 矩阵，则同一方向图应用于 **Operating frequency vector (Hz)** 参数中指定的*所有*频率。
- 如果该值是 *Q*×*P*×*L* 数组，则数组的每个 *Q*×*P* 页指定 **Operating frequency vector (** 中指定的*对应*频率的方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **MatchArrayNormal** — 将天线阵元旋转到阵列法线 `on`（默认）| `off`

选中此复选框以旋转天线阵元方向图，使其与阵列法线对齐。未选中时，阵元方向图不旋转。

当天线用于天线阵列且 **Input Pattern Coordinate System** 参数为 `az-el` 时，选中此复选框会旋转方向图，使阵元坐标系的 *x* 轴指向阵列法线方向。不选中时使用未经旋转的阵元方向图。

当天线用于天线阵列且 **Input Pattern Coordinate System** 设置为 `phi-theta` 时，选中此复选框会旋转方向图，使阵元坐标系的 *z* 轴指向阵列法线方向。

将此参数与 `URA` 和 `UCA` 阵列的 **Array normal** 参数结合使用。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Antenna`。

### **Polar pattern frequencies (Hz)** — 极坐标方向图麦克风响应频率 1e3（默认）| 实标量 | 实值 1×*L* 行向量

极坐标方向图麦克风响应频率，指定为实标量或实值 1×*L* 向量。响应频率位于 **Operating frequency vector (Hz)** 向量指定的频率范围内。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern angles (deg)** — 极坐标方向图响应角度 `[-180:180]`（默认）| 实值 -by-*P* 行向量

将极坐标方向图响应角度指定为 1×*P* 向量。角度从麦克风中心拾取轴测量，且必须介于 –180° 和 180° 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

### **Polar pattern (dB)** — 自定义麦克风极坐标响应 `zeros(1,361)`（默认）| 实值 *L*×*P* 矩阵

将自定义麦克风阵元极坐标方向图的幅度指定为 *L*×*P* 矩阵。*L* 是 **Polar pattern frequencies (Hz)** 中指定的频率数。*P* 是 **Polar pattern angles (deg)** 中指定的角度数。矩阵的每一行表示在 **Polar pattern frequencies (Hz)** 中指定的对应频率以及 **Polar pattern angles (deg)** 中指定的所有角度处测得的极坐标方向图幅度。该方向图在方位平面中测量。在方位平面中，仰角为 0°，中心拾取轴为 0° 方位角和 0° 仰角。极坐标方向图围绕中心轴对称。可以根据极坐标方向图构造 3-D 空间中的麦克风响应方向图。

#### 依赖关系

要启用此参数，请将 **Element type** 设置为 `Custom Microphone`。

#### 阵列参数

### **Geometry** — 阵列几何 `ULA`（默认）| `URA` | `UCA` | `Conformal Array`

阵列几何，指定为以下之一

- `ULA` — 均匀线阵
- `URA` — 均匀矩形阵列
- `UCA` — 均匀圆形阵列
- `Conformal Array` — 任意阵元位置

### **Number of elements** — 阵列阵元数，对于 ULA 阵列为 `2`，对于 UCA 阵列为 `5`（默认）| 大于或等于 2 的整数

ULA 或 UCA 阵列的阵元数，指定为大于或等于 2 的整数。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `UCA`。

### **Element spacing (m)** — 阵列阵元间距，对于 ULA 阵列为 `0.5`，对于 URA 阵列为 `[0.5,0.5]`（默认）| ULA 或 URA 阵列的正标量 | URA 阵列的正值 2 元素向量

相邻阵列阵元之间的间距：

- ULA — 将阵列中两个相邻阵元之间的间距指定为正标量。
- URA — 将间距指定为正标量或正值 1×2 向量。如果 **Element spacing (m)** 是标量，则行间距和列间距相等。如果 **Element spacing (m)** 是向量，则该向量具有形式 `[SpacingBetweenArrayRows,SpacingBetweenArrayColumns]`。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `ULA` 或 `URA`。

### **Array axis** — ULA 的线性轴方向 `y`（默认）| `x` | `z`

ULA 的线性轴方向，指定为 `y`、`x` 或 `z`。所有 ULA 阵列阵元在局部阵列坐标系中沿此轴均匀间隔。

#### 依赖关系

- 要启用此参数，请将 **Geometry** 设置为 `ULA`。
- 当模块仅支持 ULA 阵列时，也会启用此参数。

### **Array size** — URA 阵列的维度 `[2,2]`（默认）| 正整数 | 正整数的 1×2 向量

URA 阵列的维度，指定为正整数或正整数的 1×2 向量。

- 如果 **Array size** 是 1×2 向量，则该向量具有形式 `[NumberOfArrayRows,NumberOfArrayColumns]`。
- 如果 **Array size** 是整数，则阵列的每一行和每一列具有相同的阵元数。

对于 URA，阵列阵元沿最左侧阵列列从上到下编号，然后从左到右继续到下一列。在此图中，**Array size** 值 `[3,2]` 创建具有三行两列的阵列。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Element lattice** — URA 阵元位置的格点 `Rectangular`（默认）| `Triangular`

URA 阵元位置的格点，指定为 `Rectangular` 或 `Triangular`。

- `Rectangular` — 在行和列方向上对齐所有阵元。
- `Triangular` — 将矩形格点的偶数行阵元向正行轴方向偏移。位移为沿行维度阵元间距的一半。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA`。

### **Array normal** — 阵列法线方向，对于 URA 阵列为 `x`，对于 UCA 阵列为 `z`（默认）| `y`

阵列法线方向，指定为 `x`、`y` 或 `z`。

平面阵列的阵元位于与所选阵列法线方向正交的平面内。阵元视轴方向沿阵列法线方向。

| Array Normal 参数值 | 阵元位置和视轴方向 |
| --- | --- |
| `x` | 阵列阵元位于 *yz* 平面内。所有阵元视轴向量沿 *x* 轴指向。 |
| `y` | 阵列阵元位于 *zx* 平面内。所有阵元视轴向量沿 *y* 轴指向。 |
| `z` | 阵列阵元位于 *xy* 平面内。所有阵元视轴向量沿 *z* 轴指向。 |

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `URA` 或 `UCA`。

### **Radius of UCA (m)** — UCA 阵列半径 0.5（默认）| 正标量

UCA 阵列的半径，指定为正标量。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `UCA`。

### **Element positions (m)** — 共形阵列阵元的位置 `[0;0;0]`（默认）| 实数值的 3×*N* 矩阵

共形阵列中阵元的位置，指定为实数值的 3×*N* 矩阵，其中 *N* 是共形阵列中的阵元数。此矩阵的每一列表示阵元在阵列局部坐标系中的位置 `[x;y;z]`。局部坐标系的原点为 *(0,0,0)*。单位为米。

#### 依赖关系

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Element normals (deg)** — 共形阵列阵元法线向量的方向 `[0;0]` | 2×1 列向量 | 2×*N* 矩阵

共形阵列中阵元法线向量的方向，指定为 2×1 列向量或 2×*N* 矩阵。*N* 表示阵列中的阵元数。如果参数值是矩阵，则每一列以 `[azimuth;elevation]` 形式指定相应阵元相对于局部坐标系的法线方向。局部坐标系将正 *x* 轴与共形阵列的法线方向对齐。如果参数值是 2×1 列向量，则所有阵列阵元使用相同的指向方向。

可以使用 **Element positions (m)** 和 **Element normals (deg)** 参数表示任何这样的排列：其中成对阵元通过某些变换而不同。这些变换可以组合平移、方位旋转和仰角旋转。但是，不能使用需要绕法线方向旋转的变换。

要启用此参数，请将 **Geometry** 设置为 `Conformal Array`。

**数据类型：** `double`

### **Taper** — 阵列阵元锥削 1（默认）| 复标量 | 复值行向量

将阵元锥削指定为复值标量或复值 1×*N* 行向量。在此向量中，*N* 表示阵列中的阵元数。

锥削也称为 *阵元权重*，其乘以阵列阵元响应。锥削修改响应的幅度和相位，以减少旁瓣或控制主响应轴方向。

如果 **Taper** 是标量，则对每个阵元应用相同的权重。如果 **Taper** 是向量，则向量中的权重应用于对应的传感器阵元。权重数必须与阵列的阵元数匹配。

**数据类型：** `double`

## 所属库

Phased Array System Toolbox / Beamforming

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

Frost beamformer

Frost Beamformer 模块实现 Frost 波束形成器。Frost 波束形成器由时域 MVDR 波束形成器后接一组 FIR 滤波器组成。MVDR 波束形成器将波束指向给定方向，而 FIR 滤波器保持输入信号功率。
