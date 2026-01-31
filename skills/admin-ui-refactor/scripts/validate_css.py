#!/usr/bin/env python3
"""
Design System CSS Validator

Validates that design-system.css contains all required:
- CSS variables
- Component classes
- Typography classes
- Utility classes

Usage:
    python validate_css.py <path_to_design-system.css>
    python validate_css.py adm_cw/css/design-system.css
"""

import sys
from pathlib import Path


# Required CSS variables
REQUIRED_VARIABLES = [
    '--color-primary-1',
    '--color-primary-2',
    '--color-primary-bg',
    '--color-gray-100',
    '--color-gray-200',
    '--color-gray-400',
    '--color-black',
    '--color-white',
    '--color-warning',
    '--color-success',
    '--color-info',
    '--spacing-xs',
    '--spacing-sm',
    '--spacing-md',
    '--spacing-lg',
    '--spacing-xl',
    '--spacing-xxl',
    '--radius-sm',
    '--radius-md',
    '--radius-lg',
    '--shadow-sm',
    '--shadow-md',
    '--shadow-lg',
    '--transition-fast',
    '--transition-base',
    '--transition-slow',
]

# Required component classes
REQUIRED_COMPONENTS = [
    '.btn',
    '.btn-primary',
    '.btn-secondary',
    '.btn-warning',
    '.btn-success',
    '.btn-sm',
    '.btn-lg',
    '.admin-table',
    '.form-group',
    '.form-label',
    '.form-control',
    '.form-error-message',
    '.form-help-text',
    '.admin-card',
    '.admin-card-header',
    '.admin-card-body',
    '.badge',
    '.badge-primary',
    '.badge-secondary',
    '.badge-success',
    '.badge-warning',
    '.alert',
    '.alert-success',
    '.alert-warning',
    '.alert-error',
    '.alert-info',
    '.pagination',
]

# Required typography classes
REQUIRED_TYPOGRAPHY = [
    '.heading-h1-bold',
    '.heading-h2-bold',
    '.heading-h3-bold',
    '.heading-h4-bold',
    '.heading-h5-bold',
    '.body-xl-bold',
    '.body-large-bold',
    '.body-medium-bold',
    '.body-small-bold',
    '.body-medium-regular',
]

# Required utility classes
REQUIRED_UTILITIES = [
    '.text-center',
    '.text-left',
    '.text-right',
    '.text-primary',
    '.text-warning',
    '.d-flex',
    '.justify-between',
    '.align-center',
    '.mt-1',
    '.mb-1',
    '.p-1',
]


def validate_css(file_path):
    """Validate design-system.css file."""

    if not Path(file_path).exists():
        print(f"❌ Error: File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n{'='*70}")
    print(f"🔍 Validating Design System CSS")
    print(f"{'='*70}\n")

    all_valid = True
    missing_items = []

    # Check CSS variables
    print("📋 Checking CSS Variables...")
    missing_vars = []
    for var in REQUIRED_VARIABLES:
        if var not in content:
            missing_vars.append(var)
            all_valid = False

    if missing_vars:
        print(f"  ❌ Missing {len(missing_vars)} variables:")
        for var in missing_vars:
            print(f"     - {var}")
    else:
        print(f"  ✅ All {len(REQUIRED_VARIABLES)} variables present")

    # Check component classes
    print("\n🎨 Checking Component Classes...")
    missing_components = []
    for component in REQUIRED_COMPONENTS:
        # Check if class is defined (either as selector or in comment)
        if f"{component} {{" not in content and f"{component}," not in content:
            missing_components.append(component)
            all_valid = False

    if missing_components:
        print(f"  ❌ Missing {len(missing_components)} components:")
        for comp in missing_components:
            print(f"     - {comp}")
    else:
        print(f"  ✅ All {len(REQUIRED_COMPONENTS)} components present")

    # Check typography classes
    print("\n✍️  Checking Typography Classes...")
    missing_typography = []
    for typo in REQUIRED_TYPOGRAPHY:
        if f"{typo} {{" not in content and f"{typo}," not in content:
            missing_typography.append(typo)
            all_valid = False

    if missing_typography:
        print(f"  ❌ Missing {len(missing_typography)} typography classes:")
        for typo in missing_typography:
            print(f"     - {typo}")
    else:
        print(f"  ✅ All {len(REQUIRED_TYPOGRAPHY)} typography classes present")

    # Check utility classes
    print("\n🔧 Checking Utility Classes...")
    missing_utilities = []
    for util in REQUIRED_UTILITIES:
        if f"{util} {{" not in content and f"{util}," not in content:
            missing_utilities.append(util)
            all_valid = False

    if missing_utilities:
        print(f"  ❌ Missing {len(missing_utilities)} utility classes:")
        for util in missing_utilities:
            print(f"     - {util}")
    else:
        print(f"  ✅ All {len(REQUIRED_UTILITIES)} utility classes present")

    # Check web fonts
    print("\n🔤 Checking Web Fonts...")
    has_paperlogy = 'Paperlogy' in content
    has_pretendard = 'Pretendard' in content

    if has_paperlogy and has_pretendard:
        print("  ✅ Both Paperlogy and Pretendard fonts referenced")
    else:
        if not has_paperlogy:
            print("  ❌ Paperlogy font not found")
            all_valid = False
        if not has_pretendard:
            print("  ❌ Pretendard font not found")
            all_valid = False

    # Check file size
    print("\n📊 File Statistics...")
    file_size = len(content)
    file_size_kb = file_size / 1024
    print(f"  File size: {file_size_kb:.2f} KB")

    if file_size_kb > 100:
        print(f"  ⚠️  Warning: File is larger than 100KB (performance concern)")
    else:
        print(f"  ✅ File size is acceptable")

    # Summary
    print(f"\n{'='*70}")
    if all_valid:
        print("✅ Validation Passed!")
        print("The design system CSS is complete and ready to use.")
    else:
        print("❌ Validation Failed!")
        print("Please add the missing items listed above.")
    print(f"{'='*70}\n")

    return all_valid


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate_css.py <path_to_design-system.css>")
        print("Example: python validate_css.py adm_cw/css/design-system.css")
        sys.exit(1)

    file_path = sys.argv[1]
    is_valid = validate_css(file_path)

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
