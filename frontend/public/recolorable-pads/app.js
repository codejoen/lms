const grid = document.querySelector('#grid');
const slider = document.querySelector('#step');
const output = document.querySelector('#step-value');
const playButton = document.querySelector('#play');
const speed = document.querySelector('#speed');

let manifest;
let timer = null;
let direction = 1;

function renderStep(step) {
  const palette = manifest.palette[step];
  output.value = `${palette.label} · ${palette.hex}`;
  document.documentElement.style.setProperty('--active', palette.hex);
  document.querySelectorAll('.card img').forEach((img, index) => {
    img.src = manifest.pads[index].steps[step];
  });
}

function tick() {
  let next = Number(slider.value) + direction;
  if (next >= 10 || next <= 0) direction *= -1;
  slider.value = next;
  renderStep(next);
}

function stop() {
  clearInterval(timer);
  timer = null;
  playButton.textContent = '▶ Animation starten';
  playButton.setAttribute('aria-pressed', 'false');
}

function start() {
  stop();
  playButton.textContent = '■ Animation stoppen';
  playButton.setAttribute('aria-pressed', 'true');
  timer = setInterval(tick, Number(speed.value));
}

fetch('manifest.json')
  .then(response => response.json())
  .then(data => {
    manifest = data;
    grid.innerHTML = manifest.pads.map((pad, index) => `
      <article class="card">
        <img src="${pad.steps[0]}" alt="${pad.name}, Farbzustand 00" width="96" height="96">
        <h2>${String(index + 1).padStart(2, '0')} · ${pad.name}</h2>
        <code>96×96 PNG</code>
      </article>`).join('');
    renderStep(0);
  });

slider.addEventListener('input', () => renderStep(Number(slider.value)));
playButton.addEventListener('click', () => timer ? stop() : start());
speed.addEventListener('change', () => { if (timer) start(); });
