---
type: simulink-block
title: 'Solver Configuration'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'solverconfiguration'
documentation_source_path: '../simscape/ref/solverconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Solver Configuration

## 端口

### 守恒端口

### **Port\_1** — 连接端口，无类型 conserving port

Conserving 连接端口。此端口为无类型。你可以通过在任何类型的 conserving 端口之间的连接线上创建分支点，将其连接到物理网络电路中的任意位置。无论连接类型如何，该模块都会为整个物理网络提供求解器设置。

## 参数

### **Equation formulation** — 指定求解器如何处理正弦变量 `Time`（默认）| `Frequency and time`

指定求解器如何处理正弦变量。

使用 `Frequency and time` 值可加速具有单一标称频率的系统的仿真。有关详细信息，请参阅 Frequency and Time Simulation Mode。

### **Index reduction method** — 选择用于求解非线性高指数 DAE 的降指数方法 `Derivative replacement`（默认）| `Projection` | `None`

选择最适合连接到 Solver Configuration 模块的网络的非线性降指数方法：

- `Derivative replacement` — 在此方法中，DAE 的部分内容会被解析微分并附加到原始系统中。对于每个附加方程，都会选择一个导数，并将其替换为一个新的代数变量，称为 *dummy derivative*。有关详细信息，请参阅 https://epubs.siam.org/doi/abs/10.1137/0914043?journalCode=sjoce3。建议从此方法开始。
- `Projection` — 如果 `Derivative replacement` 方法由于动态状态选择问题而失败，请使用此选项。
- `None` — 如果你的模型不包含非线性高指数 DAE，请使用此选项完全绕过非线性降指数并移除分析开销。

### **Start simulation from steady state** — 选择是从初始状态开始仿真，还是从稳态开始仿真 off（默认）| on

默认情况下，当此复选框清除时，仿真会从由初始条件计算得到的初始状态开始。

当你选中此复选框时，求解器会尝试寻找在系统输入保持恒定足够长时间时将会得到的稳态。有关详细信息，请参阅 Initial Conditions Computation。随后仿真会从此稳态开始。

对于与 frequency-and-time 方程公式兼容的模型，当你选中此复选框时，求解器会尝试执行正弦稳态初始化。换句话说，初始化使用 frequency-time 方程执行，然后仿真使用实际方程公式以及 Solver Configuration 模块中选择的其他选项继续进行。有关详细信息，请参阅 Frequency and Time Simulation Mode。

**注意**

在 Configuration Parameters 对话框的 **Data Import/Export** 窗格中使用 **Initial state** 选项会覆盖 **Start simulation from steady state** 选项。

### **Consistency tolerance** — 用于初始条件和瞬态初始化计算的基于状态的容差模式 `Model AbsTol and RelTol`（默认）| `Local tolerance settings`

此参数影响用于计算初始条件和进行瞬态初始化的非线性求解器。选择基于状态的容差来源：

- `Model AbsTol and RelTol` — 使用模型容差设置，即在“配置参数”对话框的**求解器**窗格中指定的**绝对容差**和**相对容差**参数。
- `Local tolerance settings` — 用局部值替换模型容差设置。选择此选项后，**绝对容差**和**相对容差**参数将出现在“求解器配置”模块对话框中。

无论使用模型容差还是局部容差设置，**容差因子**参数都为这些值提供缩放因子。所得值决定在仿真开始时以及每个离散事件之后（例如，由阀门打开、硬停止等引起的不连续）代数约束应被满足的精确程度。

### **Absolute tolerance** — 局部绝对容差 `0.001`（默认）| 正标量

指定用于计算初始条件和进行瞬态初始化的局部值，而不是使用“配置参数”对话框的**求解器**窗格中的**绝对容差**参数。

#### 依赖关系

要启用此参数，请将**一致性容差**设置为 `Local tolerance settings`。

### **Relative tolerance** — 局部相对容差 `0.001`（默认）| 正标量

指定用于计算初始条件和进行瞬态初始化的局部值，而不是使用“配置参数”对话框的**求解器**窗格中的**相对容差**参数。

#### 依赖关系

要启用此参数，请将**一致性容差**设置为 `Local tolerance settings`。

