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
});