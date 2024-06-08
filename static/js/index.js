document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.slide .img');

    const pauseAnimations = () => {
        images.forEach(image => {
            image.style.animationPlayState = 'paused';
        });
    };

    const resumeAnimations = () => {
        images.forEach(image => {
            image.style.animationPlayState = 'running';
        });
    };

    images.forEach(img => {
        img.addEventListener('mouseover', pauseAnimations);
        img.addEventListener('mouseout', resumeAnimations);
    });
});
