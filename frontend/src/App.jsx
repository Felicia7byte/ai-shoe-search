import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!query.trim()) {
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_URL}/search`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
          top_k: 10,
        }),
      });

      if (!response.ok) {
        throw new Error("Search request failed");
      }

      const data = await response.json();

      setResults(data.results);
    } catch (err) {
      console.error(err);
      setError("Gagal menghubungi backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="hero">
        <h1>AI Shoe Search</h1>
        <p>Find shoes using natural language</p>

        <div className="search-box">
          <input
            type="text"
            placeholder="Try: white running shoes"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSearch();
              }
            }}
          />

          <button onClick={handleSearch} disabled={loading}>
            {loading ? "Searching..." : "Search"}
          </button>
        </div>
      </header>

      <main className="results-container">
        {error && <p className="error">{error}</p>}

        {!loading && results.length === 0 && !error && (
          <p className="empty">
            Search for something like "white running shoes"
          </p>
        )}

        <div className="results-grid">
          {results.map((shoe, index) => (
            <div className="shoe-card" key={index}>
              <div className="image-container">
                <img
                  src={`${API_URL}/${shoe.path}`}
                  alt={`Shoe ${index + 1}`}
                />
              </div>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;
