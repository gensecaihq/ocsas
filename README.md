# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-Profile-blue)](https://github.com/gensecaihq/ossasai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** (OpenClaw Security Assurance Standard) is the official [OSSASAI](https://github.com/gensecaihq/ossasai) implementation profile for [OpenClaw](https://openclaw.ai) — a WhatsApp, Telegram, Discord, iMessage, and Slack gateway for AI agents with shell, filesystem, and browser access.

> **Parent Framework:** This profile implements [OSSASAI](https://github.com/gensecaihq/ossasai) (Open Security Standard for Agentic Systems) — a vendor-neutral security framework for AI agent systems.

## Overview

OCSAS maps OSSASAI's 24 security controls to OpenClaw's built-in security features:

- **DM Policies** (pairing, allowlist, open, disabled)
- **Session Isolation** (dmScope configuration)
- **Docker Sandboxing** (mode, scope, workspace access)
- **Gateway Authentication** (token/password, Tailscale identity)
- **Tool Governance** (allow/deny lists, elevated exec gates)
- **Security Audit CLI** (`openclaw security audit`)

## Quick Start

```bash
# Run security audit
openclaw security audit

# Deep audit with Gateway probe
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix

# Explain sandbox configuration
openclaw sandbox explain
```

## Relationship to OSSASAI

```
┌─────────────────────────────────────────────────────────┐
│                       OSSASAI                            │
│     Open Security Standard for Agentic Systems          │
│     github.com/gensecaihq/ossasai                       │
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐        │
│  │ Spec       │  │ Threat     │  │ Controls   │        │
│  │ L1/L2/L3   │  │ Model      │  │ 24 total   │        │
│  └────────────┘  └────────────┘  └────────────┘        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                        OCSAS                             │
│       OpenClaw Security Assurance Standard              │
│       github.com/gensecaihq/ocsas (this repo)           │
│                                                          │
│  Maps OSSASAI controls to OpenClaw features:            │
│  • dmPolicy, dmScope, allowFrom                         │
│  • agents.defaults.sandbox.*                            │
│  • gateway.auth, gateway.bind                           │
│  • tools.elevated, tools.allow/deny                     │
│  • openclaw security audit CLI                          │
└─────────────────────────────────────────────────────────┘
```

## Documentation Structure

```
ocsas/
├── profiles/
│   └── openclaw.mdx          # OpenClaw-specific control mappings
├── spec/                     # OSSASAI spec (reference)
├── threat-model/             # OSSASAI threat model (reference)
├── controls/                 # OSSASAI controls (reference)
├── implementation/           # Deployment guides
├── testing/                  # Security testing
├── compliance/               # Compliance program
├── incident-response/        # IR procedures
├── tools/                    # Audit scripts
└── appendices/               # Standards mapping, glossary
```

## Assurance Levels

| Level | Name | OpenClaw Configuration |
|-------|------|------------------------|
| **L1** | Local-First | `gateway.bind: "loopback"`, basic auth |
| **L2** | Network-Aware | Tailscale/SSH tunnel, sandboxing enabled |
| **L3** | High-Assurance | Full sandboxing, formal verification |

## Control Mapping Summary

| OSSASAI Control | OpenClaw Feature |
|-----------------|------------------|
| CP-01: Default-Deny Exposure | `gateway.bind: "loopback"` |
| CP-02: Strong Auth | `gateway.auth.mode: "token"` |
| ID-01: Peer Verification | `dmPolicy: "pairing"` |
| ID-02: Session Isolation | `session.dmScope` |
| TB-01: Least Privilege | `agents.list[].tools.allow/deny` |
| TB-03: Sandboxing | `agents.defaults.sandbox.mode` |
| LS-01: Secrets Protection | `~/.openclaw/` permissions |
| LS-02: Log Redaction | `logging.redactSensitive` |
| NS-04: mDNS Security | `discovery.mdns.mode` |

See [profiles/openclaw.mdx](profiles/openclaw.mdx) for complete mappings.

## L1 Conformance Checklist

```bash
# Verify these settings for L1 compliance
openclaw security audit --deep
```

- [ ] Gateway bound to loopback (`gateway.bind: "loopback"`)
- [ ] Gateway auth configured (token or password)
- [ ] DM policy set to `pairing` or `allowlist`
- [ ] Session isolation configured (`dmScope`)
- [ ] File permissions correct (700/600 on `~/.openclaw/`)
- [ ] Log redaction enabled (`redactSensitive: "tools"`)

## Evidence Generation

```bash
# Create evidence directory
mkdir -p evidence

# Full security audit
openclaw security audit --deep 2>&1 | tee evidence/audit-report.txt

# Safe diagnostic (secrets redacted)
openclaw status --all > evidence/status-redacted.txt

# Permission check
ls -la ~/.openclaw/ > evidence/permissions.txt

# Sandbox configuration
openclaw sandbox explain > evidence/sandbox-config.txt
```

## Related Resources

- **Parent Framework:** [OSSASAI](https://github.com/gensecaihq/ossasai) - Open Security Standard for Agentic Systems
- **Platform:** [OpenClaw](https://openclaw.ai) - AI agent gateway
- **Security Docs:** [docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security)
- **Sandboxing:** [docs.openclaw.ai/gateway/sandboxing](https://docs.openclaw.ai/gateway/sandboxing)

## Contributing

Contributions welcome. Please ensure changes align with the parent OSSASAI framework.

## License

Apache License 2.0 - See [LICENSE](LICENSE) for details.

---

**OCSAS v0.1.0** | January 2025 | [OSSASAI](https://github.com/gensecaihq/ossasai) Implementation Profile for [OpenClaw](https://openclaw.ai)
