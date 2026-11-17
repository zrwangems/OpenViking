---
type: simulink-block
title: 'Hydraulic Constant Pressure Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Sources'
documentation_page: 'hydraulicconstantpressuresource'
documentation_source_path: 'ref/hydraulicconstantpressuresource.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Constant Pressure Source

## 端口
```yaml
ports: []
```

该模块具有以下端口：

`T`
:   与源入口关联的液压守恒端口。

`P`
:   与源出口关联的液压守恒端口。
## 参数
```yaml
parameters: []
```

**Pressure**
:   指定源入口与出口之间的压力差。默认值为 `1e6` Pa。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）理想液压能源，具有恒定压力特性

Hydraulic Constant Pressure Source 模块表示一个理想液压能源，其功率足以在源入口和出口之间维持指定的压力差，而不受通过源的流量影响。

**Pressure** 参数指定源两端的压力差

p=pP−pT

其中 *p*P、*p*T 是源端口处的表压。

模块连接 T 和 P 分别对应液压入口和出口端口。模块正方向为从端口 P 到端口 T。
