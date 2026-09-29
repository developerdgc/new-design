# Limos 4 Less — Homepage Redesign

A simpler, more polished homepage for [limos4less.com](https://limos4less.com/). All text, images, and links come from the current website.

**Open `index.html` in a browser to view it.** Screenshots are in `preview/`.

## Structure

Backgrounds alternate dark and light down the page:

| Section | Background |
|---|---|
| Header (unchanged) | White |
| Hero: full width video, 3 feature icons | Dark |
| Trust: Trustpilot badge + 6 client logos | White |
| About Us: photo, "Since 2004" badge, 2x2 stats | Dark |
| Our Services: 3 cards | Light |
| CTA: Book Now / Call + quote form | Blue |
| Occasions: 6 black cards | White |
| Why Customers Book With Us | Dark |
| Blog | Light |
| Footer (unchanged) | Dark |

## Design

Gold is the accent. Headings use Montserrat like the live site. Content width is 1300px with 20px side padding, matching the live homepage. Corners are small (4-8px); cards on light backgrounds have visible borders and a soft shadow.

The quote form in the CTA is not connected yet. Hook it up to the site's form handler (for example the form used on the Contact Us page).

## Files

- `index.html` — page markup
- `styles.css` — styles (no framework)
- `assets/img/` — images taken from the current website
- `preview/` — desktop and mobile screenshots