### **Tolerance factor** — 用于绝对容差和相对容差的缩放因子 `0.001`（默认）| 范围 (0,1] 内的标量

此参数为基于状态的绝对容差和相对容差提供缩放因子，无论使用模型容差还是局部容差设置。减小参数值（即收紧容差）可获得更可靠的时间仿真。如果初始条件求解未能收敛，或为了减少计算时间，可增大参数值（即放宽容差）。

### **Use local solver** — 对模型中的物理网络使用基于采样的局部求解器 off（默认）| on

允许使用基于采样的局部求解器，其采样时间由**采样时间**参数指定。在基于采样的仿真中，所有原本为连续的物理网络状态在 Simulink® 中表示为离散状态。求解器每个时间步更新一次状态。此选项对于生成代码或硬件在环 (HIL) 仿真特别有用。

**注意**

如果使用局部求解器，不建议同时使用 Simulink 或 Simulink Control Design™ 线性化工具。

### **Solver type** — 局部求解器用于更新状态的求解器类型 `Backward Euler`（默认）| `Trapezoidal Rule` | `Partitioning`

选择用于更新状态的求解器类型：

- `Backward Euler` — 倾向于抑制振荡，但更稳定，尤其是在增大时间步长时。
- `Trapezoidal Rule` — 比 `Backward Euler` 更能捕捉振荡，但稳定性较差。
- `Partitioning` — 通过将对应于 Simscape 网络的整个方程组划分为一系列较小的方程组级联，从而提高实时仿真速度。并非所有网络都可以进行划分。然而，当系统可以进行划分时，该求解器可显著提高实时仿真速度。有关详细信息，请参阅 Understanding How the Partitioning Solver Works 和 Increase Simulation Speed Using the Partitioning Solver。

无论选择哪种局部求解器，Backward Euler 方法始终会在以下情况下应用：

- 仿真刚开始时。
- 瞬时变化之后，当相应模块发生内部离散变化时。此类变化包括离合器锁定和解锁、阀门执行器打开和关闭，以及 PS Asynchronous Sample & Hold 模块的切换。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框。

### **Sample time** — 局部求解器的采样时间 `0.001`（默认）| 正标量

指定局部求解器采样时间，单位为秒。求解器每个时间步更新一次状态。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框。

### **Partition method** — 选择使用 Partitioning 局部求解器时优先考虑速度还是稳健性 `Robust simulation`（默认）| `Fast simulation`

选择使用 Partitioning 局部求解器时优先考虑速度还是稳健性：

- `Fast simulation` — 通过使用前向 Euler 方案求解大多数微分方程来提高仿真性能。
- `Robust simulation` — 通过使用后向 Euler 方案求解更多方程来提高仿真稳健性。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框，并将 **Solver type** 设置为 `Partitioning`。

### **Partition storage method** — 选择使用 Partitioning 局部求解器时用于存储划分数据的方法 `As needed`（默认）| `Exhaustive`

使用 Partitioning 求解器时，它会连续求解小型切换线性方程。您可以选择存储矩阵逆，以提高仿真性能。然后，如果在后续时间步中检测到相同配置，Partitioning 求解器将使用存储的矩阵逆，而不是重新计算它们。选择用于存储划分数据的方法：

- `As needed` — 在仿真期间根据需要计算矩阵逆。此方法不需要那么多内存，但可能导致性能尖峰。
- `Exhaustive` — 在仿真前计算并存储矩阵逆。此方法可提高仿真性能，但需要更多内存。使用 **Partition memory budget [kB]** 参数指定用于存储数据的最大允许内存预算。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框，并将 **Solver type** 设置为 `Partitioning`。

### **Partition memory budget [kB]** — 用于存储划分数据的 exhaustive 方法的内存预算 `1024`（默认）| 正标量

指定允许用于存储缓存划分数据的最大内存预算，单位为 kB。如果超出此预算，仿真将报错。您可以根据可用内存资源以及 Statistics Viewer 中的 **Total memory estimate** 数据调整默认值。有关详细信息，请参阅 Partitioning Solver Statistics。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框。将 **Solver type** 设置为 `Partitioning`，并将 **Partition storage method** 设置为 `Exhaustive`。

