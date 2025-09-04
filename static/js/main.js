document.addEventListener('DOMContentLoaded', function() {
    // --- LÓGICA DO HEADER SCROLLED ---
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

    // --- LÓGICA DO CARROSSEL DE PARCEIROS (SCROLLER) ---
    const scrollers = document.querySelectorAll(".scroller");
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        scrollers.forEach((scroller) => {
            addAnimation(scroller);
        });
    }

    // Função addAnimation RESTAURADA da versão 6.0
    function addAnimation(scroller) {
        const scrollerInner = scroller.querySelector(".scroller-inner");
        const scrollerContent = Array.from(scrollerInner.children);

        // Trava de segurança para evitar erros se não houver logos.
        if (scrollerContent.length === 0) {
            return;
        }

        // Etapa 1: Garante que o conteúdo seja largo o suficiente para preencher o scroller
        let contentWidth = 0;
        scrollerContent.forEach(item => {
            const style = window.getComputedStyle(item);
            contentWidth += item.offsetWidth +
                (parseFloat(style.marginLeft) || 0) + (parseFloat(style.marginRight) || 0);
        });

        if (contentWidth > 0 && contentWidth < scroller.offsetWidth) {
            const clonesNeeded = Math.ceil(scroller.offsetWidth / contentWidth);
            for (let i = 0; i < clonesNeeded; i++) {
                scrollerContent.forEach(item => {
                    const duplicatedItem = item.cloneNode(true);
                    duplicatedItem.setAttribute('aria-hidden', true);
                    scrollerInner.appendChild(duplicatedItem);
                });
            }
        }

        // Etapa 2: Duplica todo o conteúdo (agora já preenchido) para o loop da animação
        const finalContent = Array.from(scrollerInner.children);
        finalContent.forEach(item => {
            const duplicatedItem = item.cloneNode(true);
            duplicatedItem.setAttribute('aria-hidden', true);
            scrollerInner.appendChild(duplicatedItem);
        });

        scroller.setAttribute("data-animated", "true");
    }

    // --- LÓGICA DO SLIDESHOW HERO ---
    const heroSlides = document.querySelectorAll('.hero-slide');
    if (heroSlides.length > 1) {
        let currentHeroSlide = 0;
        setInterval(function() {
            if (heroSlides[currentHeroSlide]) {
                heroSlides[currentHeroSlide].classList.remove('is-active');
            }
            currentHeroSlide = (currentHeroSlide + 1) % heroSlides.length;
            if (heroSlides[currentHeroSlide]) {
                heroSlides[currentHeroSlide].classList.add('is-active');
            }
        }, 10000); // Troca de slide a cada 10 segundos
    }

    // -------------------------------------------------------------------
    // --- NOVO CÓDIGO PARA FORMULÁRIOS (COMPLETO E ATUALIZADO) ---
    // -------------------------------------------------------------------

    // Função global para o callback do reCAPTCHA
    window.recaptchaCallback = function() {
        const registrationForm = document.getElementById('registrationForm');
        if (registrationForm) {
            checkRegistrationFormValidity();
        }
    };

    // Função para exibir mensagens de aviso temporárias
    const showTemporaryMessage = (messageElement) => {
        if (messageElement) {
            messageElement.classList.add('show');
            setTimeout(() => {
                messageElement.classList.remove('show');
            }, 3000); // A mensagem some após 3 segundos
        }
    };

    // --- Lógica do Formulário de Registro ---
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        const userTypeRadios = document.querySelectorAll('input[name="user_type"]');
        const username = document.getElementById('id_username');
        const email = document.getElementById('id_email');
        const email2 = document.getElementById('id_email2');
        const password = document.getElementById('id_password1');
        const password2 = document.getElementById('id_password2');
        const submitButton = document.getElementById('submitButton');
        const formMessage = document.getElementById('form-message');

        const emailError = document.getElementById('email-error');
        const email2Error = document.getElementById('email2-error');
        const password2Error = document.getElementById('password2-error');
        const passwordFeedback = document.getElementById('password-feedback');

        const iconError = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293z"/></svg>';
        const iconSuccess = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/></svg>';

        const passwordRules = [
            { regex: /.{8,}/, text: "Pelo menos 8 caracteres" },
            { regex: /[A-Z]/, text: "Pelo menos uma letra maiúscula" },
            { regex: /[a-z]/, text: "Pelo menos uma letra minúscula" },
            { regex: /[0-9]/, text: "Pelo menos um número" },
        ];

        const rulesContainer = passwordFeedback.querySelector('.validation-rules');
        if (rulesContainer) {
            rulesContainer.innerHTML = '';
            passwordRules.forEach((rule, index) => {
                const ruleDiv = document.createElement('div');
                ruleDiv.id = `rule-${index}`;
                ruleDiv.classList.add('invalid');
                ruleDiv.innerHTML = `<span class="validation-icon">${iconError}</span><span>${rule.text}</span>`;
                rulesContainer.appendChild(ruleDiv);
            });
        }

        const validateEmailFormat = () => {
            if (!email) return false;
            const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value);
            email.classList.toggle('valid', isValid && email.value.length > 0);
            email.classList.toggle('invalid', !isValid && email.value.length > 0);
            if (emailError) emailError.textContent = (!isValid && email.value.length > 0) ? "Formato de e-mail inválido." : "";
            return isValid;
        };

        const validateEmailConfirmation = () => {
            if (!email || !email2) return false;
            const isValid = email.value === email2.value && email.value.length > 0;
            email2.classList.toggle('valid', isValid && email2.value.length > 0);
            email2.classList.toggle('invalid', !isValid && email2.value.length > 0);
            if (email2Error) email2Error.textContent = (!isValid && email2.value.length > 0) ? "Os e-mails não são iguais." : "";
            return isValid;
        };

        const validatePasswordStrength = () => {
            if (!password) return false;
            let allValid = true;
            passwordRules.forEach((rule, index) => {
                const ruleDiv = document.getElementById(`rule-${index}`);
                if (!ruleDiv) return;
                const iconSpan = ruleDiv.querySelector('.validation-icon');
                if (rule.regex.test(password.value)) {
                    ruleDiv.classList.add('valid');
                    ruleDiv.classList.remove('invalid');
                    iconSpan.innerHTML = iconSuccess;
                } else {
                    ruleDiv.classList.remove('valid');
                    ruleDiv.classList.add('invalid');
                    iconSpan.innerHTML = iconError;
                    allValid = false;
                }
            });
            password.classList.toggle('valid', allValid);
            password.classList.toggle('invalid', !allValid && password.value.length > 0);
            return allValid;
        };

        const validatePasswordConfirmation = () => {
            if (!password || !password2) return false;
            const isValid = password.value === password2.value && password.value.length > 0;
            password2.classList.toggle('valid', isValid && password2.value.length > 0);
            password2.classList.toggle('invalid', !isValid && password2.value.length > 0);
            if (password2Error) password2Error.textContent = (!isValid && password2.value.length > 0) ? "As senhas não são iguais." : "";
            return isValid;
        };

        const checkRegistrationFormValidity = () => {
            const isUserTypeSelected = Array.from(userTypeRadios).some(radio => radio.checked);
            const isEmailValid = email.classList.contains('valid');
            const isEmail2Valid = email2.classList.contains('valid');
            const isPasswordValid = password.classList.contains('valid');
            const isPassword2Valid = password2.classList.contains('valid');
            const recaptchaResponse = document.getElementById('g-recaptcha-response');
            const isRecaptchaValid = recaptchaResponse && recaptchaResponse.value !== '';

            if (submitButton) {
                const allValid = isUserTypeSelected && isEmailValid && isEmail2Valid && isPasswordValid && isPassword2Valid && isRecaptchaValid;
                submitButton.disabled = !allValid;
            }
        };

        if (submitButton) {
            submitButton.addEventListener('click', function(event) {
                if (submitButton.disabled) {
                    event.preventDefault();
                    showTemporaryMessage(formMessage);
                }
            });
        }
        
        const allInputs = [username, email, email2, password, password2];
        allInputs.forEach(input => {
            if(input) {
                input.addEventListener('input', () => {
                    validateEmailFormat();
                    validateEmailConfirmation();
                    validatePasswordStrength();
                    validatePasswordConfirmation();
                    checkRegistrationFormValidity();
                });
            }
        });

        userTypeRadios.forEach(radio => radio.addEventListener('change', checkRegistrationFormValidity));
        
        // Adiciona um observador para o reCAPTCHA, já que o callback pode ser difícil de implementar
        const recaptchaResponseEl = document.getElementById('g-recaptcha-response');
        if (recaptchaResponseEl) {
            const observer = new MutationObserver(() => {
                recaptchaCallback();
            });
            observer.observe(recaptchaResponseEl, {
                attributes: true,
                attributeFilter: ['value']
            });
        }

        checkRegistrationFormValidity();
    }

    // --- Lógica do Formulário de Login ---
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        const usernameInput = document.getElementById('id_username');
        const passwordInput = document.getElementById('id_password');
        const loginButton = document.getElementById('loginButton');
        const formMessage = document.getElementById('form-message');

        function checkLoginForm() {
            usernameInput.classList.toggle('filled', usernameInput.value.length > 0);
            passwordInput.classList.toggle('filled', passwordInput.value.length > 0);
            
            const isFormValid = usernameInput.value.length > 0 && passwordInput.value.length >= 8;
            
            if (loginButton) {
                loginButton.disabled = !isFormValid;
            }
        }

        if (loginButton) {
            loginButton.addEventListener('click', function(event) {
                if (loginButton.disabled) {
                    event.preventDefault();
                    showTemporaryMessage(formMessage);
                }
            });
        }

        usernameInput.addEventListener('input', checkLoginForm);
        passwordInput.addEventListener('input', checkLoginForm);
        
        checkLoginForm();
    }
});