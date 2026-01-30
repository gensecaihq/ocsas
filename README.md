# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-Profile-blue)](https://github.com/gensecaihq/ossasai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** (OpenClaw Security Assurance Standard) is the official [OSSASAI](https://github.com/gensecaihq/ossasai) implementation profile for [OpenClaw](https://openclaw.ai) — a WhatsApp, Telegram, Discord, iMessage, and Slack gateway for AI agents with shell, filesystem, and browser access.

## Quick Start

```bash
# Run security audit
openclaw security audit

# Deep audit with Gateway probe
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix
```

## What This Profile Does

OCSAS maps [OSSASAI](https://github.com/gensecaihq/ossasai)'s 24 security controls to OpenClaw's built-in features:

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

## Assurance Levels

| Level | Name | Configuration |
|-------|------|---------------|
| **L1** | Local-First | Loopback binding, basic auth, pairing |
| **L2** | Network-Aware | Tailscale/SSH, sandboxing, mention gating |
| **L3** | High-Assurance | Full sandboxing, strict session isolation |

## L1 Conformance Checklist

```bash
openclaw security audit --deep
```

- [ ] Gateway bound to loopback (`gateway.bind: "loopback"`)
- [ ] Gateway auth configured (token or password)
- [ ] DM policy set to `pairing` or `allowlist`
- [ ] File permissions correct (700/600 on `~/.openclaw/`)
- [ ] Log redaction enabled (`redactSensitive: "tools"`)

## Evidence Generation

```bash
mkdir -p evidence
openclaw security audit --deep 2>&1 | tee evidence/audit-report.txt
openclaw status --all > evidence/status-redacted.txt
openclaw sandbox explain > evidence/sandbox-config.txt
```

## Related

- **Parent Framework:** [OSSASAI](https://github.com/gensecaihq/ossasai) - Open Security Standard for Agentic Systems
- **Platform:** [OpenClaw](https://openclaw.ai)
- **Security Docs:** [docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security)

## License

Apache License 2.0

---

**OCSAS v0.1.0** | [OSSASAI](https://github.com/gensecaihq/ossasai) Profile for [OpenClaw](https://openclaw.ai)
