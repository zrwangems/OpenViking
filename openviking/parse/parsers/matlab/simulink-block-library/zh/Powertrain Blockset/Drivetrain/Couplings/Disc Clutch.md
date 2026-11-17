---
type: simulink-block
title: 'Disc Clutch'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'discclutch'
documentation_source_path: 'ref/discclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Disc Clutch

## 端口

### 输入

### **Press** — 施加的离合器压力 `scalar`

基础齿轮输入扭矩，*Pc*，
单位为 N·m^2。

### **BTrq** — 施加的输入扭矩 `scalar`

施加的输入扭矩，*Ti*，
通常来自发动机曲轴或双质量飞轮减振器，单位为
N·m。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **FTrq** — 施加的负载扭矩 `scalar`

施加的负载扭矩，*To*，
通常来自差速器或驱动轴，单位为 N·m。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **B** — 施加的驱动轴角速度和扭矩双向连接端口

施加的驱动轴角速度，*ωi*，
单位为 rad/s。施加的驱动轴扭矩，*Ti*，
单位为 N·m。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Two-way connection`。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `Base` | `BTrq` | | 施加的输入扭矩，通常来自发动机曲轴或双质量飞轮减振器 | N·m |
| `BSpd` | | 施加的驱动轴角速度输入 | rad/s |
| `Flwr` | `FTrq` | | 施加的负载扭矩，通常来自差速器 | N·m |
| `FSpd` | | 驱动轴角速度输出 | rad/s |
| `Cltch` | `CltchForce` | | 施加的离合器力 | N |
| `CltchLocked` | | 离合器锁定状态 | NA |
| `CltchSpdRatio` | | 离合器速度比 | NA |
| `CltchEta` | | 离合器动力传输效率 | NA |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBase` | 施加的基础功率 | W |
| `PwrFlwr` | 从动输出功率 | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 阻尼功率损耗 | W |
| `PwrCltchSlipLoss` | 离合器滑差功率损耗 | W |
| `PwrStored` | `PwrStoredBase` | 基础旋转动能变化率 | W |
| `PwrStoredFlwr` | 从动旋转动能变化率 | W |

### **BSpd** — 角速度 `scalar`

施加的驱动轴角速度输入，
*ωi*，单位为 rad/s。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **FSpd** — 角速度 `scalar`

驱动轴角速度输出，
*ωo*，单位为 rad/s。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **F** — 输出速度和扭矩双向连接端口

输出驱动轴角速度，*ωoi*，
单位为 rad/s。输出驱动轴扭矩，*To*，
单位为 N·m。

#### 依赖关系

要创建此端口，请将 **Port Configuration** 设置为
`Two-way connection`。

## 参数

#### 模块选项

### **Port Configuration** — 指定配置 `Simulink`（默认）| `Two-way connection`

指定端口配置。

#### 依赖关系

指定 `Simulink` 会创建以下端口：

- `BSpd`
- `FSpd`
- `BTrq`
- `FTrq`

指定 `Two-way connection` 会创建以下端口：

- `B`
- `F`

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Simulink`（默认）| `Two-way connection` |
| **数据类型：** | `character vector` |

### **Clutch force equivalent net radius, Reff** — 半径 `1`（默认）| 正标量

离合器力等效净半径，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Reff` |
| **值：** | `1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Number of disks, Ndisk** — 比值 `1`（默认）| 正标量

磁盘数量，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ndisk` |
| **值：** | `1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **有效施加压力面积，Aeff** — 压力面积 `.01`（默认）| 正标量

有效施加压力面积，单位为 m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aeff` |
| **值：** | `.01`（默认）| 正标量 |
| **数据类型：** | `double` |

### **接合压力阈值，Peng** — 压力阈值 `0`（默认）| 标量

接合离合器的压力，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Peng` |
| **值：** | `0`（默认）| 标量 |
| **数据类型：** | `double` |

### **输入轴惯量，Jin** — 惯量 `.1`（默认）| 正标量

输入轴惯量，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jin` |
| **值：** | `.1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **输出轴惯量，Jout** — 惯量 `.1`（默认）| 正标量

输出轴惯量，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jout` |
| **值：** | `.1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **动摩擦系数，muk** — 系数 `.3`（默认）| 正标量

动摩擦系数，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `muk` |
| **值：** | `.3`（默认）| 正标量 |
| **数据类型：** | `double` |

### **静摩擦系数，mus** — 系数 `.5`（默认）| 正标量

静摩擦系数，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mus` |
| **值：** | `.5`（默认）| 正标量 |
| **数据类型：** | `double` |

