<script lang="ts">
    import { onMount } from 'svelte';
    import { fade, fly } from 'svelte/transition';
  
    let showContent = false;
  
    onMount(() => {
      showContent = true;
    });
  </script>
  
  {#if showContent}
  <div class="error-page" in:fade={{ duration: 300 }}>
    <div class="content" in:fly={{ y: 50, duration: 500, delay: 300 }}>
      <h1>404</h1>
      <h2>Oops! You've gone off track</h2>
      <p>The page you're looking for seems to have taken a detour.</p>
      <div class="car-animation">
        <div class="smoke">💨</div>
        <div class="car">🏎️</div>
      </div>
      <a href="/" class="btn">Return to Pit Lane (Home)</a>
    </div>
  </div>
  {/if}
  
  <style>
    .error-page {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f3f4f6;
      font-family: Arial, sans-serif;
    }
  
    .content {
      text-align: center;
      background-color: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
  
    h1 {
      font-size: 6rem;
      color: #e10600;
      margin: 0;
    }
  
    h2 {
      font-size: 2rem;
      color: #15151e;
      margin-top: 0;
    }
  
    p {
      font-size: 1.2rem;
      color: #15151e;
      margin-bottom: 2rem;
    }
  
    .btn {
      display: inline-block;
      background-color: #e10600;
      color: white;
      padding: 0.75rem 1.5rem;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      transition: background-color 0.3s ease;
    }
  
    .btn:hover {
      background-color: #b30500;
    }
  
    .car-animation {
      position: relative;
      height: 60px;
      margin: 2rem 0;
      overflow: hidden;
    }
  
    .car {
      font-size: 3rem;
      position: absolute;
      right: -50px;
      animation: drive 4s linear infinite;
    }
  
    .smoke {
      font-size: 2rem;
      position: absolute;
      right: -80px;
      top: 15px;
      opacity: 0;
      animation: smoke 4s linear infinite;
    }
  
    @keyframes drive {
      0% { right: -50px; }
      100% { right: calc(100% + 50px); }
    }
  
    @keyframes smoke {
      0% { right: -100px; opacity: 0; }
      20% { opacity: 1; }
      60% { opacity: 0; }
      100% { right: calc(100% + 80px); opacity: 0; }
    }
  </style>