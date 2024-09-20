<script lang="ts">
    import { fade, fly, type TransitionConfig } from 'svelte/transition';
    import { onMount } from 'svelte';

    import formulaOneCar from '../images/formula1car.png';
    import f1Track from '../images/f1tracks.png';
    import f1Grid from '../images/f1grid.png'; 

    let showContent: boolean = false;
  
    onMount(() => {
      showContent = true;
    });
  
    interface Race {
      name: string;
      date: string;
    }
  
    const races: Race[] = [
      { name: "Monaco Grand Prix", date: "May 28, 2024" },
      { name: "British Grand Prix", date: "July 7, 2024" },
      { name: "Italian Grand Prix", date: "September 1, 2024" }
    ];
  
    function handleSubmit(event: Event): void {
      event.preventDefault();
      // Add form submission logic here
      console.log("Form submitted");
    }
  
    function flyIn(node: Element, options?: TransitionConfig): TransitionConfig {
      return fly(node, { y: 50, duration: 500, ...options });
    }
</script>

{#if showContent}
<section in:fade>
    <h1>Welcome to FormulaUn</h1>
    <p>Experience the thrill of Formula 1 racing!</p>
    <img src={formulaOneCar} alt="Formula 1 car" />
</section>

<section in:flyIn>
    <h2>About FormulaUn</h2>
    <p>FormulaUn is your ultimate destination for all things Formula 1.</p>
    <img src={f1Track} alt="F1 track" />
</section>

<section in:flyIn>
    <h2>Upcoming Races</h2>
    <ul>
    {#each races as race}
        <li>{race.name} - {race.date}</li>
    {/each}
    </ul>
    <img src={f1Grid} alt="F1 race start" />
</section>

<section in:flyIn>
    <h2>Contact Us</h2>
    <p>Get in touch with us for more information.</p>
    <form on:submit={handleSubmit}>
    <input type="text" placeholder="Name" required />
    <input type="email" placeholder="Email" required />
    <textarea placeholder="Message" required></textarea>
    <button type="submit">Send</button>
    </form>
</section>
{/if}

<style>
section {
    margin-bottom: 3rem;
}

img {
    max-width: 100%;
    height: auto;
}

form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

input, textarea, button {
    padding: 0.5rem;
}
</style>