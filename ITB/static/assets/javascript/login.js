document.addEventListener('DOMContentLoaded', function() {
  const password = document.getElementById('password');
  const confirmPassword = document.getElementById('confirm-password');
  const matchIndicator = document.createElement('div');
  matchIndicator.className = 'password-match';
  confirmPassword.parentNode.insertBefore(matchIndicator, confirmPassword.nextSibling);

  function checkPasswords() {
    if (confirmPassword.value === '') {
      matchIndicator.classList.remove('visible');
      return;
    }
    
    matchIndicator.classList.add('visible');
    if (password.value === confirmPassword.value) {
      matchIndicator.textContent = '✓ Passwords match';
      matchIndicator.classList.add('valid');
      matchIndicator.classList.remove('invalid');
    } else {
      matchIndicator.textContent = '✗ Passwords do not match';
      matchIndicator.classList.add('invalid');
      matchIndicator.classList.remove('valid');
    }
  }

  password.addEventListener('input', checkPasswords);
  confirmPassword.addEventListener('input', checkPasswords);
});