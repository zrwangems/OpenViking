---
type: simulink-block
title: 'Split Torsional Compliance'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain / Drivetrain / Couplings'
documentation_page: 'splittorsionalcompliance'
documentation_source_path: 'ref/splittorsionalcompliance.html'
language: zh-CN
chinese_source: worker-translation
---

# Split Torsional Compliance

## 端口

### 输入

### **RSpd** — 输入轴转速 `scalar`

输入轴旋转速度，*ωin*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **C1Spd** — 第一输出轴转速 `scalar`

第一输出轴旋转速度，*ω1out*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **C2Spd** — 第二输出轴转速 `scalar`

第二输出轴旋转速度，*ω2out*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **CSpd** — 输入转速 `scalar`

输出轴旋转速度，*ωout*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **R1Spd** — 第一输入轴转速 `scalar`

第一输入轴旋转速度，*ω1in*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **R2Spd** — 第二输入轴转速 `scalar`

第二输入轴旋转速度，*ω2in*，以 rad/s 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **R** — 输入轴角速度和扭矩双向连接器端口

输入轴角速度，*ωin*，以 rad/s 为单位；以及扭矩，*Tin*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **R1** — 第一输入轴角速度和扭矩双向连接器端口

第一输入轴角速度，*ω1in*，以 rad/s 为单位；以及扭矩，*T1in*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`

### **R2** — 第二输入轴角速度和扭矩双向连接器端口

第二输入轴角速度，*ω2in*，以 rad/s 为单位；以及扭矩，*T2in*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`
### 输出

### **Info** — 总线信号 bus

如果将 **Coupling Configuration** 设置为 `Shaft split`，则 Info 总线包含以下信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | | 输入轴扭矩 | *Tin* | N·m |
| `C1` | | 第一输出轴扭矩 | *T1out* | N·m |
| `C2` | | 第二输出轴扭矩 | *T2out* | N·m |
| `Damp` | `C1` | 第一输出轴阻尼扭矩 | *b1**ω1out* | N·m |
| `C2` | 第二输出轴阻尼扭矩 | *b2**ω2out* | N·m |
| `Spring` | `C1` | 第一输出轴弹簧扭矩 | *k1**θ1* | N·m |
| `C2` | 第二输出轴弹簧扭矩 | *k2**θ2* | N·m |
| Spd | `R` | | | 输入轴角速度 | *ωin* | rad/s |
| `C1` | | 第一输出轴角速度 | *ω1out* | rad/s |
| `C2` | | 第二输出轴角速度 | *ω2out* | rad/s |
| `deltadot1` | | 输入轴与第一输出轴角速度之差 | θ˙1 | rad/s |
| `deltadot2` | | 输入轴与第二输出轴角速度之差 | θ˙2 | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | 来自输入轴的机械功率 | *PTR* | W |
| `PwrC1` | 来自第一输出轴的机械功率 | *PTC1* | W |
| `PwrC2` | 来自第二输出轴的机械功率 | *PTC2* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 机械阻尼损耗 | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | 存储的内部扭转能变化率 | *Ps* | W |

如果将 **Coupling Configuration** 设置为 `Shaft merge`，则 Info 总线包含以下信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Trq | `C` | | | 输出轴扭矩 | *Tout* | N·m |
| `R1` | | 第一输入轴扭矩 | *T1in* | N·m |
| `R2` | | 第二输入轴扭矩 | *T2in* | N·m |
| `Damp` | `R1` | 第一输入轴阻尼扭矩 | *b1**ω1in* | N·m |
| `R2` | 第二输入轴阻尼扭矩 | *b2**ω2in* | N·m |
| `Spring` | `R1` | 第一输入轴弹簧扭矩 | *k1**θ1* | N·m |
| `R2` | 第二输入轴弹簧扭矩 | *k2**θ2* | N·m |
| Spd | `C` | | | 输出轴角速度 | *ωout* | rad/s |
| `R1` | | 第一输入轴角速度 | *ω1in* | rad/s |
| `R2` | | 第二输入轴角速度 | *ω2in* | rad/s |
| `deltadot1` | | 第一输入轴与输出轴角速度之差 | θ˙1 | rad/s |
| `deltadot2` | | 第二输入轴与输出轴角速度之差 | θ˙2 | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrC` | 来自输出轴的机械功率 | *PTC* | W |
| `PwrR1` | 来自第一输入轴的机械功率 | *PTR1* | W |
| `PwrR2` | 来自第二输入轴的机械功率 | *PTR2* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 机械阻尼损耗 | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | 存储的内部扭转能变化率 | *Ps* | W |

#### 依赖关系

要启用此端口，请选择 **Output Info bus**。

### **RTrq** — 输入轴扭矩 `scalar`

输入轴扭矩，*Tin*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **C1Trq** — 第一输出轴扭矩 `scalar`

第一输出轴扭矩，*T1out*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **C2Trq** — 第二输出轴扭矩 `scalar`

第二输出轴扭矩，*T2out*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft split`

