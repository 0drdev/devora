const form = document.getElementById('form');
const estado = document.getElementById('estado');
const resultado = document.getElementById('resultado');
const md = document.getElementById('md');
const avisos = document.getElementById('avisos');
const confirm = document.getElementById('confirm');
let downloadName = 'documento.md';

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  estado.textContent = 'Convirtiendo…';
  confirm.textContent = '';
  const data = new FormData(form);
  const r = await fetch('/api/convert', { method: 'POST', body: data });
  const j = await r.json();
  if (!r.ok) { estado.textContent = j.error || 'No se pudo convertir.'; return; }
  md.value = j.markdown;
  downloadName = j.download_name || downloadName;
  avisos.innerHTML = '';
  (j.warnings || []).forEach((w) => {
    const li = document.createElement('li');
    li.textContent = w;
    avisos.appendChild(li);
  });
  if (!(j.warnings || []).length) {
    const li = document.createElement('li');
    li.textContent = 'Conversión completa sin advertencias.';
    avisos.appendChild(li);
  }
  resultado.hidden = false;
  estado.textContent = 'Conversión lista.';
});

document.getElementById('copiar').addEventListener('click', async () => {
  await navigator.clipboard.writeText(md.value);
  confirm.textContent = 'Markdown copiado al portapapeles.';
});

document.getElementById('descargar').addEventListener('click', () => {
  const blob = new Blob([md.value], { type: 'text/markdown' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = downloadName;
  a.click();
  URL.revokeObjectURL(a.href);
  confirm.textContent = 'Archivo ' + downloadName + ' descargado.';
});

document.getElementById('descartar').addEventListener('click', () => {
  md.value = '';
  resultado.hidden = true;
  form.reset();
  confirm.textContent = '';
  estado.textContent = 'Contenido descartado y purgado.';
});
