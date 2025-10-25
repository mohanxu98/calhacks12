# CalHacks12 - Minimal Theme Variations Documentation

## Overview
This project demonstrates minimal variations of a base Flask landing page template. Each variation focuses on changing only **one specific design element** while keeping everything else identical to the original.

## Base Template
- **File**: `templates/index.html`
- **CSS**: `static/css/style.css`
- **URL**: `http://localhost:5000/`

## Theme Variations

### 1. Color Variation (`/colors`)
**What Changed**: Only colors and gradients
- **Background**: Purple-blue gradient → Green-teal gradient
- **Text Gradient**: Purple-blue → Green-teal
- **Button Gradient**: Purple-blue → Green-teal
- **Feature Titles**: Purple → Green-teal
- **Button Hover Shadow**: Purple → Green-teal

**Files Modified**:
- `templates/colors.html`
- `static/css/colors.css`

**Elements Affected**:
- `body` background gradient
- `h1` text gradient
- `.button` background gradient
- `.feature h3` color
- `.button:hover` box-shadow color

---

### 2. Size Variation (`/sizes`)
**What Changed**: Only element dimensions and font sizes
- **Container Padding**: 60px → 80px
- **Container Max-width**: 600px → 700px
- **H1 Font Size**: 2.5em → 3em
- **Paragraph Font Size**: 1.2em → 1.4em
- **Button Padding**: 15px 40px → 20px 50px
- **Button Font Size**: 1.1em → 1.3em
- **Feature Icon Size**: 2em → 2.5em
- **Feature H3 Size**: 1.1em → 1.3em
- **Feature P Size**: 0.9em → 1.1em
- **Mobile Container Padding**: 40px → 50px
- **Mobile H1 Size**: 2em → 2.5em

**Files Modified**:
- `templates/sizes.html`
- `static/css/sizes.css`

**Elements Affected**:
- `.container` padding and max-width
- `h1` font-size
- `p` font-size
- `.button` padding and font-size
- `.feature-icon` font-size
- `.feature h3` font-size
- `.feature p` font-size
- Mobile responsive sizes

---

### 3. Spacing Variation (`/spacing`)
**What Changed**: Only margins and gaps between elements
- **H1 Margin-bottom**: 20px → 40px
- **Paragraph Margin-bottom**: 30px → 50px
- **Features Margin-top**: 40px → 60px
- **Features Gap**: 20px → 40px
- **Feature Icon Margin-bottom**: 10px → 20px
- **Feature H3 Margin-bottom**: 8px → 15px
- **Mobile Features Gap**: 15px → 25px

**Files Modified**:
- `templates/spacing.html`
- `static/css/spacing.css`

**Elements Affected**:
- `h1` margin-bottom
- `p` margin-bottom
- `.features` margin-top and gap
- `.feature-icon` margin-bottom
- `.feature h3` margin-bottom
- Mobile responsive gaps

---

### 4. Typography Variation (`/typography`)
**What Changed**: Only font families, weights, and text styling
- **Body Font**: System fonts → Georgia serif
- **H1 Font Weight**: normal → bold
- **H1 Letter Spacing**: none → 1px
- **Paragraph Font Weight**: normal → 300 (light)
- **Button Font Weight**: 600 → 700 (bold)
- **Button Text Transform**: none → uppercase
- **Button Letter Spacing**: none → 1px
- **Feature H3 Font Weight**: normal → 600 (semi-bold)
- **Feature H3 Letter Spacing**: none → 0.5px
- **Feature P Font Weight**: normal → 400
- **Feature P Font Style**: normal → italic

**Files Modified**:
- `templates/typography.html`
- `static/css/typography.css`

**Elements Affected**:
- `body` font-family
- `h1` font-weight and letter-spacing
- `p` font-weight
- `.button` font-weight, text-transform, and letter-spacing
- `.feature h3` font-weight and letter-spacing
- `.feature p` font-weight and font-style

---

## Technical Implementation

### File Structure
```
calhacks12/
├── app.py                    # Flask routes
├── templates/
│   ├── index.html           # Original template
│   ├── colors.html          # Color variation
│   ├── sizes.html           # Size variation
│   ├── spacing.html         # Spacing variation
│   └── typography.html      # Typography variation
└── static/css/
    ├── style.css            # Original styles
    ├── colors.css           # Color variation styles
    ├── sizes.css            # Size variation styles
    ├── spacing.css          # Spacing variation styles
    └── typography.css       # Typography variation styles
```

### Flask Routes
```python
@app.route('/')              # Original
@app.route('/colors')         # Color variation
@app.route('/sizes')          # Size variation
@app.route('/spacing')        # Spacing variation
@app.route('/typography')     # Typography variation
```

### CSS Documentation Pattern
Each variation CSS file includes:
- Comments marking exactly what changed
- Original values preserved in comments
- Only the specific properties that differ from the base template

## Usage
1. Run the Flask application: `python app.py`
2. Navigate between variations using the navigation bar
3. Compare each variation to see the isolated changes
4. Use the CSS comments to understand exactly what was modified

## Design Philosophy
Each variation demonstrates how **single design decisions** can impact the overall user experience while maintaining the core structure and functionality of the original design.
