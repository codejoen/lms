#!/usr/bin/env python3
"""Recolor one transparent pad PNG to any hue while preserving neutral details."""

from __future__ import annotations

import argparse
import colorsys
from pathlib import Path

import numpy as np
from PIL import Image


def recolor(image: Image.Image, hue: float) -> Image.Image:
    rgba = np.array(image.convert("RGBA"), dtype=np.uint8)
    rgb = rgba[..., :3].astype(np.float32) / 255.0
    flat = rgb.reshape(-1, 3)
    alpha = rgba[..., 3].reshape(-1)
    for index, (red, green, blue) in enumerate(flat.copy()):
        if alpha[index] == 0:
            continue
        _, lightness, saturation = colorsys.rgb_to_hls(float(red), float(green), float(blue))
        if saturation < 0.16 or lightness < 0.075 or lightness > 0.965:
            continue
        strength = min(1.0, max(0.0, (saturation - 0.12) / 0.28))
        target = np.array(colorsys.hls_to_rgb((hue % 360) / 360, lightness, max(saturation, 0.42)))
        flat[index] = flat[index] * (1 - strength) + target * strength
    result = np.dstack([(rgb * 255 + 0.5).astype(np.uint8), rgba[..., 3]])
    return Image.fromarray(result, "RGBA")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--hue", type=float, required=True, help="Hue angle, e.g. 0=red, 60=yellow, 120=green")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    recolor(Image.open(args.input), args.hue).save(args.output, optimize=True)


if __name__ == "__main__":
    main()
