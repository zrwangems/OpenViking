---
type: simulink-block
title: 'Register Read/Write'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Memory Operations'
documentation_page: 'registerreadwrite'
documentation_source_path: 'ref/registerreadwrite.html'
language: en
---

# Register Read/Write

## Ports

### Output

### **All** — Bit fields selected scalar

The outports depends on the number of bit fields selected when registers are
accessed using specified bits. In the Register bit fields parameter, option
**All** is selected by default which is visible as the
output port. If any other bit field is selected, the outports will change
depending on the selected bit fields.

The bit field **All** will access the entire register.

**Note**

In Register bit field parameter, you can either select option All or
other specific bit fields.

The output ports are dynamic and depends on the number bit field selected.
When registers are accessed using custom bits, it depends upon the length of
cell array specified in the parameter **Bits to
process**.

#### Dependencies

To enable this port, set the **Operation**
parameter to `Read`.

**Data Types:** `uint16` | `uint32`
### Input

### **All** — Number bit field selected scalar

The inports depends on the number bit field selected when registers are
accessed using specified bits.

In the Register bit fields parameter, option **All** is
selected by default which is visible as the input port. If any other bit field
is selected, the inports will change depending on the selected bit
fields.

The bit field **All** will access the entire register.

**Note**

In Register bit field parameter, you can either select option All or
other specific bit fields.

The input ports are dynamic and depends on the number bit field selected.
When registers are accessed using custom bits, it depends upon the length of
cell array specified in the parameter **Bits to
process**.

#### Dependencies

To enable this port, set the **Operation**
parameter to `Write`.

**Data Types:** `uint16` | `uint32`

## Parameters

### **Device family** — Select TI C2000 device family `None` (default) | `F2804x` | `F280x` | `F281x` | `F2833x` | `F2844x` | `F280013x` | `F280015x` | `F28002x` | `F28003x` | `F28004x` | `F2802x` | `F2803x` | `F2805x` | `F2806x` | `F2807x` | `F2837xS` | `F2837xD_CPU1` | `F2837xD_CPU2` | `F2838x_CPU1` | `F2838x_CPU2` | `F2838x_CORTEXM4` | `F28M35x` | `F28M35x` | `F28M35x` | `F28p65x_CPU1` | `F28p65x_CPU2`

Select the TI C2000 device family for which you want to access the
registers.

### **Register group** — Select required register groups Unspecified (default)

Select the register group for the Register Read/Write block.

The options for the parameter is populated depending on the device family
selected after you have performed C2000 HW setup. This parameter groups the TI
C2000 registers into various categories namely ADC, PWM and so on.

Selecting the register group defines the parameters such as Register name,
Register fields and Register bit fields of the block. For example, if you select
the Register group as ADC their corresponding Register name, Register fields and
Register bit fields gets populated.

### **Register name** — Select register name `Unspecified` (default)

Select the register name for the selected register group. The options are
populated based on the register group and device family selected. For example, if
the Register group is ADC, the Register name parameter will populate options such
as AdcaRegs, AdcbRegs, and so on.

### **Register field** — Select register filed `Unspecified` (default)

Select the Register field for the selected register group. The options are
populated based on the device family, register group, and register field selected.
For example, if the Register group is ADC and Register name is AdcaRegs, the
Register field parameter will populate options such as ADCCTL1, ADCCTL2,
ADCBURSTCTL, and so on.

### **Access register using** — Select register access `Specified bits` (default) | `Custom bits`

Select access register using specified bits or custom bits.

- **Specified bits:** Selecting specified bits will
  display all the registers bits fields in a table format in the Register bit
  fields parameter.
- **Custom bit fields:** Select custom bit fields when you
  want to access the bits position manually.

In case of specified bits, if you are accessing AdcaRegs.ADCCTL1 using the
Register Read/Write block, the parameter Register bit fields will display option
**All** the bits of the corresponding register in a table
format, such as INTPULSEPOS, ADCPWDNZ, ADCBSYCHN, and so on.

In case of custom bits, you need to manually specify the bit positions you want
to access in the form of cell array. For example, when bits to process parameters
is {[2,0],[5,3],[7,4]}, indicates accessing 3 ranges of bits. It generates three
inports or outports depending upon the Operation parameter type. The first port
will access bits from position 2 to position 0 of the corresponding register field
ADCCTL1. Similarly the second port will access bits from position 5 to position 3,
and the third port will access bits from position 7 to position 4.

### **Operation** — Select read or write operation `Read` (default) | `Write`

- **Read operation** - Select when you want to read data
  from registers. Read operation will generate the selected bit fields in the
  parameter **Register bit fields** or the **Bits to
  process** parameter as outports.
- **Write operation** - Select when you want to write data
  to registers. Write operation will generate the selected bit fields in the
  parameter **Register bit fields** or the **Bits to
  process** parameter as inports.

### **Insert code before/after** — Insert code before or after `None` (default) | `EALLOW/EDIS`

Select **EALLOW/EDIS** to access the write protected TI
registers.

### **Bit to process** — Specify custom bits `{[15,0]}|` (default)

Bit to process parameter accepts the cell array where each element is a
`1x2` array where the smaller number indicates the start bit
and larger number indicates the end bit. For example, when the custom bit is in
the following format **{[1], [2 3], [ 5 10 ], [11
16]}** then:

- From the custom bits mentioned, you are accessing four different set
  of bits I.e.

  - Bit 1
  - Bit 2 and Bit 3
  - Bit 5 to 10
  - Bit 11 to 16
- The specified custom bit will generate four different ports(inport or
  outport)

The corresponding ports generated for each element of cell array will access
the range of bits between the start bit and end bit.

**Note**

The bit position should be less than the length of the register field
accessed. Also there should not be any overlap of bit positions between any
2 entries of cell array.

#### Dependencies

To enable this parameter, set the **Access register
using** parameter to `Custom bits`.

### **Register bit fields** — Select bit field to access `All` (default)

Select bit field you want to access. The options for register bit fields are
populated based on the selection of register group, register field, and register
name.

#### Dependencies

To enable this parameter, set the **Access register
using** parameter to `Specified bits`.

## Libraries

C2000 Microcontroller Blockset / Memory Operations

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Read from or write to various bit fields of TI C2000 Registers

You can use the Register Read/Write block in C2000 Microcontroller Blockset to read data
from and write data to various bit fields of TI C2000 registers. The block depends on files
generated during hardware setup, which are determined by the selected processor and the CCS
version. If the parameters on the block are **Unspecified**, configure the
hardware setup using `c2000setup`.

You can also use the block to specify bit positions using custom bits. It accepts a cell
array where each element is a `1x2` array that specifies the start bit and
end bit.

**Note**

- Register Read/Write block depend upon CCS installation and register xmls
  present in CCS to populate various entries in the block. Some registers may not be
  available in CCS xmls and hence you will not be able to access them in the block.
  For example, the HRCAP in F2803x.
- When you try to modify the peripheral registers for different CPU cores, make
  sure that the CPU core has access to the particular peripheral, else the register
  read/write access may fail.
