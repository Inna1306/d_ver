document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', event => {
      const target = document.querySelector(link.getAttribute('href'));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      history.replaceState(null, '', link.getAttribute('href'));
    });
  });

  document.querySelectorAll('.btn--danger').forEach(button => {
    button.addEventListener('click', event => {
      if (!confirm('Подтвердить удаление?')) event.preventDefault();
    });
  });
});