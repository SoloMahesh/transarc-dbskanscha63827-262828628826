/*
========================================================================
© 2026 Mahesh Palalarthi. All Rights Reserved.
PROPRIETARY & CONFIDENTIAL: This logic and codebase is the exclusive 
property of Mahesh Palalarthi. Unauthorized copying is strictly prohibited.
========================================================================
*/
// js/main.js

document.addEventListener('DOMContentLoaded', () => {
    // 1. Security & Protection (Prevent Copy/Paste/Inspect)
    const disableEvent = (e) => {
        e.preventDefault();
        return false;
    };

    // Disable Right-Click
    document.addEventListener('contextmenu', disableEvent);

    // Disable copy, cut, paste
    document.addEventListener('copy', disableEvent);
    document.addEventListener('cut', disableEvent);
    document.addEventListener('paste', disableEvent);

    // Disable drag
    document.addEventListener('dragstart', disableEvent);
    document.addEventListener('drop', disableEvent);

    // Prevent specific keyboard shortcuts (F12, Ctrl+Shift+I, Ctrl+U, Ctrl+C)
    document.addEventListener('keydown', (e) => {
        if (
            e.keyCode === 123 || // F12
            (e.ctrlKey && e.shiftKey && e.keyCode === 73) || // Ctrl+Shift+I
            (e.ctrlKey && e.shiftKey && e.keyCode === 74) || // Ctrl+Shift+J
            (e.ctrlKey && e.keyCode === 85) || // Ctrl+U
            (e.ctrlKey && e.keyCode === 67) || // Ctrl+C
            (e.metaKey && e.keyCode === 67)    // Cmd+C (Mac)
        ) {
            e.preventDefault();
            return false;
        }
    });

    // 2. Scroll Reveal Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible if you only want it to animate once
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up').forEach((el) => {
        observer.observe(el);
    });

    // 3. Navbar scroll effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-md');
            navbar.classList.replace('bg-surface/80', 'bg-surface/95');
        } else {
            navbar.classList.remove('shadow-md');
            navbar.classList.replace('bg-surface/95', 'bg-surface/80');
        }
    });

    // 4. Mobile Menu functionality
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuCloseBtn = document.getElementById('mobile-menu-close');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = mobileMenu.querySelectorAll('a');

    const openMenu = () => {
        mobileMenu.classList.add('open');
        document.body.style.overflow = 'hidden'; // Prevent scrolling
    };

    const closeMenu = () => {
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
    };

    mobileMenuBtn?.addEventListener('click', openMenu);
    mobileMenuCloseBtn?.addEventListener('click', closeMenu);

    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMenu);
    });
});
