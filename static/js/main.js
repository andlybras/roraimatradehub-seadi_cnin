// Em: static/js/main.js (VERSÃO FINAL COM SLIDESHOW)

document.addEventListener('DOMContentLoaded', function() {

    // --- LÓGICA 1: EFEITO DE SCROLL DO HEADER (PRESERVADA) ---
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

    // --- LÓGICA 2: CARROSSEL DE PARCEIROS (PRESERVADA) ---
    const scroller = document.querySelector('.scroller');
    if (scroller) {
        const scrollerInner = scroller.querySelector('.scroller-inner');
        if (scrollerInner && scrollerInner.children.length > 0) {
            const scrollerContent = Array.from(scrollerInner.children);
            let contentWidth = scrollerInner.offsetWidth;
            let scrollerWidth = scroller.offsetWidth;
            if (contentWidth < scrollerWidth) {
                const clonesNeeded = Math.ceil(scrollerWidth / contentWidth);
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

    // --- LÓGICA 3: SLIDESHOW DO HERO (ADICIONADA) ---
    const slides = document.querySelectorAll('.hero-slide');

    // Só inicia o slideshow se houver MAIS DE UMA imagem
    if (slides.length > 1) {
        let currentSlide = 0;

        setInterval(function() {
            // Torna o slide atual invisível
            slides[currentSlide].classList.remove('is-active');
            // Calcula qual é o próximo slide
            currentSlide = (currentSlide + 1) % slides.length;
            // Torna o novo slide visível
            slides[currentSlide].classList.add('is-active');
        }, 10000); // 10 segundos
    }
    const slideshow = document.querySelector('#info-slideshow');

    // Só executa se o slideshow existir na página
    if (slideshow) {
        const slides = slideshow.querySelectorAll('.slide');
        const navItems = slideshow.querySelectorAll('.nav-item');
        const slideDuration = 15000; // 15 segundos por slide
        let currentSlideIndex = 0;
        let intervalId;

        function activateSlide(index) {
            // Para o timer atual
            clearInterval(intervalId);

            // Remove a classe 'is-active' de todos
            slides.forEach(s => s.classList.remove('is-active'));
            navItems.forEach(n => n.classList.remove('is-active'));

            // Adiciona a classe 'is-active' ao slide e navegação corretos
            slides[index].classList.add('is-active');
            navItems[index].classList.add('is-active');

            currentSlideIndex = index;

            // Reinicia o timer
            startSlideshow();
        }

        function startSlideshow() {
            // Garante que qualquer timer antigo seja limpo
            clearInterval(intervalId);
            // Remove a classe de pausa
            navItems[currentSlideIndex].classList.remove('is-paused');

            // Cria um novo timer
            intervalId = setInterval(() => {
                let nextSlideIndex = (currentSlideIndex + 1) % slides.length;
                activateSlide(nextSlideIndex);
            }, slideDuration);
        }

        function pauseSlideshow() {
            clearInterval(intervalId);
            // Adiciona a classe que pausa a animação CSS
            navItems[currentSlideIndex].classList.add('is-paused');
        }

        // Adiciona os event listeners
        navItems.forEach((item, index) => {
            item.addEventListener('click', () => {
                activateSlide(index);
            });
        });

        const slidesContainer = slideshow.querySelector('.slides-container');
        slidesContainer.addEventListener('mouseenter', pauseSlideshow);
        slidesContainer.addEventListener('mouseleave', startSlideshow);

        // Inicia o slideshow
        startSlideshow();
    }
});