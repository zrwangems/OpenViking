---
type: simulink-block
title: 'Ideal Fixed Gear Transmission'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Transmission'
documentation_page: 'idealfixedgeartransmission'
documentation_source_path: 'ref/idealfixedgeartransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Fixed Gear Transmission

## 端口

### 输入

### **Gear** — 要接合的挡位编号 `scalar`

要接合的挡位编号的整数值，*Gcmd*。

### **EngTrq** — 施加的输入扭矩 `scalar`

施加的输入扭矩，*Ti*，通常来自发动机曲轴或双质量飞轮减振器，单位为 N·m。

### **DiffTrq** — 施加的负载扭矩 `scalar`

施加的负载扭矩，*To*，通常来自差速器，单位为 N·m。

### **Temp** — 油温 `scalar`

油温，单位为 K。为确定效率，模块使用一个 4D 查找表，该表是以下各项的函数：

- 挡位
- 输入扭矩
- 输入速度
- 油温

#### 依赖项

要启用此端口，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `Eng` | `EngTrq` | | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 | *Ti* | N·m |
| `EngSpd` | | 施加的驱动轴角速度输入 | *ωi* | rad/s |
| `Diff` | `DiffTrq` | | 施加的负载扭矩，通常来自差速器 | *To* | N·m |
| `DiffSpd` | | 驱动轴角速度输出 | *ωo* | rad/s |
| `Trans` | `TransSpdRatio` | | 时间 t 的输入输出速度比 | *Φ(t)* | N/A |
| `TransEta` | | 输出功率与输入功率之比 | *ηN* | N/A |
| `TransGearCmd` | | 命令挡位 | *Ncmd* | N/A |
| `TransGear` | | 接合挡位 | *N* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | 发动机功率 | *Peng* | W |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrEffLoss` | 机械功率损失 | *Peffloss* | W |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | W |
| `PwrStored` | `PwrStoredTrans` | 旋转动能变化率 | *Pstr* | W |

### **EngSpd** — 角速度 `scalar`

施加的驱动轴角速度输入，*ωi*，单位为 rad/s。

### **DiffSpd** — 角速度 `scalar`

驱动轴角速度输出，*ωo*，单位为 rad/s。

## 参数

### **Efficiency factors** — 指定效率计算 `Gear only`（默认） | `Gear, input torque, input speed, and temperature`

要指定模块效率计算，请在 **Efficiency factors** 中选择以下任一选项。

| 设置 | 模块实现 |
| --- | --- |
| `Gear only` | 效率由基于挡位的一维查找表确定。 |
| `Gear, input torque, input speed, and temperature` | 效率由基于以下内容的 4D 查找表确定：  - 挡位 - 输入扭矩 - 输入速度 - 油温 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TransEffModelPopup` |
| **值：** | `Gear only`（默认） | `Gear, input torque, input speed, and temperature` |
| **数据类型：** | `character vector` |

#### 依赖项

| 将参数设置为 | 启用 |
| --- | --- |
| `Gear only` | **Efficiency vector, eta** |
| `Gear, input torque, input speed, and temperature` | **Efficiency torque breakpoints, Trq\_bpts**  **Efficiency speed breakpoints, omega\_bpts**  **Efficiency temperature breakpoints, Temp\_bpts**  **Efficiency lookup table, eta\_tbl** |

### **Gear property interpolation method** — 插值 `Nearest`（默认） | `Linear` | `Flat` | `Cubic spline`