### **Resolve indeterminate equations during runtime** — 应用运行时正则化以求解静不定系统，on（默认）| off

某些模型配置（例如并联离合器锁定或电流传感器并联连接）允许无限多个解，这使得它们成为静不定系统。正则化是一种将具有不定 Through 变量的模型转换为可求解系统的变换。默认情况下，如果求解器遇到静不定系统，它会应用运行时正则化来求解。

如果您的模型不包含具有无损并联流动路径的配置，您可以清除 **Resolve indeterminate equations during runtime** 复选框以加快仿真速度。

#### 依赖关系

要启用此复选框，请选中 **Use local solver** 复选框，并将 **Solver type** 设置为 `Backward Euler` 或 `Trapezoidal Rule`。

### **Use fixed-cost runtime consistency iterations** — 固定成本仿真选项，off（默认）| on

是否以固定成本计算瞬态初始化和求解器阶段。选中此参数后，您可以指定瞬态初始化和求解器计算的非线性迭代次数和模式迭代次数。如果系统在执行指定迭代次数后未收敛，求解器将忽略失败并继续执行下一步。

如果清除此复选框，系统将使用更稳健但更耗时的算法，执行达到收敛所需的尽可能多的迭代，并在瞬态初始化时未能达到收敛时抛出错误。

有关详细信息，请参阅 Fixed-Cost Simulation。

### **Nonlinear iterations** — 瞬态初始化的牛顿迭代次数，`3`（默认）| 正整数

指定在瞬态初始化时执行的牛顿迭代次数。您可以使用 `simscape.getLocalSolverFixedCostInfo` 函数来查找每步所需的迭代次数，以作为固定步长、固定成本仿真运行。

#### 依赖关系

要启用此参数，请选中 **Use fixed-cost runtime consistency iterations** 复选框。

### **Mode iterations** — 瞬态初始化的模式迭代次数，`2`（默认）| 正整数

指定在瞬态初始化时执行的模式迭代次数。

#### 依赖关系

要启用此参数，请选中 **Use fixed-cost runtime consistency iterations** 复选框并清除 **Use local solver** 复选框。使用局部求解器时，每步仅执行一次主模式更新，因此如果选中了 **Use local solver** 复选框，此参数不可用。

### **Compute impulses** — 允许您管理瞬态初始化期间脉冲检测的计算成本，off（默认）| on

允许您管理瞬态初始化期间脉冲检测的计算成本，适用于全局求解器和局部求解器。

基于事件的状态重新初始化和脉冲处理方法允许您对物理现象（如碰撞和弹跳球）进行建模，并为此类模型显著提升仿真速度。然而，脉冲检测会增加瞬态初始化的成本。此成本与达到收敛所执行的脉冲迭代次数成正比。

如果选中 **Compute impulses** 复选框，您可以指定在瞬态初始化期间执行的脉冲迭代次数。如果系统在达到这些次数后未收敛，它将忽略失败并继续执行下一步。

如果清除此复选框，系统将计算脉冲达到收敛所需的尽可能多的次数。

#### 依赖关系

要启用此复选框，请选中 **Use fixed-cost runtime consistency iterations** 复选框。

### **Impulse iterations** — 瞬态初始化的脉冲迭代次数 `2`（默认）| 正整数

指定在瞬态初始化时执行的脉冲迭代次数。如果系统在达到这些次数后仍未收敛，则忽略该失败并进入下一步。

#### 依赖关系

要启用此参数，请选中 **Compute impulses** 复选框。

### **Maximum threads for function evaluation** — 使用多线程加速 Backward Euler 求解器的 Newton 迭代 `1`（默认）| 正整数

指定在实时仿真中使用 Backward Euler 求解器时函数求值的最大线程数。实际使用的线程数是不超过该参数值的最近的 2 的幂。例如，如果将该参数值指定为 `5`，则求解器使用 4 个线程。默认值 `1` 对应于单线程函数求值。

要使用多线程函数求值，必须清除 **Resolve indeterminate equations during runtime** 复选框。如果选中 **Resolve indeterminate equations during runtime** 复选框，求解器会发出警告并切换为单线程函数求值。

