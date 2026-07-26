#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

p = argparse.ArgumentParser()
p.add_argument('--receipt', required=True)
p.add_argument('--artifact', required=True)
p.add_argument('--repository', required=True)
p.add_argument('--head', required=True)
p.add_argument('--capsule', required=True)
a = p.parse_args()
r = json.loads(Path(a.receipt).read_text())
errors = []
for key, expected in [('task_id', 'TASK-CPG-MVS-001'), ('repository', a.repository), ('candidate_sha', a.head)]:
    if r.get(key) != expected: errors.append(key)
if r.get('task_capsule_sha256') != digest(a.capsule): errors.append('task_capsule_sha256')
if r.get('artifact_sha256') != digest(a.artifact): errors.append('artifact_sha256')
if r.get('verifier_exit_status') != 0: errors.append('verifier_exit_status')
if len(str(r.get('verifier_sha256',''))) != 64: errors.append('verifier_sha256')
print(json.dumps({'status': 'PASS' if not errors else 'FAIL', 'errors': errors, 'head': a.head}))
sys.exit(bool(errors))
