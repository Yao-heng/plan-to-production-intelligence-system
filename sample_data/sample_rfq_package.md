# Sample RFQ Package

## BIOS-REQ-001: Secure Boot and TPM Measurement Enablement
- **Description**: Enable UEFI Secure Boot with TPM PCR measurements for production server platforms.
- **Owner Team**: BIOS
- **Impacted Teams**: BMC, Validation, Program / Quality
- **Upstream Dependency**: Customer security profile, TPM module AVL
- **Downstream Dependency**: VAL-REQ-001, MFG-REQ-001
- **Milestone**: EVT
- **Acceptance Criteria**: Secure Boot enabled by default, TPM event log verified, recovery path documented
- **Status**: Open
- **Priority**: P1
- **Risk If Late**: High

## BMC-REQ-001: Redfish Power Telemetry
- **Description**: Provide BMC Redfish endpoints for power telemetry, PSU status, and event log export.
- **Owner Team**: BMC
- **Impacted Teams**: BIOS, Validation, Application
- **Upstream Dependency**: PSU firmware interface
- **Downstream Dependency**: VAL-REQ-002
- **Milestone**: DVT
- **Acceptance Criteria**: Redfish schema validated, telemetry polling under 2 seconds, SEL export verified
- **Status**: Open
- **Priority**: P1
- **Risk If Late**: Medium

## EC-REQ-001: Thermal Table Coordination
- **Description**: EC firmware shall coordinate fan curve and thermal table behavior with BIOS platform policy.
- **Owner Team**: EC
- **Impacted Teams**: BIOS, Validation
- **Upstream Dependency**: Thermal sensor map
- **Downstream Dependency**: VAL-REQ-003
- **Milestone**: EVT
- **Acceptance Criteria**: Fan curve validated, thermal trip behavior verified, AC loss recovery tested
- **Status**: Blocked
- **Priority**: P1
- **Risk If Late**: High

## OS-REQ-001: Linux Driver Readiness
- **Description**: Deliver Linux kernel driver package and OS validation notes for storage and network devices.
- **Owner Team**: Driver / OS
- **Impacted Teams**: BIOS, Validation, Factory / Diagnostics
- **Upstream Dependency**: Device firmware release candidate
- **Downstream Dependency**: MFG-REQ-001
- **Milestone**: DVT
- **Acceptance Criteria**: Driver package signed, device enumeration verified, installation guide published
- **Status**: Open
- **Priority**: P2
- **Risk If Late**: Medium

## VAL-REQ-001: Security Feature Validation
- **Description**: Validation team shall run secure boot, TPM, and firmware resiliency test coverage.
- **Owner Team**: Validation
- **Impacted Teams**: BIOS, Program / Quality
- **Upstream Dependency**: BIOS-REQ-001
- **Downstream Dependency**: Customer FC signoff
- **Milestone**: DVT
- **Acceptance Criteria**: Test plan approved, all P1 tests executed, defects triaged within 24 hours
- **Status**: Open
- **Priority**: P1
- **Risk If Late**: High

## MFG-REQ-001: Factory Diagnostic Package
- **Description**: Manufacturing diagnostic flow shall verify boot, TPM presence, NIC link, and BMC sensor data.
- **Owner Team**: Factory / Diagnostics
- **Impacted Teams**: BIOS, BMC, Driver / OS, Validation
- **Upstream Dependency**: BIOS-REQ-001, OS-REQ-001
- **Downstream Dependency**: Production line pilot
- **Milestone**: PVT
- **Acceptance Criteria**: Diagnostic image released, factory log format approved, pilot yield report generated
- **Status**: Open
- **Priority**: P1
- **Risk If Late**: High
