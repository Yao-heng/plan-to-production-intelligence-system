# Dependency Graph

| Source | Target | Type | Rationale |
| --- | --- | --- | --- |
| External:Customer security profile | BIOS-REQ-001 | upstream | BIOS-REQ-001 lists upstream dependency Customer security profile. |
| External:TPM module AVL | BIOS-REQ-001 | upstream | BIOS-REQ-001 lists upstream dependency TPM module AVL. |
| BIOS-REQ-001 | VAL-REQ-001 | downstream | BIOS-REQ-001 lists downstream dependency VAL-REQ-001. |
| BIOS-REQ-001 | MFG-REQ-001 | downstream | BIOS-REQ-001 lists downstream dependency MFG-REQ-001. |
| BIOS-REQ-001 | Team:BMC | impacted_team | BMC is listed as an impacted team. |
| BIOS-REQ-001 | Team:Validation | impacted_team | Validation is listed as an impacted team. |
| BIOS-REQ-001 | Team:Program / Quality | impacted_team | Program / Quality is listed as an impacted team. |
| External:PSU firmware interface | BMC-REQ-001 | upstream | BMC-REQ-001 lists upstream dependency PSU firmware interface. |
| BMC-REQ-001 | External:VAL-REQ-002 | downstream | BMC-REQ-001 lists downstream dependency VAL-REQ-002. |
| BMC-REQ-001 | Team:BIOS | impacted_team | BIOS is listed as an impacted team. |
| BMC-REQ-001 | Team:Validation | impacted_team | Validation is listed as an impacted team. |
| BMC-REQ-001 | Team:Application | impacted_team | Application is listed as an impacted team. |
| External:Thermal sensor map | EC-REQ-001 | upstream | EC-REQ-001 lists upstream dependency Thermal sensor map. |
| EC-REQ-001 | External:VAL-REQ-003 | downstream | EC-REQ-001 lists downstream dependency VAL-REQ-003. |
| EC-REQ-001 | Team:BIOS | impacted_team | BIOS is listed as an impacted team. |
| EC-REQ-001 | Team:Validation | impacted_team | Validation is listed as an impacted team. |
| External:Device firmware release candidate | OS-REQ-001 | upstream | OS-REQ-001 lists upstream dependency Device firmware release candidate. |
| OS-REQ-001 | MFG-REQ-001 | downstream | OS-REQ-001 lists downstream dependency MFG-REQ-001. |
| OS-REQ-001 | Team:BIOS | impacted_team | BIOS is listed as an impacted team. |
| OS-REQ-001 | Team:Validation | impacted_team | Validation is listed as an impacted team. |
| OS-REQ-001 | Team:Factory / Diagnostics | impacted_team | Factory / Diagnostics is listed as an impacted team. |
| BIOS-REQ-001 | VAL-REQ-001 | upstream | VAL-REQ-001 lists upstream dependency BIOS-REQ-001. |
| VAL-REQ-001 | External:Customer FC signoff | downstream | VAL-REQ-001 lists downstream dependency Customer FC signoff. |
| VAL-REQ-001 | Team:BIOS | impacted_team | BIOS is listed as an impacted team. |
| VAL-REQ-001 | Team:Program / Quality | impacted_team | Program / Quality is listed as an impacted team. |
| BIOS-REQ-001 | MFG-REQ-001 | upstream | MFG-REQ-001 lists upstream dependency BIOS-REQ-001. |
| OS-REQ-001 | MFG-REQ-001 | upstream | MFG-REQ-001 lists upstream dependency OS-REQ-001. |
| MFG-REQ-001 | External:Production line pilot | downstream | MFG-REQ-001 lists downstream dependency Production line pilot. |
| MFG-REQ-001 | Team:BIOS | impacted_team | BIOS is listed as an impacted team. |
| MFG-REQ-001 | Team:BMC | impacted_team | BMC is listed as an impacted team. |
| MFG-REQ-001 | Team:Driver / OS | impacted_team | Driver / OS is listed as an impacted team. |
| MFG-REQ-001 | Team:Validation | impacted_team | Validation is listed as an impacted team. |
