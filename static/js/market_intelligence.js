document.addEventListener('DOMContentLoaded', function () {
    const moduleContainer = document.getElementById('intelligence-module-container');

    if (!moduleContainer) return; // Só executa se estivermos na página certa

    let currentCategory = null; // Guarda a categoria da lista de cards que estamos vendo

    const fetchAndInject = (url, container) => {
        container.innerHTML = '<p>Carregando...</p>'; // Feedback visual
        fetch(url, {
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                container.innerHTML = data.html;
                // Executa scripts dos gráficos se existirem
                const scripts = container.querySelectorAll('script');
                scripts.forEach(script => {
                    const newScript = document.createElement('script');
                    newScript.text = script.innerText;
                    document.body.appendChild(newScript).parentNode.removeChild(newScript);
                });
            }
        })
        .catch(error => {
            console.error('Erro ao carregar conteúdo:', error);
            container.innerHTML = '<p>Ocorreu um erro ao carregar o conteúdo.</p>';
        });
    };

    // Funções para cada estado da tela
    const showInitialView = () => {
        currentCategory = null;
        fetchAndInject('/inteligencia-de-mercado/initial-view/', moduleContainer);
    };

    const showCardListView = (categoria) => {
        currentCategory = categoria;
        fetchAndInject(`/inteligencia-de-mercado/cards/${categoria}/`, moduleContainer);
    };

    const showDetailView = (cardId) => {
        fetchAndInject(`/inteligencia-de-mercado/card/${cardId}/`, moduleContainer);
    };

    // Event Delegation para todo o módulo
    moduleContainer.addEventListener('click', function(event) {
        const categoryButton = event.target.closest('.category-button');
        const cardLink = event.target.closest('.card-link');
        const backToInitialButton = event.target.closest('#back-to-initial-button');
        const backToListButton = event.target.closest('#back-to-list-button');

        if (categoryButton) {
            event.preventDefault();
            const categoria = categoryButton.dataset.categoria;
            showCardListView(categoria);
        } else if (cardLink) {
            event.preventDefault();
            const cardId = cardLink.dataset.cardId;
            showDetailView(cardId);
        } else if (backToInitialButton) {
            event.preventDefault();
            showInitialView();
        } else if (backToListButton) {
            event.preventDefault();
            if (currentCategory) {
                showCardListView(currentCategory);
            } else {
                showInitialView(); // Fallback de segurança
            }
        }
    });

    // Carrega a visualização inicial ao entrar na página
    showInitialView();
});