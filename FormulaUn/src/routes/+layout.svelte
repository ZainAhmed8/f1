<script lang="ts">
    import '../app.css'; // Assuming you have a global CSS file
</script>

<div class="layout">

    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/races">Races</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>
    
    <main>
        <slot />
    </main>
</div>
    
<style>
    .layout {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }

    nav {
        background-color: #f1f1f1;
        padding: 1rem;
    }

    nav ul {
        list-style-type: none;
        display: flex;
        justify-content: space-around;
        max-width: 800px;
        margin: 0 auto;
    }

    nav a {
        text-decoration: none;
        color: #333;
        font-weight: bold;
    }

    main {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
</style>