模块在换挡期间用于切换传动比的方法。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gearInterp` |
| **值：** | `Nearest`（默认） | `Linear` | `Flat` | `Cubic spline` |
| **数据类型：** | `character vector` |

#### 变速器

### **Gear number vector, G** — 指定变速器挡位数 `[-1,0,1,2,3,4,5]`（默认） | `vector`

用于指定变速器挡位数的整数挡位命令向量。空挡为 `0`。例如，可以设置以下参数值。

| 要指定 | 将 **Gear number, G** 设置为 |
| --- | --- |
| 四个变速器挡位，包括空挡 | `[0,1,2,3,4]` |
| 三个变速器挡位，包括空挡和倒挡 | `[-1,0,1,2,3]` |
| 五个变速器挡位，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G` |
| **值：** | `[-1,0,1,2,3,4,5]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Efficiency torque breakpoints, Trq\_bpts** — 断点 `[25,50,75,100,150,200,250]`（默认） | `vector`

效率表的扭矩断点。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25,50,75,100,150,200,250]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认） | `vector`

效率表的速度断点，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 断点 `[313 358]`（默认） | `vector`

效率表的温度断点。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[313 358]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Gear ratio vector, N** — 输入速度与输出速度之比 `[-4.47,4.47,4.47,2.47,1.47,1,0.8]`（默认） | `vector`

传动比（即输入速度与输出速度之比）向量，其索引对应于 **Gear number, G** 中指定的传动比。对于空挡，将传动比设置为 `1`。例如，可以设置以下参数值。

| 要为以下项指定传动比 | 将 **Gear number, G** 设置为 | 将 **Gear ratio, N** 设置为 |
| --- | --- | --- |
| 四个变速器挡位，包括空挡 | `[0,1,2,3,4]` | `[1,4.47,2.47,1.47,1]` |
| 五个变速器挡位，包括空挡和倒挡 | `[-1,0,1,2,3,4,5]` | `[-4.47,1,4.47,2.47, 1.47,1,0.8]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N` |
| **值：** | `[-4.47,4.47,4.47,2.47,1.47,1,0.8]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Inertia vector, Jout** — 挡位转动惯量 `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认） | `vector`

挡位转动惯量 *JN* 的向量，其索引对应于 **Gear number, G** 中指定的转动惯量，单位为 kg\*m^2。例如，可以设置以下参数值。

| 要为以下项指定转动惯量 | 将 **Gear number, G** 设置为 | 将 **Inertia, J** 设置为 |
| --- | --- | --- |
| 四个挡位，包括空挡 | `[0,1,2,3,4]` | `[0.01,2.28,2.04, 0.32,0.028]` |
| 五个挡位的转动惯量，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[2.28,0.01,2.28, 2.04,0.32,0.028,0.01]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jout` |
| **值：** | `[0.128 0.01 0.128 0.1 0.062 0.028 0.01]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Damping vector, bout** — 挡位粘性阻尼系数 `[.003 .001 .003 .0025 .002 .001 .001]`（默认） | `vector`

挡位粘性阻尼系数 *bN* 的向量，其索引对应于 **Gear number, G** 中指定的系数，单位为 N·m·s/rad。例如，可以设置以下参数值。

| 要为以下项指定阻尼 | 将 **Gear number, G** 设置为 | 将 **Damping, b** 设置为 |
| --- | --- | --- |
| 四个挡位，包括空挡 | `[0,1,2,3,4]` | `[0.001,0.003, 0.0025,0.002,0.001]` |
| 五个挡位，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.003,0.001, 0.003,0.0025, 0.002,0.001,0.001]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bout` |
| **值：** | `[.003 .001 .003 .0025 .002 .001 .001]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Efficiency vector, eta** — 挡位效率 `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]`（默认） | `vector`

挡位机械效率 *ηN* 的向量，其索引对应于 **Gear number, G** 中指定的效率。例如，可以设置以下参数值。

| 要为以下项指定效率 | 将 **Gear number, G** 设置为 | 将 **Efficiency, eta** 设置为 |
| --- | --- | --- |
| 四个挡位，包括空挡 | `[0,1,2,3,4]` | `[0.9,0.9,0.9,0.9,0.95]` |
| 五个挡位，包括倒挡和空挡 | `[-1,0,1,2,3,4,5]` | `[0.9,0.9,0.9, 0.9,0.9,0.95,0.95]` |

**Gear number vector**、**Gear ratio vector**、**Inertia vector**、**Damping vector** 和 **Efficiency vector** 参数的向量维度必须相等。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta` |
| **值：** | `[0.9,0.9,0.9,0.9,0.9,0.95,0.95]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请将 **Efficiency factors** 设置为 `Gear only`。

### **Efficiency lookup table, eta\_tbl** — 挡位效率 `array`

挡位机械效率 *ηN* 随挡位、输入扭矩、输入速度和温度变化的表格。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_tbl` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请将 **Efficiency factors** 设置为 `Gear, input torque, input speed, and temperature`。

