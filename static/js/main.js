// Enhanced JavaScript with GA4 Analytics Integration
document.addEventListener('DOMContentLoaded', function() {
    // GA4 Helper Functions
    function trackGA4Event(eventName, parameters = {}) {
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, {
                ...parameters,
                page_variant: window.pageVariant || 'unknown'
            });
        }
    }

    // Track page view with additional parameters
    trackGA4Event('page_view', {
        page_title: document.title,
        page_location: window.location.href,
        page_variant: window.pageVariant || 'unknown'
    });

    // Track time on page
    const startTime = Date.now();
    window.addEventListener('beforeunload', function() {
        const timeOnPage = Math.round((Date.now() - startTime) / 1000);
        trackGA4Event('time_on_page', {
            value: timeOnPage,
            event_category: 'engagement'
        });
    });

    // Enhanced button click tracking
    const button = document.querySelector('.button');
    if (button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Track button click
            trackGA4Event('cta_click', {
                event_category: 'engagement',
                event_label: 'get_started_button',
                value: 1
            });
            
            // Add a simple animation effect
            button.style.transform = 'scale(0.95)';
            setTimeout(() => {
                button.style.transform = 'translateY(-2px)';
            }, 150);
            
            // Show an alert (you can replace this with actual functionality)
            alert('Welcome to CalHacks12! This is where your journey begins.');
        });
    }
    
    // Enhanced feature interaction tracking
    const features = document.querySelectorAll('.feature');
    features.forEach((feature, index) => {
        feature.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
            
            // Track feature hover
            trackGA4Event('feature_hover', {
                event_category: 'engagement',
                event_label: `feature_${index + 1}`,
                value: 1
            });
        });
        
        feature.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });

        // Track feature clicks
        feature.addEventListener('click', function() {
            trackGA4Event('feature_click', {
                event_category: 'engagement',
                event_label: `feature_${index + 1}`,
                value: 1
            });
        });
    });

    // Navigation tracking
    const navLinks = document.querySelectorAll('.theme-nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            trackGA4Event('navigation_click', {
                event_category: 'navigation',
                event_label: this.textContent.trim(),
                value: 1
            });
        });
    });

    // Track form interactions (if any forms are added later)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            trackGA4Event('form_submit', {
                event_category: 'conversion',
                event_label: 'contact_form',
                value: 1
            });
        });
    });

    // Track external link clicks
    const externalLinks = document.querySelectorAll('a[href^="http"]');
    externalLinks.forEach(link => {
        link.addEventListener('click', function() {
            trackGA4Event('external_link_click', {
                event_category: 'outbound',
                event_label: this.href,
                value: 1
            });
        });
    });

    // Performance tracking
    if ('performance' in window) {
        // Track page load performance
        window.addEventListener('load', function() {
            setTimeout(() => {
                const perfData = performance.getEntriesByType('navigation')[0];
                if (perfData) {
                    trackGA4Event('page_performance', {
                        event_category: 'performance',
                        load_time: Math.round(perfData.loadEventEnd - perfData.loadEventStart),
                        dom_content_loaded: Math.round(perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart),
                        first_paint: Math.round(perfData.responseEnd - perfData.requestStart)
                    });
                }
            }, 0);
        });
    }

    // Track scroll depth (25%, 50%, 75%, 100%)
    let maxScrollDepth = 0;
    const scrollThresholds = [25, 50, 75, 100];
    
    window.addEventListener('scroll', function() {
        const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
        
        scrollThresholds.forEach(threshold => {
            if (scrollPercent >= threshold && maxScrollDepth < threshold) {
                maxScrollDepth = threshold;
                trackGA4Event('scroll_depth', {
                    event_category: 'engagement',
                    value: threshold
                });
            }
        });
    });

    // Track user engagement time
    let engagementStart = Date.now();
    let isEngaged = true;
    
    // Reset engagement on user activity
    ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'].forEach(event => {
        document.addEventListener(event, function() {
            if (!isEngaged) {
                isEngaged = true;
                engagementStart = Date.now();
            }
        });
    });
    
    // Track engagement time every 30 seconds
    setInterval(function() {
        if (isEngaged) {
            const engagementTime = Math.round((Date.now() - engagementStart) / 1000);
            if (engagementTime >= 30) {
                trackGA4Event('user_engagement', {
                    event_category: 'engagement',
                    value: engagementTime
                });
                engagementStart = Date.now();
            }
        }
    }, 30000);
    
    // Track when user becomes inactive
    let inactivityTimer;
    ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'].forEach(event => {
        document.addEventListener(event, function() {
            clearTimeout(inactivityTimer);
            isEngaged = true;
            inactivityTimer = setTimeout(function() {
                isEngaged = false;
            }, 30000); // 30 seconds of inactivity
        });
    });
});
