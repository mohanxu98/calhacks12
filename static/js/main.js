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

    // Enhanced button click tracking with detailed engagement metrics
    const button = document.querySelector('.button');
    if (button) {
        let buttonHoverStart = null;
        let buttonHoverDuration = 0;
        
        // Track button hover start
        button.addEventListener('mouseenter', function() {
            buttonHoverStart = Date.now();
            trackGA4Event('button_hover_start', {
                event_category: 'engagement',
                event_label: 'get_started_button',
                button_type: 'cta',
                page_variant: window.pageVariant || 'unknown'
            });
        });
        
        // Track button hover end and duration
        button.addEventListener('mouseleave', function() {
            if (buttonHoverStart) {
                buttonHoverDuration = Date.now() - buttonHoverStart;
                trackGA4Event('button_hover_end', {
                    event_category: 'engagement',
                    event_label: 'get_started_button',
                    button_type: 'cta',
                    hover_duration: Math.round(buttonHoverDuration),
                    page_variant: window.pageVariant || 'unknown'
                });
            }
        });
        
        // Track button click with detailed metrics
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Calculate total engagement time (hover + click)
            const totalEngagement = buttonHoverDuration + (Date.now() - (buttonHoverStart || Date.now()));
            
            // Track comprehensive button click
            trackGA4Event('cta_click', {
                event_category: 'engagement',
                event_label: 'get_started_button',
                button_type: 'cta',
                hover_duration: Math.round(buttonHoverDuration),
                total_engagement: Math.round(totalEngagement),
                page_variant: window.pageVariant || 'unknown',
                value: 1
            });
            
            // Track button interaction success
            trackGA4Event('button_interaction_success', {
                event_category: 'conversion',
                event_label: 'get_started_button',
                button_type: 'cta',
                page_variant: window.pageVariant || 'unknown'
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
    
    // Enhanced feature button tracking with detailed engagement metrics
    const features = document.querySelectorAll('.feature');
    features.forEach((feature, index) => {
        let featureHoverStart = null;
        let featureHoverDuration = 0;
        const featureTitle = feature.querySelector('h3')?.textContent || `Feature ${index + 1}`;
        
        feature.addEventListener('mouseenter', function() {
            featureHoverStart = Date.now();
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
            
            // Track feature hover start
            trackGA4Event('feature_hover_start', {
                event_category: 'engagement',
                event_label: `feature_${index + 1}`,
                feature_title: featureTitle,
                feature_type: 'card',
                page_variant: window.pageVariant || 'unknown'
            });
        });
        
        feature.addEventListener('mouseleave', function() {
            if (featureHoverStart) {
                featureHoverDuration = Date.now() - featureHoverStart;
                this.style.transform = 'translateY(0)';
                
                // Track feature hover end with duration
                trackGA4Event('feature_hover_end', {
                    event_category: 'engagement',
                    event_label: `feature_${index + 1}`,
                    feature_title: featureTitle,
                    feature_type: 'card',
                    hover_duration: Math.round(featureHoverDuration),
                    page_variant: window.pageVariant || 'unknown'
                });
            }
        });

        // Track feature clicks with comprehensive metrics
        feature.addEventListener('click', function() {
            const totalEngagement = featureHoverDuration + (Date.now() - (featureHoverStart || Date.now()));
            
            trackGA4Event('feature_click', {
                event_category: 'engagement',
                event_label: `feature_${index + 1}`,
                feature_title: featureTitle,
                feature_type: 'card',
                hover_duration: Math.round(featureHoverDuration),
                total_engagement: Math.round(totalEngagement),
                page_variant: window.pageVariant || 'unknown',
                value: 1
            });
            
            // Track feature interaction success
            trackGA4Event('feature_interaction_success', {
                event_category: 'engagement',
                event_label: `feature_${index + 1}`,
                feature_title: featureTitle,
                feature_type: 'card',
                page_variant: window.pageVariant || 'unknown'
            });
        });
    });

    // Enhanced navigation button tracking with engagement metrics
    const navLinks = document.querySelectorAll('.theme-nav a');
    navLinks.forEach((link, index) => {
        let navHoverStart = null;
        let navHoverDuration = 0;
        
        // Track navigation hover start
        link.addEventListener('mouseenter', function() {
            navHoverStart = Date.now();
            trackGA4Event('nav_hover_start', {
                event_category: 'navigation',
                event_label: this.textContent.trim(),
                nav_item: `nav_${index + 1}`,
                nav_text: this.textContent.trim(),
                page_variant: window.pageVariant || 'unknown'
            });
        });
        
        // Track navigation hover end and duration
        link.addEventListener('mouseleave', function() {
            if (navHoverStart) {
                navHoverDuration = Date.now() - navHoverStart;
                trackGA4Event('nav_hover_end', {
                    event_category: 'navigation',
                    event_label: this.textContent.trim(),
                    nav_item: `nav_${index + 1}`,
                    nav_text: this.textContent.trim(),
                    hover_duration: Math.round(navHoverDuration),
                    page_variant: window.pageVariant || 'unknown'
                });
            }
        });
        
        // Track navigation click with detailed metrics
        link.addEventListener('click', function() {
            const totalEngagement = navHoverDuration + (Date.now() - (navHoverStart || Date.now()));
            
            trackGA4Event('navigation_click', {
                event_category: 'navigation',
                event_label: this.textContent.trim(),
                nav_item: `nav_${index + 1}`,
                nav_text: this.textContent.trim(),
                hover_duration: Math.round(navHoverDuration),
                total_engagement: Math.round(totalEngagement),
                page_variant: window.pageVariant || 'unknown',
                value: 1
            });
            
            // Track navigation success
            trackGA4Event('navigation_success', {
                event_category: 'navigation',
                event_label: this.textContent.trim(),
                nav_item: `nav_${index + 1}`,
                nav_text: this.textContent.trim(),
                page_variant: window.pageVariant || 'unknown'
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
