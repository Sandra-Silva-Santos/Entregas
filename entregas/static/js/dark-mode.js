function toggleDarkMode() {
  let body = document.getElementsByTagName('body')[0];
  if (body.classList.contains('dark-mode')) {
    body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', 'false');
  } else {
    body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'true');
  }
}

// Verifica se o usuário já optou pelo modo escuro
if (localStorage.getItem('darkMode') === null) {
  localStorage.setItem('darkMode', 'false');
} else if (localStorage.getItem('darkMode') === 'true') {
  toggleDarkMode();
}

// Adiciona um ouvinte de eventos para o botão de alternância de modo claro/escuro
document.getElementById('dark-mode-toggle').addEventListener('click', toggleDarkMode);

const darkModeToggle = document.getElementById('dark-mode-toggle');

function updateToggleButtonText() {
  if (localStorage.getItem('darkMode') === 'true') {
    darkModeToggle.innerHTML = '<i class="bi bi-brightness-high">';
  } else {
    darkModeToggle.innerHTML = '<i class="bi-moon"></i>';
  }
}

updateToggleButtonText();

darkModeToggle.addEventListener('click', updateToggleButtonText);
