const form = document.querySelector("#chat-form");
const messageInput = document.querySelector("#message");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    result.textContent = "傳送中…";

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: messageInput.value }),
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const data = await response.json();
        result.textContent = data.reply;
    } catch (error) {
        result.textContent = `連線失敗：${error.message}`;
    }
});
