---
type: simulink-block
title: 'Sensorless Six-Step Commutation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'sensorlesssixstepcommutation'
documentation_source_path: 'ref/sensorlesssixstepcommutation.html'
language: zh-CN
chinese_source: worker-translation
---

# Sensorless Six-Step Commutation

## 端口

### 输入

### **StartDir** — 电机旋转方向 +1 | -1

电机旋转方向。

**数据类型：** `int16`

### **VabcMeas** — 测量的电机端子电压向量

测量的电机端子电压（A、B、C），单位为伏特。

**数据类型：** `single` | `double` | `fixed point`

### **VdcMeas** — 测量的直流母线电压向量

测量的直流母线电压，单位为伏特。

**数据类型：** `single` | `double` | `fixed point`

### **DutyRef** — 参考占空比输入 标量 | [0,1]

参考占空比输入，即速度控制器或电流控制器的输出，范围为 0 到 1。

**数据类型：** `single` | `double` | `fixed point`

### **[Tf,Td]** — 滤波器时间延迟和退磁时间延迟 向量

滤波器延迟时间和退磁时间延迟（单位为秒），指定为向量，需予以考虑。该输入补偿由于使用硬件或软件滤波器而在电压（Vabc）测量中引入的延迟，以及防止检测到虚假过零点所需的延迟。

#### 依赖关系

要启用此端口，请将 **Compensation for filter delay (Tf) and demagnetization time (Td)** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 启用或禁用该模块 标量

启用或禁用该模块以执行六步换相。

**数据类型：** `Boolean`
### 输出

### **Duty** — 使用六步换相模式的六个开关的占空比 标量

驱动电机的定子相 *a*、*b* 和 *c* 电压。数据类型与输入 DutyRef 相同。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 基于 BEMF（反电动势）过零检测检测到的角速度 标量

基于 BEMF（反电动势）过零检测检测到的角速度。

**数据类型：** `single` | `double` | `fixed point`

### **Info** — 用于测试或调试的信号信息 总线

用于测试或调试的信号信息，可使用点表示法访问。此总线输出的信号可使用总线选择器访问，它提供以下值：

- `Info.StateAlignment` – 如果电机处于 Alignment 阶段（模块中的 Operating mode selection 设置为 **Alignment**），则返回 1
- `Info.StateOpenLoop` – 如果电机处于开环运行状态（模块中的 Operating mode selection 设置为 **Alignment -> Open-loop run** 且电机已开始开环运行），则返回 1
- `Info.StateAcquisition` – 如果电机处于开环运行状态（模块中的 Operating mode selection 设置为 **Alignment -> Open-loop run**）且控制器正在采集用于检测反电动势过零点的信号，则返回 1
- `Info.OpenLoopSwitchState` – 返回逆变器中活动开关状态的信息。此信号提供逆变器中哪两个开关已接通的信息。六步换相在一个电气周期内具有六个状态（编号从 1 到 6）。
- `Info.EnableCommutation` – 如果电机通过正确检测过零点处于受控换相状态（模块中的 Operating mode selection 设置为 **Alignment -> Open-loop run -> Controlled commutation**），则返回 1
- `Info.Counter30deg` – 计数器，保存给定电机转速下检测 30 电角度所需的时间采样数
- `Info.FilterDelayinSamples` – 滤波器延迟输入转换为时间采样数 `n`（n = Tf/Ts，其中 Ts 为模块采样时间，Tf 为电压检测滤波器引起的时间延迟）
- `Info.DemagTimeinSamples` – 退磁时间输入转换为时间采样数 `n`（n = Td/Ts，其中 Ts 为模块采样时间，Td 为退磁时间）

**数据类型：** `uint16`

### **ComStatus** — 指示模块正在从开环切换到受控六步换相逻辑

当反电动势过零检测成功时，指示模块正在从开环切换到受控六步换相（返回 1）。

**数据类型：** `Boolean`

## 参数

### **Alignment** — 通过检查转子对齐来确定初始转子位置 `off`（默认）| `on`

通过检查转子对齐来确定初始转子位置的选项。选择此选项将打开 **Alignment** 窗格以指定相关参数。

