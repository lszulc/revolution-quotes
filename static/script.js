function loadNewQuote() {
    fetch("/api/random")
        .then(response => response.json())
        .then(data => {
            document.getElementById("quote-text").innerText = `„${data.content}”`;
            document.getElementById("quote-author").innerText = `— ${data.author}`;
        })
        .catch(error => console.error("Error fetching quote:", error));
}
