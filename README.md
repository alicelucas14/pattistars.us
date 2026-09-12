# Teen Patti Stars - Cloned Homepage

Exact replica of the [teenpattistars.io](https://teenpattistars.io/) homepage, complete with all local assets, media, fonts, styles, scripts, interactive components, and responsive design.

## Project Structure

```
.
├── index.html                   # Cloned homepage HTML with full styles and interactive components
├── package.json                 # Project configuration and local server scripts
├── download_assets.py           # Asset scraper script used to pull media
├── images/                      # Downloaded logo and brand assets
│   └── Teen-Patti-Stars-Logo.webp
└── uploads/                     # Hero graphics, video tutorial, promo badges, and game artwork
    ├── 1781004980190.webp       # Hero graphic
    ├── 1778569497278.webp       # Casino games artwork
    ├── TPS-Video.mov            # Installation guide video
    └── ... (other media assets)
```

## How to Preview & Run

You can run the homepage locally using any local web server:

### Option 1: Using Python
```bash
python -m http.server 3000
```
Then visit `http://localhost:3000` in your browser.

### Option 2: Using Node / npx
```bash
npx serve .
```

### Option 3: VSCode / IDE Live Server
Right-click on `index.html` and select **"Open with Live Server"**.
