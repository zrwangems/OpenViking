---
type: simulink-block
title: 'C2803x LIN Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c2803xlintransmit'
documentation_source_path: 'ref/c2803xlintransmit.html'
language: en
---

# C2803x LIN Transmit

## Ports

Not documented in R2025b.

## Parameters

**Send checksum**
:   Select this checkbox to include a checksum in the last data field of the
    checkbyte. LIN 2.0 implementations require this checksum.

    The default value is unchecked (disabled).

**Physical bus error interrupt**
:   The LIN controller node detects when the physical bus
    cannot convey a valid message. For example, if the bus had a short circuit to ground
    or to VBAT. This raises a physical bus error flag in
    all of the LIN nodes on the network. If you enable
    **Physical bus error interrupt**, the LIN transmit node generates
    an interrupt in response to a physical bus error flag.

**Bit error interrupt**
:   If you enable this option, the LIN node compares the data it transmits and the
    data on the LIN bus.

    The default value is `Disabled`.

    The TXRX Error Detector Bit Monitor compares data bits on the LIN transmit (LINTX)
    and receive (LINRX) pins. If the data do not match, the Bit Monitor raises a bit-error
    flag. When you enable this option, the bit-error flag also produces a bit-error
    interrupt.

**Transmit buffer interrupt**
:   If you enable this option, the LIN node generates an interrupt while it is
    generating a checksum and setting the Transmitter buffer register ready flag.

    The default value is `Disabled`.

**Send checksum**
:   Select this checkbox to include a checksum in the last data field of the
    checkbyte. LIN 2.0 implementations require this checksum.

    The default value is unchecked (disabled).

**Physical bus error interrupt**
:   The LIN controller node detects when the physical bus
    cannot convey a valid message. For example, if the bus had a short circuit to ground
    or to VBAT. This raises a physical bus error flag in
    all of the LIN nodes on the network. If you enable
    **Physical bus error interrupt**, the LIN transmit node generates
    an interrupt in response to a physical bus error flag.

**Bit error interrupt**
:   If you enable this option, the LIN node compares the data it transmits and the
    data on the LIN bus.

    The default value is `Disabled`.

    The TXRX Error Detector Bit Monitor compares data bits on the LIN transmit (LINTX)
    and receive (LINRX) pins. If the data do not match, the Bit Monitor raises a bit-error
    flag. When you enable this option, the bit-error flag also produces a bit-error
    interrupt.

**Transmit buffer interrupt**
:   If you enable this option, the LIN node generates an interrupt while it is
    generating a checksum and setting the Transmitter buffer register ready flag.

    The default value is `Disabled`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Transmit data from target via serial communications interface (SCI) to host

# C2803x LIN Transmit

Transmit data from target via serial communications interface (SCI) to
host

The Local Interconnect Network (LIN) bus implements a serial communications protocol for
distributed automotive and industrial applications. In particular, LIN serves low cost
applications that do not require the bandwidth or robustness provided by the CAN
protocol.

The C2803x LIN Transmit block takes three inputs:

- **ID**: Set the value of the LIN ID for the LIN transmit
  node.
- **TX ID Mask**: Set the value of the LIN ID mask for the LIN
  transmit node.
- **Data**: Connect this input to the data source.

**Note**

Many LIN-specific settings are located under **Peripherals** >
**LIN** in **Hardware Implementation** >
**Target hardware resources** for your model. Verify that these
settings meet the requirements of your application.

- C2803x LIN Transmit block
