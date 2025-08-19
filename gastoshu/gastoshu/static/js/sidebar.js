function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  if (!sidebar) return; // Salir si no existe el sidebar

  const labels = document.querySelectorAll('.sidebar-label');
  const title = document.getElementById('sidebar-title');
  const isExpanded = sidebar.getAttribute('data-expanded') === 'true';

  // Alternar clases y atributos
  if (isExpanded) {
    sidebar.classList.replace('w-64', 'w-16');
    labels.forEach(label => label.classList.add('hidden'));
    if (title) title.classList.add('hidden');
  } else {
    sidebar.classList.replace('w-16', 'w-64');
    labels.forEach(label => label.classList.remove('hidden'));
    if (title) title.classList.remove('hidden');
  }

  // Actualizar estado
  sidebar.setAttribute('data-expanded', String(!isExpanded));
}