### **Initial gear number, G\_o** — 挡位 `0`（默认） | `scalar`

初始挡位编号，*Go*，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Initial output velocity, omega\_o** — 输出速度 `0`（默认） | `scalar`

变速器初始输出旋转速度，*ωo*，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Initial neutral input velocity, omegainN\_o** — 空挡输入速度 `0`（默认） | `scalar`

初始空挡输入旋转速度，*ωNo*，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegainN_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Shift time constant, tau\_s** — 时间 `.01`（默认） | `scalar`

换挡时间常数，*τs*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_s` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Transmission / Transmission Systems Vehicle Dynamics Blockset / Powertrain / Transmission

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

不带离合器或同步器的理想固定挡变速器

Ideal Fixed Gear Transmission 模块实现了一个不带离合器或同步器的理想化固定挡变速器。当不需要详细的变速器模型时（例如在部件尺寸设计、燃油经济性和排放研究中），可使用该模块对总体传动比和功率损失进行建模。该模块以最少的参数化或计算成本实现变速器模型。

要指定模块效率计算，请在 **Efficiency factors** 中选择以下任一选项。

| 设置 | 模块实现 |
| --- | --- |
| `Gear only` | 效率由基于挡位的一维查找表确定。 |
| `Gear, input torque, input speed, and temperature` | 效率由基于以下内容的 4D 查找表确定：  - 挡位 - 输入扭矩 - 输入速度 - 油温 |

模块使用以下方程确定变速器动力学：

ω˙iJNN2=ηN(ToN+Ti)−ωiN2bNωi=Nωo

模块对挡位命令信号进行滤波：

GGcmd(s)=1τss+1

### 空挡

当 **Initial gear number, G\_o** 等于 `0` 时，初始挡位为空挡。模块使用以下参数将输入飞轮与下游齿轮传动解耦。

- **Initial input velocity, omega\_o**
- **Initial neutral input velocity, omegainN\_o**

模块使用以下方程计算空挡速度和飞轮。

ω˙neutralJNN2=ηNToN−ωneutralN2bNωneutral=Nωo

ω˙1JF=η@N=0Ti−b@N=0ωiJF=J@N=1−J@N=0

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrEng` | 发动机功率 | *Peng* | ωiTi |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | ωoTo |
| `PwrNotTrnsfrd` — 越过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrEffLoss` | 机械功率损失 | *Peffloss* | ωoTo(ηN−1) |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | 当 G=0:     −bNωi2\|N2\|当 G≠0:  −bNωi2 −bNωneutral2\|N2\| |
| `PwrStored` — 储存能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredTrans` | 旋转动能的变化率 | *Pstr* | 当 G=0:     JNN2ω˙iωi当 G≠0:   JFω˙iωi+JNN2ω˙neutralωneutral |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *bN* | 接合挡位黏性阻尼 |
| *JN* | 接合挡位转动惯量 |
| *JF* | 飞轮转动惯量 |
| *ηN* | 接合挡位效率 |
| *G* | 接合挡位编号 |
| *Gcmd* | 要接合的挡位编号 |
| *N* | 接合挡位传动比 |
| *Ti* | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 |
| *To* | 施加的负载扭矩，通常来自差速器或驱动轴 |
| *ωo* | 初始输入驱动轴转速 |
| *ωi*, *ώi* | 施加的驱动轴角速度和角加速度 |
| *ωNo* | 初始空挡输入转速 |
| *ωneutral* | 空挡驱动轴转速 |
| *τs* | 换挡时间常数 |
