// --- Theme Toggle (Dark/Light) ---
const themeToggle = document.getElementById('theme-toggle');
const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark');
} else {
    document.documentElement.classList.remove('dark');
}
updateThemeIcon(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        let isDark = document.documentElement.classList.contains('dark');
        let newTheme = isDark ? 'light' : 'dark';
        
        if (newTheme === 'dark') {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });
}

function updateThemeIcon(theme) {
    if (!themeToggle) return;
    if (theme === 'dark') {
        themeToggle.innerHTML = '<svg class="w-6 h-6 inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>';
    } else {
        themeToggle.innerHTML = '<svg class="w-6 h-6 inline-block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>';
    }
}

// --- Direction Toggle (LTR/RTL) ---
const dirToggle = document.getElementById('dir-toggle');
const savedDir = localStorage.getItem('dir') || 'ltr';
document.documentElement.setAttribute('dir', savedDir);
updateDirText(savedDir);

if (dirToggle) {
    dirToggle.addEventListener('click', () => {
        let currentDir = document.documentElement.getAttribute('dir');
        let newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
        document.documentElement.setAttribute('dir', newDir);
        localStorage.setItem('dir', newDir);
        updateDirText(newDir);
    });
}

function updateDirText(dir) {
    if (!dirToggle) return;
    dirToggle.textContent = dir === 'ltr' ? 'LTR' : 'RTL';
}

// --- Mobile Menu Toggle ---
const menuBtn = document.getElementById('menu-toggle');
const mobileOverlay = document.getElementById('mobile-nav-overlay');
const closeBtn = document.getElementById('mobile-nav-close');

if (menuBtn && mobileOverlay) {
    menuBtn.addEventListener('click', () => {
        mobileOverlay.classList.remove('translate-x-full');
        mobileOverlay.classList.add('translate-x-0');
    });
}
if (closeBtn && mobileOverlay) {
    closeBtn.addEventListener('click', () => {
        mobileOverlay.classList.add('translate-x-full');
        mobileOverlay.classList.remove('translate-x-0');
    });
}
// --- Active Nav Link Highlighting ---
const currentPath = window.location.pathname.split('/').pop() || 'index.html';

// Desktop Nav
document.querySelectorAll('header nav a').forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentPath) {
        link.classList.add('text-blue-600', 'dark:text-blue-400', 'font-bold');
        
        // Highlight parent button if in a dropdown
        const group = link.closest('.group');
        if (group) {
            const btn = group.querySelector('button');
            if (btn) btn.classList.add('text-blue-600', 'dark:text-blue-400', 'font-bold');
        }
    }
});

// Mobile Nav
document.querySelectorAll('#mobile-nav a, #mobile-nav-overlay a').forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentPath) {
        link.classList.add('text-blue-600', 'dark:text-blue-400');
    }
});

// --- Sidebar Toggle ---
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.getElementById('sidebar');

if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        sidebar.classList.toggle('-translate-x-full');
    });

    document.addEventListener('click', (e) => {
        if (window.innerWidth < 1024) { // lg breakpoint
            if (!sidebar.contains(e.target) && !sidebar.classList.contains('-translate-x-full')) {
                sidebar.classList.add('-translate-x-full');
            }
        }
    });
}
