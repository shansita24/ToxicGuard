const API_URL = "http://127.0.0.1:8000/batch";

async function analyzeTexts(elements) {
    const texts = elements.map(el => el.innerText);
    console.log("TEXTS SENT:", texts);

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ texts })
        });

        const data = await res.json();
        console.log("API RESPONSE:", data);
        data.forEach((result, i) => {
        console.log("RESULT:", result);
        const el = elements[i];

        if (!el) return;

        if (result.toxic === true && result.confidence > 0.7) {
        el.style.background = "rgba(255,0,0,0.3)";
         }
    });

    } catch (err) {
        console.error("API error:", err);
    }
}


function scanComments() {
    const nodes = Array.from(document.querySelectorAll("span"))
        .filter(el => el.innerText.length > 3 && !el.dataset.checked);

    nodes.forEach(el => el.dataset.checked = "true");

    if (nodes.length > 0) {
        analyzeTexts(nodes);
    }
}


// Handle dynamic Instagram loading
const observer = new MutationObserver(() => {
    scanComments();
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});

// Initial run
scanComments();