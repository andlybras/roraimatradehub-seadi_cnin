// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    
    // --- LÓGICA GERAL DO SITE ---

    // Scroll do Header
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

    // Animação do carrossel de parceiros
    const scrollers = document.querySelectorAll(".scroller");
    if (scrollers.length > 0) {
        scrollers.forEach((scroller) => {
            scroller.setAttribute("data-animated", true);
            const scrollerInner = scroller.querySelector(".scroller-inner");
            const scrollerContent = Array.from(scrollerInner.children);
            scrollerContent.forEach((item) => {
                const duplicatedItem = item.cloneNode(true);
                duplicatedItem.setAttribute("aria-hidden", true);
                scrollerInner.appendChild(duplicatedItem);
            });
        });
    }
    
    // Slideshow da seção Hero
    const heroSlides = document.querySelectorAll('.hero-slide');
    if (heroSlides.length > 1) {
        let currentHeroSlide = 0;
        setInterval(function() {
            heroSlides[currentHeroSlide].classList.remove('is-active');
            currentHeroSlide = (currentHeroSlide + 1) % heroSlides.length;
            heroSlides[currentHeroSlide].classList.add('is-active');
        }, 10000);
    }

    // --- LÓGICA DO FORMULÁRIO DE REGISTRO ---
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        // (Aqui dentro fica toda a lógica de validação do registro que já fizemos)
        const email = document.getElementById('id_email');
        const email2 = document.getElementById('id_email2');
        const password = document.getElementById('id_password1');
        const password2 = document.getElementById('id_password2');
        const submitButton = document.getElementById('submitButton');
        const emailError = document.getElementById('email-error');
        const email2Error = document.getElementById('email2-error');
        const password2Error = document.getElementById('password2-error');
        const passwordFeedback = document.getElementById('password-feedback');
        const iconError = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/></svg>';
        const iconSuccess = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/></svg>';
        const passwordRules = [
            { regex: /.{8,}/, text: "Pelo menos 8 caracteres" },
            { regex: /[A-Z]/, text: "Pelo menos uma letra maiúscula" },
            { regex: /[a-z]/, text: "Pelo menos uma letra minúscula" },
            { regex: /[0-9]/, text: "Pelo menos um número" },
        ];
        const rulesContainer = passwordFeedback.querySelector('.validation-rules');
        if (rulesContainer) { /* ... código para popular as regras de senha ... */ }
        const validateEmailFormat = () => { /* ... código de validação ... */ };
        const validateEmailConfirmation = () => { /* ... código de validação ... */ };
        const validatePasswordStrength = () => { /* ... código de validação ... */ };
        const validatePasswordConfirmation = () => { /* ... código de validação ... */ };
        function checkRegistrationFormValidity() { /* ... código de validação ... */ }
        if (emailError) emailError.dataset.errorMessage = "Formato de e-mail inválido.";
        if (email2Error) email2Error.dataset.errorMessage = "Os e-mails não são iguais.";
        if (password2Error) password2Error.dataset.errorMessage = "As senhas não são iguais.";
        email.addEventListener('input', () => { /* ... */ });
        email2.addEventListener('input', () => { /* ... */ });
        password.addEventListener('input', () => { /* ... */ });
        password2.addEventListener('input', () => { /* ... */ });
        checkRegistrationFormValidity();
    }


    // --- LÓGICA PARA O FORMULÁRIO DE LOGIN ---
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        const usernameInput = document.getElementById('id_username');
        const passwordInput = document.getElementById('id_password');
        const loginButton = document.getElementById('loginButton');

        function checkLoginForm() {
            // Adiciona ou remove a classe 'filled' para o estilo do CSS
            if (usernameInput.value.length > 0) {
                usernameInput.classList.add('filled');
            } else {
                usernameInput.classList.remove('filled');
            }

            if (passwordInput.value.length > 0) {
                passwordInput.classList.add('filled');
            } else {
                passwordInput.classList.remove('filled');
            }

            // Habilita ou desabilita o botão
            const isFormValid = usernameInput.value.length > 0 && passwordInput.value.length > 0;
            loginButton.disabled = !isFormValid;
        }

        // Adiciona os "escutadores" de eventos para rodar a checagem a cada tecla digitada
        usernameInput.addEventListener('input', checkLoginForm);
        passwordInput.addEventListener('input', checkLoginForm);

        // Roda a função uma vez no início para garantir o estado correto do botão
        checkLoginForm();
    }

});