# Changelog

All notable changes to OCSAS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-30

### Added

- Initial release of OCSAS (OpenClaw Security Assurance Standard)
- Complete OSSASAI implementation profile for OpenClaw
- Control mappings for all 24 OSSASAI controls:
  - **Control Plane (CP):** CP-01 through CP-04
  - **Identity & Session (ID):** ID-01 through ID-03
  - **Tool Blast Radius (TB):** TB-01 through TB-04
  - **Local State (LS):** LS-01 through LS-04
  - **Supply Chain (SC):** SC-01 through SC-02
  - **Formal Verification (FV):** FV-01 through FV-03
  - **Network Security (NS):** NS-01 through NS-04
- L1/L2/L3 conformance recipes with checklists
- Evidence generation procedures
- Incident response guidance
- Mintlify documentation configuration

### Verified

- All CLI commands verified against OpenClaw documentation
- All configuration keys verified against OpenClaw source
- All file paths verified against OpenClaw architecture

## Links

- [OSSASAI Framework](https://github.com/gensecaihq/ossasai)
- [OpenClaw](https://openclaw.ai)
- [OpenClaw Security Docs](https://docs.openclaw.ai/gateway/security)
