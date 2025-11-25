let ws;

function startBuild() {
    const idea = document.getElementById('ideaInput').value;
    if (!idea) return;

    // Reset UI
    document.getElementById('buildBtn').disabled = true;
    document.getElementById('terminalOutput').innerHTML = '';
    document.getElementById('specOutput').innerHTML = '<p class="placeholder-text">Generating spec...</p>';
    document.getElementById('archOutput').innerHTML = '<p class="placeholder-text">Waiting for spec...</p>';

    // Switch to terminal tab initially
    switchTab('terminal');

    // Connect WebSocket
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    ws = new WebSocket(`${protocol}//${window.location.host}/ws/build`);

    ws.onopen = () => {
        log("Connected to Ryha Engine...");
        ws.send(idea);
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === 'log') {
            log(data.message);
        } else if (data.type === 'status') {
            // Could update status indicators here
        } else if (data.type === 'artifact') {
            if (data.name === 'Product Specification') {
                renderMarkdown('specOutput', data.content);
                log(">> Artifact created: Product Specification");
            } else if (data.name === 'System Architecture') {
                renderMarkdown('archOutput', data.content);
                log(">> Artifact created: System Architecture");
            }
        } else if (data.type === 'complete') {
            log(">> Build Cycle Complete.");
            document.getElementById('buildBtn').disabled = false;
            ws.close();
        } else if (data.type === 'done') {
            ws.close();
            document.getElementById('buildBtn').disabled = false;
        }
    };

    ws.onerror = (error) => {
        log("Error: Connection lost.");
        console.error(error);
        document.getElementById('buildBtn').disabled = false;
    };

    ws.onclose = () => {
        document.getElementById('buildBtn').disabled = false;
    };
}

function log(message) {
    const term = document.getElementById('terminalOutput');
    const line = document.createElement('div');
    line.className = 'log-line';
    line.innerText = message;
    term.appendChild(line);
    term.scrollTop = term.scrollHeight;
}

function switchTab(tabId) {
    // Hide all contents
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    // Deactivate all buttons
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

    // Activate target
    document.getElementById(tabId).classList.add('active');
    // Activate button (simple search)
    const btns = document.querySelectorAll('.tab-btn');
    if (tabId === 'terminal') btns[0].classList.add('active');
    if (tabId === 'spec') btns[1].classList.add('active');
    if (tabId === 'architecture') btns[2].classList.add('active');
}

function renderMarkdown(elementId, markdown) {
    // Simple markdown renderer for the MVP
    // In production, use a library like marked.js
    const el = document.getElementById(elementId);
    let html = markdown
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^\- (.*$)/gim, '<li>$1</li>')
        .replace(/\*\*(.*)\*\*/gim, '<b>$1</b>')
        .replace(/\n/gim, '<br>');

    el.innerHTML = html;
}
