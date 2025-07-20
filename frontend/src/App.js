import React, { useState } from 'react';
import './App.css';
import Login from './Login';
import MovieGallery from './MovieGallery';

function App() {
  // Declaramos el estado del token, inicialmente nulo
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {!token ? (
        // Si NO hay token, mostramos el componente de Login
        <Login setToken={setToken} />
      ) : (
        // Si hay token, mostramos la galería de películas
        <MovieGallery token={token} />
      )}
    </div>
  );
}

export default App;