### **CTrq** — 输出轴扭矩 `scalar`

输出轴扭矩，*Tout*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **R1Trq** — 第一输入轴扭矩 `scalar`

第一输入轴扭矩，*T1in*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **R2Trq** — 第二输入轴扭矩 `scalar`

第二输入轴扭矩，*T2in*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请设置以下两个参数：

- 将 **Port Configuration** 设置为 `Simulink`
- 将 **Coupling Configuration** 设置为 `Shaft merge`

### **C1** — 第一输出轴角速度和扭矩双向连接器端口

第一输出轴角速度，*ω1out*，以 rad/s 为单位；以及扭矩，*T1out*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **C2** — 第二输出轴角速度和扭矩双向连接器端口

第二输出轴角速度，*ω2out*，以 rad/s 为单位；以及扭矩，*T2out*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft split`

### **C** — 输出轴角速度和扭矩双向连接器端口

输出轴角速度，*ωout*，以 rad/s 为单位；以及扭矩，*Tout*，以 N·m 为单位。

#### 依赖关系

要启用此端口，请选择：

- **Port Configuration**>`Two-way connection`
- **Coupling Configuration**>`Shaft merge`

## 参数

#### 模块选项

### **Port Configuration** — 指定配置 `Simulink`（默认） | `Two-way connection`

指定端口配置。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Simulink`（默认） | `Two-way connection` |
| **数据类型：** | `character vector` |

### **Coupling Configuration** — 指定配置 `Shaft split`（默认） | `Shaft merge`

指定耦合类型。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CplrMode` |
| **值：** | `Shaft split`（默认） | `Shaft merge` |
| **数据类型：** | `character vector` |

### **Output Info bus** — 选择 `off`（默认） | `on`

选择以创建 `Info` 输出端口。

#### 耦合 1

### **Torsional stiffness, k1** — 刚度 `5e4`（默认） | 大于或等于 0 的 scalar

转动惯量，*k1*，以 N·m/rad 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `k1` |
| **值：** | `5e4`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **Torsional damping, b1** — 阻尼 `1e2`（默认） | 大于或等于 0 的 scalar

扭转阻尼，*b1*，以 N·m· s/rad 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b1` |
| **值：** | `1e2`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **Damping cutoff frequency, omega1\_c** — 频率 `3000`（默认） | 正 scalar

阻尼截止频率，以 rad/s 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega1_c` |
| **值：** | `3000`（默认） | 正 scalar |
| **数据类型：** | `double` |

#### 耦合 2

### **Torsional stiffness, k2** — 刚度 `5e4`（默认） | 大于或等于 0 的 scalar

转动惯量，*k2*，以 N·m/rad 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `k2` |
| **值：** | `5e4`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **Torsional damping, b2** — 阻尼 `1e2`（默认） | `scalar`

扭转阻尼，*b2*，以 N·m· s/rad 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b2` |
| **值：** | `1e2`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **Damping cutoff frequency, omega2\_c** — 频率 `3000`（默认） | 正 scalar

