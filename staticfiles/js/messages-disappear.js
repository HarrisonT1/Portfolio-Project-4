window.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show')
            setTimeout(() => {
                alert.remove();
            }, 500);
        }, 3000);
    });
});