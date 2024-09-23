<script lang="ts">
    import { fade, fly, type TransitionConfig } from 'svelte/transition';
    import { onMount } from 'svelte';
    import { tweened } from 'svelte/motion';

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
      image: string;
    }
  
    const races: Race[] = [
      { name: "Italian Grand Prix", date: "September 1, 2024", image: f1Grid },
      { name: "Azerbaijan Grand Prix", date: "September 15, 2024", image: f1Grid },
      { name: "Singapore Grand Prix", date: "September 22, 2024", image: f1Grid }
    ];
  
    function handleSubmit(event: Event): void {
      event.preventDefault();
      // Add form submission logic here
      console.log("Form submitted");
    }
  
    function flyIn(node: Element, options?: TransitionConfig): TransitionConfig {
      return fly(node, { y: 50, duration: 500, ...options });
    }

    let currFrame = 0;
    const totalFrames = 19;
    const scrollProgress = tweened(0);

    onMount(() => {
      showContent = true;

      const handleScroll = () => {
        const scrollPosition = window.scrollY;
        const maxScrollDist = 800;
        const progress = Math.min(scrollPosition / maxScrollDist, 1);

        scrollProgress.set(progress);
      };

      window.addEventListener('scroll', handleScroll);

      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    });

    $: currFrame = Math.floor($scrollProgress * (totalFrames - 1));

    function getImageSrc(frame: number) {
      return `src/frames/frame_${String(frame).padStart(2, '0')}_delay-0.06s.png`;
    }



</script>

{#if showContent}
<section in:fade class="split-section">
  <div class="img-cont">
    <img src={getImageSrc(currFrame)} alt="Formula 1 car" />
  </div>
  <div class="text-cont">
    <h1>Welcome to Formula <t>Un</t></h1>
    <p>Experience the thrill of Formula 1 racing!</p>
  </div>
</section>

<section in:flyIn>
    <h2>About FormulaUn</h2>
    <p>FormulaUn is your ultimate destination for all things Formula 1.</p>
    <img src={f1Track} alt="F1 track" />
</section>

<section in:flyIn>
  <div class="upcoming-races">
    <h2>Upcoming Races</h2>
    <div class="race-grid">
      {#each races as race}
        <div class="race-card">
          <div class="image-wrapper">
            <img src={race.image} alt={`${race.name} circuit`} />
          </div>
          <div class="race-info">
            <h3>{race.name}</h3>
            <p>{race.date}</p>
          </div>
        </div>
      {/each}
    </div>
  </div>
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
    margin: 5%;
}

.split-section {
  display: flex;
  align-items: stretch;
  gap: 5%;
  height: calc(100vh - 56px);
  margin-bottom: 0;
  margin: 5%;
}

.text-cont {
  flex: 0 0 35%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 2rem;
}
.text-cont t {
    color: #e10600;
}

.img-cont {
  flex: 0 0 60%;
  position: relative;
  overflow: hidden;
}

.img-cont img {
  width: 100%;
  height: auto;
  object-fit: cover;
  object-position: center;
  border-radius: 25px;
}

.upcoming-races {
  background-color: #f3f4f6;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  font-size: 1.875rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  text-align: center;
}

.race-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.race-card {
  background-color: white;
  padding: 0.5rem;
  overflow: hidden;
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.race-card:hover {
  transform: scale(1.05);
}

.image-wrapper {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  text-align: center;
}

p {
  color: #4b5563;
  text-align: center;
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

@media (max-width: 768px) {
  .split-section {
    flex-direction: column;
    height: auto;
  }

  .split-section .img-cont,
  .split-section .text-cont {
    flex: 0 0 100%;
  }

  .split-section .img-cont {
    height: 50vh;
  }

  .race-grid {
    grid-template-columns: 1fr;
  }
}
</style>