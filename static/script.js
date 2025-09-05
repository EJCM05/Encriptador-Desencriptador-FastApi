const encryptText = async () => {
            const text = document.getElementById('encrypt-input').value;
            if (!text) {
                document.getElementById('encrypt-result').innerText = "Por favor, introduce texto para encriptar.";
                return;
            }
            const response = await fetch('/encrypt/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            const data = await response.json();
            document.getElementById('encrypt-result').innerText = data.encrypted_text || data.error;
        };

        const decryptText = async () => {
            const text = document.getElementById('decrypt-input').value;
             if (!text) {
                document.getElementById('decrypt-result').innerText = "Por favor, introduce texto para desencriptar.";
                return;
            }
            const response = await fetch('/decrypt/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            const data = await response.json();
            document.getElementById('decrypt-result').innerText = data.decrypted_text || data.error;
        };

        // Función para copiar al portapapeles
        const copyToClipboard = async (elementId) => {
            const textElement = document.getElementById(elementId);
            const textToCopy = textElement.innerText;

            try {
                await navigator.clipboard.writeText(textToCopy);
            } catch (err) {
                console.error('Error al copiar el texto: ', err);
            }
        };