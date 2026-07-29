"use client";

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");

  const handleClick = async () => {
    const res = await fetch("http://localhost:8000/echo", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    setResponse(data.message);
  };

  return (
    <div>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{color:"black",backgroundColor:"white",border:"1px solid gray"}}
      />
      <button onClick={handleClick}>Send</button>
      <p>{response}</p>
    </div>
  );
}