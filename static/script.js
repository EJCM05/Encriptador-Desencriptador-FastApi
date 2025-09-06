const encryptText = async () => {
  const text = document.getElementById("encrypt-input").value;
  if (!text) {
    document.getElementById("encrypt-result").innerText =
      "Por favor, introduce texto para encriptar.";
    return;
  }
  const response = await fetch("/encrypt/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text }),
  });
  const data = await response.json();
  document.getElementById("encrypt-result").innerText =
    data.encrypted_text || data.error;
};

const decryptText = async () => {
  const text = document.getElementById("decrypt-input").value;
  if (!text) {
    document.getElementById("decrypt-result").innerText =
      "Por favor, introduce texto para desencriptar.";
    return;
  }
  const response = await fetch("/decrypt/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text }),
  });
  const data = await response.json();
  document.getElementById("decrypt-result").innerText =
    data.decrypted_text || data.error;
};
const copyToClipboard = async (elementId) => {
  const textElement = document.getElementById(elementId);
  const textToCopy = textElement.innerText;

  // Verificar si la API del portapapeles está disponible
  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      await navigator.clipboard.writeText(textToCopy);
      alert("Texto copiado al portapapeles.");
    } catch (err) {
      console.error("Error al copiar el texto: ", err);
      // Fallback para entornos inseguros
      copyFallback(textToCopy);
    }
  } else {
    // Fallback si la API no está disponible (ej. en HTTP no-localhost)
    copyFallback(textToCopy);
  }
};

// Función de respaldo para copiar el texto
const copyFallback = (text) => {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  try {
    document.execCommand("copy");
    alert("Texto copiado al portapapeles (método de respaldo).");
  } catch (err) {
    console.error("Error al copiar el texto (fallback): ", err);
    alert("No se pudo copiar el texto. Por favor, cópialo manualmente.");
  }
  document.body.removeChild(textarea);
};