### **输入轴粘性阻尼，bin** — 阻尼 `.001`（默认）| 正标量

输入轴粘性阻尼，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bin` |
| **值：** | `.001`（默认）| 正标量 |
| **数据类型：** | `double` |

### **输出轴粘性阻尼，bout** — 阻尼 `.001`（默认）| 正标量

输出轴粘性阻尼，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bout` |
| **值：** | `.001`（默认）| 正标量 |
| **数据类型：** | `double` |

### **初始输入轴速度，win\_o** — 初始速度 `0`（默认）| `scalar`

输入轴初始速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `win_o` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **初始输出轴速度，wout\_o** — 初始速度 `0`（默认）| `scalar`

输入轴初始速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `wout_o` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **离合器致动时间常数，tauC** — 常数 `.01`（默认）| `scalar`

离合器致动时间常数，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauC` |
| **值：** | `.01`（默认）| `scalar` |
| **数据类型：** | `double` |

### **以离合器锁止状态开始仿真** — 选择以初始锁止离合器 `off`（默认）| `on`

选择以初始锁止离合器。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitiallyLocked` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

## 所属库

Powertrain Blockset / Drivetrain / Couplings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

理想化盘式离合器耦合器

Disc Clutch 模块实现了一个理想化的
盘式离合器耦合器。该模块通过理想化摩擦模型耦合旋转输入轴和输出
轴。为确定输出
扭矩，该模块使用摩擦参数、相对滑移速度
和施加的输入压力。

在燃油经济性和动力总成效率研究中，您可以使用
Disc Clutch 模块来建模常见传动系统元件（如变速器、
发动机和差速器）之间的机械功率
传递。

为近似扭矩响应，Disc Clutch 模块
实现了取决于离合器锁止
条件的摩擦和动力学模型。该模块基于理想化干式离合器摩擦模型确定锁止或未锁止
条件。此表总结了该模块用于确定离合器条件的
逻辑。

| 离合器条件 | 何时 |
| --- | --- |
| 未锁止 | ωi≠ωoorTfmax<|JoTi−(Jobi−Jibo)ωi/oJo+Ji| |
| 锁止 | ωi=ωoandTfmax<|Ti−Ji(bi+bo)ωiJo+Ji+boωi| |

此表总结了该模块用于锁止或未锁止离合器条件的
摩擦和动力学模型。

| 离合器条件 | 摩擦模型 | 动力学模型 |
| --- | --- | --- |
| 未锁止 | Tfmax=Tkwhere,Tk=NdiscPcAeffReffμktanh[4(ωi−ωo)]Reff=2(Ro3-Ri3)3(Ro2-Ri2) andPc=max(Pc−Peng,0) | ω˙iJi=Ti−Tf−ωibiω˙oJo=Tf+To−ωobo |
| 锁止 | Tfmax=Tswhere,Ts=NdiscPcAeffReffμsReff=2(Ro3-Ri3)3(Ro2-Ri2) | ω˙i(Jo+Ji)=To−ωi(bi+bo)+Tiωi=ωo |

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrBase` | 施加的基准功率 | ωiTi |
| `PwrFlwr` | 施加的从动输出功率 | ωoTo |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 阻尼功率损失 | −boωo2 −biωi2 |
| `PwrCltchSlipLoss` | 离合器滑差功率损失 | −Tk(ωi−ωo) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredBase` | 基准旋转动能的变化率 | ω˙iωiJi |
| `PwrStoredFlwr` | 从动旋转动能的变化率 | ω˙oωoJo |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωi* | 输入轴角速度 |
| *ωo* | 输出轴角速度 |
| *bi* | 输入轴粘性阻尼 |
| *bo* | 输出轴粘性阻尼 |
| *Ji* | 输入轴转动惯量 |
| *Jo* | 输出轴转动惯量 |
| *Tf* | 摩擦力矩 |
| *Ti* | 净输入力矩 |
| *Tk* | 动摩擦力矩 |
| *To* | 净输出力矩 |
| *Ts* | 静摩擦力矩 |
| *Tfmax* | 打滑前的最大摩擦力矩 |
| *Pc* | 施加的离合器压力 |
| *Peng* | 接合压力 |
| *Aeff* | 有效面积 |
| *Ndisc* | 摩擦片数量 |
| *Reff* | 离合器有效半径 |
| *Ro* | 环形盘外半径 |
| *Ri* | 环形盘内半径 |
| *Re* | 在载荷下且给定压力下的有效轮胎半径 |
| *μs* | 静摩擦系数 |
| *μk* | 动摩擦系数 |
