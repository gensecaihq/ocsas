#!/usr/bin/env python3
"""
OSSASAI Compliance Report Generator

Generates compliance reports from audit results in various formats.

Usage:
    python ossasai-report.py --assessment audit.json --output report.pdf
    python ossasai-report.py --assessment audit.json --format yaml --output statement.yaml
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

VERSION = "1.0.0"

def load_assessment(path: str) -> Dict[str, Any]:
    """Load assessment results from JSON file."""
    with open(path, 'r') as f:
        return json.load(f)

def generate_text_report(assessment: Dict[str, Any], evidence_path: Optional[str] = None) -> str:
    """Generate text-format compliance report."""
    summary = assessment.get('summary', {})
    controls = assessment.get('controls', [])

    report = []
    report.append("=" * 60)
    report.append("OSSASAI COMPLIANCE REPORT")
    report.append("=" * 60)
    report.append("")
    report.append(f"Generated: {datetime.utcnow().isoformat()}Z")
    report.append(f"Target Level: {assessment.get('assessment', {}).get('target_level', 'Unknown')}")
    report.append("")
    report.append("-" * 60)
    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 60)
    report.append(f"Total Controls: {summary.get('total_controls', 0)}")
    report.append(f"Passing: {summary.get('passing', 0)}")
    report.append(f"Failing: {summary.get('failing', 0)}")
    report.append(f"Compliance: {summary.get('compliance_percentage', 0)}%")
    report.append("")

    status = "ACHIEVED" if summary.get('failing', 1) == 0 else "NOT ACHIEVED"
    report.append(f"Status: {status}")
    report.append("")

    report.append("-" * 60)
    report.append("CONTROL RESULTS")
    report.append("-" * 60)

    for control in controls:
        status_symbol = "[PASS]" if control.get('status') == 'PASS' else "[FAIL]"
        report.append(f"{status_symbol} {control.get('id', 'Unknown')}")
        if control.get('status') != 'PASS' and control.get('finding'):
            report.append(f"         Finding: {control.get('finding')}")

    report.append("")
    report.append("-" * 60)
    report.append("END OF REPORT")
    report.append("-" * 60)

    return "\n".join(report)

def generate_json_report(assessment: Dict[str, Any], evidence_path: Optional[str] = None) -> str:
    """Generate JSON-format compliance report."""
    report = {
        "report_version": VERSION,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "assessment": assessment.get('assessment', {}),
        "summary": assessment.get('summary', {}),
        "controls": assessment.get('controls', []),
        "evidence_path": evidence_path
    }
    return json.dumps(report, indent=2)

def generate_yaml_statement(assessment: Dict[str, Any]) -> str:
    """Generate YAML compliance statement."""
    summary = assessment.get('summary', {})
    target_level = assessment.get('assessment', {}).get('target_level', 'L1')

    failing = summary.get('failing', 0)
    status = "conformant" if failing == 0 else "non_conformant"

    statement = f"""# OCSAS Compliance Statement
# Generated: {datetime.utcnow().isoformat()}Z

compliance_statement:
  schema_version: "1.0"

  assessment:
    ocsas_version: "1.0.0"
    assurance_level: "{target_level}"
    date: "{datetime.utcnow().strftime('%Y-%m-%d')}"
    tool_version: "{VERSION}"

  results:
    status: "{status}"
    controls:
      total: {summary.get('total_controls', 0)}
      passed: {summary.get('passing', 0)}
      failed: {failing}
    compliance_percentage: {summary.get('compliance_percentage', 0)}

  validity:
    effective_date: "{datetime.utcnow().strftime('%Y-%m-%d')}"
    # Validity period: 12 months from assessment date
"""
    return statement

def generate_junit_report(assessment: Dict[str, Any]) -> str:
    """Generate JUnit XML format for CI integration."""
    controls = assessment.get('controls', [])
    summary = assessment.get('summary', {})

    xml_parts = []
    xml_parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    xml_parts.append(f'<testsuite name="OCSAS Compliance" tests="{summary.get("total_controls", 0)}" '
                    f'failures="{summary.get("failing", 0)}" errors="0" '
                    f'timestamp="{datetime.utcnow().isoformat()}">')

    for control in controls:
        ctrl_id = control.get('id', 'unknown')
        status = control.get('status', 'UNKNOWN')

        xml_parts.append(f'  <testcase name="{ctrl_id}" classname="ocsas.controls">')
        if status != 'PASS':
            finding = control.get('finding', 'Control failed')
            xml_parts.append(f'    <failure message="{finding}"/>')
        xml_parts.append('  </testcase>')

    xml_parts.append('</testsuite>')

    return "\n".join(xml_parts)

def main():
    parser = argparse.ArgumentParser(description='OCSAS Compliance Report Generator')
    parser.add_argument('--assessment', required=True, help='Path to assessment JSON file')
    parser.add_argument('--evidence', help='Path to evidence directory')
    parser.add_argument('--format', choices=['text', 'json', 'yaml', 'junit'], default='text',
                       help='Output format (default: text)')
    parser.add_argument('--output', help='Output file path (default: stdout)')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')

    args = parser.parse_args()

    try:
        assessment = load_assessment(args.assessment)
    except Exception as e:
        print(f"Error loading assessment: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate report in requested format
    if args.format == 'text':
        report = generate_text_report(assessment, args.evidence)
    elif args.format == 'json':
        report = generate_json_report(assessment, args.evidence)
    elif args.format == 'yaml':
        report = generate_yaml_statement(assessment)
    elif args.format == 'junit':
        report = generate_junit_report(assessment)
    else:
        print(f"Unknown format: {args.format}", file=sys.stderr)
        sys.exit(1)

    # Output report
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report written to: {args.output}")
    else:
        print(report)

if __name__ == '__main__':
    main()
