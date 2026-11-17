---
type: simulink-block
title: 'CVT Controller'
family: 'autoblks'
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

方向请求，*Dirreq*，
控制方向，前进或后退。*Dir* 等于 `1` 表示
前进运动。*Dir* 等于 `-1` 表示
后退。

Dir={1   当 Dirreq≥0−1  当 Dirreq<0

### **PllyRatioReq** — 带轮比请求 `scalar`

CVT 带轮比请求，
*ratiorequest*。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- |
| `Radius` | `PriRadius` | 变速器主带轮半径，由控制器请求产生 | *rpri* | m |
| `SecRadius` | 变速器副带轮半径，由控制器请求产生 | *rsec* | m |
| `InitPllyRadius` | 传动比为 1 时的初始带轮半径 | *ro* | m |
| `RatioAdj` | | 带轮传动比指令，基于请求和物理限制 | *ratiocommand* | N/A |
| `RatioMax` | | 最大带轮传动比 | *ratiomax* | N/A |
| `RatioMin` | | 最小带轮传动比 | *ratiomin* | N/A |
| `PriDispCmd` | | 变速器主带轮位移，由控制器请求产生 | *xpri* | m |
| `SecDispCmd` | | 变速器副带轮位移，由控制器请求产生 | *xsec* | m |

### **Dir** — 方向请求 `scalar`

方向请求，*Dirreq*，
控制方向，前进或后退。*Dir* 等于 `1` 表示
前进运动。*Dir* 等于 `-1` 表示
后退。

Dir={1   当 Dirreq≥0−1  当 Dirreq<0

### **PriDispCmd** — 主带轮位移 `scalar`

变速器主带轮位移，
*xpri*，单位为 m。

### **SecDispCmd** — 副带轮位移 `scalar`

变速器副带轮位移，
*xsec*，单位为 m。

## 参数

#### 运动学

### **Maximum variator primary pulley radius, rp\_max** — 半径 `.08`（默认）| `scalar`

最大变速器主带轮半径，
*rpmax*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_max` |
| **值：** | `.08`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Maximum variator secondary pulley radius, rs\_max** — 半径 `.07`（默认）| `scalar`

最大变速器副带轮半径，
*rsmax*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_max` |
| **值：** | `.07`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Minimum variator primary pulley radius, rp\_min** — 半径 `.03`（默认）| `scalar`

最小变速器主带轮半径，
*rpmin*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rp_min` |
| **值：** | `.03`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Minimum variator secondary pulley radius, rs\_min** — 半径 `.03`（默认）| `scalar`

最小变速器副带轮半径，
*rsmin*，单位为 m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rs_min` |
| **值：** | `.03`（默认）| `scalar` |
| **数据类型：** | `double` |

### **变速器带轮之间的间隙距离，rgap** — 指定冠轮连接 `.025`（默认）| `scalar`

次级带轮与初级带轮之间的间隙，
*rgap*，单位为 m。该图显示了
带轮几何结构。

初级带轮和次级带轮通过皮带连接。初级带轮半径为 rpri。次级带轮半径为 rsec。带轮排成一线并相隔距离 rgap。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rgap` |
| **值：** | `.025`（默认）| `scalar` |
| **数据类型：** | `double` |

### **变速器楔角，thetawedge** — 指定冠轮连接 `11`（默认）| `scalar`

变速器楔角，*Θwedge*，单位为 deg。

变速器楔角，theta，显示垂直线与楔形投影之间的角度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `thetaWedge` |
| **值：** | `11`（默认）| `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Transmission / Transmission Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

无级变速器控制器

CVT Controller 模块实现推带式
无级变速器（CVT）控制器。该模块使用
标准带轮和几何方程来计算 CVT 变速器的运动学
设定点。您可以使用该模块控制
CVT。

### 带轮运动学

使用系统的物理尺寸，该模块计算
满足带轮速比请求的初级和次级变速器位置。

该图和方程总结了几何依赖关系。

初级带轮和次级带轮通过皮带连接。初级带轮半径为 rpri。次级带轮半径为 rsec。带轮排成一线并相隔距离 rgap。

Cdist=rpmax+rgap+rsec\_maxL0=f(rpmax,rsmax,rpmin,rsmin,Cdist)ratiocommand=f(ratiorequest,ratiomax,ratiomin)rpri=f(r0,ratiocommand,Cdist)rsec=f(r0,ratiocommand,Cdist)xpri=f(r0,rpri,θwedge)xsec=f(r0,rsec,θwedge)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ratiorequest* | 带轮齿轮比请求 |
| *ratiocommand* | 带轮齿轮比命令，基于请求和物理限制 |
| *rgap* | 变速器带轮之间的间隙距离 |
| *Cdist* | 变速器带轮中心之间的距离 |
| *rpmax* | 最大变速器初级带轮半径 |
| *rsmax* | 最大变速器次级带轮半径 |
| *rpmin* | 最小变速器初级带轮半径 |
| *rsmin* | 最小变速器次级带轮半径 |
| *ro* | 齿轮比为 `1` 时的初始带轮半径 |
| *Lo* | 初始皮带长度，由变速器规格产生 |
| *xpri* | 变速器初级带轮位移，由控制器请求产生 |
| *xsec* | 变速器次级带轮位移，由控制器请求产生 |
| *rpri* | 变速器初级带轮半径，由控制器请求产生 |
| *rsec* | 变速器次级带轮半径，由控制器请求产生 |
| *Θwedge* | 变速器楔角 |
| *Φ* | 皮带与带轮接触点的角度 |
| *L* | 皮带长度，由变速器位置产生 |
