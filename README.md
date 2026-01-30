# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-v0.1-blue)](https://github.com/gensecaihq/ossasai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** is the official [OSSASAI](https://github.com/gensecaihq/ossasai) implementation profile for [OpenClaw](https://openclaw.ai) — a multi-platform AI agent gateway for WhatsApp, Telegram, Discord, iMessage, and Slack with shell, filesystem, and browser access.

## Overview

OCSAS maps OSSASAI's 24 security controls to OpenClaw's built-in security features, providing structured verification for secure AI agent deployments.

```
OSSASAI (Framework)          OCSAS (This Profile)           OpenClaw (Platform)
─────────────────────        ────────────────────           ───────────────────
24 Security Controls    →    Control Mappings          →    CLI & Config
L1/L2/L3 Levels         →    Conformance Recipes       →    Security Audit
Trust Boundaries        →    Verification Steps        →    Built-in Features
```

## Quick Start

```bash
# Verify your OpenClaw deployment
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix

# Check sandbox configuration
openclaw sandbox explain
```

## Control Mappings

| OSSASAI Control | OpenClaw Implementation |
|-----------------|-------------------------|
| **CP-01** Default-Deny Exposure | `gateway.bind: "loopback"` |
| **CP-02** Strong Authentication | `gateway.auth.mode: "token"` |
| **ID-01** Peer Verification | `dmPolicy: "pairing"` |
| **ID-02** Session Isolation | `session.dmScope: "per-channel-peer"` |
| **TB-01** Least Privilege Tools | `agents.list[].tools.allow/deny` |
| **TB-03** Sandboxing | `agents.defaults.sandbox.mode: "non-main"` |
| **LS-01** Secrets at Rest | `~/.openclaw/` permissions (700/600) |
| **LS-02** Log Redaction | `logging.redactSensitive: "tools"` |
| **NS-04** mDNS Security | `discovery.mdns.mode: "minimal"` |

[View complete mappings →](profiles/openclaw.mdx)

## Assurance Levels

| Level | Name | When to Use |
|-------|------|-------------|
| **L1** | Local-First | Single-user, loopback-only, development |
| **L2** | Network-Aware | Multi-user, LAN/Tailnet, team deployments |
| **L3** | High-Assurance | Production, public exposure, regulated environments |

### L1 Checklist

```bash
openclaw security audit --deep
```

- [ ] Gateway bound to loopback
- [ ] Gateway auth configured
- [ ] DM policy set to `pairing` or `allowlist`
- [ ] File permissions correct (700/600)
- [ ] Log redaction enabled

### L2 Checklist (includes L1)

- [ ] Trusted proxies configured (if applicable)
- [ ] Mention gating enabled for groups
- [ ] Sandboxing enabled for non-main sessions
- [ ] Elevated exec restricted

### L3 Checklist (includes L2)

- [ ] Strictest session isolation
- [ ] All sessions sandboxed
- [ ] mDNS discovery disabled
- [ ] No workspace access from sandbox

## Evidence Generation

```bash
mkdir -p evidence
openclaw security audit --deep 2>&1 | tee evidence/audit.txt
openclaw status --all > evidence/status.txt
openclaw sandbox explain > evidence/sandbox.txt
ls -la ~/.openclaw/ > evidence/permissions.txt
```

## Documentation

| Document | Description |
|----------|-------------|
| [profiles/openclaw.mdx](profiles/openclaw.mdx) | Complete control mappings |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [SECURITY.md](SECURITY.md) | Security policy |

## Related Projects

| Project | Description |
|---------|-------------|
| [OSSASAI](https://github.com/gensecaihq/ossasai) | Parent security framework |
| [OpenClaw](https://openclaw.ai) | AI agent gateway platform |
| [OpenClaw Docs](https://docs.openclaw.ai/gateway/security) | Security documentation |

## Contributing

Contributions welcome. Please ensure:

1. Changes align with OSSASAI framework
2. All claims are verified against OpenClaw documentation
3. No placeholder or fictional information

## License

[Apache License 2.0](LICENSE)

---

**OCSAS v0.1.0** | [OSSASAI](https://github.com/gensecaihq/ossasai) Profile | [OpenClaw](https://openclaw.ai)
