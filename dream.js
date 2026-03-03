document.addEventListener('DOMContentLoaded', () => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartCountElement = document.querySelector('.cart-count');
    let cartCount = 0;

    addToCartButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            // Increment the cart count
            cartCount++;
            cartCountElement.textContent = cartCount;
            
            // Visual feedback on the button
            const originalText = e.target.textContent;
            e.target.textContent = 'Added!';
            e.target.style.backgroundColor = '#10b981'; // Green color
            
            // Reset button text after 2 seconds
            setTimeout(() => {
                e.target.textContent = originalText;
                e.target.style.backgroundColor = '#1e293b'; // Original color
            }, 2000);
        });
    });
});
