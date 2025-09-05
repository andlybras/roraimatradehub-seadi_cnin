document.addEventListener('DOMContentLoaded', function () {
    const contentArea = document.getElementById('intelligence-content-area');
    const categoryLinks = document.querySelectorAll('.category-link');

    let currentCategory = null;

    const fetchAndDisplayCards = (categoria) => {

        currentCategory = categoria;

        fetch(`/inteligencia-de-mercado/cards/${categoria}/`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                contentArea.innerHTML = data.html;
            }
        })
        .catch(error => {
            console.error('Erro ao buscar os cards:', error);
            contentArea.innerHTML = '<p>Ocorreu um erro ao carregar o conteúdo. Tente novamente mais tarde.</p>';
        });
    };

    const fetchAndDisplayDetail = (cardId) => {
        fetch(`/inteligencia-de-mercado/card/${cardId}/`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                contentArea.innerHTML = data.html;

                const scripts = contentArea.querySelectorAll('script');
                scripts.forEach(script => {
                    const newScript = document.createElement('script');
                    newScript.text = script.innerText;
                    document.body.appendChild(newScript).parentNode.removeChild(newScript);
                });
            }
        })
        .catch(error => {
            console.error('Erro ao buscar o detalhe do card:', error);
            contentArea.innerHTML = '<p>Ocorreu um erro ao carregar o conteúdo. Tente novamente mais tarde.</p>';
        });
    };
    categoryLinks.forEach(link => {
        link.addEventListener('click', () => {
            const categoria = link.dataset.categoria;
            fetchAndDisplayCards(categoria);
        });
    });
    contentArea.addEventListener('click', function(event) {
        const cardLink = event.target.closest('.card-link');
        if (cardLink) {
            event.preventDefault();
            const cardId = cardLink.dataset.cardId;
            fetchAndDisplayDetail(cardId);
        }
        const backButton = event.target.closest('#back-to-list-button');
        if (backButton) {
            if (currentCategory) {
                fetchAndDisplayCards(currentCategory);
            }
        }
    });
});