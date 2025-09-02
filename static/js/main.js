document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.main-header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    const scroller = document.querySelector('.scroller');
    if (scroller) {
        const scrollerInner = scroller.querySelector('.scroller-inner');
        if (scrollerInner && scrollerInner.children.length > 0) {
            const scrollerContent = Array.from(scrollerInner.children);
            let contentWidth = 0;
            scrollerContent.forEach(item => {
                const style = window.getComputedStyle(item);
                contentWidth += item.offsetWidth + (parseFloat(style.marginLeft) || 0) + (parseFloat(style.marginRight) || 0);
            });

            if (contentWidth < scroller.offsetWidth) {
                const clonesNeeded = Math.ceil(scroller.offsetWidth / contentWidth);
                for (let i = 0; i < clonesNeeded; i++) {
                    scrollerContent.forEach(item => {
                        const duplicatedItem = item.cloneNode(true);
                        duplicatedItem.setAttribute('aria-hidden', true);
                        scrollerInner.appendChild(duplicatedItem);
                    });
                }
            }

            const finalContent = Array.from(scrollerInner.children);
            finalContent.forEach(item => {
                const duplicatedItem = item.cloneNode(true);
                duplicatedItem.setAttribute('aria-hidden', true);
                scrollerInner.appendChild(duplicatedItem);
            });

            scroller.setAttribute('data-animated', true);
        }
    }

    const heroSlides = document.querySelectorAll('.hero-slide');
    if (heroSlides.length > 1) {
        let currentHeroSlide = 0;
        setInterval(function() {
            heroSlides[currentHeroSlide].classList.remove('is-active');
            currentHeroSlide = (currentHeroSlide + 1) % heroSlides.length;
            heroSlides[currentHeroSlide].classList.add('is-active');
        }, 10000);
    }

    const slideshow = document.querySelector('#info-slideshow');
    if (slideshow) {
        const slides = slideshow.querySelectorAll('.slide');
        const navItems = slideshow.querySelectorAll('.nav-item');
        const slideDuration = 15000;
        let currentSlideIndex = 0;
        let intervalId;

        function activateSlide(index) {
            clearInterval(intervalId);

            navItems.forEach((nav, i) => {
                nav.classList.remove('is-active', 'is-complete', 'is-paused');
                if (i < index) {
                    nav.classList.add('is-complete');
                } else if (i === index) {
                    nav.classList.add('is-active');
                }
            });

            slides.forEach(s => s.classList.remove('is-active'));
            slides[index].classList.add('is-active');

            currentSlideIndex = index;
            startSlideshow();
        }

        function startSlideshow() {
            clearInterval(intervalId);
            if (navItems[currentSlideIndex]) {
                navItems[currentSlideIndex].classList.remove('is-paused');
            }

            intervalId = setInterval(() => {
                let nextSlideIndex = (currentSlideIndex + 1) % slides.length;
                activateSlide(nextSlideIndex);
            }, slideDuration);
        }

        function pauseSlideshow() {
            clearInterval(intervalId);
            if (navItems[currentSlideIndex]) {
                navItems[currentSlideIndex].classList.add('is-paused');
            }
        }

        navItems.forEach(item => {
            item.addEventListener('click', () => {
                const index = parseInt(item.dataset.index, 10);
                activateSlide(index);
            });
        });

        const slidesContainer = slideshow.querySelector('.slides-container');
        slidesContainer.addEventListener('mouseenter', pauseSlideshow);
        slidesContainer.addEventListener('mouseleave', startSlideshow);

        activateSlide(0);
    }
});