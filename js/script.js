document.addEventListener('DOMContentLoaded', () => {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mobileOverlay = document.querySelector('.mobile-nav-overlay');
    const hamburgerLines = document.querySelectorAll('.hamburger-line');
    
    let isMenuOpen = false;

    if (hamburgerMenu && mobileOverlay) {
        hamburgerMenu.addEventListener('click', () => {
            isMenuOpen = !isMenuOpen;
            
            if (isMenuOpen) {
                mobileOverlay.classList.add('open');
                // Animate hamburger to X
                hamburgerLines[0].style.transform = 'translateY(9px) rotate(45deg)';
                hamburgerLines[1].style.opacity = '0';
                hamburgerLines[2].style.transform = 'translateY(-9px) rotate(-45deg)';
            } else {
                mobileOverlay.classList.remove('open');
                // Revert hamburger
                hamburgerLines[0].style.transform = 'translateY(0) rotate(0)';
                hamburgerLines[1].style.opacity = '1';
                hamburgerLines[2].style.transform = 'translateY(0) rotate(0)';
            }
        });
    }
});