电机对齐阶段为电机的两相（a 相和 b 相）通电。产生的磁场迫使转子对齐在距 a 相轴 -30 度（电角度）的位置。

### **Alignment -> Open-loop run** — 通过以开环方式启动电机来确定转子位置 `off`（默认）| `on`

通过以开环方式启动电机来确定转子位置的选项。选择此选项将打开 **Open loop** 窗格以指定相关参数。

在选择 **Alignment -> Open-loop run** 选项后运行模型，会按顺序为电机的后续各相通电（以六步模式使用预定义的加速度），以拖动转子并在空载或低载条件下运行，使其逐渐增加电机转速。开环阶段用于将电机转速提升至能够产生足够可精确测量的反电动势的值。

### **Alignment -> Open-loop run -> Controlled commutation** — 通过以闭环方式运行电机来确定转子位置 `on`（默认）| `of`

通过以闭环方式运行电机来确定转子位置的选项。选择此选项将打开 **Controlled commutation** 窗格以指定相关参数。

在选择 **Alignment -> Open-loop run -> Controlled commutation** 选项后运行模型，会检测电机反电动势过零点，以精确生成施加到 BLDC 电机各相的六步换相模式（以占空比的形式）。

在使用开环六步控制运行电机并完成转速获取后，您可以使用闭环受控换相运行电机

### **Number of motor pole pairs** — 电机极对数 `4`（默认）| 标量

电机极对数。

### **Discrete step size (s)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

模块每两次连续执行之间的固定时间间隔（以秒为单位）。

#### Alignment

### **Alignment duty cycle** — 要施加在 A 相和 B 相之间的电压占空比 `0.3`（默认）| 标量

要施加在 A 相和 B 相之间的电压占空比，用于将转子对齐在相对于 A 相 -30 度（电角度）的位置（作为 **Alignment** 阶段的一部分）。

### **Alignment time** — 在 A 相和 B 相之间施加电压的持续时间 `0.5`（默认）| 标量

在 A 相和 B 相之间施加电压的持续时间（以秒为单位），用于指定转子从初始未知位置移动到相对于 a 相 -30 度的已知位置所需的时间（作为 **Alignment** 阶段的一部分）。此参数取决于电机参数以及 **Alignment duty cycle** 参数的值。

#### Open-Loop

### **Open-loop duty cycle (range: [0,1])** — 要施加到所有三相的电压占空比 `0.4`（默认）| 标量

要施加到所有三相的电压占空比，用于以开环方式运行电机（作为 **Alignment –-> Open-loop run** 阶段的一部分）。电压必须足够大以拖动转子并在空载或低载条件下运行，使其逐渐增加电机转速。

### **Target open-loop speed (RPM)** — 开环运行期间为生成足够反电动势而要达到的目标转速（RPM） `800`（默认）| 标量

转子在开环运行期间为生成足够反电动势而要达到的目标转速（RPM）。

### **Ramp up time to reach target open-loop speed (s)** — 达到 Target open-loop speed 所指定 RPM 值的斜坡上升时间（s） `0.7`（默认）| 标量

在开环运行期间，达到你为 **Target open-loop speed** 参数指定的 RPM 值所需的斜坡上升时间（s）。
这两个参数值共同决定转子在开始开环阶段时的加速度。

### **Open-loop speed to initiate transition to controlled commutation (RPM)** — 在开环阶段算法开始电机相电压采集过程时的转速 `500`（默认）| 标量

在开环阶段算法开始电机相电压采集过程时的转速。该值定义了算法必须开始检测过零点以计算电机转速的转速下限。确保将该值设置为小于 **Target open-loop speed** 参数的值。

#### Controlled Commutation

### **Speed samples required to complete transition to controlled commutation** — 在转换到受控换相阶段之前要考虑的最小转速采样数 `10`（默认）| 标量

在转换到受控换相阶段之前，用于与 **Open-loop speed to initiate transition to controlled commutation** 参数所定义的转速进行比较的最小转速采样数。

为该参数定义正确的值可确保电机在转换到闭环控制之前达到并保持在最低转速以上，以生成足够的反电动势（用于准确检测过零点）。

