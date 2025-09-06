self.addEventListener("install", (event) => {
  console.log("Service Worker instalado");
});

// Evento de activación: se activa cuando el Service Worker toma el control.
// Esto es útil para limpiar cachés viejos si tuvieras una versión anterior.
self.addEventListener("activate", (event) => {
  console.log("Service Worker activado");
  // Se usa clients.claim() para que el nuevo Service Worker tome control inmediatamente
  // de las páginas abiertas.
  event.waitUntil(self.clients.claim());
});

// Evento de 'fetch': intercepta todas las peticiones de red.
// Aquí, simplemente reenviamos la petición a la red y devolvemos la respuesta.
self.addEventListener("fetch", (event) => {
  event.respondWith(fetch(event.request));
});

// Puedes agregar más lógica aquí para notificaciones push u otras APIs
// específicas de Service Workers.