其他不支持的仿真模式包括频率-时间仿真、延迟、可扩展编译、加速器模式和快速加速器模式。您可以使用 Simulink Real-Time™ 生成代码，但不支持其他类型的代码生成。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框，将 **Local solver** 参数设置为 `Backward Euler`，并选中 **Use fixed-cost runtime consistency iterations** 复选框。

### **Linear Algebra** — 指定求解器如何处理矩阵 `auto`（默认）| `Sparse` | `Full`

指定求解器如何处理矩阵：

- `auto` — 求解器自动选择适当的选项（稀疏或满矩阵）来处理矩阵。
- `Sparse` — 求解器将矩阵视为稀疏矩阵。
- `Full` — 求解器将矩阵视为满矩阵。

### **Number of threads (specify n for 2^n)** — 使用多线程线性代数加速多核机器上的桌面仿真 `0`（默认）| 正整数

通过提供 2 的整数指数来指定多线程线性代数的线程数。线程数等于 2 的该参数值次幂。默认值 `0` 对应于单线程线性代数。

对于小型模型，使用大于 0 的数值的多线程算法可能比单线程更慢。

#### 依赖关系

要启用此参数，请选中 **Use local solver** 复选框，并将 **Linear algebra** 参数设置为 `Sparse`。对于全局求解器，Simulink 在不使用 Simscape 线性代数算法的情况下求解方程。

### **Delay memory budget [kB]** — 处理延迟的内存预算 `1024`（默认）| 正标量

指定在仿真包含 Delays 库中的模块或使用 `delay` Simscape 语言构造的自定义模块的模型时，允许用于处理延迟的最大内存预算（以 kB 为单位）。此参数的目的是防止过度的内存交换。如果超出此预算，仿真将报错。您可以根据可用的内存资源调整此值。

### **Apply filtering at 1-D/3-D connections when needed** — 在需要时对 1-D/3-D 连接应用滤波 — 自动提供 Simscape Multibody™ 模块所需的附加导数 on（默认）| off

此选项仅适用于将 Simscape Multibody 库中的模块连接到 Simscape 模块，或连接到其他附加产品模块的模型。使用 Statistics Viewer 确定您的模型是否具有 1-D/3-D 连接。有关详细信息，请参阅 1-D/3-D Interface Statistics。

当 Simscape Multibody 模块直接连接到 Simscape 网络时，网络求解可能需要附加导数。选中此复选框后，求解器会自动对进入 Simulink-PS Converter 模块的信号应用输入滤波，以获得此附加导数。**Filtering time constant** 参数提供延迟的时间常数。

**注意**

此复选框默认处于选中状态。如果清除它，并且 1-D/3-D 连接需要附加导数，求解器将发出错误消息。

### **Filtering time constant** — 延迟的时间常数，以秒为单位 `0.001`（默认）| 正标量

此参数指定用于 1-D/3-D 连接自动输入滤波的滤波时间常数，以秒为单位。该参数值全局应用于属于包含此 Solver Configuration 模块的网络的所有连接。

#### 依赖关系

要启用此参数，请选中 **Apply filtering at 1-D/3-D connections when needed** 复选框。

#### Multibody

### **Use local solver** — 对 Simscape Multibody 网络使用基于样本的局部求解器 off（默认）| on

允许您对连接的 Simscape Multibody 网络使用基于样本的局部求解器。对于具有简单 Simscape Multibody 网络的复杂 Simulink 模型，使用局部求解器可以降低计算成本。使用局部求解器的 Simscape Multibody 网络对于全局 Simulink 求解器而言，就如同它具有离散状态一样。局部求解器每个时间步更新一次状态。

**注意**

此设置独立于模块对话框主体部分中的 **Use local solver** 设置，后者适用于连接到该模块的 Simscape 网络。

### **Solver type** — 局部求解器用于更新 Simscape Multibody 网络中状态的求解器类型 `First-order explicit formula`（默认）| `Second-order explicit formula` | `Third-order explicit formula` | `Fourth-order explicit formula` | `Fifth-order explicit formula` | `Eight-order explicit formula`

选择用于更新 Simscape Multibody 网络中状态的求解器类型：

