// static/js/main.js (VERSÃO FINAL E CORRIGIDA)

document.addEventListener('DOMContentLoaded', function() {
    
    // --- LÓGICA DO HEADER SCROLL (RESTAURADA E GARANTIDA) ---
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

    // --- LÓGICA DO CARROSSEL INFINITO (A PROVA DE FALHAS) ---
    const scroller = document.querySelector('.scroller');
    if (scroller) {
        const scrollerInner = scroller.querySelector('.scroller-inner');
        
        if (scrollerInner && scrollerInner.children.length > 0) {
            const scrollerContent = Array.from(scrollerInner.children);
            
            // INTELIGÊNCIA ESPECIAL: Se o conteúdo for menor que a tela, duplique até preencher
            // Isso garante o efeito de continuidade mesmo com 1 ou 2 logos.
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
            
            // DUPLICAÇÃO FINAL: Agora, duplica todo o conteúdo (já preenchido) mais uma vez para o loop da animação
            const finalContent = Array.from(scrollerInner.children);
            finalContent.forEach(item => {
                const duplicatedItem = item.cloneNode(true);
                duplicatedItem.setAttribute('aria-hidden', true);
                scrollerInner.appendChild(duplicatedItem);
            });

            // Ativa a animação no CSS
            scroller.setAttribute('data-animated', true);
        }
    }
});