### **Compensation for filter delay (Tf) and demagnetization time (Td)** — 指定两种方法之一来定义对 Tf 和 Td 的补偿 `Specify via dialog`（默认）| `Input port`

指定定义对 Tf 和 Td 补偿的方法之一。指定时间延迟允许该模块补偿测量电压中引入的这些已知时间延迟。否则，该时间延迟将导致过零点检测延迟，还会导致生成错误的换相模式，可能造成电机堵转。

### **Time delay due to voltage sense filter, Tf (s)** — 用于补偿电压测量所用硬件或软件滤波器延迟的时间延迟 `450e-6`（默认）| 标量

用于补偿电压测量所用硬件或软件滤波器（滤波器类型可以不同，且滤波器可位于电路或代码中）延迟的时间延迟。为该参数提供正确的值可确保该模块能够生成准确的换相序列而不产生相位延迟。

### **Demagnetization time, Td (s)** — 绕组正在退磁且不应采集电压信号的时间 `175e-6`（默认）| 标量

绕组正在退磁且不应采集电压信号的时间，用于防止虚假的过零点检测。它也被定义为从定子相退磁发生的时间点到反电动势越过过零点线的时间点之间的等待时段。

## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2025a 中引入**

## 描述

使用六步换相通过无传感器控制运行 BLDC 电机或 PMSM

Sensorless Six-Step Commutation 模块使用六步换相，通过无传感器控制运行无刷直流（BLDC）电机或永磁同步电机（PMSM）。

该模块使用 V`abc`Meas（测量的端子电压）和 V`dc`Meas（直流母线电压）输入，为逆变器的六个开关生成占空比。您可以将运行模式选择为 **Alignment**、**Alignment -> Open-loop run** 或 **Alignment -> Open-loop run -> Controlled commutation**。

无传感器六步换相中的 `Alignment` 阶段用于初始化 BLDC 电机的转子位置，以便其能够正确启动。该方法将特定电压施加到电机 A 相和 B 相，使转子被迫对齐到已知位置（相对于 A 相为 -30 电角度）。

无传感器六步换相中的 `Open-loop run` 阶段用于使电机达到某一转速，以产生足够的反电动势，从而可用于检测反电动势的过零点（该转速的推荐值可为电机额定转速的 10 - 30%）。在此阶段，您需要提供电压幅值（Open-loop duty cycle）和加速度作为输入。所施加电压的频率（或电机转速）根据另一组输入——斜坡上升时间和目标开环转速——线性增加。最初，向所有三相施加电压，并缓慢增加所施加电压的频率。转子预期会与所施加电压同步，并以指定转速持续旋转。该模块获取端子电压并检测电机反电动势的过零点。这些检测用于计算电机的实际转速，并指示已准备好进入受控换相状态。

在最后阶段，`Controlled commutation`，转速和六步换相时刻根据反电动势过零检测被准确确定。所施加的磁场超前转子 60-120 度（电角度）。此行为与使用霍尔传感器进行六步换相时所能实现的行为相同。该模块在每个 60 度扇区期间使用休眠电机相中反电动势的过零点来确定休眠相激活的时刻。它在过零点上增加 30 度偏移，以在正确时刻开启休眠相（并关断其他相之一）。

**注意**

默认情况下，该模块使用 `Controlled commutation` 阶段，该阶段使用各参数的默认预填充值。但是，您可以通过使用在同一模块中选择其他两个阶段的选项来遵循顺序工作流，这也有助于在进入 `Controlled commutation` 阶段之前，获得针对您电机的所有所需参数的派生值。例如，您可以遵循以下顺序：

1. 选择 `Alignment` 阶段并部署模型以运行电机，并获得与该阶段相关的派生值。
2. 选择 `Open-loop run` 阶段，使用来自 `Alignment` 阶段的派生值，并部署模型以运行电机，并获得与 `Open-loop run` 阶段相关的派生值。
3. 选择 `Controlled Commutation` 阶段，使用来自 `Alignment` 和 `Open-loop run` 阶段的派生值，并部署模型以在受控换相下运行电机。