阻尼截止频率，以 rad/s 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega2_c` |
| **值：** | `3000`（默认） | 正 scalar |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

分流扭转耦合器

Split Torsional Compliance 模块实现轴之间的并联弹簧-阻尼耦合。您可以通过选择 **Coupling Configuration** 参数之一来指定耦合类型：

- `Shaft split` — 单个输入轴耦合到两个输出轴
- `Shaft merge` — 两个输入轴耦合到单个输出轴

在燃油经济性和排放研究中，您可以使用 Split Torsional Compliance 模块对常见传动系统元件（如电机、行星齿轮和离合器）之间的机械旋转柔度进行建模。例如，使用 `Shaft split` 配置将电机和两个行星齿轮组耦合。使用 `Shaft merge` 配置将双离合变速器耦合到输出轴。

### Shaft Split

对于 `Shaft split` 配置，该模块实现以下示意图和方程。

轴分流旋转柔度示意图

Tin=−(ωin−ω1out)b1−(ωin−ω2out)b2−θ1k1−θ2k2T1out=(ωin−ω1out)b1+θ1k1T2out=(ωin−ω2out)b2+θ2k2θ˙1=(ωin−ω1out)θ˙2=(ωin−ω2out)

为了考虑频率相关阻尼，两个阻尼项均包含一个低通滤波器。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tin* | 产生的施加输入反作用扭矩 |
| *ωin* | 输入轴旋转速度 |
| *T1out* | 产生的施加到第一输出轴的扭矩 |
| *ω1out* | 第一输出轴旋转速度 |
| *T2out* | 产生的施加到第二输出轴的扭矩 |
| *ω2out* | 第二输出轴旋转速度 |
| *θ1*, *θ2* | 分别为第一、第二轴的旋转角 |
| *b1*, *b2* | 分别为第一、第二轴的粘性阻尼 |
| *k1*, *k2* | 分别为第一、第二轴的扭转刚度 |

### Shaft Merge

对于 `Shaft merge` 配置，该模块实现以下示意图和方程。

轴合并旋转柔度示意图

Tout=(−ωout+ω1in)b1+(−ωout+ω2in)b2+θ1k1+θ2k2T1out=(ωout−ω1in)b1−θ1k1T2out=(ωout−ω2in)b2−θ2k2θ˙1=(ω1in−ωout)θ˙2=(ω2in−ωout)

为了考虑频率相关阻尼，两个阻尼项均包含一个低通滤波器。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tout* | 产生的施加输出扭矩 |
| *ωout* | 输出轴旋转速度 |
| *T1in* | 对第一输入轴的反作用扭矩 |
| *ω1in* | 第一输入轴旋转速度 |
| *T2in* | 对第二输入轴的反作用扭矩 |
| *ω2in* | 第二输入轴旋转速度 |
| *θ1*, *θ2* | 分别为第一、第二轴的旋转角 |
| *b1*, *b2* | 分别为第一、第二轴的粘性阻尼 |
| *k1*, *k2* | 分别为第一、第二轴的扭转刚度 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 在模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrR` | 对于 `Shaft split` 配置，来自输入轴的机械功率 | *PTR* | PTR= −TRωR |
| `PwrC1` | 对于 `Shaft split` 配置，来自第一个输出轴的机械功率 | *PTC1* | PTC1= −TC1ωC1 |
| `PwrC2` | 对于 `Shaft split` 配置，来自第二个输出轴的机械功率 | *PTC2* | PTC2= −TC2ωC2 |
| `PwrC` | 对于 `Shaft merge` 配置，来自输出轴的机械功率 | *PTC* | PTC= TCωC |
| `PwrR1` | 对于 `Shaft merge` 配置，来自第一个输入轴的机械功率 | *PTR1* | PTR1= TR1ωR1 |
| `PwrR2` | 对于 `Shaft merge` 配置，来自第二个输入轴的机械功率 | *PTR2* | PTR2= TR2ωR2 |
| `PwrNotTrnsfrd` — 跨过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 机械阻尼损失 | *Pd* | Pd=−(b1|θ˙1|2+b2|θ˙2|2) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 弹簧能量的变化率 | *Ps* | Ps=(k1θ1θ˙1+k2θ2θ˙2) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *TR* | Shaft R 扭矩 |
| *TC* | Shaft C 扭矩 |
| *ωR* | Shaft R 角速度 |
| *ωC* | Shaft C 角速度 |
| *θ* | 耦合轴旋转 |
| *k* | 轴扭转刚度 |
| *b* | 旋转粘性阻尼 |
| *Pt* | 总机械功率 |
| *Pd* | 由阻尼导致的功率损失 |
| *Ps* | 存储的弹簧能量的变化率 |
