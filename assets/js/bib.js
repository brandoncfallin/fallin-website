// Load bibliography data from an external JSON file
let bibliographyData = [];

// Function to fetch the bibliography data from the JSON file in /assets directory
async function loadBibliographyData() {
    try {
        const response = await fetch('/assets/fallin-bib.json');
        if (!response.ok) {
            throw new Error(`Failed to load bibliography data: ${response.status} ${response.statusText}`);
        }
        bibliographyData = await response.json();
        // After loading the data, render the bibliography
        renderBibliography();
    } catch (error) {
        console.error('Error loading bibliography data:', error);
        document.getElementById('bibliography').innerHTML = `<p class="error">Error loading bibliography: ${error.message}</p>`;
    }
}

// Function to format authors in IEEE style with specific author highlighted
function formatAuthors(authorString) {
    const authors = authorString.split(' and ');
    let formattedAuthors = '';
    
    authors.forEach((author, index) => {
        // Handle different name formats
        let family = '';
        let given = '';
        
        // Check if the name is in "LastName, FirstName" format
        if (author.includes(', ')) {
            const nameParts = author.split(', ');
            family = nameParts[0];
            given = nameParts[1];
        }
        // Handle "FirstName MiddleName LastName" format (as in arXiv entries)
        else {
            const nameParts = author.split(' ');
            family = nameParts[nameParts.length - 1]; // Last part is family name
            given = nameParts.slice(0, nameParts.length - 1).join(' '); // All but last are given names
        }
        
        // Format as initials + family name
        const initials = given.split(' ').map(name => name.charAt(0) + '.').join(' ');
        
        // Add separator based on position
        if (index > 0) {
            formattedAuthors += index === authors.length - 1 ? ' and ' : ', ';
        }
        
        // Bold if the author is Brandon Fallin (with or without middle initial)
        if (family === 'Fallin' && (given.startsWith('Brandon') || given.includes('Brandon'))) {
            formattedAuthors += '<strong>' + initials + ' ' + family + '</strong>';
        } else {
            formattedAuthors += initials + ' ' + family;
        }
    });
    
    return formattedAuthors;
}

// Function to format citations in IEEE style
function formatIEEECitation(entry) {
    let citation = '';
    
    // Authors
    if (entry.author) {
        citation += formatAuthors(entry.author) + ', ';
    }
    
    // Title in quotes, with link if URL is present
    if (entry.url) {
        // Updated code
        citation += `<a href="${entry.url}" target="_blank">"${entry.title}"</a>, `;
    } else {
        citation += `"${entry.title}", `;
    }
    
    // Conference/journal title in italics
    if (entry.booktitle) {
        citation += `<em>${entry.booktitle}</em>, `;
    } else if (entry.archiveprefix && entry.eprint) {
        // Handle arXiv entries - show "arXiv preprint:eprint"
        citation += `<em>arXiv preprint:${entry.eprint}</em>, `;
    }
    
    // Volume and number
    if (entry.volume && entry.volume !== '') {
        citation += `vol. ${entry.volume}`;
        if (entry.number && entry.number !== '') {
            citation += `, no. ${entry.number}`;
        }
        citation += ', ';
    }
    
    // Pages
    if (entry.pages && entry.pages !== '') {
        citation += `pp. ${entry.pages}, `;
    }
    
    // Year
    if (entry.year) {
        citation += entry.year;
    }
    
    // Removed DOI and URL links as requested
    
    return citation + '.';
}

// Function to render bibliography
function renderBibliography() {
    const bibliographyElement = document.getElementById('bibliography');
    if (!bibliographyElement) return;
    
    let html = '<ol class="bibliography">';
    bibliographyData.forEach(entry => {
        html += `<li id="${entry.ID}">${formatIEEECitation(entry)}</li>`;
    });
    html += '</ol>';
    
    bibliographyElement.innerHTML = html;
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Load the bibliography data, which will then render it when complete
    loadBibliographyData();
});