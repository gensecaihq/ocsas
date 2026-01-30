# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-Profile-blue)](https://ossasai.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** (OpenClaw Security Assurance Standard) is the official [OSSASAI](https://ossasai.org) implementation profile for [OpenClaw](https://openclaw.ai) — a WhatsApp, Telegram, Discord, iMessage, and Slack gateway for AI agents with shell, filesystem, and browser access.

## Overview

OCSAS provides a structured security verification framework that complements OpenClaw's built-in security features. It maps OSSASAI controls to OpenClaw's security architecture, CLI tooling, and formal verification suite.

### Key Features

- **Three Assurance Levels**: L1 (Local-First), L2 (Network-Aware), L3 (High-Assurance)
- **Four Trust Boundaries**: B1 (Inbound Identity), B2 (Control Plane), B3 (Tool Governance), B4 (Local State)
- **24 Security Controls**: Across 7 domains (CP, ID, TB, LS, SC, FV, NS)
- **Automated Auditing**: CLI-based security verification with `openclaw security audit`
- **Formal Verification**: TLA+/TLC models for security-critical paths

## Quick Start

```bash
# Run security audit
openclaw security audit

# Deep audit with Gateway probe
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix
```

## Documentation Structure

```
ocsas/
├── introduction.mdx          # Framework overview
├── spec/                     # Core specification
│   ├── overview.mdx          # OSSASAI specification
│   ├── assurance-levels.mdx  # L1/L2/L3 definitions
│   ├── trust-boundaries.mdx  # B1-B4 boundary definitions
│   └── compliance-workflow.mdx
├── threat-model/             # Threat analysis
│   ├── adversary-classes.mdx # A1-A5 adversary taxonomy
│   ├── ai-agent-threats.mdx  # AI-specific threats (AATT)
│   ├── attack-vectors.mdx    # Attack surface analysis
│   └── risk-scoring.mdx      # Blast radius framework
├── controls/                 # Security controls
│   ├── control-plane.mdx     # CP-01 to CP-04
│   ├── identity-session.mdx  # ID-01 to ID-03
│   ├── tool-blast-radius.mdx # TB-01 to TB-04
│   ├── local-state.mdx       # LS-01 to LS-04
│   ├── supply-chain.mdx      # SC-01 to SC-02
│   ├── formal-verification.mdx # FV-01 to FV-03
│   └── network-security.mdx  # NS-01 to NS-04
├── profiles/                 # Implementation profiles
│   └── openclaw.mdx          # OpenClaw-specific mappings
├── implementation/           # Deployment guides
├── testing/                  # Security testing
├── compliance/               # Compliance program
├── incident-response/        # IR procedures
├── tools/                    # Audit scripts
└── appendices/               # References & glossary
```

## Assurance Levels

| Level | Name | Use Case |
|-------|------|----------|
| **L1** | Local-First | Single-user, loopback-only deployments |
| **L2** | Network-Aware | Multi-user, LAN/Tailnet exposure |
| **L3** | High-Assurance | Production, public-facing, regulated environments |

## Control Domains

| Domain | ID | Controls | Description |
|--------|-------|----------|-------------|
| Control Plane | CP | 4 | Gateway exposure, authentication, proxy trust |
| Identity & Session | ID | 3 | Peer verification, session isolation, group policies |
| Tool Blast Radius | TB | 4 | Least privilege, approval gates, sandboxing, exfiltration |
| Local State | LS | 4 | Secrets protection, log redaction, memory safety, retention |
| Supply Chain | SC | 2 | Plugin trust, reproducible builds |
| Formal Verification | FV | 3 | Security invariants, negative models, CI integration |
| Network Security | NS | 4 | TLS, certificates, API security, mDNS discovery |

## Conformance

### L1 Baseline Checklist

- [ ] Gateway bound to loopback (`gateway.bind: "loopback"`)
- [ ] Gateway auth configured (token or password)
- [ ] DM policy set to `pairing` or `allowlist`
- [ ] Session isolation configured (`dmScope`)
- [ ] File permissions correct (700/600)
- [ ] Log redaction enabled (`redactSensitive: "tools"`)

### Verification

```bash
# Generate evidence
mkdir -p evidence
openclaw security audit --deep 2>&1 | tee evidence/audit-report.txt
openclaw status --all > evidence/status-redacted.txt
openclaw sandbox explain > evidence/sandbox-config.txt
```

## Formal Verification

Security-critical paths are verified using TLA+/TLC models:

```bash
git clone https://github.com/vignesh07/openclaw-formal-models
cd openclaw-formal-models
make gateway-exposure-v2
make nodes-pipeline
make pairing
```

## Standards Mapping

OCSAS controls map to established security frameworks:

| Standard | Mapping |
|----------|---------|
| OWASP ASVS v4.0 | Authentication, Session Management, Access Control |
| NIST SP 800-53 | AC, AU, CM, IA, SC families |
| CIS Controls v8 | Controls 3, 4, 5, 6, 12, 16 |
| MITRE ATT&CK | Initial Access, Execution, Persistence, Exfiltration |

## Related Resources

- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenClaw Security Guide](https://docs.openclaw.ai/gateway/security)
- [OpenClaw Formal Verification](https://docs.openclaw.ai/security/formal-verification/)
- [OSSASAI Specification](https://ossasai.org)

## Contributing

Contributions are welcome. Please read the contribution guidelines before submitting pull requests.

## License

Apache License 2.0 - See [LICENSE](LICENSE) for details.

---

**OCSAS v0.1.0** | January 2025 | [OSSASAI](https://ossasai.org) Implementation Profile
