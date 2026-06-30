# Sample RFQ Package

## Project Name

AI Server Platform X100

## Product Overview

AI Server Platform X100 is a next-generation rack-scale AI compute platform designed for enterprise AI training, inference, and cloud infrastructure deployments.

The platform integrates high-performance CPUs, multiple AI accelerators, high-speed networking, redundant power, advanced thermal control, secure firmware, remote manageability, and production-ready validation coverage.

This sample RFQ package is fictional and is designed for demonstrating the Plan-to-Production Intelligence System.

---

## Platform Scope

The platform includes the following functional areas:

* BIOS / UEFI
* BMC firmware
* EC / MCU firmware
* PCIe device enablement
* GPU / accelerator readiness
* OS and driver integration
* System image readiness
* Thermal control
* Fan table support
* Redfish / IPMI management
* Factory diagnostics
* Validation automation
* Production readiness
* Sustaining handoff

---

## Business Requirements

### BR-001: Production Schedule

The platform must reach Feature Complete by 2026-09-15 and Production Readiness by 2026-11-30.

### BR-002: Product Quality

All Sev1 and gating issues must be closed before Production Readiness. Sev2 issues require approved recovery plans before release.

### BR-003: Customer Readiness

The platform must support remote management, validation diagnostics, firmware update capability, and system health monitoring before customer qualification.

---

## BIOS Requirements

### BIOS-REQ-001: PCIe Topology Initialization

BIOS must correctly initialize all PCIe root ports, risers, GPU slots, storage devices, and network adapters according to the platform topology.

Owner Team: BIOS
Impacted Teams: EE, GPU, Driver, Validation
Milestone: Feature Complete

### BIOS-REQ-002: Fan Table Integration

BIOS must consume fan table data provided by the Thermal team and expose required thermal control interfaces for platform validation.

Owner Team: BIOS
Upstream Dependency: Thermal
Downstream Dependency: Validation
Milestone: Feature Complete

### BIOS-REQ-003: Graphics Output Configuration

BIOS must support the required graphics output configuration and platform display policy based on input from the Graphics team.

Owner Team: BIOS
Upstream Dependency: Graphics
Downstream Dependency: OS, Driver, Validation
Milestone: Feature Complete

### BIOS-REQ-004: Secure Boot

BIOS must support secure boot enablement and validation-ready default configuration.

Owner Team: BIOS
Impacted Teams: OS, Security, Validation
Milestone: Feature Complete

---

## BMC Requirements

### BMC-REQ-001: Redfish Management

BMC must support Redfish APIs for inventory, power state, firmware version, sensor status, and system health reporting.

Owner Team: BMC
Impacted Teams: Validation, Customer Support
Milestone: Feature Complete

### BMC-REQ-002: IPMI Compatibility

BMC must maintain IPMI command compatibility for legacy management workflows.

Owner Team: BMC
Impacted Teams: Validation, Customer Support
Milestone: Feature Complete

### BMC-REQ-003: Sensor Telemetry

BMC must collect and report CPU, GPU, memory, power, fan, and thermal telemetry.

Owner Team: BMC
Upstream Dependency: Thermal, EE
Downstream Dependency: Validation, Diagnostics
Milestone: Feature Complete

---

## EC / MCU Requirements

### EC-REQ-001: Power Sequencing

EC / MCU firmware must support platform power sequencing according to the hardware design guide.

Owner Team: EC
Impacted Teams: BIOS, EE, Validation
Milestone: Feature Complete

### EC-REQ-002: Recovery Behavior

EC / MCU firmware must support recovery behavior for abnormal power events and thermal emergency cases.

Owner Team: EC
Impacted Teams: BMC, BIOS, Validation
Milestone: Pilot

---

## Driver and OS Requirements

### OS-REQ-001: Driver Package Readiness

All required device drivers must be included in the OS image before pilot validation.

Owner Team: Driver / OS
Impacted Teams: System Image, Validation
Milestone: Pilot

### OS-REQ-002: System Health Agent

The OS image must include a system health agent capable of collecting platform logs and basic telemetry.

Owner Team: OS / Application
Impacted Teams: BMC, Diagnostics, Customer Support
Milestone: Pilot

---

## Validation Requirements

### VAL-REQ-001: Feature Complete Validation

Validation team must prepare FC validation test cases based on BIOS, BMC, EC, Driver, OS, and Application feature checklists.

Owner Team: Validation
Upstream Dependency: BIOS, BMC, EC, Driver, OS, Application
Milestone: Feature Complete

### VAL-REQ-002: Long Run Stress Test

Validation team must complete long-run and stress testing on DVT hardware before Production Readiness.

Owner Team: Validation
Upstream Dependency: DVT Hardware, BIOS, BMC, Driver, OS
Milestone: Pilot

---

## Factory and Production Requirements

### MFG-REQ-001: Factory Diagnostic Tool

Factory diagnostic tool must support BIOS version check, BMC version check, sensor check, PCIe device enumeration, and basic stress test.

Owner Team: Factory / Diagnostics
Upstream Dependency: BIOS, BMC, Driver, OS
Milestone: Production Readiness

### MFG-REQ-002: Production Build Exit

All gating issues must be closed or approved by AQE, manufacturing, validation, and program leadership before production build exit.

Owner Team: Program / Quality
Impacted Teams: AQE, Manufacturing, Validation, BIOS, BMC, Driver, OS
Milestone: Production Readiness
