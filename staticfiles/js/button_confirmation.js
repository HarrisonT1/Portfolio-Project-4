/* global bootstrap */

document.addEventListener("DOMContentLoaded", function() {
    const cancelButtons = document.querySelectorAll(".cancel-btn");
    const modal = new bootstrap.Modal(document.getElementById('cancelConfirmation'));
    const confirmBtn = document.getElementById('cancelConfirm');

    cancelButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            const href = this.getAttribute("href");
            confirmBtn.setAttribute("href", href);
            modal.show();
        });
    });
});