# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in OCSAS documentation or tooling, please report it responsibly:

1. **Do not** open a public GitHub issue
2. Email: security@gensecai.com
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work with you to address the issue.

## Scope

This security policy covers:

- OCSAS profile documentation
- Configuration examples
- Audit scripts and tooling

For vulnerabilities in OpenClaw itself, please report to: security@openclaw.ai

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Security Best Practices

When implementing OCSAS:

1. **Start with L1** - Verify baseline controls before expanding exposure
2. **Run audits regularly** - `openclaw security audit --deep`
3. **Keep secrets secure** - Never commit credentials or tokens
4. **Use pairing** - Default to `dmPolicy: "pairing"` for new deployments
5. **Enable sandboxing** - Use Docker isolation for untrusted contexts
