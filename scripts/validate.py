import sys

config_file = "configs/router_valid.cfg"
errors = []

with open(config_file) as f:
    lines = f.readlines()
    full_text = ''.join(lines)
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if "permit ip any any" in stripped:
            errors.append("Line " + str(i) + ": ACL FAIL - Overly permissive rule found")
        if stripped == "service telnet":
            errors.append("Line " + str(i) + ": SECURITY FAIL - Telnet detected, use SSH")
    if "ip route 0.0.0.0" not in full_text:
        errors.append("ROUTING FAIL - Default route is missing")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print(" - " + e)
    sys.exit(1)
else:
    print("VALIDATION PASSED: All checks OK")
