#!/usr/bin/env python3
"""Add display-name variants (e.g. 'ČT1 HD', 'Prima SK HD') so IPTV players
that match EPG by channel name (Televizo, TiviMate...) find more channels."""
import sys, re, xml.etree.ElementTree as ET
src = sys.argv[1]
tree = ET.parse(src); root = tree.getroot()
for ch in root.findall('channel'):
    names = [d.text for d in ch.findall('display-name') if d.text]
    if not names: continue
    base = names[0].strip()
    stems = {base}
    if base.startswith('TV '): stems.add(base[3:])
    for suf in (' HD', ' SD', ' FHD'):
        if base.endswith(suf): stems.add(base[:-len(suf)])
    variants = []
    for s in sorted(stems):
        for v in (s, s + ' HD', s + ' SK', s + ' SK HD', s + ' CZ', s + ' CZ HD', s + ' FHD'):
            if v not in names and v not in variants: variants.append(v)
    idx = list(ch).index(ch.findall('display-name')[-1]) + 1
    for i, v in enumerate(variants):
        el = ET.Element('display-name'); el.text = v
        ch.insert(idx + i, el)
ET.indent(tree) if hasattr(ET, 'indent') else None
tree.write(src, encoding='UTF-8', xml_declaration=True)
