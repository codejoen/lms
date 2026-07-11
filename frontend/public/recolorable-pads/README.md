# Recolorable Pads

Dieses Paket enthält die neun vollständig sichtbaren Pixel-Art-Figuren aus dem gelieferten Screenshot. Alle Figuren wurden pixelgenau freigestellt und auf eine einheitliche transparente Fläche von **96 × 96 px** gesetzt.

## Inhalt

- `originals/` — neun freigestellte Originale als transparente PNGs
- `steps/` — pro Figur elf Farbstufen von Rot (`00`) bis Grün (`10`)
- `animations/` — pro Figur animiertes GIF, lossless WebP und APNG
- `preview-all-steps.png` — statische Gesamtübersicht
- `preview-animated.webp` — animierte Gesamtübersicht
- `index.html` — interaktive Vorschau mit Regler, Play/Pause und Tempo
- `manifest.json` — maschinenlesbare Pfade, Farben und Metadaten
- `recolor.py` — erzeugt aus jedem Original weitere frei wählbare Farbtöne

## Palette

Die elf Zustände verwenden HSL-Hues von 0° bis 120° in 12°-Schritten. Dadurch sind beide Endpunkte und neun Zwischenstufen vorhanden.

## Eigene Farbe erzeugen

Voraussetzungen: Python 3, Pillow und NumPy.

```bash
python3 recolor.py \
  originals/pad-01-cloud-terminal.png \
  custom-purple.png \
  --hue 285
```

Hue-Beispiele: `0` Rot, `30` Orange, `60` Gelb, `120` Grün, `210` Blau, `285` Violett.

## Web-Vorschau öffnen

Da der Browser lokale JSON-Dateien teilweise blockiert, am besten in diesem Ordner einen kleinen Server starten:

```bash
python3 -m http.server 8080
```

Danach `http://localhost:8080` öffnen.

## Animationen

- **WebP**: empfohlen für Webseiten; lossless, volle Transparenz
- **APNG**: gute Alternative mit voller Farbtiefe
- **GIF**: maximale Kompatibilität, aber reduzierte Farbtiefe

Alle Animationen laufen als weicher Ping-Pong-Loop Rot → Grün → Rot mit 140 ms pro Frame.
