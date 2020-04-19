//Function to highlight the cart on the navigation bar when there's more than 0 items in it.
function highlightCart(){
    if (document.getElementById("cart-count").innerHTML > 0) {
        document.getElementById("cart-nav-bar").classList.add("cart-text--green")
    } else {
        document.getElementById("cart-nav-bar").classList.remove("cart-text--green")
    }
}