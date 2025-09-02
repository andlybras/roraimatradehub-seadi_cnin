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
    const form = document.getElementById('registrationForm');
    if (form) {
        const email = document.getElementById('id_email');
        const email2 = document.getElementById('id_email2');
        const password = document.getElementById('id_password');
        const password2 = document.getElementById('id_password2');
        const submitButton = document.getElementById('submitButton');
        const emailError = document.getElementById('email-error');
        const email2Error = document.getElementById('email2-error');
        const password2Error = document.getElementById('password2-error');
        const passwordFeedback = document.getElementById('password-feedback');
        const iconError = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/></svg>`;
        const iconSuccess = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/></svg>`;
        const passwordRules = [
            { regex: /.{8,}/, text: "Pelo menos 8 caracteres" },
            { regex: /[A-Z]/, text: "Pelo menos uma letra maiúscula" },
            { regex: /[a-z]/, text: "Pelo menos uma letra minúscula" },
            { regex: /[0-9]/, text: "Pelo menos um número" },
        ];
        const rulesContainer = passwordFeedback.querySelector('.validation-rules');
        rulesContainer.innerHTML = '';
        passwordRules.forEach((rule, index) => {
            const ruleDiv = document.createElement('div');
            ruleDiv.id = `rule-${index}`;
            ruleDiv.classList.add('invalid');
            ruleDiv.innerHTML = `<span class="validation-icon">${iconError}</span><span>${rule.text}</span>`;
            rulesContainer.appendChild(ruleDiv);
        });
        const validators = {
            email: () => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value),
            email2: () => email.value === email2.value && email.value.length > 0,
            password: () => passwordRules.every(rule => rule.regex.test(password.value)),
            password2: () => password.value === password2.value && password.value.length > 0
        };
        function validateField(field, errorElement, validator) {
            if (field.value.length === 0) {
                field.classList.remove('valid', 'invalid');
                if (errorElement) errorElement.textContent = '';
                return false;
            }           
            const isValid = validator();
            field.classList.toggle('valid', isValid);
            field.classList.toggle('invalid', !isValid);            
            if (errorElement) {
                errorElement.textContent = isValid ? '' : errorElement.dataset.errorMessage;
            }
            return isValid;
        }
        function validatePassword() {
            let allValid = true;
            passwordRules.forEach((rule, index) => {
                const ruleDiv = document.getElementById(`rule-${index}`);
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
        }
        function checkFormValidity() {
            const isEmailValid = validateField(email, emailError, validators.email);
            const isEmail2Valid = validateField(email2, email2Error, validators.email2);
            const isPasswordValid = validatePassword();
            const isPassword2Valid = validateField(password2, password2Error, validators.password2);
            
            submitButton.disabled = !(isEmailValid && isEmail2Valid && isPasswordValid && isPassword2Valid);
        }
        emailError.dataset.errorMessage = "Formato de e-mail inválido.";
        email2Error.dataset.errorMessage = "Os e-mails não são iguais.";
        password2Error.dataset.errorMessage = "As senhas não são iguais.";
        form.addEventListener('input', checkFormValidity);
        checkFormValidity();
    }
});