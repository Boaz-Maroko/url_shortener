let copyBtn = document.getElementById('copy-url'); // Corrected to getElementById

// Add event listeners
copyBtn.addEventListener('click', async function() {
    let copyText = document.getElementById('short-url').innerText; // Corrected variable name

    try {
        // Copy the text.
        await navigator.clipboard.writeText(copyText);
        copyBtn.innerText = 'Copied!';

        setTimeout(function() {
            copyBtn.innerText = 'Copy URL'; // Revert to original text instead of hiding the button
        }, 3000);
    } catch (err) {
        console.error(`Failed to copy: ${err}`); // Corrected the error message
    }
});