- `First-order explicit formula` — 显式固定步长求解器，使用与 `ode1` 相同的数学方程。
- `Second-order explicit formula` — 显式固定步长求解器，使用与 `ode2` 相同的数学方程。
- `Third-order explicit formula` — 显式固定步长求解器，使用与 `ode3` 相同的数学方程。
- `Fourth-order explicit formula` — 显式固定步长求解器，使用与 `ode4` 相同的数学方程。
- `Fifth-order explicit formula` — 显式固定步长求解器，使用与 `ode5` 相同的数学方程。
- `Eight-order explicit formula` — 显式固定步长求解器，使用与 `ode8` 相同的数学方程。

#### 依赖关系

要启用此参数，请在 **Multibody** 部分中选中 **Use local solver** 复选框。

### **Sample time** — Multibody 局部求解器的采样时间 `0.001`（默认）| 正标量

指定 Multibody 局部求解器采样时间，以秒为单位。求解器每个时间步更新一次连接的 Simscape Multibody 网络的状态。

#### 依赖关系

要启用此参数，请在 **Multibody** 部分中选中 **Use local solver** 复选框。

## 所属库

Simscape / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2024a: 独立于固定成本仿真控制运行时正则化

Solver Configuration 模块中的 **Resolve indeterminate equations** 复选框用于应用运行时正则化以求解静态不定系统，现已重命名为 **Resolve indeterminate equations at runtime**，并移至对话框的不同部分。以前，您需要选中 **Use fixed-cost runtime consistency iterations** 复选框才能启用它。现在，要启用 **Resolve indeterminate equations at runtime** 复选框，您需要选中 **Use local solver** 复选框，并将 **Solver type** 设置为 `Backward Euler` 或 `Trapezoidal Rule`。除非您的模型包含无损并联流动路径（例如理想并联离合器或开关），否则您现在可以清除 **Resolve indeterminate equations at runtime** 复选框，并在使用这些类型的局部求解器时加快仿真速度，无论仿真是否为固定成本。

您不能再对全局求解器关闭运行时正则化。

### R2023b: 多体局部求解器

新的 **Multibody** 部分包含特定于求解所连接的 Simscape Multibody 网络的设置和参数。**Use local solver** 复选框允许您通过将 Simscape Multibody 网络表示为具有离散状态来降低计算成本。此部分中的 **Solver type** 和 **Sample time** 参数仅适用于 Multibody 局部求解器。

### R2022b: 指定一致性容差的新方法

该模块使用基于状态的绝对和相对一致性容差，乘以缩放因子，来计算初始条件和进行瞬态初始化。**Consistency tolerance** 参数允许您在模型容差或局部容差设置之间进行选择。新的 **Tolerance factor** 参数为这些值提供缩放因子。这种基于状态的方法提供了更好的鲁棒性和效率，特别是在与按标称值缩放模型结合使用时。

在以前的版本中，**Consistency tolerance** 参数具有数值，并且该模块使用基于方程残差容差的非线性求解器来初始化模型。

如果您打开一个现有模型，其中 **Consistency tolerance** 参数具有数值，则该模型将继续使用与以前版本相同的基于残差的计算方法。您的仿真结果不会改变。

要将现有模型升级为使用基于状态的方法，请使用 Upgrade Advisor 中的 **Check Simscape use of state-based consistency tolerances** 检查。

### R2022b: 固定成本仿真的多线程函数求值

如果您的模型使用 Backward Euler 局部求解器，则计算 Newton 迭代非常耗时，并且可能会给固定成本仿真带来问题。您可以使用多线程函数求值，通过使用新的 **Maximum threads for function evaluation** 参数并清除新的 **Resolve indeterminate equations** 复选框，在多核机器上加快仿真速度。

在以前的版本中，求解器使用单线程函数求值，并且始终应用运行时正则化。**Maximum threads for function evaluation** 参数和 **Resolve indeterminate equations** 复选框的默认值等同于以前版本中使用的算法。

## 描述

物理网络环境和求解器配置

每个由连接的 Simscape™ 模块图表示的物理网络都需要求解器设置信息才能进行仿真。Solver Configuration 模块指定了模型在开始仿真之前所需的求解器参数。

每个拓扑上不同的 Simscape 模块图都需要恰好一个 Solver Configuration 模块连接到它。
