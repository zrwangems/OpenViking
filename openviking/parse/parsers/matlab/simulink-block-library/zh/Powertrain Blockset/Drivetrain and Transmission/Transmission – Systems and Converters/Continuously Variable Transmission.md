---
type: simulink-block
title: 'Continuously Variable Transmission'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain and Transmission / Transmission – Systems and Converters'
documentation_page: 'continuouslyvariabletransmission'
documentation_source_path: 'ref/continuouslyvariabletransmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Continuously Variable Transmission

## 端口

### 输入

### **Dir** — 方向请求 `scalar`

方向请求，*Dirreq*，用于控制方向。该模块对请求进行滤波以确定方向，即前进或倒车。*Dir* 对于前进运动等于 `1`。*Dir* 对于倒车等于 `-1`。

Dir={1   when Dirreq≥0−1  when Dirreq<0

### **PllyRatioReq** — 带轮速比请求 `scalar`

CVT 带轮速比请求，*ratiorequest*。

#### 依赖项

要创建此端口，请对 **Control mode** 参数选择 `Ideal integrated controller`。

### **PriDisp** — 主带轮位移 `scalar`

变速器主带轮位移，*xpri*，单位为 m。

#### 依赖项

要创建此端口，请对 **Control mode** 参数选择 `External control`。

### **SecDisp** — 次级带轮位移 `scalar`

变速器次级带轮位移，*xsec*，单位为 m。

#### 依赖项

要创建此端口，请对 **Control mode** 参数选择 `External control`。

### **EngTrq** — 输入驱动轴扭矩 `scalar`

施加到输入驱动轴的外部扭矩，*Ti*，单位为 N·m。

### **DiffTrq** — 输出驱动轴扭矩 `scalar`

施加到输出驱动轴的外部扭矩，*To*，单位为 N·m。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `EngTrq` | | | 输入轴扭矩 | *Ti* | N·m |
| `DiffTrq` | | | 输出轴扭矩 | *To* | N·m |
| `EngSpd` | | | 输入轴速度 | *ωi* | rad/s |
| `DiffSpd` | | | 输出轴速度 | *ωo* | rad/s |
| `PriRadius` | | | 主带轮半径 | *rpri* | m |
| `PriPhi` | | | 主带轮包角 | *Φpri* | rad |
| `SecRadius` | | | 次级带轮半径 | *rsec* | m |
| `SecPhi` | | | 次级带轮包角 | *Φsec* | rad |
| `BltLngthDelta` | | | 皮带长度变化 | *ΔL* | m |
| `BltLngth` | | | 皮带长度 | *L* | m |
| `BltLngthInit` | | | 初始皮带长度 | *Lo* | m |
| `BltOnPriTrq` | | | 作用在主带轮上的皮带扭矩 | *TBoP\_pri* | N·m |
| `BltOnSecTrq` | | | 作用在次级带轮上的皮带扭矩 | *TBoP\_sec* | N·m |
| `BltVel` | | | 皮带的线速度 | *vb* | m/s |
| `PriAngVel` | | | 主带轮速度 | *ωpri* | rad/s |
| `SecAngVel` | | | 次级带轮速度 | *ωsec* | rad/s |
| `PriSlipDir` | | | 主带轮打滑方向指示 | *PriSlipDir* | N/A |
| `SecSlipDir` | | | 次级带轮打滑方向指示 | *SecSlipDir* | N/A |
| `TransSpdRatio` | | | 总无打滑速比 | *Nfinal* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | 发动机功率 | *Peng* | W |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrBltLoss` | 皮带打滑功率损失 | *Pbltloss* | W |
| `PwrGearInLoss` | 输入行星齿轮机械功率损失 | *Pgrinloss* | W |
| `PwrGearOutLoss` | 输出齿轮减速机械功率损失 | *Pgroutloss* | W |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | W |
| `PwrStored` | `PwrStoredTrans` | 转动动能变化率 | *Pstr* | W |

### **EngSpd** — 输入驱动轴速度 `scalar`

输入驱动轴角速度，*ωi*，单位为 rad/sec。

### **DiffSpd** — 输出驱动轴速度 `scalar`

输出驱动轴角速度，*ωo*，单位为 rad/sec。

## 参数

### **Control mode** — 外部或内部 `Ideal integrated controller` (default) | `External control`

指定控制方法，内部或外部。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `CtrlType` |
| **值：** | `Ideal integrated controller` (default) | `External control` |
| **数据类型：** | `character vector` |

#### 依赖项

此表汇总了端口和输入模型配置。

| 控制模式 | 创建的端口 |
| --- | --- |
| `Ideal integrated controller` | `PllyRatioReq` |
| `External control` | `PriDisp`  `SecDisp` |

#### 运动学

### **Maximum variator primary pulley radius, rp\_max** — 半径 `.08` (default) | `scalar`

最大变速器主带轮半径，*rpmax*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_max` |
| **值：** | `.08` (default) | `scalar` |
| **数据类型：** | `double` |

### **Maximum variator secondary pulley radius, rs\_max** — 半径 `.07` (default) | `scalar`

最大变速器次级带轮半径，*rsmax*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_max` |
| **值：** | `.07` (default) | `scalar` |
| **数据类型：** | `double` |

### **Minimum variator primary pulley radius, rp\_min** — 半径 `.03` (default) | `scalar`

最小变速器主带轮半径，*rpmin*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_min` |
| **值：** | `.03` (default) | `scalar` |
| **数据类型：** | `double` |

### **Minimum variator secondary pulley radius, rs\_min** — 半径 `.03` (default) | `scalar`

最小变速器次级带轮半径，*rsmin*，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_min` |
| **值：** | `.03` (default) | `scalar` |
| **数据类型：** | `double` |

### **Gap distance between variator pulleys, rgap** — 指定冠轮连接 `.025` (default) | `scalar`

次级与主带轮之间的间隙，*rgap*，单位为 m。图中展示了带轮几何。

主带轮和次级带轮通过皮带连接。主带轮半径为 rpri。次级带轮半径为 rsec。带轮在同一线上，相隔距离 rgap。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rgap` |
| **值：** | `.025` (default) | `scalar` |
| **数据类型：** | `double` |

### **Variator wedge angle, thetawedge** — 指定冠轮连接 `11` (default) | `scalar`

变速器楔角，*Θwedge*，单位为 deg。

变速器楔角 theta，显示竖直线与楔形投影之间的角度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `thetaWedge` |
| **值：** | `11` (default) | `scalar` |
| **数据类型：** | `double` |

#### 动力学

### **Primary pulley inertia, J\_pri** — 惯量 `0.1` (default) | `scalar`

主带轮惯量，*Jpri*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_pri` |
| **值：** | `0.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Secondary pulley inertia, J\_sec** — 惯量 `0.1` (default) | `scalar`

次级带轮惯量，*Jsec*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_sec` |
| **值：** | `0.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Primary pulley damping coefficient, b\_pri** — 阻尼 `0.001` (default) | `scalar`

主带轮阻尼系数，*bpri*，单位为 N·m·s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b_pri` |
| **值：** | `0.001` (default) | `scalar` |
| **数据类型：** | `double` |

### **Secondary pulley damping coefficient, b\_sec** — 阻尼 `0.001` (default) | `scalar`

次级带轮阻尼系数，*bsec*，单位为 N·m·s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b_sec` |
| **值：** | `0.001` (default) | `scalar` |
| **数据类型：** | `double` |

### **Belt damping coefficient, b\_b** — 阻尼 `0.0025` (default) | `scalar`

皮带阻尼系数，*bb*，单位为 kg/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b_b` |
| **值：** | `0.0025` (default) | `scalar` |
| **数据类型：** | `double` |

### **Static friction coefficient, mu\_static** — 摩擦 `0.3` (default) | `scalar`

皮带与主带轮之间的静摩擦系数，*μstatic*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_static` |
| **值：** | `0.3` (default) | `scalar` |
| **数据类型：** | `double` |

### **Kinetic friction coefficient, mu\_kin** — 摩擦 `0.2` (default) | `scalar`

皮带与主带轮之间的动摩擦系数，*μkin*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mu_kin` |
| **值：** | `0.2` (default) | `scalar` |
| **数据类型：** | `double` |

### **Belt mass, m\_b** — 质量 `3` (default) | `scalar`

皮带质量，*mb*，单位为 kg。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `m_b` |
| **值：** | `3` (default) | `scalar` |
| **数据类型：** | `double` |

### **Pulley clamp force, F\_ax** — 带轮夹紧力 `5000` (default) | `scalar`

带轮夹紧力，*Fax*，单位为 N。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `F_ax` |
| **值：** | `5000` (default) | `scalar` |
| **数据类型：** | `double` |

#### 倒车与输出速比

### **Forward inertia, J\_fwd** — 惯量 `0.1` (default) | `scalar`

前进惯量，*Jfwd*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_fwd` |
| **值：** | `0.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Reverse inertia, J\_rev** — 惯量 `0.1` (default) | `scalar`

倒车惯量，*Jrev*，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_rev` |
| **值：** | `0.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **Forward efficiency, eta\_fwd** — 效率 `0.95` (default) | `scalar`

前进效率，*ηfwd*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_fwd` |
| **值：** | `0.95` (default) | `scalar` |
| **数据类型：** | `double` |

### **Reverse efficiency, eta\_rev** — 效率 `0.95` (default) | `scalar`

倒车效率，*ηrev*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_rev` |
| **值：** | `0.95` (default) | `scalar` |
| **数据类型：** | `double` |

### **Reverse gear ratio, N\_rev** — 速比 `2` (default) | `scalar`

倒车速比，*Nrev*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_rev` |
| **值：** | `2` (default) | `scalar` |
| **数据类型：** | `double` |

### **Shift time constant, tau\_s** — 常数 `.01` (default) | `scalar`

换挡时间常数，*τs*，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tau_s` |
| **值：** | `.01` (default) | `scalar` |
| **数据类型：** | `double` |

### **Output gear ratio, N\_o** — 速比 `2` (default) | `scalar`

输出齿轮速比，*No*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `N_o` |
| **值：** | `2` (default) | `scalar` |
| **数据类型：** | `double` |

### **Output gear efficiency, eta\_o** — 效率 `0.98` (default) | `scalar`

输出齿轮效率，*ηo*，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_o` |
| **值：** | `0.98` (default) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Transmission / Transmission Systems

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

具有独立半径控制的推带式无级变速器

Continuously Variable Transmission 模块实现具有独立半径控制的推带式无级变速器 (CVT)。将该模块用于控制系统设计、动力总成匹配和燃油经济性研究。您可以将该模块配置为内部或外部控制：

- 内部 — 输入方向和带轮速比请求
- 外部 — 输入方向和带轮位移请求

该表汇总了 Continuously Variable Transmission 模块进行的带轮运动学、减速和动力学计算。

| 计算 | 带轮运动学 | 倒车与最终减速 | 动力学 |
| --- | --- | --- | --- |
| 最终角速度比 | ✓ | ✓ | ✓ |
| 施加到次级和初级带轮的皮带扭矩 |  |  | ✓ |
| 施加到次级和初级带轮的扭矩 |  | ✓ |  |
| 次级和初级带轮的角速度 | ✓ | ✓ | ✓ |
| 皮带和带轮几何 | ✓ |  |  |
| 皮带线速度 |  |  | ✓ |
| 次级和初级带轮上的包角 | ✓ |  |  |
| 主带轮和次级带轮半径 | ✓ |  |  |

图中显示了具有两种配置的 CVT 变速器。在第一种配置中，即减速，变速器设置为减小主带轮半径并增大次级带轮半径。在第二种配置中，即超速挡，变速器设置为增大主带轮半径并减小次级带轮半径。

图中显示了具有两种配置的 CVT 变速器。在第一种配置中，即减速，变速器设置为减小主带轮半径并增大次级带轮半径。在第二种配置中，即超速挡，变速器设置为增大主带轮半径并减小次级带轮半径。

### 带轮运动学

使用系统的物理尺寸，该模块计算满足带轮速比请求的主变速器位置和次级变速器位置。

图和方程汇总了几何依赖关系。

主带轮和次级带轮通过皮带连接。主带轮半径为 rpri。次级带轮半径为 rsec。带轮在同一线上，相隔距离 rgap。

Cdist=rpmax+rgap+rsec\_maxL0=f(rpmax,rsmax,rpmin,rsmin,Cdist)ratiocommand=f(ratiorequest,ratiomax,ratiomin)rpri=f(r0,ratiocommand,Cdist)rsec=f(r0,ratiocommand,Cdist)xpri=f(r0,rpri,θwedge)xsec=f(r0,rsec,θwedge)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ratiorequest* | 带轮速比请求 |
| *ratiocommand* | 带轮速比命令，基于请求和物理限制 |
| *rgap* | 变速器带轮之间的间隙距离 |
| *Cdist* | 变速器带轮中心之间的距离 |
| *rpmax* | 最大变速器主带轮半径 |
| *rsmax* | 最大变速器次级带轮半径 |
| *rpmin* | 最小变速器主带轮半径 |
| *rsmin* | 最小变速器次级带轮半径 |
| *ro* | 速比为 `1` 时的初始带轮半径 |
| *Lo* | 初始皮带长度，由变速器规格确定 |
| *xpri* | 变速器主带轮位移，由控制器请求产生 |
| *xsec* | 变速器次级带轮位移，由控制器请求产生 |
| *rpri* | 变速器主带轮半径，由控制器请求产生 |
| *rsec* | 变速器次级带轮半径，由控制器请求产生 |
| *Θwedge* | 变速器楔角 |
| *Φ* | 皮带与带轮接触点的角度 |
| *L* | 皮带长度，由变速器位置产生 |

### 倒车与最终减速

CVT 输入轴连接到行星齿轮组，该齿轮组驱动主带轮。换挡方向决定输入齿轮惯量、效率和速比。换挡方向是经过滤波的命令方向：

DirshiftDir(s)=1τss+1

对于前进运动 (Dirshift=1)：

Ni=1ηi=ηfwdJi=Jfwd

对于倒车运动 (Dirshift=−1)：

Ni=−Nrevηi=ηrevJi=Jrev

速比和效率决定输入驱动轴速度以及施加到主带轮的扭矩：

Tapp\_pri=ηiNiTi

该模块使用固定速比降低次级带轮速度和施加的扭矩。

Tapp\_sec=ToηoNoωo=ωsecNo

无打滑时的最终速比由下式给出：

Nfinal=ωiωo=NiNorsecrpri

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Ni* | 输入行星齿轮速比 |
| *Dir* | CVT 方向命令 |
| *Dirshift* | 用于确定行星齿轮惯量、效率和速比的方向 |
| *τs* | 方向换挡时间常数 |
| *ηfwd*, *ηrev* | 分别为前进和倒车齿轮效率 |
| *Jfwd*, *Jrev* | 分别为前进和倒车齿轮惯量 |
| *Nrev* | 倒车速比 |
| *Tapp\_pri*, *Tapp\_sec* | 分别施加到主带轮和次级带轮的扭矩 |
| *Ti* | 输入驱动轴扭矩 |
| *ωi*, *ωo* | 分别为输入和输出驱动轴速度 |
| *ωpri*, *ωsec* | 分别为主带轮和次级带轮速度 |
| *Nfinal* | 总无打滑速比 |

### 动力学

CVT 可传递的最大扭矩取决于带轮与皮带之间的摩擦。根据 *Prediction of Friction Drive Limit of Metal V-Belt*，扭矩摩擦定义为：

Tfric(rp,μ)=2μFaxrpcos(ϑwedge)

在没有宏观打滑的情况下，假设带轮的切向加速度等于皮带加速度。一旦扭矩达到静摩擦极限，皮带开始打滑，带轮和皮带加速度相互独立。在打滑期间，皮带传递的扭矩是动摩擦系数的函数。在从打滑到非打滑条件的过渡期间，皮带和带轮切向速度相等。

该模块针对四种不同的打滑条件实现这些方程。

| 条件 | 方程 |
| --- | --- |
| 皮带在次级和主带轮上均打滑 | (Jpri+Ji)ω˙pri=Tapp\_pri-TBoP\_pri-bpriωpriJsecω˙sec=Tapp\_sec-TBoP\_sec-bsecωsecmbv˙b=TBoP\_prirpri+TBoP\_secrsec-bbvbrpriωpri≠vbrsecωsec≠vb |
| 皮带仅在主带轮上打滑 | (Jpri+Ji)ω˙pri=Tapp\_pri-TBoP\_pri-bpriωpri(mb+Jsecr2sec)v˙b=TBoP\_prirpri+TBoP\_secrsec-(bb+bsecr2sec)vbωsec=vbrsecrpriωpri≠vbTBoP\_pri=sgn(rpriωpri−vb)Tfric(rpri,μkin)|TBoP\_sec|<Tfric(rsec,μstatic) |
| 皮带仅在次级带轮上打滑 | (mb+Jpri+Jir2pri)v˙b=Tapp\_prirpri+TBoP\_secrsec-(bb+bprir2pri)vbJsecω˙b=Tapp\_sec+TBoP\_sec-bsecωsecωpri=vbrprirsecωsec≠vbTBoP\_sec=sgn(rsecωsec−vb)Tfric(rsec,μkin)|TBoP\_pri|<Tfric(rpri,μstatic) |
| 皮带不打滑 | (mb+Jsecr2sec+Jpri+Jir2pri)v˙b=Tapp\_prirpri+Tapp\_secrsec-(bb+bsecr2sec+bprir2pri)vbωpri=vbrpriωsec=vbrsec|TBoP\_pri|<Tfric(rpri,μstatic)|TBoP\_sec|<Tfric(rsec,μstatic) |
| 打滑方向 | PriSlipDir={0rpriωpri=vb1rpriωpri>vb−1rpriωpri<vbSecSlipDir={0rsecωsec=vb1rsecωsec>vb−1rsecωsec<vb |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *TBoP\_pri*, *TBoP\_sec* | 分别作用在主带轮和次级带轮上的皮带扭矩 |
| *Tapp\_pri*, *Tapp\_sec* | 分别施加到主带轮和次级带轮上的扭矩 |
| *Jpri*, *Jsec* | 分别为主带轮和次级带轮的转动惯量 |
| *bpri*, *bsec* | 分别为主带轮和次级带轮的转动粘性阻尼 |
| *Fax* | 带轮夹紧力 |
| *μ* | 摩擦系数 |
| *μkin*, *μstatic* | 动摩擦系数和静摩擦系数 |
| *vb*, *аb* | 分别为皮带的线速度和加速度 |
| *mb* | 皮带总质量 |
| *rpri*, *rsec* | 分别为主带轮和次级带轮的半径 |
| *Φwrap* | 皮带与带轮接触点的包角 |
| *Φwrap\_pri*, *Φwrap\_sec* | 分别为主带轮和次级带轮包角 |

### 功率核算

对于功率核算，该模块实现这些方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrEng` | 发动机功率 | *Peng* | ωiTi |
| `PwrDiffrntl` | 差速器功率 | *Pdiff* | ωoTo |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrBltLoss` | 皮带打滑功率损失 | *Pbltloss* | (Jin+Jpri)ω˙priωpri+Jsecω˙secωsec+mbv˙bvb+bpriωpri2+bsecωsec2+bbvb2−Tapppriωpri−Tappsecωsec |
| `PwrGearInLoss` | 输入行星齿轮机械功率损失 | *Pgrinloss* | −|ωiTi−Τapp\_priωpri| |
| `PwrGearOutLoss` | 输出齿轮减速机械功率损失 | *Pgroutloss* | −|ωoTo−Τapp\_secωsec| |
| `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | −bpriωpri2−bsecωsec2−bbvb2 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredTrans` | 转动动能变化率 | *Pstr* | (Jin+Jpri)ω˙priωpri+Jsecω˙secωsec+mbv˙bvb |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Tapp\_pri*, *Tapp\_sec* | 分别施加到主带轮和次级带轮上的扭矩 |
| *Ti*, *To* | 分别为输入和输出驱动轴扭矩 |
| *Jpri*, *Jsec* | 分别为主带轮和次级带轮的转动惯量 |
| *bpri*, *bsec* | 分别为主带轮和次级带轮的转动粘性阻尼 |
| *ωpri*, *ωsec* | 分别为主带轮和次级带轮速度 |
| *ωi*, *ωo* | 分别为输入和输出驱动轴速度 |
| *vb*, *аb* | 分别为皮带的线速度和加速度 |
| *rpri*, *rsec* | 分别为主带轮和次级带轮的半径 |
