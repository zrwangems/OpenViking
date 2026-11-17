---
type: simulink-block
title: 'CVT Controller'
family: 'transmission'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Transmission Controllers'
documentation_page: 'cvtcontroller'
documentation_source_path: 'ref/cvtcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# CVT Controller

## 端口

### 输入

### **DirReq** — 方向请求 `scalar`

方向请求，*Dirreq*，控制方向，即前进或倒车。前进运动时 *Dir* 等于 `1`。倒车时 *Dir* 等于 `-1`。

Dir={1   当 Dirreq≥0−1  当 Dirreq<0

### **PllyRatioReq** — 带轮传动比请求 `scalar`

CVT 带轮传动比请求，*ratiorequest*。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- |
| `Radius` | `PriRadius` | 由控制器请求产生的变速器主动带轮半径 | *rpri* | m |
| `SecRadius` | 由控制器请求产生的变速器从动带轮半径 | *rsec* | m |
| `InitPllyRadius` | 传动比为 1 时的初始带轮半径 | *ro* | m |
| `RatioAdj` | | 带轮传动比指令，基于请求和物理限制 | *ratiocommand* | N/A |
| `RatioMax` | | 最大带轮传动比 | *ratiomax* | N/A |
| `RatioMin` | | 最小带轮传动比 | *ratiomin* | N/A |
| `PriDispCmd` | | 由控制器请求产生的变速器主动带轮位移 | *xpri* | m |
| `SecDispCmd` | | 由控制器请求产生的变速器从动带轮位移 | *xsec* | m |

### **Dir** — 方向请求 `scalar`

方向请求，*Dirreq*，控制方向，即前进或倒车。前进运动时 *Dir* 等于 `1`。倒车时 *Dir* 等于 `-1`。

Dir={1   当 Dirreq≥0−1  当 Dirreq<0

### **PriDispCmd** — 主动带轮位移 `scalar`

变速器主动带轮位移，*xpri*，单位为 m。

### **SecDispCmd** — 从动带轮位移 `scalar`

变速器从动带轮位移，*xsec*，单位为 m。

## 参数

#### 运动学

### **Maximum variator primary pulley radius, rp\_max** — 半径 `.08`（默认） | `scalar`

最大变速器主动带轮半径，*rpmax*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_max` |
| **值：** | `.08`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Maximum variator secondary pulley radius, rs\_max** — 半径 `.07`（默认） | `scalar`

最大变速器从动带轮半径，*rsmax*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_max` |
| **值：** | `.07`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Minimum variator primary pulley radius, rp\_min** — 半径 `.03`（默认） | `scalar`

最小变速器主动带轮半径，*rpmin*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_min` |
| **值：** | `.03`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Minimum variator secondary pulley radius, rs\_min** — 半径 `.03`（默认） | `scalar`

最小变速器从动带轮半径，*rsmin*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_min` |
| **值：** | `.03`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Gap distance between variator pulleys, rgap** — 指定冠轮连接 `.025`（默认） | `scalar`

从动带轮和主动带轮之间的间隙，*rgap*，单位为 m。该图显示了带轮几何结构。

主动带轮和从动带轮通过皮带连接。主动带轮半径为 rpri。从动带轮半径为 rsec。带轮共线，间距为 rgap。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rgap` |
| **值：** | `.025`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Variator wedge angle, thetawedge** — 指定冠轮连接 `11`（默认） | `scalar`

变速器楔角，*Θwedge*，单位为 deg。

变速器楔角 theta，显示垂直线与楔投影之间的角度。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `thetaWedge` |
| **值：** | `11`（默认） | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Transmission / Transmission Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

无级变速器控制器

CVT Controller 模块实现推带式无级变速器（CVT）控制器。该模块使用标准带轮方程和几何方程计算 CVT 变速机构的运动学设定点。您可以使用该模块控制 CVT。

### 带轮运动学

使用系统的物理尺寸，该模块计算满足带轮传动比请求的主动和从动变速机构位置。

该图和方程总结了这些几何依赖关系。

主动带轮和从动带轮通过皮带连接。主动带轮半径为 rpri。从动带轮半径为 rsec。带轮共线，间距为 rgap。

Cdist=rpmax+rgap+rsec\_maxL0=f(rpmax,rsmax,rpmin,rsmin,Cdist)ratiocommand=f(ratiorequest,ratiomax,ratiomin)rpri=f(r0,ratiocommand,Cdist)rsec=f(r0,ratiocommand,Cdist)xpri=f(r0,rpri,θwedge)xsec=f(r0,rsec,θwedge)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ratiorequest* | 带轮传动比请求 |
| *ratiocommand* | 带轮传动比指令，基于请求和物理限制 |
| *rgap* | 变速器带轮之间的间隙距离 |
| *Cdist* | 变速器带轮中心之间的距离 |
| *rpmax* | 最大变速器主动带轮半径 |
| *rsmax* | 最大变速器从动带轮半径 |
| *rpmin* | 最小变速器主动带轮半径 |
| *rsmin* | 最小变速器从动带轮半径 |
| *ro* | 传动比为 `1` 时的初始带轮半径 |
| *Lo* | 由变速器规格得到的初始皮带长度 |
| *xpri* | 由控制器请求产生的变速器主动带轮位移 |
| *xsec* | 由控制器请求产生的变速器从动带轮位移 |
| *rpri* | 由控制器请求产生的变速器主动带轮半径 |
| *rsec* | 由控制器请求产生的变速器从动带轮半径 |
| *Θwedge* | 变速器楔角 |
| *Φ* | 皮带与带轮接触点的角度 |
| *L* | 由变速器位置得到的皮带长度 |
