# PHASE_4_FILE: Renders 2D layout from spatial map and zone tags
# Origin: Blueprint Phase 4 — STATIC 2D BLUEPRINT GENERATION
# Role: Uses spatial inference data to draw SVG layout of rooms + connections

import os
import json
import svgwrite

def render_blueprint(spatial_map_path, output_svg_path):
    with open(spatial_map_path, "r", encoding="utf-8") as f:
        spatial_data = json.load(f)

    zones = spatial_data.get("sequence", [])
    adjacency = spatial_data.get("adjacency_matrix", {})
    dwg = svgwrite.Drawing(output_svg_path, size=("1200px", "800px"))

    zone_positions = {}
    x, y = 100, 100
    spacing = 200

    for zone in zones:
        zone_positions[zone] = (x, y)
        dwg.add(dwg.rect(insert=(x, y), size=("150px", "100px"), fill="lightblue", stroke="black"))
        dwg.add(dwg.text(zone, insert=(x + 10, y + 20), font_size="15px", fill="black"))
        y += spacing

    for z1 in adjacency:
        for z2 in adjacency[z1]:
            x1, y1 = zone_positions.get(z1, (0, 0))
            x2, y2 = zone_positions.get(z2, (0, 0))
            dwg.add(dwg.line(start=(x1+75, y1+50), end=(x2+75, y2+50), stroke="gray"))

    dwg.save()
    return output_svg_path
