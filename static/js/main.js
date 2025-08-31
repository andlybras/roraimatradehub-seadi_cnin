// static/js/main.js

// Espera o documento HTML ser completamente carregado
document.addEventListener('DOMContentLoaded', function() {

    // Seleciona o nosso header
    const header = document.querySelector('.main-header');

    // Se o header não existir, não faz nada
    if (!header) return;

    // Escuta o evento de rolagem da página
    window.addEventListener('scroll', function() {
        // Se a página for rolada mais de 50 pixels para baixo
        if (window.scrollY > 50) {
            // Adiciona a classe 'scrolled' ao header
            header.classList.add('scrolled');
        } else {
            // Remove a classe 'scrolled' se estiver perto do topo
            header.classList.remove('scrolled');
        }
    });
});