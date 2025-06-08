// script.js - Fixed version with proper async handling
document.addEventListener('DOMContentLoaded', function() {
    // 1. Mobile Menu Toggle (synchronous)
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // 2. Navigation with proper async handling
    const handleNavigation = async (e) => {
        const link = e.target.closest('.nav-link');
        if (!link) return;
        
        // Handle anchor links
        if (link.getAttribute('href').startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
            return;
        }
        
        // Handle external links
        if (link.hostname !== window.location.hostname) {
            return; // Let browser handle normally
        }
        
        // Prevent default for same-origin navigation
        e.preventDefault();
        
        try {
            // Show loading indicator
            document.body.classList.add('page-loading');
            
            // Scroll to top immediately
            window.scrollTo(0, 0);
            
            // Close mobile menu if open
            if (navMenu && navMenu.classList.contains('active')) {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            }
            
            // Wait briefly for UI updates
            await new Promise(resolve => setTimeout(resolve, 50));
            
            // Navigate
            window.location.href = link.href;
            
        } catch (error) {
            console.error('Navigation failed:', error);
            document.body.classList.remove('page-loading');
            window.location.href = link.href; // Fallback
        }
    };

    // Attach event listeners
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', handleNavigation);
    });
});

// Reset scroll on page load
window.addEventListener('load', function() {
    window.scrollTo(0, 0);
    document.body.classList.remove('page-loading');
});


// Course Filtering
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const courseCards = document.querySelectorAll('.course-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Update active button
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.dataset.filter;
            
            // Filter courses
            courseCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
 document.addEventListener("DOMContentLoaded", function () {
    const currentPage = window.location.pathname.split("/").pop(); // e.g., 'services.html'
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
      const linkPage = link.getAttribute("href");
      if (linkPage === currentPage) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });
  });