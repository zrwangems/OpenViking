---
type: simulink-block
title: 'C2802x/C2803x/C2806x/F28M3x COMP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c2802xc2803xc2806xf28m3xcomp'
documentation_source_path: 'ref/c2802xc2803xc2806xf28m3xcomp.html'
language: en
---

# C2802x/C2803x/C2806x/F28M3x COMP

## Ports

Not documented in R2025b.

## Parameters

**Comparator module**
:   Select the comparator module to configure. Use only one block per module.

**Second input**
:   Select `COMPxB` to compare the voltage of **Input Pin A** with **Input Pin B**

    Select `Internal DAC` to compare the voltage of **Input Pin A** with the output of a DAC reference located in the
    comparator. For more information, see the “DAC Reference” section of the
    *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter (ADC) and
    Comparator*.

    The comparator source outputs 1, if **Input Pin A** has a value
    greater than **Input Pin B** or the 10-bit DAC reference. Otherwise,
    it outputs 0.

**Invert comparator output**
:   Select this check box to apply a logical NOT to the output of the comparator
    source. For example, when the comparator source outputs 1, the circuit inverts it to
    0.

**Synchronization**
:   Select `Asynchronous` to pass the asynchronous version of the
    comparator output. Select `Synchronous` to pass the synchronous
    version of the comparator output. Selecting `Synchronous` enables the
    **Qualification period** option.

**Qualification period**
:   Qualify changes in the comparator output before passing them along. The
    `Passed through` setting passes changes in the comparator value
    along without qualifying them. The `consecutive clocks` settings pass
    changes in the comparator value along after receiving the specified number of
    consecutive samples with the same value. Use this setting to prevent intermittent and
    spurious changes in the comparator output.

**Sample time**
:   Specify the time interval between samples. To inherit sample time from the
    upstream block, set this parameter to -1.

**Comparator module**
:   Select the comparator module to configure. Use only one block per module.

**Second input**
:   Select `COMPxB` to compare the voltage of **Input Pin A** with **Input Pin B**

    Select `Internal DAC` to compare the voltage of **Input Pin A** with the output of a DAC reference located in the
    comparator. For more information, see the “DAC Reference” section of the
    *TMS320x2802x, 2803x Piccolo Analog-to-Digital Converter (ADC) and
    Comparator*.

    The comparator source outputs 1, if **Input Pin A** has a value
    greater than **Input Pin B** or the 10-bit DAC reference. Otherwise,
    it outputs 0.

**Invert comparator output**
:   Select this check box to apply a logical NOT to the output of the comparator
    source. For example, when the comparator source outputs 1, the circuit inverts it to
    0.

**Synchronization**
:   Select `Asynchronous` to pass the asynchronous version of the
    comparator output. Select `Synchronous` to pass the synchronous
    version of the comparator output. Selecting `Synchronous` enables the
    **Qualification period** option.

**Qualification period**
:   Qualify changes in the comparator output before passing them along. The
    `Passed through` setting passes changes in the comparator value
    along without qualifying them. The `consecutive clocks` settings pass
    changes in the comparator value along after receiving the specified number of
    consecutive samples with the same value. Use this setting to prevent intermittent and
    spurious changes in the comparator output.

**Sample time**
:   Specify the time interval between samples. To inherit sample time from the
    upstream block, set this parameter to -1.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Compare two input voltages on comparator pins

# C2802x/C2803x/C2806x/F28M3x COMP

Compare two input voltages on comparator pins

Configure the comparator module to output the comparison result on the comparator pins
of the processor.

- C2802x/C2803x/C2806x/F28M3x COMP block

##
