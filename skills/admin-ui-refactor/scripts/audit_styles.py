#!/usr/bin/env python3
"""
Admin Page Style Audit Script

Analyzes admin PHP pages to identify:
- Inline styles that should use design system classes
- Inconsistent color usage
- Missing design system classes
- Tables, forms, buttons needing refactoring

Usage:
    python audit_styles.py <path_to_php_file>
    python audit_styles.py adm_cw/member_list_bri.php
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


# Design system colors
DESIGN_COLORS = {
    '#003179': '--color-primary-1',
    '#0046ac': '--color-primary-2',
    '#f1f3f7': '--color-primary-bg',
    '#f9f9f9': '--color-gray-100',
    '#dddddd': '--color-gray-200',
    '#f2f2f2': '--color-gray-400',
    '#000000': '--color-black',
    '#ffffff': '--color-white',
    '#ff0004': '--color-warning',
}


def analyze_file(file_path):
    """Analyze a PHP file for style issues."""

    if not Path(file_path).exists():
        print(f"❌ Error: File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    print(f"\n{'='*70}")
    print(f"📋 Style Audit Report: {Path(file_path).name}")
    print(f"{'='*70}\n")

    # Track findings
    findings = {
        'inline_styles': [],
        'tables': [],
        'buttons': [],
        'forms': [],
        'colors': [],
        'typography': [],
    }

    # Analyze line by line
    for i, line in enumerate(lines, 1):
        line_num = i

        # Find inline styles
        inline_styles = re.findall(r'style=["\'](.*?)["\']', line)
        if inline_styles:
            for style in inline_styles:
                findings['inline_styles'].append((line_num, style, line.strip()))

        # Find tables without design system classes
        if '<table' in line and 'admin-table' not in line:
            findings['tables'].append((line_num, line.strip()))

        # Find buttons without design system classes
        if '<button' in line and 'btn' not in line:
            findings['buttons'].append((line_num, line.strip()))

        if '<input type="button"' in line or '<input type="submit"' in line:
            if 'btn' not in line:
                findings['buttons'].append((line_num, line.strip()))

        # Find form inputs without design system classes
        if ('<input' in line or '<select' in line or '<textarea' in line):
            if 'form-control' not in line and 'type="hidden"' not in line and 'type="checkbox"' not in line and 'type="radio"' not in line:
                findings['forms'].append((line_num, line.strip()))

        # Find hardcoded colors
        color_matches = re.findall(r'#[0-9a-fA-F]{3,6}', line)
        for color in color_matches:
            color_lower = color.lower()
            if color_lower in DESIGN_COLORS:
                findings['colors'].append((line_num, color, DESIGN_COLORS[color_lower], line.strip()))
            else:
                findings['colors'].append((line_num, color, 'UNKNOWN', line.strip()))

        # Find typography issues (font-size, font-weight in styles)
        if 'font-size' in line or 'font-weight' in line:
            findings['typography'].append((line_num, line.strip()))

    # Print findings
    total_issues = sum(len(v) for v in findings.values())

    if total_issues == 0:
        print("✅ No issues found! This page follows design system guidelines.\n")
        return

    print(f"⚠️  Found {total_issues} issues\n")

    # Inline styles
    if findings['inline_styles']:
        print(f"📌 Inline Styles ({len(findings['inline_styles'])} found)")
        print("-" * 70)
        for line_num, style, line in findings['inline_styles'][:10]:  # Show first 10
            print(f"Line {line_num}: {style}")
            print(f"  {line[:100]}...")
            print()
        if len(findings['inline_styles']) > 10:
            print(f"  ... and {len(findings['inline_styles']) - 10} more\n")

    # Tables
    if findings['tables']:
        print(f"\n📊 Tables without .admin-table ({len(findings['tables'])} found)")
        print("-" * 70)
        for line_num, line in findings['tables'][:5]:
            print(f"Line {line_num}: {line[:80]}...")
        if len(findings['tables']) > 5:
            print(f"  ... and {len(findings['tables']) - 5} more\n")

    # Buttons
    if findings['buttons']:
        print(f"\n🔘 Buttons without .btn classes ({len(findings['buttons'])} found)")
        print("-" * 70)
        for line_num, line in findings['buttons'][:5]:
            print(f"Line {line_num}: {line[:80]}...")
        if len(findings['buttons']) > 5:
            print(f"  ... and {len(findings['buttons']) - 5} more\n")

    # Forms
    if findings['forms']:
        print(f"\n📝 Form inputs without .form-control ({len(findings['forms'])} found)")
        print("-" * 70)
        for line_num, line in findings['forms'][:5]:
            print(f"Line {line_num}: {line[:80]}...")
        if len(findings['forms']) > 5:
            print(f"  ... and {len(findings['forms']) - 5} more\n")

    # Colors
    if findings['colors']:
        print(f"\n🎨 Hardcoded Colors ({len(findings['colors'])} found)")
        print("-" * 70)

        # Group by color
        color_groups = defaultdict(list)
        for line_num, color, var_name, line in findings['colors']:
            color_groups[color].append((line_num, var_name))

        for color, occurrences in sorted(color_groups.items()):
            var_name = occurrences[0][1]
            if var_name == 'UNKNOWN':
                print(f"  {color}: ❌ Not in design system ({len(occurrences)} times)")
            else:
                print(f"  {color}: Use {var_name} ({len(occurrences)} times)")

    # Typography
    if findings['typography']:
        print(f"\n✍️  Typography Issues ({len(findings['typography'])} found)")
        print("-" * 70)
        for line_num, line in findings['typography'][:5]:
            print(f"Line {line_num}: {line[:80]}...")
        if len(findings['typography']) > 5:
            print(f"  ... and {len(findings['typography']) - 5} more\n")

    # Recommendations
    print(f"\n{'='*70}")
    print("💡 Recommendations")
    print(f"{'='*70}")

    if findings['inline_styles']:
        print("\n1. Remove inline styles and use design system classes:")
        print("   - text-align:center → class='text-center'")
        print("   - margin-top:20px → class='mt-3'")
        print("   - color:#003179 → class='text-primary'")

    if findings['tables']:
        print("\n2. Update tables to use .admin-table:")
        print("   <table class='admin-table'>")
        print("   <th class='center'>...</th>")

    if findings['buttons']:
        print("\n3. Update buttons to use .btn classes:")
        print("   <button class='btn btn-primary'>저장</button>")
        print("   <button class='btn btn-secondary'>취소</button>")
        print("   <button class='btn btn-warning'>삭제</button>")

    if findings['forms']:
        print("\n4. Update form inputs:")
        print("   <div class='form-group'>")
        print("     <label class='form-label'>이름</label>")
        print("     <input type='text' class='form-control'>")
        print("   </div>")

    if findings['colors']:
        print("\n5. Replace hardcoded colors with CSS variables:")
        print("   Use var(--color-primary-1) instead of #003179")

    print("\n" + "="*70)
    print("📚 For detailed migration guide, see:")
    print("   references/migration-checklist.md")
    print("="*70 + "\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python audit_styles.py <path_to_php_file>")
        print("Example: python audit_styles.py adm_cw/member_list_bri.php")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_file(file_path)


if __name__ == '__main__':
    main()
