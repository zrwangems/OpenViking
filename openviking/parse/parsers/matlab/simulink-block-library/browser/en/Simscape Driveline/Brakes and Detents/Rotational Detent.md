---
type: simulink-block
title: 'Rotational Detent'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Brakes and Detents'
documentation_page: 'rotationaldetent'
documentation_source_path: 'ref/rotationaldetent.html'
language: en
---

# Rotational Detent

## Ports

**R** and **C** are rotational conserving ports
associated with the rod and case, respectively.

## Parameters

### Detent Characteristics

**Parameterization**
:   Select how to specify the detent characteristics. The default is
    `By peak torque and notch width`.

    - `By peak torque and notch width` —
      Specify detent characteristics by the peak torque and the notch
      width.

       Peak Torque and Notch Width

      **Peak torque**
      :   The peak torque developed inside the detent.
          The default is `0.25`.

          From the drop-down list, choose units. The
          default is newton-meters
          (`N*m`).

      **Notch width**
      :   The width of the region where the torque
          develops. The default is
          `5`.

          From the drop-down list, choose units. The
          default is degrees
          (`deg`).
    - `By table lookup` — Define the detent
      characteristics by one-dimensional table lookup based on the
      relative displacement between the slider and case. If you select
      this option, the panel changes from its default option.

       Table Lookup

      **Relative rotation vector**
      :   Specify the vector of input relative rotations
          that correspond to the values in **Torque
          vector**. These two vectors must be of
          the same size. The angles must be specified in
          strictly increasing order. The default values are
          `[-5.0 -4.0 -3.0 -1.0 1.0 3.0 4.0
          5.0]`.

          From the drop-down list, choose units. The
          default is degrees
          (`deg`).

      **Torque vector**
      :   Specify the vector of input values for the
          developed torque that correspond to the values in
          **Relative rotation vector**. The
          default values are `[0 0 -0.25 -0.10 0.10
          0.25 0 0]`.

          From the drop-down list, choose units. The
          default is newton-meters
          (`N*m`).

      **Initial relative rotation**
      :   The relative angle of the rod and case when
          simulation starts. The default is
          `0`.

          From the drop-down list, choose units. The
          default is degrees
          (`deg`).

      **Interpolation method**
      :   Select one of these interpolation methods for
          approximating the output value when the input
          value is between two consecutive grid
          points:

          - `Linear` —
            Select this, default, option to get the best
            performance.
          - `Smooth` —
            Select this option to produce a continuous curve
            with continuous first-order derivatives.

          For more information on interpolation
          algorithms, see the PS Lookup
          Table (1D) block reference page.

### Spacing

**Detent spacing**
:   Select how to specify the detent spacing. The default is
    `Regularly spaced`.

    - `Regularly spaced` — Specify detent
      spacing by regular intervals.

       Regular spacing

      **Number of detents**
      :   Specify the number of identical, regularly
          spaced detents. Must be greater than or equal to
          1. The default is `1`.

          Creates a number of detents evenly spaced from
          –180 to +180 degrees, with one detent center at 0
          degrees. Non-integer values are rounded to the
          nearest integer.
    - `By angle vector` — Specify detent
      spacing by custom intervals. If you select this option, the
      panel changes from its default option.

       Custom intervals

      **Vector of detent centers**
      :   Specify the locations of the centers of
          identical detents as a vector of angles. These
          values must lie between –180 and +180 degrees. The
          minimum spacing between the detents must be
          greater than the **Notch width**
          parameter. The default values are `[-40 0
          30 85]`.

          From the drop-down list, choose units. The
          default is degrees
          (`deg`).

### Friction

**Viscous friction coefficient**
:   Specify the viscous friction coefficient for the rod-case contact.
    Must be greater than or equal to 0. The default is
    `0.1`.

    From the drop-down list, choose units. The default is
    newton-meters/(radians/second) (`N*m/(rad/s)`).

**Friction to peak torque ratio**
:   Specify the kinetic friction coefficient for the rod-case contact.
    Must be greater than or equal to 0. The default is
    `0.01`.

    The kinetic friction is this ratio multiplied by the peak
    torque.

**Friction velocity threshold**
:   Specify the relative angular velocity required for peak kinetic
    friction in the detent. Must be greater than 0. The default is
    `10`.

    From the drop-down list, choose units. The default is
    revolutions/minute (`rpm`).

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

## Description

Double-sided, spring-loaded rotational detent

The Rotational Detent block represents a double-sided, spring-loaded rotational
detent.

The detent rod rotates over the detent case. The case has notches or magnets that
create a net relative torque with the rod as the rod rotates. With the block, you can
model rotational detents with peak torque and notch width, or with a table lookup. The
model also includes viscous damping and kinetic friction between the rod and case. You
can set the friction to zero.
