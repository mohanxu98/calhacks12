// Simple JavaScript for interactive features
document.addEventListener('DOMContentLoaded', function() {
    // Add click event to the button
    const button = document.querySelector('.button');
    
    button.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Add a simple animation effect
        button.style.transform = 'scale(0.95)';
        setTimeout(() => {
            button.style.transform = 'translateY(-2px)';
        }, 150);
        
        // Show an alert (you can replace this with actual functionality)
        alert('Welcome to CalHacks12! This is where your journey begins.');
    });
    
    // Add hover effects to features
    const features = document.querySelectorAll('.feature');
    features.forEach(feature => {
        feature.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        feature.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
